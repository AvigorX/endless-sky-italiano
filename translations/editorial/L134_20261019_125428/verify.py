r"""verify.py — L134 (`data/hai/unfettered side missions.txt`, 8 unita', righe 494-510). **CHIUDE IL FILE.**

Invariante di **file**: legge i **tre** `translation.json` del percorso (L132, L133, L134) e dimostra che il file e'
**159/159**, con **sovrapposti = 0** e `max(line) = 510`. Ricalcolato dal repository e da `state.db`.

Misure proprie: **1 contesto**, **8 `MISSION_TEXT`**, **zero `VALUE`**, **zero `UI_LABEL`**, **zero token**; **7 unita'
con tab**; **13 virgolette** (una sola nell'unita' 6); **8 testi distinti**.
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
PATH = 'data/hai/unfettered side missions.txt'
LOTS = [os.path.join(L10N, 'staging/editorial', d) for d in
        ('L132_20261019_124026', 'L133_20261019_124700', 'L134_20261019_125428')]
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
ck('idx 1..8 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 9)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 8 righe 494 - 510', len(tu) == 8 and (first, last) == (494, 510), (len(tu), first, last))
ck('151 unita prima della riga 494 (L132 + L133)',
   db.execute('select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0] == 151)
ck('ZERO unita dopo: il lotto chiude il file',
   db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0] == 0)
ck('max(line) del file = 510', db.execute('select max(line) from units where path=?', (PATH,)).fetchone()[0] == 510)
ck('tipi: 8 MISSION_TEXT', collections.Counter(u['kind'] for u in su) == {'MISSION_TEXT': 8},
   collections.Counter(u['kind'] for u in su))
ck('ZERO VALUE, ZERO UI_LABEL nel segmento (due asserzioni vuote)',
   [u['idx'] for u in su if u['kind'] in ('VALUE', 'UI_LABEL')] == [])
ck('ZERO token nel segmento (asserzione vuota)',
   collections.Counter(t for u in su for t in TAGS.findall(u['english'])) == {})
ck('tutte PENDING',
   not [u['idx'] for u in su
        if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('tutte le unita sono tradotte',
   not [u['idx'] for u in tu if u['italian'].strip() == u['english'].strip()])
ck('spazi iniziali e finali identici al sorgente (8/8)',
   not [u['idx'] for u in tu
        if len(u['italian']) - len(u['italian'].rstrip()) != len(u['english']) - len(u['english'].rstrip())])
tabs = [u['idx'] for u in su if u['english'].startswith('\t')]
ck('7 unita con tab iniziale, le stesse in traduzione',
   len(tabs) == 7 and tabs == [u['idx'] for u in tu if u['italian'].startswith('\t')], len(tabs))
ck('conteggio dei tab identico per unita',
   not [u['idx'] for u in tu if u['english'].count('\t') != u['italian'].count('\t')])
ck('13 virgolette, stesse per unita',
   sum(u['english'].count('"') for u in su) == 13 == sum(u['italian'].count('"') for u in tu)
   and not [u['idx'] for u in tu if u['english'].count('"') != u['italian'].count('"')])
ck('una sola unita dispari (6, una virgoletta)',
   [u['idx'] for u in su if u['english'].count('"') % 2] == [6] and by[6]['italian'].count('"') == 1)
ck('ZERO quadre e zero backtick nella traduzione',
   not [u for u in tu if any(c in u['italian'] for c in '[]`')])
ck('1 contesto: 8 unita', [v for v in collections.Counter(u['context'] for u in su).values()] == [8])
grp = {u['english'].lstrip('\t') for u in tu}
ck('8 testi inglesi distinti su 8 unita', len(grp) == 8, len(grp))
ck('nomi di moduli e modelli restano: Jump Drive, Lightning Bug, Anomalocaris',
   all(t in ' '.join(u['italian'] for u in tu) for t in ('Jump Drive', 'Lightning Bug', 'Anomalocaris')))
CORT = re.findall(r'\bLei\b|(?<![.!?] )\b(?:Suo|Sua|Suoi|Sue)\b', ' '.join(u['italian'] for u in tu))
ck('nessuna forma di cortesia «Lei»', not CORT, CORT)
NONLAT = re.compile(r'[^\x00-\x7F\u00C0-\u024F]')
ck('nessun carattere non latino', not [u for u in tu if NONLAT.search(u['italian'])])
ck('nessun trattino lungo, virgoletta curva o ellissi tipografica',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate', 0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
merged = {}
for f in sorted(os.listdir(os.path.join(HERE, 'parts'))):
    if f.endswith('.json'):
        for k, v in json.load(open(os.path.join(HERE, 'parts', f), encoding='utf-8')).items():
            merged[int(k)] = v
ck('le due parti ricostruiscono translation.json (1..8)',
   sorted(merged) == list(range(1, 9)) and merged == {u['idx']: u['italian'] for u in tu})

# --- invariante di FILE: i tre lotti insieme devono coprire 159/159 righe, senza sovrapposizioni ---
seen_lines = collections.Counter()
per_lot = []
for lot in LOTS:
    d = json.load(open(os.path.join(lot, 'translation.json'), encoding='utf-8'))['units']
    per_lot.append(len(d))
    for u in d:
        assert u['path'] == PATH, (lot, u['path'])
        seen_lines[u['line']] += 1
ck('i tre lotti hanno 84 + 67 + 8 = 159 unita', per_lot == [84, 67, 8] and sum(per_lot) == 159, per_lot)
ck('file coperto 159/159 righe', len(seen_lines) == 159
   and len(seen_lines) == db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0],
   (len(seen_lines), db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0]))
ck('sovrapposti = 0', [l for l, n in seen_lines.items() if n > 1] == [],
   [l for l, n in seen_lines.items() if n > 1])
ck('max(line) coperta = 510', max(seen_lines) == 510, max(seen_lines))
ck('nessuna unita del file resta fuori', not [l for l, _ in db.execute(
    'select line,id from units where path=?', (PATH,)).fetchall() if l not in seen_lines])
ck('nessun altro lotto rivendica queste righe',
   not [f for f in os.listdir(os.path.join(L10N, 'staging/editorial'))
        if f.startswith('L') and os.path.exists(os.path.join(L10N, 'staging/editorial', f, 'translation.json'))
        and os.path.join(L10N, 'staging/editorial', f) not in LOTS
        and any(u['path'] == PATH for u in json.load(open(os.path.join(L10N, 'staging/editorial', f,
                'translation.json'), encoding='utf-8'))['units'])])
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('file CHIUSO: 159/159 (100.0%) · tre lotti 84 + 67 + 8 · sovrapposti 0 · max(line) 510')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L134 superato' if not fail else 'verify L134 fallito')
raise SystemExit(0 if not fail else 1)
