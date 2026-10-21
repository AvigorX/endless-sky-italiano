r"""verify.py — L317 (`data/coalition/coalition ships.txt`, righe 1141-2195). **LOTTO TERMINALE**.

Verifica da sola e verifica il **FILE INTERO** (che questo lotto chiude): **27 unita'**, **prima riga 59**, **ultima 2195**, **zero
unita' dopo**, **somma dei lotti 10 + 17 = 27**, **righe distinte**. Poi il lotto: riga grezza, campi del DB, la **nota del
hyperdrive** ripetuta **identica in tre unita'** e **diversa** dalla quarta, le **quattro tab**, i **nomi invariati**, le **asserzioni
vuote**, l'**unico apice inglese**.

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
PATH = 'data/coalition/coalition ships.txt'
NOTE = (1505, 1564, 1621)
TAB_RIGHE = [1504, 1505, 1564, 1621]
NAVI = ['Neutralizer', 'Punisher', 'Pursuer', 'Rover', 'Stalker', 'Briar', 'Spire', 'Thistle', 'Thorn',
        'Runabout', 'Sojourner', 'Traveler', 'Visitor', 'Skylance']
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


ck('riga grezza identica al sorgente (17/17)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = [u['idx'] for u in su
       if db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
       != (u['english'], u['kind'], u['path'], u['context'])]
ck('english/kind/path/context identici al DB', not bad, bad)
ck('17 unita, tutte DESCRIPTION, 13 contesti',
   len(tu) == 17 and collections.Counter(u['kind'] for u in tu) == {'DESCRIPTION': 17}
   and len({u['context'] for u in tu}) == 13)
ck("ZERO unita' dopo la 2195: il lotto chiude il file",
   db.execute('select count(*) from units where path=? and line>2195', (PATH,)).fetchone()[0] == 0)
ck("10 unita' prima della 1141 (L316)",
   db.execute('select count(*) from units where path=? and line<1141', (PATH,)).fetchone()[0] == 10)
righe = set()
somma = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    us = [u for u in json.load(open(f, encoding='utf-8'))['units'] if u['path'] == PATH]
    if us:
        somma.append(len(us))
        righe |= {u['line'] for u in us}
ck('FILE: somma dei lotti 10 + 17 = 27', somma == [10, 17] and sum(somma) == 27, somma)
ck('FILE: 27 unita, 27 righe distinte, prima 59, ultima 2195',
   len(righe) == 27 and min(righe) == 59 and max(righe) == 2195
   and db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (27, 59, 2195))
ck('FILE: copertura 27/27 (100%)',
   len(righe) == db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0], '%d/27' % len(righe))
ck('la nota del hyperdrive e identica nelle tre unita (1505, 1564, 1621)',
   by[5]['italian'] == by[7]['italian'] == by[9]['italian']
   and by[5]['english'] == by[7]['english'] == by[9]['english'])
ck('la 1504 e una nota DIVERSA (progetto Kimek, piu veloce)',
   by[4]['italian'] != by[5]['italian'] and 'Kimek' in by[4]['italian']
   and 'seminare' in by[4]['italian'])
ck('la nota usa «baia di caccia» e «motore iperspaziale», e la seconda persona sta SOLO li',
   'baia di caccia' in by[5]['italian'] and 'motore iperspaziale' in by[5]['italian']
   and [u['line'] for u in tu if re.search(r'\b(puoi|tuo|tua|ti)\b', u['italian'])] == list(NOTE))
ck('quattro tab alle righe attese',
   [u['line'] for u in tu if u['italian'].startswith(TAB)] == TAB_RIGHE)
ck('nomi delle navi invariati dove compaiono (incluse le Skylance rubate ai Quarg)',
   all(n in u['italian'] for u in tu for n in NAVI if n in u['english']))
ck('`Coalition` -> «Coalizione»',
   'Coalition' not in ''.join(u['italian'] for u in tu)
   and 'Coalizione' in by[11]['italian'])
ck('lo Spire: cabine per un Kimek, soffitti bassi per un Saryd, letti piccoli per un Arach',
   all(k in by[11]['italian'] for k in ('cabine a cuccette', 'soffitti', 'letti')))
ck('il Visitor: versatili, un lavoro diverso ogni settimana',
   'versatili' in by[17]['italian'] and 'ogni settimana' in by[17]['italian'])
ck('il Traveler: navi scientifiche e radici su un pianeta',
   'navi scientifiche' in by[16]['italian'] and 'radici' in by[16]['italian'])
ck('VIRGOLETTE: zero · SEGNAPOSTO: nessuno · ALTERNATIVE: nessuna (asserzioni vuote)',
   sum(u['italian'].count(QUOTE) for u in tu) == 0
   and not TAG.findall(''.join(u['italian'] for u in tu))
   and sum(len(ALT.findall(u['italian'])) for u in tu) == 0)
ck('apici: 1 in inglese (1753), 7 in italiano',
   [u['line'] for u in tu if u['english'].count(APOS)] == [1753]
   and sum(u['italian'].count(APOS) for u in tu) == 7)
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in tu for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessun doppio spazio (la tab iniziale non conta)',
   not [u['idx'] for u in tu if '  ' in u['italian'].lstrip(TAB)])
ck('rapporto nel gate 0,55-1,90',
   all(0.55 < u['ratio'] < 1.90 for u in tu),
   [(u['idx'], u['ratio']) for u in tu if not 0.55 < u['ratio'] < 1.90])
ck('tutte e 17 le unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in tu))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('FILE: 27/27 (100%) · prima riga 59 · ultima 2195 · zero dopo · somma lotti 10+17')
print('parole EN %d -> IT %d · ratio %.2f - %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(u['ratio'] for u in tu), max(u['ratio'] for u in tu)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L317 superato' if not fail else 'verify L317 fallito')
raise SystemExit(0 if not fail else 1)
