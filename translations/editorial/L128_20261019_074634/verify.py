r"""verify.py — L128 (`data/incipias/incipias first contact.txt`, 43 unita', righe 343-439). **CHIUDE IL FILE.**

Invariante di **file**: legge i **tre** `translation.json` del percorso (L126, L127, L128) e dimostra che il file è
**161/161**, con **sovrapposti = 0** e `max(line) = 439`. Ricalcolato dal repository e da `state.db`.

Misure proprie: **3 contesti** (2 + 1 + 40), **33 `MISSION_TEXT`**, **4 `UI_LABEL`** identiche, **3 `LOGBOOK`**, **1
`DIALOG`**, **1 `VALUE`** identico, **1 `DESCRIPTION`**, **30 unita' con tab**, **43 virgolette** (tre unita' con una
sola), **6 token** in **5 famiglie**, **43 testi distinti**.
"""
import collections
import glob
import hashlib
import json
import os
import re
import sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
ROOT = os.path.abspath(os.path.join(L10N, '..'))
PATH = 'data/incipias/incipias first contact.txt'
LOTS = [os.path.join(L10N, 'staging/editorial', d) for d in
        ('L126_20261019_073300', 'L127_20261019_073900', 'L128_20261019_074634')]
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
ck('idx 1..43 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 44)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 43 righe 343 - 439', len(tu) == 43 and (first, last) == (343, 439), (len(tu), first, last))
ck('118 unita prima della riga 343 (L126 + L127)',
   db.execute('select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0] == 118)
ck('ZERO unita dopo: il lotto chiude il file',
   db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0] == 0)
ck('max(line) del file = 439', db.execute('select max(line) from units where path=?', (PATH,)).fetchone()[0] == 439)
ck('tipi: 33 MISSION_TEXT · 4 UI_LABEL · 3 LOGBOOK · 1 DIALOG · 1 VALUE · 1 DESCRIPTION',
   collections.Counter(u['kind'] for u in su) == {'MISSION_TEXT': 33, 'UI_LABEL': 4, 'LOGBOOK': 3, 'DIALOG': 1,
                                                  'VALUE': 1, 'DESCRIPTION': 1},
   collections.Counter(u['kind'] for u in su))
LAB = [u['idx'] for u in su if u['kind'] == 'UI_LABEL']
ck('le 4 UI_LABEL (11, 13, 38, 42) sono identiche al sorgente',
   LAB == [11, 13, 38, 42]
   and [by[i]['italian'] for i in LAB] == ['has incipias ship', 'initial choice', 'odd question', 'end no time'])
ck('il VALUE (unita 4) e identico al sorgente',
   by[4]['italian'] == by[4]['english'] == 'Bring Incipias back to <planet>')
ck('tutte PENDING',
   not [u['idx'] for u in su
        if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('tutte le unita prosaiche sono tradotte',
   not [u['idx'] for u in tu if u['kind'] not in ('UI_LABEL', 'VALUE')
        and u['italian'].strip() == u['english'].strip()])
tk = collections.Counter(t for u in su for t in TAGS.findall(u['english']))
ck('6 token in 5 famiglie, nelle unita 1/4/5/6/19, uguali in traduzione',
   dict(tk) == {'<ship>': 2, '<planet>': 1, '<destination>': 1, '<origin>': 1, '<bunks>': 1}
   and [u['idx'] for u in su if TAGS.findall(u['english'])] == [1, 4, 5, 6, 19]
   and not [u['idx'] for u in tu if TAGS.findall(u['english']) != TAGS.findall(u['italian'])],
   (dict(tk), [u['idx'] for u in su if TAGS.findall(u['english'])]))
tabs = [u['idx'] for u in su if u['english'].startswith('\t')]
ck('30 unita con tab iniziale, le stesse in traduzione',
   len(tabs) == 30 and tabs == [u['idx'] for u in tu if u['italian'].startswith('\t')], len(tabs))
ck('conteggio dei tab identico per unita',
   not [u['idx'] for u in tu if u['english'].count('\t') != u['italian'].count('\t')])
ck('43 virgolette, stesse per unita',
   sum(u['english'].count('"') for u in su) == 43 == sum(u['italian'].count('"') for u in tu)
   and not [u['idx'] for u in tu if u['english'].count('"') != u['italian'].count('"')])
ck('una sola virgoletta nelle unita 28, 30, 36',
   [u['idx'] for u in su if u['english'].count('"') % 2] == [28, 30, 36]
   and all(by[i]['italian'].count('"') == 1 for i in (28, 30, 36)))
ck('ZERO quadre e zero backtick nella traduzione',
   not [u for u in tu if any(c in u['italian'] for c in '[]`')])
seen = collections.OrderedDict()
for u in su:
    seen[u['context']] = seen.get(u['context'], 0) + 1
ck('3 contesti: 2 / 1 / 40',
   list(seen.items()) == [('mission:Incipias: Fix Saves Missing Language', 2),
                          ('mission:Incipias: No Help For The Stranded', 1),
                          ('mission:Incipias: Help The Stranded 2', 40)], list(seen.items()))
ck('43 testi inglesi distinti per 43 unita', len({u['english'] for u in su}) == 43)
it_grp = {}
for u in tu:
    it_grp.setdefault(u['italian'], []).append(u)
ck('nessun duplicato italiano',
   not [g for g in it_grp.values() if len(g) > 1], [[v['idx'] for v in g] for g in it_grp.values() if len(g) > 1])
LOW = ' '.join(u['italian'] for u in tu).lower()
COMP = ('giorno-momento', 'protettore-di-vite', 'calamità-meteo', 'aiutante-esterno', 'capi-governatori',
        'domande-quesiti', 'tempo-pazienza', 'vuoto-spazio', 'osservare-studiare', 'mondo-origine',
        'orgoglio-azione', 'ponte-stellare', 'sale-nuvole', 'incontro-colloquio', 'comprensione-triste')
ck('stile Incipias: 15 composti con trattino', all(c in LOW for c in COMP), [c for c in COMP if c not in LOW])
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
ck('le tre parti ricostruiscono translation.json (1..43)',
   sorted(merged) == list(range(1, 44)) and merged == {u['idx']: u['italian'] for u in tu})

# --- invariante di FILE: i tre lotti insieme devono coprire 161/161 righe, senza sovrapposizioni ---
seen_lines = collections.Counter()
per_lot = []
for lot in LOTS:
    d = json.load(open(os.path.join(lot, 'translation.json'), encoding='utf-8'))['units']
    per_lot.append(len(d))
    for u in d:
        assert u['path'] == PATH, (lot, u['path'])
        seen_lines[u['line']] += 1
ck('i tre lotti hanno 55 + 63 + 43 = 161 unita', per_lot == [55, 63, 43] and sum(per_lot) == 161, per_lot)
ck('file coperto 161/161 righe', len(seen_lines) == 161
   and len(seen_lines) == db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0],
   (len(seen_lines), db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0]))
ck('sovrapposti = 0', [l for l, n in seen_lines.items() if n > 1] == [],
   [l for l, n in seen_lines.items() if n > 1])
ck('max(line) coperta = 439', max(seen_lines) == 439, max(seen_lines))
ck('nessuna unita del file resta fuori', not [l for l, _ in db.execute(
    'select line,id from units where path=?', (PATH,)).fetchall() if l not in seen_lines])
ck('nessun altro lotto rivendica queste righe',
   not [f for f in os.listdir(os.path.join(L10N, 'staging/editorial'))
        if f.startswith('L') and os.path.exists(os.path.join(L10N, 'staging/editorial', f, 'translation.json'))
        and os.path.join(L10N, 'staging/editorial', f) not in LOTS
        and any(u['path'] == PATH for u in json.load(open(os.path.join(L10N, 'staging/editorial', f,
                'translation.json'), encoding='utf-8'))['units'])])
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('file CHIUSO: 161/161 (100.0%) · tre lotti 55 + 63 + 43 · sovrapposti 0 · max(line) 439')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L128 superato' if not fail else 'verify L128 fallito')
raise SystemExit(0 if not fail else 1)
