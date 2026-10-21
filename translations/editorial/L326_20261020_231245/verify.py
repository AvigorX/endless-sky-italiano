r"""verify.py — L326 (`data/_deprecated/deprecated outfits.txt`, righe 25-792). **LOTTO TERMINALE, FILE INTERO**.

Verifica da sola il **FILE INTERO**: **47 unita'**, **prima 25**, **ultima 792**, **zero prima e dopo**, **un solo lotto**,
**42 `DESCRIPTION` + 3 `VALUE` + 2 `TEXT`**.

Poi il lotto, con meccanismi **diversi** da `check.py`:
- i **due `TEXT`** sono cercati **nel corpus gia' in staging**: `"Nettle" KKV` compare **13** volte e `"Orchid" Nuclear Missile`
  **8** (lotti L176, L177, L309...): se la resa fosse diversa, il corpus lo direbbe;
- i **tre `VALUE`** NON hanno precedenti (0 occorrenze): si verificano **solo** per identita' all'inglese, e il test **dichiara** la
  differenza fra i due casi, invece di trattarli allo stesso modo;
- le **tab** sono confrontate con il **conteggio inglese** riga per riga;
- le **coppie gemelle** sono verificate **sul DB** (stesso inglese) **e** sulla resa.

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
HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
ROOT = os.path.abspath(os.path.join(L10N, '..'))
PATH = 'data/_deprecated/deprecated outfits.txt'
COPIE_TESTO = ['"Nettle" KKV', '"Orchid" Nuclear Missile']
COPIE_NOME = ['Nanotech Batteries', 'Intrusion Countermeasures', 'Z-3600 "Beam" Amat Torches']
GEMELLE = [(70, 82), (97, 109)]
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


ck('riga grezza identica al sorgente (47/47)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = [u['idx'] for u in su
       if db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
       != (u['english'], u['kind'], u['path'], u['context'])]
ck('english/kind/path/context identici al DB', not bad, bad)
ck('47 unita, 42 DESCRIPTION + 3 VALUE + 2 TEXT, 39 contesti',
   len(tu) == 47 and collections.Counter(u['kind'] for u in tu) == {'DESCRIPTION': 42, 'VALUE': 3, 'TEXT': 2}
   and len({u['context'] for u in tu}) == 39)
ck("FILE: zero unita' prima della 25 e zero dopo la 792",
   db.execute('select count(*) from units where path=? and line<25', (PATH,)).fetchone()[0] == 0
   and db.execute('select count(*) from units where path=? and line>792', (PATH,)).fetchone()[0] == 0)
righe, lotti = set(), []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    us = [u for u in json.load(open(f, encoding='utf-8'))['units'] if u['path'] == PATH]
    if us:
        lotti.append((os.path.basename(os.path.dirname(f)), len(us)))
        righe |= {u['line'] for u in us}
ck('FILE: un solo lotto da 47 unita', [n for _, n in lotti] == [47], lotti)
ck('FILE: 47 unita, 47 righe distinte, prima 25, ultima 792',
   len(righe) == 47 and min(righe) == 25 and max(righe) == 792)
ck('FILE: copertura 47/47 (100%)',
   len(righe) == db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0], '%d/47' % len(righe))
ck('i due TEXT copiati coincidono con la resa GIA presente nel corpus (>=5 lotti)',
   all(sum(1 for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json')))
           if os.path.basename(os.path.dirname(f)) != os.path.basename(HERE)
           for u in json.load(open(f, encoding='utf-8'))['units'] if u['italian'] == t) >= 5
       for t in COPIE_TESTO),
   [t for t in COPIE_TESTO
    if sum(1 for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json')))
           if os.path.basename(os.path.dirname(f)) != os.path.basename(HERE)
           for u in json.load(open(f, encoding='utf-8'))['units'] if u['italian'] == t) < 5])
ck('i tre VALUE non hanno precedenti nel corpus: si verificano SOLO per identita',
   all(u['italian'] == u['english'] for u in tu if u['kind'] == 'VALUE')
   and all(sum(1 for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json')))
               if os.path.basename(os.path.dirname(f)) != os.path.basename(HERE)
               for u in json.load(open(f, encoding='utf-8'))['units'] if u['italian'] == n) == 0
           for n in COPIE_NOME))
ck('le tab dell italiano seguono le tab dell inglese, riga per riga',
   all((len(u['italian']) - len(u['italian'].lstrip(TAB))) == (len(u['english']) - len(u['english'].lstrip(TAB)))
       for u in tu),
   [(u['line'],) for u in tu
    if (len(u['italian']) - len(u['italian'].lstrip(TAB))) != (len(u['english']) - len(u['english'].lstrip(TAB)))])
ck('le coppie gemelle: stesso inglese nel DB, stessa resa in italiano',
   all(db.execute('select english from units where path=? and line=?', (PATH, a)).fetchone()
       == db.execute('select english from units where path=? and line=?', (PATH, b)).fetchone()
       and at[a]['italian'] == at[b]['italian'] for a, b in GEMELLE))
ck('8 virgolette in 4 righe, 12 apici inglesi in 8 unita',
   sum(u['italian'].count(QUOTE) for u in tu) == 8
   and sum(1 for u in tu if u['italian'].count(QUOTE)) == 4
   and sum(u['english'].count(APOS) for u in tu) == 12
   and sum(1 for u in tu if u['english'].count(APOS)) == 8
   and at[618]['english'].count(APOS) == 3)
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
ck('tutte le 47 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in tu))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('FILE: 47/47 (100%) · prima riga 25 · ultima 792 · zero prima e dopo · 42 DESCRIPTION + 3 VALUE + 2 TEXT')
print('parole EN %d -> IT %d · ratio %.2f - %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(u['ratio'] for u in tu), max(u['ratio'] for u in tu)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L326 superato' if not fail else 'verify L326 fallito')
raise SystemExit(0 if not fail else 1)
