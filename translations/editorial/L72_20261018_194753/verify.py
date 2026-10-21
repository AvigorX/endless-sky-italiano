r"""verify.py — L72 (data/successors/successor 2 ghosts myurej.txt, 50 unita', righe 402-531)

Verifica **indipendente** da `check.py`.

**Chiude il file**: L68 (49) + L69 (31) + L70 (39) + L71 (42) + L72 (50) = **211/211**, `max(line) = 531`,
**0 unita' dopo**. Qui l'invariante «di file» torna legittimo (decisione 181) ed e' asserito insieme:
chiusura, `max(line)` e copertura 211/211.

Misure attese, lette dal workspace il 2026-10-18:
  - 50 unita', righe 407-531, **3 contesti** (`Myurej 6`, `7`, `8`);
  - tipi: 40 `MISSION_TEXT`, 3 `VALUE`, 3 `DESCRIPTION`, 2 `DIALOG`, 2 `LOGBOOK`; 0 `UI_LABEL`;
  - **`DIALOG` 2** (unita' 3 e 4): testo, non etichette; **`LOGBOOK` 2** (5 e 30), forma diretta;
  - **18 token** in 8 famiglie: `<planet>` 5, `<last>` 3, `<ship>` 2, `<destination>` 2, `<origin>` 2,
    `<tons>` 2, `<payment>` 1, `<first>` 1;
  - **36 tab su 36 unita'**, **96 virgolette**, 0 dispari, 0 quadre, 0 backtick;
  - **0 gruppi** di duplicati inglesi.
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
PATH = 'data/successors/successor 2 ghosts myurej.txt'
SRC = os.path.join(ROOT, 'endless-sky', *PATH.split('/'))

source = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
trans = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))
su, tu = source['units'], trans['units']
lines = open(SRC, encoding='utf-8').read().split('\n')

NT = set()
LOG = {5, 30}
DIALOG = {3, 4}
TAGS = re.compile(r'<[^<>]+>')

fail = []


def ck(name, cond, detail=''):
    print('%-64s %s %s' % (name, 'OK' if cond else 'FAIL', '' if cond else detail))
    if not cond:
        fail.append(name)


bad_raw = [u['idx'] for u in su if lines[u['line'] - 1] != u['raw']]
ck('riga grezza identica al file sorgente (50 righe)', not bad_raw, bad_raw[:10])

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
ck('idx del segmento senza buchi (1..50)', [u['idx'] for u in tu] == list(range(1, 51)))

first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 50 righe 407 - 531', len(tu) == 50 and (first, last) == (407, 531), (len(tu), first, last))

tot = db.execute('select count(*) from units where path = ?', (PATH,)).fetchone()[0]
before = db.execute('select count(*) from units where path = ? and line < ?', (PATH, first)).fetchone()[0]
after = db.execute('select count(*) from units where path = ? and line > ?', (PATH, last)).fetchone()[0]
maxline = db.execute('select max(line) from units where path = ?', (PATH,)).fetchone()[0]
ck('eredita L68-L71: 161 unita prima della riga 407', before == 161, before)
ck('CHIUDE il file: 0 unita dopo la riga 531', after == 0, after)
ck('file: 211 unita totali, max(line) = 531', tot == 211 and maxline == 531, (tot, maxline))
infile = db.execute('select count(*) from units where path = ? and line <= ?', (PATH, last)).fetchone()[0]
ck('copertura del file 211/211 (%d)' % infile, infile == 211 == len(tu) + before, infile)

lrows = sorted(u['line'] for u in su)
ck('segmento 407-531: prima/ultima riga coerenti', lrows[0] == 407 and lrows[-1] == 531, (lrows[0], lrows[-1]))
ck('nessuna riga del segmento con due unita (50 righe distinte)', len(set(lrows)) == 50 == len(lrows))
inrange = db.execute('select count(*) from units where path = ? and line between ? and ?',
                     (PATH, first, last)).fetchone()[0]
ck('nessun altra unita nel DB dentro 407-531 (%d)' % inrange, inrange == len(tu), inrange)
ctxs = []
for u in su:
    if u['context'] not in ctxs:
        ctxs.append(u['context'])
ck('3 contesti, in ordine di riga',
   ctxs == ['mission:Successors: Ghosts Myurej 6', 'mission:Successors: Ghosts Myurej 7',
            'mission:Successors: Ghosts Myurej 8'], ctxs)

kinds = collections.Counter(u['kind'] for u in su)
ck('kind: 40 MISSION_TEXT, 3 VALUE, 3 DESCRIPTION, 2 DIALOG, 2 LOGBOOK',
   dict(kinds) == {'MISSION_TEXT': 40, 'VALUE': 3, 'DESCRIPTION': 3, 'DIALOG': 2, 'LOGBOOK': 2},
   dict(kinds))

by_idx = {u['idx']: u for u in tu}
ui = sorted(u['idx'] for u in su if u['kind'] == 'UI_LABEL')
ck('UI_LABEL: nessuna nel segmento (assenza dichiarata)', ui == [] and NT == set(), ui)
raw_by_idx = {u['idx']: u['raw'] for u in su}
ck('nessun riferimento di dato nel `raw` del lotto',
   [i for i, r in raw_by_idx.items() if re.match(r'\t*(government|scene|thumbnail)\b', r)] == [])
log_units = sorted(u['idx'] for u in tu if u['kind'] == 'LOGBOOK')
ck('LOGBOOK: 2 unita (5, 30)', log_units == sorted(LOG), log_units)
ck('i due LOGBOOK sono tradotti e distinti',
   all(by_idx[i]['italian'].strip() != by_idx[i]['english'].strip() for i in LOG)
   and by_idx[5]['italian'] != by_idx[30]['italian'])
dlg = sorted(u['idx'] for u in tu if u['kind'] == 'DIALOG')
ck('DIALOG: 2 unita (3, 4), primi del file', dlg == sorted(DIALOG), dlg)
ck('DIALOG sono testo tradotto, non etichette',
   all(by_idx[i]['italian'].strip() != by_idx[i]['english'].strip() for i in DIALOG))
for kind in ('CONVERSATION', 'TEXT'):
    got = [u['idx'] for u in tu if u['kind'] == kind]
    ck('%s: nessuna unita nel segmento (assenza dichiarata)' % kind, got == [], got)
vd = sorted(u['idx'] for u in su if u['kind'] in ('VALUE', 'DESCRIPTION'))
ck('VALUE e DESCRIPTION: 3 + 3 presenti e tradotti', len(vd) == 6, vd)

tok_en = sum(len(TAGS.findall(u['english'])) for u in su)
tok_it = sum(len(TAGS.findall(u['italian'])) for u in tu)
fam_en = collections.Counter(t for u in su for t in TAGS.findall(u['english']))
fam_it = collections.Counter(t for u in tu for t in TAGS.findall(u['italian']))
ck('token <...>: 18 in inglese e 18 in italiano, 8 famiglie (%s)' % dict(fam_en),
   tok_en == 18 and tok_it == 18 and fam_en == fam_it
   and fam_en == collections.Counter({'<planet>': 5, '<last>': 3, '<ship>': 2, '<destination>': 2,
                                      '<origin>': 2, '<tons>': 2, '<payment>': 1, '<first>': 1}),
   (tok_en, tok_it, dict(fam_en), dict(fam_it)))
diff = [u['idx'] for u in tu
        if collections.Counter(TAGS.findall(u['english'])) != collections.Counter(TAGS.findall(u['italian']))]
ck('nessuna unita con token diversi (parita per simbolo e per unita)', not diff, sorted(set(diff))[:10])

for ch, nome, atteso_n in (('\t', 'tab', 36), ('"', 'virgolette', 96)):
    a = sum(u['english'].count(ch) for u in su)
    b = sum(u['italian'].count(ch) for u in tu)
    ck('%s totali %d = %d (attese %d)' % (nome, b, a, atteso_n), a == b == atteso_n, (a, b))

per_unit = [u['idx'] for u in tu if u['english'].count('\t') != u['italian'].count('\t')
            or u['english'].count('"') != u['italian'].count('"')]
ck('tab e virgolette: parita per unita (50 unita)', per_unit == [], per_unit[:10])
ntab = len([u for u in tu if u['italian'].startswith('\t')])
lead = [u['idx'] for u in tu if u['english'].startswith('\t') != u['italian'].startswith('\t')]
ck('tab iniziale presente dove il sorgente lo ha (36 unita)', ntab == 36 and lead == [], (ntab, lead[:5]))
ck('14 unita senza tab iniziale (6 nome/descrizione, 2 DIALOG, 2 log, 4 testi non indentati)',
   len([u for u in tu if not u['italian'].startswith('\t')]) == 14,
   len([u for u in tu if not u['italian'].startswith('\t')]))

odd_en = tuple(sorted(u['idx'] for u in su if u['english'].count('"') % 2))
odd_it = tuple(sorted(u['idx'] for u in tu if u['italian'].count('"') % 2))
ck('virgolette dispari: nessuna nel lotto (assenza dichiarata)', odd_en == () and odd_it == (),
   (odd_en, odd_it))
brk = [u['idx'] for u in tu if u['italian'].count('[') != u['english'].count('[')
       or u['italian'].count(']') != u['english'].count(']')]
bt = [u['idx'] for u in tu if '`' in u['italian']]
ck('quadre e backtick: nessuna nel lotto (assenza dichiarata)', brk == [] and bt == [], (brk, bt))

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

rs = [u['ratio'] for u in tu if u['ratio'] is not None]
ck('rapporto definito per tutte le unita', len(rs) == len(tu), (len(rs), len(tu)))
ck('rapporto dentro il gate 0,55-1,90', 0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
print('rapporto IT/EN: min %.2f max %.2f' % (min(rs), max(rs)))

dup_en = [e for e, n in collections.Counter(u['english'] for u in su).items() if n > 1]
ck('duplicati inglesi: nessun gruppo (controllo negativo)', len(dup_en) == 0, len(dup_en))
seen = collections.Counter(by_idx[u['idx']]['italian'] for u in tu)
ck('nessuna resa italiana ripetuta fra unita con inglese diverso',
   not [k[:40] for k, n in seen.items() if n > 1], [k[:40] for k, n in seen.items() if n > 1])

merged = {}
for f in sorted(glob.glob(os.path.join(HERE, 'parts', 'part*.json'))):
    for k, v in json.load(open(f, encoding='utf-8')).items():
        merged[int(k)] = v
en_by_idx = {u['idx']: u['english'] for u in su}
rebuilt = {i: '\t' * (len(en_by_idx[i]) - len(en_by_idx[i].lstrip('\t'))) + v
           for i, v in merged.items()}
ck('le parti su disco ricostruiscono translation.json (tab compresi)',
   rebuilt == {u['idx']: u['italian'] for u in tu})
ck('le parti coprono tutti gli idx, senza chiavi fuori lotto',
   sorted(merged) == list(range(1, 51)), (len(merged), sorted(merged)[:5]))

h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
en_w = sum(len(u['english'].split()) for u in tu)
it_w = sum(len(u['italian'].split()) for u in tu)
print('parole EN %d -> IT %d · traduzione sha256[:16] %s' % (en_w, it_w, h[:16]))

print()
print('FAIL:', len(fail), '·', 'verify L72 superato' if not fail else 'verify L72 fallito')
raise SystemExit(0 if not fail else 1)
