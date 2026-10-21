r"""verify.py — L268 (`data/human/engines.txt`, righe 195-323). **Secondo lotto del file**.

Verifica da sola: riga grezza, campi del DB, il **segmento** (12 prima, 15 qui, **34** dopo la 323), gli **otto contesti**
con le righe, gli **otto tab**, la scheda ionica ripetuta, e che **nessun altro lotto** rivendichi queste righe.

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
PATH = 'data/human/engines.txt'
OUTFIT = ['X4700 Ion Thruster', 'X5700 Ion Thruster', 'X1200 Ion Steering', 'X2200 Ion Steering',
          'X3200 Ion Steering', 'X4200 Ion Steering', 'X5200 Ion Steering', 'X1100 Ion Reverse Thruster']
src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
su = sorted(src['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
raw_lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
fail = []


def ck(n, c, d=''):
    print('%-96s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente (15/15)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = [u['idx'] for u in su
       if db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
       != (u['english'], u['kind'], u['path'], u['context'])]
ck('english/kind/path/context identici al DB', not bad, bad)
ck('15 unita, righe 195-323, tutte DESCRIPTION',
   len(tu) == 15 and [u['line'] for u in tu] == sorted({u['line'] for u in tu})
   and {u['kind'] for u in tu} == {'DESCRIPTION'}, (len(tu), {u['kind'] for u in tu}))
ck('gli otto equipaggiamenti compaiono in quest ordine, senza altri',
   [c.replace('outfit:', '') for c in dict.fromkeys(u['context'] for u in tu)] == OUTFIT,
   [c for c in dict.fromkeys(u['context'] for u in tu)])
ck("12 unita' prima, e la precedente e lo stesso equipaggiamento (X4700)",
   db.execute('select count(*) from units where path=? and line<195', (PATH,)).fetchone()[0] == 12
   and db.execute('select context from units where path=? and line<195 order by line desc limit 1', (PATH,)).fetchone()
   == ('outfit:X4700 Ion Thruster',))
ck("34 unita' dopo la 323", db.execute('select count(*) from units where path=? and line>323', (PATH,)).fetchone()[0] == 34)
ck('confine: la 342 apre un equipaggiamento nuovo (`Chipmunk Plasma Thruster`)',
   db.execute('select line,context from units where path=? and line>323 order by line limit 1', (PATH,)).fetchone()
   == (342, 'outfit:Chipmunk Plasma Thruster'))
ck('il file ha 61 unita, righe 27-717',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (61, 27, 717))
per_lotto, righe = [], set()
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    us = [u for u in json.load(open(f, encoding='utf-8'))['units'] if u['path'] == PATH]
    if us:
        per_lotto.append((os.path.basename(os.path.dirname(f)), len(us)))
        righe |= {u['line'] for u in us}
seg = {l for l in righe if 195 <= l <= 323}
ck('SEGMENTO: le 15 righe del lotto sono esattamente quelle 195-323',
   seg == {u['line'] for u in tu} and len(seg) == 15, (sorted(seg - {u['line'] for u in tu}), len(seg)))
overlap = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    if os.path.basename(os.path.dirname(f)) == os.path.basename(HERE):
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH and 195 <= u['line'] <= 323:
            overlap.append((os.path.basename(os.path.dirname(f)), u['line']))
ck('nessun altro lotto rivendica le righe 195-323', not overlap, overlap)
ck('copertura del SEGMENTO: 15/15 righe; il totale del file e stampato, non asserito',
   len(seg) == 15 and 61 - len(seg) == 46, '%d/61 (file)' % len(righe))
ck('tutte tradotte, nessuna copiata',
   not [u['idx'] for u in tu if u['italian'] == u['english']],
   [u['idx'] for u in tu if u['italian'] == u['english']])
ck('TAB: otto, uno per blocco, primi caratteri in entrambe le lingue',
   sum(u['english'].count(TAB) for u in tu) == 8 == sum(u['italian'].count(TAB) for u in tu)
   and [u['idx'] for u in tu if TAB in u['italian']] == [1, 3, 5, 7, 9, 11, 13, 15]
   and all(u['italian'].startswith(TAB) for u in tu if TAB in u['italian']))
by = {u['idx']: u for u in tu}
ck('la scheda ionica ripetuta sette volte ha una sola resa',
   len({by[i]['italian'] for i in (1, 3, 5, 7, 9, 11, 13)}) == 1)
ck('ZERO virgolette, ZERO apici in inglese e ZERO segnaposto',
   sum(u['english'].count(QUOTE) + u['italian'].count(QUOTE) for u in tu) == 0
   and sum(u['english'].count(APOS) for u in tu) == 0
   and not [t for u in tu for t in TAG.findall(u['english']) + TAG.findall(u['italian'])])
ck('apici italiani: 6, uno per unita',
   sum(u['italian'].count(APOS) for u in tu) == 6
   and sorted(u['idx'] for u in tu if APOS in u['italian']) == [2, 4, 6, 10, 12, 14],
   sum(u['italian'].count(APOS) for u in tu))
ck('lessico: sterzata, propulsore inverso, navi capitali, mercantili',
   'sterzata' in by[4]['italian'] and 'propulsore inverso' in by[14]['italian']
   and 'navi capitali' in by[2]['italian'] and 'mercantili' in by[8]['italian'])
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in tu for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90 per ogni unita',
   all(0.55 < u['ratio'] < 1.90 for u in tu),
   [(u['idx'], u['ratio']) for u in tu if not 0.55 < u['ratio'] < 1.90])
ck('tutte le 15 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in tu))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('SEGMENTO: 12 prima · 15 qui · 34 dopo · 8 contesti · 8 tab')
print('parole EN %d -> IT %d · ratio %.2f - %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(u['ratio'] for u in tu), max(u['ratio'] for u in tu)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L268 superato' if not fail else 'verify L268 fallito')
raise SystemExit(0 if not fail else 1)
