r"""verify.py — L226 (`data/remnant/remnant outfits.txt`, 11 unita', righe 675-864). Quarto lotto del file.

Quarto lotto: **36** unita' gia' tradotte prima della 675 (L223 12 + L224 13 + L225 11), **11** in questo, **10** dopo la
864.

    36 + 11 + 10 = 57  (le unita' del file)

Confine: riga **884**, una **`DESCRIPTION`** di `outfit:Forge-Class Steering`.

**Il residuo e' il lotto terminale**: le 10 unita' dopo la 864 includono l'**ultimo `VALUE` del file** (riga **948**,
`Void Sprite Parts`). Il controllo lo asserisce qui, cosi' L227 sa gia' che dovra' copiare **1** unita' e non 0.
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
fail = []


def ck(n, c, d=''):
    print('%-74s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente (11/11)', not [u for u in su if lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck('unita: 11 righe 675 - 864', len(tu) == 11 and (tu[0]['line'], tu[-1]['line']) == (675, 864))
ck('36 unita tradotte prima della 675 (L223 12 + L224 13 + L225 11)', db.execute(
    'select count(*) from units where path=? and line<675', (PATH,)).fetchone()[0] == 36)
ck('10 unita dopo la 864 (57 - 47)', db.execute(
    'select count(*) from units where path=? and line>864', (PATH,)).fetchone()[0] == 10)
nxt = db.execute('select line,kind,context from units where path=? and line>864 order by line limit 1',
                 (PATH,)).fetchone()
ck('confine misurato: riga 884, DESCRIPTION di outfit:Forge-Class Steering, venti righe dopo',
   nxt == (884, 'DESCRIPTION', 'outfit:Forge-Class Steering'), nxt)
ck('il residuo contiene l\'ULTIMO VALUE del file (riga 948, Void Sprite Parts): L227 copiera\' 1 unita\'',
   [r[0] for r in db.execute('select line from units where path=? and line>864 and kind="VALUE"',
                             (PATH,)).fetchall()] == [948]
   and db.execute('select english from units where path=? and line=948', (PATH,)).fetchone()[0] == 'Void Sprite Parts')
ck('il file intero: 57 unita, righe 48 - 979',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (57, 48, 979))
ck('lotto + residuo = file: 36 + 11 + 10 = 57',
   36 + len(tu) + db.execute('select count(*) from units where path=? and line>864',
                             (PATH,)).fetchone()[0] == 57)
ck('tipi del lotto: 11 DESCRIPTION, nessun\'altra unita\'',
   collections.Counter(u['kind'] for u in su) == {'DESCRIPTION': 11})
ck('ZERO unita\' identiche all\'inglese e 11 tradotte',
   sum(1 for u in tu if u['italian'] == u['english']) == 0
   and all(u['italian'] != u['english'] for u in tu))
ck('3 tab (unita\' 1, 4, 6) e ZERO virgolette in entrambe le lingue',
   [u['idx'] for u in tu if TAB in u['italian']] == [1, 4, 6]
   and sum(u['english'].count(QUOTE) for u in su) == 0 == sum(u['italian'].count(QUOTE) for u in tu))
ck('i tre punti dell\'unita\' 9 sono tre punti, non un carattere …',
   tu[8]['italian'].count('...') == 1 and '\u2026' not in tu[8]['italian'])
ck('0 segnaposto', sum(len(TAG.findall(u['english'])) for u in su) == 0
   == sum(len(TAG.findall(u['italian'])) for u in tu))
ck('PENDING su tutte e 11', not [u['idx'] for u in su
                                 if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('nessuno spazio finale e nessun doppio spazio (tab iniziali ammessi)',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip()
        or '  ' in u['italian'].strip(TAB)])
ck('nessun carattere tipografico e nessun non latino',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')
        or any(ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F for c in u['italian'])])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate 0,55-1,90 (1,00 - 1,21; 445 -> 447 parole)',
   0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('APERTO: 47/57 unita\' del file (36 + 11) · restano 10 dopo la 864 · confine riga 884 (DESCRIPTION)')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L226 superato' if not fail else 'verify L226 fallito')
raise SystemExit(0 if not fail else 1)
