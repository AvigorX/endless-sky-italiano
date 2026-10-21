r"""verify.py — L107 (data/korath/korath missions.txt, 38 unita', righe 121-212)

Invariante di **segmento**, indipendente da `check.py`: rilegge il repository originale, `state.db` e i
`parts/`.

Misure attese: **25 unita' prima** della riga 126 (L106), **95 dopo la 212**, file di **158 unita'**,
`max(line) = 580`, confine alla riga **216** (`phrase:kor efret small package offer`). Tre contesti in ordine di
riga. **34 `MISSION_TEXT` + 2 `VALUE` (identici) + 2 `DESCRIPTION` (tradotte)**, **29 tab**, **20 virgolette**
tutte binate, **zero quadre**, **21 token** in sei famiglie (`<bunks>` distinto da `<tons>`), zero ripetizioni.
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
VALS = [3, 20]
DESC = [4, 21]
NOTAB = [1, 3, 4, 5, 14, 20, 21, 22, 37]
TABS = [i for i in range(1, 39) if i not in NOTAB]
FAM = {'<planet>': 12, '<bunks>': 3, '<payment>': 2, '<destination>': 2, '<cargo>': 1, '<tons>': 1}
CTX = ['mission:Setar Fort Heating', 'mission:Korath Family to Ringworld', 'mission:Korath Livestock']
fail = []


def ck(n, c, d=''):
    print('%-66s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
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
ck('unita: 38 righe 126 - 212', len(tu) == 38 and (first, last) == (126, 212), (len(tu), first, last))
tot = db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0]
before = db.execute('select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0]
after = db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0]
maxl = db.execute('select max(line) from units where path=?', (PATH,)).fetchone()[0]
ck('25 unita prima della riga 126 (solo L106)', before == 25, before)
ck('95 unita dopo la riga 212', after == 95, after)
ck('file: 158 unita, max(line) = 580', tot == 158 and maxl == 580, (tot, maxl))
ck('il confine: la riga 216 apre un phrase:',
   db.execute('select line,context from units where path=? and line>? order by line limit 1',
              (PATH, last)).fetchone() == (216, 'phrase:kor efret small package offer'))
ck('0 sovrapposizioni con L106', db.execute(
   'select count(*) from units where path=? and line<=? and line>=?', (PATH, 1, 120)).fetchone()[0] == 0)
ck('kind: 34 MISSION_TEXT + 2 VALUE + 2 DESCRIPTION',
   collections.Counter(u['kind'] for u in su) == {'MISSION_TEXT': 34, 'VALUE': 2, 'DESCRIPTION': 2},
   collections.Counter(u['kind'] for u in su))
by = {u['idx']: u for u in tu}
ck('i due VALUE restano identici',
   by[3]['italian'].strip() == 'Korath to <planet>' and by[20]['italian'].strip() == 'Livestock to <planet>'
   and [u['idx'] for u in tu if u['italian'].strip() == u['english'].strip() and u['kind'] == 'VALUE'] == VALS)
ck('le due DESCRIPTION sono tradotte',
   all(by[i]['italian'].strip() != by[i]['english'].strip() for i in DESC))
ck('unica altra unita identica: la 10 `(No.)`',
   [u['idx'] for u in tu if u['italian'].strip() == u['english'].strip()] == sorted(VALS + [10]))
ctxs = []
for u in su:
    if u['context'] not in ctxs:
        ctxs.append(u['context'])
ck('3 contesti in ordine di riga', ctxs == CTX, ctxs)
ck('tab: 29 nel sorgente, nelle unita attese',
   sum(1 for u in su if u['english'].startswith('\t')) == 29
   and [u['idx'] for u in tu if u['italian'].startswith('\t')] == TABS,
   (sum(1 for u in su if u['english'].startswith('\t')), [u['idx'] for u in tu if u['italian'].startswith('\t')]))
ck('nessun tab aggiunto', not [u for u in tu if u['english'].count('\t') != u['italian'].count('\t')])
a = sum(u['english'].count('"') for u in su)
b = sum(u['italian'].count('"') for u in tu)
ck('virgolette: %d = %d (20)' % (a, b), a == b == 20, (a, b))
ck('virgolette per unita', not [u for u in tu if u['english'].count('"') != u['italian'].count('"')])
ck('ZERO citazioni aperte (asserito vuoto)',
   not [u['idx'] for u in tu if u['italian'].count('"') % 2]
   and not [u['idx'] for u in su if u['english'].count('"') % 2])
ck('ZERO quadre (asserito vuoto)', not [u['idx'] for u in tu if '[' in u['italian'] or ']' in u['italian']])
te = [t for u in su for t in TAGS.findall(u['english'])]
ti = [t for u in tu for t in TAGS.findall(u['italian'])]
ck('token: 21 = 21, sei famiglie', te == ti and collections.Counter(te) == FAM and len(te) == 21,
   (len(te), collections.Counter(te), collections.Counter(ti)))
ck('<bunks> in 4, 21, 31 e mai in unita di <tons>',
   [u['idx'] for u in tu if '<bunks>' in u['italian']] == [4, 21, 31]
   and [u['idx'] for u in tu if '<tons>' in u['italian']] == [31])
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
merged = {}
for f in sorted(glob.glob(os.path.join(HERE, 'parts', 'part*.json'))):
    for kk, v in json.load(open(f, encoding='utf-8')).items():
        merged[int(kk)] = v
ck('le due parti ricostruiscono translation.json (1..38)',
   sorted(merged) == list(range(1, 39))
   and {i: '\t' * (len(by[i]['english']) - len(by[i]['english'].lstrip('\t'))) + v
        for i, v in merged.items()} == {u['idx']: u['italian'] for u in tu})
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('parole EN %d -> IT %d · sha256[:16] %s' % (sum(len(u['english'].split()) for u in tu),
      sum(len(u['italian'].split()) for u in tu), h[:16]))
print()
print('FAIL:', len(fail), '·', 'verify L107 superato' if not fail else 'verify L107 fallito')
raise SystemExit(0 if not fail else 1)
