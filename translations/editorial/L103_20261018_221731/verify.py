r"""verify.py — L103 (data/quarg/quarg missions.txt, 42 unita', righe 118-249)

Invariante di **segmento**. Indipendente da `check.py`: rilegge il repository originale, `state.db` e i `parts/`.

Misure attese: **48 unita' prima** della riga 124 (L102), **88 dopo la 249**, file di **178 unita'**,
`max(line) = 506`, confine alla riga **265** (`Ask Quarg About Coalition Early`).
**28 `MISSION_TEXT` + 8 `DIALOG` + 3 `DESCRIPTION` + 3 `VALUE`** (i `VALUE` identici all'inglese), **25 tab**,
**43 virgolette** con **una citazione aperta** (unita' 30), **19 token** in sei famiglie, cinque ripetizioni.
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
VALUE = [1, 21, 39]
GROUPS = [(8, 12), (10, 13), (21, 39), (22, 40), (36, 41)]
FAM = {'<destination>': 4, '<stopovers>': 3, '<cargo>': 5, '<payment>': 5, '<waypoints>': 1, '<system>': 1}
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
ck('idx 1..42 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 43)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 42 righe 124 - 249', len(tu) == 42 and (first, last) == (124, 249), (len(tu), first, last))
tot = db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0]
before = db.execute('select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0]
after = db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0]
maxl = db.execute('select max(line) from units where path=?', (PATH,)).fetchone()[0]
ck('48 unita prima della riga 124 (L102)', before == 48, before)
ck('88 unita dopo la riga 249', after == 88, after)
ck('file: 178 unita, max(line) = 506', tot == 178 and maxl == 506, (tot, maxl))
ck('il confine: la riga 265 apre Ask Quarg About Coalition Early',
   db.execute('select line,context from units where path=? and line>? order by line limit 1',
              (PATH, last)).fetchone() == (265, 'mission:Ask Quarg About Coalition Early'))
ck('kind: 28 MISSION_TEXT + 8 DIALOG + 3 DESCRIPTION + 3 VALUE',
   collections.Counter(u['kind'] for u in su)
   == {'MISSION_TEXT': 28, 'DIALOG': 8, 'DESCRIPTION': 3, 'VALUE': 3},
   collections.Counter(u['kind'] for u in su))
by = {u['idx']: u for u in tu}
ck('i 3 VALUE restano identici all\'inglese',
   [u['idx'] for u in tu if u['italian'].strip() == u['english'].strip()] == VALUE
   and all(by[i]['kind'] == 'VALUE' for i in VALUE),
   [u['idx'] for u in tu if u['italian'].strip() == u['english'].strip()])
ck('DESCRIPTION e DIALOG tradotti', all(by[i]['italian'].strip() != by[i]['english'].strip()
   for i in (2, 22, 40, 16, 17, 18, 19, 20, 36, 41, 42)))
ctxs = []
for u in su:
    if u['context'] not in ctxs:
        ctxs.append(u['context'])
ck('3 contesti in ordine di riga',
   len(ctxs) == 3 and [c.split(':', 1)[1] for c in ctxs]
   == ['Quarg Satellites', 'Lagrange Ring: Cargo', 'Lagrange Ring: Cargo Job'], ctxs)
TABS = [i for i in range(1, 43) if i not in (1, 2, 3, 16, 17, 18, 19, 20, 21, 22, 23, 36, 37, 39, 40, 41, 42)]
ck('tab: 25 nel sorgente, nelle unita attese',
   sum(1 for u in su if u['english'].startswith('\t')) == 25
   and [u['idx'] for u in tu if u['italian'].startswith('\t')] == TABS)
ck('nessun tab aggiunto', not [u for u in tu if u['english'].count('\t') != u['italian'].count('\t')])
a = sum(u['english'].count('"') for u in su)
b = sum(u['italian'].count('"') for u in tu)
ck('virgolette: %d = %d (43)' % (a, b), a == b == 43, (a, b))
ck('virgolette per unita', not [u for u in tu if u['english'].count('"') != u['italian'].count('"')])
ck("l'unica virgoletta dispari e' nell'unita 30",
   [u['idx'] for u in tu if u['italian'].count('"') % 2] == [30]
   and [u['idx'] for u in su if u['english'].count('"') % 2] == [30])
ck('unita 30 finisce senza virgoletta',
   not tu[29]['italian'].rstrip().endswith('"'))
te = [t for u in su for t in TAGS.findall(u['english'])]
ti = [t for u in tu for t in TAGS.findall(u['italian'])]
ck('token: 19 = 19, sei famiglie', te == ti and collections.Counter(te) == FAM and len(te) == 19,
   (collections.Counter(te), collections.Counter(ti)))
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
ck('5 ripetizioni: 8/12, 10/13, 21/39, 22/40, 36/41',
   sorted(tuple(v) for v in grp.values() if len(v) > 1) == sorted(GROUPS))
ck('ogni gruppo reso identico', all(len({by[i]['italian'] for i in g}) == 1 for g in GROUPS))
merged = {}
for f in sorted(glob.glob(os.path.join(HERE, 'parts', 'part*.json'))):
    for kk, v in json.load(open(f, encoding='utf-8')).items():
        merged[int(kk)] = v
ck('le due parti ricostruiscono translation.json (1..42)',
   sorted(merged) == list(range(1, 43))
   and {i: '\t' * (len(by[i]['english']) - len(by[i]['english'].lstrip('\t'))) + v
        for i, v in merged.items()} == {u['idx']: u['italian'] for u in tu})
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('parole EN %d -> IT %d · sha256[:16] %s' % (sum(len(u['english'].split()) for u in tu),
      sum(len(u['italian'].split()) for u in tu), h[:16]))
print()
print('FAIL:', len(fail), '·', 'verify L103 superato' if not fail else 'verify L103 fallito')
raise SystemExit(0 if not fail else 1)
