r"""verify.py — L84 (data/successors/predecessors.txt, 4 unita', righe 521-620)

Indipendente da `check.py`. Segmento: **48 prima**, **7 dopo**, `max(line) = 782`, file di **59 unita'**,
confine alla riga 648 (`outfit:"Tijra" Heirloom Lance`). Misure: 4 unita', righe 534-608; 1 `TEXT` (dato) +
3 `DESCRIPTION` (prosa); 1 tab (unita' 3); 2 virgolette; 0 token; 0 duplicati.
"""
import collections, glob, hashlib, json, os, re, sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
ROOT = os.path.abspath(os.path.join(L10N, '..'))
PATH = 'data/successors/predecessors.txt'
su = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units']
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
PROSE = {2, 3, 4}
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
ck('idx 1..4 e ordine = sorgente', [u['idx'] for u in tu] == [1, 2, 3, 4] == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 4 righe 534 - 608', len(tu) == 4 and (first, last) == (534, 608), (len(tu), first, last))
tot = db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0]
before = db.execute('select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0]
after = db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0]
maxl = db.execute('select max(line) from units where path=?', (PATH,)).fetchone()[0]
ck('48 unita prima della riga 534', before == 48, before)
ck('7 unita dopo la riga 608', after == 7, after)
ck('file: 59 unita, max(line) = 782', tot == 59 and maxl == 782, (tot, maxl))
nxt = db.execute('select line,context from units where path=? and line>? order by line limit 1', (PATH, last)).fetchone()
ck('confine: riga 648 apre outfit:"Tijra" Heirloom Lance',
   nxt is not None and nxt[0] == 648 and nxt[1] == 'outfit:"Tijra" Heirloom Lance',
   tuple(nxt) if nxt else None)
k = collections.Counter(u['kind'] for u in su)
ck('kind: 1 TEXT, 3 DESCRIPTION', dict(k) == {'TEXT': 1, 'DESCRIPTION': 3}, dict(k))
by = {u['idx']: u for u in tu}
ck('il TEXT resta identico', by[1]['italian'] == by[1]['english'] == '"Tijra" Heirloom Lance')
ck('le 3 DESCRIPTION sono tradotte',
   all(by[i]['italian'].strip() != by[i]['english'].strip() for i in PROSE))
a = sum(u['english'].count('"') for u in su)
b = sum(u['italian'].count('"') for u in tu)
ck('virgolette: %d = %d (2)' % (b, a), a == b == 2, (a, b))
ck('tab: 1 nel sorgente, solo in unita 3',
   sum(1 for u in su if u['english'].startswith('\t')) == 1
   and [u['idx'] for u in tu if u['italian'].startswith('\t')] == [3])
ck('nessun tab aggiunto', not [u for u in tu if u['english'].count('\t') != u['italian'].count('\t')])
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
print('FAIL:', len(fail), '·', 'verify L84 superato' if not fail else 'verify L84 fallito')
raise SystemExit(0 if not fail else 1)
