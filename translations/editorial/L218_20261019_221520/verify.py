r"""verify.py — L218 (`data/successors/successor ships.txt`, 45 unita', righe 17-381). **Primo lotto del file.**

Essendo il **primo** lotto, non c'e' nulla prima: `line < 17` deve valere **0**. Il confine dopo e' la riga **386**, un
`VALUE` di `ship:Kvelqde`, cinque righe dopo l'ultima unita' del lotto (381).

Il file ha **146** unita' (righe 17-1338): il lotto ne copre **45**, ne restano **101**.

**39 unita' su 45 restano identiche all'inglese** (35 `TEXT` = nomi di equipaggiamento, 4 `VALUE` = nomi di specie): il
controllo lo asserisce esplicitamente, perche' e' la regola del file e non una dimenticanza.
"""
import collections
import hashlib
import json
import os
import re
import sqlite3

TAB = chr(9)
TAG = re.compile(r'<[^<>]+>')
HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
ROOT = os.path.abspath(os.path.join(L10N, '..'))
PATH = 'data/successors/successor ships.txt'
su = sorted(json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
fail = []


def ck(n, c, d=''):
    print('%-74s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente (45/45)', not [u for u in su if lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck('unita: 45 righe 17 - 381', len(tu) == 45 and (tu[0]['line'], tu[-1]['line']) == (17, 381))
ck('PRIMO LOTTO: zero unita prima della riga 17 (invariante misurata)',
   db.execute('select count(*) from units where path=? and line<17', (PATH,)).fetchone()[0] == 0)
ck('la riga 17 e\' la PRIMA unita\' del percorso nel DB',
   db.execute('select min(line) from units where path=?', (PATH,)).fetchone()[0] == 17)
ck('101 unita dopo la 381', db.execute('select count(*) from units where path=? and line>381',
                                       (PATH,)).fetchone()[0] == 101)
nxt = db.execute('select line,kind,context from units where path=? and line>381 order by line limit 1',
                 (PATH,)).fetchone()
ck('confine misurato: riga 386, VALUE di ship:Kvelqde, cinque righe dopo',
   nxt == (386, 'VALUE', 'ship:Kvelqde'), nxt)
ck('il file intero: 146 unita, righe 17 - 1338',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (146, 17, 1338))
ck('lotto + residuo = file: 45 + 101 = 146',
   len(tu) + db.execute('select count(*) from units where path=? and line>381', (PATH,)).fetchone()[0] == 146)
ck('tipi del lotto: 35 TEXT, 6 DESCRIPTION, 4 VALUE',
   collections.Counter(u['kind'] for u in su) == {'TEXT': 35, 'DESCRIPTION': 6, 'VALUE': 4})
ck('39 unita\' IDENTICHE all\'inglese (35 TEXT + 4 VALUE), 6 tradotte: e\' la regola del file',
   sum(1 for u in tu if u['italian'] == u['english']) == 39
   and sorted(u['idx'] for u in tu if u['italian'] != u['english'])
   == sorted(u['idx'] for u in tu if u['kind'] == 'DESCRIPTION'))
ck('70 virgolette (2 per ognuna delle 35 TEXT), 1 tab (unita\' 32), 0 segnaposto',
   sum(u['english'].count('"') for u in su) == 70 == sum(u['italian'].count('"') for u in tu)
   and [u['idx'] for u in tu if '"' in u['italian']] == [u['idx'] for u in tu if u['kind'] == 'TEXT']
   and [u['idx'] for u in tu if TAB in u['italian']] == [32]
   and sum(len(TAG.findall(u['english'])) for u in su) == 0
   == sum(len(TAG.findall(u['italian'])) for u in tu))
ck('«"Ojet" Bimodal Coilgun» dieci volte in entrambe le lingue',
   sum(1 for u in tu if u['italian'] == '"Ojet" Bimodal Coilgun') == 10)
ck('PENDING su tutte e 45', not [u['idx'] for u in su
                                 if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('nessuno spazio finale e nessun doppio spazio (tab iniziale dell\'unita\' 32 ammesso)',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip()
        or '  ' in u['italian'].strip(TAB)])
ck('nessun carattere tipografico e nessun non latino',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')
        or any(ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F for c in u['italian'])])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate 0,55-1,90 (nomi 1,00; DESCRIPTION 1,09-1,15; totale 499 -> 549 parole)',
   0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('APERTO: 45/146 unita\' del file · restano 101 dopo la riga 381 · confine riga 386 (VALUE)')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L218 superato' if not fail else 'verify L218 fallito')
raise SystemExit(0 if not fail else 1)
