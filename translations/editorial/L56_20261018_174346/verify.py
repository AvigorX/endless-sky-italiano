r"""verify.py — L56 (data/gegno/gegno I corroboration.txt, 171 unita', righe 29-904)

Il lotto **apre il file** (0 unita' prima della 29) e lo lascia aperto: **127 unita' dopo** la 904
(file di 298, `max(line) = 1287`). La copertura del file NON e' un invariante qui.

Differenze rispetto a L55, tutte asserite:
  - `NT` = **28** `UI_LABEL` (il numero piu' alto della serie), tutte identiche al sorgente;
  - **`DIALOG` 3** (62, 170, 171): 170 e 171 sono **identiche** nel sorgente (stessa scena per due esiti);
  - **`LOGBOOK` 0**, **`CONVERSATION` 0**, **`TEXT` 0**: assenze dichiarate;
  - **12 token in 5 famiglie**: parita' esatta per unita'.

Controlli indipendenti da check.py, senza riusarne la logica:

  1. la riga grezza di ogni unita' coincide con quella del file sorgente
  2. english / kind / path / context coincidono con state.db, e lo stato e' PENDING
  3. nessuna unita' del lotto risulta APPROVED
  4. id univoci e ordine = ordine del sorgente
  5. collocazione: 171 unita', righe 29-904
  6. **apre il file**: 0 prima, **127 dopo**, 298 totali, `max(line) = 1287`
  7. copertura del segmento: righe [29, 904] senza buchi
  8. distribuzione dei kind misurata: 137/28/3/2/1
  9. `NT`: 28 label identiche al sorgente, tutte `label "…"`
 10. `DIALOG` 3 con 170 == 171 in inglese e in italiano; `LOGBOOK`/`CONVERSATION`/`TEXT` 0
 11. **12 token in 5 famiglie**: parita' esatta (multiset, maiuscole comprese)
 12. `label` identiche: nessuna tradotta
 13. tab 129 e virgolette 238: parita' sui totali e per unita'
 14. nessuna unita' con italiano vuoto; tipografia (accenti, apostrofi, dash)
 15. rapporto lunghezze dentro il gate 0,55-1,90
 16. duplicati inglesi (10 gruppi, 30 unita'): resa italiana identica
 17. le parti su disco ricostruiscono translation.json (tab del costruttore compresi)
"""
import collections
import glob
import hashlib
import json
import os
import re
import sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
ROOT = os.path.abspath(os.path.join(L10N, '..'))
PATH = 'data/gegno/gegno I corroboration.txt'
SRC = os.path.join(ROOT, 'endless-sky', *PATH.split('/'))

source = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
trans = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))
su, tu = source['units'], trans['units']
lines = open(SRC, encoding='utf-8').read().split('\n')

NT = set([24, 26, 49, 77, 81, 89, 93, 100, 102, 104, 106, 108, 114, 116, 120, 122, 124,
          126, 139, 143, 147, 151, 155, 157, 159, 161, 166, 168])
DIALOG = (62, 170, 171)
TAGS = re.compile(r'<[^<>]+>')

fail = []


def ck(name, cond, detail=''):
    print('%-58s %s %s' % (name, 'OK' if cond else 'FAIL', '' if cond else detail))
    if not cond:
        fail.append(name)


bad_raw = [u['idx'] for u in su if lines[u['line'] - 1] != u['raw']]
ck('riga grezza identica al file sorgente', not bad_raw, bad_raw[:10])

db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
db.row_factory = sqlite3.Row
bad_db, bad_state, approved = [], [], []
for u in su:
    row = db.execute('select english, kind, path, context, state from units where id = ?',
                     (u['id'],)).fetchone()
    if row is None or row['english'] != u['english'] or row['kind'] != u['kind'] \
            or row['path'] != u['path'] or row['context'] != u['context']:
        bad_db.append(u['idx'])
    elif row['state'] == 'APPROVED':
        approved.append(u['idx'])
    elif row['state'] != 'PENDING':
        bad_state.append((u['idx'], row['state']))
ck('english/kind/path/context identici al DB', not bad_db, bad_db[:10])
ck('state = PENDING per tutte le unita', not bad_state, bad_state[:10])
ck('nessuna unita del lotto e APPROVED nel DB', not approved, approved[:10])

ids = [u['id'] for u in tu]
ck('id univoci in translation.json', len(ids) == len(set(ids)))
ck('ordine delle unita = ordine del sorgente', [u['idx'] for u in tu] == [u['idx'] for u in su])
ck('stesse unita in source.json e translation.json',
   len(tu) == len(su) and [u['idx'] for u in tu] == [u['idx'] for u in su])

first, last = tu[0]['line'], tu[-1]['line']
ck('unita: %d righe %d - %d' % (len(tu), first, last),
   len(tu) == 171 and (first, last) == (29, 904), (len(tu), first, last))

tot = db.execute('select count(*) from units where path = ?', (PATH,)).fetchone()[0]
before = db.execute('select count(*) from units where path = ? and line < ?',
                    (PATH, first)).fetchone()[0]
after = db.execute('select count(*) from units where path = ? and line > ?',
                   (PATH, last)).fetchone()[0]
maxline = db.execute('select max(line) from units where path = ?', (PATH,)).fetchone()[0]
ck('apre il file: 0 prima della 29, 127 dopo la 904',
   before == 0 and after == 127 and tot == 298, (before, after, tot, maxline))
ck('max(line) del file = 1287', maxline == 1287, maxline)

lrows = sorted(u['line'] for u in su)
buchi = [x for i, x in enumerate(lrows) if i and lrows[i - 1] >= x]
ck('copertura del segmento: righe 29-904 continue',
   lrows[0] == 29 and lrows[-1] == 904 and buchi == [], (lrows[0], lrows[-1]))
dupl_lines = db.execute('select count(*) from units where path = ? and line between ? and ?',
                        (PATH, first, last)).fetchone()[0]
ck('nessun altra unita nel DB dentro 29-904 (%d)' % dupl_lines, dupl_lines == len(tu), dupl_lines)

kinds = collections.Counter(u['kind'] for u in su)
atteso = {'MISSION_TEXT': 137, 'UI_LABEL': 28, 'DIALOG': 3, 'DESCRIPTION': 2, 'VALUE': 1}
ck('distribuzione dei kind come misurata', dict(kinds) == atteso, dict(kinds))

by_idx = {u['idx']: u for u in tu}
raw_by_idx = {u['idx']: u['raw'] for u in su}
ui = sorted(u['idx'] for u in tu if u['kind'] == 'UI_LABEL')
ck('UI_LABEL: 28 attese, tutte elencate', ui == sorted(NT), ui)
notid = [i for i in NT if by_idx[i]['italian'] != by_idx[i]['english']]
ck('NT: tutte le 28 label identiche al sorgente', not notid, notid)
ck('NT: tutte sono label di salto, nessun riferimento di dato',
   all(re.match(r'\t+label "', raw_by_idx[i]) for i in NT))

dlg = tuple(u['idx'] for u in tu if u['kind'] == 'DIALOG')
ck('DIALOG: 3 unita (62, 170, 171)', dlg == DIALOG, dlg)
ck('DIALOG: 170 e 171 sono identiche nel sorgente',
   by_idx[170]['english'] == by_idx[171]['english'])
ck('DIALOG: 170 e 171 sono identiche anche in italiano',
   by_idx[170]['italian'] == by_idx[171]['italian'])
ck('DIALOG: tutti tradotti e non lasciati in inglese',
   not [i for i in DIALOG if by_idx[i]['italian'].strip() == by_idx[i]['english'].strip()])

for kind in ('LOGBOOK', 'CONVERSATION', 'TEXT'):
    got = [u['idx'] for u in tu if u['kind'] == kind]
    ck('%s: nessuna unita nel segmento (assenza dichiarata)' % kind, got == [], got)

diff = [u['idx'] for u in tu
        if collections.Counter(TAGS.findall(u['english'])) != collections.Counter(TAGS.findall(u['italian']))]
ck('nessuna unita con token diversi (parita esatta)', not diff, sorted(set(diff))[:10])
tot_en = sum(len(TAGS.findall(u['english'])) for u in su)
tot_it = sum(len(TAGS.findall(u['italian'])) for u in tu)
fam = collections.Counter(t for u in su for t in TAGS.findall(u['english']))
ck('token totali %d = %d (5 famiglie)' % (tot_it, tot_en), tot_en == tot_it and len(fam) == 5,
   (tot_it, tot_en, len(fam)))

for ch, nome in (('\t', 'tab'), ('"', 'virgolette')):
    a = sum(u['english'].count(ch) for u in su)
    b = sum(u['italian'].count(ch) for u in tu)
    ck('%s totali %d = %d' % (nome, b, a), a == b)

per_unit = [u['idx'] for u in tu if u['english'].count('\t') != u['italian'].count('\t')
            or u['english'].count('"') != u['italian'].count('"')]
ck('tab e virgolette: parita per unita (171 unita)', per_unit == [], per_unit[:10])
lead = [u['idx'] for u in tu if u['english'].startswith('\t') != u['italian'].startswith('\t')]
ntab = len([u for u in tu if u['italian'].startswith('\t')])
ck('tab iniziale presente dove il sorgente lo ha (129)', ntab == 129 and lead == [], (ntab, lead[:5]))

odd_en = tuple(sorted(u['idx'] for u in su if u['english'].count('"') % 2))
odd_it = tuple(sorted(u['idx'] for u in tu if u['italian'].count('"') % 2))
ck('virgolette dispari: nessuna nel lotto (assenza dichiarata)', odd_en == () and odd_it == (),
   (odd_en, odd_it))

ck('nessuna unita con italiano vuoto', all(u['italian'].strip() for u in tu))
NONLAT = re.compile(r'[^\x00-\x7F\u00C0-\u024F\u2018\u2019\u201C\u201D\u2013\u2014\u2026]')
sus = [(u['idx'], NONLAT.findall(u['italian'])[:3]) for u in tu if NONLAT.search(u['italian'])]
ck('nessun carattere non latino sospetto', not sus, sus[:10])

dash = [u['idx'] for u in tu if '\u2014' in u['italian'] or '\u2013' in u['italian']]
ck('nessun trattino lungo/en-dash (vietati)', not dash, dash[:10])
curly = [u['idx'] for u in tu if '\u2018' in u['italian'] or '\u2019' in u['italian']
         or '\u201C' in u['italian'] or '\u201D' in u['italian']]
ck('nessuna virgoletta curva (apostrofo dritto)', not curly, curly[:10])
apos = [u['idx'] for u in tu if re.search(r"\b(e|piu|perche|cosi|gia|puo|citta|verita|entita)'", u['italian'])]
ck('nessun accento sostitutivo con apostrofo', not apos, apos[:10])

bad_ratio = [u['idx'] for u in tu if u['ratio'] is None]
ck('rapporto lunghezze definito per tutte le unita', not bad_ratio, bad_ratio[:10])
rs = [u['ratio'] for u in tu if u['ratio'] is not None]
ck('rapporto dentro il gate 0,55-1,90', 0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
print('rapporto IT/EN: min %.2f max %.2f' % (min(rs), max(rs)))

merged = {}
for f in sorted(glob.glob(os.path.join(HERE, 'parts', 'part*.json'))):
    for k, v in json.load(open(f, encoding='utf-8')).items():
        merged[int(k)] = v
en_by_idx = {u['idx']: u['english'] for u in su}
rebuilt = {i: '\t' * (len(en_by_idx[i]) - len(en_by_idx[i].lstrip('\t'))) + v
           for i, v in merged.items()}
ck('le parti su disco ricostruiscono translation.json (tab compresi)',
   rebuilt == {u['idx']: u['italian'] for u in tu})

dup_en = [e for e, n in collections.Counter(u['english'] for u in su).items() if n > 1]
dup_ok = all(len(set(by_idx[u['idx']]['italian'] for u in su if u['english'] == e)) == 1
             for e in dup_en)
ck('duplicati inglesi (%d gruppi): resa italiana identica' % len(dup_en), dup_ok)
nondup = [u['idx'] for u in tu if u['english'] not in dup_en]
seen = collections.Counter(by_idx[i]['italian'] for i in nondup)
ck('nessuna resa italiana ripetuta fra unita con inglese diverso',
   not [k[:40] for k, n in seen.items() if n > 1],
   [k[:40] for k, n in seen.items() if n > 1])

h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
en_w = sum(len(u['english'].split()) for u in tu)
it_w = sum(len(u['italian'].split()) for u in tu)
print('parole EN %d -> IT %d · traduzione sha256[:16] %s' % (en_w, it_w, h[:16]))

print()
print('FAIL:', len(fail), '·', 'verify L56 superato' if not fail else 'verify L56 fallito')
raise SystemExit(0 if not fail else 1)
