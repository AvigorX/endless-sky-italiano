r"""verify.py — L266 (`data/kahet/aberrant ships.txt`, righe 686-1007). **LOTTO TERMINALE**.

**Invariante di FILE**: dopo questo lotto `aberrant ships.txt` deve avere **65 unita' distinte su 65** (`43 + 22`), la riga
**1007** come ultima e **0** unita' dopo; le righe dei due lotti devono coincidere **esattamente** con quelle del database.

Verifica da sola: riga grezza, campi del DB, i cinque contesti in sequenza, le **18 virgolette**, i 13 `VALUE` copiati, la
scheda anomala di **Trip**, e che **nessun altro lotto** rivendichi queste righe.

Indipendente da `check.py`: rilegge `source.json`, il `translation.json`, il database, il file del gioco e **tutti** i
`translation.json` dello staging.
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
HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
ROOT = os.path.abspath(os.path.join(L10N, '..'))
PATH = 'data/kahet/aberrant ships.txt'
NAVI = ['Aberrant Pike', 'Aberrant Mole', 'Aberrant Whiskers', 'Aberrant Trip', 'Aberrant Triplet']
src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
su = sorted(src['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
raw_lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
fail = []


def ck(n, c, d=''):
    print('%-96s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente (22/22)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = [u['idx'] for u in su
       if db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
       != (u['english'], u['kind'], u['path'], u['context'])]
ck('english/kind/path/context identici al DB', not bad, bad)
ck('22 unita, righe 686-1007, tipi 13/9',
   len(tu) == 22 and [u['line'] for u in tu] == sorted({u['line'] for u in tu})
   and collections.Counter(u['kind'] for u in tu) == {'VALUE': 13, 'DESCRIPTION': 9},
   (len(tu), collections.Counter(u['kind'] for u in tu)))
ck('i cinque contesti compaiono nell ordine delle navi, senza altri',
   [c.replace('ship:', '') for c in dict.fromkeys(u['context'] for u in tu)] == NAVI,
   [c for c in dict.fromkeys(u['context'] for u in tu)])
ck("43 unita' prima, e la precedente e nella stessa nave (Pike)",
   db.execute('select count(*) from units where path=? and line<686', (PATH,)).fetchone()[0] == 43
   and db.execute('select context from units where path=? and line<686 order by line desc limit 1', (PATH,)).fetchone()
   == ('ship:Aberrant Pike',))
ck("ZERO unita' dopo la 1007: il lotto CHIUDE il file",
   db.execute('select count(*) from units where path=? and line>1007', (PATH,)).fetchone()[0] == 0)
ck("la 1007 e l'ultima riga del file (65 unita', righe 16 - 1007)",
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (65, 16, 1007))
lotti, righe = [], set()
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    us = [u for u in json.load(open(f, encoding='utf-8'))['units'] if u['path'] == PATH]
    if us:
        lotti.append((os.path.basename(os.path.dirname(f)), len(us)))
        righe |= {u['line'] for u in us}
ck('INVARIANTE DI FILE: 2 lotti (43 + 22) coprono 65 righe distinte su 65',
   [n for _, n in lotti] == [43, 22] and len(righe) == 65, (lotti, len(righe)))
ck('nessun buco: le 65 righe dei lotti sono esattamente quelle del database',
   righe == {l for l, in db.execute('select line from units where path=?', (PATH,))})
overlap = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    if os.path.basename(os.path.dirname(f)) == os.path.basename(HERE):
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH and 686 <= u['line'] <= 1007:
            overlap.append((os.path.basename(os.path.dirname(f)), u['line']))
ck('nessun altro lotto rivendica le righe 686-1007', not overlap, overlap)
ck('copertura: 65/65 (100%)', len(righe) == 65, '%d/65' % len(righe))
ck('i 13 VALUE sono copiati; le 9 DESCRIPTION sono tradotte',
   all(u['italian'] == u['english'] for u in tu if u['kind'] == 'VALUE')
   and all(u['italian'] != u['english'] for u in tu if u['kind'] == 'DESCRIPTION'))
ck('VIRGOLETTE: 18 in inglese e 18 in italiano, mappa per unita identica',
   sum(u['english'].count(QUOTE) for u in tu) == 18 == sum(u['italian'].count(QUOTE) for u in tu)
   and {u['idx']: u['english'].count(QUOTE) for u in tu if QUOTE in u['english']}
   == {u['idx']: u['italian'].count(QUOTE) for u in tu if QUOTE in u['italian']})
by = {u['idx']: u for u in tu}
ck('le 4 note organo-metalliche hanno una sola resa; le 5 frasi sulla variante sono distinte',
   len({by[i]['italian'] for i in (5, 10, 15, 20)}) == 1
   and len({by[i]['italian'] for i in (1, 6, 11, 16, 21)}) == 5)
ck('la scheda di Trip resta un DIFETTO di germinazione, non una variante riuscita',
   'andato terribilmente storto' in by[16]['italian'] and 'deforme' in by[16]['italian'])
ck('ZERO tab e ZERO segnaposto in entrambe le lingue',
   sum(u['english'].count(TAB) + u['italian'].count(TAB) for u in tu) == 0
   and not [t for u in tu for t in TAG.findall(u['english']) + TAG.findall(u['italian'])])
ck('APICI: zero in inglese, 6 in italiano su 6 unita',
   sum(u['english'].count(APOS) for u in tu) == 0 and sum(u['italian'].count(APOS) for u in tu) == 6
   and sorted(u['idx'] for u in tu if APOS in u['italian']) == [5, 10, 11, 15, 20, 21],
   (sum(u['english'].count(APOS) for u in tu), sum(u['italian'].count(APOS) for u in tu)))
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in tu for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90 per ogni unita',
   all(0.55 < u['ratio'] < 1.90 for u in tu),
   [(u['idx'], u['ratio']) for u in tu if not 0.55 < u['ratio'] < 1.90])
ck('tutte le 22 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in tu))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print("FILE: 65/65 unita' · 2 lotti (43 + 22) · 65 righe distinte · ultima riga 1007 · 0 dopo")
print('parole EN %d -> IT %d · ratio %.2f - %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(u['ratio'] for u in tu), max(u['ratio'] for u in tu)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L266 superato' if not fail else 'verify L266 fallito')
raise SystemExit(0 if not fail else 1)
