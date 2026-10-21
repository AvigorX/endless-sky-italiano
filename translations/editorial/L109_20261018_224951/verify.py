r"""verify.py — L109 (data/korath/korath missions.txt, 33 unita', righe 338-451)

Invariante di **segmento**, indipendente da `check.py`: rilegge il repository originale, `state.db` e i `parts/`.

Misure attese: **99 unita' prima** della riga 338 (L106+L107+L108), **26 dopo la 451**, file di **158 unita'**,
`max(line) = 580`, confine alla riga **474** (`mission:Efreti: Distress Call 6`). **Quattro contesti** in ordine di
riga. **27 `MISSION_TEXT` + 3 `VALUE` + 3 `DESCRIPTION`**, **20 tab**, **14 virgolette**, **23 token** in sette
famiglie, zero quadre, zero ripetizioni. **`<origin>` = partenza, `<destination>` = arrivo.**
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
VALS = [4, 16, 29]
NOTAB = [1, 4, 5, 6, 16, 17, 18, 19, 26, 29, 30, 31, 32]
TABS = [i for i in range(1, 34) if i not in NOTAB]
FAM = {'<EDC-ship>': 11, '<destination>': 4, '<origin>': 2, '<planet>': 2, '<bunks>': 2, '<ship>': 1, '<payment>': 1}
CTX = ['mission:Efreti: Distress Call 2', 'mission:Efreti: Distress Call 3',
       'mission:Efreti: Distress Call 4', 'mission:Efreti: Distress Call 5']
fail = []


def ck(n, c, d=''):
    print('%-70s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
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
ck('idx 1..33 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 34)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 33 righe 338 - 451', len(tu) == 33 and (first, last) == (338, 451), (len(tu), first, last))
tot = db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0]
before = db.execute('select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0]
after = db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0]
maxl = db.execute('select max(line) from units where path=?', (PATH,)).fetchone()[0]
ck('99 unita prima della riga 338 (L106+L107+L108)', before == 99, before)
ck('26 unita dopo la riga 451', after == 26, after)
ck('file: 158 unita, max(line) = 580', tot == 158 and maxl == 580, (tot, maxl))
ck('il confine: la riga 474 apre Distress Call 6',
   db.execute('select line,context from units where path=? and line>? order by line limit 1',
              (PATH, last)).fetchone() == (474, 'mission:Efreti: Distress Call 6'))
ck('0 sovrapposizioni con le righe 1-335', db.execute(
   'select count(*) from units where path=? and line<=? and line>=?', (PATH, 1, 335)).fetchone()[0] == 0)
ck('kind: 27 MISSION_TEXT + 3 VALUE + 3 DESCRIPTION',
   collections.Counter(u['kind'] for u in su) == {'MISSION_TEXT': 27, 'VALUE': 3, 'DESCRIPTION': 3},
   collections.Counter(u['kind'] for u in su))
by = {u['idx']: u for u in tu}
ck('i tre VALUE restano identici',
   [u['idx'] for u in tu if u['italian'].strip() == u['english'].strip()] == VALS
   and by[4]['italian'].strip() == 'Recover the fallen crew of the <EDC-ship>'
   and by[16]['italian'].strip() == 'Recover the fallen of <EDC-ship>'
   and by[29]['italian'].strip() == '<EDC-ship> salvage team')
ck('le tre DESCRIPTION sono tradotte',
   all(by[i]['italian'].strip() != by[i]['english'].strip() for i in (5, 17, 30)))
ck('nessuno scambio fra <origin> e <destination>', all(
   u['italian'].count('<origin>') == u['english'].count('<origin>')
   and u['italian'].count('<destination>') == u['english'].count('<destination>') for u in tu))
ck('unita 5: <EDC-ship>, <destination>, <origin> in quest ordine',
   TAGS.findall(by[5]['italian']) == ['<EDC-ship>', '<destination>', '<origin>'])
ck('unita 8: <planet> e <origin>', TAGS.findall(by[8]['italian']) == ['<planet>', '<origin>'])
ck('<bunks> in 30 e 31, con ruoli diversi',
   TAGS.findall(by[30]['italian'])[0] == '<bunks>' and TAGS.findall(by[31]['italian']) == ['<bunks>'])
ctxs = []
for u in su:
    if u['context'] not in ctxs:
        ctxs.append(u['context'])
ck('4 contesti in ordine di riga', ctxs == CTX, ctxs)
ck('tab: 20 nel sorgente, nelle unita attese',
   sum(1 for u in su if u['english'].startswith('\t')) == 20
   and [u['idx'] for u in tu if u['italian'].startswith('\t')] == TABS)
ck('nessun tab aggiunto', not [u for u in tu if u['english'].count('\t') != u['italian'].count('\t')])
a = sum(u['english'].count('"') for u in su)
b = sum(u['italian'].count('"') for u in tu)
ck('virgolette: %d = %d (14)' % (a, b), a == b == 14, (a, b))
ck('virgolette per unita', not [u for u in tu if u['english'].count('"') != u['italian'].count('"')])
ck('ZERO citazioni aperte (asserito vuoto)', not [u['idx'] for u in tu if u['italian'].count('"') % 2])
ck('ZERO quadre (asserito vuoto)', not [u['idx'] for u in tu if '[' in u['italian'] or ']' in u['italian']])
te = [t for u in su for t in TAGS.findall(u['english'])]
ti = [t for u in tu for t in TAGS.findall(u['italian'])]
ck('token: 23 = 23, sette famiglie', te == ti and collections.Counter(te) == FAM and len(te) == 23,
   (len(te), collections.Counter(te), collections.Counter(ti)))
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
ck('ZERO ripetizioni (asserito vuoto)', not [v for v in grp.values() if len(v) > 1])
ck('i tre quasi-duplicati restano distinti', len({by[20]['italian'], by[21]['italian'],
   by[22]['italian']}) == 3 and len({by[18]['italian'], by[19]['italian']}) == 2
   and len({by[24]['italian'], by[25]['italian']}) == 2)
merged = {}
for f in sorted(glob.glob(os.path.join(HERE, 'parts', 'part*.json'))):
    for kk, v in json.load(open(f, encoding='utf-8')).items():
        merged[int(kk)] = v
ck('le due parti ricostruiscono translation.json (1..33)',
   sorted(merged) == list(range(1, 34))
   and {i: '\t' * (len(by[i]['english']) - len(by[i]['english'].lstrip('\t'))) + v
        for i, v in merged.items()} == {u['idx']: u['italian'] for u in tu})
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('parole EN %d -> IT %d · sha256[:16] %s' % (sum(len(u['english'].split()) for u in tu),
      sum(len(u['italian'].split()) for u in tu), h[:16]))
print()
print('FAIL:', len(fail), '·', 'verify L109 superato' if not fail else 'verify L109 fallito')
raise SystemExit(0 if not fail else 1)
