r"""verify.py — L204 (`data/hai/hai outfits.txt`, 19 unita', righe 603-788). Quarto lotto; il file resta aperto.

Il file ha ora **quattro finestre reali** (L201 8, L202 16, L203 9, L204 19) e **13 unita' residue**.

Il **confine** e' misurato: la prima unita' dopo la 788 e' la riga **805**, una `DESCRIPTION` del contesto
`outfit:"Bondir" Atomic Thruster` — con **virgolette dentro il contesto**, che vanno confrontate alla lettera.
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
REAL = [('L201_20261019_204959', 8), ('L202_20261019_205624', 16),
        ('L203_20261019_210258', 9), ('L204_20261019_210851', 19)]
su = sorted(json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
fail = []


def ck(n, c, d=''):
    print('%-72s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente (19/19)', not [u for u in su if lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck('unita: 19 righe 603 - 788', len(tu) == 19 and (tu[0]['line'], tu[-1]['line']) == (603, 788))
ck('33 unita prima della 603, coperte da L201+L202+L203', db.execute(
    'select count(*) from units where path=? and line<603', (PATH,)).fetchone()[0] == 33)
ck('13 unita dopo la 788 (32 - 19)', db.execute(
    'select count(*) from units where path=? and line>788', (PATH,)).fetchone()[0] == 13)
nxt = db.execute('select line,kind,context from units where path=? and line>788 order by line limit 1',
                 (PATH,)).fetchone()
ck('confine misurato: riga 805, DESCRIPTION di \'"Bondir" Atomic Thruster\' (virgolette nel contesto)',
   nxt == (805, 'DESCRIPTION', 'outfit:"Bondir" Atomic Thruster'), nxt)
ck('il file intero: 65 unita, min(line) 27, max(line) 984',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (65, 27, 984),
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone())
allu, per_win = [], {}
for w, n in REAL:
    d = json.load(open(os.path.join(ED, w, 'translation.json'), encoding='utf-8'))['units']
    per_win[w] = len(d)
    allu += [(w, u['line']) for u in d if u['path'] == PATH]
ck('quattro finestre reali: 8, 16, 9, 19', list(per_win.values()) == [8, 16, 9, 19], per_win)
rest = {r[0] for r in db.execute('select line from units where path=? and line>788', (PATH,))}
ck('somma: 8 + 16 + 9 + 19 + residuo 13 = 65 unita', len(allu) + len(rest) == 65, (len(allu), len(rest)))
ck('65 righe DISTINTE (nessuna rivendicata due volte)',
   len({l for _, l in allu} | rest) == 65 and len({l for _, l in allu} & rest) == 0,
   (len({l for _, l in allu} | rest), len({l for _, l in allu} & rest)))
dbl = {r[0] for r in db.execute('select line from units where path=?', (PATH,))}
ck('le finestre + residuo coprono ESATTAMENTE le righe del DB (nessun buco)',
   ({l for _, l in allu} | rest) == dbl, sorted(dbl - ({l for _, l in allu} | rest))[:5])
ck('tipi del lotto: 13 DESCRIPTION, 6 VALUE',
   collections.Counter(u['kind'] for u in su) == {'DESCRIPTION': 13, 'VALUE': 6})
ck('0 segnaposto, 0 tab, 6 virgolette, 2 apici EN / 6 IT',
   sum(u['english'].count('<') for u in su) == 0 == sum(u['italian'].count('<') for u in tu)
   and sum(u['english'].count(TAB) for u in su) == 0 == sum(u['italian'].count(TAB) for u in tu)
   and sum(u['english'].count('"') for u in su) == 6 == sum(u['italian'].count('"') for u in tu)
   and sum(u['english'].count(chr(39)) for u in su) == 2
   and sum(u['italian'].count(chr(39)) for u in tu) == 6)
ck('6 VALUE restano inglesi alla lettera, virgolette comprese',
   all(u['italian'] == u['english'] for u in tu if u['kind'] == 'VALUE'))
ck('PENDING su tutte e 19', not [u['idx'] for u in su
                                 if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('nessun carattere tipografico e nessun non latino',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')
        or any(ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F for c in u['italian'])])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate 0,55-1,90', 0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('APERTO: 52/65 unita del file (80.0%) · 13 dopo la riga 788 · confine riga 805')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L204 superato' if not fail else 'verify L204 fallito')
raise SystemExit(0 if not fail else 1)
