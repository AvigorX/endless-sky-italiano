r"""verify.py — L219 (`data/successors/successor ships.txt`, 25 unita', righe 386-629). Secondo lotto del file.

Secondo lotto: **45** unita' gia' tradotte prima della 386 (L218), **25** in questo lotto, **76** dopo la 629.

    45 + 25 + 76 = 146  (le unita' del file)

Confine: riga **634**, un `VALUE` di `ship:Nnaatej`, cinque righe dopo l'ultima unita' del lotto.

**19 unita' identiche all'inglese e 6 tradotte**: il controllo verifica che le tradotte siano esattamente le `DESCRIPTION`,
perche' e' la regola del file e non una dimenticanza.
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


ck('riga grezza identica al sorgente (25/25)', not [u for u in su if lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck('unita: 25 righe 386 - 629', len(tu) == 25 and (tu[0]['line'], tu[-1]['line']) == (386, 629))
ck('45 unita tradotte prima della 386 (L218)', db.execute(
    'select count(*) from units where path=? and line<386', (PATH,)).fetchone()[0] == 45)
ck('76 unita dopo la 629 (146 - 70)', db.execute(
    'select count(*) from units where path=? and line>629', (PATH,)).fetchone()[0] == 76)
nxt = db.execute('select line,kind,context from units where path=? and line>629 order by line limit 1',
                 (PATH,)).fetchone()
ck('confine misurato: riga 634, VALUE di ship:Nnaatej, cinque righe dopo',
   nxt == (634, 'VALUE', 'ship:Nnaatej'), nxt)
ck('il file intero: 146 unita, righe 17 - 1338',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (146, 17, 1338))
ck('lotto + residuo = file: 45 + 25 + 76 = 146',
   45 + len(tu) + db.execute('select count(*) from units where path=? and line>629',
                             (PATH,)).fetchone()[0] == 146)
ck('tipi del lotto: 16 TEXT, 6 DESCRIPTION, 3 VALUE',
   collections.Counter(u['kind'] for u in su) == {'TEXT': 16, 'DESCRIPTION': 6, 'VALUE': 3})
ck('19 unita\' IDENTICHE all\'inglese + 6 tradotte = le 6 DESCRIPTION',
   sum(1 for u in tu if u['italian'] == u['english']) == 19
   and sorted(u['idx'] for u in tu if u['italian'] != u['english'])
   == sorted(u['idx'] for u in tu if u['kind'] == 'DESCRIPTION'))
ck('32 virgolette (2 x 16 TEXT), 1 tab (unita\' 8), 0 segnaposto',
   sum(u['english'].count('"') for u in su) == 32 == sum(u['italian'].count('"') for u in tu)
   and [u['idx'] for u in tu if '"' in u['italian']] == [u['idx'] for u in tu if u['kind'] == 'TEXT']
   and [u['idx'] for u in tu if TAB in u['italian']] == [8]
   and sum(len(TAG.findall(u['english'])) for u in su) == 0
   == sum(len(TAG.findall(u['italian'])) for u in tu))
ck('coerenza 7/9 (stessa apertura) e 24/25 («non è né elegante né veloce»)',
   tu[6]['italian'][:70] == tu[8]['italian'][:70]
   and 'non è né elegante né veloce' in tu[23]['italian']
   and 'non è né elegante né veloce' in tu[24]['italian'])
ck('PENDING su tutte e 25', not [u['idx'] for u in su
                                 if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('nessuno spazio finale e nessun doppio spazio (tab iniziale dell\'unita\' 8 ammesso)',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip()
        or '  ' in u['italian'].strip(TAB)])
ck('nessun carattere tipografico e nessun non latino',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')
        or any(ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F for c in u['italian'])])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate 0,55-1,90 (nomi 1,00; DESCRIPTION 1,05-1,16; totale 467 -> 487 parole)',
   0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('APERTO: 70/146 unita\' del file (45 + 25) · restano 76 dopo la 629 · confine riga 634 (VALUE)')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L219 superato' if not fail else 'verify L219 fallito')
raise SystemExit(0 if not fail else 1)
