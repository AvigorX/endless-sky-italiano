r"""verify.py — L102 (data/quarg/quarg missions.txt, 48 unita', righe 1-117)

Primo lotto del file: invariante di **segmento**. Indipendente da `check.py`: rilegge il repository originale,
`state.db` e i `parts/`.

Misure attese: **0 unita' prima** della riga 19 (nessun lotto precedente su questo file), **130 dopo la 117**,
file di **178 unita'**, `max(line) = 506`, confine alla riga **124** (`Quarg Satellites`). **46 `MISSION_TEXT` +
2 `LOGBOOK`** (unita' 1 e 2, tradotti e non identici), **44 tab**, **98 virgolette**, **2 token** (`<first>`,
`<last>`), **0 quadre**, tre ripetizioni (17/20, 35/40, 37/38).
"""
import collections, glob, hashlib, json, os, re, sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
ROOT = os.path.abspath(os.path.join(L10N, '..'))
PATH = 'data/quarg/quarg missions.txt'
su = sorted(json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
TAGS = re.compile(r'<[^<>]+>')
GROUPS = [(17, 20), (35, 40), (37, 38)]
fail = []


def ck(n, c, d=''):
    print('%-64s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente', not [u for u in su if lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context,state from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck('tutte PENDING', not [u['idx'] for u in su
   if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('idx 1..48 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 49)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 48 righe 19 - 117', len(tu) == 48 and (first, last) == (19, 117), (len(tu), first, last))
tot = db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0]
before = db.execute('select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0]
after = db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0]
maxl = db.execute('select max(line) from units where path=?', (PATH,)).fetchone()[0]
ck('0 unita prima della riga 19 (primo lotto del file)', before == 0, before)
ck('130 unita dopo la riga 117', after == 130, after)
ck('file: 178 unita, max(line) = 506', tot == 178 and maxl == 506, (tot, maxl))
ck('il confine: la riga 124 apre Quarg Satellites',
   db.execute('select line,context from units where path=? and line>? order by line limit 1',
              (PATH, last)).fetchone() == (124, 'mission:Quarg Satellites'))
ck('kind: 46 MISSION_TEXT + 2 LOGBOOK',
   collections.Counter(u['kind'] for u in su) == {'MISSION_TEXT': 46, 'LOGBOOK': 2},
   collections.Counter(u['kind'] for u in su))
by = {u['idx']: u for u in tu}
ck('LOGBOOK nelle unita 1 e 2, tradotti (non identici)',
   [u['idx'] for u in tu if u['kind'] == 'LOGBOOK'] == [1, 2]
   and all(by[i]['italian'].strip() != by[i]['english'].strip() for i in (1, 2)))
ck('tutte tradotte', all(u['italian'].strip() != u['english'].strip() for u in tu))
ctxs = []
for u in su:
    if u['context'] not in ctxs:
        ctxs.append(u['context'])
ck('2 contesti in ordine di riga',
   len(ctxs) == 2 and [c.split(':', 1)[1] for c in ctxs] == ['First Contact: Quarg', 'First Contact: Kuwaru Efreti'],
   ctxs)
TABS = [i for i in range(1, 49) if i not in (1, 2, 3, 28)]
ck('tab: 44 nel sorgente, nelle unita attese',
   sum(1 for u in su if u['english'].startswith('\t')) == 44
   and [u['idx'] for u in tu if u['italian'].startswith('\t')] == TABS)
ck('nessun tab aggiunto', not [u for u in tu if u['english'].count('\t') != u['italian'].count('\t')])
a = sum(u['english'].count('"') for u in su)
b = sum(u['italian'].count('"') for u in tu)
ck('virgolette: %d = %d (98)' % (a, b), a == b == 98, (a, b))
ck('virgolette per unita', not [u for u in tu if u['english'].count('"') != u['italian'].count('"')])
ck('nessuna virgoletta dispari', not [u for u in tu if u['italian'].count('"') % 2])
te = [t for u in su for t in TAGS.findall(u['english'])]
ti = [t for u in tu for t in TAGS.findall(u['italian'])]
ck('token: <first> e <last>, nell\'unita 42', te == ti == ['<first>', '<last>'] and '<first> <last>' in by[42]['italian'])
ck('nessuna quadra', not [u for u in tu if any(c in u['italian'] for c in '[]')])
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
ck('3 ripetizioni: 17/20, 35/40, 37/38',
   sorted(tuple(v) for v in grp.values() if len(v) > 1) == sorted(GROUPS))
ck('ogni gruppo reso identico', all(len({by[i]['italian'] for i in g}) == 1 for g in GROUPS))
merged = {}
for f in sorted(glob.glob(os.path.join(HERE, 'parts', 'part*.json'))):
    for kk, v in json.load(open(f, encoding='utf-8')).items():
        merged[int(kk)] = v
ck('le tre parti ricostruiscono translation.json (1..48)',
   sorted(merged) == list(range(1, 49))
   and {i: '\t' * (len(by[i]['english']) - len(by[i]['english'].lstrip('\t'))) + v
        for i, v in merged.items()} == {u['idx']: u['italian'] for u in tu})
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('parole EN %d -> IT %d · sha256[:16] %s' % (sum(len(u['english'].split()) for u in tu),
      sum(len(u['italian'].split()) for u in tu), h[:16]))
print()
print('FAIL:', len(fail), '·', 'verify L102 superato' if not fail else 'verify L102 fallito')
raise SystemExit(0 if not fail else 1)
