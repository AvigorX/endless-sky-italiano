r"""verify.py — L121 (`data/human/campaign events.txt`, 56 unita', righe 282-1332)

Invariante di **segmento** (il file non si chiude): 150 unità, `max(line) = 3468`, **52 prima** della riga 282
(L120), **42 dopo** la 1332, confine alla riga **1338** (`event:memorial on Deep`). Ricalcolato dal repository e da
`state.db`, senza fidarsi di `check.py`.

Misure proprie: **41 `DESCRIPTION`**, **14 `MISSION_TEXT`**, **1 `UI_LABEL`** (identica al sorgente), **12
contesti**, **28 unità con tab**, **46 virgolette**, **1 token** `<origin>`, **52 testi distinti** con **4 coppie**.
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
ck('idx 1..56 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 57)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 56 righe 282 - 1332', len(tu) == 56 and (first, last) == (282, 1332), (len(tu), first, last))
tot = db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0]
before = db.execute('select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0]
after = db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0]
maxl = db.execute('select max(line) from units where path=?', (PATH,)).fetchone()[0]
ck('file: 150 unita, max(line) = 3468', tot == 150 and maxl == 3468, (tot, maxl))
ck('52 unita prima della riga 282 (L120)', before == 52, before)
ck('42 unita dopo la riga 1332', after == 42, after)
ck('il confine: la riga 1338 apre event:memorial on Deep',
   db.execute('select line,context from units where path=? and line>? order by line limit 1',
              (PATH, last)).fetchone() == (1338, 'event:memorial on Deep'))
ck('tipi: 41 DESCRIPTION · 14 MISSION_TEXT · 1 UI_LABEL',
   collections.Counter(u['kind'] for u in su) == {'DESCRIPTION': 41, 'MISSION_TEXT': 14, 'UI_LABEL': 1},
   collections.Counter(u['kind'] for u in su))
LAB = [u['idx'] for u in su if u['kind'] == 'UI_LABEL']
ck('la UI_LABEL (unita 20) e identica al sorgente',
   LAB == [20] and by[20]['italian'] == by[20]['english'] == 'new stock')
ck('tutte PENDING',
   not [u['idx'] for u in su
        if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('tutte le unita prosaiche sono tradotte',
   not [u['idx'] for u in tu if u['kind'] != 'UI_LABEL' and u['italian'].strip() == u['english'].strip()])
tabs = [u['idx'] for u in su if u['english'].startswith('\t')]
ck('28 unita con tab iniziale, le stesse in traduzione',
   len(tabs) == 28 and tabs == [u['idx'] for u in tu if u['italian'].startswith('\t')], len(tabs))
ck('conteggio dei tab identico per unita',
   not [u['idx'] for u in tu if u['english'].count('\t') != u['italian'].count('\t')])
ck('46 virgolette in inglese e in italiano',
   sum(u['english'].count('"') for u in su) == 46 == sum(u['italian'].count('"') for u in tu))
ck('virgolette per unita: stesso numero',
   not [u['idx'] for u in tu if u['english'].count('"') != u['italian'].count('"')])
ck('1 token <origin>',
   collections.Counter(t for u in su for t in TAGS.findall(u['english'])) == {'<origin>': 1}
   == collections.Counter(t for u in tu for t in TAGS.findall(u['italian'])))
ck('token per unita: stessi simboli e stesso ordine',
   not [u['idx'] for u in tu if TAGS.findall(u['italian']) != TAGS.findall(u['english'])])
seen = collections.Counter(u['context'] for u in su)
ck('12 contesti, distribuzione 15/10/5/4x3/3x2/2x4',
   len(seen) == 12 and collections.Counter(seen.values()) == {15: 1, 10: 1, 5: 1, 4: 3, 3: 2, 2: 4},
   collections.Counter(seen.values()))
grp = collections.Counter(u['english'] for u in su)
ck('52 testi inglesi distinti, 4 coppie ripetute',
   len(grp) == 52 and collections.Counter(grp.values()) == {1: 48, 2: 4}, collections.Counter(grp.values()))
ck('nessun gruppo con due rese diverse',
   not [k for k in grp if len({by[u['idx']]['italian'] for u in su if u['english'] == k}) > 1])
it_grp = {}
for u in tu:
    it_grp.setdefault(u['italian'], []).append(u)
ck('nessun duplicato italiano non spiegato dal sorgente',
   not [g for g in it_grp.values() if len(g) > 1 and len({v['english'] for v in g}) > 1])
ck('nessun backtick e nessuna quadra nella traduzione',
   not [u for u in tu if '`' in u['italian'] or '[' in u['italian'] or ']' in u['italian']])
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
ck('le tre parti ricostruiscono translation.json (1..56)',
   sorted(merged) == list(range(1, 57)) and merged == {u['idx']: u['italian'] for u in tu})
ck('nessun altro lotto rivendica queste righe',
   not [f for f in os.listdir(os.path.join(L10N, 'staging/editorial'))
        if f.startswith('L') and os.path.exists(os.path.join(L10N, 'staging/editorial', f, 'translation.json'))
        and f != os.path.basename(HERE)
        and any(u['path'] == PATH and 282 <= u['line'] <= 1332
                for u in json.load(open(os.path.join(L10N, 'staging/editorial', f, 'translation.json'),
                                        encoding='utf-8'))['units'])])
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('copertura file: 108/150 (72.0%) · segmento (282, 1332) · 42 unita dopo')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L121 superato' if not fail else 'verify L121 fallito')
raise SystemExit(0 if not fail else 1)
