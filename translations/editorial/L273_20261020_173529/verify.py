r"""verify.py — L273 (`data/korath/korath ships.txt`, righe 95-360). **Primo lotto del file**.

Verifica da sola: riga grezza, campi del DB, il **segmento** (0 prima — apre il file — 8 qui, **42** dopo la 360), i **quattro
contesti** con le righe, i **quattro tab**, i nomi Korath con apostrofo, e che **nessun altro lotto** rivendichi queste righe.

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
CTX = ["Rano'erek", 'Palavret', 'Tubfalet', "'nra'ret"]
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


ck('riga grezza identica al sorgente (8/8)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = [u['idx'] for u in su
       if db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
       != (u['english'], u['kind'], u['path'], u['context'])]
ck('english/kind/path/context identici al DB', not bad, bad)
ck('8 unita, righe 95-360, tutte DESCRIPTION',
   len(tu) == 8 and [u['line'] for u in tu] == sorted({u['line'] for u in tu})
   and {u['kind'] for u in tu} == {'DESCRIPTION'}, (len(tu), {u['kind'] for u in tu}))
ck('i quattro contesti compaiono in quest ordine, senza altri',
   [c.replace('ship:', '', 1) for c in dict.fromkeys(u['context'] for u in tu)] == CTX,
   [c for c in dict.fromkeys(u['context'] for u in tu)])
ck("ZERO unita' prima della 95: il lotto APRE il file",
   db.execute('select count(*) from units where path=? and line<95', (PATH,)).fetchone()[0] == 0)
ck("42 unita' dopo la 360",
   db.execute('select count(*) from units where path=? and line>360', (PATH,)).fetchone()[0] == 42)
ck('confine: la 364 apre `olofez`',
   db.execute('select line,context from units where path=? and line>360 order by line limit 1', (PATH,)).fetchone()
   == (364, "ship:'olofez"))
ck('il file ha 50 unita, righe 95-2363',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (50, 95, 2363))
per_lotto, righe = [], set()
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    us = [u for u in json.load(open(f, encoding='utf-8'))['units'] if u['path'] == PATH]
    if us:
        per_lotto.append((os.path.basename(os.path.dirname(f)), len(us)))
        righe |= {u['line'] for u in us}
seg = {l for l in righe if 95 <= l <= 360}
ck('SEGMENTO: le 8 righe del lotto sono esattamente quelle 95-360',
   seg == {u['line'] for u in tu} and len(seg) == 8, (sorted(seg - {u['line'] for u in tu}), len(seg)))
overlap = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    if os.path.basename(os.path.dirname(f)) == os.path.basename(HERE):
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH and 95 <= u['line'] <= 360:
            overlap.append((os.path.basename(os.path.dirname(f)), u['line']))
ck('nessun altro lotto rivendica le righe 95-360', not overlap, overlap)
ck('copertura del SEGMENTO: 8/8 righe; il totale del file e stampato, non asserito',
   len(seg) == 8 and 50 - len(seg) == 42, '%d/50 (file)' % len(righe))
ck('tutte tradotte, nessuna copiata',
   not [u['idx'] for u in tu if u['italian'] == u['english']],
   [u['idx'] for u in tu if u['italian'] == u['english']])
ck('TAB: quattro, sulle unita pari, primi caratteri in entrambe le lingue',
   sum(u['english'].count(TAB) for u in tu) == 4 == sum(u['italian'].count(TAB) for u in tu)
   and [u['idx'] for u in tu if TAB in u['italian']] == [2, 4, 6, 8]
   and all(u['italian'].startswith(TAB) for u in tu if TAB in u['italian']))
ck('nomi Korath con apostrofo invariati dove l inglese li nomina',
   not [(u['idx'], n) for u in tu for n in ("Rano'erek", 'Palavret', 'Tubfalet', "nra'ret", 'olofez',
                                            "Ik'atilajej", "Korsmanath A'awoj")
        if n in u['english'] and n not in u['italian']])
ck('zero virgolette e zero segnaposto',
   sum(u['english'].count(QUOTE) + u['italian'].count(QUOTE) for u in tu) == 0
   and not [t for u in tu for t in TAG.findall(u['english']) + TAG.findall(u['italian'])])
ck('apici: 9 in inglese, 15 in italiano',
   sum(u['english'].count(APOS) for u in tu) == 9 and sum(u['italian'].count(APOS) for u in tu) == 15,
   (sum(u['english'].count(APOS) for u in tu), sum(u['italian'].count(APOS) for u in tu)))
ck('lessico: Esiliati, razziatori, navi-mondo, nave da razzia, cacciatore',
   'Esiliati' in by[7]['italian'] and 'razziatori' in by[1]['italian']
   and 'navi-mondo' in by[1]['italian'] and 'nave da razzia' in by[3]['italian'])
ck('armamento: lanciamissili, mitraglia, Lance di fuoco',
   'lanciamissili' in by[8]['italian'] and 'mitraglia' in by[8]['italian']
   and 'Lance di fuoco' in by[8]['italian'])
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in tu for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90 per ogni unita',
   all(0.55 < u['ratio'] < 1.90 for u in tu),
   [(u['idx'], u['ratio']) for u in tu if not 0.55 < u['ratio'] < 1.90])
ck('tutte le 8 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in tu))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('SEGMENTO: 0 prima (apre il file) · 8 qui · 42 dopo · 4 contesti · 4 tab')
print('parole EN %d -> IT %d · ratio %.2f - %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(u['ratio'] for u in tu), max(u['ratio'] for u in tu)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L273 superato' if not fail else 'verify L273 fallito')
raise SystemExit(0 if not fail else 1)
