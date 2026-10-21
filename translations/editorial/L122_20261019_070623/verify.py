r"""verify.py — L122 (`data/human/campaign events.txt`, 42 unita', righe 1338-3468)

Il lotto **chiude il file**, quindi l'invariante è **di file** (come in L116 e L119): si leggono i tre
`translation.json` del percorso (`L120`, `L121`, `L122`) e si dimostra che l'unione copre **tutte** le 150 unità
del file.

Misure attese: **150 unità**, `max(line) = 3468`, **108 prima** della riga 1338, **0 dopo** la 3468,
**sovrapposti = 0**, **tre lotti**; il segmento L122 con **42 unità**, `{'DESCRIPTION': 41, 'MISSION_TEXT': 1}`,
**18 contesti**, **36 testi distinti**, **21 unità con tab**, **8 virgolette**, **zero token**.
"""
import collections
import hashlib
import json
import os
import re
import sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
ROOT = os.path.abspath(os.path.join(L10N, '..'))
PATH = 'data/human/campaign events.txt'
TAGS = re.compile(r'<[^<>]+>')
su = sorted(json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
by = {u['idx']: u for u in tu}
lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
fail = []


def ck(n, c, d=''):
    print('%-70s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente', not [u for u in su if lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck('idx 1..42 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 43)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 42 righe 1338 - 3468', len(tu) == 42 and (first, last) == (1338, 3468), (len(tu), first, last))
ck('tipi: 41 DESCRIPTION · 1 MISSION_TEXT',
   collections.Counter(u['kind'] for u in su) == {'DESCRIPTION': 41, 'MISSION_TEXT': 1},
   collections.Counter(u['kind'] for u in su))
ck('nessun VALUE e nessuna UI_LABEL nel segmento',
   not [u['idx'] for u in su if u['kind'] in ('VALUE', 'UI_LABEL')])
ck('tutte PENDING',
   not [u['idx'] for u in su
        if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('tutte le unita sono tradotte',
   not [u['idx'] for u in tu if u['italian'].strip() == u['english'].strip()])
tabs = [u['idx'] for u in su if u['english'].startswith('\t')]
ck('21 unita con tab iniziale, le stesse in traduzione',
   len(tabs) == 21 and tabs == [u['idx'] for u in tu if u['italian'].startswith('\t')], len(tabs))
ck('conteggio dei tab identico per unita',
   not [u['idx'] for u in tu if u['english'].count('\t') != u['italian'].count('\t')])
ck('8 virgolette, nelle unita 19, 21 e 32',
   sum(u['english'].count('"') for u in su) == 8 == sum(u['italian'].count('"') for u in tu)
   and [u['idx'] for u in su if '"' in u['english']] == [19, 21, 32])
ck('ZERO token (asserito)', collections.Counter(t for u in su for t in TAGS.findall(u['english'])) == {}
   == collections.Counter(t for u in tu for t in TAGS.findall(u['italian'])))
ck('nessun backtick e nessuna quadra nella traduzione',
   not [u for u in tu if '`' in u['italian'] or '[' in u['italian'] or ']' in u['italian']])
seen = collections.Counter(u['context'] for u in su)
ck('18 contesti: 8x2, 4x1, 4x4, 2x3',
   len(seen) == 18 and collections.Counter(seen.values()) == {2: 8, 1: 4, 4: 4, 3: 2},
   collections.Counter(seen.values()))
grp = collections.Counter(u['english'] for u in su)
ck('36 testi inglesi distinti per 42 unita', len(grp) == 36, len(grp))
ck('nessun gruppo con due rese diverse',
   not [k for k in grp if len({by[u['idx']]['italian'] for u in su if u['english'] == k}) > 1])
it_grp = {}
for u in tu:
    it_grp.setdefault(u['italian'], []).append(u)
ck('nessun duplicato italiano non spiegato dal sorgente',
   not [g for g in it_grp.values() if len(g) > 1 and len({v['english'] for v in g}) > 1])
NONLAT = re.compile(r'[^\x00-\x7F\u00C0-\u024F]')
ck('nessun carattere non latino', not [u for u in tu if NONLAT.search(u['italian'])])
ck('nessun trattino lungo, virgoletta curva o ellissi tipografica',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate', 0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
ck('registro approvato: nessun «voi» e nessuna cortesia «lei»',
   not [u['idx'] for u in tu if re.search(
       r'\b(avete|potete|potrete|siete|vostro|vostra|vostri|vostre|Pensi quello|la sua nave|la farò)\b',
       u['italian'])])
merged = {}
for f in sorted(os.listdir(os.path.join(HERE, 'parts'))):
    if f.endswith('.json'):
        for k, v in json.load(open(os.path.join(HERE, 'parts', f), encoding='utf-8')).items():
            merged[int(k)] = v
ck('le tre parti ricostruiscono translation.json (1..42)',
   sorted(merged) == list(range(1, 43)) and merged == {u['idx']: u['italian'] for u in tu})
# --- INVARIANTE DI FILE ------------------------------------------------------------------
lots = []
for f in sorted(os.listdir(os.path.join(L10N, 'staging/editorial'))):
    if not f.startswith('L'):
        continue
    p = os.path.join(L10N, 'staging/editorial', f, 'translation.json')
    if not os.path.exists(p):
        continue
    d = json.load(open(p, encoding='utf-8'))['units']
    if d and d[0]['path'] == PATH:
        lots.append((f, d))
ck('tre lotti coprono il file', len(lots) == 3 and [l[0][:4] for l in lots] == ['L120', 'L121', 'L122'],
   [l[0] for l in lots])
tot = db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0]
maxl = db.execute('select max(line) from units where path=?', (PATH,)).fetchone()[0]
ck('file: 150 unita, max(line) = 3468', tot == 150 and maxl == 3468, (tot, maxl))
lines_cov = [u['line'] for _, d in lots for u in d]
ck('150/150 righe coperte dai tre lotti', len(lines_cov) == 150 and len(set(lines_cov)) == 150,
   (len(lines_cov), len(set(lines_cov))))
ck('sovrapposti = 0', len(lines_cov) == len(set(lines_cov)))
db_lines = {r[0] for r in db.execute('select line from units where path=?', (PATH,))}
ck('l\'unione coincide con le righe del database', set(lines_cov) == db_lines,
   sorted(db_lines - set(lines_cov))[:5])
ck('108 unita prima della riga 1338, 0 dopo la 3468',
   db.execute('select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0] == 108
   and db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0] == 0)
ck('nessun lotto oltre la coda del file', max(u['line'] for _, d in lots for u in d) == 3468)
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('copertura file: 150/150 (100.0%) · 3 lotti · 6961 EN -> 6788 IT parole')
print('L122: parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L122 superato (file chiuso)' if not fail else 'verify L122 fallito')
raise SystemExit(0 if not fail else 1)
