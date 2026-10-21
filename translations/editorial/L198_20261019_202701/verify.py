r"""verify.py — L198 (`data/hai/hai jobs.txt`, 51 unita', righe 988-1565). Terzo lotto; il file resta aperto.

**Invariante delle finestre, a tre reali + due pianificate**: L196, L197 e L198 esistono come
`translation.json`; L199 e L200 no. La somma deve dare **175 unita' su 175 righe distinte**, esattamente le
righe del DB, senza buchi, `min(line) = 15`, `max(line) = 2067`.

Il **confine** e' misurato: la prima unita' dopo la 1565 e' la riga **1579**, una `DIALOG` del contesto
`mission:Swiftsong Business Convention [2]`.
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
REAL = [('L196_20261019_200808', 39), ('L197_20261019_202004', 36), ('L198_20261019_202701', 51)]
PLANNED = [('L199', 1579, 1750, 26), ('L200', 1753, 2067, 23)]
su = sorted(json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
fail = []


def ck(n, c, d=''):
    print('%-72s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente (51/51)', not [u for u in su if lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck('unita: 51 righe 988 - 1565', len(tu) == 51 and (tu[0]['line'], tu[-1]['line']) == (988, 1565))
ck('75 unita prima della 988, coperte da L196+L197', db.execute(
    'select count(*) from units where path=? and line<988', (PATH,)).fetchone()[0] == 75)
ck('49 unita dopo la 1565 (100 - 51)', db.execute(
    'select count(*) from units where path=? and line>1565', (PATH,)).fetchone()[0] == 49)
nxt = db.execute('select line,kind,context from units where path=? and line>1565 order by line limit 1',
                 (PATH,)).fetchone()
ck('confine misurato: riga 1579, DIALOG di "Swiftsong Business Convention [2]"',
   nxt == (1579, 'DIALOG', 'mission:Swiftsong Business Convention [2]'), nxt)
ck('il file intero: 175 unita, min(line) 15, max(line) 2067',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (175, 15, 2067),
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone())
allu, per_win = [], {}
for w, n in REAL:
    d = json.load(open(os.path.join(ED, w, 'translation.json'), encoding='utf-8'))['units']
    per_win[w] = len(d)
    allu += [(w, u['line']) for u in d if u['path'] == PATH]
ck('tre finestre reali: L196 39, L197 36, L198 51', list(per_win.values()) == [39, 36, 51], per_win)
for w, a, b, n in PLANNED:
    c = db.execute('select count(*) from units where path=? and line between ? and ?', (PATH, a, b)).fetchone()[0]
    allu += [(w, r[0]) for r in db.execute('select line from units where path=? and line between ? and ?', (PATH, a, b))]
    per_win[w] = (c, n)
ck('due finestre pianificate con le unita dichiarate (1579-1750 26, 1753-2067 23)',
   all(per_win[w] == (n, n) for w, a, b, n in PLANNED), {w: per_win[w] for w, a, b, n in PLANNED})
ck('somma delle 5 finestre = 175 unita', len(allu) == 175, len(allu))
ck('175 righe DISTINTE (nessuna riga rivendicata due volte)', len({l for _, l in allu}) == 175,
   len({l for _, l in allu}))
dbl = {r[0] for r in db.execute('select line from units where path=?', (PATH,))}
ck('le 5 finestre coprono ESATTAMENTE le righe del DB (nessun buco)',
   {l for _, l in allu} == dbl, sorted(dbl - {l for _, l in allu})[:5])
ck('tipi del lotto: 22 VALUE, 24 DESCRIPTION, 5 DIALOG',
   collections.Counter(u['kind'] for u in su) == {'VALUE': 22, 'DESCRIPTION': 24, 'DIALOG': 5})
ck('0 tab, 2 virgolette in entrambe le lingue, 112 segnaposto su 7 simboli',
   sum(u['english'].count(TAB) for u in su) == 0
   and sum(u['english'].count('"') for u in su) == 2 == sum(u['italian'].count('"') for u in tu)
   and sum(u['english'].count('<') for u in su) == 112 == sum(u['italian'].count('<') for u in tu))
ck('1 apice inglese e 3 italiani (causa: elisione italiana)',
   sum(u['english'].count(chr(39)) for u in su) == 1
   and sum(u['italian'].count(chr(39)) for u in tu) == 3)
ck('22 VALUE restano inglesi alla lettera', all(u['italian'] == u['english'] for u in tu if u['kind'] == 'VALUE'))
ck('PENDING su tutte e 51', not [u['idx'] for u in su
                                 if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('nessun carattere tipografico e nessun non latino',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')
        or any(ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F for c in u['italian'])])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate 0,55-1,90', 0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('APERTO: 126/175 unita del file (72.0%) · 49 dopo la riga 1565 · confine riga 1579')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L198 superato' if not fail else 'verify L198 fallito')
raise SystemExit(0 if not fail else 1)
