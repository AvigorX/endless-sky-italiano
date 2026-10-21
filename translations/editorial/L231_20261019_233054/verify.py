r"""verify.py — L231 (`data/korath/korath outfits.txt`, 21 unita', righe 596-808). Quarto lotto del file.

Quarto lotto: **61** unita' gia' tradotte prima della 596 (L228 20 + L229 15 + L230 26), **21** in questo, **10** dopo la
808.

    61 + 21 + 10 = 92  (le unita' del file)

Confine: riga **809**, una **`DESCRIPTION`** di `outfit:Nelmeb GP Hybrid Thruster` — la **seconda parte** della scheda il cui
primo paragrafo chiude questo lotto (riga 808). Il controllo verifica che il contesto dell'ultima unita' del lotto sia lo
stesso della prima unita' esclusa.

**Il residuo e' di 10 unita', tutte `DESCRIPTION`**: L232 chiudera' il file con **0 identiche / 10 tradotte**.
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


ck('riga grezza identica al sorgente (21/21)', not [u for u in su if lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck('unita: 21 righe 596 - 808', len(tu) == 21 and (tu[0]['line'], tu[-1]['line']) == (596, 808))
ck('61 unita tradotte prima della 596 (20+15+26)', db.execute(
    'select count(*) from units where path=? and line<596', (PATH,)).fetchone()[0] == 61)
ck('10 unita dopo la 808 (92 - 82)', db.execute(
    'select count(*) from units where path=? and line>808', (PATH,)).fetchone()[0] == 10)
nxt = db.execute('select line,kind,context from units where path=? and line>808 order by line limit 1',
                 (PATH,)).fetchone()
ck('confine misurato: riga 809, DESCRIPTION di outfit:Nelmeb GP Hybrid Thruster, una riga dopo',
   nxt == (809, 'DESCRIPTION', 'outfit:Nelmeb GP Hybrid Thruster'), nxt)
ck('il confine SPEZZA la scheda: l\'ultima unita\' del lotto e la prima dopo hanno lo stesso contesto',
   tu[20]['context'] == nxt[2] == 'outfit:Nelmeb GP Hybrid Thruster')
ck('il residuo e\' di 10 unita\' TUTTE DESCRIPTION: L232 chiudera\' il file con 0 identiche / 10 tradotte',
   db.execute('select count(*) from units where path=? and line>808 and kind="DESCRIPTION"',
              (PATH,)).fetchone()[0] == 10
   and db.execute('select count(*) from units where path=? and line>808 and kind="VALUE"',
                  (PATH,)).fetchone()[0] == 0)
ck('il file intero: 92 unita, righe 16 - 908',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (92, 16, 908))
ck('lotto + residuo = file: 61 + 21 + 10 = 92',
   61 + len(tu) + db.execute('select count(*) from units where path=? and line>808',
                             (PATH,)).fetchone()[0] == 92)
ck('tipi del lotto: 13 DESCRIPTION, 8 VALUE',
   collections.Counter(u['kind'] for u in su) == {'DESCRIPTION': 13, 'VALUE': 8})
ck('8 identiche (tutti e soli i VALUE) e 13 tradotte (tutte e sole le DESCRIPTION)',
   sum(1 for u in tu if u['italian'] == u['english']) == 8
   and sorted(u['idx'] for u in tu if u['italian'] == u['english'])
   == sorted(u['idx'] for u in tu if u['kind'] == 'VALUE')
   and sorted(u['idx'] for u in tu if u['italian'] != u['english'])
   == sorted(u['idx'] for u in tu if u['kind'] == 'DESCRIPTION'))
ck('ZERO tab e ZERO virgolette, in inglese e in italiano',
   sum(u['english'].count(TAB) for u in su) == 0 == sum(u['italian'].count(TAB) for u in tu)
   and sum(u['english'].count(QUOTE) for u in su) == 0 == sum(u['italian'].count(QUOTE) for u in tu))
ck('0 segnaposto', sum(len(TAG.findall(u['english'])) for u in su) == 0
   == sum(len(TAG.findall(u['italian'])) for u in tu))
ck('Quarg ed Efreti invariati (5 ciascuno) e thruster/steering resi con termini distinti',
   ' '.join(u['italian'] for u in tu).count('Quarg') == 5
   and ' '.join(u['italian'] for u in tu).count('Efreti') == 5
   and 'sistema di sterzata' in ' '.join(u['italian'] for u in tu))
ck('PENDING su tutte e 21', not [u['idx'] for u in su
                                 if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('nessun carattere tipografico e nessun non latino',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')
        or any(ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F for c in u['italian'])])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate 0,55-1,90 (1,04 - 1,37; 455 -> 498 parole)',
   0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('APERTO: 82/92 unita\' del file (61 + 21) · restano 10 dopo la 808 (tutte DESCRIPTION) · confine riga 809')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L231 superato' if not fail else 'verify L231 fallito')
raise SystemExit(0 if not fail else 1)
