r"""verify.py — L76 (data/successors/successor 2 ghosts aqrabe.txt, 30 unita', righe 401-478)

**Lotto che chiude il file**, quindi vale l'invariante **di file** (decisione 166), non di segmento:
  - `0` unita' dopo la riga 478, `max(line) = 478`, **180 unita' totali** nel file;
  - copertura dell'**intero file**: le 180 unita' sono in staging nei lotti L73-L76, senza buchi.

Misure attese, lette dal workspace il 2026-10-18:
  - 30 unita', righe 404-478, **1 contesto** (`Ghosts Aqrabe 7`);
  - tipi: 24 `MISSION_TEXT`, 1 `VALUE`, 1 `DESCRIPTION`, 2 `DIALOG`, 1 `LOGBOOK`, 1 `UI_LABEL`;
  - **`UI_LABEL` 1** (28, `not confronted`) identica in `NT`; **`LOGBOOK` 1** (14) forma diretta, tradotto;
  - **`DIALOG` 2** (12 con backtick nel `raw`, 13 con virgolette): testi, tradotti;
  - **1 virgoletta dispari** (25): la virgoletta **non** chiude, e la coppia 23/25 differisce **solo** per
    quello;
  - **6 token** in 5 famiglie: `<ship>` 2, `<destination>`/`<capacity>`/`<planet>`/`<payment>` 1;
  - **21 tab** su **21 unita'**, **43 virgolette**, 0 quadre, 0 backtick; **0 duplicati**.
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
PATH = 'data/successors/successor 2 ghosts aqrabe.txt'
SRC = os.path.join(ROOT, 'endless-sky', *PATH.split('/'))

source = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
trans = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))
su, tu = source['units'], trans['units']
lines = open(SRC, encoding='utf-8').read().split('\n')

NT = {28}
LOG = {14}
DLG = {12, 13}
ODD = (25,)
TAGS = re.compile(r'<[^<>]+>')

fail = []


def ck(name, cond, detail=''):
    print('%-70s %s %s' % (name, 'OK' if cond else 'FAIL', '' if cond else detail))
    if not cond:
        fail.append(name)


bad_raw = [u['idx'] for u in su if lines[u['line'] - 1] != u['raw']]
ck('riga grezza identica al file sorgente (30 righe)', not bad_raw, bad_raw[:10])

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
ck('idx del segmento senza buchi (1..30)', [u['idx'] for u in tu] == list(range(1, 31)))

first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 30 righe 404 - 478', len(tu) == 30 and (first, last) == (404, 478), (len(tu), first, last))

# --- invariante di FILE
tot = db.execute('select count(*) from units where path = ?', (PATH,)).fetchone()[0]
before = db.execute('select count(*) from units where path = ? and line < ?', (PATH, first)).fetchone()[0]
after = db.execute('select count(*) from units where path = ? and line > ?', (PATH, last)).fetchone()[0]
maxline = db.execute('select max(line) from units where path = ?', (PATH,)).fetchone()[0]
ck('continua il file: 150 unita prima della riga 404 (L73 + L74 + L75)', before == 150, before)
ck('CHIUDE il file: 0 unita dopo la riga 478', after == 0, after)
ck('file completo: 180 unita totali, max(line) = 478', tot == 180 and maxline == 478, (tot, maxline))

# copertura dell'intero file: ogni unita' del file deve stare in un translation.json dei lotti
staged_ids = set()
staged_lines = set()
for f in glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json')):
    try:
        data = json.load(open(f, encoding='utf-8'))
    except Exception:
        continue
    for u in data.get('units', []):
        if u.get('path') == PATH:
            staged_ids.add(u['id'])
            staged_lines.add(u['line'])
file_ids = set(r[0] for r in db.execute('select id from units where path = ?', (PATH,)).fetchall())
ck('copertura del file intero: tutte le 180 unita sono in staging', len(staged_ids) == 180 == len(file_ids),
   (len(staged_ids), len(file_ids)))
ck('copertura del file intero: nessuna riga senza unita in staging', len(staged_lines) == 180, len(staged_lines))
ck('nessuna unita fuori dal file attribuita a questo lotto', all(u['path'] == PATH for u in tu))

lrows = sorted(u['line'] for u in su)
ck('segmento 404-478: prima/ultima riga coerenti', lrows[0] == 404 and lrows[-1] == 478, (lrows[0], lrows[-1]))
ck('nessuna riga del segmento con due unita (30 righe distinte)', len(set(lrows)) == 30 == len(lrows))
inrange = db.execute('select count(*) from units where path = ? and line between ? and ?',
                     (PATH, first, last)).fetchone()[0]
ck('nessun altra unita nel DB dentro 404-478 (%d)' % inrange, inrange == len(tu), inrange)
ctxs = []
for u in su:
    if u['context'] not in ctxs:
        ctxs.append(u['context'])
ck('1 contesto: Successors: Ghosts Aqrabe 7', ctxs == ['mission:Successors: Ghosts Aqrabe 7'], ctxs)

kinds = collections.Counter(u['kind'] for u in su)
ck('kind: 24 MISSION_TEXT, 1 VALUE, 1 DESCRIPTION, 2 DIALOG, 1 LOGBOOK, 1 UI_LABEL',
   dict(kinds) == {'MISSION_TEXT': 24, 'VALUE': 1, 'DESCRIPTION': 1, 'DIALOG': 2, 'LOGBOOK': 1,
                   'UI_LABEL': 1}, dict(kinds))

by_idx = {u['idx']: u for u in tu}
ui = sorted(u['idx'] for u in su if u['kind'] == 'UI_LABEL')
ck('UI_LABEL: 1 unita (28)', ui == [28], ui)
ck('label `not confronted` lasciata identica',
   by_idx[28]['italian'] == by_idx[28]['english'] == 'not confronted')
raw_by_idx = {u['idx']: u['raw'] for u in su}
ck('la riga `log` e diretta (un solo argomento)',
   re.match(r'\t+log "[^"]+"\s*$', raw_by_idx[14]) is not None, raw_by_idx[14][:60])
ck('LOGBOOK: 1 unita (14), testo tradotto', by_idx[14]['italian'].strip() != by_idx[14]['english'].strip())
dlg = sorted(u['idx'] for u in tu if u['kind'] == 'DIALOG')
ck('DIALOG: 2 unita (12, 13), testi tradotti', dlg == sorted(DLG)
   and all(by_idx[i]['italian'].strip() != by_idx[i]['english'].strip() for i in DLG), dlg)
ck('il raw dei due DIALOG usa forme diverse (backtick in 12, virgolette in 13)',
   '`' in raw_by_idx[12] and '`' not in raw_by_idx[13])
conv = [u['idx'] for u in tu if u['kind'] == 'CONVERSATION']
txt = [u['idx'] for u in tu if u['kind'] == 'TEXT']
ck('CONVERSATION e TEXT: nessuna unita (assenze dichiarate)', conv == [] and txt == [], (conv, txt))
vd = sorted(u['idx'] for u in su if u['kind'] in ('VALUE', 'DESCRIPTION'))
ck('VALUE e DESCRIPTION: 1 + 1 presenti e tradotti (1, 2)', vd == [1, 2], vd)
ck('i due VALUE/DESCRIPTION hanno testo diverso dall inglese',
   all(by_idx[i]['italian'].strip() != by_idx[i]['english'].strip() for i in vd))

tok_en = sum(len(TAGS.findall(u['english'])) for u in su)
tok_it = sum(len(TAGS.findall(u['italian'])) for u in tu)
fam_en = collections.Counter(t for u in su for t in TAGS.findall(u['english']))
fam_it = collections.Counter(t for u in tu for t in TAGS.findall(u['italian']))
ck('token <...>: 6 in inglese e 6 in italiano, 5 famiglie',
   tok_en == 6 and tok_it == 6 and fam_en == fam_it
   and fam_en == collections.Counter({'<ship>': 2, '<destination>': 1, '<capacity>': 1,
                                      '<planet>': 1, '<payment>': 1}),
   (tok_en, tok_it, dict(fam_en), dict(fam_it)))
diff = [u['idx'] for u in tu
        if collections.Counter(TAGS.findall(u['english'])) != collections.Counter(TAGS.findall(u['italian']))]
ck('nessuna unita con token diversi (parita per simbolo e per unita)', not diff, sorted(set(diff))[:10])

for ch, nome, atteso_n in (('\t', 'tab', 21), ('"', 'virgolette', 43)):
    a = sum(u['english'].count(ch) for u in su)
    b = sum(u['italian'].count(ch) for u in tu)
    ck('%s totali %d = %d (attese %d)' % (nome, b, a, atteso_n), a == b == atteso_n, (a, b))

per_unit = [u['idx'] for u in tu if u['english'].count('\t') != u['italian'].count('\t')
            or u['english'].count('"') != u['italian'].count('"')]
ck('tab e virgolette: parita per unita (30 unita)', per_unit == [], per_unit[:10])
ntab = len([u for u in tu if u['italian'].startswith('\t')])
lead = [u['idx'] for u in tu if u['english'].startswith('\t') != u['italian'].startswith('\t')]
ck('tab iniziale su 21 unita su 30', ntab == 21 and lead == [], (ntab, lead[:5]))

odd_en = tuple(sorted(u['idx'] for u in su if u['english'].count('"') % 2))
odd_it = tuple(sorted(u['idx'] for u in tu if u['italian'].count('"') % 2))
ck('virgoletta dispari: insieme (25) in inglese e in italiano',
   odd_en == tuple(sorted(ODD)) and odd_it == tuple(sorted(ODD)), (odd_en, odd_it))
ck('in 25 la virgoletta NON chiude (come in inglese)',
   not by_idx[25]['italian'].rstrip().endswith('"') and not by_idx[25]['english'].rstrip().endswith('"'))
ck('coppia quasi identica 23/25: differiscono solo per la virgoletta finale',
   by_idx[23]['italian'].rstrip('"') == by_idx[25]['italian'].rstrip('"')
   and by_idx[23]['italian'].endswith('"') and not by_idx[25]['italian'].endswith('"'),
   (by_idx[23]['italian'], by_idx[25]['italian']))
brk = [u['idx'] for u in tu if u['italian'].count('[') != u['english'].count('[')
       or u['italian'].count(']') != u['english'].count(']')]
bt = [u['idx'] for u in tu if '`' in u['italian']]
ck('quadre e backtick: nessuna nel tradotto (assenza dichiarata)', brk == [] and bt == [], (brk, bt))

ck('nessuna unita con italiano vuoto', all(u['italian'].strip() for u in tu))
NONLAT = re.compile(r'[^\x00-\x7F\u00C0-\u024F\u2018\u2019\u201C\u201D\u2013\u2014\u2026]')
sus = [(u['idx'], NONLAT.findall(u['italian'])[:3]) for u in tu if NONLAT.search(u['italian'])]
ck('nessun carattere non latino sospetto', not sus, sus[:10])
dash = [u['idx'] for u in tu if '\u2014' in u['italian'] or '\u2013' in u['italian']]
ck('nessun trattino lungo/en-dash (vietati)', not dash, dash[:10])
curly = [u['idx'] for u in tu if '\u2018' in u['italian'] or '\u2019' in u['italian']
         or '\u201C' in u['italian'] or '\u201D' in u['italian']]
ck('nessuna virgoletta curva (apostrofo dritto)', not curly, curly[:10])
apos = [u['idx'] for u in tu if re.search(r"\b(e|piu|perche|cosi|gia|puo|citta|verita|entita|percio)'", u['italian'])]
ck('nessun accento sostitutivo con apostrofo', not apos, apos[:10])

rs = [u['ratio'] for u in tu if u['ratio'] is not None]
ck('rapporto definito per tutte le unita', len(rs) == len(tu), (len(rs), len(tu)))
ck('rapporto dentro il gate 0,55-1,90', 0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
print('rapporto IT/EN: min %.2f max %.2f' % (min(rs), max(rs)))

grp = {}
for u in su:
    grp.setdefault(u['english'], []).append(u['idx'])
dups = {k: v for k, v in grp.items() if len(v) > 1}
ck('duplicati inglesi esatti: nessun gruppo (controllo negativo)', len(dups) == 0, len(dups))
seen = collections.Counter(by_idx[u['idx']]['italian'] for u in tu)
ck('nessuna resa italiana ripetuta', not [k[:40] for k, n in seen.items() if n > 1],
   [k[:40] for k, n in seen.items() if n > 1])

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
   sorted(merged) == list(range(1, 31)), (len(merged), sorted(merged)[:5]))

h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
en_w = sum(len(u['english'].split()) for u in tu)
it_w = sum(len(u['italian'].split()) for u in tu)
print('parole EN %d -> IT %d · traduzione sha256[:16] %s' % (en_w, it_w, h[:16]))

print()
print('FAIL:', len(fail), '·', 'verify L76 superato' if not fail else 'verify L76 fallito')
raise SystemExit(0 if not fail else 1)
