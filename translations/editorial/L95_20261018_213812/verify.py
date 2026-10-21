r"""verify.py — L95 (data/coalition/coalition culture conversations.txt, 27 unita', righe 148-190)

Indipendente da `check.py`. Segmento: **67 unita' prima** (L93+L94), **63 dopo**, file di **157**,
`max(line) = 462`. Il lotto finisce **dentro** il contesto: la prima unita' dopo la 190 e' la riga 192, ancora
`mission:Coalition Folklore: Kimek`.

Misure attese: 24 `MISSION_TEXT` + 3 `UI_LABEL` (`defend r`, `defend rw`, `defend w`, **identiche**: sono
etichette di salto), 23 tab, 38 virgolette, **0 token** (asserzione), ripetizione 20/27 resa identica.
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
NT = [18, 23, 25]
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
ck('idx 1..27 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 28)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 27 righe 148 - 190', len(tu) == 27 and (first, last) == (148, 190), (len(tu), first, last))
tot = db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0]
before = db.execute('select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0]
after = db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0]
maxl = db.execute('select max(line) from units where path=?', (PATH,)).fetchone()[0]
ck('67 unita prima della riga 148 (L93+L94)', before == 67, before)
ck('63 unita dopo la riga 190', after == 63, after)
ck('file: 157 unita, max(line) = 462', tot == 157 and maxl == 462, (tot, maxl))
nxt = db.execute('select line,context from units where path=? and line>? order by line limit 1', (PATH, last)).fetchone()
ck('confine: riga 192, stesso contesto Kimek', nxt is not None
   and tuple(nxt) == (192, 'mission:Coalition Folklore: Kimek'), tuple(nxt) if nxt else None)
prev = db.execute('select line,context from units where path=? and line<? order by line desc limit 1', (PATH, first)).fetchone()
ck('inizio: la precedente e la 133 (Arach)', prev is not None
   and tuple(prev) == (133, 'mission:Coalition Folklore: Arach'), tuple(prev) if prev else None)
ck('kind: 24 MISSION_TEXT + 3 UI_LABEL',
   collections.Counter(u['kind'] for u in su) == {'MISSION_TEXT': 24, 'UI_LABEL': 3})
by = {u['idx']: u for u in tu}
ck('UI_LABEL 18/23/25 identiche (etichette di salto)',
   [u['idx'] for u in tu if u['kind'] == 'UI_LABEL'] == NT
   and all(by[i]['italian'] == by[i]['english'] for i in NT)
   and [by[i]['english'] for i in NT] == ['defend r', 'defend rw', 'defend w'])
ck('le altre 24 sono tradotte',
   all(u['italian'].strip() != u['english'].strip() for u in tu if u['idx'] not in NT),
   [u['idx'] for u in tu if u['idx'] not in NT and u['italian'].strip() == u['english'].strip()])
ctxs = []
for u in su:
    if u['context'] not in ctxs:
        ctxs.append(u['context'])
ck('1 contesto: Coalition Folklore: Kimek', ctxs == ['mission:Coalition Folklore: Kimek'], ctxs)
TABS = list(range(2, 18)) + [19, 20, 21, 22, 24, 26, 27]
ck('tab: 23 nel sorgente, nelle unita attese',
   sum(1 for u in su if u['english'].startswith('\t')) == 23
   and [u['idx'] for u in tu if u['italian'].startswith('\t')] == TABS,
   [u['idx'] for u in tu if u['italian'].startswith('\t')])
ck('nessun tab aggiunto', not [u for u in tu if u['english'].count('\t') != u['italian'].count('\t')])
a = sum(u['english'].count('"') for u in su)
b = sum(u['italian'].count('"') for u in tu)
ck('virgolette: %d = %d (38)' % (a, b), a == b == 38, (a, b))
ck('virgolette per unita, 6 nella 14', not [u for u in tu if u['english'].count('"') != u['italian'].count('"')]
   and [u['idx'] for u in su if u['english'].count('"') == 6] == [14])
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
ck('ripetizione inglese: 20/27', sorted(tuple(v) for v in grp.values() if len(v) > 1) == [(20, 27)])
ck('20/27 resa identica', by[20]['italian'] == by[27]['italian'])
merged = {}
for f in sorted(glob.glob(os.path.join(HERE, 'parts', 'part*.json'))):
    for kk, v in json.load(open(f, encoding='utf-8')).items():
        merged[int(kk)] = v
ck('le tre parti ricostruiscono translation.json (24 unita + 3 UI_LABEL)',
   sorted(merged) == [i for i in range(1, 28) if i not in NT]
   and {i: '\t' * (len(by[i]['english']) - len(by[i]['english'].lstrip('\t'))) + v
        for i, v in merged.items()} == {u['idx']: u['italian'] for u in tu if u['idx'] not in NT})
ids = [u['id'] for u in tu]
cov = db.execute('select count(*) from units where path=? and id in (%s)' % ','.join('?' * len(ids)),
                 [PATH] + ids).fetchone()[0]
ck('copertura del file: 94/157 (59,9%)', cov + 67 == 94, (cov + 67, 157))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('parole EN %d -> IT %d · sha256[:16] %s' % (sum(len(u['english'].split()) for u in tu),
      sum(len(u['italian'].split()) for u in tu), h[:16]))
print()
print('FAIL:', len(fail), '·', 'verify L95 superato' if not fail else 'verify L95 fallito')
raise SystemExit(0 if not fail else 1)
