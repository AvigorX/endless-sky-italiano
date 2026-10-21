r"""verify.py — L83 (data/successors/predecessors.txt, 11 unita', righe 401-520)

Verifica **indipendente**. Invariante di **segmento**: **37 prima** (L81+L82), **11 dopo**, `max(line) = 782`,
file di **59 unita'**, confine alla riga 534 (`ship:Valkkyiara-Khorasaqra`). Misure: 11 unita', righe
446-520; **7 TEXT + 3 DESCRIPTION + 1 VALUE**; **8 di dato** identiche, **3 di prosa** tradotte; 0 tab,
12 virgolette, 0 dispari, 0 token, 0 duplicati.
"""
import collections, glob, hashlib, json, os, re, sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
ROOT = os.path.abspath(os.path.join(L10N, '..'))
PATH = 'data/successors/predecessors.txt'
SRC = os.path.join(ROOT, 'endless-sky', *PATH.split('/'))
su = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units']
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
lines = open(SRC, encoding='utf-8').read().split('\n')
DATA, PROSE = {4, 5, 6, 7, 8, 9, 10, 11}, {1, 2, 3}
TAGS = re.compile(r'<[^<>]+>')
fail = []


def ck(n, c, d=''):
    print('%-66s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente (11 righe)', not [u['idx'] for u in su if lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
db.row_factory = sqlite3.Row
bad = [u['idx'] for u in su
       for row in [db.execute('select english,kind,path,context,state from units where id=?', (u['id'],)).fetchone()]
       if row is None or row['english'] != u['english'] or row['kind'] != u['kind']
       or row['path'] != u['path'] or row['context'] != u['context']]
ck('english/kind/path/context identici al DB', not bad, bad[:6])
ck('nessuna unita APPROVED / fuori PENDING',
   not [u['idx'] for u in su
        if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('idx senza buchi (1..11) e ordine = sorgente',
   [u['idx'] for u in tu] == list(range(1, 12)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 11 righe 446 - 520', len(tu) == 11 and (first, last) == (446, 520), (len(tu), first, last))
tot = db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0]
before = db.execute('select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0]
after = db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0]
maxl = db.execute('select max(line) from units where path=?', (PATH,)).fetchone()[0]
ck('continua il file: 37 unita prima della riga 446', before == 37, before)
ck('il file prosegue: 11 unita dopo la riga 520', after == 11, after)
ck('file: 59 unita, max(line) = 782', tot == 59 and maxl == 782, (tot, maxl))
nxt = db.execute('select line,context from units where path=? and line>? order by line limit 1', (PATH, last)).fetchone()
ck('confine dopo: riga 534 apre ship:Valkkyiara-Khorasaqra',
   nxt is not None and nxt['line'] == 534 and nxt['context'] == 'ship:Valkkyiara-Khorasaqra',
   tuple(nxt) if nxt else None)
ctxs = []
for u in su:
    if u['context'] not in ctxs:
        ctxs.append(u['context'])
ck('4 contesti in ordine di riga',
   ctxs == ['outfit:"Torji," Lethal Sight', 'outfit:Crimson Halo', 'outfit:Visions of Rime',
            'ship:Valkkyiara-Khorasaqra'], ctxs)
k = collections.Counter(u['kind'] for u in su)
ck('kind: 7 TEXT, 3 DESCRIPTION, 1 VALUE', dict(k) == {'TEXT': 7, 'DESCRIPTION': 3, 'VALUE': 1}, dict(k))
by = {u['idx']: u for u in tu}
ck('8 unita di dato identiche', all(by[i]['italian'] == by[i]['english'] for i in DATA),
   [i for i in sorted(DATA) if by[i]['italian'] != by[i]['english']])
ck('3 unita di prosa tradotte', all(by[i]['italian'].strip() != by[i]['english'].strip() for i in PROSE),
   [i for i in sorted(PROSE) if by[i]['italian'].strip() == by[i]['english'].strip()])
tok = sum(len(TAGS.findall(u['english'])) for u in su) + sum(len(TAGS.findall(u['italian'])) for u in tu)
ck('token: 0 = 0', tok == 0, tok)
a = sum(u['english'].count('"') for u in su)
b = sum(u['italian'].count('"') for u in tu)
ck('virgolette: %d = %d (12)' % (b, a), a == b == 12, (a, b))
ck('virgolette: parita per unita e nessuna dispari',
   not [u['idx'] for u in tu if u['english'].count('"') != u['italian'].count('"')]
   and not [u['idx'] for u in tu if u['italian'].count('"') % 2])
ck('tab: 0 nel sorgente e 0 nel tradotto',
   not [u for u in su if '\t' in u['english']] and not [u for u in tu if '\t' in u['italian']])
ck('quadre e backtick: nessuna', not [u for u in tu if '[' in u['italian'] or '`' in u['italian']])
ck('nessuna traduzione vuota', all(u['italian'].strip() for u in tu))
NONLAT = re.compile(r'[^\x00-\x7F\u00C0-\u024F\u2018\u2019\u201C\u201D\u2013\u2014\u2026]')
ck('nessun carattere non latino', not [u for u in tu if NONLAT.search(u['italian'])])
ck('nessun trattino lungo o virgoletta curva',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D')])
ck('nessun accento sostitutivo',
   not [u['idx'] for u in tu if re.search(r"\b(e|piu|perche|cosi|gia|puo|ciita|verita)'", u['italian'])])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate 0,55-1,90', 0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
print('rapporto IT/EN: min %.2f max %.2f' % (min(rs), max(rs)))
grp = {}
for u in su:
    grp.setdefault(u['english'], []).append(u['idx'])
ck('nessun duplicato inglese', not [v for v in grp.values() if len(v) > 1])
ck('nessuna resa ripetuta',
   not [k2 for k2, n in collections.Counter(u['italian'] for u in tu).items() if n > 1])
merged = {}
for f in sorted(glob.glob(os.path.join(HERE, 'parts', 'part*.json'))):
    for kk, v in json.load(open(f, encoding='utf-8')).items():
        merged[int(kk)] = v
ck('le parti ricostruiscono translation.json',
   {i: '\t' * (len(by[i]['english']) - len(by[i]['english'].lstrip('\t'))) + v for i, v in merged.items()}
   == {u['idx']: u['italian'] for u in tu})
ck('le parti coprono 1..11', sorted(merged) == list(range(1, 12)), len(merged))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('parole EN %d -> IT %d · sha256[:16] %s'
      % (sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu), h[:16]))
print()
print('FAIL:', len(fail), '·', 'verify L83 superato' if not fail else 'verify L83 fallito')
raise SystemExit(0 if not fail else 1)
