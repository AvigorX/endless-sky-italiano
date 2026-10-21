r"""verify.py — L276 (`data/korath/korath ships.txt`, righe 1375-1961). **Quarto lotto del file**.

Verifica da sola: riga grezza, campi del DB, il **segmento** (31 prima, 12 qui, **7** dopo la 1961), i **dieci contesti** con le
righe, i **due tab**, le **due virgolette**, e che **nessun altro lotto** rivendichi queste righe.

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
CTX = ['Echo-Galleon', 'Arch-Carrack', 'Charm-Shallop', 'Kar Ik Vot 349', 'Tek Far 71 - Lek',
       'Tek Far 78 - Osk', 'Tek Far 109', 'Met Par Tek 53', 'Far Lek 14', 'Far Osk 27']
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


ck('riga grezza identica al sorgente (12/12)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = [u['idx'] for u in su
       if db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
       != (u['english'], u['kind'], u['path'], u['context'])]
ck('english/kind/path/context identici al DB', not bad, bad)
ck('12 unita, righe 1375-1961, tutte DESCRIPTION',
   len(tu) == 12 and [u['line'] for u in tu] == sorted({u['line'] for u in tu})
   and {u['kind'] for u in tu} == {'DESCRIPTION'}, (len(tu), {u['kind'] for u in tu}))
ck('i dieci contesti compaiono in quest ordine, senza altri',
   [c.replace('ship:', '', 1) for c in dict.fromkeys(u['context'] for u in tu)] == CTX,
   [c for c in dict.fromkeys(u['context'] for u in tu)])
ck("31 unita' prima (L273 + L274 + L275)",
   db.execute('select count(*) from units where path=? and line<1375', (PATH,)).fetchone()[0] == 31)
ck("7 unita' dopo la 1961",
   db.execute('select count(*) from units where path=? and line>1961', (PATH,)).fetchone()[0] == 7)
ck('confine: la 2010 apre `Model 8`',
   db.execute('select line,context from units where path=? and line>1961 order by line limit 1', (PATH,)).fetchone()
   == (2010, 'ship:Model 8'))
ck('il file ha 50 unita, righe 95-2363',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (50, 95, 2363))
per_lotto, righe = [], set()
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    us = [u for u in json.load(open(f, encoding='utf-8'))['units'] if u['path'] == PATH]
    if us:
        per_lotto.append((os.path.basename(os.path.dirname(f)), len(us)))
        righe |= {u['line'] for u in us}
seg = {l for l in righe if 1375 <= l <= 1961}
ck('SEGMENTO: le 12 righe del lotto sono esattamente quelle 1375-1961',
   seg == {u['line'] for u in tu} and len(seg) == 12, (sorted(seg - {u['line'] for u in tu}), len(seg)))
overlap = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    if os.path.basename(os.path.dirname(f)) == os.path.basename(HERE):
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH and 1375 <= u['line'] <= 1961:
            overlap.append((os.path.basename(os.path.dirname(f)), u['line']))
ck('nessun altro lotto rivendica le righe 1375-1961', not overlap, overlap)
ck('copertura del SEGMENTO: 12/12 righe; il totale del file e stampato, non asserito',
   len(seg) == 12 and 50 - len(seg) == 38, '%d/50 (file)' % len(righe))
ck('tutte tradotte, nessuna copiata',
   not [u['idx'] for u in tu if u['italian'] == u['english']],
   [u['idx'] for u in tu if u['italian'] == u['english']])
ck('TAB: due, alle unita 10 e 12, primi caratteri in entrambe le lingue',
   sum(u['english'].count(TAB) for u in tu) == 2 == sum(u['italian'].count(TAB) for u in tu)
   and [u['idx'] for u in tu if TAB in u['italian']] == [10, 12]
   and all(u['italian'].startswith(TAB) for u in tu if TAB in u['italian']))
ck('VIRGOLETTE: due, all unita 1, dritte',
   sum(u['english'].count(QUOTE) for u in tu) == 2 == sum(u['italian'].count(QUOTE) for u in tu)
   and [u['idx'] for u in tu if QUOTE in u['italian']] == [1])
ck('apici: 2 in inglese, 7 in italiano',
   sum(u['english'].count(APOS) for u in tu) == 2 and sum(u['italian'].count(APOS) for u in tu) == 7,
   (sum(u['english'].count(APOS) for u in tu), sum(u['italian'].count(APOS) for u in tu)))
ck('lessico: mercantile, portatrice, incrociatori da battaglia, scafo ultradenso',
   'mercantile' in by[2]['italian'] and 'portatrice' in by[6]['italian']
   and 'incrociatori da battaglia' in by[4]['italian'] and 'scafo ultradenso' in by[9]['italian'])
ck('i nomi delle fazioni restano dove l inglese li nomina',
   not [(u['idx'], n) for u in tu for n in ('Efreti', 'Quarg', 'Mereti', 'Kor Sestor', 'TF109', 'FS27')
        if n in u['english'] and n not in u['italian']])
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in tu for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90 per ogni unita',
   all(0.55 < u['ratio'] < 1.90 for u in tu),
   [(u['idx'], u['ratio']) for u in tu if not 0.55 < u['ratio'] < 1.90])
ck('tutte le 12 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in tu))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('SEGMENTO: 31 prima · 12 qui · 7 dopo · 10 contesti · 2 tab · 2 virgolette')
print('parole EN %d -> IT %d · ratio %.2f - %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(u['ratio'] for u in tu), max(u['ratio'] for u in tu)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L276 superato' if not fail else 'verify L276 fallito')
raise SystemExit(0 if not fail else 1)
