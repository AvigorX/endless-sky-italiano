r"""verify.py — L90 (data/successors/successor culture conversations.txt, 34 unita', righe 1-142)

Indipendente da `check.py`. Segmento: **0 prima** (primo lotto del file), **80 dopo**, file di **114**,
`max(line) = 647`? no: **351**. Confine dichiarato: la prima unita' dopo la 142 appartiene al contesto
`mission:Successors: Graffiti`. Misure: 34 `MISSION_TEXT`, 28 tab, 2 virgolette, 3 token `<ship>`.
"""
import collections, glob, hashlib, json, os, re, sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
ROOT = os.path.abspath(os.path.join(L10N, '..'))
PATH = 'data/successors/successor culture conversations.txt'
su = sorted(json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
TAGS = re.compile(r'<[^<>]+>')
fail = []


def ck(n, c, d=''):
    print('%-62s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
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
ck('idx 1..34 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 35)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 34 righe 23 - 142', len(tu) == 34 and (first, last) == (23, 142), (len(tu), first, last))
tot = db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0]
before = db.execute('select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0]
after = db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0]
maxl = db.execute('select max(line) from units where path=?', (PATH,)).fetchone()[0]
ck('primo lotto del file: 0 unita prima della riga 23', before == 0, before)
ck('80 unita dopo la riga 142', after == 80, after)
ck('file: 114 unita, max(line) = 351', tot == 114 and maxl == 351, (tot, maxl))
nxt = db.execute('select line,context from units where path=? and line>? order by line limit 1', (PATH, last)).fetchone()
ck('confine: la prossima unita e Graffiti', nxt is not None and nxt[1] == 'mission:Successors: Graffiti',
   tuple(nxt) if nxt else None)
ck('kind: 34 MISSION_TEXT', collections.Counter(u['kind'] for u in su) == {'MISSION_TEXT': 34})
ck('tutte tradotte', all(u['italian'].strip() != u['english'].strip() for u in tu))
ctxs = []
for u in su:
    if u['context'] not in ctxs:
        ctxs.append(u['context'])
ck('6 contesti in ordine di riga', len(ctxs) == 6 and ctxs[0].endswith('Kua-Oa-Aava')
   and ctxs[-1].endswith('Buskers'), (len(ctxs), ctxs[0], ctxs[-1]))
ck('tab: 28 nel sorgente',
   sum(1 for u in su if u['english'].startswith('\t')) == 28
   and [u['idx'] for u in tu if u['italian'].startswith('\t')]
   == [i for i in range(3, 11)] + [13, 14, 15, 16] + list(range(19, 35)))
ck('nessun tab aggiunto', not [u for u in tu if u['english'].count('\t') != u['italian'].count('\t')])
a = sum(u['english'].count('"') for u in su)
b = sum(u['italian'].count('"') for u in tu)
ck('virgolette: %d = %d (2)' % (a, b), a == b == 2, (a, b))
ck('nessuna virgoletta dispari', not [u for u in tu if u['italian'].count('"') % 2])
te = [t for u in su for t in TAGS.findall(u['english'])]
ti = [t for u in tu for t in TAGS.findall(u['italian'])]
ck('token: 3 = 3 e identici', te == ti == ['<ship>'] * 3, (te, ti))
ck('nessuna quadra o backtick', not [u for u in tu if '[' in u['italian'] or '`' in u['italian']])
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
ck('ripetizioni inglesi: 3/13 e 26/31', [tuple(v) for v in grp.values() if len(v) > 1] == [(3, 13), (26, 31)])
by = {u['idx']: u for u in tu}
ck('3/13: stesso inglese, genere diverso (bastone/nave-sfera)',
   by[3]['italian'][:-3] == by[13]['italian'][:-3] and (by[3]['italian'][-3], by[13]['italian'][-3]) == ('o', 'a'),
   (by[3]['italian'], by[13]['italian']))
ck('26/31: rese identiche', by[26]['italian'] == by[31]['italian'])
merged = {}
for f in sorted(glob.glob(os.path.join(HERE, 'parts', 'part*.json'))):
    for kk, v in json.load(open(f, encoding='utf-8')).items():
        merged[int(kk)] = v
ck('le due parti ricostruiscono translation.json (1..34)', sorted(merged) == list(range(1, 35))
   and {i: '\t' * (len({u['idx']: u for u in tu}[i]['english'])
                    - len({u['idx']: u for u in tu}[i]['english'].lstrip('\t'))) + v
        for i, v in merged.items()} == {u['idx']: u['italian'] for u in tu})
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('parole EN %d -> IT %d · sha256[:16] %s' % (sum(len(u['english'].split()) for u in tu),
      sum(len(u['italian'].split()) for u in tu), h[:16]))
print()
print('FAIL:', len(fail), '·', 'verify L90 superato' if not fail else 'verify L90 fallito')
raise SystemExit(0 if not fail else 1)
