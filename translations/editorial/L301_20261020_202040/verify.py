r"""verify.py — L301 (`data/remnant/remnant ships.txt`, righe 17-806). **PRIMO lotto del file**.

Verifica da sola: riga grezza, campi del DB, il **segmento** (**0** prima, **12** qui, **26** dopo la 806), i **due `VALUE`
copiati**, le **due terzine** con due tab consecutive, la **coppia** 474/475, la **ripetizione 350/474**, le **quattro
virgolette**, e che **nessun altro lotto** rivendichi le righe 17-806.

Il **confine** e' un caso dichiarato: la **806** e' l'unica unita' `Heron` del lotto e la **807** e' la **seconda** unita' dello
**stesso** contesto, fuori segmento. Il test verifica che il taglio sia **dove e' stato dichiarato**, non che i contesti cambino.

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
PATH = 'data/remnant/remnant ships.txt'
TRIPLE1 = [350, 351, 352]
TRIPLE2 = [547, 548, 549]
TABBED = [351, 352, 475, 548, 549]
VALUES = {1: 'Albatrosses', 3: 'Modified Dromedaries'}
NAMES = ['Remnant', 'Alphas', 'Korath', 'Starling', 'Shattered Light', 'Tycho Crater Cooperative']
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


ck('riga grezza identica al sorgente (12/12)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = [u['idx'] for u in su
       if db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
       != (u['english'], u['kind'], u['path'], u['context'])]
ck('english/kind/path/context identici al DB', not bad, bad)
grp = collections.Counter(u['context'] for u in tu)
ck('12 unita: 10 DESCRIPTION + 2 VALUE; contesti 6 + 3 + 2 + 1',
   len(tu) == 12 and collections.Counter(u['kind'] for u in tu) == {'DESCRIPTION': 10, 'VALUE': 2}
   and dict(grp) == {'ship:Modified Dromedary': 6, 'ship:Gull': 3, 'ship:Albatross': 2, 'ship:Heron': 1}, dict(grp))
ck("ZERO unita' prima della 17 (il lotto apre il file) e 26 dopo la 806",
   db.execute('select count(*) from units where path=? and line<17', (PATH,)).fetchone()[0] == 0
   and db.execute('select count(*) from units where path=? and line>806', (PATH,)).fetchone()[0] == 26)
ck('la 807 e la SECONDA unita di `Heron` (taglio dichiarato, non coppia spezzata nel lotto)',
   db.execute('select line,context from units where path=? and line>806 order by line limit 1', (PATH,)).fetchone()
   == (807, 'ship:Heron')
   and sum(1 for u in tu if u['context'] == 'ship:Heron') == 1)
ck('il file ha 38 unita (35 DESCRIPTION + 3 VALUE), righe 17-1826',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (38, 17, 1826))
righe = set()
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH:
            righe.add(u['line'])
seg = {l for l in righe if 17 <= l <= 806}
ck('SEGMENTO: le 12 righe del lotto sono esattamente quelle 17-806',
   seg == {u['line'] for u in tu} and len(seg) == 12, (sorted(seg - {u['line'] for u in tu}), len(seg)))
overlap = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    if os.path.basename(os.path.dirname(f)) == os.path.basename(HERE):
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH and 17 <= u['line'] <= 806:
            overlap.append((os.path.basename(os.path.dirname(f)), u['line']))
ck('nessun altro lotto rivendica le righe 17-806', not overlap, overlap)
ck('copertura: 12 righe nel segmento; totale del file stampato e non supera 38',
   len(seg) == 12 and len(righe) <= 38, '%d/38 al momento' % len(righe))
ck('VALUE copiati identici all inglese',
   all(by[i]['italian'] == VALUES[i] == by[i]['english'] for i in VALUES))
ck('le 10 DESCRIPTION sono tutte tradotte',
   all(u['italian'] != u['english'] for u in tu if u['kind'] == 'DESCRIPTION'))
ck('TERZINE e tab: 350/351/352 e 547/548/549 con due tab consecutive; 5 tab in tutto',
   [u['line'] for u in tu if u['context'] == 'ship:Modified Dromedary'
    and u['kind'] == 'DESCRIPTION' and u['line'] < 400] == TRIPLE1
   and [u['line'] for u in tu if u['context'] == 'ship:Gull'] == TRIPLE2
   and sorted(u['line'] for u in tu if u['english'].startswith(TAB)) == TABBED
   and sum(u['italian'].count(TAB) for u in tu) == 5)
ck('COPPIA 474/475 con tab sulla seconda', at[475]['context'] == at[474]['context']
   and at[475]['english'].startswith(TAB) and at[475]['italian'].startswith(TAB))
ck('RIPETIZIONE: 350 e 474 identiche in inglese e in italiano',
   at[350]['english'] == at[474]['english'] and at[350]['italian'] == at[474]['italian'])
ck('VIRGOLETTE: 4 in inglese, 4 in italiano, tutte dritte, su "celle del sogno"',
   sum(u['english'].count(QUOTE) for u in tu) == 4 == sum(u['italian'].count(QUOTE) for u in tu)
   and at[350]['italian'].count(QUOTE) == 2 and 'celle del sogno' in at[350]['italian'])
ck('ASSERZIONI VUOTE: 0 segnaposto, 0 alternative',
   sum(len(TAG.findall(u['italian'])) for u in tu) == 0
   and sum(len(ALT.findall(u['italian'])) for u in tu) == 0)
ck('apici: 6 in inglese, 14 in italiano',
   sum(u['english'].count(APOS) for u in tu) == 6 and sum(u['italian'].count(APOS) for u in tu) == 14,
   (sum(u['english'].count(APOS) for u in tu), sum(u['italian'].count(APOS) for u in tu)))
ck('nomi invariati', all(n in ''.join(u['italian'] for u in tu) for n in NAMES),
   [n for n in NAMES if n not in ''.join(u['italian'] for u in tu)])
ck('registro: nessuna seconda persona',
   not [u['idx'] for u in tu if re.search(r'\b(tu|tuo|tua|tuoi|tue|ti|te)\b', u['italian'])])
ck('terminologia: navi-città, serre idroponiche, spazioporti mobili, occultamento',
   'navi-città' in at[350]['italian'] and 'serre idroponiche' in at[350]['italian']
   and 'spazioporti mobili' in at[806]['italian'] and 'occultamento' in at[549]['italian'])
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in tu for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessun doppio spazio (la tab iniziale non conta)',
   not [u['idx'] for u in tu if '  ' in u['italian'].lstrip(TAB)])
ck('rapporto nel gate 0,55-1,90',
   all(0.55 < u['ratio'] < 1.90 for u in tu),
   [(u['idx'], u['ratio']) for u in tu if not 0.55 < u['ratio'] < 1.90])
ck('tutte le 12 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in tu))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('SEGMENTO: 0 prima · 12 qui · 26 dopo la 806 · 2 terzine + 1 coppia · file %d/38' % len(righe))
print('parole EN %d -> IT %d · ratio %.2f - %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(u['ratio'] for u in tu), max(u['ratio'] for u in tu)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L301 superato' if not fail else 'verify L301 fallito')
raise SystemExit(0 if not fail else 1)
