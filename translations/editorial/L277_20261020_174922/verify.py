r"""verify.py — L277 (`data/korath/korath ships.txt`, righe 2010-2363). **LOTTO TERMINALE: chiude il file.**

Verifica da sola: riga grezza, campi del DB, il **segmento** (43 prima, 7 qui, **0 dopo** la 2363) e l'**invariante di FILE**
(50 unità, righe distinte, ultima riga 2363, somma dei cinque lotti), i **sette contesti `Model`** con le righe, e che **nessun
altro lotto** rivendichi queste righe.

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
PATH = 'data/korath/korath ships.txt'
CTX = ['Model 8', 'Model 16', 'Model 32', 'Model 64', 'Model 128', 'Model 256', 'Model 512']
src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
su = sorted(src['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
raw_lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
by = {u['idx']: u for u in tu}
fail = []


def ck(n, c, d=''):
    print('%-96s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente (7/7)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = [u['idx'] for u in su
       if db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
       != (u['english'], u['kind'], u['path'], u['context'])]
ck('english/kind/path/context identici al DB', not bad, bad)
ck('7 unita, righe 2010-2363, tutte DESCRIPTION',
   len(tu) == 7 and [u['line'] for u in tu] == [2010, 2065, 2121, 2179, 2238, 2299, 2363]
   and {u['kind'] for u in tu} == {'DESCRIPTION'}, (len(tu), {u['kind'] for u in tu}))
ck('i sette contesti `Model` compaiono in quest ordine, senza altri',
   [c.replace('ship:', '', 1) for c in dict.fromkeys(u['context'] for u in tu)] == CTX,
   [c for c in dict.fromkeys(u['context'] for u in tu)])
ck("43 unita' prima (L273-L276)",
   db.execute('select count(*) from units where path=? and line<2010', (PATH,)).fetchone()[0] == 43)
ck("ZERO unita' dopo la 2363: il lotto CHIUDE il file",
   db.execute('select count(*) from units where path=? and line>2363', (PATH,)).fetchone()[0] == 0)
ck('INVARIANTE DI FILE: il database ha 50 unita, righe 95-2363, ultima alla 2363',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (50, 95, 2363))
per_lotto, righe = [], set()
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    us = [u for u in json.load(open(f, encoding='utf-8'))['units'] if u['path'] == PATH]
    if us:
        per_lotto.append((os.path.basename(os.path.dirname(f)), len(us)))
        righe |= {u['line'] for u in us}
seg = {l for l in righe if 2010 <= l <= 2363}
ck('SEGMENTO: le 7 righe del lotto sono esattamente quelle 2010-2363',
   seg == {u['line'] for u in tu} and len(seg) == 7, (sorted(seg - {u['line'] for u in tu}), len(seg)))
ck('INVARIANTE DI FILE: cinque lotti, somma 50, righe distinte 50, nessuna riga fuori',
   sum(n for _, n in per_lotto) == 50 and len(righe) == 50 and min(righe) == 95 and max(righe) == 2363,
   (sum(n for _, n in per_lotto), len(righe)))
ck('COPERTURA: 50/50 righe del file (100%)', len(righe) == 50, '%d/50' % len(righe))
overlap = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    if os.path.basename(os.path.dirname(f)) == os.path.basename(HERE):
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH and 2010 <= u['line'] <= 2363:
            overlap.append((os.path.basename(os.path.dirname(f)), u['line']))
ck('nessun altro lotto rivendica le righe 2010-2363', not overlap, overlap)
ck('tutte tradotte, nessuna copiata',
   not [u['idx'] for u in tu if u['italian'] == u['english']],
   [u['idx'] for u in tu if u['italian'] == u['english']])
ck('zero tab, zero virgolette, zero apici inglesi, zero segnaposto',
   sum(u['english'].count(TAB) + u['italian'].count(TAB) for u in tu) == 0
   and sum(u['english'].count(QUOTE) + u['italian'].count(QUOTE) for u in tu) == 0
   and sum(u['english'].count(APOS) for u in tu) == 0
   and not [t for u in tu for t in TAG.findall(u['english']) + TAG.findall(u['italian'])])
ck('apici italiani: 4, uno per unita (1, 3, 6, 7)',
   sum(u['italian'].count(APOS) for u in tu) == 4
   and sorted(u['idx'] for u in tu if APOS in u['italian']) == [1, 3, 6, 7])
ck('i nomi numerati restano e la serie racconta una crescita',
   'estrazione mineraria' in by[1]['italian'] and 'modulare' in by[2]['italian']
   and 'fregata' in by[4]['italian'] and 'anello perfetto' in by[7]['italian'])
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in tu for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90 per ogni unita',
   all(0.55 < u['ratio'] < 1.90 for u in tu),
   [(u['idx'], u['ratio']) for u in tu if not 0.55 < u['ratio'] < 1.90])
ck('tutte le 7 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in tu))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('SEGMENTO: 43 prima · 7 qui · 0 dopo (FINE FILE) · 7 contesti')
print('parole EN %d -> IT %d · ratio %.2f - %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(u['ratio'] for u in tu), max(u['ratio'] for u in tu)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L277 superato' if not fail else 'verify L277 fallito')
raise SystemExit(0 if not fail else 1)
