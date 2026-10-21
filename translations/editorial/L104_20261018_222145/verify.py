r"""verify.py — L104 (data/quarg/quarg missions.txt, 27 unita', righe 250-334)

Invariante di **segmento**. Indipendente da `check.py`: rilegge il repository originale, `state.db` e i `parts/`.

Misure attese: **90 unita' prima** della riga 265 (L102 + L103), **61 dopo la 334**, file di **178 unita'**,
`max(line) = 506`, confine alla riga **356** (`Ask Quarg About Coalition Late`).
**27 `MISSION_TEXT`**, **24 tab**, **37 virgolette** con **cinque citazioni aperte** (5, 19, 22, 23, 24),
**0 token**, **0 quadre**, nessuna ripetizione. L'unita' **3** e' identica al sorgente per coincidenza
linguistica: `(No.)` = `(No.)`.
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
OPEN = [5, 19, 22, 23, 24]
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
ck('idx 1..27 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 28)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 27 righe 265 - 334', len(tu) == 27 and (first, last) == (265, 334), (len(tu), first, last))
tot = db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0]
before = db.execute('select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0]
after = db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0]
maxl = db.execute('select max(line) from units where path=?', (PATH,)).fetchone()[0]
ck('90 unita prima della riga 265 (L102 + L103)', before == 90, before)
ck('61 unita dopo la riga 334', after == 61, after)
ck('file: 178 unita, max(line) = 506', tot == 178 and maxl == 506, (tot, maxl))
ck('il confine: la riga 356 apre Ask Quarg About Coalition Late',
   db.execute('select line,context from units where path=? and line>? order by line limit 1',
              (PATH, last)).fetchone() == (356, 'mission:Ask Quarg About Coalition Late'))
ck('kind: 27 MISSION_TEXT, 0 UI_LABEL, 0 VALUE',
   collections.Counter(u['kind'] for u in su) == {'MISSION_TEXT': 27},
   collections.Counter(u['kind'] for u in su))
by = {u['idx']: u for u in tu}
ck('unica identica al sorgente: l\'unita 3, (No.) = (No.)',
   [u['idx'] for u in tu if u['italian'].strip() == u['english'].strip()] == [3]
   and by[3]['italian'].strip() == '(No.)',
   [u['idx'] for u in tu if u['italian'].strip() == u['english'].strip()])
ctxs = []
for u in su:
    if u['context'] not in ctxs:
        ctxs.append(u['context'])
ck('2 contesti in ordine di riga',
   len(ctxs) == 2 and [c.split(':', 1)[1] for c in ctxs]
   == ['Ask Quarg About Coalition Early', 'Quarg Pug Arfecta Warning'], ctxs)
TABS = [i for i in range(1, 28) if i not in (1, 12, 13)]
ck('tab: 24 nel sorgente, nelle unita attese',
   sum(1 for u in su if u['english'].startswith('\t')) == 24
   and [u['idx'] for u in tu if u['italian'].startswith('\t')] == TABS)
ck('nessun tab aggiunto', not [u for u in tu if u['english'].count('\t') != u['italian'].count('\t')])
a = sum(u['english'].count('"') for u in su)
b = sum(u['italian'].count('"') for u in tu)
ck('virgolette: %d = %d (37)' % (a, b), a == b == 37, (a, b))
ck('virgolette per unita', not [u for u in tu if u['english'].count('"') != u['italian'].count('"')])
ck('cinque citazioni aperte: 5, 19, 22, 23, 24',
   [u['idx'] for u in tu if u['italian'].count('"') % 2] == OPEN
   and [u['idx'] for u in su if u['english'].count('"') % 2] == OPEN)
ck('nessuna delle cinque chiude la citazione',
   all(not by[i]['italian'].rstrip().endswith('"') for i in OPEN))
ck('unita 23: trattino isolato, non em dash', ' - ' in by[23]['italian'] and '\u2014' not in by[23]['italian'])
te = [t for u in su for t in TAGS.findall(u['english'])]
ti = [t for u in tu for t in TAGS.findall(u['italian'])]
ck('zero token nel sorgente e nella resa', not te and not ti)
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
ck('nessuna ripetizione inglese nel segmento', [v for v in grp.values() if len(v) > 1] == [])
merged = {}
for f in sorted(glob.glob(os.path.join(HERE, 'parts', 'part*.json'))):
    for kk, v in json.load(open(f, encoding='utf-8')).items():
        merged[int(kk)] = v
ck('le due parti ricostruiscono translation.json (1..27)',
   sorted(merged) == list(range(1, 28))
   and {i: '\t' * (len(by[i]['english']) - len(by[i]['english'].lstrip('\t'))) + v
        for i, v in merged.items()} == {u['idx']: u['italian'] for u in tu})
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('parole EN %d -> IT %d · sha256[:16] %s' % (sum(len(u['english'].split()) for u in tu),
      sum(len(u['italian'].split()) for u in tu), h[:16]))
print()
print('FAIL:', len(fail), '·', 'verify L104 superato' if not fail else 'verify L104 fallito')
raise SystemExit(0 if not fail else 1)
