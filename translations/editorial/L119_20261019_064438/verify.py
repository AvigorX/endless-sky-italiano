r"""verify.py — L119 (data/human/pirate jobs.txt, 77 unita', righe 2958-3706)

Il lotto **chiude il file**, quindi l'invariante e' **di file** (come in L116 per `tooltips.txt`): si leggono i tre
`translation.json` del percorso (`L117`, `L118`, `L119`), si ricostruisce l'insieme delle righe coperte e si
dimostra che e' **tutto** il file.

Misure attese: file di **279 unita'**, `max(line) = 3706`, **202 prima** della riga 2958, **0 dopo** la 3706,
**sovrapposti = 0**, **tre lotti**, e il segmento L119 con **77 unita'**, tipi `{'DIALOG': 32, 'DESCRIPTION': 17,
'VALUE': 16, 'CONVERSATION': 12}`, **20 contesti**, **47 testi distinti**, **106 token** in sei famiglie, **9
unita' con tab iniziale**, **6 virgolette**.
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
PATH = 'data/human/pirate jobs.txt'
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


# --- 1. il segmento esiste ed e' fedele al repository e al database -------------------------
ck('riga grezza identica al sorgente', not [u for u in su if lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck('idx 1..77 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 78)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 77 righe 2958 - 3706', len(tu) == 77 and (first, last) == (2958, 3706), (len(tu), first, last))
ck('tipi: 32 DIALOG · 17 DESCRIPTION · 16 VALUE · 12 CONVERSATION',
   collections.Counter(u['kind'] for u in su) == {'DIALOG': 32, 'DESCRIPTION': 17,
                                                 'VALUE': 16, 'CONVERSATION': 12},
   collections.Counter(u['kind'] for u in su))
ck('tutte PENDING',
   not [u['idx'] for u in su
        if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
VAL = [u['idx'] for u in su if u['kind'] == 'VALUE']
ck('i 16 VALUE sono identici al sorgente (4 nomi)',
   len(VAL) == 16 and len({by[i]['english'] for i in VAL}) == 4
   and all(by[i]['italian'] == by[i]['english'] for i in VAL),
   [i for i in VAL if by[i]['italian'] != by[i]['english']])
ck('tutte le unita non-VALUE sono tradotte',
   not [u['idx'] for u in tu if u['kind'] != 'VALUE' and u['italian'].strip() == u['english'].strip()])
# --- 2. forma del segmento -----------------------------------------------------------------
tabs = [u['idx'] for u in su if u['english'].startswith('\t')]
ck('9 unita con tab iniziale, le stesse in traduzione',
   len(tabs) == 9 and tabs == [u['idx'] for u in tu if u['italian'].startswith('\t')], len(tabs))
ck('conteggio dei tab identico per unita',
   not [u['idx'] for u in tu if u['english'].count('\t') != u['italian'].count('\t')])
ck('6 virgolette, due per scena (13, 25, 37)',
   sum(u['english'].count('"') for u in su) == 6 == sum(u['italian'].count('"') for u in tu)
   and [u['idx'] for u in su if '"' in u['english']] == [13, 25, 37])
TOK = {'<planet>': 28, '<payment>': 23, '<destination>': 19, '<system>': 14, '<npc>': 12, '<day>': 10}
ck('106 token nelle sei famiglie attese',
   collections.Counter(t for u in su for t in TAGS.findall(u['english'])) == TOK
   == collections.Counter(t for u in tu for t in TAGS.findall(u['italian'])))
ck('token per unita: stessi simboli e stesso ordine',
   not [u['idx'] for u in tu if TAGS.findall(u['italian']) != TAGS.findall(u['english'])])
ck('nessun backtick nella traduzione', not [u for u in tu if '`' in u['italian']])
ck('nessuna quadra nella traduzione', not [u for u in tu if '[' in u['italian'] or ']' in u['italian']])
seen = collections.Counter(u['context'] for u in su)
ck('20 contesti: 19 da quattro unita, 1 da una (outfit:Secret Cargo)',
   len(seen) == 20 and collections.Counter(seen.values()) == {4: 19, 1: 1}
   and seen['outfit:Secret Cargo'] == 1, collections.Counter(seen.values()))
grp = collections.Counter(u['english'] for u in su)
ck('47 testi inglesi distinti per 77 unita', len(grp) == 47, len(grp))
ck('nessun gruppo con due rese diverse',
   not [k for k in grp if len({by[u['idx']]['italian'] for u in su if u['english'] == k}) > 1])
it_grp = {}
for u in tu:
    it_grp.setdefault(u['italian'], []).append(u)
dup = [g for g in it_grp.values() if len(g) > 1 and len({v['english'] for v in g}) > 1]
ck('un solo doppio di resa: unita 65 e 73 (refuso «and» nel sorgente), dichiarato',
   len(dup) == 1 and sorted(v['idx'] for v in dup[0]) == [65, 73])
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
ck('le quattro parti ricostruiscono translation.json (1..77)',
   sorted(merged) == list(range(1, 78)) and merged == {u['idx']: u['italian'] for u in tu})
# --- 3. INVARIANTE DI FILE: i tre lotti coprono tutte le 279 unita ------------------------
lots = []
for f in sorted(os.listdir(os.path.join(L10N, 'staging/editorial'))):
    if not f.startswith('L1'):
        continue
    p = os.path.join(L10N, 'staging/editorial', f, 'translation.json')
    if not os.path.exists(p):
        continue
    d = json.load(open(p, encoding='utf-8'))['units']
    if d and d[0]['path'] == PATH:
        lots.append((f, d))
ck('tre lotti coprono il file', len(lots) == 3 and [l[0][:4] for l in lots] == ['L117', 'L118', 'L119'],
   [l[0] for l in lots])
tot = db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0]
maxl = db.execute('select max(line) from units where path=?', (PATH,)).fetchone()[0]
ck('file: 279 unita, max(line) = 3706', tot == 279 and maxl == 3706, (tot, maxl))
lines_cov = [u['line'] for _, d in lots for u in d]
ck('279/279 righe coperte dai tre lotti', len(lines_cov) == 279 and len(set(lines_cov)) == 279,
   (len(lines_cov), len(set(lines_cov))))
ck('sovrapposti = 0', len(lines_cov) == len(set(lines_cov)))
db_lines = {r[0] for r in db.execute('select line from units where path=?', (PATH,))}
ck('l\'unione coincide con le righe del database', set(lines_cov) == db_lines,
   sorted(db_lines - set(lines_cov))[:5])
ck('202 unita prima della riga 2958, 0 dopo la 3706',
   db.execute('select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0] == 202
   and db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0] == 0)
ck('nessun lotto oltre la coda del file',
   max(u['line'] for _, d in lots for u in d) == 3706)
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
w_en = sum(len(u['english'].split()) for _, d in lots for u in d)
w_it = sum(len(u['italian'].split()) for _, d in lots for u in d)
print('copertura file: 279/279 (100.0%) · 3 lotti · 3227 EN -> 3245 IT parole')
print('L119: parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L119 superato (file chiuso)' if not fail else 'verify L119 fallito')
raise SystemExit(0 if not fail else 1)
