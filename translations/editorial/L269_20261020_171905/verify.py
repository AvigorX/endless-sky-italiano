r"""verify.py — L269 (`data/human/engines.txt`, righe 342-487). **Terzo lotto del file**.

Verifica da sola: riga grezza, campi del DB, il **segmento** (27 prima, 17 qui, **17** dopo la 487), i **nove contesti** con
le righe, gli **otto tab** della nota del plasma, l'unica resa della nota, e che **nessun altro lotto** rivendichi queste
righe.

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
OUTFIT = ['Chipmunk Plasma Thruster', 'Greyhound Plasma Thruster', 'Impala Plasma Thruster',
          'Orca Plasma Thruster', 'Tyrant Plasma Thruster', 'Chipmunk Plasma Steering',
          'Greyhound Plasma Steering', 'Impala Plasma Steering', 'Orca Plasma Steering']
NOTA = [2, 4, 6, 8, 10, 12, 14, 16]
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
ck('17 unita, righe 342-487, tutte DESCRIPTION',
   len(tu) == 17 and [u['line'] for u in tu] == sorted({u['line'] for u in tu})
   and {u['kind'] for u in tu} == {'DESCRIPTION'}, (len(tu), {u['kind'] for u in tu}))
ck('i nove equipaggiamenti compaiono in quest ordine, senza altri',
   [c.replace('outfit:', '') for c in dict.fromkeys(u['context'] for u in tu)] == OUTFIT,
   [c for c in dict.fromkeys(u['context'] for u in tu)])
ck("27 unita' prima (L267 + L268)",
   db.execute('select count(*) from units where path=? and line<342', (PATH,)).fetchone()[0] == 27)
ck("17 unita' dopo la 487", db.execute('select count(*) from units where path=? and line>487', (PATH,)).fetchone()[0] == 17)
ck('confine: la 488 resta in `Orca Plasma Steering`, poi cambia contesto',
   db.execute('select line,context from units where path=? and line>487 order by line limit 1', (PATH,)).fetchone()
   == (488, 'outfit:Orca Plasma Steering'))
ck('il file ha 61 unita, righe 27-717',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (61, 27, 717))
per_lotto, righe = [], set()
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    us = [u for u in json.load(open(f, encoding='utf-8'))['units'] if u['path'] == PATH]
    if us:
        per_lotto.append((os.path.basename(os.path.dirname(f)), len(us)))
        righe |= {u['line'] for u in us}
seg = {l for l in righe if 342 <= l <= 487}
ck('SEGMENTO: le 17 righe del lotto sono esattamente quelle 342-487',
   seg == {u['line'] for u in tu} and len(seg) == 17, (sorted(seg - {u['line'] for u in tu}), len(seg)))
overlap = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    if os.path.basename(os.path.dirname(f)) == os.path.basename(HERE):
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH and 342 <= u['line'] <= 487:
            overlap.append((os.path.basename(os.path.dirname(f)), u['line']))
ck('nessun altro lotto rivendica le righe 342-487', not overlap, overlap)
ck('copertura del SEGMENTO: 17/17 righe; il totale del file e stampato, non asserito',
   len(seg) == 17 and 61 - len(seg) == 44, '%d/61 (file)' % len(righe))
ck('tutte tradotte, nessuna copiata',
   not [u['idx'] for u in tu if u['italian'] == u['english']],
   [u['idx'] for u in tu if u['italian'] == u['english']])
ck('TAB: otto, sulle sole unita della nota, primi caratteri in entrambe le lingue',
   sum(u['english'].count(TAB) for u in tu) == 8 == sum(u['italian'].count(TAB) for u in tu)
   and [u['idx'] for u in tu if TAB in u['italian']] == NOTA
   and all(u['italian'].startswith(TAB) for u in tu if u['idx'] in NOTA))
by = {u['idx']: u for u in tu}
ck('la nota del plasma ripetuta otto volte ha una sola resa',
   len({by[i]['italian'] for i in NOTA}) == 1)
ck('ZERO virgolette e ZERO segnaposto',
   sum(u['english'].count(QUOTE) + u['italian'].count(QUOTE) for u in tu) == 0
   and not [t for u in tu for t in TAG.findall(u['english']) + TAG.findall(u['italian'])])
ck('apici: uno in inglese (riga 451), 11 in italiano',
   sum(u['english'].count(APOS) for u in tu) == 1 and sum(u['italian'].count(APOS) for u in tu) == 11,
   (sum(u['english'].count(APOS) for u in tu), sum(u['italian'].count(APOS) for u in tu)))
ck('lessico: propulsione al plasma, sterzata al plasma, motori al plasma',
   'propulsione al plasma' in by[1]['italian'] and 'sterzata al plasma' in by[11]['italian']
   and 'motori al plasma' in by[2]['italian'])
ck('i nomi di modello restano dove l inglese li nomina',
   not [(u['idx'], n) for u in tu for n in ('Greyhound', 'Impala', 'Orca', 'Tyrant')
        if n in u['english'] and n not in u['italian']])
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
print('SEGMENTO: 27 prima · 17 qui · 17 dopo · 9 contesti · 8 tab')
print('parole EN %d -> IT %d · ratio %.2f - %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(u['ratio'] for u in tu), max(u['ratio'] for u in tu)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L269 superato' if not fail else 'verify L269 fallito')
raise SystemExit(0 if not fail else 1)
