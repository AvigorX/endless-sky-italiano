r"""verify.py — L229 (`data/korath/korath outfits.txt`, 15 unita', righe 208-318). Secondo lotto del file.

Secondo lotto: **20** unita' gia' tradotte prima della 208 (L228), **15** in questo, **57** dopo la 318.

    20 + 15 + 57 = 92  (le unita' del file)

Confine: riga **319**, una **`DESCRIPTION`** di `outfit:Afterburner (Planetary Class)`: la **seconda scheda** dello stesso
equipaggiamento dell'unita' 15. La scheda e' spezzata dal confine, e il controllo lo registra verificando che il contesto
dell'ultima unita' del lotto sia lo stesso della prima unita' dopo.
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


ck('riga grezza identica al sorgente (15/15)', not [u for u in su if lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck('unita: 15 righe 208 - 318', len(tu) == 15 and (tu[0]['line'], tu[-1]['line']) == (208, 318))
ck('20 unita tradotte prima della 208 (L228)', db.execute(
    'select count(*) from units where path=? and line<208', (PATH,)).fetchone()[0] == 20)
ck('57 unita dopo la 318 (92 - 35)', db.execute(
    'select count(*) from units where path=? and line>318', (PATH,)).fetchone()[0] == 57)
nxt = db.execute('select line,kind,context from units where path=? and line>318 order by line limit 1',
                 (PATH,)).fetchone()
ck('confine misurato: riga 319, DESCRIPTION di outfit:Afterburner (Planetary Class), una riga dopo',
   nxt == (319, 'DESCRIPTION', 'outfit:Afterburner (Planetary Class)'), nxt)
ck('il confine SPEZZA la scheda: l\'ultima unita\' del lotto e la prima dopo hanno lo stesso contesto',
   tu[14]['context'] == nxt[2] == 'outfit:Afterburner (Planetary Class)')
ck('il file intero: 92 unita, righe 16 - 908',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (92, 16, 908))
ck('lotto + residuo = file: 20 + 15 + 57 = 92',
   20 + len(tu) + db.execute('select count(*) from units where path=? and line>318',
                             (PATH,)).fetchone()[0] == 92)
ck('tipi del lotto: 11 DESCRIPTION, 4 VALUE',
   collections.Counter(u['kind'] for u in su) == {'DESCRIPTION': 11, 'VALUE': 4})
ck('4 identiche (tutti e soli i VALUE) e 11 tradotte (tutte e sole le DESCRIPTION)',
   sum(1 for u in tu if u['italian'] == u['english']) == 4
   and sorted(u['idx'] for u in tu if u['italian'] == u['english'])
   == sorted(u['idx'] for u in tu if u['kind'] == 'VALUE')
   and sorted(u['idx'] for u in tu if u['italian'] != u['english'])
   == sorted(u['idx'] for u in tu if u['kind'] == 'DESCRIPTION'))
ck('3 tab (unita\' 7, 10, 13) e 0 virgolette, in inglese e in italiano',
   [u['idx'] for u in tu if TAB in u['italian']] == [7, 10, 13]
   and sum(u['english'].count(QUOTE) for u in su) == 0 == sum(u['italian'].count(QUOTE) for u in tu))
ck('la 10 e la 13 sono identiche; la 7 ha il `may` in piu\' reso con «può quasi fondere»',
   tu[9]['italian'] == tu[12]['italian']
   and tu[6]['italian'] == tu[9]['italian'].replace('che quasi fonde', 'che può quasi fondere'))
ck('0 segnaposto', sum(len(TAG.findall(u['english'])) for u in su) == 0
   == sum(len(TAG.findall(u['italian'])) for u in tu))
ck('PENDING su tutte e 15', not [u['idx'] for u in su
                                 if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('nessuno spazio finale e nessun doppio spazio (tab iniziali ammessi)',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip()
        or '  ' in u['italian'].strip(TAB)])
ck('nessun carattere tipografico e nessun non latino',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')
        or any(ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F for c in u['italian'])])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate 0,55-1,90 (1,00 - 1,21; 431 -> 442 parole)',
   0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('APERTO: 35/92 unita\' del file (20 + 15) · restano 57 dopo la 318 · confine riga 319 (DESCRIPTION)')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L229 superato' if not fail else 'verify L229 fallito')
raise SystemExit(0 if not fail else 1)
