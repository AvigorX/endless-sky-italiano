r"""verify.py — L91 (data/successors/successor culture conversations.txt, 34 unita', righe 155-229)

Indipendente da `check.py`: rilegge il repository originale, `state.db` e `translation.json`, e verifica il
**segmento**, non la copertura. Segmento: **34 prima** (L90, righe 23-142), **46 dopo**, file di **114**,
`max(line) = 351`. Confine dichiarato: la prima unita' dopo la 229 e' la riga 230, contesto
`mission:Successors: Stage Play`.

Misure attese: 33 `MISSION_TEXT` + 1 `UI_LABEL` (`myiara system`, idx 29, **identica**), 30 tab,
60 virgolette (4 unita' con 4 virgolette: 19, 27, 31, 34), 5 token (4 `<ship>`, 1 `<origin>`),
3 coppie di inglese identico (8/12, 9/13, 10/14).
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
NT = [29]
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
ck('idx 1..34 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 35)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 34 righe 155 - 229', len(tu) == 34 and (first, last) == (155, 229), (len(tu), first, last))
tot = db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0]
before = db.execute('select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0]
after = db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0]
maxl = db.execute('select max(line) from units where path=?', (PATH,)).fetchone()[0]
ck('34 unita prima della riga 155 (L90)', before == 34, before)
ck('46 unita dopo la riga 229 (restano a L92)', after == 46, after)
ck('file: 114 unita, max(line) = 351', tot == 114 and maxl == 351, (tot, maxl))
nxt = db.execute('select line,context from units where path=? and line>? order by line limit 1', (PATH, last)).fetchone()
ck('confine: riga 230 apre Stage Play', nxt is not None
   and tuple(nxt) == (230, 'mission:Successors: Stage Play'), tuple(nxt) if nxt else None)
prev = db.execute('select line,context from units where path=? and line<? order by line desc limit 1', (PATH, first)).fetchone()
ck('inizio: la precedente e la 142 (Buskers)', prev is not None
   and tuple(prev) == (142, 'mission:Successors: Buskers'), tuple(prev) if prev else None)
ck('kind: 33 MISSION_TEXT + 1 UI_LABEL',
   collections.Counter(u['kind'] for u in su) == {'MISSION_TEXT': 33, 'UI_LABEL': 1})
by = {u['idx']: u for u in tu}
ck('UI_LABEL idx 29 identica al sorgente', [u['idx'] for u in tu if u['kind'] == 'UI_LABEL'] == NT
   and by[29]['italian'] == by[29]['english'] == 'myiara system', by[29]['italian'])
ck('le altre 33 sono tradotte',
   all(u['italian'].strip() != u['english'].strip() for u in tu if u['idx'] not in NT),
   [u['idx'] for u in tu if u['idx'] not in NT and u['italian'].strip() == u['english'].strip()])
ctxs = []
for u in su:
    if u['context'] not in ctxs:
        ctxs.append(u['context'])
ck('2 contesti in ordine di riga', len(ctxs) == 2 and ctxs[0].endswith('Graffiti')
   and ctxs[-1].endswith('Stage Play'), (len(ctxs), ctxs[0], ctxs[-1]))
TABS = list(range(2, 28)) + [31, 32, 33, 34]
ck('tab: 30 nel sorgente, nelle unita attese',
   sum(1 for u in su if u['english'].startswith('\t')) == 30
   and [u['idx'] for u in tu if u['italian'].startswith('\t')] == TABS,
   [u['idx'] for u in tu if u['italian'].startswith('\t')])
ck('nessun tab aggiunto', not [u for u in tu if u['english'].count('\t') != u['italian'].count('\t')])
a = sum(u['english'].count('"') for u in su)
b = sum(u['italian'].count('"') for u in tu)
ck('virgolette: %d = %d (60)' % (a, b), a == b == 60, (a, b))
ck('virgolette per unita: 4 nelle unita 19, 27, 31, 34',
   [u['idx'] for u in su if u['english'].count('"') == 4] == [19, 27, 31, 34]
   and not [u for u in tu if u['english'].count('"') != u['italian'].count('"')])
ck('nessuna virgoletta dispari', not [u for u in tu if u['italian'].count('"') % 2])
te = [t for u in su for t in TAGS.findall(u['english'])]
ti = [t for u in tu for t in TAGS.findall(u['italian'])]
ck('token: 5 = 5 e per unita', te == ti and te.count('<ship>') == 4 and te.count('<origin>') == 1, (te, ti))
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
ck('ripetizioni inglesi: 8/12, 9/13, 10/14',
   sorted(tuple(v) for v in grp.values() if len(v) > 1) == [(8, 12), (9, 13), (10, 14)])
ck('le tre coppie hanno resa identica',
   all(by[x]['italian'] == by[y]['italian'] for x, y in ((8, 12), (9, 13), (10, 14))))
merged = {}
for f in sorted(glob.glob(os.path.join(HERE, 'parts', 'part*.json'))):
    for kk, v in json.load(open(f, encoding='utf-8')).items():
        merged[int(kk)] = v
ck('le due parti ricostruiscono translation.json (33 unita + UI_LABEL)',
   sorted(merged) == [i for i in range(1, 35) if i not in NT]
   and {i: '\t' * (len(by[i]['english']) - len(by[i]['english'].lstrip('\t'))) + v
        for i, v in merged.items()} == {u['idx']: u['italian'] for u in tu if u['idx'] not in NT})
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('parole EN %d -> IT %d · sha256[:16] %s' % (sum(len(u['english'].split()) for u in tu),
      sum(len(u['italian'].split()) for u in tu), h[:16]))
print()
print('FAIL:', len(fail), '·', 'verify L91 superato' if not fail else 'verify L91 fallito')
raise SystemExit(0 if not fail else 1)
