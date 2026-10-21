r"""verify.py — L223 (`data/remnant/remnant outfits.txt`, 12 unita', righe 48-297). **Primo lotto del file.**

Primo lotto: `line < 48` deve valere **0**. Confine dopo: riga **298**, una **`DESCRIPTION`** di `outfit:EMP Torpedo Bay`,
una riga dopo l'ultima unita' del lotto.

Il file ha **57** unita' (righe 48-979): il lotto ne copre **12**, ne restano **45**. Il file e' quasi tutto prosa
(**55 `DESCRIPTION`, 2 `VALUE`**): il controllo lo misura dal database, non lo deduce dal lotto.
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
PATH = 'data/remnant/remnant outfits.txt'
su = sorted(json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
IT_ALL = ' '.join(u['italian'] for u in tu)
fail = []


def ck(n, c, d=''):
    print('%-74s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente (12/12)', not [u for u in su if lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck('unita: 12 righe 48 - 297', len(tu) == 12 and (tu[0]['line'], tu[-1]['line']) == (48, 297))
ck('PRIMO LOTTO: zero unita prima della riga 48 (invariante misurata)',
   db.execute('select count(*) from units where path=? and line<48', (PATH,)).fetchone()[0] == 0)
ck('la riga 48 e\' la PRIMA unita\' del percorso nel DB',
   db.execute('select min(line) from units where path=?', (PATH,)).fetchone()[0] == 48)
ck('45 unita dopo la 297 (57 - 12)', db.execute(
    'select count(*) from units where path=? and line>297', (PATH,)).fetchone()[0] == 45)
nxt = db.execute('select line,kind,context from units where path=? and line>297 order by line limit 1',
                 (PATH,)).fetchone()
ck('confine misurato: riga 298, DESCRIPTION di outfit:EMP Torpedo Bay, una riga dopo',
   nxt == (298, 'DESCRIPTION', 'outfit:EMP Torpedo Bay'), nxt)
ck('il file intero: 57 unita, righe 48 - 979',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (57, 48, 979))
ck('lotto + residuo = file: 12 + 45 = 57',
   len(tu) + db.execute('select count(*) from units where path=? and line>297', (PATH,)).fetchone()[0] == 57)
ck('il file e\' quasi tutto prosa: 55 DESCRIPTION e 2 VALUE (misurato dal DB)',
   db.execute('select kind,count(*) from units where path=? group by kind',
              (PATH,)).fetchall() == [('DESCRIPTION', 55), ('VALUE', 2)])
ck('tipi del lotto: 11 DESCRIPTION, 1 VALUE',
   collections.Counter(u['kind'] for u in su) == {'DESCRIPTION': 11, 'VALUE': 1})
ck('1 unita\' identica all\'inglese (il VALUE) e 11 tradotte: qui si traduce quasi tutto',
   sum(1 for u in tu if u['italian'] == u['english']) == 1
   and tu[7]['italian'] == 'EMP Torpedoes'
   and all(u['italian'] != u['english'] for u in tu if u['kind'] == 'DESCRIPTION'))
ck('3 tab (unita\' 2, 4, 11), 2 virgolette (unita\' 1), 0 segnaposto',
   [u['idx'] for u in tu if TAB in u['italian']] == [2, 4, 11]
   and sum(u['english'].count(QUOTE) for u in su) == 2 == sum(u['italian'].count(QUOTE) for u in tu)
   and [u['idx'] for u in tu if QUOTE in u['italian']] == [1]
   and sum(len(TAG.findall(u['english'])) for u in su) == 0
   == sum(len(TAG.findall(u['italian'])) for u in tu))
ck('i nomi degli equipaggiamenti restano inglesi nella prosa, le parole comuni sono tradotte',
   'Inhibitor Cannon' in IT_ALL and 'Thrasher Cannons' in IT_ALL
   and re.search(r'\bcannoni\b', IT_ALL) is not None
   and re.search(r'\btorrette?\b', IT_ALL) is not None)
ck('PENDING su tutte e 12', not [u['idx'] for u in su
                                 if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('nessuno spazio finale e nessun doppio spazio (tab iniziali ammessi)',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip()
        or '  ' in u['italian'].strip(TAB)])
ck('nessun carattere tipografico e nessun non latino',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')
        or any(ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F for c in u['italian'])])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate 0,55-1,90 (0,99 - 1,15; 463 -> 458 parole: qui l\'italiano e\' piu\' corto)',
   0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('APERTO: 12/57 unita\' del file · restano 45 dopo la 297 · confine riga 298 (DESCRIPTION)')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L223 superato' if not fail else 'verify L223 fallito')
raise SystemExit(0 if not fail else 1)
