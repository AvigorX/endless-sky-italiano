r"""verify.py — L117 (data/human/pirate jobs.txt, 98 unita', righe 20-1624)

Invariante di **segmento**, indipendente da `check.py`: rilegge il repository originale, `state.db`, i
`parts/` e `translation.json`, e ricalcola tutto.

Misure attese: **0 unita' prima** della riga 20 (primo lotto del file), **181 dopo** la 1624, file di **279
unita'**, `max(line) = 3706`, confine alla riga **1627** (`mission:Highly Wanted Passenger (Core)`).
**98 unita'** con tipi `{'VALUE': 31, 'DESCRIPTION': 31, 'MISSION_TEXT': 31, 'DIALOG': 5}`, **31 contesti**
(26 con tre unita', 5 con quattro), **26 testi distinti**, **108 token** in sei famiglie, **2 virgolette**
(solo l'unita' 81). I **31 `VALUE`** sono identici al sorgente: sono nomi di missione (decisione 259/L103).
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
PATH = 'data/human/pirate jobs.txt'
su = sorted(json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
TAGS = re.compile(r'<[^<>]+>')
fail = []


def ck(n, c, d=''):
    print('%-72s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
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
ck('idx 1..98 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 99)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 98 righe 20 - 1624', len(tu) == 98 and (first, last) == (20, 1624), (len(tu), first, last))
tot = db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0]
before = db.execute('select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0]
after = db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0]
maxl = db.execute('select max(line) from units where path=?', (PATH,)).fetchone()[0]
ck('0 unita prima della riga 20 (primo lotto del file)', before == 0, before)
ck('181 unita dopo la riga 1624', after == 181, after)
ck('file: 279 unita, max(line) = 3706', tot == 279 and maxl == 3706, (tot, maxl))
ck('il confine: la riga 1627 apre mission:Highly Wanted Passenger (Core)',
   db.execute('select line,context from units where path=? and line>? order by line limit 1',
              (PATH, last)).fetchone() == (1627, 'mission:Highly Wanted Passenger (Core)'))
ck('tipi: 31 VALUE · 31 DESCRIPTION · 31 MISSION_TEXT · 5 DIALOG',
   collections.Counter(u['kind'] for u in su) == {'VALUE': 31, 'DESCRIPTION': 31,
                                                 'MISSION_TEXT': 31, 'DIALOG': 5},
   collections.Counter(u['kind'] for u in su))
ck('tutte PENDING',
   not [u['idx'] for u in su
        if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
by = {u['idx']: u for u in tu}
VAL = [u['idx'] for u in su if u['kind'] == 'VALUE']
ck('i 31 VALUE sono identici al sorgente (nomi di missione)',
   len(VAL) == 31 and all(by[i]['italian'] == by[i]['english'] for i in VAL),
   [i for i in VAL if by[i]['italian'] != by[i]['english']])
ck('tutte le unita non-VALUE sono tradotte',
   not [u['idx'] for u in tu if u['kind'] != 'VALUE' and u['italian'].strip() == u['english'].strip()])
ck('i 5 DIALOG sono tradotti',
   not [u['idx'] for u in tu if u['kind'] == 'DIALOG' and u['italian'] == u['english']])
# --- contesti e ripetizioni ----------------------------------------------------------------
seen = collections.Counter(u['context'] for u in su)
ck('31 contesti distinti, tutti mission:', len(seen) == 31 and all(c.startswith('mission:') for c in seen),
   len(seen))
ck('distribuzione 26 con tre unita, 5 con quattro',
   collections.Counter(seen.values()) == {3: 26, 4: 5}, collections.Counter(seen.values()))
grp = collections.Counter(u['english'] for u in su)
ck('26 testi inglesi distinti per 98 unita', len(grp) == 26, len(grp))
ck('nessun gruppo con due rese diverse',
   not [k for k in grp if len({by[u['idx']]['italian'] for u in su if u['english'] == k}) > 1])
it_grp = {}
for u in tu:
    it_grp.setdefault(u['italian'], []).append(u)
ck('nessun duplicato italiano non spiegato dal sorgente',
   not [g for g in it_grp.values() if len(g) > 1 and len({v['english'] for v in g}) > 1])
# --- forma --------------------------------------------------------------------------------
ck('nessun tab (sorgente e traduzione)',
   not [u['idx'] for u in su if '\t' in u['english']] and not [u['idx'] for u in tu if '\t' in u['italian']])
a = sum(u['english'].count('"') for u in su)
b = sum(u['italian'].count('"') for u in tu)
ck('virgolette: %d = %d (2, unita 81)' % (a, b), a == b == 2 and by[81]['italian'].count('"') == 2, (a, b))
TOK = {'<payment>': 36, '<planet>': 31, '<cargo>': 31, '<destination>': 31, '<passengers>': 4, '<bunks>': 3}
ck('108 token nelle sei famiglie attese',
   collections.Counter(t for u in su for t in TAGS.findall(u['english'])) == TOK
   == collections.Counter(t for u in tu for t in TAGS.findall(u['italian'])),
   collections.Counter(t for u in tu for t in TAGS.findall(u['italian'])))
ck('token per unita: stessi simboli e stesso ordine',
   not [u['idx'] for u in tu if TAGS.findall(u['italian']) != TAGS.findall(u['english'])])
ck('ZERO quadre (asserito vuoto)', not [u['idx'] for u in tu if '[' in u['italian'] or ']' in u['italian']])
ck('nessun backtick', not [u for u in tu if '`' in u['italian']])
ck('nessuna traduzione vuota', all(u['italian'].strip() for u in tu))
NONLAT = re.compile(r'[^\x00-\x7F\u00C0-\u024F]')
ck('nessun carattere non latino', not [u for u in tu if NONLAT.search(u['italian'])])
ck('nessun trattino lungo o virgoletta curva',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB')])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate', 0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
print('rapporto IT/EN: min %.2f max %.2f · media %.2f' % (min(rs), max(rs), sum(rs) / len(rs)))
ck('registro approvato: nessun «voi»',
   not [u['idx'] for u in tu if re.search(r'\b(avete|potete|potrete|siete|vostro|vostra|vostri|vostre)\b',
                                          u['italian'])])
LOW = ' '.join(u['italian'] for u in tu).lower()
for t in ('contrabbando', 'carico', 'compenso', 'multa', 'criminale', 'ricercato', 'passeggero',
          'spazioporto'):
    ck('termine chiave presente: %s' % t, t in LOW)
merged = {}
for f in sorted(glob.glob(os.path.join(HERE, 'parts', 'part*.json'))):
    for kk, v in json.load(open(f, encoding='utf-8')).items():
        merged[int(kk)] = v
ck('le tre parti ricostruiscono translation.json (1..98)',
   sorted(merged) == list(range(1, 99))
   and {i: v for i, v in merged.items()} == {u['idx']: u['italian'] for u in tu})
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('copertura file: 98/279 (35.1%)')
print('parole EN %d -> IT %d · sha256[:16] %s' % (sum(len(u['english'].split()) for u in tu),
      sum(len(u['italian'].split()) for u in tu), h[:16]))
print()
print('FAIL:', len(fail), '·', 'verify L117 superato' if not fail else 'verify L117 fallito')
raise SystemExit(0 if not fail else 1)
