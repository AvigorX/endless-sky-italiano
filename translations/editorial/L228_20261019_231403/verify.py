r"""verify.py — L228 (`data/korath/korath outfits.txt`, 20 unita', righe 16-195). **Primo lotto del file.**

Primo lotto: `line < 16` deve valere **0**. Confine dopo: riga **208**, una **`DESCRIPTION`** di `outfit:Fuel Processor`.

Il file ha **92** unita' (righe 16-908): il lotto ne copre **20**, ne restano **72**. Il file e' **misto**
(**29 `VALUE` + 63 `DESCRIPTION`**): il controllo lo misura dal database, e distingue nel lotto **7 identiche** (tutti i
`VALUE`) da **13 tradotte** (tutte le `DESCRIPTION`), verificando che i due insiemi coincidano esattamente.
"""
import collections
import hashlib
import json
import os
import re
import sqlite3

TAB = chr(9)
QUOTE = chr(34)
TAG = re.compile(r'<[^<>]+>')
HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
ROOT = os.path.abspath(os.path.join(L10N, '..'))
PATH = 'data/korath/korath outfits.txt'
su = sorted(json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
fail = []


def ck(n, c, d=''):
    print('%-74s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente (20/20)', not [u for u in su if lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck('unita: 20 righe 16 - 195', len(tu) == 20 and (tu[0]['line'], tu[-1]['line']) == (16, 195))
ck('PRIMO LOTTO: zero unita prima della riga 16 (invariante misurata)',
   db.execute('select count(*) from units where path=? and line<16', (PATH,)).fetchone()[0] == 0)
ck('la riga 16 e\' la PRIMA unita\' del percorso nel DB',
   db.execute('select min(line) from units where path=?', (PATH,)).fetchone()[0] == 16)
ck('72 unita dopo la 195 (92 - 20)', db.execute(
    'select count(*) from units where path=? and line>195', (PATH,)).fetchone()[0] == 72)
nxt = db.execute('select line,kind,context from units where path=? and line>195 order by line limit 1',
                 (PATH,)).fetchone()
ck('confine misurato: riga 208, DESCRIPTION di outfit:Fuel Processor, tredici righe dopo',
   nxt == (208, 'DESCRIPTION', 'outfit:Fuel Processor'), nxt)
ck('il file intero: 92 unita, righe 16 - 908',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (92, 16, 908))
ck('il file e\' misto: 29 VALUE e 63 DESCRIPTION (misurato dal DB)',
   db.execute('select kind,count(*) from units where path=? group by kind',
              (PATH,)).fetchall() == [('DESCRIPTION', 63), ('VALUE', 29)])
ck('lotto + residuo = file: 20 + 72 = 92',
   len(tu) + db.execute('select count(*) from units where path=? and line>195', (PATH,)).fetchone()[0] == 92)
ck('tipi del lotto: 7 VALUE, 13 DESCRIPTION',
   collections.Counter(u['kind'] for u in su) == {'VALUE': 7, 'DESCRIPTION': 13})
ck('7 identiche (tutti e soli i VALUE) e 13 tradotte (tutte e sole le DESCRIPTION)',
   sum(1 for u in tu if u['italian'] == u['english']) == 7
   and sorted(u['idx'] for u in tu if u['italian'] == u['english'])
   == sorted(u['idx'] for u in tu if u['kind'] == 'VALUE')
   and sorted(u['idx'] for u in tu if u['italian'] != u['english'])
   == sorted(u['idx'] for u in tu if u['kind'] == 'DESCRIPTION'))
ck('ZERO tab e ZERO virgolette, in inglese e in italiano (due primati asseriti)',
   sum(u['english'].count(TAB) for u in su) == 0 == sum(u['italian'].count(TAB) for u in tu)
   and sum(u['english'].count(QUOTE) for u in su) == 0 == sum(u['italian'].count(QUOTE) for u in tu))
ck('0 segnaposto', sum(len(TAG.findall(u['english'])) for u in su) == 0
   == sum(len(TAG.findall(u['italian'])) for u in tu))
ck('i nomi restano inglesi nella prosa, la parola comune si traduce',
   'Systems Core' in ' '.join(u['italian'] for u in tu)
   and 'Fusion Reactor' in ' '.join(u['italian'] for u in tu)
   and 'reattore a fusione' in tu[8]['italian'])
ck('PENDING su tutte e 20', not [u['idx'] for u in su
                                 if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('nessun carattere tipografico e nessun non latino',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')
        or any(ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F for c in u['italian'])])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate 0,55-1,90 (1,00 - 1,26; 434 -> 474 parole)',
   0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('APERTO: 20/92 unita\' del file · restano 72 dopo la 195 · confine riga 208 (DESCRIPTION)')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L228 superato' if not fail else 'verify L228 fallito')
raise SystemExit(0 if not fail else 1)
