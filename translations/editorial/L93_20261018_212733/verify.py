r"""verify.py — L93 (data/coalition/coalition culture conversations.txt, 31 unita', righe 24-66)

Indipendente da `check.py`. **Primo lotto del file**: 0 unita' prima della riga 24, **126 dopo**, file di
**157** unita', `max(line) = 462`. Confine dichiarato: la prima unita' dopo la 66 e' la riga 81, contesto
`mission:Coalition Folklore: Arach`.

Misure attese: 31 `MISSION_TEXT` (0 `UI_LABEL` nella finestra — il file ne ha 8 piu' avanti), 30 tab,
22 virgolette (4 nell'unita' 5), **0 token** (asserzione), ripetizione tripla 15/20/25 resa identica.
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
ck('idx 1..31 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 32)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 31 righe 24 - 66', len(tu) == 31 and (first, last) == (24, 66), (len(tu), first, last))
tot = db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0]
before = db.execute('select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0]
after = db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0]
maxl = db.execute('select max(line) from units where path=?', (PATH,)).fetchone()[0]
ck('primo lotto del file: 0 unita prima della riga 24', before == 0, before)
ck('126 unita dopo la riga 66', after == 126, after)
ck('file: 157 unita, max(line) = 462', tot == 157 and maxl == 462, (tot, maxl))
nxt = db.execute('select line,context from units where path=? and line>? order by line limit 1', (PATH, last)).fetchone()
ck('confine: riga 81 apre Arach', nxt is not None
   and tuple(nxt) == (81, 'mission:Coalition Folklore: Arach'), tuple(nxt) if nxt else None)
ck('kind: 31 MISSION_TEXT, 0 UI_LABEL',
   collections.Counter(u['kind'] for u in su) == {'MISSION_TEXT': 31}
   and not [u for u in su if u['kind'] == 'UI_LABEL'])
ck('tutte tradotte', all(u['italian'].strip() != u['english'].strip() for u in tu))
ctxs = []
for u in su:
    if u['context'] not in ctxs:
        ctxs.append(u['context'])
ck('1 contesto: Coalition Folklore: Saryd', ctxs == ['mission:Coalition Folklore: Saryd'], ctxs)
TABS = list(range(2, 32))
ck('tab: 30 nel sorgente, nelle unita attese',
   sum(1 for u in su if u['english'].startswith('\t')) == 30
   and [u['idx'] for u in tu if u['italian'].startswith('\t')] == TABS,
   [u['idx'] for u in tu if u['italian'].startswith('\t')])
ck('nessun tab aggiunto', not [u for u in tu if u['english'].count('\t') != u['italian'].count('\t')])
a = sum(u['english'].count('"') for u in su)
b = sum(u['italian'].count('"') for u in tu)
ck('virgolette: %d = %d (22)' % (a, b), a == b == 22, (a, b))
ck('virgolette per unita, 4 nell\'unita 5',
   not [u for u in tu if u['english'].count('"') != u['italian'].count('"')]
   and [u['idx'] for u in su if u['english'].count('"') == 4] == [5])
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
ck('ripetizione inglese: 15/20/25',
   sorted(tuple(v) for v in grp.values() if len(v) > 1) == [(15, 20, 25)])
ck('15/20/25 resa identica', by[15]['italian'] == by[20]['italian'] == by[25]['italian'])
merged = {}
for f in sorted(glob.glob(os.path.join(HERE, 'parts', 'part*.json'))):
    for kk, v in json.load(open(f, encoding='utf-8')).items():
        merged[int(kk)] = v
ck('le tre parti ricostruiscono translation.json (1..31)',
   sorted(merged) == list(range(1, 32))
   and {i: '\t' * (len(by[i]['english']) - len(by[i]['english'].lstrip('\t'))) + v
        for i, v in merged.items()} == {u['idx']: u['italian'] for u in tu})
ids = [u['id'] for u in tu]
cov = db.execute('select count(*) from units where path=? and id in (%s)' % ','.join('?' * len(ids)),
                  [PATH] + ids).fetchone()[0]
ck('copertura del file: 31/157 (19,7%)', cov == 31, cov)
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('parole EN %d -> IT %d · sha256[:16] %s' % (sum(len(u['english'].split()) for u in tu),
      sum(len(u['italian'].split()) for u in tu), h[:16]))
print()
print('FAIL:', len(fail), '·', 'verify L93 superato' if not fail else 'verify L93 fallito')
raise SystemExit(0 if not fail else 1)
