r"""verify.py — L201 (`data/hai/hai outfits.txt`, 8 unita', righe 27-164). **APRE IL FILE**; non lo chiude.

Non e' un lotto terminale: le finestre successive di `hai outfits.txt` non esistono ancora. Si verificano percio'
**quattro invarianti misurate sul database**:

1. **0 unita' prima della riga 27** — il lotto apre davvero il file;
2. **57 unita' dopo la riga 164** (65 - 8) — il residuo del file e' quello dichiarato;
3. **il file intero**: 65 unita', `min(line) = 27`, `max(line) = 984`;
4. **righe del lotto e righe residue sono disgiunte e la loro somma e' 65** — nessuna riga rivendicata due volte.

Il **confine** e' misurato: la prima unita' dopo la 164 e' la riga **205**, una `DESCRIPTION` del contesto
`outfit:Ionic Blaster Prototype`.
"""
import collections
import hashlib
import json
import os
import sqlite3

TAB = chr(9)
HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
ROOT = os.path.abspath(os.path.join(L10N, '..'))
PATH = 'data/hai/hai outfits.txt'
su = sorted(json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
fail = []


def ck(n, c, d=''):
    print('%-72s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente (8/8)', not [u for u in su if lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck('unita: 8 righe 27 - 164', len(tu) == 8 and (tu[0]['line'], tu[-1]['line']) == (27, 164))
ck('il lotto APRE il file: 0 unita prima della riga 27',
   db.execute('select count(*) from units where path=? and line<27', (PATH,)).fetchone()[0] == 0)
ck('57 unita dopo la riga 164 (65 - 8)', db.execute(
    'select count(*) from units where path=? and line>164', (PATH,)).fetchone()[0] == 57)
nxt = db.execute('select line,kind,context from units where path=? and line>164 order by line limit 1',
                 (PATH,)).fetchone()
ck('confine misurato: riga 205, DESCRIPTION di "Ionic Blaster Prototype"',
   nxt == (205, 'DESCRIPTION', 'outfit:Ionic Blaster Prototype'), nxt)
ck('il file intero: 65 unita, min(line) 27, max(line) 984',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (65, 27, 984),
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone())
lot = {u['line'] for u in tu}
rest = {r[0] for r in db.execute('select line from units where path=? and line>164', (PATH,))}
ck('righe del lotto e righe residue sono DISGIUNTE', not (lot & rest), sorted(lot & rest)[:5])
ck('lotto (8) + residuo (57) = 65 righe = tutto il file',
   len(lot) == 8 and len(rest) == 57 and len(lot | rest) == 65, (len(lot), len(rest), len(lot | rest)))
ck('tipi del lotto: 8 DESCRIPTION', collections.Counter(u['kind'] for u in su) == {'DESCRIPTION': 8})
ck('0 segnaposto, 2 tab, 2 virgolette, 0 apici EN / 5 IT',
   sum(u['english'].count('<') for u in su) == 0 == sum(u['italian'].count('<') for u in tu)
   and [u['idx'] for u in su if u['english'].startswith(TAB)] == [3, 4]
   and sum(u['english'].count('"') for u in su) == 2 == sum(u['italian'].count('"') for u in tu)
   and sum(u['english'].count(chr(39)) for u in su) == 0
   and sum(u['italian'].count(chr(39)) for u in tu) == 5)
ck('PENDING su tutte e 8', not [u['idx'] for u in su
                                if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('nessuno spazio finale e nessun doppio spazio (tab iniziali ammessi)',
   not [u['idx'] for u in tu if u['italian'].rstrip(TAB) != u['italian'].rstrip(TAB).rstrip()
        or '  ' in u['italian']])
ck('nessun carattere tipografico e nessun non latino',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')
        or any(ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F for c in u['italian'])])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate 0,55-1,90', 0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('APERTO: 8/65 unita del file (12.3%) · 57 dopo la riga 164 · confine riga 205')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L201 superato' if not fail else 'verify L201 fallito')
raise SystemExit(0 if not fail else 1)
