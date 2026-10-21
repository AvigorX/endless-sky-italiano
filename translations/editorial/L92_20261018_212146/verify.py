r"""verify.py — L92 (data/successors/successor culture conversations.txt, 46 unita', righe 230-351)

**Ultimo segmento: invariante di FILE, non di segmento.** Indipendente da `check.py`: rilegge il repository
originale, `state.db` e i `translation.json` di **tutti** i lotti del path (L90, L91, L92).

Asserzioni di segmento: 68 unita' prima della riga 230, **0 dopo la 351**, `max(line) = 351`, confine alla
prim'ultima unita' (riga 351). Asserzione di file: i tre lotti coprono **114 id distinti su 114 righe**, senza
sovrapposizioni, e 34 + 34 + 46 = 114.

Misure attese: 46 `MISSION_TEXT` (0 `UI_LABEL`), 42 tab, 48 virgolette (13 e 21 con una sola, riprodotta),
1 token `<ship>` (unita' 41), ripetizione inglese 17/20 resa identica.
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
odd = [13, 21]
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
ck('idx 1..46 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 47)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 46 righe 230 - 351', len(tu) == 46 and (first, last) == (230, 351), (len(tu), first, last))
tot = db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0]
before = db.execute('select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0]
after = db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0]
maxl = db.execute('select max(line) from units where path=?', (PATH,)).fetchone()[0]
ck('68 unita prima della riga 230 (L90+L91)', before == 68, before)
ck('0 unita dopo la riga 351: il file finisce qui', after == 0, after)
ck('file: 114 unita, max(line) = 351', tot == 114 and maxl == 351, (tot, maxl))
prev = db.execute('select line,context from units where path=? and line<? order by line desc limit 1', (PATH, first)).fetchone()
ck('inizio: la precedente e la 229 (Stage Play)', prev is not None
   and tuple(prev) == (229, 'mission:Successors: Stage Play'), tuple(prev) if prev else None)
ck('kind: 46 MISSION_TEXT, 0 UI_LABEL',
   collections.Counter(u['kind'] for u in su) == {'MISSION_TEXT': 46}
   and not [u for u in tu if u['kind'] == 'UI_LABEL'])
ck('tutte tradotte', all(u['italian'].strip() != u['english'].strip() for u in tu))
ctxs = []
for u in su:
    if u['context'] not in ctxs:
        ctxs.append(u['context'])
ck('5 contesti in ordine di riga', len(ctxs) == 5 and ctxs[0].endswith('Stage Play')
   and ctxs[-1].endswith('Armor Reconfiguration'), (len(ctxs), ctxs[0], ctxs[-1]))
TABS = [i for i in range(1, 47) if i not in (21, 37, 44, 46)]
ck('tab: 42 nel sorgente, nelle unita attese',
   sum(1 for u in su if u['english'].startswith('\t')) == 42
   and [u['idx'] for u in tu if u['italian'].startswith('\t')] == TABS,
   [u['idx'] for u in tu if u['italian'].startswith('\t')])
ck('nessun tab aggiunto', not [u for u in tu if u['english'].count('\t') != u['italian'].count('\t')])
a = sum(u['english'].count('"') for u in su)
b = sum(u['italian'].count('"') for u in tu)
ck('virgolette: %d = %d (48)' % (a, b), a == b == 48, (a, b))
ck('virgolette per unita identiche al sorgente',
   not [u for u in tu if u['english'].count('"') != u['italian'].count('"')])
ck('virgolette dispari solo in 13 e 21 (una ciascuna)',
   [u['idx'] for u in tu if u['italian'].count('"') % 2] == odd
   and all({u['idx']: u for u in tu}[i]['italian'].count('"') == 1 for i in odd))
by = {u['idx']: u for u in tu}
te = [t for u in su for t in TAGS.findall(u['english'])]
ti = [t for u in tu for t in TAGS.findall(u['italian'])]
ck('token: 1 = 1, <ship> all\'unita 41', te == ti == ['<ship>'] and TAGS.findall(by[41]['italian']) == ['<ship>'], (te, ti))
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
ck('ripetizione inglese: 17/20',
   sorted(tuple(v) for v in grp.values() if len(v) > 1) == [(17, 20)])
ck('17/20 resa identica', by[17]['italian'] == by[20]['italian'])
merged = {}
for f in sorted(glob.glob(os.path.join(HERE, 'parts', 'part*.json'))):
    for kk, v in json.load(open(f, encoding='utf-8')).items():
        merged[int(kk)] = v
ck('le tre parti ricostruiscono translation.json (1..46)',
   sorted(merged) == list(range(1, 47))
   and {i: '\t' * (len(by[i]['english']) - len(by[i]['english'].lstrip('\t'))) + v
        for i, v in merged.items()} == {u['idx']: u['italian'] for u in tu})

# --- invariante di FILE: tutti i lotti del path, nessuna sovrapposizione, 114 id su 114 righe ---
per_lot = {}
ids = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging/editorial/L*/translation.json'))):
    d = json.load(open(f, encoding='utf-8'))['units']
    mine = [u for u in d if u.get('path') == PATH]
    if not mine:
        continue
    name = os.path.basename(os.path.dirname(f))
    per_lot[name] = len(mine)
    ids += [u['id'] for u in mine]
db_ids = {r[0] for r in db.execute('select id from units where path=?', (PATH,))}
ck('lotti del file: 3 (L90, L91, L92), 34 + 34 + 46',
   len(per_lot) == 3 and sorted(per_lot.values()) == [34, 34, 46]
   and sum(per_lot.values()) == 114, per_lot)
ck('nessuna sovrapposizione fra lotti', len(ids) == len(set(ids)) == 114, (len(ids), len(set(ids))))
ck('copertura del file: 114 id distinti = 114 unita del DB', set(ids) == db_ids, len(db_ids - set(ids)))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('parole EN %d -> IT %d · sha256[:16] %s' % (sum(len(u['english'].split()) for u in tu),
      sum(len(u['italian'].split()) for u in tu), h[:16]))
print()
print('FAIL:', len(fail), '·', 'verify L92 superato (file chiuso)' if not fail else 'verify L92 fallito')
raise SystemExit(0 if not fail else 1)
