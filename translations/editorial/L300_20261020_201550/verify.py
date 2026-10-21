r"""verify.py — L300 (`data/coalition/coalition outfits.txt`, righe 516-533). **LOTTO TERMINALE**.

Verifica da sola, e verifica il **FILE INTERO**: 49 unita', **somma dei lotti 15 + 15 + 14 + 5 = 49**, **righe distinte**,
**prima riga 26**, **ultima 533**, **zero unita' dopo**. Poi il lotto: riga grezza, campi del DB, **due coppie con tab**, la
**singola**, la **seconda persona narrativa** in una sola unita', i **nomi degli atti di legge**, e che **nessun altro lotto**
rivendichi le righe 516-533.

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
PATH = 'data/coalition/coalition outfits.txt'
PAIRS = [(516, 517), (532, 533)]
TABBED = [517, 533]
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


ck('riga grezza identica al sorgente (5/5)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = [u['idx'] for u in su
       if db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
       != (u['english'], u['kind'], u['path'], u['context'])]
ck('english/kind/path/context identici al DB', not bad, bad)
ck('5 unita, tutte DESCRIPTION, tre contesti (due doppi + una singola)',
   len(tu) == 5 and {u['kind'] for u in tu} == {'DESCRIPTION'}
   and sorted(collections.Counter(u['context'] for u in tu).values()) == [1, 2, 2])
ck("44 unita' prima della 516 (15 + 15 + 14)",
   db.execute('select count(*) from units where path=? and line<516', (PATH,)).fetchone()[0] == 44)
ck("ZERO unita' dopo la 533: il lotto CHIUDE il file",
   db.execute('select count(*) from units where path=? and line>533', (PATH,)).fetchone()[0] == 0)
righe, lotti = set(), []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    us = [u for u in json.load(open(f, encoding='utf-8'))['units'] if u['path'] == PATH]
    if us:
        lotti.append((os.path.basename(os.path.dirname(f)), len(us)))
        righe |= {u['line'] for u in us}
ck('FILE: i quattro lotti sommano 49 unita (15 + 15 + 14 + 5)',
   [n for _, n in lotti] == [15, 15, 14, 5] and sum(n for _, n in lotti) == 49 == len(righe),
   (lotti, len(righe)))
ck('FILE: 49 unita, 49 righe distinte, prima 26, ultima 533',
   len(righe) == 49 and min(righe) == 26 and max(righe) == 533
   and db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (49, 26, 533))
ck('FILE: copertura 49/49 (100%)',
   len(righe) == db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0], '%d/49' % len(righe))
overlap = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    if os.path.basename(os.path.dirname(f)) == os.path.basename(HERE):
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH and 516 <= u['line'] <= 533:
            overlap.append((os.path.basename(os.path.dirname(f)), u['line']))
ck('nessun altro lotto rivendica le righe 516-533', not overlap, overlap)
ck('tutte e 5 le unita sono tradotte', all(u['italian'] != u['english'] for u in tu))
ck('TAB: due unita (517, 533), primo carattere conservato',
   sorted(u['line'] for u in tu if u['english'].startswith(TAB)) == TABBED
   and all(at[l]['italian'].startswith(TAB) for l in TABBED)
   and sum(u['italian'].count(TAB) for u in tu) == 2)
ck('le due coppie hanno lo stesso contesto e la tab sulla seconda',
   all(at[b]['context'] == at[a]['context'] and at[b]['english'].startswith(TAB) for a, b in PAIRS))
ck('asserzioni vuote: 0 virgolette, 0 segnaposto, 0 alternative',
   sum(u['english'].count(QUOTE) for u in tu) == 0 == sum(u['italian'].count(QUOTE) for u in tu)
   and sum(len(TAG.findall(u['italian'])) for u in tu) == 0
   and sum(len(ALT.findall(u['italian'])) for u in tu) == 0)
ck('apici: 2 in inglese, 5 in italiano',
   sum(u['english'].count(APOS) for u in tu) == 2 and sum(u['italian'].count(APOS) for u in tu) == 5,
   (sum(u['english'].count(APOS) for u in tu), sum(u['italian'].count(APOS) for u in tu)))
ck('seconda persona NARRATIVA solo nella 532 («un libro che ti ha regalato»)',
   [u['idx'] for u in tu if re.search(r'\b(tu|tuo|tua|tuoi|tue|ti|te)\b', u['italian'])] == [4])
ck('atti di legge resi in italiano; `Rectification` e `Civil Goods` non restano in inglese',
   'Guerra d\'Indipendenza' in at[517]['italian']
   and 'Nona Rettifica su Commercio e Traffico' in at[517]['italian']
   and 'Legge sui Beni e sulle Tariffe Civili' in at[517]['italian']
   and 'Rectification' not in ''.join(u['italian'] for u in tu)
   and 'Civil Goods' not in ''.join(u['italian'] for u in tu))
ck('lessico: motore di salto, ipervie, copia autografata',
   'motore di salto' in at[533]['italian'] and 'ipervie' in at[533]['italian']
   and 'autografata' in at[532]['italian'])
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in tu for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessun doppio spazio (la tab iniziale non conta)',
   not [u['idx'] for u in tu if '  ' in u['italian'].lstrip(TAB)])
ck('rapporto nel gate 0,55-1,90',
   all(0.55 < u['ratio'] < 1.90 for u in tu),
   [(u['idx'], u['ratio']) for u in tu if not 0.55 < u['ratio'] < 1.90])
ck('tutte le 5 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in tu))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('FILE: 49/49 (100%) · somma lotti 15+15+14+5 · prima riga 26 · ultima 533 · zero dopo')
print('parole EN %d -> IT %d · ratio %.2f - %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(u['ratio'] for u in tu), max(u['ratio'] for u in tu)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L300 superato' if not fail else 'verify L300 fallito')
raise SystemExit(0 if not fail else 1)
