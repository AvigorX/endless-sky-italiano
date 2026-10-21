r"""verify.py — L267 (`data/human/engines.txt`, righe 27-194). **Primo lotto del file**.

Verifica da sola: riga grezza, campi del DB, il **segmento** (0 prima della 27, **49** dopo la 194 — il lotto apre il file),
gli **otto contesti** con le righe, i **tre tab** (141, 159, 177) e le **due virgolette** (121) per unita', il `VALUE`
copiato, e che **nessun altro lotto** rivendichi queste righe.

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
OUTFIT = ['Volcano Afterburner', 'Caldera Afterburner', 'Ionic Afterburner', 'X1050 Ion Engines',
          'X1700 Ion Thruster', 'X2700 Ion Thruster', 'X3700 Ion Thruster', 'X4700 Ion Thruster']
src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
su = sorted(src['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
raw_lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
fail = []


def ck(n, c, d=''):
    print('%-96s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente (12/12)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = [u['idx'] for u in su
       if db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
       != (u['english'], u['kind'], u['path'], u['context'])]
ck('english/kind/path/context identici al DB', not bad, bad)
ck('12 unita, righe 27-194, tipi 11/1',
   len(tu) == 12 and [u['line'] for u in tu] == sorted({u['line'] for u in tu})
   and collections.Counter(u['kind'] for u in tu) == {'DESCRIPTION': 11, 'VALUE': 1},
   (len(tu), collections.Counter(u['kind'] for u in tu)))
ck('gli otto equipaggiamenti compaiono in quest ordine, senza altri',
   [c.replace('outfit:', '') for c in dict.fromkeys(u['context'] for u in tu)] == OUTFIT,
   [c for c in dict.fromkeys(u['context'] for u in tu)])
ck("ZERO unita' prima della 27: il lotto APRE il file",
   db.execute('select count(*) from units where path=? and line<27', (PATH,)).fetchone()[0] == 0)
ck("49 unita' dopo la 194", db.execute('select count(*) from units where path=? and line>194', (PATH,)).fetchone()[0] == 49)
ck('confine: la 195 apre `outfit:X4700 Ion Thruster`, il contesto dell ultima unita',
   db.execute('select line,context from units where path=? and line>194 order by line limit 1', (PATH,)).fetchone()
   == (195, 'outfit:X4700 Ion Thruster'))
ck('il file ha 61 unita, righe 27-717',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (61, 27, 717))
per_lotto, righe = [], set()
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    us = [u for u in json.load(open(f, encoding='utf-8'))['units'] if u['path'] == PATH]
    if us:
        per_lotto.append((os.path.basename(os.path.dirname(f)), len(us)))
        righe |= {u['line'] for u in us}
seg = {l for l in righe if 27 <= l <= 194}
ck('SEGMENTO: le 12 righe del lotto sono esattamente quelle 27-194',
   seg == {u['line'] for u in tu} and len(seg) == 12, (sorted(seg - {u['line'] for u in tu}), len(seg)))
overlap = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    if os.path.basename(os.path.dirname(f)) == os.path.basename(HERE):
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH and 27 <= u['line'] <= 194:
            overlap.append((os.path.basename(os.path.dirname(f)), u['line']))
ck('nessun altro lotto rivendica le righe 27-194', not overlap, overlap)
ck('copertura del SEGMENTO: 12/12 righe; il totale del file e stampato, non asserito',
   len(seg) == 12 and 61 - len(seg) == 49, '%d/61 (file)' % len(righe))
ck('il VALUE e copiato; le 11 DESCRIPTION sono tradotte',
   all(u['italian'] == u['english'] for u in tu if u['kind'] == 'VALUE')
   and all(u['italian'] != u['english'] for u in tu if u['kind'] == 'DESCRIPTION'))
ck('TAB: tre, alle righe 141, 159 e 177, primi caratteri in entrambe le lingue',
   sum(u['english'].count(TAB) for u in tu) == 3 == sum(u['italian'].count(TAB) for u in tu)
   and [u['line'] for u in tu if TAB in u['italian']] == [141, 159, 177]
   and all(u['italian'].startswith(TAB) for u in tu if TAB in u['italian']))
ck('VIRGOLETTE: due, entrambe all unita della riga 121 e dritte',
   sum(u['english'].count(QUOTE) for u in tu) == 2 == sum(u['italian'].count(QUOTE) for u in tu)
   and [u['line'] for u in tu if QUOTE in u['italian']] == [121])
by = {u['idx']: u for u in tu}
ck('le tre copie della scheda ionica hanno una sola resa',
   len({by[u['idx']]['italian'] for u in tu if u['line'] in (141, 159, 177)}) == 1)
ck('APICI: uno in inglese (riga 83), 6 in italiano su 5 unita',
   sum(u['english'].count(APOS) for u in tu) == 1 and sum(u['italian'].count(APOS) for u in tu) == 6,
   (sum(u['english'].count(APOS) for u in tu), sum(u['italian'].count(APOS) for u in tu)))
ck('ZERO segnaposto in entrambe le lingue',
   not [t for u in tu for t in TAG.findall(u['english']) + TAG.findall(u['italian'])])
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in tu for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90 per ogni unita',
   all(0.55 < u['ratio'] < 1.90 for u in tu),
   [(u['idx'], u['ratio']) for u in tu if not 0.55 < u['ratio'] < 1.90])
ck('terminologia del corpus presente: postbruciatore, propulsore, carburante per l\'iperspazio, motori ionici',
   'postbruciatore' in by[1]['italian'] and 'propulsore' in by[6]['italian']
   and "carburante per l'iperspazio" in by[1]['italian'] and 'motori ionici' in by[7]['italian'])
ck('tutte le 12 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in tu))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('SEGMENTO: 0 prima · 12 qui · 49 dopo · 8 contesti · 3 tab · 2 virgolette')
print('parole EN %d -> IT %d · ratio %.2f - %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(u['ratio'] for u in tu), max(u['ratio'] for u in tu)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L267 superato' if not fail else 'verify L267 fallito')
raise SystemExit(0 if not fail else 1)
