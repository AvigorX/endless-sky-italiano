r"""verify.py — L289 (`data/gegno/gegno ships.txt`, righe 1193-1616). **LOTTO TERMINALE**.

Verifica da sola, e verifica il **FILE INTERO**: 37 unita', **somma dei lotti 7 + 9 + 9 + 12 = 37**, **righe distinte**,
**ultima riga 1616**, **zero unita' dopo**. Poi il lotto: riga grezza, campi del DB, **otto contesti**, **quattro coppie**,
la **continuita' del `Halite`** con L288, i **cinque tab**, l'**istruzione di gioco in seconda persona** come unica eccezione al
registro impersonale, le **asserzioni vuote**, e che **nessun altro lotto** rivendichi le righe 1193-1616.

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
PATH = 'data/gegno/gegno ships.txt'
NAMES = ['Halite', 'Mica', 'Coesite', 'Tridymite', 'Felsic', 'Feldspar', 'Epidote', 'Kyanite', 'Gegno', 'Scin', 'Vi']
PAIRS = [(1193, 1194), (1480, 1481), (1547, 1548), (1615, 1616)]
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
ck('12 unita, righe distinte, tutte DESCRIPTION, otto contesti',
   len(tu) == 12 and len({u['line'] for u in tu}) == 12 and {u['kind'] for u in tu} == {'DESCRIPTION'}
   and len({u['context'] for u in tu}) == 8)
ck("25 unita' prima della 1193 (7 + 9 + 9)",
   db.execute('select count(*) from units where path=? and line<1193', (PATH,)).fetchone()[0] == 25)
ck("ZERO unita' dopo la 1616: il lotto CHIUDE il file",
   db.execute('select count(*) from units where path=? and line>1616', (PATH,)).fetchone()[0] == 0)
righe, lotti = set(), []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    us = [u for u in json.load(open(f, encoding='utf-8'))['units'] if u['path'] == PATH]
    if us:
        lotti.append((os.path.basename(os.path.dirname(f)), len(us)))
        righe |= {u['line'] for u in us}
ck('FILE: i quattro lotti del file sommano 37 unita (7 + 9 + 9 + 12)',
   [n for _, n in lotti] == [7, 9, 9, 12] and sum(n for _, n in lotti) == 37 == len(righe),
   (lotti, len(righe)))
ck('FILE: 37 unita, 37 righe distinte, prima 53, ultima 1616',
   len(righe) == 37 and min(righe) == 53 and max(righe) == 1616
   and db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (37, 53, 1616))
ck('FILE: copertura 37/37 (100%)',
   len(righe) == db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0],
   '%d/37' % len(righe))
overlap = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    if os.path.basename(os.path.dirname(f)) == os.path.basename(HERE):
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH and 1193 <= u['line'] <= 1616:
            overlap.append((os.path.basename(os.path.dirname(f)), u['line']))
ck('nessun altro lotto rivendica le righe 1193-1616', not overlap, overlap)
ck('quattro coppie consecutive, stesso contesto',
   all(b == a + 1 and at[a]['context'] == at[b]['context'] for a, b in PAIRS),
   [(a, b) for a, b in PAIRS if not (b == a + 1 and at[a]['context'] == at[b]['context'])])
ck('continuita cross-lot: L288 chiude il Halite con «nuovi sviluppi.», L289 riprende con «Capaci»',
   at[1193]['italian'].lstrip(TAB).startswith('Capaci'))
prev = sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L288_*', 'translation.json')))
p1192 = [u for u in json.load(open(prev[-1], encoding='utf-8'))['units'] if u['path'] == PATH and u['line'] == 1192] if prev else []
ck('L288 ha la riga 1192 e la chiude con «nuovi sviluppi.»',
   len(p1192) == 1 and p1192[0]['italian'].endswith('nuovi sviluppi.'),
   p1192[0]['italian'][-40:] if p1192 else 'L288 assente')
ck('tab: cinque, righe 1193, 1194, 1481, 1548, 1616, primo carattere',
   sum(u['english'].count(TAB) for u in tu) == 5 == sum(u['italian'].count(TAB) for u in tu)
   and sorted(l for l in at if at[l]['italian'].startswith(TAB)) == [1193, 1194, 1481, 1548, 1616])
ck('asserzioni vuote: 0 virgolette, 0 segnaposto, 0 alternative',
   sum(u['english'].count(QUOTE) for u in tu) == 0 == sum(u['italian'].count(QUOTE) for u in tu)
   and sum(len(TAG.findall(u['english'])) for u in tu) == 0 == sum(len(TAG.findall(u['italian'])) for u in tu)
   and sum(len(ALT.findall(u['english'])) for u in tu) == 0 == sum(len(ALT.findall(u['italian'])) for u in tu))
ck('apici: 4 in inglese, 5 in italiano',
   sum(u['english'].count(APOS) for u in tu) == 4 and sum(u['italian'].count(APOS) for u in tu) == 5,
   (sum(u['english'].count(APOS) for u in tu), sum(u['italian'].count(APOS) for u in tu)))
ck('registro: la seconda persona compare SOLO nell istruzione di gioco (riga 1194)',
   [u['line'] for u in tu if re.search(r'\b(tu|tuo|tua|tuoi|tue|ti|te|puoi)\b', u['italian'])] == [1194]
   and 'Non puoi trasportare' in at[1194]['italian'])
ck('nomi di modello e di fazione invariati, nessun plurale inglese riprodotto',
   all(n in ''.join(u['italian'] for u in tu) for n in NAMES)
   and not [p for p in ('Halites', 'Coesites', 'Kyanites', 'Feldspars', 'Epidotes', 'Tridymites', 'Felsics')
            if p in ''.join(u['italian'] for u in tu)])
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
print('FILE: 37/37 (100%) · somma lotti 7+9+9+12 · prima riga 53 · ultima 1616 · zero dopo')
print('parole EN %d -> IT %d · ratio %.2f - %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(u['ratio'] for u in tu), max(u['ratio'] for u in tu)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L289 superato' if not fail else 'verify L289 fallito')
raise SystemExit(0 if not fail else 1)
