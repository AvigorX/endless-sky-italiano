r"""verify.py — L294 (`data/human/marauders.txt`, righe 62-484). **Primo lotto del file**.

Verifica da sola: riga grezza, campi del DB, il **segmento** (0 prima — il lotto **apre** il file — 12 qui, **17** dopo la 484),
le **quattro serie da tre**, le **asserzioni vuote** (tab, virgolette, segnaposto, alternative), i **nomi invariati**, il
**registro** con le quattro unita' che si rivolgono al lettore, e che **nessun altro lotto** rivendichi le righe 62-484.

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
PATH = 'data/human/marauders.txt'
SERIES = {'ship:Marauder Arrow': [62, 84, 111], 'ship:Marauder Bounder': [166, 193, 223],
          'ship:Marauder Falcon': [288, 325, 364], 'ship:Marauder Firebird': [423, 453, 484]}
NAMES = ['Arrow', 'Bounder', 'Falcon', 'Firebird', 'Megaparsec', 'Tarazed', 'Betelgeuse', 'Headhunter', 'Lionheart',
         'Flivver']
TU = [1, 8, 9, 10]
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
ck('12 unita, righe tutte quelle dichiarate, tutte DESCRIPTION',
   len(tu) == 12 and {u['line'] for u in tu} == {l for ls in SERIES.values() for l in ls}
   and {u['kind'] for u in tu} == {'DESCRIPTION'})
ck('quattro serie da tre, contesti con le righe dichiarate',
   {(u['context'], u['line']) for u in tu} == {(c, l) for c, ls in SERIES.items() for l in ls}
   and all(sum(1 for u in tu if u['context'] == c) == 3 for c in SERIES),
   {c: sum(1 for u in tu if u['context'] == c) for c in SERIES})
ck("ZERO unita' prima della 62: il lotto APRE il file",
   db.execute('select count(*) from units where path=? and line<62', (PATH,)).fetchone()[0] == 0)
ck("17 unita' dopo la 484",
   db.execute('select count(*) from units where path=? and line>484', (PATH,)).fetchone()[0] == 17)
ck('confine: la 548 apre `Marauder Leviathan`',
   db.execute('select line,context from units where path=? and line>484 order by line limit 1', (PATH,)).fetchone()
   == (548, 'ship:Marauder Leviathan'))
ck('il file ha 29 unita, righe 62-1146',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (29, 62, 1146))
righe = set()
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH:
            righe.add(u['line'])
seg = {l for l in righe if 62 <= l <= 484}
ck('SEGMENTO: le 12 righe del lotto sono esattamente quelle 62-484',
   seg == {u['line'] for u in tu} and len(seg) == 12, (sorted(seg - {u['line'] for u in tu}), len(seg)))
overlap = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    if os.path.basename(os.path.dirname(f)) == os.path.basename(HERE):
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH and 62 <= u['line'] <= 484:
            overlap.append((os.path.basename(os.path.dirname(f)), u['line']))
ck('nessun altro lotto rivendica le righe 62-484', not overlap, overlap)
ck('copertura: 12 righe nel segmento, il totale del file e stampato e non supera 29',
   len(seg) == 12 and len(righe) <= 29, '%d/29 al momento' % len(righe))
ck('tutte e 12 le unita sono tradotte', all(u['italian'] != u['english'] for u in tu))
ck('asserzioni vuote: 0 tab, 0 virgolette, 0 segnaposto, 0 alternative',
   sum(u['english'].count(TAB) for u in tu) == 0 == sum(u['italian'].count(TAB) for u in tu)
   and sum(u['english'].count(QUOTE) for u in tu) == 0 == sum(u['italian'].count(QUOTE) for u in tu)
   and sum(len(TAG.findall(u['italian'])) for u in tu) == 0
   and sum(len(ALT.findall(u['italian'])) for u in tu) == 0)
ck('apici: 5 in inglese, 7 in italiano',
   sum(u['english'].count(APOS) for u in tu) == 5 and sum(u['italian'].count(APOS) for u in tu) == 7,
   (sum(u['english'].count(APOS) for u in tu), sum(u['italian'].count(APOS) for u in tu)))
ck('registro: la seconda persona compare solo nelle unita 1, 8, 9, 10',
   [i for i, u in sorted(by.items())
    if re.search(r'\b(tu|tuo|tua|tuoi|tue|ti|te|possiate|sospetti)\b', u['italian'])] == TU,
   [i for i, u in sorted(by.items())
    if re.search(r'\b(tu|tuo|tua|tuoi|tue|ti|te|possiate|sospetti)\b', u['italian'])])
ck('nomi di modello e di cantiere invariati',
   all(n in ''.join(u['italian'] for u in tu) for n in NAMES),
   [n for n in NAMES if n not in ''.join(u['italian'] for u in tu)])
ck('terminologia del corpus: «porto per cannoni», «corazzatura», «intercettore»',
   'porto per cannoni' in at[166]['italian'] and 'corazzatura' in at[84]['italian']
   and 'intercettori' in at[62]['italian'])
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in tu for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90',
   all(0.55 < u['ratio'] < 1.90 for u in tu),
   [(u['idx'], u['ratio']) for u in tu if not 0.55 < u['ratio'] < 1.90])
ck('tutte le 12 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in tu))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('SEGMENTO: 0 prima (apre il file) · 12 qui · 17 dopo la 484 · 4 serie da 3')
print('parole EN %d -> IT %d · ratio %.2f - %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(u['ratio'] for u in tu), max(u['ratio'] for u in tu)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L294 superato' if not fail else 'verify L294 fallito')
raise SystemExit(0 if not fail else 1)
