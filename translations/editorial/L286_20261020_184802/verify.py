r"""verify.py — L286 (`data/gegno/gegno ships.txt`, righe 53-302). **Primo lotto del file**.

Verifica da sola: riga grezza, campi del DB, il **segmento** (0 prima — il lotto **apre** il file — 7 qui, **30** dopo la 302), i
**sei contesti** con le righe, le **asserzioni vuote** (0 virgolette, 0 segnaposto, 0 alternative), il **tab unico**, i nomi di
modello invariati, il **refuso `Gypusm's`**, e che **nessun altro lotto** rivendichi le righe 53-302.

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
ALT = re.compile(r'\[[^\]]*\]')
HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
ROOT = os.path.abspath(os.path.join(L10N, '..'))
PATH = 'data/gegno/gegno ships.txt'
CTX = [('ship:Shale', 53), ('ship:Dolomite', 97), ('ship:Conglomerate', 146), ('ship:Granofel', 194),
       ('ship:Gypsum', 243), ('ship:Gypsum', 244), ('ship:Corundum', 302)]
src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
su = sorted(src['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
raw_lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
by = {u['idx']: u for u in tu}
fail = []


def ck(n, c, d=''):
    print('%-96s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente (7/7)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = [u['idx'] for u in su
       if db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
       != (u['english'], u['kind'], u['path'], u['context'])]
ck('english/kind/path/context identici al DB', not bad, bad)
ck('7 unita, righe distinte, tutte DESCRIPTION',
   len(tu) == 7 and len({u['line'] for u in tu}) == 7 and {u['kind'] for u in tu} == {'DESCRIPTION'})
ck('sei contesti con le righe dichiarate (53, 97, 146, 194, 243, 244, 302)',
   [(u['context'], u['line']) for u in tu] == CTX, [(u['context'], u['line']) for u in tu])
ck("ZERO unita' prima della 53: il lotto APRE il file",
   db.execute('select count(*) from units where path=? and line<53', (PATH,)).fetchone()[0] == 0)
ck("30 unita' dopo la 302",
   db.execute('select count(*) from units where path=? and line>302', (PATH,)).fetchone()[0] == 30)
ck('confine: la 303 riprende `ship:Corundum`',
   db.execute('select line,context from units where path=? and line>302 order by line limit 1', (PATH,)).fetchone()
   == (303, 'ship:Corundum'))
ck('il file ha 37 unita, righe 53-1616',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (37, 53, 1616))
righe = set()
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH:
            righe.add(u['line'])
seg = {l for l in righe if 53 <= l <= 302}
ck('SEGMENTO: le 7 righe del lotto sono esattamente quelle 53-302', seg == {u['line'] for u in tu} and len(seg) == 7,
   (sorted(seg - {u['line'] for u in tu}), len(seg)))
overlap = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    if os.path.basename(os.path.dirname(f)) == os.path.basename(HERE):
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH and 53 <= u['line'] <= 302:
            overlap.append((os.path.basename(os.path.dirname(f)), u['line']))
ck('nessun altro lotto rivendica le righe 53-302', not overlap, overlap)
ck('copertura: il lotto copre 7 righe e non supera il file (stampata, non asserita)',
   len(seg) == 7 and len(righe) <= 37, '%d/37 al momento' % len(righe))
ck('tutte le 7 unita sono tradotte', all(u['italian'] != u['english'] for u in tu))
ck('Gypsum: due unita consecutive, la seconda continua la prima',
   by[6]['line'] == by[5]['line'] + 1 and by[5]['context'] == by[6]['context'] == 'ship:Gypsum'
   and by[6]['italian'].lstrip(TAB).startswith('Poiché'))
ck('TAB: uno solo, sull unita 6, primo carattere',
   sum(u['english'].count(TAB) for u in tu) == 1 == sum(u['italian'].count(TAB) for u in tu)
   and [u['idx'] for u in tu if TAB in u['italian']] == [6])
ck('asserzioni vuote: 0 virgolette, 0 segnaposto, 0 alternative in entrambe le lingue',
   sum(u['english'].count(QUOTE) for u in tu) == 0 == sum(u['italian'].count(QUOTE) for u in tu)
   and sum(len(TAG.findall(u['english'])) for u in tu) == 0 == sum(len(TAG.findall(u['italian'])) for u in tu)
   and sum(len(ALT.findall(u['english'])) for u in tu) == 0 == sum(len(ALT.findall(u['italian'])) for u in tu))
ck('apici: 4 in inglese, 6 in italiano',
   sum(u['english'].count(APOS) for u in tu) == 4 and sum(u['italian'].count(APOS) for u in tu) == 6,
   (sum(u['english'].count(APOS) for u in tu), sum(u['italian'].count(APOS) for u in tu)))
ck("refuso del sorgente: `Gypusm's` -> `Gypsum`, e nessun `Gypusm` in italiano",
   "Gypusm's" in by[7]['english'] and 'Gypusm' not in by[7]['italian'])
ck('nomi di modello invariati (Shale, Dolomite, Conglomerate, Granofel, Gypsum, Corundum, Gegno, Vi, Scin)',
   all(n in ''.join(u['italian'] for u in tu)
       for n in ['Shale', 'Dolomite', 'Conglomerate', 'Granofel', 'Gypsum', 'Corundum', 'Gegno', 'Vi', 'Scin',
                 'Shuttle', 'Excavator Drill']))
ck('registro in terza persona: nessun «tu»/«tuo»',
   not [u['idx'] for u in tu if re.search(r'\b(tu|tuo|tua|tuoi|tue|ti|te)\b', u['italian'])])
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in tu for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90',
   all(0.55 < u['ratio'] < 1.90 for u in tu),
   [(u['idx'], u['ratio']) for u in tu if not 0.55 < u['ratio'] < 1.90])
ck('tutte le 7 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in tu))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('SEGMENTO: 0 prima (apre il file) · 7 qui · 30 dopo · 6 contesti')
print('parole EN %d -> IT %d · ratio %.2f - %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(u['ratio'] for u in tu), max(u['ratio'] for u in tu)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L286 superato' if not fail else 'verify L286 fallito')
raise SystemExit(0 if not fail else 1)
