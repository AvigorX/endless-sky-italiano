r"""verify.py — L224 (`data/remnant/remnant outfits.txt`, 13 unita', righe 298-565). Secondo lotto del file.

Secondo lotto: **12** unita' gia' tradotte prima della 298 (L223), **13** in questo, **32** dopo la 565.

    12 + 13 + 32 = 57  (le unita' del file)

Confine: riga **581**, una **`DESCRIPTION`** di `outfit:Millennium Cell`, sedici righe dopo l'ultima unita' del lotto.

**Zero unita' identiche all'inglese**: tutte e 13 sono `DESCRIPTION` tradotte. Il controllo lo asserisce esplicitamente,
perche' in questo file le unita' «copiate» non esistono e un `0` silenzioso sarebbe indistinguibile da un errore.
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
AMMO = ('\tLe munizioni per quest\'arma possono essere rifornite presso qualsiasi negozio di equipaggiamenti.')
su = sorted(json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
fail = []


def ck(n, c, d=''):
    print('%-74s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente (13/13)', not [u for u in su if lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck('unita: 13 righe 298 - 565', len(tu) == 13 and (tu[0]['line'], tu[-1]['line']) == (298, 565))
ck('12 unita tradotte prima della 298 (L223)', db.execute(
    'select count(*) from units where path=? and line<298', (PATH,)).fetchone()[0] == 12)
ck('32 unita dopo la 565 (57 - 25)', db.execute(
    'select count(*) from units where path=? and line>565', (PATH,)).fetchone()[0] == 32)
nxt = db.execute('select line,kind,context from units where path=? and line>565 order by line limit 1',
                 (PATH,)).fetchone()
ck('confine misurato: riga 581, DESCRIPTION di outfit:Millennium Cell, sedici righe dopo',
   nxt == (581, 'DESCRIPTION', 'outfit:Millennium Cell'), nxt)
ck('il file intero: 57 unita, righe 48 - 979',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (57, 48, 979))
ck('lotto + residuo = file: 12 + 13 + 32 = 57',
   12 + len(tu) + db.execute('select count(*) from units where path=? and line>565',
                             (PATH,)).fetchone()[0] == 57)
ck('tipi del lotto: 13 DESCRIPTION, nessun\'altra unita\'',
   collections.Counter(u['kind'] for u in su) == {'DESCRIPTION': 13})
ck('ZERO unita\' identiche all\'inglese e 13 tradotte (primato: niente da copiare)',
   sum(1 for u in tu if u['italian'] == u['english']) == 0
   and all(u['italian'] != u['english'] for u in tu))
ck('9 tab (unita\' 1, 3, 4, 5, 7, 8, 10, 11, 13) e 2 virgolette (unita\' 3)',
   [u['idx'] for u in tu if TAB in u['italian']] == [1, 3, 4, 5, 7, 8, 10, 11, 13]
   and sum(u['english'].count(QUOTE) for u in su) == 2 == sum(u['italian'].count(QUOTE) for u in tu)
   and [u['idx'] for u in tu if QUOTE in u['italian']] == [3])
ck('le tre righe di servizio (1, 5, 8) hanno la stessa resa',
   tu[0]['italian'] == tu[4]['italian'] == tu[7]['italian'] == AMMO)
ck('coerenza con L223/12: «furono sviluppate originariamente dai Remnant»',
   tu[1]['italian'].startswith('Le armi a impulso elettromagnetico furono sviluppate originariamente dai Remnant'))
ck('0 segnaposto', sum(len(TAG.findall(u['english'])) for u in su) == 0
   == sum(len(TAG.findall(u['italian'])) for u in tu))
ck('PENDING su tutte e 13', not [u['idx'] for u in su
                                 if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('nessuno spazio finale e nessun doppio spazio (tab iniziali ammessi)',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip()
        or '  ' in u['italian'].strip(TAB)])
ck('nessun carattere tipografico e nessun non latino',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')
        or any(ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F for c in u['italian'])])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate 0,55-1,90 (0,98 - 1,58; 472 -> 483 parole)',
   0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('APERTO: 25/57 unita\' del file (12 + 13) · restano 32 dopo la 565 · confine riga 581 (DESCRIPTION)')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L224 superato' if not fail else 'verify L224 fallito')
raise SystemExit(0 if not fail else 1)
