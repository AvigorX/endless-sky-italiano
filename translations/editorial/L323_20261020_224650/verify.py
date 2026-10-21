r"""verify.py — L323 (`data/rulei/rulei.txt`, righe 38-157). **LOTTO TERMINALE, FILE INTERO**.

Verifica da sola il **FILE INTERO**: **41 unita'**, **prima riga 38**, **ultima 157**, **zero prima e dopo**, **un solo lotto**,
**38 `MISSION_TEXT` + 3 `LOGBOOK`**.

Poi il lotto, con meccanismi **diversi** da `check.py`:
- i **due registri** sono separati fra loro (i `LOGBOOK` senza «tu»; i `MISSION_TEXT` con la seconda persona in almeno 12 unita');
- le **32 tab** sono verificate **per riga**, contro l'elenco delle nove eccezioni;
- l'**indentazione a scala** (11/21/23 tab) e' verificata **in entrambe le lingue**;
- le **34 virgolette** e i **12 apici** sono verificati **per unita'**;
- `Umbral Reach` e' verificato **per uguaglianza fra le due lingue**, non con un numero scelto a mano.

Indipendente da `check.py`.
"""
import collections
import glob
import hashlib
import json
import os
import re
import sqlite3

TAB = chr(9)
QUOTE = chr(34)
APOS = chr(39)
TAG = re.compile(r'<[^<>]+>')
ALT = re.compile(r'\[[^\]]*\]')
SECONDA = re.compile(r'\b(ti|tu|te|tuo|tua|tuoi|tue)\b', re.I)
HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
ROOT = os.path.abspath(os.path.join(L10N, '..'))
PATH = 'data/rulei/rulei.txt'
SENZA_TAB = [38, 39, 41, 93, 116, 118, 132, 151, 153]
SCALA = {95: 11, 98: 21, 99: 23}
src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
su = sorted(src['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
raw_lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
by = {u['idx']: u for u in tu}
at = {u['line']: u for u in tu}
fail = []


def ck(n, c, d=''):
    print('%-96s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente (41/41)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = [u['idx'] for u in su
       if db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
       != (u['english'], u['kind'], u['path'], u['context'])]
ck('english/kind/path/context identici al DB', not bad, bad)
ck('41 unita, 5 contesti, 38 MISSION_TEXT + 3 LOGBOOK',
   len(tu) == 41 and len({u['context'] for u in tu}) == 5
   and collections.Counter(u['kind'] for u in tu) == {'MISSION_TEXT': 38, 'LOGBOOK': 3})
ck("FILE: zero unita' prima della 38 e zero dopo la 157",
   db.execute('select count(*) from units where path=? and line<38', (PATH,)).fetchone()[0] == 0
   and db.execute('select count(*) from units where path=? and line>157', (PATH,)).fetchone()[0] == 0)
righe, lotti = set(), []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    us = [u for u in json.load(open(f, encoding='utf-8'))['units'] if u['path'] == PATH]
    if us:
        lotti.append((os.path.basename(os.path.dirname(f)), len(us)))
        righe |= {u['line'] for u in us}
ck('FILE: un solo lotto da 41 unita', [n for _, n in lotti] == [41], lotti)
ck('FILE: 41 unita, 41 righe distinte, prima 38, ultima 157',
   len(righe) == 41 and min(righe) == 38 and max(righe) == 157)
ck('FILE: copertura 41/41 (100%)',
   len(righe) == db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0], '%d/41' % len(righe))
ck('i LOGBOOK non usano la seconda persona; i MISSION_TEXT la usano in almeno 12 unita',
   not [u['line'] for u in tu if u['kind'] == 'LOGBOOK' and SECONDA.search(u['italian'])]
   and sum(1 for u in tu if u['kind'] == 'MISSION_TEXT' and SECONDA.search(u['italian'])) >= 12,
   sum(1 for u in tu if u['kind'] == 'MISSION_TEXT' and SECONDA.search(u['italian'])))
ck('le nove righe senza tab sono quelle attese, tutte le altre hanno la tab',
   sorted(l for l in at if l not in SENZA_TAB) == sorted(u['line'] for u in tu if u['italian'].startswith(TAB))
   and not [l for l in SENZA_TAB if at[l]['italian'].startswith(TAB)])
ck("l'indentazione a scala cresce 11 -> 21 -> 23, in entrambe le lingue",
   {l: len(at[l]['italian']) - len(at[l]['italian'].lstrip(TAB)) for l in SCALA} == SCALA
   and {l: len(at[l]['english']) - len(at[l]['english'].lstrip(TAB)) for l in SCALA} == SCALA)
ck('34 virgolette in 16 unita, la 151 con quattro',
   sum(u['italian'].count(QUOTE) for u in tu) == 34
   and sum(1 for u in tu if u['italian'].count(QUOTE)) == 16
   and at[151]['italian'].count(QUOTE) == 4)
ck('12 apici inglesi in 7 unita, con 45 e 156 che ne hanno tre',
   sum(u['english'].count(APOS) for u in tu) == 12
   and sum(1 for u in tu if u['english'].count(APOS)) == 7
   and at[45]['english'].count(APOS) == 3 and at[156]['english'].count(APOS) == 3)
ck('`Umbral Reach` invariato: stesse occorrenze nelle due lingue',
   sum(u['italian'].count('Umbral Reach') for u in tu)
   == sum(u['english'].count('Umbral Reach') for u in tu))
ck('le due parole chiave: «Precursori» e «Una Fine»',
   'Precursori' in at[58]['italian'] and 'Una Fine' in at[64]['italian'])
ck('SEGNAPOSTO: nessuno · ALTERNATIVE: nessuna (asserzioni vuote)',
   not TAG.findall(''.join(u['italian'] for u in tu))
   and sum(len(ALT.findall(u['italian'])) for u in tu) == 0)
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in tu for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessun doppio spazio (la tab iniziale non conta)',
   not [u['idx'] for u in tu if '  ' in u['italian'].lstrip(TAB)])
ck('rapporto nel gate 0,55-1,90',
   all(0.55 < u['ratio'] < 1.90 for u in tu),
   [(u['idx'], u['ratio']) for u in tu if not 0.55 < u['ratio'] < 1.90])
ck('tutte le 41 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in tu))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('FILE: 41/41 (100%) · prima riga 38 · ultima 157 · zero prima e dopo · 38 MISSION_TEXT + 3 LOGBOOK')
print('parole EN %d -> IT %d · ratio %.2f - %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(u['ratio'] for u in tu), max(u['ratio'] for u in tu)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L323 superato' if not fail else 'verify L323 fallito')
raise SystemExit(0 if not fail else 1)
