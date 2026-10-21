r"""verify.py — L105 (data/quarg/quarg missions.txt, 61 unita', righe 335-506)

**Ultimo segmento: invariante di FILE.** Indipendente da `check.py`: rilegge il repository originale, `state.db`
e i `translation.json` di **tutti** i lotti del path (L102–L105).

Segmento: **117 unita' prima** della riga 356, **0 dopo la 506** (il file finisce qui), `max(line) = 506`.
File: i quattro lotti coprono **178 id distinti su 178 righe**, senza sovrapposizioni: 48 + 42 + 27 + 61.

Misure attese: **56 `MISSION_TEXT` + 4 `UI_LABEL` (identiche) + 1 `LOGBOOK` (tradotto)**, **54 tab**,
**99 virgolette** con **una citazione aperta** (unita' 26), **sette token** in cinque famiglie, cinque ripetizioni.
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
LABELS = {29: 'heliarch 2', 31: 'heliarch ask', 36: 'lunarium 2', 38: 'lunarium ask'}
GROUPS = [(2, 6), (3, 7), (4, 8), (17, 20, 24), (21, 25)]
FAM = {'<origin>': 1, '<first>': 2, '<last>': 2, '<start planet>': 1, '<start system>': 1}
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
ck('idx 1..61 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 62)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 61 righe 356 - 506', len(tu) == 61 and (first, last) == (356, 506), (len(tu), first, last))
tot = db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0]
before = db.execute('select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0]
after = db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0]
maxl = db.execute('select max(line) from units where path=?', (PATH,)).fetchone()[0]
ck('117 unita prima della riga 356 (L102-L104)', before == 117, before)
ck('0 unita dopo la riga 506: il file finisce qui', after == 0, after)
ck('file: 178 unita, max(line) = 506', tot == 178 and maxl == 506, (tot, maxl))
ck('kind: 56 MISSION_TEXT + 4 UI_LABEL + 1 LOGBOOK',
   collections.Counter(u['kind'] for u in su) == {'MISSION_TEXT': 56, 'UI_LABEL': 4, 'LOGBOOK': 1},
   collections.Counter(u['kind'] for u in su))
by = {u['idx']: u for u in tu}
ck('le 4 UI_LABEL identiche e il LOGBOOK tradotto',
   [i for i in tu if u'italian' and by[i['idx']]['italian'].strip() == by[i['idx']]['english'].strip()] == []
   or all(by[i]['italian'].strip() == LABELS[i] for i in LABELS))
ck('nessuna riga identica salvo le 4 etichette',
   [u['idx'] for u in tu if u['italian'].strip() == u['english'].strip()] == list(LABELS),
   [u['idx'] for u in tu if u['italian'].strip() == u['english'].strip()])
ck('il LOGBOOK e prosa tradotta',
   by[58]['kind'] == 'LOGBOOK' and by[58]['italian'] != by[58]['english']
   and by[58]['italian'].startswith('Nome completo:'))
ctxs = []
for u in su:
    if u['context'] not in ctxs:
        ctxs.append(u['context'])
ck('un solo contesto, che chiude il file',
   len(ctxs) == 1 and ctxs[0] == 'mission:Ask Quarg About Coalition Late')
TABS = [i for i in range(1, 62) if i not in (1, 5, 29, 31, 36, 38, 58)]
ck('tab: 54 nel sorgente, nelle unita attese',
   sum(1 for u in su if u['english'].startswith('\t')) == 54
   and [u['idx'] for u in tu if u['italian'].startswith('\t')] == TABS)
ck('nessun tab aggiunto', not [u for u in tu if u['english'].count('\t') != u['italian'].count('\t')])
a = sum(u['english'].count('"') for u in su)
b = sum(u['italian'].count('"') for u in tu)
ck('virgolette: %d = %d (99)' % (a, b), a == b == 99, (a, b))
ck('virgolette per unita', not [u for u in tu if u['english'].count('"') != u['italian'].count('"')])
ck("l'unica citazione aperta e' l'unita 26",
   [u['idx'] for u in tu if u['italian'].count('"') % 2] == [26]
   and [u['idx'] for u in su if u['english'].count('"') % 2] == [26])
te = [t for u in su for t in TAGS.findall(u['english'])]
ti = [t for u in tu for t in TAGS.findall(u['italian'])]
ck('token: 7 = 7, cinque famiglie', te == ti and collections.Counter(te) == FAM and len(te) == 7,
   (collections.Counter(te), collections.Counter(ti)))
ck('<start planet> e <start system> nell\'unita 49, in ordine',
   TAGS.findall(by[49]['italian']) == ['<start planet>', '<start system>'])
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
ck('5 ripetizioni: 2/6, 3/7, 4/8, 17/20/24, 21/25',
   sorted(tuple(v) for v in grp.values() if len(v) > 1) == sorted(GROUPS))
ck('ogni gruppo reso identico', all(len({by[i]['italian'] for i in g}) == 1 for g in GROUPS))
merged = {}
for f in sorted(glob.glob(os.path.join(HERE, 'parts', 'part*.json'))):
    for kk, v in json.load(open(f, encoding='utf-8')).items():
        merged[int(kk)] = v
ck('le quattro parti ricostruiscono translation.json (1..61)',
   sorted(merged) == list(range(1, 62))
   and {i: '\t' * (len(by[i]['english']) - len(by[i]['english'].lstrip('\t'))) + v
        for i, v in merged.items()} == {u['idx']: u['italian'] for u in tu})

# --- invariante di FILE: tutti i lotti del path, nessuna sovrapposizione, 178 id su 178 righe ---
per_lot = {}
ids = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging/editorial/L*/translation.json'))):
    d = json.load(open(f, encoding='utf-8'))['units']
    mine = [u for u in d if u.get('path') == PATH]
    if not mine:
        continue
    per_lot[os.path.basename(os.path.dirname(f))] = len(mine)
    ids += [u['id'] for u in mine]
db_ids = {r[0] for r in db.execute('select id from units where path=?', (PATH,))}
ck('lotti del file: 4 (L102-L105), 48+42+27+61 = 178',
   len(per_lot) == 4 and sorted(per_lot.values()) == [27, 42, 48, 61]
   and sum(per_lot.values()) == 178, per_lot)
ck('nessuna sovrapposizione fra lotti', len(ids) == len(set(ids)) == 178, (len(ids), len(set(ids))))
ck('copertura del file: 178 id distinti = 178 unita del DB', set(ids) == db_ids, len(db_ids - set(ids)))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('parole EN %d -> IT %d · sha256[:16] %s' % (sum(len(u['english'].split()) for u in tu),
      sum(len(u['italian'].split()) for u in tu), h[:16]))
print()
print('FAIL:', len(fail), '·', 'verify L105 superato (file chiuso)' if not fail else 'verify L105 fallito')
raise SystemExit(0 if not fail else 1)
