r"""verify.py — L230 (`data/korath/korath outfits.txt`, 26 unita', righe 319-581). Terzo lotto del file.

Terzo lotto: **35** unita' gia' tradotte prima della 319 (L228 20 + L229 15), **26** in questo, **31** dopo la 581.

    35 + 26 + 31 = 92  (le unita' del file)

Confine: riga **596**, una **`DESCRIPTION`** di `outfit:Thruster (Comet Class)` — la **seconda parte** della scheda il cui
`VALUE` chiude questo lotto (riga 581). Il controllo verifica che il contesto dell'ultima unita' del lotto sia lo stesso
della prima unita' esclusa.

**La prima unita' e' la seconda parte** dell'`Afterburner (Planetary Class)` iniziato in L229: il suo testo e' identico a
quello di L229 unita' 10, e il controllo lo confronta con il `translation.json` del lotto precedente.
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
ED = os.path.join(L10N, 'staging/editorial')
PATH = 'data/korath/korath outfits.txt'
PREV = os.path.join(ED, 'L229_20261019_231932', 'translation.json')
su = sorted(json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
prev = {u['line']: u['italian'] for u in json.load(open(PREV, encoding='utf-8'))['units']}
fail = []


def ck(n, c, d=''):
    print('%-74s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente (26/26)', not [u for u in su if lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck('unita: 26 righe 319 - 581', len(tu) == 26 and (tu[0]['line'], tu[-1]['line']) == (319, 581))
ck('35 unita tradotte prima della 319 (L228 20 + L229 15)', db.execute(
    'select count(*) from units where path=? and line<319', (PATH,)).fetchone()[0] == 35)
ck('31 unita dopo la 581 (92 - 61)', db.execute(
    'select count(*) from units where path=? and line>581', (PATH,)).fetchone()[0] == 31)
nxt = db.execute('select line,kind,context from units where path=? and line>581 order by line limit 1',
                 (PATH,)).fetchone()
ck('confine misurato: riga 596, DESCRIPTION di outfit:Thruster (Comet Class), quindici righe dopo',
   nxt == (596, 'DESCRIPTION', 'outfit:Thruster (Comet Class)'), nxt)
ck('il confine SPEZZA la scheda: il VALUE finale del lotto e la DESCRIPTION dopo hanno lo stesso contesto',
   tu[25]['context'] == nxt[2] == 'outfit:Thruster (Comet Class)')
ck('la PRIMA unita\' e\' la seconda parte di una scheda di L229 e riusa la sua resa',
   tu[0]['context'] == 'outfit:Afterburner (Planetary Class)' and tu[0]['italian'] == prev[300])
ck('il file intero: 92 unita, righe 16 - 908',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (92, 16, 908))
ck('lotto + residuo = file: 35 + 26 + 31 = 92',
   35 + len(tu) + db.execute('select count(*) from units where path=? and line>581',
                             (PATH,)).fetchone()[0] == 92)
ck('tipi del lotto: 16 DESCRIPTION, 10 VALUE',
   collections.Counter(u['kind'] for u in su) == {'DESCRIPTION': 16, 'VALUE': 10})
ck('10 identiche (tutti e soli i VALUE) e 16 tradotte (tutte e sole le DESCRIPTION)',
   sum(1 for u in tu if u['italian'] == u['english']) == 10
   and sorted(u['idx'] for u in tu if u['italian'] == u['english'])
   == sorted(u['idx'] for u in tu if u['kind'] == 'VALUE')
   and sorted(u['idx'] for u in tu if u['italian'] != u['english'])
   == sorted(u['idx'] for u in tu if u['kind'] == 'DESCRIPTION'))
ck('7 tab e 0 virgolette, in inglese e in italiano',
   [u['idx'] for u in tu if TAB in u['italian']] == [1, 4, 11, 14, 17, 20, 23]
   and sum(u['english'].count(QUOTE) for u in su) == 0 == sum(u['italian'].count(QUOTE) for u in tu))
ck('le cinque copie (11, 14, 17, 20, 23) hanno una sola resa, e le unita\' 1 e 4 coincidono',
   len({tu[i]['italian'] for i in (10, 13, 16, 19, 22)}) == 1
   and tu[0]['italian'] == tu[3]['italian'])
ck('0 segnaposto', sum(len(TAG.findall(u['english'])) for u in su) == 0
   == sum(len(TAG.findall(u['italian'])) for u in tu))
ck('PENDING su tutte e 26', not [u['idx'] for u in su
                                 if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('nessuno spazio finale e nessun doppio spazio (tab iniziali ammessi)',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip()
        or '  ' in u['italian'].strip(TAB)])
ck('nessun carattere tipografico e nessun non latino',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')
        or any(ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F for c in u['italian'])])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate 0,55-1,90 (1,04 - 1,25; 430 -> 448 parole)',
   0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('APERTO: 61/92 unita\' del file (35 + 26) · restano 31 dopo la 581 · confine riga 596 (DESCRIPTION)')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L230 superato' if not fail else 'verify L230 fallito')
raise SystemExit(0 if not fail else 1)
