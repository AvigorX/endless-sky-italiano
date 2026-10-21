r"""verify.py — L270 (`data/human/engines.txt`, righe 488-717). **LOTTO TERMINALE: chiude il file.**

Verifica da sola: riga grezza, campi del DB, il **segmento** (44 prima, 17 qui, **0 dopo** la 717) e l'**invariante di FILE**
(61 unità, righe distinte, ultima riga 717, somma dei quattro lotti), i **quattordici contesti** con le righe, i **quattro
tab**, e che **nessun altro lotto** rivendichi queste righe.

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
OUTFIT = ['Orca Plasma Steering', 'Tyrant Plasma Steering', 'Capybara Reverse Thruster',
          'A120 Atomic Thruster', 'A250 Atomic Thruster', 'A370 Atomic Thruster', 'A520 Atomic Thruster',
          'A860 Atomic Thruster', 'A125 Atomic Steering', 'A255 Atomic Steering', 'A375 Atomic Steering',
          'A525 Atomic Steering', 'A865 Atomic Steering', 'AR120 Reverse Thruster']
src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
su = sorted(src['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
raw_lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
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
ck('17 unita, righe 488-717, tutte DESCRIPTION',
   len(tu) == 17 and [u['line'] for u in tu] == sorted({u['line'] for u in tu})
   and {u['kind'] for u in tu} == {'DESCRIPTION'}, (len(tu), {u['kind'] for u in tu}))
ck('i quattordici equipaggiamenti compaiono in quest ordine, senza altri',
   [c.replace('outfit:', '') for c in dict.fromkeys(u['context'] for u in tu)] == OUTFIT,
   [c for c in dict.fromkeys(u['context'] for u in tu)])
ck("44 unita' prima (L267 + L268 + L269)",
   db.execute('select count(*) from units where path=? and line<488', (PATH,)).fetchone()[0] == 44)
ck("ZERO unita' dopo la 717: il lotto CHIUDE il file",
   db.execute('select count(*) from units where path=? and line>717', (PATH,)).fetchone()[0] == 0)
ck('INVARIANTE DI FILE: il database ha 61 unita, righe 27-717, ultima alla 717',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (61, 27, 717))
per_lotto, righe = [], set()
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    us = [u for u in json.load(open(f, encoding='utf-8'))['units'] if u['path'] == PATH]
    if us:
        per_lotto.append((os.path.basename(os.path.dirname(f)), len(us)))
        righe |= {u['line'] for u in us}
seg = {l for l in righe if 488 <= l <= 717}
ck('SEGMENTO: le 17 righe del lotto sono esattamente quelle 488-717',
   seg == {u['line'] for u in tu} and len(seg) == 17, (sorted(seg - {u['line'] for u in tu}), len(seg)))
ck('INVARIANTE DI FILE: quattro lotti, somma 61, righe distinte 61, nessuna riga fuori',
   sum(n for _, n in per_lotto) == 61 and len(righe) == 61 and min(righe) == 27 and max(righe) == 717,
   (sum(n for _, n in per_lotto), len(righe)))
ck('COPERTURA: 61/61 righe del file (100%)', len(righe) == 61, '%d/61' % len(righe))
overlap = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    if os.path.basename(os.path.dirname(f)) == os.path.basename(HERE):
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH and 488 <= u['line'] <= 717:
            overlap.append((os.path.basename(os.path.dirname(f)), u['line']))
ck('nessun altro lotto rivendica le righe 488-717', not overlap, overlap)
ck('tutte tradotte, nessuna copiata',
   not [u['idx'] for u in tu if u['italian'] == u['english']],
   [u['idx'] for u in tu if u['italian'] == u['english']])
ck('TAB: quattro, primi caratteri in entrambe le lingue',
   sum(u['english'].count(TAB) for u in tu) == 4 == sum(u['italian'].count(TAB) for u in tu)
   and [u['idx'] for u in tu if TAB in u['italian']] == [1, 3, 5, 17]
   and all(u['italian'].startswith(TAB) for u in tu if TAB in u['italian']))
by = {u['idx']: u for u in tu}
ck('la nota del plasma (unita 1, 3) ha una sola resa',
   len({by[1]['italian'], by[3]['italian']}) == 1)
ck('la nota del montaggio (unita 5, 17) ha una sola resa',
   len({by[5]['italian'], by[17]['italian']}) == 1)
ck('ZERO virgolette e ZERO segnaposto',
   sum(u['english'].count(QUOTE) + u['italian'].count(QUOTE) for u in tu) == 0
   and not [t for u in tu for t in TAG.findall(u['english']) + TAG.findall(u['italian'])])
ck('apici: 7 in inglese, 8 in italiano',
   sum(u['english'].count(APOS) for u in tu) == 7 and sum(u['italian'].count(APOS) for u in tu) == 8,
   (sum(u['english'].count(APOS) for u in tu), sum(u['italian'].count(APOS) for u in tu)))
ck('lessico: propulsori atomici, motori atomici, sterzata, propulsore inverso',
   'propulsori atomici' in by[6]['italian'] and 'motori atomici' in by[9]['italian']
   and 'sterzata' in by[2]['italian'] and 'propulsore inverso' in by[4]['italian'])
ck('Deep Sky invariato e i numeri dei modelli restano nei contesti',
   'Deep Sky' in by[6]['italian'] and all(any(n in u['context'] for u in tu) for n in
                                         ('A120', 'A860', 'A125', 'A865')))
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in tu for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90 per ogni unita',
   all(0.55 < u['ratio'] < 1.90 for u in tu),
   [(u['idx'], u['ratio']) for u in tu if not 0.55 < u['ratio'] < 1.90])
ck('tutte le 17 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in tu))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('SEGMENTO: 44 prima · 17 qui · 0 dopo (FINE FILE) · 14 contesti · 4 tab')
print('parole EN %d -> IT %d · ratio %.2f - %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(u['ratio'] for u in tu), max(u['ratio'] for u in tu)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L270 superato' if not fail else 'verify L270 fallito')
raise SystemExit(0 if not fail else 1)
