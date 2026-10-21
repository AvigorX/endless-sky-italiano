r"""verify.py — L110 (data/korath/korath missions.txt, 26 unita', righe 474-580) — CHIUDE il file

**Invariante di file**, indipendente da `check.py`: rilegge il repository originale, `state.db`, i `parts/` e i
`translation.json` di **tutti** i lotti del file.

Misure attese: **132 unita' prima** della riga 474 (L106+L107+L108+L109), **0 dopo la 580**, file di **158 unita'**,
`max(line) = 580`. I cinque lotti (25 + 38 + 36 + 33 + 26) devono **coprire il file senza sovrapposizioni**, con
`id` distinti: è la prova che il file è **completo**. Tre contesti in ordine di riga, **2 ripetizioni** (1/4, 2/5)
rese identiche, **19 token** in sette famiglie, **8 virgolette**, **17 tab**.
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
VALS = [1, 4]
DESC = [2, 5]
GROUPS = [(1, 4), (2, 5)]
NOTAB = [1, 2, 3, 4, 5, 6, 11, 12, 20]
TABS = [i for i in range(1, 27) if i not in NOTAB]
FAM = {'<EDC-ship>': 12, '<planet>': 2, '<bunks>': 1, '<ship>': 1, '<destination>': 1, '<first>': 1, '<last>': 1}
CTX = ['mission:Efreti: Distress Call 6', 'mission:Efreti: Distress Call 7', 'mission:Efreti: Distress Call 8']
LOTS = [25, 38, 36, 33, 26]          # L106, L107, L108, L109, L110
fail = []


def ck(n, c, d=''):
    print('%-72s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
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
ck('idx 1..26 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 27)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 26 righe 474 - 580', len(tu) == 26 and (first, last) == (474, 580), (len(tu), first, last))
tot = db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0]
before = db.execute('select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0]
after = db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0]
maxl = db.execute('select max(line) from units where path=?', (PATH,)).fetchone()[0]
ck('132 unita prima della riga 474 (L106+L107+L108+L109)', before == 132, before)
ck('0 unita dopo la riga 580: il lotto chiude il file', after == 0, after)
ck('file: 158 unita, max(line) = 580', tot == 158 and maxl == 580, (tot, maxl))
ck('nessuna unita dopo l ultima riga del file', last == maxl)
# --- invariante di file: i cinque lotti coprono il file senza buchi ne' sovrapposizioni -------
ids = [u['id'] for u in su]
lot_ids = set(ids)
covered = []
for d in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L1*'))):
    f = os.path.join(d, 'translation.json')
    if not os.path.exists(f):
        continue
    try:
        us = json.load(open(f, encoding='utf-8'))['units']
    except Exception:
        continue
    mine = [u for u in us if u.get('path') == PATH]
    if mine:
        covered.append((os.path.basename(d), len(mine), [u['idx'] for u in mine]))
ck('cinque lotti su questo file', len(covered) == 5 and [c[1] for c in covered] == LOTS,
   [(c[0], c[1]) for c in covered])
allids = [u['id'] for _n, _k, us in covered for u in
          json.load(open(os.path.join(L10N, 'staging', 'editorial', _n, 'translation.json'), encoding='utf-8'))['units']
          if u.get('path') == PATH]
ck('158 id distinti sui cinque lotti, nessun duplicato', len(allids) == len(set(allids)) == 158,
   (len(allids), len(set(allids))))
ck('la somma dei lotti e il totale del file', sum(LOTS) == 158 == tot, sum(LOTS))
ck('gli id del file nel DB sono tutti coperti',
   set(r[0] for r in db.execute('select id from units where path=?', (PATH,)).fetchall()) == set(allids))
ck('0 sovrapposizioni con le righe 1-451', db.execute(
   'select count(*) from units where path=? and line<=? and line>=?', (PATH, 1, 451)).fetchone()[0] == 0)
ck('kind: 21 MISSION_TEXT + 2 VALUE + 2 DESCRIPTION + 1 DIALOG',
   collections.Counter(u['kind'] for u in su) ==
   {'MISSION_TEXT': 21, 'VALUE': 2, 'DESCRIPTION': 2, 'DIALOG': 1},
   collections.Counter(u['kind'] for u in su))
by = {u['idx']: u for u in tu}
ck('i due VALUE sono lo stesso testo e restano identici',
   by[1]['italian'].strip() == by[4]['italian'].strip() == 'Salvage the <EDC-ship>'
   and [u['idx'] for u in tu if u['italian'].strip() == u['english'].strip()] == VALS)
ck('le due DESCRIPTION sono identiche fra loro e tradotte',
   by[2]['italian'].strip() == by[5]['italian'].strip()
   and by[2]['italian'].strip() != by[2]['english'].strip())
ck('il DIALOG 11 e tradotto', by[11]['italian'].strip() != by[11]['english'].strip())
ck('la dedica: <EDC-ship>, <first> <last>, <EDC-ship> in quest ordine',
   TAGS.findall(by[25]['italian']) == ['<EDC-ship>', '<first>', '<last>', '<EDC-ship>'],
   TAGS.findall(by[25]['italian']))
ctxs = []
for u in su:
    if u['context'] not in ctxs:
        ctxs.append(u['context'])
ck('3 contesti in ordine di riga', ctxs == CTX, ctxs)
ck('tab: 17 nel sorgente, nelle unita attese',
   sum(1 for u in su if u['english'].startswith('\t')) == 17
   and [u['idx'] for u in tu if u['italian'].startswith('\t')] == TABS)
ck('nessun tab aggiunto', not [u for u in tu if u['english'].count('\t') != u['italian'].count('\t')])
a = sum(u['english'].count('"') for u in su)
b = sum(u['italian'].count('"') for u in tu)
ck('virgolette: %d = %d (8)' % (a, b), a == b == 8, (a, b))
ck('virgolette per unita', not [u for u in tu if u['english'].count('"') != u['italian'].count('"')])
ck('ZERO citazioni aperte (asserito vuoto)', not [u['idx'] for u in tu if u['italian'].count('"') % 2])
ck('ZERO quadre (asserito vuoto)', not [u['idx'] for u in tu if '[' in u['italian'] or ']' in u['italian']])
te = [t for u in su for t in TAGS.findall(u['english'])]
ti = [t for u in tu for t in TAGS.findall(u['italian'])]
ck('token: 19 = 19, sette famiglie', te == ti and collections.Counter(te) == FAM and len(te) == 19,
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
dups = sorted(tuple(v) for v in grp.values() if len(v) > 1)
ck('ESATTAMENTE 2 ripetizioni (1/4, 2/5): criterio rovesciato', dups == GROUPS, dups)
ck('ogni ripetizione resa identica', all(len({by[i]['italian'] for i in g}) == 1 for g in GROUPS))
merged = {}
for f in sorted(glob.glob(os.path.join(HERE, 'parts', 'part*.json'))):
    for kk, v in json.load(open(f, encoding='utf-8')).items():
        merged[int(kk)] = v
ck('le due parti ricostruiscono translation.json (1..26)',
   sorted(merged) == list(range(1, 27))
   and {i: '\t' * (len(by[i]['english']) - len(by[i]['english'].lstrip('\t'))) + v
        for i, v in merged.items()} == {u['idx']: u['italian'] for u in tu})
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('parole EN %d -> IT %d · sha256[:16] %s' % (sum(len(u['english'].split()) for u in tu),
      sum(len(u['italian'].split()) for u in tu), h[:16]))
print()
print('FAIL:', len(fail), '·', 'verify L110 superato' if not fail else 'verify L110 fallito')
raise SystemExit(0 if not fail else 1)
