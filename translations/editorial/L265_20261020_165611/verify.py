r"""verify.py — L265 (`data/kahet/aberrant ships.txt`, righe 16-685). **Primo lotto del file**.

Verifica da sola: riga grezza, campi del DB, il **segmento** (0 prima della 16, **22** dopo la 685 — il lotto apre il file),
i **nove contesti** in sequenza, le **32 virgolette** per unita', i 26 `VALUE` copiati, e che **nessun altro lotto**
rivendichi queste righe.

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
PATH = 'data/kahet/aberrant ships.txt'
NAVI = ['Aberrant Latte', 'Aberrant Chomper', 'Aberrant Pileup', 'Aberrant Hugger', 'Aberrant Longfellow',
        'Aberrant Dancer', 'Aberrant Junior', 'Aberrant Icebreaker', 'Aberrant Pike']
src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
su = sorted(src['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
raw_lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
fail = []


def ck(n, c, d=''):
    print('%-96s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente (43/43)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = [u['idx'] for u in su
       if db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
       != (u['english'], u['kind'], u['path'], u['context'])]
ck('english/kind/path/context identici al DB', not bad, bad)
ck('43 unita, righe 16-685, tipi 26/17',
   len(tu) == 43 and [u['line'] for u in tu] == sorted({u['line'] for u in tu})
   and collections.Counter(u['kind'] for u in tu) == {'VALUE': 26, 'DESCRIPTION': 17},
   (len(tu), collections.Counter(u['kind'] for u in tu)))
ck('i nove contesti compaiono nell ordine delle navi, senza altri',
   [c.replace('ship:', '') for c in dict.fromkeys(u['context'] for u in tu)] == NAVI,
   [c for c in dict.fromkeys(u['context'] for u in tu)])
ck("ZERO unita' prima della 16: il lotto APRE il file",
   db.execute('select count(*) from units where path=? and line<16', (PATH,)).fetchone()[0] == 0)
ck("22 unita' dopo la 685", db.execute('select count(*) from units where path=? and line>685', (PATH,)).fetchone()[0] == 22)
ck('confine: la 686 apre `ship:Aberrant Pike`, il contesto dell ultima unita',
   db.execute('select line,context from units where path=? and line>685 order by line limit 1', (PATH,)).fetchone()
   == (686, 'ship:Aberrant Pike'))
ck('il file ha 65 unita, righe 16-1007',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (65, 16, 1007))
per_lotto, righe = [], set()
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    us = [u for u in json.load(open(f, encoding='utf-8'))['units'] if u['path'] == PATH]
    if us:
        per_lotto.append((os.path.basename(os.path.dirname(f)), len(us)))
        righe |= {u['line'] for u in us}
seg = {l for l in righe if 16 <= l <= 685}
ck('SEGMENTO: le 43 righe del lotto sono esattamente quelle 16-685',
   seg == {u['line'] for u in tu} and len(seg) == 43, (sorted(seg - {u['line'] for u in tu}), len(seg)))
overlap = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    if os.path.basename(os.path.dirname(f)) == os.path.basename(HERE):
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH and 16 <= u['line'] <= 685:
            overlap.append((os.path.basename(os.path.dirname(f)), u['line']))
ck('nessun altro lotto rivendica le righe 16-685', not overlap, overlap)
ck('copertura del SEGMENTO: 43/43 righe; il totale del file e stampato, non asserito',
   len(seg) == 43 and 65 - len(seg) == 22, '%d/65 (file)' % len(righe))
ck('i 26 VALUE sono copiati identici; le 17 DESCRIPTION sono tradotte',
   all(u['italian'] == u['english'] for u in tu if u['kind'] == 'VALUE')
   and all(u['italian'] != u['english'] for u in tu if u['kind'] == 'DESCRIPTION'))
ck('VIRGOLETTE: 32 in inglese e 32 in italiano, mappa per unita identica',
   sum(u['english'].count(QUOTE) for u in tu) == 32 == sum(u['italian'].count(QUOTE) for u in tu)
   and {u['idx']: u['english'].count(QUOTE) for u in tu if QUOTE in u['english']}
   == {u['idx']: u['italian'].count(QUOTE) for u in tu if QUOTE in u['italian']})
by = {u['idx']: u for u in tu}
ck('le 9 note organo-metalliche hanno una sola resa; le 8 frasi sulla variante sono distinte',
   len({by[i]['italian'] for i in (3, 8, 13, 18, 23, 28, 33, 38, 43)}) == 1
   and len({by[i]['italian'] for i in (4, 9, 14, 19, 24, 29, 34, 39)}) == 8)
ck('ZERO tab e ZERO segnaposto in entrambe le lingue',
   sum(u['english'].count(TAB) + u['italian'].count(TAB) for u in tu) == 0
   and not [t for u in tu for t in TAG.findall(u['english']) + TAG.findall(u['italian'])])
ck('APICI: zero in inglese, 10 in italiano (le elisioni delle schede)',
   sum(u['english'].count(APOS) for u in tu) == 0 and sum(u['italian'].count(APOS) for u in tu) == 10,
   (sum(u['english'].count(APOS) for u in tu), sum(u['italian'].count(APOS) for u in tu)))
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in tu for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90 per ogni unita',
   all(0.55 < u['ratio'] < 1.90 for u in tu),
   [(u['idx'], u['ratio']) for u in tu if not 0.55 < u['ratio'] < 1.90])
ck('lessico: organo-metallica, fusoliera, punti di attacco, torrette, scafo',
   'organo-metallica' in by[3]['italian'] and 'fusoliera' in by[24]['italian']
   and 'punti di attacco' in by[29]['italian'] and 'scafo' in by[39]['italian'])
ck('tutte le 43 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in tu))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('SEGMENTO: 0 prima · 43 qui · 22 dopo · 9 contesti · 32 virgolette nei nomi')
print('parole EN %d -> IT %d · ratio %.2f - %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(u['ratio'] for u in tu), max(u['ratio'] for u in tu)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L265 superato' if not fail else 'verify L265 fallito')
raise SystemExit(0 if not fail else 1)
