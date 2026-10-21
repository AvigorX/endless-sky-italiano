r"""verify.py — L304 (`data/quarg/quarg outfits.txt`, righe 37-137). **PRIMO lotto del file**.

Verifica da sola: riga grezza, campi del DB, il **segmento** (**0** prima, **11** qui, **20** dopo la 137), le **cinque coppie**
con tab, la **prima meta'** della sesta, le **quattro ripetizioni identiche** e la **variante della riga 38**, e che **nessun
altro lotto** rivendichi le righe 37-137.

Il **confine** e' un caso dichiarato: la **137** e' la **prima** unita' di `Large Graviton Steering`, la **138** la **seconda**,
fuori segmento. Il test verifica il taglio **dove e' stato dichiarato**, non che i contesti cambino.

Indipendente da `check.py`. La copertura del **FILE** e' **stampata, non asserita**.
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
PATH = 'data/quarg/quarg outfits.txt'
COPPIE = [(37, 38), (54, 55), (77, 78), (95, 96), (119, 120)]
TABBED = [38, 55, 78, 96, 120]
QUATTRO = [4, 6, 8, 10]
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


ck('riga grezza identica al sorgente (11/11)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = [u['idx'] for u in su
       if db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
       != (u['english'], u['kind'], u['path'], u['context'])]
ck('english/kind/path/context identici al DB', not bad, bad)
grp = collections.Counter(u['context'] for u in tu)
ck('11 unita DESCRIPTION, sei contesti (5 doppi + 1 prima meta)',
   len(tu) == 11 and {u['kind'] for u in tu} == {'DESCRIPTION'}
   and sorted(grp.values()) == [1, 2, 2, 2, 2, 2], dict(grp))
ck("ZERO unita' prima della 37 e 20 dopo la 137",
   db.execute('select count(*) from units where path=? and line<37', (PATH,)).fetchone()[0] == 0
   and db.execute('select count(*) from units where path=? and line>137', (PATH,)).fetchone()[0] == 20)
ck('la 138 e la SECONDA meta di `Large Graviton Steering` (taglio dichiarato)',
   db.execute('select line,context from units where path=? and line>137 order by line limit 1', (PATH,)).fetchone()
   == (138, 'outfit:Large Graviton Steering')
   and at[137]['context'] == 'outfit:Large Graviton Steering' and not at[137]['english'].startswith(TAB))
ck('il file ha 31 unita, righe 37-579, tutte DESCRIPTION',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (31, 37, 579))
righe = set()
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH:
            righe.add(u['line'])
seg = {l for l in righe if 37 <= l <= 137}
ck('SEGMENTO: le 11 righe del lotto sono esattamente quelle 37-137',
   seg == {u['line'] for u in tu} and len(seg) == 11, (sorted(seg - {u['line'] for u in tu}), len(seg)))
overlap = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    if os.path.basename(os.path.dirname(f)) == os.path.basename(HERE):
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH and 37 <= u['line'] <= 137:
            overlap.append((os.path.basename(os.path.dirname(f)), u['line']))
ck('nessun altro lotto rivendica le righe 37-137', not overlap, overlap)
ck('copertura: 11 righe nel segmento; totale del file stampato e non supera 31',
   len(seg) == 11 and len(righe) <= 31, '%d/31 al momento' % len(righe))
ck('tutte e 11 le unita sono tradotte', all(u['italian'] != u['english'] for u in tu))
ck('TAB: cinque unita, righe dichiarate, primo carattere conservato',
   sorted(u['line'] for u in tu if u['english'].startswith(TAB)) == TABBED
   and all(at[l]['italian'].startswith(TAB) for l in TABBED)
   and sum(u['italian'].count(TAB) for u in tu) == 5)
ck('le cinque coppie hanno lo stesso contesto e la tab sulla seconda',
   all(at[b]['context'] == at[a]['context'] and at[b]['english'].startswith(TAB) for a, b in COPPIE))
ck('RIPETIZIONE: le quattro 4, 6, 8, 10 identiche in inglese e in italiano',
   len({by[i]['english'] for i in QUATTRO}) == 1 and len({by[i]['italian'] for i in QUATTRO}) == 1)
ck('VARIANTE 38: diversa dalle quattro, con `These engines` -> «Questi motori»',
   by[2]['italian'] != by[4]['italian'] and 'Questi motori' in by[2]['italian']
   and 'ne sono dotate' in by[2]['italian'])
ck('ASSERZIONI VUOTE: 0 virgolette, 0 segnaposto, 0 alternative',
   sum(u['english'].count(QUOTE) for u in tu) == 0 == sum(u['italian'].count(QUOTE) for u in tu)
   and sum(len(TAG.findall(u['italian'])) for u in tu) == 0
   and sum(len(ALT.findall(u['italian'])) for u in tu) == 0)
ck('apici: 1 in inglese, 11 in italiano',
   sum(u['english'].count(APOS) for u in tu) == 1 and sum(u['italian'].count(APOS) for u in tu) == 11,
   (sum(u['english'].count(APOS) for u in tu), sum(u['italian'].count(APOS) for u in tu)))
ck('terminologia: propulsori Quarg, motori di governo, centro di massa, giroscopio, onde gravitazionali',
   'propulsori Quarg' in at[37]['italian'] and 'motori di governo' in at[54]['italian']
   and 'centro di massa' in at[54]['italian'] and 'giroscopio' in at[95]['italian']
   and 'onde gravitazionali' in at[77]['italian'])
ck('registro: nessuna seconda persona',
   not [u['idx'] for u in tu if re.search(r'\b(tu|tuo|tua|tuoi|tue|ti|te)\b', u['italian'])])
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in tu for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessun doppio spazio (la tab iniziale non conta)',
   not [u['idx'] for u in tu if '  ' in u['italian'].lstrip(TAB)])
ck('rapporto nel gate 0,55-1,90',
   all(0.55 < u['ratio'] < 1.90 for u in tu),
   [(u['idx'], u['ratio']) for u in tu if not 0.55 < u['ratio'] < 1.90])
ck('tutte le 11 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in tu))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('SEGMENTO: 0 prima · 11 qui · 20 dopo la 137 · 5 coppie + 1 prima meta · file %d/31' % len(righe))
print('parole EN %d -> IT %d · ratio %.2f - %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(u['ratio'] for u in tu), max(u['ratio'] for u in tu)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L304 superato' if not fail else 'verify L304 fallito')
raise SystemExit(0 if not fail else 1)
