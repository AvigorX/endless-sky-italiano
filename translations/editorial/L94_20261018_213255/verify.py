r"""verify.py — L94 (data/coalition/coalition culture conversations.txt, 36 unita', righe 81-133)

Indipendente da `check.py`. Segmento: **31 unita' prima** (L93, righe 24-66), **90 dopo**, file di **157**,
`max(line) = 462`. Confine: la prima unita' dopo la 133 e' la riga 148, contesto
`mission:Coalition Folklore: Kimek`.

Misure attese: 36 `MISSION_TEXT` (0 `UI_LABEL`), 35 tab, 64 virgolette (6 nelle unita' 1 e 7), **0 token**
(asserzione), due gruppi di ripetizioni (16/22 e 17/23/29) resi identici.
"""
import collections, glob, hashlib, json, os, re, sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
ROOT = os.path.abspath(os.path.join(L10N, '..'))
PATH = 'data/coalition/coalition culture conversations.txt'
su = sorted(json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
TAGS = re.compile(r'<[^<>]+>')
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
ck('idx 1..36 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 37)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 36 righe 81 - 133', len(tu) == 36 and (first, last) == (81, 133), (len(tu), first, last))
tot = db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0]
before = db.execute('select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0]
after = db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0]
maxl = db.execute('select max(line) from units where path=?', (PATH,)).fetchone()[0]
ck('31 unita prima della riga 81 (L93)', before == 31, before)
ck('90 unita dopo la riga 133', after == 90, after)
ck('file: 157 unita, max(line) = 462', tot == 157 and maxl == 462, (tot, maxl))
nxt = db.execute('select line,context from units where path=? and line>? order by line limit 1', (PATH, last)).fetchone()
ck('confine: riga 148 apre Kimek', nxt is not None
   and tuple(nxt) == (148, 'mission:Coalition Folklore: Kimek'), tuple(nxt) if nxt else None)
prev = db.execute('select line,context from units where path=? and line<? order by line desc limit 1', (PATH, first)).fetchone()
ck('inizio: la precedente e la 66 (Saryd)', prev is not None
   and tuple(prev) == (66, 'mission:Coalition Folklore: Saryd'), tuple(prev) if prev else None)
ck('kind: 36 MISSION_TEXT, 0 UI_LABEL',
   collections.Counter(u['kind'] for u in su) == {'MISSION_TEXT': 36}
   and not [u for u in su if u['kind'] == 'UI_LABEL'])
ck('tutte tradotte', all(u['italian'].strip() != u['english'].strip() for u in tu))
ctxs = []
for u in su:
    if u['context'] not in ctxs:
        ctxs.append(u['context'])
ck('1 contesto: Coalition Folklore: Arach', ctxs == ['mission:Coalition Folklore: Arach'], ctxs)
TABS = list(range(2, 37))
ck('tab: 35 nel sorgente, nelle unita attese',
   sum(1 for u in su if u['english'].startswith('\t')) == 35
   and [u['idx'] for u in tu if u['italian'].startswith('\t')] == TABS,
   [u['idx'] for u in tu if u['italian'].startswith('\t')])
ck('nessun tab aggiunto', not [u for u in tu if u['english'].count('\t') != u['italian'].count('\t')])
a = sum(u['english'].count('"') for u in su)
b = sum(u['italian'].count('"') for u in tu)
ck('virgolette: %d = %d (64)' % (a, b), a == b == 64, (a, b))
ck('virgolette per unita, 6 nelle unita 1 e 7',
   not [u for u in tu if u['english'].count('"') != u['italian'].count('"')]
   and [u['idx'] for u in su if u['english'].count('"') == 6] == [1, 7])
ck('nessuna virgoletta dispari', not [u for u in tu if u['italian'].count('"') % 2])
te = [t for u in su for t in TAGS.findall(u['english'])]
ti = [t for u in tu for t in TAGS.findall(u['italian'])]
ck('token: 0 = 0 (asserzione)', te == ti == [], (te, ti))
ck('nessuna quadra o backtick', not [u for u in tu if any(c in u['italian'] for c in '[]`')])
ck('nessuna traduzione vuota', all(u['italian'].strip() for u in tu))
NONLAT = re.compile(r'[^\x00-\x7F\u00C0-\u024F]')
ck('nessun carattere non latino', not [u for u in tu if NONLAT.search(u['italian'])])
ck('nessun trattino lungo o virgoletta curva',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB')])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate', 0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
print('rapporto IT/EN: min %.2f max %.2f' % (min(rs), max(rs)))
grp = {}
for u in su:
    grp.setdefault(u['english'], []).append(u['idx'])
by = {u['idx']: u for u in tu}
ck('ripetizioni inglesi: 16/22 e 17/23/29',
   sorted(tuple(v) for v in grp.values() if len(v) > 1) == [(16, 22), (17, 23, 29)])
ck('16/22 e 17/23/29 rese identiche',
   by[16]['italian'] == by[22]['italian'] and by[17]['italian'] == by[23]['italian'] == by[29]['italian'])
merged = {}
for f in sorted(glob.glob(os.path.join(HERE, 'parts', 'part*.json'))):
    for kk, v in json.load(open(f, encoding='utf-8')).items():
        merged[int(kk)] = v
ck('le tre parti ricostruiscono translation.json (1..36)',
   sorted(merged) == list(range(1, 37))
   and {i: '\t' * (len(by[i]['english']) - len(by[i]['english'].lstrip('\t'))) + v
        for i, v in merged.items()} == {u['idx']: u['italian'] for u in tu})
ids = [u['id'] for u in tu]
cov = db.execute('select count(*) from units where path=? and id in (%s)' % ','.join('?' * len(ids)),
                 [PATH] + ids).fetchone()[0]
ck('copertura del file: 67/157 (42,7%)', cov + 31 == 67, (cov + 31, 157))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('parole EN %d -> IT %d · sha256[:16] %s' % (sum(len(u['english'].split()) for u in tu),
      sum(len(u['italian'].split()) for u in tu), h[:16]))
print()
print('FAIL:', len(fail), '·', 'verify L94 superato' if not fail else 'verify L94 fallito')
raise SystemExit(0 if not fail else 1)
