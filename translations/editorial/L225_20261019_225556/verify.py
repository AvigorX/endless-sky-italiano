r"""verify.py — L225 (`data/remnant/remnant outfits.txt`, 11 unita', righe 581-674). Terzo lotto del file.

Terzo lotto: **25** unita' gia' tradotte prima della 581 (L223 12 + L224 13), **11** in questo, **21** dopo la 674.

    25 + 11 + 21 = 57  (le unita' del file)

Confine: riga **675**, una **`DESCRIPTION`** di `outfit:Research Laboratory`, **una riga dopo** l'ultima unita' del lotto —
lo stesso equipaggiamento dell'unita' 11: la scheda continua oltre il confine.

**Zero unita' identiche all'inglese**: tutte e 11 sono `DESCRIPTION` tradotte; il `0` e' asserito.
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
ck('unita: 11 righe 581 - 674', len(tu) == 11 and (tu[0]['line'], tu[-1]['line']) == (581, 674))
ck('25 unita tradotte prima della 581 (L223 12 + L224 13)', db.execute(
    'select count(*) from units where path=? and line<581', (PATH,)).fetchone()[0] == 25)
ck('21 unita dopo la 674 (57 - 36)', db.execute(
    'select count(*) from units where path=? and line>674', (PATH,)).fetchone()[0] == 21)
nxt = db.execute('select line,kind,context from units where path=? and line>674 order by line limit 1',
                 (PATH,)).fetchone()
ck('confine misurato: riga 675, DESCRIPTION di outfit:Research Laboratory, UNA riga dopo',
   nxt == (675, 'DESCRIPTION', 'outfit:Research Laboratory'), nxt)
ck('il confine prosegue lo stesso equipaggiamento dell\'unita\' 11',
   tu[10]['context'] == 'outfit:Research Laboratory' == nxt[2])
ck('il file intero: 57 unita, righe 48 - 979',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (57, 48, 979))
ck('lotto + residuo = file: 25 + 11 + 21 = 57',
   25 + len(tu) + db.execute('select count(*) from units where path=? and line>674',
                             (PATH,)).fetchone()[0] == 57)
ck('tipi del lotto: 11 DESCRIPTION, nessun\'altra unita\'',
   collections.Counter(u['kind'] for u in su) == {'DESCRIPTION': 11})
ck('ZERO unita\' identiche all\'inglese e 11 tradotte',
   sum(1 for u in tu if u['italian'] == u['english']) == 0
   and all(u['italian'] != u['english'] for u in tu))
ck('4 tab (unita\' 2, 4, 6, 10) e 2 virgolette (unita\' 8, le "branchie")',
   [u['idx'] for u in tu if TAB in u['italian']] == [2, 4, 6, 10]
   and sum(u['english'].count(QUOTE) for u in su) == 2 == sum(u['italian'].count(QUOTE) for u in tu)
   and [u['idx'] for u in tu if QUOTE in u['italian']] == [8])
ck('famiglia di «ion» coerente e nomi propri invariati (Remnant, Ember Waste, Viminal)',
   'ionizzazione' in ' '.join(u['italian'] for u in tu)
   and 'dissipazione ionica' in ' '.join(u['italian'] for u in tu)
   and 'Ember Waste' in ' '.join(u['italian'] for u in tu)
   and 'Viminal' in ' '.join(u['italian'] for u in tu))
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
ck('rapporto nel gate 0,55-1,90 (1,04 - 1,15; 455 -> 461 parole)',
   0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('APERTO: 36/57 unita\' del file (25 + 11) · restano 21 dopo la 674 · confine riga 675 (DESCRIPTION)')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L225 superato' if not fail else 'verify L225 fallito')
raise SystemExit(0 if not fail else 1)
