r"""verify.py — L131 (`data/human/boarding missions.txt`, 76 unita', righe 695-959). **CHIUDE IL FILE.**

Invariante di **file**: legge i **tre** `translation.json` del percorso (L129, L130, L131) e dimostra che il file è
**240/240**, con **sovrapposti = 0** e `max(line) = 959`. Ricalcolato dal repository e da `state.db`.

Misure proprie: **2 contesti** (1 / 75), **75 `MISSION_TEXT`**, **1 `DESCRIPTION`**, **zero `VALUE`**, **zero
`UI_LABEL`**; **74 unita' con tab**; **2 virgolette** (unita' 60); **22 token** in **2 famiglie**; **52 testi
distinti** su 76 unita'.
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
PATH = 'data/human/boarding missions.txt'
LOTS = [os.path.join(L10N, 'staging/editorial', d) for d in
        ('L129_20261019_121941', 'L130_20261019_122807', 'L131_20261019_123356')]
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
ck('idx 1..76 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 77)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 76 righe 695 - 959', len(tu) == 76 and (first, last) == (695, 959), (len(tu), first, last))
ck('164 unita prima della riga 695 (L129 + L130)',
   db.execute('select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0] == 164)
ck('ZERO unita dopo: il lotto chiude il file',
   db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0] == 0)
ck('max(line) del file = 959', db.execute('select max(line) from units where path=?', (PATH,)).fetchone()[0] == 959)
ck('tipi: 75 MISSION_TEXT · 1 DESCRIPTION',
   collections.Counter(u['kind'] for u in su) == {'MISSION_TEXT': 75, 'DESCRIPTION': 1},
   collections.Counter(u['kind'] for u in su))
ck('ZERO VALUE e ZERO UI_LABEL nel segmento (due asserzioni vuote)',
   [u['idx'] for u in su if u['kind'] in ('VALUE', 'UI_LABEL')] == [])
ck('tutte PENDING',
   not [u['idx'] for u in su
        if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('tutte le unita sono tradotte',
   not [u['idx'] for u in tu if u['italian'].strip() == u['english'].strip()])
ck('spazi iniziali e finali identici al sorgente (76/76)',
   not [u['idx'] for u in tu
        if len(u['italian']) - len(u['italian'].rstrip()) != len(u['english']) - len(u['english'].rstrip())])
tabs = [u['idx'] for u in su if u['english'].startswith('\t')]
ck('74 unita con tab iniziale, le stesse in traduzione',
   len(tabs) == 74 and tabs == [u['idx'] for u in tu if u['italian'].startswith('\t')], len(tabs))
ck('conteggio dei tab identico per unita',
   not [u['idx'] for u in tu if u['english'].count('\t') != u['italian'].count('\t')])
ck('2 virgolette, entrambe nell unita 60, stesse in traduzione',
   sum(u['english'].count('"') for u in su) == 2 == sum(u['italian'].count('"') for u in tu)
   and [u['idx'] for u in tu if '"' in u['english']] == [60]
   and by[60]['italian'].count('"') == 2)
tk = collections.Counter(t for u in su for t in TAGS.findall(u['english']))
ck('22 token in 2 famiglie, sequenza identica per unita',
   dict(tk) == {'<origin>': 14, '<payment>': 8}
   and not [u['idx'] for u in tu if TAGS.findall(u['english']) != TAGS.findall(u['italian'])], dict(tk))
ck('ZERO quadre e zero backtick nella traduzione',
   not [u for u in tu if any(c in u['italian'] for c in '[]`')])
seen = collections.OrderedDict()
for u in su:
    seen[u['context']] = seen.get(u['context'], 0) + 1
ck('2 contesti: 1 / 75', list(seen.values()) == [1, 75], list(seen.items()))
grp = {}
for u in tu:
    grp.setdefault(u['english'].lstrip('\t'), set()).add(u['italian'])
ck('52 testi inglesi distinti su 76 unita', len(grp) == 52, len(grp))
ck('stesso inglese => stessa resa', not [(k, v) for k, v in grp.items() if len(v) > 1])
CORT = re.findall(r'\bLei\b|(?<![.!?] )\b(?:Suo|Sua|Sue|Suoi)\b', ' '.join(u['italian'] for u in tu))
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
ck('le tre parti ricostruiscono translation.json (1..76)',
   sorted(merged) == list(range(1, 77)) and merged == {u['idx']: u['italian'] for u in tu})

# --- invariante di FILE: i tre lotti insieme devono coprire 240/240 righe, senza sovrapposizioni ---
seen_lines = collections.Counter()
per_lot = []
for lot in LOTS:
    d = json.load(open(os.path.join(lot, 'translation.json'), encoding='utf-8'))['units']
    per_lot.append(len(d))
    for u in d:
        assert u['path'] == PATH, (lot, u['path'])
        seen_lines[u['line']] += 1
ck('i tre lotti hanno 89 + 75 + 76 = 240 unita', per_lot == [89, 75, 76] and sum(per_lot) == 240, per_lot)
ck('file coperto 240/240 righe', len(seen_lines) == 240
   and len(seen_lines) == db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0],
   (len(seen_lines), db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0]))
ck('sovrapposti = 0', [l for l, n in seen_lines.items() if n > 1] == [],
   [l for l, n in seen_lines.items() if n > 1])
ck('max(line) coperta = 959', max(seen_lines) == 959, max(seen_lines))
ck('nessuna unita del file resta fuori', not [l for l, _ in db.execute(
    'select line,id from units where path=?', (PATH,)).fetchall() if l not in seen_lines])
ck('nessun altro lotto rivendica queste righe',
   not [f for f in os.listdir(os.path.join(L10N, 'staging/editorial'))
        if f.startswith('L') and os.path.exists(os.path.join(L10N, 'staging/editorial', f, 'translation.json'))
        and os.path.join(L10N, 'staging/editorial', f) not in LOTS
        and any(u['path'] == PATH for u in json.load(open(os.path.join(L10N, 'staging/editorial', f,
                'translation.json'), encoding='utf-8'))['units'])])
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('file CHIUSO: 240/240 (100.0%) · tre lotti 89 + 75 + 76 · sovrapposti 0 · max(line) 959')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L131 superato' if not fail else 'verify L131 fallito')
raise SystemExit(0 if not fail else 1)
