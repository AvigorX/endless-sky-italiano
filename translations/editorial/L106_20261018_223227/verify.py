r"""verify.py — L106 (data/korath/korath missions.txt, 25 unita', righe 1-120)

Primo lotto del file: invariante di **segmento**. Indipendente da `check.py`: rilegge il repository originale,
`state.db` e i `parts/`.

Misure attese: **0 unita' prima** della riga 21, **133 dopo la 119**, file di **158 unita'**, `max(line) = 580`,
confine alla riga **126** (`Setar Fort Heating`). **Sei contesti** in ordine di riga.
**22 `MISSION_TEXT` + 1 `LOGBOOK` + 1 `VALUE` (identico) + 1 `DESCRIPTION`**, **17 tab**, **45 virgolette** con
**una citazione aperta** (unita' 16), **13 token**, **16 coppie di quadre** (voce dei Wanderer), due ripetizioni.
"""
import collections, glob, hashlib, json, os, re, sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
ROOT = os.path.abspath(os.path.join(L10N, '..'))
PATH = 'data/korath/korath missions.txt'
su = sorted(json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
TAGS = re.compile(r'<[^<>]+>')
BR = {11: 3, 16: 7, 17: 1, 20: 4, 25: 1}
GROUPS = [(2, 3, 4), (15, 19)]
FAM = {'<planet>': 4, '<payment>': 4, '<last>': 2, '<cargo>': 1, '<destination>': 1, '<tons>': 1}
CTX = ['mission:First Contact: Korati Efreti', 'mission:First Contact: Laki Nemparu',
       'mission:First Contact: Karek Fornati', 'mission:First Contact: Setar Fort',
       'mission:Discovered Korath Space', 'mission:Setar Fort Heating']
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
ck('idx 1..25 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 26)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 25 righe 21 - 119', len(tu) == 25 and (first, last) == (21, 119), (len(tu), first, last))
tot = db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0]
before = db.execute('select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0]
after = db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0]
maxl = db.execute('select max(line) from units where path=?', (PATH,)).fetchone()[0]
ck('0 unita prima della riga 21 (primo lotto del file)', before == 0, before)
ck('133 unita dopo la riga 119', after == 133, after)
ck('file: 158 unita, max(line) = 580', tot == 158 and maxl == 580, (tot, maxl))
ck('il confine: la riga 126 apre Setar Fort Heating',
   db.execute('select line,context from units where path=? and line>? order by line limit 1',
              (PATH, last)).fetchone() == (126, 'mission:Setar Fort Heating'))
ck('kind: 22 MISSION_TEXT + 1 LOGBOOK + 1 VALUE + 1 DESCRIPTION',
   collections.Counter(u['kind'] for u in su) == {'MISSION_TEXT': 22, 'LOGBOOK': 1, 'VALUE': 1, 'DESCRIPTION': 1},
   collections.Counter(u['kind'] for u in su))
by = {u['idx']: u for u in tu}
ck('il VALUE resta identico: Supplies to <planet>',
   by[6]['italian'].strip() == by[6]['english'].strip() == 'Supplies to <planet>'
   and [u['idx'] for u in tu if u['italian'].strip() == u['english'].strip()] == [6],
   [u['idx'] for u in tu if u['italian'].strip() == u['english'].strip()])
ck('LOGBOOK e DESCRIPTION tradotti',
   by[5]['italian'] != by[5]['english'] and by[7]['italian'] != by[7]['english'])
ctxs = []
for u in su:
    if u['context'] not in ctxs:
        ctxs.append(u['context'])
ck('6 contesti in ordine di riga', ctxs == CTX, ctxs)
TABS = [i for i in range(1, 26) if i not in (1, 2, 3, 4, 5, 6, 7, 8)]
ck('tab: 17 nel sorgente, nelle unita attese',
   sum(1 for u in su if u['english'].startswith('\t')) == 17
   and [u['idx'] for u in tu if u['italian'].startswith('\t')] == TABS)
ck('nessun tab aggiunto', not [u for u in tu if u['english'].count('\t') != u['italian'].count('\t')])
a = sum(u['english'].count('"') for u in su)
b = sum(u['italian'].count('"') for u in tu)
ck('virgolette: %d = %d (45)' % (a, b), a == b == 45, (a, b))
ck('virgolette per unita', not [u for u in tu if u['english'].count('"') != u['italian'].count('"')])
ck("l'unica citazione aperta e' l'unita 16",
   [u['idx'] for u in tu if u['italian'].count('"') % 2] == [16]
   and [u['idx'] for u in su if u['english'].count('"') % 2] == [16])
ck('quadre: 16 coppie, per unita, tutte bilanciate',
   {i: by[i]['italian'].count('[') for i in BR} == BR
   and sum(u['italian'].count('[') for u in tu) == 16
   and sum(u['italian'].count(']') for u in tu) == 16)
ck('ogni coppia contiene due alternative',
   all(',' in f or '?' in f for i in BR for f in re.findall(r'\[([^\]]*)\]', by[i]['italian'])))
te = [t for u in su for t in TAGS.findall(u['english'])]
ti = [t for u in tu for t in TAGS.findall(u['italian'])]
ck('token: 13 = 13, sei famiglie', te == ti and collections.Counter(te) == FAM and len(te) == 13,
   (collections.Counter(te), collections.Counter(ti)))
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
ck('2 ripetizioni: 2/3/4 e 15/19',
   sorted(tuple(v) for v in grp.values() if len(v) > 1) == sorted(GROUPS))
ck('ogni gruppo reso identico', all(len({by[i]['italian'] for i in g}) == 1 for g in GROUPS))
merged = {}
for f in sorted(glob.glob(os.path.join(HERE, 'parts', 'part*.json'))):
    for kk, v in json.load(open(f, encoding='utf-8')).items():
        merged[int(kk)] = v
ck('le due parti ricostruiscono translation.json (1..25)',
   sorted(merged) == list(range(1, 26))
   and {i: '\t' * (len(by[i]['english']) - len(by[i]['english'].lstrip('\t'))) + v
        for i, v in merged.items()} == {u['idx']: u['italian'] for u in tu})
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('parole EN %d -> IT %d · sha256[:16] %s' % (sum(len(u['english'].split()) for u in tu),
      sum(len(u['italian'].split()) for u in tu), h[:16]))
print()
print('FAIL:', len(fail), '·', 'verify L106 superato' if not fail else 'verify L106 fallito')
raise SystemExit(0 if not fail else 1)
