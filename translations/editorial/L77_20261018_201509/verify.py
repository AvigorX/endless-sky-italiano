r"""verify.py — L77 (data/successors/successor side missions.txt, 63 unita', righe 1-220)

Verifica **indipendente** da `check.py`.

Invariante di **segmento** (il file prosegue): segmento 17-220, **0 unita' prima** (il lotto apre il file),
**101 dopo**, `max(line) = 453`, file di **164 unita'**, confine alla riga 224 (`Stargazing 1`).

Misure attese, lette dal workspace il 2026-10-18:
  - 63 unita', righe 17-220, **2 contesti interi** (`Predecessor Research 1` 37, `Biology Research 1` 26);
  - tipi: 58 `MISSION_TEXT`, 2 `VALUE`, 2 `DESCRIPTION`, 1 `UI_LABEL`;
  - **`UI_LABEL` 1** (12, `has deferred`) identica in `NT`;
  - **0 `LOGBOOK` / `DIALOG` / `CONVERSATION` / `TEXT`**: assenze dichiarate (in L76 erano 1 e 2);
  - **virgolette dispari: insieme (56, 57)**, entrambe **aprono e non chiudono**;
  - **3 gruppi di duplicati inglesi** (7/42, 9/43, 28/55) con resa identica;
  - **13 token** in 6 famiglie, `<planet stopovers>` compreso (spazio nel nome);
  - **53 tab** su 53 unita', **68 virgolette**, 0 quadre, 0 backtick.
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
PATH = 'data/successors/successor side missions.txt'
SRC = os.path.join(ROOT, 'endless-sky', *PATH.split('/'))

source = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
trans = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))
su, tu = source['units'], trans['units']
lines = open(SRC, encoding='utf-8').read().split('\n')

NT = {12}
ODD = (56, 57)
DUPS = [frozenset([7, 42]), frozenset([9, 43]), frozenset([28, 55])]
TAGS = re.compile(r'<[^<>]+>')

fail = []


def ck(name, cond, detail=''):
    print('%-70s %s %s' % (name, 'OK' if cond else 'FAIL', '' if cond else detail))
    if not cond:
        fail.append(name)


bad_raw = [u['idx'] for u in su if lines[u['line'] - 1] != u['raw']]
ck('riga grezza identica al file sorgente (63 righe)', not bad_raw, bad_raw[:10])

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
ck('idx del segmento senza buchi (1..63)', [u['idx'] for u in tu] == list(range(1, 64)))

first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 63 righe 17 - 220', len(tu) == 63 and (first, last) == (17, 220), (len(tu), first, last))

tot = db.execute('select count(*) from units where path = ?', (PATH,)).fetchone()[0]
before = db.execute('select count(*) from units where path = ? and line < ?', (PATH, first)).fetchone()[0]
after = db.execute('select count(*) from units where path = ? and line > ?', (PATH, last)).fetchone()[0]
maxline = db.execute('select max(line) from units where path = ?', (PATH,)).fetchone()[0]
ck('apre il file: 0 unita prima della riga 17', before == 0, before)
ck('il file prosegue: 101 unita dopo la riga 220', after == 101, after)
ck('file: 164 unita totali, max(line) = 453', tot == 164 and maxline == 453, (tot, maxline))
nxt = db.execute('select line, context from units where path = ? and line > ? order by line limit 1',
                 (PATH, last)).fetchone()
ck('confine dopo: riga 224 apre Successors: Stargazing 1',
   nxt is not None and nxt['line'] == 224 and nxt['context'] == 'mission:Successors: Stargazing 1',
   tuple(nxt) if nxt else None)

lrows = sorted(u['line'] for u in su)
ck('segmento 17-220: prima/ultima riga coerenti', lrows[0] == 17 and lrows[-1] == 220, (lrows[0], lrows[-1]))
ck('nessuna riga del segmento con due unita (63 righe distinte)', len(set(lrows)) == 63 == len(lrows))
inrange = db.execute('select count(*) from units where path = ? and line between ? and ?',
                     (PATH, first, last)).fetchone()[0]
ck('nessun altra unita nel DB dentro 17-220 (%d)' % inrange, inrange == len(tu), inrange)
ctxs = []
for u in su:
    if u['context'] not in ctxs:
        ctxs.append(u['context'])
ck('2 contesti interi, in ordine di riga',
   ctxs == ['mission:Successors: Predecessor Research 1', 'mission:Successors: Biology Research 1'], ctxs)
c1 = db.execute("select count(*) from units where path = ? and context = 'mission:Successors: Predecessor Research 1'",
                (PATH,)).fetchone()[0]
c2 = db.execute("select count(*) from units where path = ? and context = 'mission:Successors: Biology Research 1'",
                (PATH,)).fetchone()[0]
ck('i due contesti sono interi: 37 + 26 unita', (c1, c2) == (37, 26), (c1, c2))

kinds = collections.Counter(u['kind'] for u in su)
ck('kind: 58 MISSION_TEXT, 2 VALUE, 2 DESCRIPTION, 1 UI_LABEL',
   dict(kinds) == {'MISSION_TEXT': 58, 'VALUE': 2, 'DESCRIPTION': 2, 'UI_LABEL': 1}, dict(kinds))

by_idx = {u['idx']: u for u in tu}
ui = sorted(u['idx'] for u in su if u['kind'] == 'UI_LABEL')
ck('UI_LABEL: 1 unita (12)', ui == [12], ui)
ck('label `has deferred` lasciata identica',
   by_idx[12]['italian'] == by_idx[12]['english'] == 'has deferred')
ck('LOGBOOK / DIALOG / CONVERSATION / TEXT: nessuna unita (assenze dichiarate)',
   all(not [u for u in tu if u['kind'] == k] for k in ('LOGBOOK', 'DIALOG', 'CONVERSATION', 'TEXT')))
vd = sorted(u['idx'] for u in su if u['kind'] in ('VALUE', 'DESCRIPTION'))
ck('VALUE e DESCRIPTION: 2 + 2 presenti e tradotti (1, 2, 38, 39)', vd == [1, 2, 38, 39], vd)
ck('i quattro VALUE/DESCRIPTION hanno testo diverso dall inglese',
   all(by_idx[i]['italian'].strip() != by_idx[i]['english'].strip() for i in vd))

tok_en = sum(len(TAGS.findall(u['english'])) for u in su)
tok_it = sum(len(TAGS.findall(u['italian'])) for u in tu)
fam_en = collections.Counter(t for u in su for t in TAGS.findall(u['english']))
fam_it = collections.Counter(t for u in tu for t in TAGS.findall(u['italian']))
ck('token <...>: 13 in inglese e 13 in italiano, 6 famiglie (`<planet stopovers>` con spazio)',
   tok_en == 13 and tok_it == 13 and fam_en == fam_it
   and fam_en == collections.Counter({'<destination>': 4, '<planet stopovers>': 3, '<date>': 2,
                                      '<payment>': 2, '<bunks>': 1, '<stopovers>': 1}),
   (tok_en, tok_it, dict(fam_en), dict(fam_it)))
diff = [u['idx'] for u in tu
        if collections.Counter(TAGS.findall(u['english'])) != collections.Counter(TAGS.findall(u['italian']))]
ck('nessuna unita con token diversi (parita per simbolo e per unita)', not diff, sorted(set(diff))[:10])

for ch, nome, atteso_n in (('\t', 'tab', 53), ('"', 'virgolette', 68)):
    a = sum(u['english'].count(ch) for u in su)
    b = sum(u['italian'].count(ch) for u in tu)
    ck('%s totali %d = %d (attese %d)' % (nome, b, a, atteso_n), a == b == atteso_n, (a, b))

per_unit = [u['idx'] for u in tu if u['english'].count('\t') != u['italian'].count('\t')
            or u['english'].count('"') != u['italian'].count('"')]
ck('tab e virgolette: parita per unita (63 unita)', per_unit == [], per_unit[:10])
ntab = len([u for u in tu if u['italian'].startswith('\t')])
lead = [u['idx'] for u in tu if u['english'].startswith('\t') != u['italian'].startswith('\t')]
ck('tab iniziale su 53 unita su 63', ntab == 53 and lead == [], (ntab, lead[:5]))

odd_en = tuple(sorted(u['idx'] for u in su if u['english'].count('"') % 2))
odd_it = tuple(sorted(u['idx'] for u in tu if u['italian'].count('"') % 2))
ck('virgolette dispari: insieme (56, 57) in inglese e in italiano',
   odd_en == tuple(sorted(ODD)) and odd_it == tuple(sorted(ODD)), (odd_en, odd_it))
ck('56 e 57 aprono la virgoletta e NON la chiudono',
   all(by_idx[i]['italian'].lstrip('\t').startswith('"') and
       not by_idx[i]['italian'].rstrip().endswith('"') for i in ODD))
ck('58 chiude la virgoletta (coppia bilanciata)',
   by_idx[58]['italian'].count('"') == 2 and by_idx[58]['italian'].rstrip().endswith('"'))
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
dups = set(frozenset(v) for v in grp.values() if len(v) > 1)
ck('duplicati inglesi: 3 gruppi (7/42, 9/43, 28/55)', len(dups), dups == set(DUPS))
ck('i tre gruppi hanno resa identica',
   all(len(set(by_idx[i]['italian'] for i in g)) == 1 for g in DUPS))
seen = collections.Counter(by_idx[u['idx']]['italian'] for u in tu)
free = [k[:40] for k, n in seen.items() if n > 1 and not any(k == by_idx[i]['italian'] for g in DUPS for i in g)]
ck('nessun altra resa ripetuta fra inglesi diversi', not free, free)

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
   sorted(merged) == list(range(1, 64)), (len(merged), sorted(merged)[:5]))

h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
en_w = sum(len(u['english'].split()) for u in tu)
it_w = sum(len(u['italian'].split()) for u in tu)
print('parole EN %d -> IT %d · traduzione sha256[:16] %s' % (en_w, it_w, h[:16]))

print()
print('FAIL:', len(fail), '·', 'verify L77 superato' if not fail else 'verify L77 fallito')
raise SystemExit(0 if not fail else 1)
