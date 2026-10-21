r"""verify.py — L99 (data/hai/hai culture conversations.txt, 38 unita', righe 106-211)

Invariante di **segmento**. Indipendente da `check.py`: rilegge il repository originale, `state.db` e i `parts/`.

Misure attese: **39 unita' prima** della riga 119 (solo L98), **70 dopo la 211**, file di **147 unita'**,
`max(line) = 386`, confine alla riga **227** (`Academy Motto`). **34 tab**, **23 virgolette** (di cui **una
sola** nell'unita' 32: citazione aperta e non chiusa, voluta), **0 token**, **0 quadre**. **7 gruppi di
ripetizioni**.
"""
import collections, glob, hashlib, json, os, re, sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
ROOT = os.path.abspath(os.path.join(L10N, '..'))
PATH = 'data/hai/hai culture conversations.txt'
su = sorted(json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
TAGS = re.compile(r'<[^<>]+>')
GROUPS = [(1, 8, 15), (2, 9, 16), (3, 10, 17), (4, 11, 18), (6, 13), (7, 14, 21), (24, 27)]
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
ck('idx 1..38 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 39)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 38 righe 119 - 211', len(tu) == 38 and (first, last) == (119, 211), (len(tu), first, last))
tot = db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0]
before = db.execute('select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0]
after = db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0]
maxl = db.execute('select max(line) from units where path=?', (PATH,)).fetchone()[0]
ck('39 unita prima della riga 119 (solo L98)', before == 39, before)
ck('70 unita dopo la riga 211', after == 70, after)
ck('file: 147 unita, max(line) = 386', tot == 147 and maxl == 386, (tot, maxl))
ck('il confine: la riga 227 apre Academy Motto',
   db.execute('select line,context from units where path=? and line>? order by line limit 1',
              (PATH, last)).fetchone() == (227, 'mission:Academy Motto'))
ck('kind: 38 MISSION_TEXT, 0 UI_LABEL',
   collections.Counter(u['kind'] for u in su) == {'MISSION_TEXT': 38}
   and not [u for u in tu if u['kind'] == 'UI_LABEL'])
ck('tutte tradotte', all(u['italian'].strip() != u['english'].strip() for u in tu))
ctxs = []
for u in su:
    if u['context'] not in ctxs:
        ctxs.append(u['context'])
ck('4 contesti in ordine di riga',
   len(ctxs) == 4 and [c.split(':', 1)[1] for c in ctxs]
   == ['Wrestling Star', 'Fencing Star', 'Mystery Sport Star', 'Gambling Judgment'], ctxs)
TABS = [i for i in range(1, 39) if i not in (1, 8, 15, 22)]
ck('tab: 34 nel sorgente, nelle unita attese',
   sum(1 for u in su if u['english'].startswith('\t')) == 34
   and [u['idx'] for u in tu if u['italian'].startswith('\t')] == TABS)
ck('nessun tab aggiunto', not [u for u in tu if u['english'].count('\t') != u['italian'].count('\t')])
a = sum(u['english'].count('"') for u in su)
b = sum(u['italian'].count('"') for u in tu)
ck('virgolette: %d = %d (23)' % (a, b), a == b == 23, (a, b))
ck('virgolette per unita', not [u for u in tu if u['english'].count('"') != u['italian'].count('"')])
ck("l'unica virgoletta dispari e' nell'unita 32 (voluta)",
   [u['idx'] for u in tu if u['italian'].count('"') % 2] == [32]
   and [u['idx'] for u in su if u['english'].count('"') % 2] == [32])
ck('unita 32: citazione aperta e non chiusa',
   tu[31]['italian'].count('"') == 1 and tu[31]['italian'].rstrip().endswith('adulto.'))
ck('zero token nel sorgente e nella resa',
   not [t for u in su for t in TAGS.findall(u['english'])]
   and not [t for u in tu for t in TAGS.findall(u['italian'])])
ck('zero quadre', not [u for u in tu if any(c in u['italian'] for c in '[]')])
ck('nessun backtick', not [u for u in tu if '`' in u['italian']])
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
ck('7 gruppi di ripetizioni, come misurati',
   sorted(tuple(v) for v in grp.values() if len(v) > 1) == sorted(GROUPS))
ck('ogni gruppo reso identico', all(len({by[i]['italian'] for i in g}) == 1 for g in GROUPS))
merged = {}
for f in sorted(glob.glob(os.path.join(HERE, 'parts', 'part*.json'))):
    for kk, v in json.load(open(f, encoding='utf-8')).items():
        merged[int(kk)] = v
ck('le tre parti ricostruiscono translation.json (1..38)',
   sorted(merged) == list(range(1, 39))
   and {i: '\t' * (len(by[i]['english']) - len(by[i]['english'].lstrip('\t'))) + v
        for i, v in merged.items()} == {u['idx']: u['italian'] for u in tu})
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('parole EN %d -> IT %d · sha256[:16] %s' % (sum(len(u['english'].split()) for u in tu),
      sum(len(u['italian'].split()) for u in tu), h[:16]))
print()
print('FAIL:', len(fail), '·', 'verify L99 superato' if not fail else 'verify L99 fallito')
raise SystemExit(0 if not fail else 1)
