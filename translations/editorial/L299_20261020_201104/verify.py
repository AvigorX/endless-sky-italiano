r"""verify.py — L299 (`data/coalition/coalition outfits.txt`, righe 356-509). **Terzo lotto del file**.

Verifica da sola: riga grezza, campi del DB, il **segmento** (**30** prima, **14** qui, **5** dopo la 509), la **terzina**
`Guardian Turret` (tre unita', **due tab consecutive**), le **due coppie**, le **sette singole**, la **ripetizione 395/415**
(unita' 4 e 6 identiche in entrambe le lingue), le asserzioni vuote, la seconda persona in **due sole** unita', e che **nessun
altro lotto** rivendichi le righe 356-509.

Indipendente da `check.py`: rilegge `source.json`, il `translation.json`, il database, il file del gioco e **tutti** i
`translation.json` dello staging. La copertura del **FILE** e' **stampata, non asserita**.
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
PATH = 'data/coalition/coalition outfits.txt'
PAIRS = [(394, 395), (414, 415)]
TRIPLE = [495, 496, 497]
SINGOLE = [356, 375, 434, 453, 467, 481, 509]
TABBED = [395, 415, 496, 497]
TU = [4, 6]
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


ck('riga grezza identica al sorgente (14/14)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = [u['idx'] for u in su
       if db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
       != (u['english'], u['kind'], u['path'], u['context'])]
ck('english/kind/path/context identici al DB', not bad, bad)
grp = collections.Counter(u['context'] for u in tu)
ck('14 unita, tutte DESCRIPTION, dieci contesti (due doppi + un triplo + sette singoli)',
   len(tu) == 14 and {u['kind'] for u in tu} == {'DESCRIPTION'} and len(grp) == 10
   and sorted(grp.values()) == [1] * 7 + [2, 2, 3], dict(grp))
ck("30 unita' prima della 356 e 5 dopo la 509",
   db.execute('select count(*) from units where path=? and line<356', (PATH,)).fetchone()[0] == 30
   and db.execute('select count(*) from units where path=? and line>509', (PATH,)).fetchone()[0] == 5)
ck('la prima unita dopo la 509 e `Coalition License` alla 516',
   db.execute('select line,context from units where path=? and line>509 order by line limit 1', (PATH,)).fetchone()
   == (516, 'outfit:Coalition License'))
ck('il file ha 49 unita, righe 26-533',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (49, 26, 533))
righe = set()
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH:
            righe.add(u['line'])
seg = {l for l in righe if 356 <= l <= 509}
ck('SEGMENTO: le 14 righe del lotto sono esattamente quelle 356-509',
   seg == {u['line'] for u in tu} and len(seg) == 14, (sorted(seg - {u['line'] for u in tu}), len(seg)))
overlap = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    if os.path.basename(os.path.dirname(f)) == os.path.basename(HERE):
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH and 356 <= u['line'] <= 509:
            overlap.append((os.path.basename(os.path.dirname(f)), u['line']))
ck('nessun altro lotto rivendica le righe 356-509', not overlap, overlap)
ck('copertura: 14 righe nel segmento; totale del file stampato e non supera 49',
   len(seg) == 14 and len(righe) <= 49, '%d/49 al momento' % len(righe))
ck('tutte e 14 le unita sono tradotte', all(u['italian'] != u['english'] for u in tu))
ck('TERZINA: tre unita consecutive stesse del contesto, tab sulla seconda e sulla terza',
   [u['line'] for u in tu if u['context'] == 'outfit:Guardian Turret'] == TRIPLE
   and at[496]['english'].startswith(TAB) and at[497]['english'].startswith(TAB)
   and not at[495]['english'].startswith(TAB)
   and at[496]['italian'].startswith(TAB) and at[497]['italian'].startswith(TAB))
ck('COPPIE: stesso contesto e tab sulla seconda', all(at[b]['context'] == at[a]['context'] for a, b in PAIRS))
ck('TAB: quattro in tutto, righe dichiarate', sorted(u['line'] for u in tu if u['english'].startswith(TAB)) == TABBED
   and sum(u['italian'].count(TAB) for u in tu) == 4)
ck('le sette singole sono quelle dichiarate', [l for l, u in at.items() if grp[u['context']] == 1] == SINGOLE)
ck('RIPETIZIONE: 395 e 415 identiche in inglese e in italiano',
   at[395]['english'] == at[415]['english'] and at[395]['italian'] == at[415]['italian'])
ck('ASSERZIONI VUOTE: 0 virgolette, 0 segnaposto, 0 alternative',
   sum(u['english'].count(QUOTE) for u in tu) == 0 == sum(u['italian'].count(QUOTE) for u in tu)
   and sum(len(TAG.findall(u['italian'])) for u in tu) == 0
   and sum(len(ALT.findall(u['italian'])) for u in tu) == 0)
ck('tre punti ASCII, nessun carattere ellissi',
   '...' in at[356]['italian'] and '\u2026' not in ''.join(u['italian'] for u in tu))
ck('apici: 4 in inglese, 13 in italiano',
   sum(u['english'].count(APOS) for u in tu) == 4 and sum(u['italian'].count(APOS) for u in tu) == 13,
   (sum(u['english'].count(APOS) for u in tu), sum(u['italian'].count(APOS) for u in tu)))
ck('seconda persona solo nelle unita 4 e 6',
   [u['idx'] for u in tu if re.search(r'\b(tu|tuo|tua|tuoi|tue|ti|te)\b', u['italian'])] == TU)
ck('terminologia: propulsore di spinta inversa, mai «invertitore»',
   'propulsore di spinta inversa' in at[395]['italian']
   and 'invertitore' not in ''.join(u['italian'] for u in tu))
ck('lessico: torretta, antiabbordaggio, cecchinaggio, dissidenti, navi capitali',
   'torretta' in at[495]['italian'] and 'antiabbordaggio' in at[495]['italian']
   and 'cecchinaggio' in at[496]['italian'] and 'dissidenti' in at[481]['italian']
   and 'navi capitali' in at[453]['italian'])
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in tu for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessun doppio spazio (la tab iniziale non conta)',
   not [u['idx'] for u in tu if '  ' in u['italian'].lstrip(TAB)])
ck('rapporto nel gate 0,55-1,90',
   all(0.55 < u['ratio'] < 1.90 for u in tu),
   [(u['idx'], u['ratio']) for u in tu if not 0.55 < u['ratio'] < 1.90])
ck('tutte le 14 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in tu))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('SEGMENTO: 30 prima · 14 qui · 5 dopo la 509 · terzina + 2 coppie + 7 singole · file %d/49' % len(righe))
print('parole EN %d -> IT %d · ratio %.2f - %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(u['ratio'] for u in tu), max(u['ratio'] for u in tu)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L299 superato' if not fail else 'verify L299 fallito')
raise SystemExit(0 if not fail else 1)
