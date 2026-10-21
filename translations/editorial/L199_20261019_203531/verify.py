r"""verify.py — L199 (`data/hai/hai jobs.txt`, 26 unita', righe 1579-1750). Quarto lotto; il file resta aperto.

**Invariante delle finestre, a quattro reali + una pianificata**: L196, L197, L198 e L199 esistono come
`translation.json`, L200 no. La somma deve dare **175 unita' su 175 righe distinte**, esattamente le righe del DB,
senza buchi, `min(line) = 15`, `max(line) = 2067`.

**Confine nuovo**: la prima unita' dopo la 1750 e' la riga **1753**, una `DESCRIPTION` che appartiene alla
**stessa** missione dell'ultima unita' del lotto (`Superstitious Hai [1]`, riga 1750, `VALUE`). E' il primo confine
del file che **non** chiude una missione: il controllo misura l'identita' del contesto e la differenza del tipo,
invece di assumere che il confine separi due missioni.
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
PATH = 'data/hai/hai jobs.txt'
REAL = [('L196_20261019_200808', 39), ('L197_20261019_202004', 36),
        ('L198_20261019_202701', 51), ('L199_20261019_203531', 26)]
PLANNED = [('L200', 1753, 2067, 23)]
su = sorted(json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
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
ck('unita: 26 righe 1579 - 1750', len(tu) == 26 and (tu[0]['line'], tu[-1]['line']) == (1579, 1750))
ck('126 unita prima della 1579, coperte da L196+L197+L198', db.execute(
    'select count(*) from units where path=? and line<1579', (PATH,)).fetchone()[0] == 126)
ck('23 unita dopo la 1750 (49 - 26)', db.execute(
    'select count(*) from units where path=? and line>1750', (PATH,)).fetchone()[0] == 23)
nxt = db.execute('select line,kind,context from units where path=? and line>1750 order by line limit 1',
                 (PATH,)).fetchone()
ck('confine misurato: riga 1753, DESCRIPTION di "Superstitious Hai [1]"',
   nxt == (1753, 'DESCRIPTION', 'mission:Superstitious Hai [1]'), nxt)
ck("il confine NON chiude la missione: stesso contesto dell'unita 26 (riga 1750, VALUE)",
   nxt is not None and nxt[2] == su[-1]['context'] and nxt[1] != su[-1]['kind'],
   (nxt[2] if nxt else None, su[-1]['context'], nxt[1] if nxt else None, su[-1]['kind']))
ck('il file intero: 175 unita, min(line) 15, max(line) 2067',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (175, 15, 2067),
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone())
allu, per_win = [], {}
for w, n in REAL:
    d = json.load(open(os.path.join(ED, w, 'translation.json'), encoding='utf-8'))['units']
    per_win[w] = len(d)
    allu += [(w, u['line']) for u in d if u['path'] == PATH]
ck('quattro finestre reali: L196 39, L197 36, L198 51, L199 26', list(per_win.values()) == [39, 36, 51, 26], per_win)
for w, a, b, n in PLANNED:
    c = db.execute('select count(*) from units where path=? and line between ? and ?', (PATH, a, b)).fetchone()[0]
    allu += [(w, r[0]) for r in db.execute('select line from units where path=? and line between ? and ?', (PATH, a, b))]
    per_win[w] = (c, n)
ck('una finestra pianificata con le unita dichiarate (1753-2067 23)',
   per_win['L200'] == (23, 23), per_win['L200'])
ck('somma delle 5 finestre = 175 unita', len(allu) == 175, len(allu))
ck('175 righe DISTINTE (nessuna riga rivendicata due volte)', len({l for _, l in allu}) == 175,
   len({l for _, l in allu}))
dbl = {r[0] for r in db.execute('select line from units where path=?', (PATH,))}
ck('le 5 finestre coprono ESATTAMENTE le righe del DB (nessun buco)',
   {l for _, l in allu} == dbl, sorted(dbl - {l for _, l in allu})[:5])
ck('tipi del lotto: 9 VALUE, 8 DESCRIPTION, 9 DIALOG',
   collections.Counter(u['kind'] for u in su) == {'VALUE': 9, 'DESCRIPTION': 8, 'DIALOG': 9})
ck('0 tab, 0 virgolette, 42 segnaposto su 3 simboli',
   sum(u['english'].count(TAB) for u in su) == 0
   and sum(u['english'].count('"') for u in su) == 0 == sum(u['italian'].count('"') for u in tu)
   and sum(u['english'].count('<') for u in su) == 42 == sum(u['italian'].count('<') for u in tu))
ck("2 apici inglesi e 0 italiani (possessivo 's senza equivalente)",
   sum(u['english'].count(chr(39)) for u in su) == 2
   and sum(u['italian'].count(chr(39)) for u in tu) == 0)
ck('9 VALUE restano inglesi alla lettera', all(u['italian'] == u['english'] for u in tu if u['kind'] == 'VALUE'))
ck('PENDING su tutte e 26', not [u['idx'] for u in su
                                 if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('nessun carattere tipografico e nessun non latino',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')
        or any(ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F for c in u['italian'])])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate 0,55-1,90', 0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('APERTO: 152/175 unita del file (86.9%) · 23 dopo la riga 1750 · confine riga 1753 (stessa missione)')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L199 superato' if not fail else 'verify L199 fallito')
raise SystemExit(0 if not fail else 1)
