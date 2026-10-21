r"""verify.py — L85 (data/successors/predecessors.txt, 7 unita', righe 621-800) — CHIUDE IL FILE

Invariante **di file**: **0 unita' dopo** la riga 782, `max(line) = 782`, **59 unita' totali**, copertura
dell'**intero** file (59 id distinti dai `translation.json` di L81-L85). Misure: 7 unita', righe 648-782,
tutte `DESCRIPTION`, 7 contesti `outfit:`, 0 tab, 4 virgolette, 0 token, 0 duplicati.
"""
import collections, glob, hashlib, json, os, re, sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
ROOT = os.path.abspath(os.path.join(L10N, '..'))
PATH = 'data/successors/predecessors.txt'
su = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units']
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
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
ck('idx 1..7 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 8)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 7 righe 648 - 782', len(tu) == 7 and (first, last) == (648, 782), (len(tu), first, last))
tot = db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0]
before = db.execute('select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0]
after = db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0]
maxl = db.execute('select max(line) from units where path=?', (PATH,)).fetchone()[0]
ck('52 unita prima della riga 648 (L81-L84)', before == 52, before)
ck('CHIUDE il file: 0 unita dopo la riga 782', after == 0, after)
ck('file completo: 59 unita, max(line) = 782', tot == 59 and maxl == 782, (tot, maxl))
staged, slines = set(), set()
for f in glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json')):
    try:
        data = json.load(open(f, encoding='utf-8'))
    except Exception:
        continue
    for u in data.get('units', []):
        if u.get('path') == PATH:
            staged.add(u['id'])
            slines.add(u['line'])
fids = set(r[0] for r in db.execute('select id from units where path=?', (PATH,)).fetchall())
ck('copertura del file intero: 59 id distinti', len(staged) == 59 == len(fids), (len(staged), len(fids)))
ck('copertura del file intero: 59 righe', len(slines) == 59, len(slines))
k = collections.Counter(u['kind'] for u in su)
ck('kind: 7 DESCRIPTION, nessun altro', dict(k) == {'DESCRIPTION': 7}, dict(k))
by = {u['idx']: u for u in tu}
ck('tutte le 7 unita sono tradotte',
   all(by[i]['italian'].strip() != by[i]['english'].strip() for i in range(1, 8)))
ctxs = []
for u in su:
    if u['context'] not in ctxs:
        ctxs.append(u['context'])
ck('7 contesti outfit: distinti', len(ctxs) == 7 and len(ctxs) == len(su), len(ctxs))
ck('primo contesto: "Tijra" Heirloom Lance', ctxs[0] == 'outfit:"Tijra" Heirloom Lance', ctxs[0])
ck('ultimo contesto: Stolen Cloak (Deactivated)', ctxs[-1] == 'outfit:Stolen Cloak (Deactivated)', ctxs[-1])
a = sum(u['english'].count('"') for u in su)
b = sum(u['italian'].count('"') for u in tu)
ck('virgolette: %d = %d (4)' % (b, a), a == b == 4, (a, b))
ck('nessun tab', not [u for u in tu if '\t' in u['italian']])
ck('nessuna quadra o backtick', not [u for u in tu if '[' in u['italian'] or '`' in u['italian']])
ck('nessun token <...>', not [u for u in tu if '<' in u['italian']])
ck('nessuna traduzione vuota', all(u['italian'].strip() for u in tu))
NONLAT = re.compile(r'[^\x00-\x7F\u00C0-\u024F\u2018\u2019\u201C\u201D\u2013\u2014\u2026]')
ck('nessun carattere non latino', not [u for u in tu if NONLAT.search(u['italian'])])
ck('nessun trattino lungo o virgoletta curva',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D')])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate', 0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
print('rapporto IT/EN: min %.2f max %.2f' % (min(rs), max(rs)))
grp = {}
for u in su:
    grp.setdefault(u['english'], []).append(u['idx'])
ck('nessun duplicato', not [v for v in grp.values() if len(v) > 1])
merged = {}
for f in sorted(glob.glob(os.path.join(HERE, 'parts', 'part*.json'))):
    for kk, v in json.load(open(f, encoding='utf-8')).items():
        merged[int(kk)] = v
ck('le parti ricostruiscono translation.json',
   {i: '\t' * (len(by[i]['english']) - len(by[i]['english'].lstrip('\t'))) + v for i, v in merged.items()}
   == {u['idx']: u['italian'] for u in tu})
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('parole EN %d -> IT %d · sha256[:16] %s' % (sum(len(u['english'].split()) for u in tu),
      sum(len(u['italian'].split()) for u in tu), h[:16]))
print()
print('FAIL:', len(fail), '·', 'verify L85 superato' if not fail else 'verify L85 fallito')
raise SystemExit(0 if not fail else 1)
