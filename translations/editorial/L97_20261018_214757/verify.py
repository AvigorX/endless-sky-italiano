r"""verify.py — L97 (data/coalition/coalition culture conversations.txt, 36 unita', righe 251-462)

**Ultimo segmento: invariante di FILE, non di segmento.** Indipendente da `check.py`: rilegge il repository
originale, `state.db` e i `translation.json` di **tutti** i lotti del path (L93–L97).

Segmento: **121 unita' prima** della riga 251, **0 dopo la 462** (il file finisce qui), `max(line) = 462`.
File: i cinque lotti coprono **157 id distinti su 157 righe**, senza sovrapposizioni: 31 + 36 + 27 + 27 + 36.

Misure attese: 36 `MISSION_TEXT`, 29 tab, 24 virgolette, **14 token** (`<origin>` x8, `<ship>` x5, `<last>` x1),
ripetizione tripla 7/9/11 resa identica.
"""
import collections, glob, hashlib, json, os, re, sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
ROOT = os.path.abspath(os.path.join(L10N, '..'))
PATH = 'data/coalition/coalition culture conversations.txt'
su = sorted(json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
TAGS = re.compile(r'<[^<>]+>')
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
ck('idx 1..36 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 37)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 36 righe 251 - 462', len(tu) == 36 and (first, last) == (251, 462), (len(tu), first, last))
tot = db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0]
before = db.execute('select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0]
after = db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0]
maxl = db.execute('select max(line) from units where path=?', (PATH,)).fetchone()[0]
ck('121 unita prima della riga 251 (L93-L96)', before == 121, before)
ck('0 unita dopo la riga 462: il file finisce qui', after == 0, after)
ck('file: 157 unita, max(line) = 462', tot == 157 and maxl == 462, (tot, maxl))
ck('kind: 36 MISSION_TEXT, 0 UI_LABEL',
   collections.Counter(u['kind'] for u in su) == {'MISSION_TEXT': 36}
   and not [u for u in tu if u['kind'] == 'UI_LABEL'])
ck('tutte tradotte', all(u['italian'].strip() != u['english'].strip() for u in tu))
ctxs = []
for u in su:
    if u['context'] not in ctxs:
        ctxs.append(u['context'])
ck('7 contesti in ordine di riga, dal primo all\'ultimo',
   len(ctxs) == 7 and ctxs[0].endswith('Departing Trouble - A') and ctxs[-1].endswith('Ring of Wisdom')
   and [c.split(':')[1][-1] for c in ctxs[:3]] == ['A', 'B', 'C'], (len(ctxs), ctxs))
TABS = [i for i in range(1, 37) if i not in (1, 6, 12, 18, 24, 27, 30)]
ck('tab: 29 nel sorgente, nelle unita attese',
   sum(1 for u in su if u['english'].startswith('\t')) == 29
   and [u['idx'] for u in tu if u['italian'].startswith('\t')] == TABS,
   [u['idx'] for u in tu if u['italian'].startswith('\t')])
ck('nessun tab aggiunto', not [u for u in tu if u['english'].count('\t') != u['italian'].count('\t')])
a = sum(u['english'].count('"') for u in su)
b = sum(u['italian'].count('"') for u in tu)
ck('virgolette: %d = %d (24)' % (a, b), a == b == 24, (a, b))
ck('virgolette per unita, 6 nella 19',
   not [u for u in tu if u['english'].count('"') != u['italian'].count('"')]
   and [u['idx'] for u in tu if u['english'].count('"') == 6] == [19])
ck('nessuna virgoletta dispari', not [u for u in tu if u['italian'].count('"') % 2])
te = [t for u in su for t in TAGS.findall(u['english'])]
ti = [t for u in tu for t in TAGS.findall(u['italian'])]
ck('token: 14 = 14, per famiglia',
   te == ti and te.count('<origin>') == 8 and te.count('<ship>') == 5 and te.count('<last>') == 1,
   (collections.Counter(te), collections.Counter(ti)))
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
by = {u['idx']: u for u in tu}
ck('ripetizione inglese tripla: 7/9/11',
   sorted(tuple(v) for v in grp.values() if len(v) > 1) == [(7, 9, 11)])
ck('7/9/11 resa identica', by[7]['italian'] == by[9]['italian'] == by[11]['italian'])
ck('le varianti 15/17 differiscono per la virgola',
   by[15]['italian'].split('"')[1] == 'collaborazione,' and by[17]['italian'].split('"')[1] == 'collaborazione')
merged = {}
for f in sorted(glob.glob(os.path.join(HERE, 'parts', 'part*.json'))):
    for kk, v in json.load(open(f, encoding='utf-8')).items():
        merged[int(kk)] = v
ck('le tre parti ricostruiscono translation.json (1..36)',
   sorted(merged) == list(range(1, 37))
   and {i: '\t' * (len(by[i]['english']) - len(by[i]['english'].lstrip('\t'))) + v
        for i, v in merged.items()} == {u['idx']: u['italian'] for u in tu})

# --- invariante di FILE: tutti i lotti del path, nessuna sovrapposizione, 157 id su 157 righe ---
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
ck('lotti del file: 5 (L93-L97), 31+36+27+27+36 = 157',
   len(per_lot) == 5 and sorted(per_lot.values()) == [27, 27, 31, 36, 36]
   and sum(per_lot.values()) == 157, per_lot)
ck('nessuna sovrapposizione fra lotti', len(ids) == len(set(ids)) == 157, (len(ids), len(set(ids))))
ck('copertura del file: 157 id distinti = 157 unita del DB', set(ids) == db_ids, len(db_ids - set(ids)))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('parole EN %d -> IT %d · sha256[:16] %s' % (sum(len(u['english'].split()) for u in tu),
      sum(len(u['italian'].split()) for u in tu), h[:16]))
print()
print('FAIL:', len(fail), '·', 'verify L97 superato (file chiuso)' if not fail else 'verify L97 fallito')
raise SystemExit(0 if not fail else 1)
