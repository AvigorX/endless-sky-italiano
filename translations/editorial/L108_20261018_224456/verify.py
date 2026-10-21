r"""verify.py — L108 (data/korath/korath missions.txt, 36 unita', righe 216-335)

Invariante di **segmento**, indipendente da `check.py`: rilegge il repository originale, `state.db` e i `parts/`.

Misure attese: **63 unita' prima** della riga 216 (L106+L107), **59 dopo la 326**, file di **158 unita'**,
`max(line) = 580`, confine alla riga **338** (`mission:Efreti: Distress Call 2`). **Quattro contesti** in ordine di
riga. **14 `TEXT` + 15 `MISSION_TEXT` + 3 `VALUE` + 3 `DESCRIPTION` + 1 `DIALOG`**, **12 tab**, **18 virgolette**,
**23 token** (`<EDC-ship>` x8), zero quadre, zero ripetizioni.

Ricalcola inoltre, in modo indipendente, i **vincoli di composizione** dei frammenti `phrase:` (unita' 1-14) e
compone **tutte** le 24 frasi soggetto x verbo x oggetto, verificando che nessuna produca punteggiatura doppia.
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
VALS = [15, 18, 29]
NOTAB = list(range(1, 21)) + [29, 30, 31, 32]
TABS = [i for i in range(1, 37) if i not in NOTAB]
FAM = {'<EDC-ship>': 8, '<planet>': 4, '<destination>': 3, '<payment>': 3, '<ship>': 3, '<bunks>': 2}
CTX = ['phrase:kor efret small package offer', 'mission:Small Scale Delivery',
       'mission:Efreti: Distress Call 1', 'mission:Efreti: Distress Call 2']
SUBJ, VERB, OBJ, DEST, TAIL = [1, 2, 3], [4, 5], [6, 7, 8, 9], [10], [11, 12, 13, 14]
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
ck('idx 1..36 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 37)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 36 righe 216 - 326', len(tu) == 36 and (first, last) == (216, 326), (len(tu), first, last))
tot = db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0]
before = db.execute('select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0]
after = db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0]
maxl = db.execute('select max(line) from units where path=?', (PATH,)).fetchone()[0]
ck('63 unita prima della riga 216 (L106+L107)', before == 63, before)
ck('59 unita dopo la riga 326', after == 59, after)
ck('file: 158 unita, max(line) = 580', tot == 158 and maxl == 580, (tot, maxl))
ck('il confine: la riga 338 apre Distress Call 2',
   db.execute('select line,context from units where path=? and line>? order by line limit 1',
              (PATH, last)).fetchone() == (338, 'mission:Efreti: Distress Call 2'))
ck('0 sovrapposizioni con le righe 1-212', db.execute(
   'select count(*) from units where path=? and line<=? and line>=?', (PATH, 1, 212)).fetchone()[0] == 0)
ck('kind: 14 TEXT + 15 MISSION_TEXT + 3 VALUE + 3 DESCRIPTION + 1 DIALOG',
   collections.Counter(u['kind'] for u in su) ==
   {'TEXT': 14, 'MISSION_TEXT': 15, 'VALUE': 3, 'DESCRIPTION': 3, 'DIALOG': 1},
   collections.Counter(u['kind'] for u in su))
by = {u['idx']: u for u in tu}
ck('i tre VALUE restano identici',
   [u['idx'] for u in tu if u['italian'].strip() == u['english'].strip()] == VALS
   and by[15]['italian'].strip() == 'Package to <planet>'
   and by[18]['italian'].strip() == 'Distress call from the <EDC-ship>'
   and by[29]['italian'].strip() == 'Return the <EDC-ship> survivors')
ck('le 14 TEXT sono le unita 1-14', [u['idx'] for u in tu if u['kind'] == 'TEXT'] == list(range(1, 15)))
# --- composizione, ricalcolata qui -------------------------------------------------------
ck('soggetto: maiuscola senza punto', all(
   by[i]['italian'][0].isupper() and not by[i]['italian'].endswith('.') for i in SUBJ))
ck('verbo: minuscola, chiude con "di"/"devi", niente punto', all(
   by[i]['italian'][0].islower() and by[i]['italian'].split()[-1] in ('di', 'devi')
   and not by[i]['italian'].endswith('.') for i in VERB))
ck('oggetto: minuscola, infinito in testa, niente punto', all(
   by[i]['italian'][0].islower() and by[i]['italian'].split()[0].endswith('are')
   and not by[i]['italian'].endswith('.') for i in OBJ))
ck('destinazione: "a " in testa e punto in coda', by[10]['italian'].startswith('a ')
   and by[10]['italian'].endswith('.') and by[10]['italian'].count('.') == 1)
ck('frase finale: maiuscola e punto', all(
   by[i]['italian'][0].isupper() and by[i]['italian'].endswith('.') for i in TAIL))
combos = [' '.join([by[s]['italian'], by[v]['italian'], by[o]['italian'], by[10]['italian']])
          for s in SUBJ for v in VERB for o in OBJ]
ck('24 combinazioni soggetto x verbo x oggetto, nessuna con punteggiatura doppia',
   len(combos) == 24 and not [c for c in combos if '  ' in c or '..' in c or ' ,' in c],
   [c for c in combos if '  ' in c or '..' in c][:3])
ck('ogni combinazione finisce con il punto della destinazione',
   all(c.endswith('per <payment>.') for c in combos))
ck('nessuna combinazione ripete la preposizione "di di"', not [c for c in combos if 'di di' in c])
# ----------------------------------------------------------------------------------------
ctxs = []
for u in su:
    if u['context'] not in ctxs:
        ctxs.append(u['context'])
ck('4 contesti in ordine di riga', ctxs == CTX, ctxs)
ck('tab: 12 nel sorgente, nelle unita attese',
   sum(1 for u in su if u['english'].startswith('\t')) == 12
   and [u['idx'] for u in tu if u['italian'].startswith('\t')] == TABS)
ck('nessun tab aggiunto', not [u for u in tu if u['english'].count('\t') != u['italian'].count('\t')])
a = sum(u['english'].count('"') for u in su)
b = sum(u['italian'].count('"') for u in tu)
ck('virgolette: %d = %d (18)' % (a, b), a == b == 18, (a, b))
ck('virgolette per unita', not [u for u in tu if u['english'].count('"') != u['italian'].count('"')])
ck('ZERO citazioni aperte (asserito vuoto)', not [u['idx'] for u in tu if u['italian'].count('"') % 2])
ck('ZERO quadre (asserito vuoto)', not [u['idx'] for u in tu if '[' in u['italian'] or ']' in u['italian']])
te = [t for u in su for t in TAGS.findall(u['english'])]
ti = [t for u in tu for t in TAGS.findall(u['italian'])]
ck('token: 23 = 23, sei famiglie', te == ti and collections.Counter(te) == FAM and len(te) == 23,
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
merged = {}
for f in sorted(glob.glob(os.path.join(HERE, 'parts', 'part*.json'))):
    for kk, v in json.load(open(f, encoding='utf-8')).items():
        merged[int(kk)] = v
ck('le due parti ricostruiscono translation.json (1..36)',
   sorted(merged) == list(range(1, 37))
   and {i: '\t' * (len(by[i]['english']) - len(by[i]['english'].lstrip('\t'))) + v
        for i, v in merged.items()} == {u['idx']: u['italian'] for u in tu})
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('parole EN %d -> IT %d · sha256[:16] %s' % (sum(len(u['english'].split()) for u in tu),
      sum(len(u['italian'].split()) for u in tu), h[:16]))
print()
print('FAIL:', len(fail), '·', 'verify L108 superato' if not fail else 'verify L108 fallito')
raise SystemExit(0 if not fail else 1)
