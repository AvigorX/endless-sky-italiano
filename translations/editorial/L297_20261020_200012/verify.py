r"""verify.py — L297 (`data/coalition/coalition outfits.txt`, righe 26-187). **PRIMO lotto del file**.

Verifica da sola: riga grezza, campi del DB, il **segmento** (**0** prima, **15** qui, **34** dopo la 187), le **tre coppie con
tab** (55, 70, 85), le **nove unita' singole**, la **citazione interna** del modulo, le **asserzioni vuote**, il **registro**, e
che **nessun altro lotto** rivendichi le righe 26-187.

Indipendente da `check.py`: rilegge `source.json`, il `translation.json`, il database, il file del gioco e **tutti** i
`translation.json` dello staging. La copertura del **FILE** e' **stampata, non asserita** (il file si chiudera' in lotti
successivi).
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
SINGOLE = [26, 40, 99, 112, 125, 141, 156, 172, 187]
NAMES = ['Heliarch', 'Kimek', 'Quarg', 'Arach', 'Coalizione']
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


ck('riga grezza identica al sorgente (15/15)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = [u['idx'] for u in su
       if db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
       != (u['english'], u['kind'], u['path'], u['context'])]
ck('english/kind/path/context identici al DB', not bad, bad)
ck('15 unita, tutte DESCRIPTION, dodici contesti',
   len(tu) == 15 and {u['kind'] for u in tu} == {'DESCRIPTION'} and len({u['context'] for u in tu}) == 12)
ck("ZERO unita' prima della 26 (il lotto apre il file) e 34 dopo la 187",
   db.execute('select count(*) from units where path=? and line<26', (PATH,)).fetchone()[0] == 0
   and db.execute('select count(*) from units where path=? and line>187', (PATH,)).fetchone()[0] == 34)
ck('la prima unita dopo la 187 e `Large Repair Module` alla 202',
   db.execute('select line,context from units where path=? and line>187 order by line limit 1', (PATH,)).fetchone()
   == (202, 'outfit:Large Repair Module'))
ck('il file ha 49 unita, righe 26-533',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (49, 26, 533))
righe = set()
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH:
            righe.add(u['line'])
seg = {l for l in righe if 26 <= l <= 187}
ck('SEGMENTO: le 15 righe del lotto sono esattamente quelle 26-187',
   seg == {u['line'] for u in tu} and len(seg) == 15, (sorted(seg - {u['line'] for u in tu}), len(seg)))
overlap = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    if os.path.basename(os.path.dirname(f)) == os.path.basename(HERE):
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH and 26 <= u['line'] <= 187:
            overlap.append((os.path.basename(os.path.dirname(f)), u['line']))
ck('nessun altro lotto rivendica le righe 26-187', not overlap, overlap)
ck('copertura: 15 righe nel segmento; totale del file stampato e non supera 49',
   len(seg) == 15 and len(righe) <= 49, '%d/49 al momento' % len(righe))
ck('tutte e 15 le unita sono tradotte', all(u['italian'] != u['english'] for u in tu))
ck('TAB: tre unita la iniziano, righe 55, 70, 85, conservata come primo carattere',
   sorted(u['line'] for u in tu if u['english'].startswith(TAB)) == [55, 70, 85]
   and all(u['italian'].startswith(TAB) for u in tu if u['english'].startswith(TAB))
   and sum(u['italian'].count(TAB) for u in tu) == 3)
ck('COPPIE: ogni unita con tab ha il compagno dello stesso contesto alla riga precedente',
   all(at[i]['context'] == at[i - 1]['context'] for i in (55, 70, 85)))
ck('le nove unita singole sono quelle dichiarate',
   [u['line'] for u in tu if collections.Counter(x['context'] for x in tu)[u['context']] == 1] == SINGOLE)
ck('ASSERZIONI VUOTE: 0 virgolette, 0 segnaposto, 0 alternative',
   sum(u['english'].count(QUOTE) for u in tu) == 0 == sum(u['italian'].count(QUOTE) for u in tu)
   and sum(len(TAG.findall(u['italian'])) for u in tu) == 0
   and sum(len(ALT.findall(u['italian'])) for u in tu) == 0)
ck('apici: 1 in inglese, 9 in italiano',
   sum(u['english'].count(APOS) for u in tu) == 1 and sum(u['italian'].count(APOS) for u in tu) == 9,
   (sum(u['english'].count(APOS) for u in tu), sum(u['italian'].count(APOS) for u in tu)))
ck('nomi invariati e `Coalition` reso «Coalizione»',
   all(n in ''.join(u['italian'] for u in tu) for n in NAMES)
   and 'Coalition' not in ''.join(u['italian'] for u in tu),
   [n for n in NAMES if n not in ''.join(u['italian'] for u in tu)])
ck('citazione interna: la 14 nomina il modulo della 13, che non nomina se stesso',
   at[156]['context'] == 'outfit:Large Shield Module'
   and 'Large Shield Module' in at[172]['italian'] and 'Large Shield Module' not in at[156]['italian'])
ck('registro: nessuna seconda persona',
   not [u['idx'] for u in tu if re.search(r'\b(tu|tuo|tua|tuoi|tue|ti|te)\b', u['italian'])])
ck('lessico del corpus: marina mercantile, pannelli solari, torri della fame, cella a combustibile',
   'marina mercantile' in at[26]['italian'] and 'pannelli solari' in at[125]['italian']
   and 'torri della fame' in at[84]['italian'] and 'cella a combustibile' in at[85]['italian'])
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in tu for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessun doppio spazio',
   not [u['idx'] for u in tu if '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90',
   all(0.55 < u['ratio'] < 1.90 for u in tu),
   [(u['idx'], u['ratio']) for u in tu if not 0.55 < u['ratio'] < 1.90])
ck('tutte le 15 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in tu))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('SEGMENTO: 0 prima · 15 qui · 34 dopo la 187 · 12 contesti · 3 coppie con tab · file %d/49' % len(righe))
print('parole EN %d -> IT %d · ratio %.2f - %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(u['ratio'] for u in tu), max(u['ratio'] for u in tu)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L297 superato' if not fail else 'verify L297 fallito')
raise SystemExit(0 if not fail else 1)
