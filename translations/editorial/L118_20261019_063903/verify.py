r"""verify.py — L118 (data/human/pirate jobs.txt, 104 unita', righe 1627-2955)

Invariante di **segmento**, indipendente da `check.py`: rilegge il repository originale, `state.db`, i
`parts/`, `translation.json` e il `translation.json` di L117 (per i testi condivisi).

Misure attese: **98 unita' prima** della riga 1627 (L117), **77 dopo** la 2955, file di **279 unita'**,
`max(line) = 3706`, confine alla riga **2958** (`mission:Raid on Merchants (South)`). **104 unita'** con tipi
`{'DIALOG': 36, 'VALUE': 33, 'DESCRIPTION': 33, 'MISSION_TEXT': 2}`, **33 contesti** (19 con quattro unita', 14
con due), **39 testi distinti**, **192 token** in nove famiglie, **zero virgolette** (asserito). I **33 `VALUE`**
sono identici al sorgente (nomi di missione, decisione 259/L103).
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
ck('idx 1..104 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 105)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 104 righe 1627 - 2955', len(tu) == 104 and (first, last) == (1627, 2955), (len(tu), first, last))
tot = db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0]
before = db.execute('select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0]
after = db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0]
maxl = db.execute('select max(line) from units where path=?', (PATH,)).fetchone()[0]
ck('98 unita prima della riga 1627 (L117)', before == 98, before)
ck('77 unita dopo la riga 2955 (279 - 98 - 104)', after == 77, after)
ck('file: 279 unita, max(line) = 3706', tot == 279 and maxl == 3706, (tot, maxl))
ck('il confine: la riga 2958 apre mission:Raid on Merchants (South)',
   db.execute('select line,context from units where path=? and line>? order by line limit 1',
              (PATH, last)).fetchone() == (2958, 'mission:Raid on Merchants (South)'))
ck('tipi: 36 DIALOG · 33 VALUE · 33 DESCRIPTION · 2 MISSION_TEXT',
   collections.Counter(u['kind'] for u in su) == {'DIALOG': 36, 'VALUE': 33,
                                                 'DESCRIPTION': 33, 'MISSION_TEXT': 2},
   collections.Counter(u['kind'] for u in su))
ck('tutte PENDING',
   not [u['idx'] for u in su
        if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
by = {u['idx']: u for u in tu}
VAL = [u['idx'] for u in su if u['kind'] == 'VALUE']
ck('i 33 VALUE sono identici al sorgente (nomi di missione)',
   len(VAL) == 33 and all(by[i]['italian'] == by[i]['english'] for i in VAL),
   [i for i in VAL if by[i]['italian'] != by[i]['english']])
ck('tutte le unita non-VALUE sono tradotte',
   not [u['idx'] for u in tu if u['kind'] != 'VALUE' and u['italian'].strip() == u['english'].strip()])
# --- contesti e ripetizioni ----------------------------------------------------------------
seen = collections.Counter(u['context'] for u in su)
ck('33 contesti distinti, tutti mission:', len(seen) == 33 and all(c.startswith('mission:') for c in seen),
   len(seen))
ck('distribuzione 19 con quattro unita, 14 con due',
   collections.Counter(seen.values()) == {4: 19, 2: 14}, collections.Counter(seen.values()))
grp = collections.Counter(u['english'] for u in su)
ck('39 testi inglesi distinti per 104 unita', len(grp) == 39, len(grp))
ck('nessun gruppo con due rese diverse',
   not [k for k in grp if len({by[u['idx']]['italian'] for u in su if u['english'] == k}) > 1])
it_grp = {}
for u in tu:
    it_grp.setdefault(u['italian'], []).append(u)
ck('nessun duplicato italiano non spiegato dal sorgente',
   not [g for g in it_grp.values() if len(g) > 1 and len({v['english'] for v in g}) > 1])
prev = {}
for f in glob.glob(os.path.join(L10N, 'staging/editorial/L117_*', 'translation.json')):
    for u in json.load(open(f, encoding='utf-8'))['units']:
        prev[u['english']] = u['italian']
shared = [u for u in tu if u['english'] in prev]
ck('le 8 unita condivise con L117 hanno la stessa resa',
   len(shared) == 8 and all(u['italian'] == prev[u['english']] for u in shared),
   len(shared))
# --- forma --------------------------------------------------------------------------------
ck('nessun tab (sorgente e traduzione)',
   not [u['idx'] for u in su if '\t' in u['english']] and not [u['idx'] for u in tu if '\t' in u['italian']])
ck('ZERO virgolette (asserito 0 = 0)',
   sum(u['english'].count('"') for u in su) == 0 == sum(u['italian'].count('"') for u in tu))
TOK = {'<planet>': 53, '<payment>': 52, '<destination>': 33, '<system>': 33, '<day>': 17,
       '<npc>': 9, '<date>': 9, '<bunks>': 5, '<cargo>': 2}
ck('192 token nelle nove famiglie attese',
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
for t in ('forze dell\'ordine', 'flotta', 'compenso', 'schiavi', 'predoni', 'milizia', 'mercanti', 'bottino'):
    ck('termine chiave presente: %s' % t, t in LOW)
merged = {}
for f in sorted(glob.glob(os.path.join(HERE, 'parts', 'part*.json'))):
    for kk, v in json.load(open(f, encoding='utf-8')).items():
        merged[int(kk)] = v
ck('le quattro parti ricostruiscono translation.json (1..104)',
   sorted(merged) == list(range(1, 105))
   and {i: v for i, v in merged.items()} == {u['idx']: u['italian'] for u in tu})
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('copertura file: 202/279 (72.4%)')
print('parole EN %d -> IT %d · sha256[:16] %s' % (sum(len(u['english'].split()) for u in tu),
      sum(len(u['italian'].split()) for u in tu), h[:16]))
print()
print('FAIL:', len(fail), '·', 'verify L118 superato' if not fail else 'verify L118 fallito')
raise SystemExit(0 if not fail else 1)
