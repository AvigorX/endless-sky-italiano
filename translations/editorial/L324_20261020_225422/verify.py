r"""verify.py — L324 (`data/incipias/incipias outfits.txt`, righe 40-388). **LOTTO TERMINALE, FILE INTERO**.

Verifica da sola il **FILE INTERO**: **23 unita'**, **prima 40**, **ultima 388**, **zero prima e dopo**, **un solo lotto**, tutte
`DESCRIPTION`.

Poi il lotto, con meccanismi **diversi** da `check.py`:
- la nota dei rifornimenti e' verificata cercando la **stringa italiana** nel resto del corpus (>= 2 altri lotti);
- la **scala dei colori** e' verificata sui **tre aggettivi del sorgente** (`weakest`, `balance`, `potent`) e sulle tre classi;
- la **distribuzione dei contesti** e' confrontata con il conteggio reale;
- gli **apici** e le **tab** sono verificati **per riga**.

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
PATH = 'data/incipias/incipias outfits.txt'
TAB_RIGHE = [41, 86, 87, 134, 135, 190]
NOMI = ['Plasma Discharger', 'Stagnation Beam', 'Star Tail', 'Horizon Grappler', 'Gas-Class Shield',
        'Liquid-Class Shield', 'Metallic Hydrogen Cell', 'MH Blue-Class', 'MH Green-Class', 'MH Red-Class',
        'Cloud Piercer', 'Hicemus']
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


ck('riga grezza identica al sorgente (23/23)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = [u['idx'] for u in su
       if db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
       != (u['english'], u['kind'], u['path'], u['context'])]
ck('english/kind/path/context identici al DB', not bad, bad)
ck('23 unita, tutte DESCRIPTION, 17 contesti',
   len(tu) == 23 and collections.Counter(u['kind'] for u in tu) == {'DESCRIPTION': 23}
   and len({u['context'] for u in tu}) == 17)
ck("FILE: zero unita' prima della 40 e zero dopo la 388",
   db.execute('select count(*) from units where path=? and line<40', (PATH,)).fetchone()[0] == 0
   and db.execute('select count(*) from units where path=? and line>388', (PATH,)).fetchone()[0] == 0)
righe, lotti = set(), []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    us = [u for u in json.load(open(f, encoding='utf-8'))['units'] if u['path'] == PATH]
    if us:
        lotti.append((os.path.basename(os.path.dirname(f)), len(us)))
        righe |= {u['line'] for u in us}
ck('FILE: un solo lotto da 23 unita', [n for _, n in lotti] == [23], lotti)
ck('FILE: 23 unita, 23 righe distinte, prima 40, ultima 388',
   len(righe) == 23 and min(righe) == 40 and max(righe) == 388)
ck('FILE: copertura 23/23 (100%)',
   len(righe) == db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0], '%d/23' % len(righe))
ck('la distribuzione dei contesti e 3, 3, 2, 2 e tredici singoli',
   sorted(collections.Counter(u['context'] for u in tu).values(), reverse=True) == [3, 3, 2, 2] + [1] * 13,
   sorted(collections.Counter(u['context'] for u in tu).values(), reverse=True))
ck('la nota dei rifornimenti usa una resa GIA presente nel corpus (>=2 altri lotti)',
   at[135]['italian'].startswith(TAB) and 'emporio' in at[135]['italian']
   and sum(1 for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json')))
           if os.path.basename(os.path.dirname(f)) != os.path.basename(HERE)
           for u in json.load(open(f, encoding='utf-8'))['units'] if u['italian'] == at[135]['italian']) >= 2)
ck('sei tab, due per Stagnation Beam e due per Star Tail',
   [u['line'] for u in tu if u['italian'].startswith(TAB)] == TAB_RIGHE
   and at[86]['context'] == at[87]['context'] and at[134]['context'] == at[135]['context'])
ck('la scala dei colori segue il testo: weakest / balance / potent',
   'weakest' in at[289]['english'] and 'debole' in at[289]['italian']
   and 'a color of balance' in at[320]['english'] and 'equilibrio' in at[320]['italian']
   and 'potent source of energy' in at[351]['english'] and 'fonte di energia potente' in at[351]['italian'])
ck('i nomi restano invariati, e `Blue-Class` compare dove compare nel sorgente',
   all(n in u['italian'] for u in tu for n in NOMI if n in u['english'])
   and [u['line'] for u in tu if 'Blue-Class' in u['english']] ==
       [u['line'] for u in tu if 'Blue-Class' in u['italian']]
   and sorted(u['context'] for u in tu if 'MH ' in u['context']) ==
       ['outfit:MH %s-Class %s' % (c, t) for c in ('Blue', 'Green', 'Red') for t in ('Steering', 'Thruster')])
ck('VIRGOLETTE: zero · SEGNAPOSTO: nessuno · ALTERNATIVE: nessuna (asserzioni vuote)',
   sum(u['italian'].count(QUOTE) for u in tu) == 0
   and not TAG.findall(''.join(u['italian'] for u in tu))
   and sum(len(ALT.findall(u['italian'])) for u in tu) == 0)
ck('9 apici inglesi su 5 unita: 40, 85 (2), 86 (3), 225 (2), 351',
   sum(u['english'].count(APOS) for u in tu) == 9
   and [u['line'] for u in tu if u['english'].count(APOS)] == [40, 85, 86, 225, 351]
   and at[86]['english'].count(APOS) == 3)
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in tu for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessun doppio spazio (la tab iniziale non conta)',
   not [u['idx'] for u in tu if '  ' in u['italian'].lstrip(TAB)])
ck('rapporto nel gate 0,55-1,90',
   all(0.55 < u['ratio'] < 1.90 for u in tu),
   [(u['idx'], u['ratio']) for u in tu if not 0.55 < u['ratio'] < 1.90])
ck('tutte le 23 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in tu))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('FILE: 23/23 (100%) · prima riga 40 · ultima 388 · zero prima e dopo · un solo lotto')
print('parole EN %d -> IT %d · ratio %.2f - %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(u['ratio'] for u in tu), max(u['ratio'] for u in tu)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L324 superato' if not fail else 'verify L324 fallito')
raise SystemExit(0 if not fail else 1)
