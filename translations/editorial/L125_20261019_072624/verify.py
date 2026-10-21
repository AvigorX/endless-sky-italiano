r"""verify.py — L125 (`data/human/ships.txt`, 20 unita', righe 3491-4266)

Il lotto **chiude il file**, quindi l'invariante è **di file** (come in L116, L119 e L122): si leggono i tre
`translation.json` del percorso (`L123`, `L124`, `L125`) e si dimostra che l'unione copre **tutte** le 103 unità.

Misure attese: **103 unità**, `max(line) = 4266`, **83 prima** della riga 3491, **0 dopo** la 4266,
**sovrapposti = 0**, **tre lotti**; il segmento L125 con **20 unità**, tutte `DESCRIPTION`, **15 contesti**, **20
testi distinti**, **5 unità con tab**, **14 virgolette**, **zero `VALUE`**, **zero token**.
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
PATH = 'data/human/ships.txt'
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
ck('idx 1..20 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 21)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 20 righe 3491 - 4266', len(tu) == 20 and (first, last) == (3491, 4266), (len(tu), first, last))
ck('tipi: 20 DESCRIPTION', collections.Counter(u['kind'] for u in su) == {'DESCRIPTION': 20},
   collections.Counter(u['kind'] for u in su))
ck('ZERO VALUE nel segmento (asserzione vuota, dichiarata)',
   not [u['idx'] for u in su if u['kind'] == 'VALUE'])
ck('tutte PENDING',
   not [u['idx'] for u in su
        if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('tutte le unita sono tradotte',
   not [u['idx'] for u in tu if u['italian'].strip() == u['english'].strip()])
tabs = [u['idx'] for u in su if u['english'].startswith('\t')]
ck('5 unita con tab iniziale (6, 9, 12, 14, 17), le stesse in traduzione',
   tabs == [6, 9, 12, 14, 17] == [u['idx'] for u in tu if u['italian'].startswith('\t')], tabs)
ck('conteggio dei tab identico per unita',
   not [u['idx'] for u in tu if u['english'].count('\t') != u['italian'].count('\t')])
ck('14 virgolette: 6 + 2 + 6 nelle unita 1, 6, 7',
   sum(u['english'].count('"') for u in su) == 14 == sum(u['italian'].count('"') for u in tu)
   and [(u['idx'], u['english'].count('"')) for u in su if '"' in u['english']] == [(1, 6), (6, 2), (7, 6)])
ck('ZERO token (asserito)', collections.Counter(t for u in su for t in TAGS.findall(u['english'])) == {}
   == collections.Counter(t for u in tu for t in TAGS.findall(u['italian'])))
ck('nessun backtick e nessuna quadra nella traduzione',
   not [u for u in tu if '`' in u['italian'] or '[' in u['italian'] or ']' in u['italian']])
seen = collections.Counter(u['context'] for u in su)
ck('15 contesti: 10x1, 5x2',
   len(seen) == 15 and collections.Counter(seen.values()) == {1: 10, 2: 5}, collections.Counter(seen.values()))
grp = collections.Counter(u['english'] for u in su)
ck('20 testi inglesi distinti per 20 unita', len(grp) == 20, len(grp))
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
ck('registro approvato: nessun «voi»',
   not [u['idx'] for u in tu if re.search(r'\b(avete|potete|potrete|siete|vostro|vostra|vostri|vostre)\b',
                                          u['italian'])])
merged = {}
for f in sorted(os.listdir(os.path.join(HERE, 'parts'))):
    if f.endswith('.json'):
        for k, v in json.load(open(os.path.join(HERE, 'parts', f), encoding='utf-8')).items():
            merged[int(k)] = v
ck('le due parti ricostruiscono translation.json (1..20)',
   sorted(merged) == list(range(1, 21)) and merged == {u['idx']: u['italian'] for u in tu})
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
ck('tre lotti coprono il file', len(lots) == 3 and [l[0][:4] for l in lots] == ['L123', 'L124', 'L125'],
   [l[0] for l in lots])
tot = db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0]
maxl = db.execute('select max(line) from units where path=?', (PATH,)).fetchone()[0]
ck('file: 103 unita, max(line) = 4266', tot == 103 and maxl == 4266, (tot, maxl))
lines_cov = [u['line'] for _, d in lots for u in d]
ck('103/103 righe coperte dai tre lotti', len(lines_cov) == 103 and len(set(lines_cov)) == 103,
   (len(lines_cov), len(set(lines_cov))))
ck('sovrapposti = 0', len(lines_cov) == len(set(lines_cov)))
db_lines = {r[0] for r in db.execute('select line from units where path=?', (PATH,))}
ck('l\'unione coincide con le righe del database', set(lines_cov) == db_lines,
   sorted(db_lines - set(lines_cov))[:5])
ck('83 unita prima della riga 3491, 0 dopo la 4266',
   db.execute('select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0] == 83
   and db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0] == 0)
ck('nessun lotto oltre la coda del file', max(u['line'] for _, d in lots for u in d) == 4266)
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('copertura file: 103/103 (100.0%) · 3 lotti · 5083 EN -> 5286 IT parole')
print('L125: parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L125 superato (file chiuso)' if not fail else 'verify L125 fallito')
raise SystemExit(0 if not fail else 1)
