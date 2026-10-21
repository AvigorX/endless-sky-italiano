r"""verify.py — L302 (`data/remnant/remnant ships.txt`, righe 807-1291). **Secondo lotto del file**.

Verifica da sola: riga grezza, campi del DB, il **segmento** (**12** prima, **12** qui, **14** dopo la 1291), la **terzina**
`Peregrine`, le **tre coppie** interne, la **continuita' di `Heron`** con L301 (806 + 807), la **famiglia della formula
dell'occultamento** (riapre `L301/translation.json`), il `VALUE` copiato, e che **nessun altro lotto** rivendichi le righe
807-1291.

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
PREV = os.path.join(L10N, 'staging', 'editorial', 'L301_20261020_202040', 'translation.json')
PATH = 'data/remnant/remnant ships.txt'
TERZINA = [1289, 1290, 1291]
COPPIE = [(892, 893), (981, 982), (1201, 1202)]
TABBED = [807, 893, 982, 1202, 1290, 1291]
CLOAK = {982: 'Merganser', 1202: 'Penguin', 1291: 'Peregrine'}
src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
su = sorted(src['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
raw_lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
by = {u['idx']: u for u in tu}
at = {u['line']: u for u in tu}
prev = {u['line']: u for u in json.load(open(PREV, encoding='utf-8'))['units']}
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
ck('12 unita: 11 DESCRIPTION + 1 VALUE; sei contesti',
   len(tu) == 12 and collections.Counter(u['kind'] for u in tu) == {'DESCRIPTION': 11, 'VALUE': 1}
   and len(grp) == 6 and sorted(grp.values()) == [1, 1, 2, 2, 3, 3], dict(grp))
ck("12 unita' prima della 807 e 14 dopo la 1291",
   db.execute('select count(*) from units where path=? and line<807', (PATH,)).fetchone()[0] == 12
   and db.execute('select count(*) from units where path=? and line>1291', (PATH,)).fetchone()[0] == 14)
ck('la prima unita dopo la 1291 e `Petrel` alla 1378',
   db.execute('select line,context from units where path=? and line>1291 order by line limit 1', (PATH,)).fetchone()
   == (1378, 'ship:Petrel'))
ck('il file ha 38 unita, righe 17-1826',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (38, 17, 1826))
righe = set()
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH:
            righe.add(u['line'])
seg = {l for l in righe if 807 <= l <= 1291}
ck('SEGMENTO: le 12 righe del lotto sono esattamente quelle 807-1291',
   seg == {u['line'] for u in tu} and len(seg) == 12, (sorted(seg - {u['line'] for u in tu}), len(seg)))
overlap = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    if os.path.basename(os.path.dirname(f)) == os.path.basename(HERE):
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH and 807 <= u['line'] <= 1291:
            overlap.append((os.path.basename(os.path.dirname(f)), u['line']))
ck('nessun altro lotto rivendica le righe 807-1291', not overlap, overlap)
ck('copertura: 12 righe nel segmento; totale del file stampato e non supera 38',
   len(seg) == 12 and len(righe) <= 38, '%d/38 al momento' % len(righe))
ck('TERZINA `Peregrine` con tab sulla seconda e sulla terza',
   [u['line'] for u in tu if u['context'] == 'ship:Peregrine'] == TERZINA
   and at[1290]['english'].startswith(TAB) and at[1291]['english'].startswith(TAB)
   and at[1290]['italian'].startswith(TAB) and at[1291]['italian'].startswith(TAB))
ck('le tre coppie interne hanno lo stesso contesto e la tab sulla seconda',
   all(at[b]['context'] == at[a]['context'] and at[b]['english'].startswith(TAB) for a, b in COPPIE))
ck('TAB: sei in tutto, righe dichiarate, primo carattere in italiano',
   sorted(u['line'] for u in tu if u['english'].startswith(TAB)) == TABBED
   and sum(u['italian'].count(TAB) for u in tu) == 6)
ck('CONTINUITA `Heron`: 806 (L301) prima unita, 807 (qui) seconda',
   prev[806]['context'] == 'ship:Heron' and at[807]['context'] == 'ship:Heron'
   and at[807]['english'].startswith(TAB) and not prev[806]['english'].startswith(TAB))
ck('FAMIGLIA dell occultamento: le tre qui sono identiche a quella di L301 a meno del nome',
   all(at[l]['italian'].replace(n, 'X') == prev[549]['italian'].replace('Gull', 'X') for l, n in CLOAK.items()),
   [(l, at[l]['italian'][:50]) for l, n in CLOAK.items()
    if at[l]['italian'].replace(n, 'X') != prev[549]['italian'].replace('Gull', 'X')])
ck('VALUE copiato: `Ibises`', by[2]['italian'] == 'Ibises' == by[2]['english'])
ck('le 11 DESCRIPTION sono tradotte', all(u['italian'] != u['english'] for u in tu if u['kind'] == 'DESCRIPTION'))
ck('ASSERZIONI VUOTE: 0 virgolette, 0 segnaposto, 0 alternative',
   sum(u['english'].count(QUOTE) for u in tu) == 0 == sum(u['italian'].count(QUOTE) for u in tu)
   and sum(len(TAG.findall(u['italian'])) for u in tu) == 0
   and sum(len(ALT.findall(u['italian'])) for u in tu) == 0)
ck('apici: 6 in inglese, 15 in italiano',
   sum(u['english'].count(APOS) for u in tu) == 6 and sum(u['italian'].count(APOS) for u in tu) == 15,
   (sum(u['english'].count(APOS) for u in tu), sum(u['italian'].count(APOS) for u in tu)))
ck('lessico: «mordi e fuggi», «spiriti del vuoto», «prefetto», `Ember Waste` invariato',
   'mordi e fuggi' in at[981]['italian'] and 'spiriti del vuoto' in at[1201]['italian']
   and 'prefetto' in at[807]['italian'] and 'Ember Waste' in at[1072]['italian']
   and 'mordi-e-fuggi' not in ''.join(u['italian'] for u in tu))
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
ck('tutte le 12 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in tu))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('SEGMENTO: 12 prima · 12 qui · 14 dopo la 1291 · terzina + 3 coppie + 2 singole · file %d/38' % len(righe))
print('parole EN %d -> IT %d · ratio %.2f - %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(u['ratio'] for u in tu), max(u['ratio'] for u in tu)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L302 superato' if not fail else 'verify L302 fallito')
raise SystemExit(0 if not fail else 1)
