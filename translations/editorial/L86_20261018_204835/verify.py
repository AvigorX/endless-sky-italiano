r"""verify.py — L86 (data/successors/successor outfits.txt, 21 unita', righe 1-240)

Indipendente da `check.py`. Invariante di **segmento**: **0 prima** (primo lotto del file), **35 dopo**,
`max(line) = 647`, file di **56 unita'**, confine alla riga 251 (`outfit:"Ryuit" Fusion Core`).
Misure: 21 unita', righe 19-235; 17 `DESCRIPTION` + 4 `VALUE`; 4 dato identiche (plurali dei cortex),
17 prosa tradotte; 1 tab; 8 virgolette; 0 token; 0 duplicati.
"""
import collections, glob, hashlib, json, os, re, sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
ROOT = os.path.abspath(os.path.join(L10N, '..'))
PATH = 'data/successors/successor outfits.txt'
su = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units']
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
DATA, PROSE = {6, 8, 10, 12}, {1, 2, 3, 4, 5, 7, 9, 11, 13, 14, 15, 16, 17, 18, 19, 20, 21}
fail = []


def ck(n, c, d=''):
    print('%-64s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente', not [u['idx'] for u in su if lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context,state from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck('tutte PENDING', not [u['idx'] for u in su
   if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('idx 1..21 e ordine = sorgente',
   [u['idx'] for u in tu] == list(range(1, 22)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 21 righe 19 - 235', len(tu) == 21 and (first, last) == (19, 235), (len(tu), first, last))
tot = db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0]
before = db.execute('select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0]
after = db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0]
maxl = db.execute('select max(line) from units where path=?', (PATH,)).fetchone()[0]
ck('primo lotto del file: 0 unita prima della riga 19', before == 0, before)
ck('il file prosegue: 35 unita dopo la riga 235', after == 35, after)
ck('file: 56 unita, max(line) = 647', tot == 56 and maxl == 647, (tot, maxl))
nxt = db.execute('select line,context from units where path=? and line>? order by line limit 1', (PATH, last)).fetchone()
ck('confine: riga 251 apre outfit:"Ryuit" Fusion Core',
   nxt is not None and nxt[0] == 251 and nxt[1] == 'outfit:"Ryuit" Fusion Core', tuple(nxt) if nxt else None)
k = collections.Counter(u['kind'] for u in su)
ck('kind: 17 DESCRIPTION, 4 VALUE', dict(k) == {'DESCRIPTION': 17, 'VALUE': 4}, dict(k))
by = {u['idx']: u for u in tu}
ck('le 4 VALUE restano identiche', all(by[i]['italian'] == by[i]['english'] for i in DATA),
   [i for i in sorted(DATA) if by[i]['italian'] != by[i]['english']])
ck('le 17 DESCRIPTION sono tradotte',
   all(by[i]['italian'].strip() != by[i]['english'].strip() for i in PROSE))
ctxs = []
for u in su:
    if u['context'] not in ctxs:
        ctxs.append(u['context'])
ck('15 contesti, in ordine di riga', len(ctxs) == 15 and ctxs[0] == 'outfit:Successor License'
   and ctxs[-1] == 'outfit:"Nnesa" Fusion Core', (len(ctxs), ctxs[0], ctxs[-1]))
a = sum(u['english'].count('"') for u in su)
b = sum(u['italian'].count('"') for u in tu)
ck('virgolette: %d = %d (8)' % (b, a), a == b == 8, (a, b))
ck('tab: 1 nel sorgente, solo in unita 3',
   sum(1 for u in su if u['english'].startswith('\t')) == 1
   and [u['idx'] for u in tu if u['italian'].startswith('\t')] == [3])
ck('nessun tab aggiunto', not [u for u in tu if u['english'].count('\t') != u['italian'].count('\t')])
ck('nessuna quadra o backtick', not [u for u in tu if '[' in u['italian'] or '`' in u['italian']])
ck('nessun token <...>', not [u for u in tu if '<' in u['italian']])
ck('nessuna traduzione vuota', all(u['italian'].strip() for u in tu))
NONLAT = re.compile(r'[^\x00-\x7F\u00C0-\u024F\u2018\u2019\u201C\u201D\u2013\u2014\u2026]')
ck('nessun carattere non latino', not [u for u in tu if NONLAT.search(u['italian'])])
ck('nessun trattino lungo o virgoletta curva',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D')])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate', 0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
print('rapporto IT/EN: min %.2f max %.2f' % (min(rs), max(rs)))
grp = {}
for u in su:
    grp.setdefault(u['english'], []).append(u['idx'])
ck('nessun duplicato', not [v for v in grp.values() if len(v) > 1])
merged = {}
for f in sorted(glob.glob(os.path.join(HERE, 'parts', 'part*.json'))):
    for kk, v in json.load(open(f, encoding='utf-8')).items():
        merged[int(kk)] = v
ck('le parti ricostruiscono translation.json',
   {i: '\t' * (len(by[i]['english']) - len(by[i]['english'].lstrip('\t'))) + v for i, v in merged.items()}
   == {u['idx']: u['italian'] for u in tu})
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('parole EN %d -> IT %d · sha256[:16] %s' % (sum(len(u['english'].split()) for u in tu),
      sum(len(u['italian'].split()) for u in tu), h[:16]))
print()
print('FAIL:', len(fail), '·', 'verify L86 superato' if not fail else 'verify L86 fallito')
raise SystemExit(0 if not fail else 1)
