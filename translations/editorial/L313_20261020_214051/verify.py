r"""verify.py — L313 (`data/bunrodea/bunrodea outfits.txt`, righe 250-402). **LOTTO TERMINALE**.

Verifica da sola e verifica il **FILE INTERO** (che questo lotto chiude): **33 unita'**, **prima riga 25**, **ultima 402**, **zero
unita' dopo**, **somma dei lotti 12 + 12 + 9 = 33**, **righe distinte**. Poi il lotto: riga grezza, campi del DB, la **scala dei
nomi giapponesi**, le **asserzioni vuote** (0 tab, 0 virgolette, 0 segnaposto, 0 alternative), i **due apici inglesi**.

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
PATH = 'data/bunrodea/bunrodea outfits.txt'
PREFISSI = ['Chiisana', 'Nami', 'Ookii', 'Subarashii']
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


ck('riga grezza identica al sorgente (9/9)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = [u['idx'] for u in su
       if db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
       != (u['english'], u['kind'], u['path'], u['context'])]
ck('english/kind/path/context identici al DB', not bad, bad)
ck('9 unita, tutte DESCRIPTION, 9 contesti distinti',
   len(tu) == 9 and collections.Counter(u['kind'] for u in tu) == {'DESCRIPTION': 9}
   and len({u['context'] for u in tu}) == 9)
ck("ZERO unita' dopo la 402: il lotto chiude il file",
   db.execute('select count(*) from units where path=? and line>402', (PATH,)).fetchone()[0] == 0)
ck("24 unita' prima della 250 (L311 + L312)",
   db.execute('select count(*) from units where path=? and line<250', (PATH,)).fetchone()[0] == 24)
righe = set()
somma = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    us = [u for u in json.load(open(f, encoding='utf-8'))['units'] if u['path'] == PATH]
    if us:
        somma.append(len(us))
        righe |= {u['line'] for u in us}
ck('FILE: somma dei lotti 12 + 12 + 9 = 33', somma == [12, 12, 9] and sum(somma) == 33, somma)
ck('FILE: 33 unita, 33 righe distinte, prima 25, ultima 402',
   len(righe) == 33 and min(righe) == 25 and max(righe) == 402
   and db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (33, 25, 402))
ck('FILE: copertura 33/33 (100%)',
   len(righe) == db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0], '%d/33' % len(righe))
ck('nomi giapponesi invariati: quattro prefissi x due (propulsori + timoni)',
   collections.Counter(p for u in tu for p in PREFISSI if p in u['context'])
   == {'Chiisana': 2, 'Nami': 2, 'Ookii': 2, 'Subarashii': 2})
ck('`rift` resta `rift` (nessuna «frattura» inventata)',
   'rift' in ''.join(u['italian'] for u in tu)
   and all('frattura' not in u['italian'] for u in tu))
ck('ASSERZIONI VUOTE: 0 tab, 0 virgolette, 0 segnaposto, 0 alternative',
   sum(u['italian'].count(TAB) for u in tu) == 0
   and sum(u['italian'].count(QUOTE) for u in tu) == 0
   and not TAG.findall(''.join(u['italian'] for u in tu))
   and sum(len(ALT.findall(u['italian'])) for u in tu) == 0)
ck('apici: 2 in inglese (327, 402), 6 in italiano',
   sum(u['english'].count(APOS) for u in tu) == 2 and sum(u['italian'].count(APOS) for u in tu) == 6
   and [u['line'] for u in tu if u['english'].count(APOS)] == [327, 402],
   (sum(u['english'].count(APOS) for u in tu), sum(u['italian'].count(APOS) for u in tu)))
ck('il confronto con i Korath regge il filo del lotto',
   sum(1 for u in tu if 'Korath' in u['italian']) >= 4)
ck('la pistola: abbordaggi dei predoni e armi leggere',
   all(k in by[1]['italian'] for k in ('abbordate', 'predoni', 'armi leggere')))
ck('la scala: potenza bruta dei Korath contro efficienza Bunrodea',
   'potenza bruta' in by[2]['italian'] and 'fabbisogno' in by[3]['italian'])
ck('la riserva antica: cometa e inseguimento',
   'riserva antica' in by[5]['italian'] and 'cometa' in by[5]['italian'])
ck('i timoni: virata invece di velocita, cannoni frontali',
   'velocità di virata' in by[6]['italian'] and 'cannoni frontali' in by[6]['italian'])
ck('il finale: le cannoniere puntano i cannoni sul bersaglio',
   'cannoniere' in by[9]['italian'] and 'bersaglio' in by[9]['italian'])
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in tu for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessun doppio spazio', not [u['idx'] for u in tu if '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90',
   all(0.55 < u['ratio'] < 1.90 for u in tu),
   [(u['idx'], u['ratio']) for u in tu if not 0.55 < u['ratio'] < 1.90])
ck('tutte e 9 le unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in tu))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('FILE: 33/33 (100%) · prima riga 25 · ultima 402 · zero dopo · somma lotti 12+12+9')
print('parole EN %d -> IT %d · ratio %.2f - %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(u['ratio'] for u in tu), max(u['ratio'] for u in tu)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L313 superato' if not fail else 'verify L313 fallito')
raise SystemExit(0 if not fail else 1)
