r"""verify.py — L203 (`data/hai/hai outfits.txt`, 9 unita', righe 508-600). Terzo lotto; il file resta aperto.

Il file ha ora **tre finestre reali** (L201 8, L202 16, L203 9) e **32 unita' residue**.

**Confine nuovo**: la prima unita' dopo la 600 e' la riga **603**, che e' un **`VALUE`** (`Hai Chasm Batteries`) e non
una `DESCRIPTION` come in L201 e L202. Il controllo verifica **riga, tipo e contesto**: il tipo non si eredita dal lotto
precedente.
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
ED = os.path.join(L10N, 'staging/editorial')
PATH = 'data/hai/hai outfits.txt'
REAL = [('L201_20261019_204959', 8), ('L202_20261019_205624', 16), ('L203_20261019_210258', 9)]
su = sorted(json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
fail = []


def ck(n, c, d=''):
    print('%-72s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente (9/9)', not [u for u in su if lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck('unita: 9 righe 508 - 600', len(tu) == 9 and (tu[0]['line'], tu[-1]['line']) == (508, 600))
ck('24 unita prima della 508, coperte da L201+L202', db.execute(
    'select count(*) from units where path=? and line<508', (PATH,)).fetchone()[0] == 24)
ck('32 unita dopo la 600 (41 - 9)', db.execute(
    'select count(*) from units where path=? and line>600', (PATH,)).fetchone()[0] == 32)
nxt = db.execute('select line,kind,context from units where path=? and line>600 order by line limit 1',
                 (PATH,)).fetchone()
ck('confine misurato: riga 603, VALUE di "Hai Chasm Batteries" (il confine e\' un VALUE, non una DESCRIPTION)',
   nxt == (603, 'VALUE', 'outfit:Hai Chasm Batteries'), nxt)
ck('il file intero: 65 unita, min(line) 27, max(line) 984',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (65, 27, 984),
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone())
allu, per_win = [], {}
for w, n in REAL:
    d = json.load(open(os.path.join(ED, w, 'translation.json'), encoding='utf-8'))['units']
    per_win[w] = len(d)
    allu += [(w, u['line']) for u in d if u['path'] == PATH]
ck('tre finestre reali: L201 8, L202 16, L203 9', list(per_win.values()) == [8, 16, 9], per_win)
rest = {r[0] for r in db.execute('select line from units where path=? and line>600', (PATH,))}
ck('somma: 8 + 16 + 9 + residuo 32 = 65 unita', len(allu) + len(rest) == 65, (len(allu), len(rest)))
ck('65 righe DISTINTE (nessuna rivendicata due volte)',
   len({l for _, l in allu} | rest) == 65 and len({l for _, l in allu} & rest) == 0,
   (len({l for _, l in allu} | rest), len({l for _, l in allu} & rest)))
dbl = {r[0] for r in db.execute('select line from units where path=?', (PATH,))}
ck('le finestre + residuo coprono ESATTAMENTE le righe del DB (nessun buco)',
   ({l for _, l in allu} | rest) == dbl, sorted(dbl - ({l for _, l in allu} | rest))[:5])
ck('tipi del lotto: 9 DESCRIPTION', collections.Counter(u['kind'] for u in su) == {'DESCRIPTION': 9})
ck('0 segnaposto, 1 tab, 0 virgolette, 1 apice EN / 4 IT',
   sum(u['english'].count('<') for u in su) == 0 == sum(u['italian'].count('<') for u in tu)
   and [u['idx'] for u in su if u['english'].startswith(TAB)] == [8]
   and sum(u['english'].count('"') for u in su) == 0 == sum(u['italian'].count('"') for u in tu)
   and sum(u['english'].count(chr(39)) for u in su) == 1
   and sum(u['italian'].count(chr(39)) for u in tu) == 4)
ck('PENDING su tutte e 9', not [u['idx'] for u in su
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
print('APERTO: 33/65 unita del file (50.8%) · 32 dopo la riga 600 · confine riga 603 (VALUE)')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L203 superato' if not fail else 'verify L203 fallito')
raise SystemExit(0 if not fail else 1)
