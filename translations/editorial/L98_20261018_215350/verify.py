r"""verify.py — L98 (data/hai/hai culture conversations.txt, 39 unita', righe 1-105)

Primo lotto del file: invariante di **segmento** (non di file). Indipendente da `check.py`: rilegge il
repository originale, `state.db` e i `parts/`.

Misure attese: **0 unita' prima** della riga 26 (nessun lotto precedente su questo file), **108 dopo la 105**,
file di **147 unita'**, `max(line) = 386`, confine alla riga **119** (`Wrestling Star`), 3 contesti in ordine di
riga. **36 tab**, **58 virgolette**, **1 token** `<destination>`, **6 quadre** (3 coppie) nell'unita' 30.
Ripetizioni 20/37, 27/31, 29/39; 28 e 32 differiscono per una virgola.
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
ck('idx 1..39 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 40)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 39 righe 26 - 105', len(tu) == 39 and (first, last) == (26, 105), (len(tu), first, last))
tot = db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0]
before = db.execute('select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0]
after = db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0]
maxl = db.execute('select max(line) from units where path=?', (PATH,)).fetchone()[0]
ck('0 unita prima della riga 26 (primo lotto del file)', before == 0, before)
ck('108 unita dopo la riga 105', after == 108, after)
ck('file: 147 unita, max(line) = 386', tot == 147 and maxl == 386, (tot, maxl))
ck('il confine: la riga 119 apre Wrestling Star',
   db.execute('select line,context from units where path=? and line>? order by line limit 1',
              (PATH, last)).fetchone() == (119, 'mission:Wrestling Star'))
ck('kind: 39 MISSION_TEXT, 0 UI_LABEL',
   collections.Counter(u['kind'] for u in su) == {'MISSION_TEXT': 39}
   and not [u for u in tu if u['kind'] == 'UI_LABEL'])
ck('tutte tradotte', all(u['italian'].strip() != u['english'].strip() for u in tu))
ctxs = []
for u in su:
    if u['context'] not in ctxs:
        ctxs.append(u['context'])
ck('3 contesti in ordine di riga',
   len(ctxs) == 3 and [c.split(':', 1)[1] for c in ctxs]
   == ['Theater Chat', 'Musical Entertainment Expo', 'The Meme Wars 1'], ctxs)
TABS = [i for i in range(1, 40) if i not in (1, 9, 25)]
ck('tab: 36 nel sorgente, nelle unita attese',
   sum(1 for u in su if u['english'].startswith('\t')) == 36
   and [u['idx'] for u in tu if u['italian'].startswith('\t')] == TABS,
   [u['idx'] for u in tu if u['italian'].startswith('\t')])
ck('nessun tab aggiunto', not [u for u in tu if u['english'].count('\t') != u['italian'].count('\t')])
a = sum(u['english'].count('"') for u in su)
b = sum(u['italian'].count('"') for u in tu)
ck('virgolette: %d = %d (58)' % (a, b), a == b == 58, (a, b))
ck('virgolette per unita', not [u for u in tu if u['english'].count('"') != u['italian'].count('"')])
ck('nessuna virgoletta dispari', not [u for u in tu if u['italian'].count('"') % 2])
te = [t for u in su for t in TAGS.findall(u['english'])]
ti = [t for u in tu for t in TAGS.findall(u['italian'])]
ck('token: 1 = 1, <destination> nell\'unita 7',
   te == ti == ['<destination>'] and any('<destination>' in u['italian'] for u in tu if u['idx'] == 7))
ck('quadre: 3 = 3, solo nell\'unita 30',
   sum(u['english'].count('[') for u in su) == sum(u['italian'].count('[') for u in tu) == 3
   and sum(u['english'].count(']') for u in su) == sum(u['italian'].count(']') for u in tu) == 3
   and [u['idx'] for u in tu if '[' in u['italian']] == [30])
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
ck('3 ripetizioni: 20/37, 27/31, 29/39',
   sorted(tuple(v) for v in grp.values() if len(v) > 1) == [(20, 37), (27, 31), (29, 39)])
ck('ogni gruppo reso identico',
   by[20]['italian'] == by[37]['italian'] and by[27]['italian'] == by[31]['italian']
   and by[29]['italian'] == by[39]['italian'])
ck('28 e 32 differiscono per una virgola',
   by[32]['italian'].count(',') == by[28]['italian'].count(',') + 1)
merged = {}
for f in sorted(glob.glob(os.path.join(HERE, 'parts', 'part*.json'))):
    for kk, v in json.load(open(f, encoding='utf-8')).items():
        merged[int(kk)] = v
ck('le due parti ricostruiscono translation.json (1..39)',
   sorted(merged) == list(range(1, 40))
   and {i: '\t' * (len(by[i]['english']) - len(by[i]['english'].lstrip('\t'))) + v
        for i, v in merged.items()} == {u['idx']: u['italian'] for u in tu})
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('parole EN %d -> IT %d · sha256[:16] %s' % (sum(len(u['english'].split()) for u in tu),
      sum(len(u['italian'].split()) for u in tu), h[:16]))
print()
print('FAIL:', len(fail), '·', 'verify L98 superato' if not fail else 'verify L98 fallito')
raise SystemExit(0 if not fail else 1)
