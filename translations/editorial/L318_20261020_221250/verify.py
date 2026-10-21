r"""verify.py — L318 (`data/korath/korath weapons.txt`, righe 53-603). **Primo lotto** del file.

Verifica da sola e **solo fatti locali al segmento**, piu' un **limite monotono** (dopo la 603 restano 22 unita'): il file **non e'
finito**, quindi la copertura **si stampa** e non si asserisce.

La nota dei rifornimenti (473) qui e' verificata con un meccanismo **diverso** da `check.py`: non si confronta con **una** unita'
scelta per testo inglese, si **cerca la stringa italiana** in tutti gli altri lotti e si pretende che compaia **almeno due volte**.
Se la resa fosse nuova, il conteggio sarebbe zero e il test lo direbbe.

Poi: la **154** e' un'ellissi (tre punti, nessun «..»), la **603** nomina il **suo** contenitore, le **due tab**, gli **apici per
unita'**, i **nomi invariati**.

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
PATH = 'data/korath/korath weapons.txt'
ARMI = ['Grab-Strike', 'Shunt-Strike', 'Banisher', 'Expeller', 'Warder', 'Fire-Lance', 'Blaze-Pike',
        'Inferno', 'Thermal Repeater', 'Piercer', 'Detainer', 'Cluster Mine']
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
ck('17 unita, tutte DESCRIPTION, 15 contesti',
   len(tu) == 17 and collections.Counter(u['kind'] for u in tu) == {'DESCRIPTION': 17}
   and len({u['context'] for u in tu}) == 15)
ck("SEGMENTO: zero unita' prima della 53 (il lotto apre il file)",
   db.execute('select count(*) from units where path=? and line<53', (PATH,)).fetchone()[0] == 0)
ck("SEGMENTO: 22 unita' dopo la 603, la prossima alla 615",
   db.execute('select count(*) from units where path=? and line>603', (PATH,)).fetchone()[0] == 22
   and db.execute('select min(line) from units where path=? and line>603', (PATH,)).fetchone()[0] == 615)
righe = {u['line'] for u in tu}
altrui = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    if os.path.basename(os.path.dirname(f)) == os.path.basename(HERE):
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH and 53 <= u['line'] <= 603:
            altrui.append((os.path.basename(os.path.dirname(f)), u['line']))
ck('SEGMENTO: 17 righe distinte 53-603, nessun ALTRO lotto sulle stesse righe',
   len(righe) == 17 and min(righe) == 53 and max(righe) == 603 and not altrui, (len(righe), altrui))
# nota dei rifornimenti: si cerca la STRINGA ITALIANA nel resto del corpus
nota = at[473]['italian']
occorrenze = 0
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    if os.path.basename(os.path.dirname(f)) == os.path.basename(HERE):
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['italian'] == nota:
            occorrenze += 1
ck('la nota dei rifornimenti usa la resa GIA ESISTENTE (compare in almeno due altri lotti)',
   occorrenze >= 2 and nota.startswith(TAB) and 'emporio' in nota, occorrenze)
ck('la 154 e un ellissi: tre punti, nessun «..», nessun carattere tipografico',
   '...' in at[154]['italian']
   and '..' not in at[154]['italian'].replace('...', '')
   and '\u2026' not in at[154]['italian'])
ck('la 603 e munizione per il Cluster Mine Layer, con undici submunizioni',
   'Cluster Mine Layer' in at[603]['italian'] and 'undici' in at[603]['italian'])
ck('due tab: 109 e 473, in prima posizione',
   [u['line'] for u in tu if u['italian'].startswith(TAB)] == [109, 473])
ck('nomi delle armi invariati dove compaiono',
   all(n in u['italian'] for u in tu for n in ARMI if n in u['english']))
ck('`Systems Core` invariato, `Exile` -> «Esilio»',
   'Systems Core' in at[108]['italian'] and "dell'Esilio" in at[108]['italian']
   and 'Exile' not in at[108]['italian'])
ck('gestalt (287) e sinergia (327)',
   'gestalt' in at[287]['italian'] and 'sinergia' in at[327]['italian'])
ck('il Detainer: portata, propulsione, nome dei Korath',
   all(k in at[563]['italian'] for k in ('portata', 'propulsione', 'nome dei Korath')))
ck('VIRGOLETTE: zero · SEGNAPOSTO: nessuno · ALTERNATIVE: nessuna (asserzioni vuote)',
   sum(u['italian'].count(QUOTE) for u in tu) == 0
   and not TAG.findall(''.join(u['italian'] for u in tu))
   and sum(len(ALT.findall(u['italian'])) for u in tu) == 0)
ck('apici inglesi: 3, uno per unita nelle righe 108, 109, 472',
   [u['line'] for u in tu if u['english'].count(APOS)] == [108, 109, 472])
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
tot = db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0]
print('copertura del file: %d/%d (%.1f%%) — stampata, NON asserita: il file non e\' finito' % (
    len(righe), tot, 100.0 * len(righe) / tot))
print('parole EN %d -> IT %d · ratio %.2f - %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(u['ratio'] for u in tu), max(u['ratio'] for u in tu)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L318 superato' if not fail else 'verify L318 fallito')
raise SystemExit(0 if not fail else 1)
