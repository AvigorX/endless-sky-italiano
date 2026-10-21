r"""verify.py — L51 (data/avgi/avgi 0 first contact.txt, 152 unita', righe 413-869)

Segmento **interno**: 119 unita' prima (L50) e 135 dopo la 869. La copertura del file NON e' un
invariante di questo lotto: si asserisce la copertura del **segmento** (per righe) e il numero di unita'
prima e dopo.

**Nessuna unita' non traducibile**: 0 `UI_LABEL`, 0 riferimenti di dato. Il controllo e' quindi
un'asserzione di **assenza**, esplicita — non un elenco vuoto lasciato passare.

Controlli indipendenti da check.py, senza riusarne la logica:

  1. la riga grezza di ogni unita' coincide con quella del file sorgente
  2. english / kind / path / context coincidono con state.db, e lo stato e' PENDING
  3. nessuna unita' del lotto risulta APPROVED
  4. id univoci e ordine = ordine del sorgente
  5. collocazione: 152 unita', righe 413-869
  6. **119 unita' prima della 413 (L50), 135 dopo la 869** (file di 406, max line 1120)
  7. copertura del segmento: le righe [413, 869] sono coperte senza buchi
  8. distribuzione dei kind misurata: 126/10/6/5/5
  9. **`NT` vuoto**: 0 `UI_LABEL` e 0 riferimenti di dato (assenza dichiarata)
 10. **`LOGBOOK` 10**: 6 a tre argomenti, 4 fra backtick, 0 dirette; nessuna categoria estratta
 11. **`DIALOG` 6** (43, 60, 119, 132, 143, 152); **`TEXT` 0**, **`CONVERSATION` 0** (assenze)
 12. **0 virgolette dispari, 0 quadre, 0 backtick**: assenze dichiarate
 13. tab 113 e virgolette 252: parita' sui totali e **per unita'**
 14. token: parita' esatta (32 occorrenze, 7 famiglie)
 15. nessuna unita' con italiano vuoto; tipografia (accenti, apostrofi, dash)
 16. rapporto lunghezze dentro il gate 0,55-1,90
 17. duplicati inglesi (6 gruppi, 12 unita'): resa italiana identica per unita' con inglese identico
 18. le parti su disco ricostruiscono translation.json (tab del costruttore compresi)
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
PATH = 'data/avgi/avgi 0 first contact.txt'
SRC = os.path.join(ROOT, 'endless-sky', *PATH.split('/'))

source = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
trans = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))
su, tu = source['units'], trans['units']
lines = open(SRC, encoding='utf-8').read().split('\n')

NT = set()
LOG = (4, 47, 48, 49, 61, 62, 63, 64, 118, 142)
DIALOG = (43, 60, 119, 132, 143, 152)
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
   len(tu) == 152 and (first, last) == (413, 869), (len(tu), first, last))

tot = db.execute('select count(*) from units where path = ?', (PATH,)).fetchone()[0]
before = db.execute('select count(*) from units where path = ? and line < ?',
                    (PATH, first)).fetchone()[0]
after = db.execute('select count(*) from units where path = ? and line > ?',
                   (PATH, last)).fetchone()[0]
maxline = db.execute('select max(line) from units where path = ?', (PATH,)).fetchone()[0]
ck('segmento interno: 119 prima della 413, 135 dopo la 869',
   before == 119 and after == 135 and tot == 406, (before, after, tot, maxline))

lrows = sorted(u['line'] for u in su)
buchi = [x for i, x in enumerate(lrows) if i and lrows[i - 1] >= x]
ck('righe del segmento crescenti e senza ripetizioni', not buchi, buchi[:5])
ck('copertura del segmento: righe 413-869 continue',
   lrows[0] == 413 and lrows[-1] == 869 and buchi == [], (lrows[0], lrows[-1]))
dupl_lines = db.execute('select count(*) from units where path = ? and line between ? and ?',
                        (PATH, first, last)).fetchone()[0]
ck('nessun altra unita nel DB dentro 413-869 (%d)' % dupl_lines, dupl_lines == len(tu), dupl_lines)

kinds = collections.Counter(u['kind'] for u in su)
atteso = {'MISSION_TEXT': 126, 'LOGBOOK': 10, 'DIALOG': 6, 'VALUE': 5, 'DESCRIPTION': 5}
ck('distribuzione dei kind come misurata', dict(kinds) == atteso, dict(kinds))

by_idx = {u['idx']: u for u in tu}
ui = sorted(u['idx'] for u in tu if u['kind'] == 'UI_LABEL')
ck('NT vuoto: 0 UI_LABEL nel segmento (assenza dichiarata)', ui == [] and NT == set(), ui)
ck('nessuna unita del segmento e non traducibile per dichiarazione',
   not [i for i in NT if i in by_idx], sorted(NT))

log_it = tuple(u['idx'] for u in tu if u['kind'] == 'LOGBOOK')
ck('LOGBOOK: %d righe nel lotto, %d attese' % (len(log_it), len(LOG)), log_it == LOG, log_it)
ck('LOGBOOK: nessuna riga lasciata identica all\'inglese',
   not [i for i in LOG if by_idx[i]['italian'].strip() == by_idx[i]['english'].strip()],
   [i for i in LOG if by_idx[i]['italian'].strip() == by_idx[i]['english'].strip()])
ck('LOGBOOK: tab del sorgente conservati',
   not [i for i in LOG if by_idx[i]['italian'].count('\t') != by_idx[i]['english'].count('\t')])
raw_by_idx = {u['idx']: u['raw'] for u in su}
f_three = tuple(i for i in LOG if re.match(r'\t+log "[^"]+" "[^"]+" `', raw_by_idx[i]))
f_back = tuple(i for i in LOG if re.match(r'\t+log `', raw_by_idx[i]))
f_quote = tuple(i for i in LOG if re.match(r'\t+log "[^"]+"\s*$', raw_by_idx[i]))
ck('LOGBOOK: forme 6 tre argomenti + 4 backtick + 0 dirette',
   (f_three, f_back, f_quote) == ((4, 48, 49, 62, 63, 64), (47, 61, 118, 142), ()),
   (f_three, f_back, f_quote))
ck('LOGBOOK: nessuna categoria estratta (a differenza di L45-L47)',
   not [i for i in LOG if re.match(r'\t+log "[^"]+" "[^"]+"\s*$', raw_by_idx[i])])

dlg = tuple(u['idx'] for u in tu if u['kind'] == 'DIALOG')
ck('DIALOG: %d nodi, controllo positivo' % len(DIALOG), dlg == DIALOG, dlg)
ck('DIALOG: tutti con testo fra backtick e tradotti',
   all(re.match(r'\t+dialog `.+`$', raw_by_idx[i]) for i in DIALOG)
   and not [i for i in DIALOG if by_idx[i]['italian'].strip() == by_idx[i]['english'].strip()])
txt = tuple(u['idx'] for u in tu if u['kind'] == 'TEXT')
ck('TEXT: 0 unita nel segmento (assenza dichiarata)', txt == (), txt)
ck('nessun contesto phrase nel segmento',
   not [u for u in su if u['context'].startswith('phrase:')])
conv = [u for u in tu if u['kind'] == 'CONVERSATION']
ck('CONVERSATION: nessuna nel segmento (assenza dichiarata)', conv == [], conv)
br = [u['idx'] for u in su if '[' in u['english'] or ']' in u['english']]
ck('quadre: nessuna unita con [ o ] nel sorgente (assenza dichiarata)', br == [], br[:5])
pair = [u['idx'] for u in tu if '[' in u['italian'] or ']' in u['italian']]
ck('quadre: nessuna quadra nell\'italiano', pair == [], pair)
bt = [u['idx'] for u in tu if '`' in u['italian']]
ck('backtick: nessuno nell\'italiano (assenza dichiarata)', bt == [], bt)

diff = [u['idx'] for u in tu
        if collections.Counter(TAGS.findall(u['english'])) != collections.Counter(TAGS.findall(u['italian']))]
ck('nessuna unita con token diversi (parita esatta)', not diff, sorted(set(diff))[:10])
tot_en = sum(len(TAGS.findall(u['english'])) for u in su)
tot_it = sum(len(TAGS.findall(u['italian'])) for u in tu)
fam = collections.Counter(t for u in su for t in TAGS.findall(u['english']))
ck('token totali %d = %d (7 famiglie)' % (tot_it, tot_en), tot_en == tot_it and len(fam) == 7,
   (tot_it, tot_en, len(fam)))

for ch, nome in (('\t', 'tab'), ('"', 'virgolette')):
    a = sum(u['english'].count(ch) for u in su)
    b = sum(u['italian'].count(ch) for u in tu)
    ck('%s totali %d = %d' % (nome, b, a), a == b)

per_unit = [u['idx'] for u in tu if u['english'].count('\t') != u['italian'].count('\t')
            or u['english'].count('"') != u['italian'].count('"')]
ck('tab e virgolette: parita per unita (152 unita)', per_unit == [], per_unit[:10])
lead = [u['idx'] for u in tu if u['english'].startswith('\t') != u['italian'].startswith('\t')]
ntab = len([u for u in tu if u['italian'].startswith('\t')])
ck('tab iniziale presente dove il sorgente lo ha (113)', ntab == 113 and lead == [], (ntab, lead[:5]))

odd_en = sorted(u['idx'] for u in su if u['english'].count('"') % 2)
odd_it = sorted(u['idx'] for u in tu if u['italian'].count('"') % 2)
ck('virgolette dispari: nessuna nel lotto (assenza dichiarata)', odd_en == [] and odd_it == [],
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
print('FAIL:', len(fail), '·', 'verify L51 superato' if not fail else 'verify L51 fallito')
raise SystemExit(0 if not fail else 1)
