r"""verify.py — L89 (data/successors/successor outfits.txt, 12 unita', righe 561-700) — CHIUDE IL FILE

Invariante **di file**: **0 unita' dopo** la riga 647, `max(line) = 647`, **56 unita'**, copertura dell'intero
file dai `translation.json` di L86-L89. Misure: 12 unita', righe 574-647, tutte `DESCRIPTION`; **6 tab**
(2, 4, 6, 8, 11, 12); **0 virgolette**; duplicato legittimo 1/3/5/7.
"""
import collections, glob, hashlib, json, os, re, sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
ROOT = os.path.abspath(os.path.join(L10N, '..'))
PATH = 'data/successors/successor outfits.txt'
su = sorted(json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
DUP = (1, 3, 5, 7)
fail = []


def ck(n, c, d=''):
    print('%-60s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
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
ck('idx 1..12 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 13)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 12 righe 574 - 647', len(tu) == 12 and (first, last) == (574, 647), (len(tu), first, last))
tot = db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0]
before = db.execute('select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0]
after = db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0]
maxl = db.execute('select max(line) from units where path=?', (PATH,)).fetchone()[0]
ck('44 unita prima della riga 574 (L86-L88)', before == 44, before)
ck('CHIUDE il file: 0 unita dopo la riga 647', after == 0, after)
ck('file completo: 56 unita, max(line) = 647', tot == 56 and maxl == 647, (tot, maxl))
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
ck('copertura del file intero: 56 id distinti', len(staged) == 56 == len(fids), (len(staged), len(fids)))
ck('copertura del file intero: 56 righe', len(slines) == 56, len(slines))
ck('kind: 12 DESCRIPTION, nessun dato',
   collections.Counter(u['kind'] for u in su) == {'DESCRIPTION': 12})
by = {u['idx']: u for u in tu}
ck('le 12 DESCRIPTION sono tradotte', all(u['italian'].strip() != u['english'].strip() for u in tu))
grp = {}
for u in su:
    grp.setdefault(u['english'], []).append(u['idx'])
ck('unica ripetizione inglese: 1/3/5/7',
   [tuple(v) for v in grp.values() if len(v) > 1] == [DUP])
ck('la ripetizione e resa identica', len(set(by[i]['italian'] for i in DUP)) == 1)
ctxs = []
for u in su:
    if u['context'] not in ctxs:
        ctxs.append(u['context'])
ck('6 contesti in ordine di riga', len(ctxs) == 6 and ctxs[0] == 'outfit:Multimodal Armor: Light'
   and ctxs[-1] == 'outfit:Radiant Shield Shunt', (len(ctxs), ctxs[0], ctxs[-1]))
ck('tab: 6 nel sorgente, in 2, 4, 6, 8, 11, 12',
   sum(1 for u in su if u['english'].startswith('\t')) == 6
   and [u['idx'] for u in tu if u['italian'].startswith('\t')] == [2, 4, 6, 8, 11, 12])
ck('nessun tab aggiunto', not [u for u in tu if u['english'].count('\t') != u['italian'].count('\t')])
a = sum(u['english'].count('"') for u in su)
b = sum(u['italian'].count('"') for u in tu)
ck('virgolette: %d = %d (0 nel sorgente)' % (a, b), a == b == 0, (a, b))
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
print('FAIL:', len(fail), '·', 'verify L89 superato' if not fail else 'verify L89 fallito')
raise SystemExit(0 if not fail else 1)
