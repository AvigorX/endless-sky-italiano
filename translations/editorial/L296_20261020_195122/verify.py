r"""verify.py — L296 (`data/human/marauders.txt`, righe 884-1146). **LOTTO TERMINALE**.

Verifica da sola, e verifica il **FILE INTERO**: 29 unita', **somma dei lotti 12 + 9 + 8 = 29**, **righe distinte**, **prima riga
62**, **ultima 1146**, **zero unita' dopo**. Poi il lotto: riga grezza, campi del DB, **le unita' 1 e 2 identiche**, i **tre
motivi delle serie**, la **seconda persona in tre unita'** (3, 5, 7), le asserzioni vuote, e che **nessun altro lotto**
rivendichi le righe 884-1146.

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
SERIES = {'ship:Marauder Quicksilver': [884, 910], 'ship:Marauder Raven': [968, 996, 1026],
          'ship:Marauder Splinter': [1083, 1114, 1146]}
NAMES = ['Quicksilver', 'Raven', 'Splinter', 'Megaparsec', 'Lionheart', 'Headhunter']
TU = [3, 5, 7]
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


ck('riga grezza identica al sorgente (8/8)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = [u['idx'] for u in su
       if db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
       != (u['english'], u['kind'], u['path'], u['context'])]
ck('english/kind/path/context identici al DB', not bad, bad)
ck('8 unita, righe tutte quelle dichiarate, tutte DESCRIPTION',
   len(tu) == 8 and {u['line'] for u in tu} == {l for ls in SERIES.values() for l in ls}
   and {u['kind'] for u in tu} == {'DESCRIPTION'})
ck('tre contesti con le righe dichiarate (2 + 3 + 3)',
   {(u['context'], u['line']) for u in tu} == {(c, l) for c, ls in SERIES.items() for l in ls}
   and {c: sum(1 for u in tu if u['context'] == c) for c in SERIES} == {c: len(ls) for c, ls in SERIES.items()})
ck("21 unita' prima della 884 (12 + 9)",
   db.execute('select count(*) from units where path=? and line<884', (PATH,)).fetchone()[0] == 21)
ck("ZERO unita' dopo la 1146: il lotto CHIUDE il file",
   db.execute('select count(*) from units where path=? and line>1146', (PATH,)).fetchone()[0] == 0)
righe, lotti = set(), []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    us = [u for u in json.load(open(f, encoding='utf-8'))['units'] if u['path'] == PATH]
    if us:
        lotti.append((os.path.basename(os.path.dirname(f)), len(us)))
        righe |= {u['line'] for u in us}
ck('FILE: i tre lotti sommano 29 unita (12 + 9 + 8)',
   [n for _, n in lotti] == [12, 9, 8] and sum(n for _, n in lotti) == 29 == len(righe),
   (lotti, len(righe)))
ck('FILE: 29 unita, 29 righe distinte, prima 62, ultima 1146',
   len(righe) == 29 and min(righe) == 62 and max(righe) == 1146
   and db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (29, 62, 1146))
ck('FILE: copertura 29/29 (100%)',
   len(righe) == db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0], '%d/29' % len(righe))
overlap = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    if os.path.basename(os.path.dirname(f)) == os.path.basename(HERE):
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH and 884 <= u['line'] <= 1146:
            overlap.append((os.path.basename(os.path.dirname(f)), u['line']))
ck('nessun altro lotto rivendica le righe 884-1146', not overlap, overlap)
ck('tutte e 8 le unita sono tradotte', all(u['italian'] != u['english'] for u in tu))
ck('ripetizione: 884 e 910 identiche in inglese e in italiano',
   at[884]['english'] == at[910]['english'] and at[884]['italian'] == at[910]['italian'])
ck('`Raven`: tutte e tre le varianti parlano delle ali',
   sum(1 for l in (968, 996, 1026) if 'ali' in at[l]['italian']) == 3)
ck('`Splinter`: tutte e tre parlano di sezioni dello scafo',
   sum(1 for l in (1083, 1114, 1146) if 'sezioni dello scafo' in at[l]['italian']) == 3)
ck('asserzioni vuote: 0 tab, 0 virgolette, 0 segnaposto, 0 alternative',
   sum(u['english'].count(TAB) for u in tu) == 0 == sum(u['italian'].count(TAB) for u in tu)
   and sum(u['english'].count(QUOTE) for u in tu) == 0 == sum(u['italian'].count(QUOTE) for u in tu)
   and sum(len(TAG.findall(u['italian'])) for u in tu) == 0
   and sum(len(ALT.findall(u['italian'])) for u in tu) == 0)
ck('apici: 10 in inglese, 10 in italiano',
   sum(u['english'].count(APOS) for u in tu) == 10 and sum(u['italian'].count(APOS) for u in tu) == 10,
   (sum(u['english'].count(APOS) for u in tu), sum(u['italian'].count(APOS) for u in tu)))
ck('registro: la seconda persona compare solo nelle unita 3, 5 e 7',
   [i for i, u in sorted(by.items()) if re.search(r'\b(tu|tuo|tua|tuoi|tue|ti|te|possa|trovi)\b', u['italian'])] == TU,
   [i for i, u in sorted(by.items()) if re.search(r'\b(tu|tuo|tua|tuoi|tue|ti|te|possa|trovi)\b', u['italian'])])
ck('nomi e cantieri invariati', all(n in ''.join(u['italian'] for u in tu) for n in NAMES),
   [n for n in NAMES if n not in ''.join(u['italian'] for u in tu)])
ck('terminologia: porti per cannoni, punti di attacco, paratie, baie motore, porto motore',
   'porti per cannoni' in at[884]['italian'] and 'punti di attacco' in at[1146]['italian']
   and 'paratie' in at[968]['italian'] and 'baie motore' in at[996]['italian']
   and 'porto motore' in at[1114]['italian'])
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in tu for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90',
   all(0.55 < u['ratio'] < 1.90 for u in tu),
   [(u['idx'], u['ratio']) for u in tu if not 0.55 < u['ratio'] < 1.90])
ck('tutte le 8 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in tu))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('FILE: 29/29 (100%) · somma lotti 12+9+8 · prima riga 62 · ultima 1146 · zero dopo')
print('parole EN %d -> IT %d · ratio %.2f - %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(u['ratio'] for u in tu), max(u['ratio'] for u in tu)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L296 superato' if not fail else 'verify L296 fallito')
raise SystemExit(0 if not fail else 1)
