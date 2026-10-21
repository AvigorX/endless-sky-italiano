r"""verify.py — L87 (data/successors/successor outfits.txt, 13 unita', righe 241-420)

Indipendente da `check.py`. Segmento: **21 prima**, **22 dopo**, file di **56**, `max(line) = 647`,
confine alla riga **429** (`outfit:"Aqra" Inductive Reverser`). Misure: 13 unita', righe 251-409;
12 `DESCRIPTION` + 1 `VALUE`; 3 tab (2, 7, 9); 2 virgolette; 0 token; 0 duplicati.
"""
import collections, glob, hashlib, json, os, re, sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
ROOT = os.path.abspath(os.path.join(L10N, '..'))
PATH = 'data/successors/successor outfits.txt'
su = sorted(json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
PROSE = {1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13}
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
ck('idx 1..13 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 14)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 13 righe 251 - 409', len(tu) == 13 and (first, last) == (251, 409), (len(tu), first, last))
tot = db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0]
before = db.execute('select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0]
after = db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0]
maxl = db.execute('select max(line) from units where path=?', (PATH,)).fetchone()[0]
ck('21 unita prima della riga 251 (L86)', before == 21, before)
ck('22 unita dopo la riga 409', after == 22, after)
ck('file: 56 unita, max(line) = 647', tot == 56 and maxl == 647, (tot, maxl))
nxt = db.execute('select line,context from units where path=? and line>? order by line limit 1', (PATH, last)).fetchone()
ck('confine: riga 429 apre "Aqra" Inductive Reverser',
   nxt is not None and nxt[0] == 429 and nxt[1] == 'outfit:"Aqra" Inductive Reverser', tuple(nxt) if nxt else None)
by = {u['idx']: u for u in tu}
ck('kind: 12 DESCRIPTION, 1 VALUE',
   collections.Counter(u['kind'] for u in su) == {'DESCRIPTION': 12, 'VALUE': 1})
ck('il VALUE resta identico', by[10]['italian'] == by[10]['english'])
ck('le 12 DESCRIPTION sono tradotte', all(by[i]['italian'].strip() != by[i]['english'].strip() for i in PROSE))
ctxs = []
for u in su:
    if u['context'] not in ctxs:
        ctxs.append(u['context'])
ck('9 contesti in ordine di riga', len(ctxs) == 9 and ctxs[0] == 'outfit:"Ryuit" Fusion Core'
   and ctxs[-1] == 'outfit:"Aqra" Inductive Steering', (len(ctxs), ctxs[0], ctxs[-1]))
ck('tab: 3 nel sorgente, in 2, 7, 9',
   sum(1 for u in su if u['english'].startswith('\t')) == 3
   and [u['idx'] for u in tu if u['italian'].startswith('\t')] == [2, 7, 9])
ck('nessun tab aggiunto', not [u for u in tu if u['english'].count('\t') != u['italian'].count('\t')])
a = sum(u['english'].count('"') for u in su)
b = sum(u['italian'].count('"') for u in tu)
ck('virgolette: %d = %d (2)' % (b, a), a == b == 2, (a, b))
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
ck('nessun duplicato inglese', not [v for v in grp.values() if len(v) > 1])
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
print('FAIL:', len(fail), '·', 'verify L87 superato' if not fail else 'verify L87 fallito')
raise SystemExit(0 if not fail else 1)
