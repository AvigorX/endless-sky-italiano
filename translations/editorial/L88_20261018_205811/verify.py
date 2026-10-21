r"""verify.py — L88 (data/successors/successor outfits.txt, 10 unita', righe 421-560)

Indipendente da `check.py`. Segmento: **34 prima**, **12 dopo**, file di **56**, `max(line) = 647`,
confine alla riga **574** (`outfit:Multimodal Armor: Light`). Misure: 10 unita', righe 429-560;
10 `DESCRIPTION`, nessun dato; **3 tab** (2, 6, 10); **0 virgolette**; duplicato legittimo 2/6/10.
"""
import collections, glob, hashlib, json, os, re, sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
ROOT = os.path.abspath(os.path.join(L10N, '..'))
PATH = 'data/successors/successor outfits.txt'
su = sorted(json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
fail = []


def ck(n, c, d=''):
    print('%-60s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
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
ck('idx 1..10 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 11)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 10 righe 429 - 560', len(tu) == 10 and (first, last) == (429, 560), (len(tu), first, last))
tot = db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0]
before = db.execute('select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0]
after = db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0]
maxl = db.execute('select max(line) from units where path=?', (PATH,)).fetchone()[0]
ck('34 unita prima della riga 429 (L86-L87)', before == 34, before)
ck('12 unita dopo la riga 560', after == 12, after)
ck('file: 56 unita, max(line) = 647', tot == 56 and maxl == 647, (tot, maxl))
nxt = db.execute('select line,context from units where path=? and line>? order by line limit 1', (PATH, last)).fetchone()
ck('confine: riga 574 apre Multimodal Armor: Light',
   nxt is not None and nxt[0] == 574 and nxt[1] == 'outfit:Multimodal Armor: Light', tuple(nxt) if nxt else None)
ck('kind: 10 DESCRIPTION, nessun dato',
   collections.Counter(u['kind'] for u in su) == {'DESCRIPTION': 10})
by = {u['idx']: u for u in tu}
ck('le 10 DESCRIPTION sono tradotte', all(u['italian'].strip() != u['english'].strip() for u in tu))
grp = {}
for u in su:
    grp.setdefault(u['english'], []).append(u['idx'])
ck('unica ripetizione inglese: 2/6/10',
   [tuple(v) for v in grp.values() if len(v) > 1] == [(2, 6, 10)])
ck('la ripetizione e resa identica', by[2]['italian'] == by[6]['italian'] == by[10]['italian'])
ctxs = []
for u in su:
    if u['context'] not in ctxs:
        ctxs.append(u['context'])
ck('7 contesti in ordine di riga', len(ctxs) == 7 and ctxs[0] == 'outfit:"Aqra" Inductive Reverser'
   and ctxs[-1] == 'outfit:"Veusa" Inductive Reverser', (len(ctxs), ctxs[0], ctxs[-1]))
ck('tab: 3 nel sorgente, in 2, 6, 10',
   sum(1 for u in su if u['english'].startswith('\t')) == 3
   and [u['idx'] for u in tu if u['italian'].startswith('\t')] == [2, 6, 10])
ck('nessun tab aggiunto', not [u for u in tu if u['english'].count('\t') != u['italian'].count('\t')])
a = sum(u['english'].count('"') for u in su)
b = sum(u['italian'].count('"') for u in tu)
ck('virgolette: %d = %d (0 nel sorgente)' % (a, b), a == b == 0, (a, b))
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
print('FAIL:', len(fail), '·', 'verify L88 superato' if not fail else 'verify L88 fallito')
raise SystemExit(0 if not fail else 1)
