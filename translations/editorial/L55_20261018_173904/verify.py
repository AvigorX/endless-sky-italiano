r"""verify.py — L55 (data/gegno/gegno intro missions.txt, 28 unita', righe 677-954)

**L55 chiude il file**: 89 (L53) + 159 (L54) + 28 (L55) = **276/276**, `max(line) = 954`, **0 dopo**.
Come per L52, l'invariante «di file» e' legittimo **solo perche'** la 954 e' l'ultima riga: le tre
condizioni sono asserite insieme.

Differenze rispetto a L54, tutte dichiarate:
  - `NT` = **4** `UI_LABEL` (12, 14, 16, 21);
  - **`CONVERSATION` 1** (unita' 28): **prima e unica** conversazione del file — controllo **positivo**;
  - `LOGBOOK` 0, `DIALOG` 0, `TEXT` 0: assenze dichiarate;
  - **0 token**, **0 quadre**, **0 backtick**, **0 virgolette dispari**.

Controlli indipendenti da check.py, senza riusarne la logica:

  1. la riga grezza di ogni unita' coincide con quella del file sorgente
  2. english / kind / path / context coincidono con state.db, e lo stato e' PENDING
  3. nessuna unita' del lotto risulta APPROVED
  4. id univoci e ordine = ordine del sorgente
  5. collocazione: 28 unita', righe 706-954
  6. **chiude il file**: 248 prima, **0 dopo**, 276 totali, `max(line) = 954`
  7. copertura del **file** 276/276 su **tre lotti** (L53 89 + L54 159 + L55 28), senza sovrapposizioni
  8. distribuzione dei kind misurata: 21/4/1/1/1
  9. `NT`: 4 label identiche al sorgente, tutte `label "…"`
 10. **`CONVERSATION` 1** (28): controllo positivo; `LOGBOOK`/`DIALOG`/`TEXT` 0 (assenze)
 11. **0 token**, **0 quadre**, **0 backtick**, **0 virgolette dispari**: assenze dichiarate
 12. tab 14 e virgolette 34: parita' sui totali e per unita'
 13. nessuna unita' con italiano vuoto; tipografia (accenti, apostrofi, dash)
 14. rapporto lunghezze dentro il gate 0,55-1,90
 15. duplicati inglesi (se ce ne sono): resa italiana identica
 16. le parti su disco ricostruiscono translation.json (tab del costruttore compresi)
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
PATH = 'data/gegno/gegno intro missions.txt'
SRC = os.path.join(ROOT, 'endless-sky', *PATH.split('/'))

source = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
trans = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))
su, tu = source['units'], trans['units']
lines = open(SRC, encoding='utf-8').read().split('\n')

NT = set([12, 14, 16, 21])
CONV = (28,)
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
   len(tu) == 28 and (first, last) == (706, 954), (len(tu), first, last))

tot = db.execute('select count(*) from units where path = ?', (PATH,)).fetchone()[0]
before = db.execute('select count(*) from units where path = ? and line < ?',
                    (PATH, first)).fetchone()[0]
after = db.execute('select count(*) from units where path = ? and line > ?',
                   (PATH, last)).fetchone()[0]
maxline = db.execute('select max(line) from units where path = ?', (PATH,)).fetchone()[0]
ck('chiude il file: 248 prima della 706, 0 dopo la 954',
   before == 248 and after == 0 and tot == 276, (before, after, tot, maxline))
ck('max(line) del file = 954', maxline == 954, maxline)

lotti = []
for name in sorted(os.listdir(os.path.join(L10N, 'staging', 'editorial'))):
    f = os.path.join(L10N, 'staging', 'editorial', name, 'translation.json')
    if not os.path.exists(f):
        continue
    d = json.load(open(f, encoding='utf-8'))['units']
    if d and d[0]['path'] == PATH:
        lotti.append((name.split('_')[0], set(u['id'] for u in d)))
sovrapposti = sum(len(a & b) for i, (_, a) in enumerate(lotti) for _, b in lotti[i + 1:])
ck('copertura del file %d / %d (tre lotti)' % (sum(len(s) for _, s in lotti), tot),
   tot == 276 and sum(len(s) for _, s in lotti) == tot, (sum(len(s) for _, s in lotti), tot))
ck('tre lotti (89 + 159 + 28), nessuna unita duplicata',
   sorted((lab, len(s)) for lab, s in lotti) == [('L53', 89), ('L54', 159), ('L55', 28)]
   and sovrapposti == 0,
   ([(lab, len(s)) for lab, s in lotti], sovrapposti))

kinds = collections.Counter(u['kind'] for u in su)
atteso = {'MISSION_TEXT': 21, 'UI_LABEL': 4, 'VALUE': 1, 'DESCRIPTION': 1, 'CONVERSATION': 1}
ck('distribuzione dei kind come misurata', dict(kinds) == atteso, dict(kinds))

by_idx = {u['idx']: u for u in tu}
raw_by_idx = {u['idx']: u['raw'] for u in su}
ui = sorted(u['idx'] for u in tu if u['kind'] == 'UI_LABEL')
ck('UI_LABEL: 4 attese, tutte elencate', ui == sorted(NT), ui)
notid = [i for i in NT if by_idx[i]['italian'] != by_idx[i]['english']]
ck('NT: tutte le 4 label identiche al sorgente', not notid, notid)
ck('NT: tutte sono label di salto, nessun riferimento di dato',
   all(re.match(r'\t+label "', raw_by_idx[i]) for i in NT))

conv = tuple(u['idx'] for u in tu if u['kind'] == 'CONVERSATION')
ck('CONVERSATION: 1 unita (28), controllo positivo', conv == CONV, conv)
ck('CONVERSATION: contesto conversation: registrato nel sorgente',
   source['units'][27]['context'].startswith('conversation:'))
ck('CONVERSATION: tradotta e non lasciata in inglese',
   by_idx[28]['italian'].strip() != by_idx[28]['english'].strip())

for kind in ('LOGBOOK', 'DIALOG', 'TEXT'):
    got = [u['idx'] for u in tu if u['kind'] == kind]
    ck('%s: nessuna unita nel segmento (assenza dichiarata)' % kind, got == [], got)

n_tok = sum(len(TAGS.findall(u['english'])) for u in su)
ck('token: nessuno nel sorgente (assenza dichiarata)', n_tok == 0, n_tok)
br = [u['idx'] for u in su if '[' in u['english'] or ']' in u['english']]
ck('quadre: nessuna nel sorgente (assenza dichiarata)', br == [], br[:5])
bt = [u['idx'] for u in tu if '`' in u['italian']]
ck('backtick: nessuno nell\'italiano (assenza dichiarata)', bt == [], bt)

for ch, nome in (('\t', 'tab'), ('"', 'virgolette')):
    a = sum(u['english'].count(ch) for u in su)
    b = sum(u['italian'].count(ch) for u in tu)
    ck('%s totali %d = %d' % (nome, b, a), a == b)

per_unit = [u['idx'] for u in tu if u['english'].count('\t') != u['italian'].count('\t')
            or u['english'].count('"') != u['italian'].count('"')]
ck('tab e virgolette: parita per unita (28 unita)', per_unit == [], per_unit[:10])
lead = [u['idx'] for u in tu if u['english'].startswith('\t') != u['italian'].startswith('\t')]
ntab = len([u for u in tu if u['italian'].startswith('\t')])
ck('tab iniziale presente dove il sorgente lo ha (14)', ntab == 14 and lead == [], (ntab, lead[:5]))

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
ck('duplicati inglesi (%d gruppi): resa italiana identica' % len(dup_en),
   all(len(set(by_idx[u['idx']]['italian'] for u in su if u['english'] == e)) == 1 for e in dup_en),
   dup_en)
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
print('FAIL:', len(fail), '·', 'verify L55 superato' if not fail else 'verify L55 fallito')
raise SystemExit(0 if not fail else 1)
