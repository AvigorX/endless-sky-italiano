r"""verify.py — L325 (`data/kahet/kahet outfits.txt`, righe 54-573). **LOTTO TERMINALE, FILE INTERO**.

Verifica da sola il **FILE INTERO**: **25 unita'**, **prima 54**, **ultima 573**, **zero prima e dopo**, **un solo lotto**,
**22 `DESCRIPTION` + 3 `VALUE`**.

Poi il lotto, con meccanismi **diversi** da `check.py`:
- i tre `VALUE` sono verificati **sulla forma della stringa** (contiene `Nacelles`, e' un nome, non una frase) **e** sull'identita';
- le **tab** sono confrontate con il **conteggio inglese** riga per riga (il sorgente decide, non il contratto);
- gli **apici** sono verificati **per riga** e in **totale**;
- la **nota dei rifornimenti** e' cercata **nel corpus intero**, non solo qui;
- la **seconda persona** e' confrontata con il **sorgente**: dove c'e' in inglese c'e' in italiano, e viceversa.

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
SECONDA = re.compile(r'\b(tua|tuo|tuoi|tue|tu|te)\b', re.I)
HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
ROOT = os.path.abspath(os.path.join(L10N, '..'))
PATH = 'data/kahet/kahet outfits.txt'
VALUE = {444: 'Maeri Engine Nacelles', 468: "Ka'het Sustainer Nacelles", 492: 'Telis Engine Nacelles'}
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


ck('riga grezza identica al sorgente (25/25)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = [u['idx'] for u in su
       if db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
       != (u['english'], u['kind'], u['path'], u['context'])]
ck('english/kind/path/context identici al DB', not bad, bad)
ck('25 unita, 22 DESCRIPTION + 3 VALUE, 20 contesti',
   len(tu) == 25 and collections.Counter(u['kind'] for u in tu) == {'DESCRIPTION': 22, 'VALUE': 3}
   and len({u['context'] for u in tu}) == 20)
ck("FILE: zero unita' prima della 54 e zero dopo la 573",
   db.execute('select count(*) from units where path=? and line<54', (PATH,)).fetchone()[0] == 0
   and db.execute('select count(*) from units where path=? and line>573', (PATH,)).fetchone()[0] == 0)
righe, lotti = set(), []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    us = [u for u in json.load(open(f, encoding='utf-8'))['units'] if u['path'] == PATH]
    if us:
        lotti.append((os.path.basename(os.path.dirname(f)), len(us)))
        righe |= {u['line'] for u in us}
ck('FILE: un solo lotto da 25 unita', [n for _, n in lotti] == [25], lotti)
ck('FILE: 25 unita, 25 righe distinte, prima 54, ultima 573',
   len(righe) == 25 and min(righe) == 54 and max(righe) == 573)
ck('FILE: copertura 25/25 (100%)',
   len(righe) == db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0], '%d/25' % len(righe))
ck('i tre VALUE hanno FORMA di nome copiato, non di frase tradotta',
   all(at[l]['italian'] == v and at[l]['italian'].endswith('Nacelles')
       and len(at[l]['italian'].split()) == len(v.split()) for l, v in VALUE.items())
   and all(at[l]['english'] == v for l, v in VALUE.items()))
ck('nessuna unita DESCRIPTION e identica al suo inglese (le copiate sono solo i VALUE)',
   not [u['line'] for u in tu if u['kind'] == 'DESCRIPTION' and u['italian'] == u['english']])
ck('le tab dell italiano seguono le tab dell inglese, riga per riga',
   all((len(u['italian']) - len(u['italian'].lstrip(TAB))) == (len(u['english']) - len(u['english'].lstrip(TAB)))
       for u in tu),
   [(u['line'], len(u['english']) - len(u['english'].lstrip(TAB)),
     len(u['italian']) - len(u['italian'].lstrip(TAB))) for u in tu
    if (len(u['italian']) - len(u['italian'].lstrip(TAB))) != (len(u['english']) - len(u['english'].lstrip(TAB)))])
ck('la nota dei rifornimenti (285) usa una resa GIA presente nel corpus (>=2 altri lotti)',
   at[285]['italian'].startswith(TAB) and sum(
       1 for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json')))
       if os.path.basename(os.path.dirname(f)) != os.path.basename(HERE)
       for u in json.load(open(f, encoding='utf-8'))['units'] if u['italian'] == at[285]['italian']) >= 2)
ck('la seconda persona compare in italiano dove l inglese dice `your`/`you` (unit 573)',
   {u['line'] for u in tu if SECONDA.search(u['italian'])}
   == {u['line'] for u in tu if re.search('your|you', u['english'], re.I)} == {573},
   ({u['line'] for u in tu if SECONDA.search(u['italian'])},
    {u['line'] for u in tu if re.search('your|you', u['english'], re.I)}))
ck('la genealogia nei tre punti chiave: Ka mar droni, Het navi, Ka het nate dopo',
   "droni Ka'mar" in at[561]['italian'] and "Ka'het" in at[561]['italian']
   and 'Het' in at[414]['italian'] and "Ka'mar" in at[414]['italian'])
ck('`Costruttori` sostituisce `Builders` in tutto il lotto',
   'Builders' not in ''.join(u['italian'] for u in tu)
   and sum(u['italian'].count('Costruttori') for u in tu) == 11)
ck('VIRGOLETTE: zero · SEGNAPOSTO: nessuno · ALTERNATIVE: nessuna (asserzioni vuote)',
   sum(u['italian'].count(QUOTE) for u in tu) == 0
   and not TAG.findall(''.join(u['italian'] for u in tu))
   and sum(len(ALT.findall(u['italian'])) for u in tu) == 0)
ck('17 apici inglesi in 15 unita, con 425 e 561 doppi',
   sum(u['english'].count(APOS) for u in tu) == 17
   and sum(1 for u in tu if u['english'].count(APOS)) == 15
   and at[425]['english'].count(APOS) == 2 and at[561]['english'].count(APOS) == 2)
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in tu for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessun doppio spazio (la tab iniziale non conta)',
   not [u['idx'] for u in tu if '  ' in u['italian'].lstrip(TAB)])
ck('rapporto nel gate 0,55-1,90',
   all(0.55 < u['ratio'] < 1.90 for u in tu),
   [(u['idx'], u['ratio']) for u in tu if not 0.55 < u['ratio'] < 1.90])
ck('tutte le 25 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in tu))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('FILE: 25/25 (100%) · prima riga 54 · ultima 573 · zero prima e dopo · 22 DESCRIPTION + 3 VALUE')
print('parole EN %d -> IT %d · ratio %.2f - %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(u['ratio'] for u in tu), max(u['ratio'] for u in tu)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L325 superato' if not fail else 'verify L325 fallito')
raise SystemExit(0 if not fail else 1)
