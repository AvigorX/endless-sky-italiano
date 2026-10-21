r"""verify.py — L321 (`data/wanderer/wanderer outfits.txt`, righe 463-659). **LOTTO TERMINALE**.

Verifica da sola e verifica il **FILE INTERO** (che questo lotto chiude): **31 unita'**, **prima riga 40**, **ultima 659**, **zero
unita' dopo**, **somma dei lotti 18 + 13 = 31**, **righe distinte**.

Poi il lotto: riga grezza, campi del DB, le **due scale `Type 1..4`**, le **tre licenze come oggetti** con tre diritti **diversi**, la
**seconda persona elencata** (solo nelle schede dei motori), gli **apici per unita'**, le **asserzioni vuote** (0 tab, 0 virgolette,
0 segnaposto, 0 alternative).

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
PATH = 'data/wanderer/wanderer outfits.txt'
NOMI = ['Ramscoop', 'Heat Sink', 'Type 1 Radiant', 'Type 2 Radiant', 'Type 3 Radiant', 'Type 4 Radiant',
        'Sentinel Skirtgrass', 'Noble Watchwood', 'Wanderer']
SECONDA = [498, 558, 598, 618]
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


ck('riga grezza identica al sorgente (13/13)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = [u['idx'] for u in su
       if db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
       != (u['english'], u['kind'], u['path'], u['context'])]
ck('english/kind/path/context identici al DB', not bad, bad)
ck('13 unita, tutte DESCRIPTION, 13 contesti distinti',
   len(tu) == 13 and collections.Counter(u['kind'] for u in tu) == {'DESCRIPTION': 13}
   and len({u['context'] for u in tu}) == 13)
ck("ZERO unita' dopo la 659: il lotto chiude il file",
   db.execute('select count(*) from units where path=? and line>659', (PATH,)).fetchone()[0] == 0)
ck("18 unita' prima della 463 (L320)",
   db.execute('select count(*) from units where path=? and line<463', (PATH,)).fetchone()[0] == 18)
righe = set()
somma = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    us = [u for u in json.load(open(f, encoding='utf-8'))['units'] if u['path'] == PATH]
    if us:
        somma.append(len(us))
        righe |= {u['line'] for u in us}
ck('FILE: somma dei lotti 18 + 13 = 31', somma == [18, 13] and sum(somma) == 31, somma)
ck('FILE: 31 unita, 31 righe distinte, prima 40, ultima 659',
   len(righe) == 31 and min(righe) == 40 and max(righe) == 659)
ck('FILE: copertura 31/31 (100%)',
   len(righe) == db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0], '%d/31' % len(righe))
ck('le due scale conservano i NUMERI: quattro Thruster e quattro Steering, Type 1..4',
   sorted(u['context'] for u in tu if 'Thruster' in u['context'])
   == ['outfit:Type %d Radiant Thruster' % i for i in (1, 2, 3, 4)]
   and sorted(u['context'] for u in tu if 'Steering' in u['context'])
   == ['outfit:Type %d Radiant Steering' % i for i in (1, 2, 3, 4)])
ck('la scala cresce dal Type 1 al Type 4',
   'più piccolo' in at[498]['italian'] and 'più grande' in at[558]['italian']
   and 'più grande' in at[638]['italian'])
ck('le tre licenze sono oggetti fisici con tre diritti diversi',
   'piatto' in at[645]['italian'] and 'ambra' in at[652]['italian'] and 'bronzo' in at[659]['italian']
   and 'equipaggiamenti Wanderer' in at[645]['italian']
   and 'non militari' in at[652]['italian'] and 'navi da guerra' in at[659]['italian'])
ck('la seconda persona compare SOLO nelle quattro schede dei motori',
   [u['line'] for u in tu if 'tua nave' in u['italian']] == SECONDA,
   [u['line'] for u in tu if 'tua nave' in u['italian']])
ck('nomi invariati dove compaiono',
   all(n in u['italian'] for u in tu for n in NOMI if n in u['english']))
ck('ASSERZIONI VUOTE: 0 tab, 0 virgolette, 0 segnaposto, 0 alternative',
   sum(u['italian'].count(TAB) for u in tu) == 0
   and sum(u['italian'].count(QUOTE) for u in tu) == 0
   and not TAG.findall(''.join(u['italian'] for u in tu))
   and sum(len(ALT.findall(u['italian'])) for u in tu) == 0)
ck('apici inglesi: 3 su due unita (645 x1, 652 x2)',
   [(u['line'], u['english'].count(APOS)) for u in tu if u['english'].count(APOS)]
   == [(645, 1), (652, 2)])
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in tu for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessun doppio spazio', not [u['idx'] for u in tu if '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90',
   all(0.55 < u['ratio'] < 1.90 for u in tu),
   [(u['idx'], u['ratio']) for u in tu if not 0.55 < u['ratio'] < 1.90])
ck('tutte e 13 le unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in tu))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('FILE: 31/31 (100%) · prima riga 40 · ultima 659 · zero dopo · somma lotti 18+13')
print('parole EN %d -> IT %d · ratio %.2f - %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(u['ratio'] for u in tu), max(u['ratio'] for u in tu)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L321 superato' if not fail else 'verify L321 fallito')
raise SystemExit(0 if not fail else 1)
