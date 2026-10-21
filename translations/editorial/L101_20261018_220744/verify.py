r"""verify.py — L101 (data/hai/hai culture conversations.txt, 26 unita', righe 321-386)

**Ultimo segmento: invariante di FILE.** Indipendente da `check.py`: rilegge il repository originale, `state.db`
e i `translation.json` di **tutti** i lotti del path (L98–L101).

Segmento: **121 unita' prima** della riga 321, **0 dopo la 386** (il file finisce qui), `max(line) = 386`.
File: i quattro lotti coprono **147 id distinti su 147 righe**, senza sovrapposizioni: 39 + 38 + 44 + 26.

Misure attese: 26 `MISSION_TEXT`, 24 tab, 34 virgolette (8 nell'unita' 25), **0 token**, **1 coppia di quadre**
(unita' 13), nessuna ripetizione, nessuna virgoletta dispari.
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
ck('idx 1..26 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 27)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 26 righe 321 - 386', len(tu) == 26 and (first, last) == (321, 386), (len(tu), first, last))
tot = db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0]
before = db.execute('select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0]
after = db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0]
maxl = db.execute('select max(line) from units where path=?', (PATH,)).fetchone()[0]
ck('121 unita prima della riga 321 (L98-L100)', before == 121, before)
ck('0 unita dopo la riga 386: il file finisce qui', after == 0, after)
ck('file: 147 unita, max(line) = 386', tot == 147 and maxl == 386, (tot, maxl))
ck('kind: 26 MISSION_TEXT, 0 UI_LABEL',
   collections.Counter(u['kind'] for u in su) == {'MISSION_TEXT': 26}
   and not [u for u in tu if u['kind'] == 'UI_LABEL'])
ck('tutte tradotte', all(u['italian'].strip() != u['english'].strip() for u in tu))
ctxs = []
for u in su:
    if u['context'] not in ctxs:
        ctxs.append(u['context'])
ck('2 contesti in ordine di riga, e il secondo chiude il file',
   len(ctxs) == 2 and [c.split(':', 1)[1] for c in ctxs] == ['Hai Film Release', 'Sick of Acorn Bread']
   and ctxs[-1] == su[-1]['context'], ctxs)
TABS = [i for i in range(1, 27) if i not in (1, 6)]
ck('tab: 24 nel sorgente, nelle unita attese',
   sum(1 for u in su if u['english'].startswith('\t')) == 24
   and [u['idx'] for u in tu if u['italian'].startswith('\t')] == TABS)
ck('nessun tab aggiunto', not [u for u in tu if u['english'].count('\t') != u['italian'].count('\t')])
a = sum(u['english'].count('"') for u in su)
b = sum(u['italian'].count('"') for u in tu)
ck('virgolette: %d = %d (34)' % (a, b), a == b == 34, (a, b))
ck('virgolette per unita', not [u for u in tu if u['english'].count('"') != u['italian'].count('"')])
ck('nessuna virgoletta dispari', not [u for u in tu if u['italian'].count('"') % 2])
ck('unita 25: 8 virgolette', [u['idx'] for u in tu if u['english'].count('"') == 8] == [25])
te = [t for u in su for t in TAGS.findall(u['english'])]
ti = [t for u in tu for t in TAGS.findall(u['italian'])]
ck('zero token nel sorgente e nella resa', not te and not ti)
ck('quadre: 1 coppia, solo nell\'unita 13',
   sum(u['english'].count('[') for u in su) == sum(u['italian'].count('[') for u in tu) == 1
   and sum(u['english'].count(']') for u in su) == sum(u['italian'].count(']') for u in tu) == 1
   and [u['idx'] for u in tu if '[' in u['italian']] == [13])
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
ck('nessuna ripetizione inglese nel segmento', [v for v in grp.values() if len(v) > 1] == [])
merged = {}
for f in sorted(glob.glob(os.path.join(HERE, 'parts', 'part*.json'))):
    for kk, v in json.load(open(f, encoding='utf-8')).items():
        merged[int(kk)] = v
by = {u['idx']: u for u in tu}
ck('le due parti ricostruiscono translation.json (1..26)',
   sorted(merged) == list(range(1, 27))
   and {i: '\t' * (len(by[i]['english']) - len(by[i]['english'].lstrip('\t'))) + v
        for i, v in merged.items()} == {u['idx']: u['italian'] for u in tu})

# --- invariante di FILE: tutti i lotti del path, nessuna sovrapposizione, 147 id su 147 righe ---
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
ck('lotti del file: 4 (L98-L101), 39+38+44+26 = 147',
   len(per_lot) == 4 and sorted(per_lot.values()) == [26, 38, 39, 44]
   and sum(per_lot.values()) == 147, per_lot)
ck('nessuna sovrapposizione fra lotti', len(ids) == len(set(ids)) == 147, (len(ids), len(set(ids))))
ck('copertura del file: 147 id distinti = 147 unita del DB', set(ids) == db_ids, len(db_ids - set(ids)))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('parole EN %d -> IT %d · sha256[:16] %s' % (sum(len(u['english'].split()) for u in tu),
      sum(len(u['italian'].split()) for u in tu), h[:16]))
print()
print('FAIL:', len(fail), '·', 'verify L101 superato (file chiuso)' if not fail else 'verify L101 fallito')
raise SystemExit(0 if not fail else 1)
