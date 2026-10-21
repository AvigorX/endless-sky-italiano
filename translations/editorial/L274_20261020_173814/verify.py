r"""verify.py — L274 (`data/korath/korath ships.txt`, righe 364-602). **Secondo lotto del file**.

Verifica da sola: riga grezza, campi del DB, il **segmento** (8 prima, 9 qui, **33** dopo la 602), i **quattro contesti** con le
righe (`'olofez` su tre righe non contigue), i **quattro tab**, il `VALUE` copiato, e che **nessun altro lotto** rivendichi
queste righe.

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
CTX = ["'olofez", "Kas'ik Tek 7", "Rai'alorej", "Ikatila'ej"]
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


ck('riga grezza identica al sorgente (9/9)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = [u['idx'] for u in su
       if db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
       != (u['english'], u['kind'], u['path'], u['context'])]
ck('english/kind/path/context identici al DB', not bad, bad)
ck('9 unita, righe 364-602, 8 DESCRIPTION + 1 VALUE',
   len(tu) == 9 and [u['line'] for u in tu] == sorted({u['line'] for u in tu})
   and collections.Counter(u['kind'] for u in tu) == {'DESCRIPTION': 8, 'VALUE': 1},
   (len(tu), collections.Counter(u['kind'] for u in tu)))
ck('i quattro contesti compaiono in quest ordine, senza altri',
   [c.replace('ship:', '', 1) for c in dict.fromkeys(u['context'] for u in tu)] == CTX,
   [c for c in dict.fromkeys(u['context'] for u in tu)])
ck("8 unita' prima (L273)",
   db.execute('select count(*) from units where path=? and line<364', (PATH,)).fetchone()[0] == 8)
ck("33 unita' dopo la 602",
   db.execute('select count(*) from units where path=? and line>602', (PATH,)).fetchone()[0] == 33)
ck('confine: la 606 apre `Lor\'kas Ik 577`',
   db.execute('select line,context from units where path=? and line>602 order by line limit 1', (PATH,)).fetchone()
   == (606, "ship:Lor'kas Ik 577"))
ck('il file ha 50 unita, righe 95-2363',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (50, 95, 2363))
per_lotto, righe = [], set()
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    us = [u for u in json.load(open(f, encoding='utf-8'))['units'] if u['path'] == PATH]
    if us:
        per_lotto.append((os.path.basename(os.path.dirname(f)), len(us)))
        righe |= {u['line'] for u in us}
seg = {l for l in righe if 364 <= l <= 602}
ck('SEGMENTO: le 9 righe del lotto sono esattamente quelle 364-602',
   seg == {u['line'] for u in tu} and len(seg) == 9, (sorted(seg - {u['line'] for u in tu}), len(seg)))
overlap = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    if os.path.basename(os.path.dirname(f)) == os.path.basename(HERE):
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH and 364 <= u['line'] <= 602:
            overlap.append((os.path.basename(os.path.dirname(f)), u['line']))
ck('nessun altro lotto rivendica le righe 364-602', not overlap, overlap)
ck('copertura del SEGMENTO: 9/9 righe; il totale del file e stampato, non asserito',
   len(seg) == 9 and 50 - len(seg) == 41, '%d/50 (file)' % len(righe))
ck('il VALUE e copiato; le 8 DESCRIPTION sono tradotte',
   all(u['italian'] == u['english'] for u in tu if u['kind'] == 'VALUE')
   and all(u['italian'] != u['english'] for u in tu if u['kind'] == 'DESCRIPTION'))
ck('TAB: quattro, sulle unita dispari, primi caratteri in entrambe le lingue',
   sum(u['english'].count(TAB) for u in tu) == 4 == sum(u['italian'].count(TAB) for u in tu)
   and [u['idx'] for u in tu if TAB in u['italian']] == [3, 5, 7, 9]
   and all(u['italian'].startswith(TAB) for u in tu if TAB in u['italian']))
ck('zero virgolette e zero segnaposto',
   sum(u['english'].count(QUOTE) + u['italian'].count(QUOTE) for u in tu) == 0
   and not [t for u in tu for t in TAG.findall(u['english']) + TAG.findall(u['italian'])])
ck('apici: 5 in inglese, 13 in italiano',
   sum(u['english'].count(APOS) for u in tu) == 5 and sum(u['italian'].count(APOS) for u in tu) == 13,
   (sum(u['english'].count(APOS) for u in tu), sum(u['italian'].count(APOS) for u in tu)))
ck('lessico: iperguida, baia di caccia, baia per droni, microbot, navi ospedale',
   'iperguida' in by[3]['italian'] and 'baia di caccia' in by[3]['italian']
   and 'baia per droni' in by[5]['italian'] and 'microbot' in by[4]['italian']
   and 'navi ospedale' in by[6]['italian'])
ck('la stazione resta una stazione e `Ikatila\'ej` e un nome proprio invariato',
   'stazioni spaziali' in by[8]['italian'] and "Ikatila'ej" in by[8]['italian'])
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in tu for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90 per ogni unita',
   all(0.55 < u['ratio'] < 1.90 for u in tu),
   [(u['idx'], u['ratio']) for u in tu if not 0.55 < u['ratio'] < 1.90])
ck('tutte le 9 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in tu))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('SEGMENTO: 8 prima · 9 qui · 33 dopo · 4 contesti · 4 tab')
print('parole EN %d -> IT %d · ratio %.2f - %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(u['ratio'] for u in tu), max(u['ratio'] for u in tu)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L274 superato' if not fail else 'verify L274 fallito')
raise SystemExit(0 if not fail else 1)
