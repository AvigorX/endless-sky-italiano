r"""verify.py — L197 (`data/hai/hai jobs.txt`, 36 unita', righe 492-967). Secondo lotto; il file resta aperto.

**Invariante delle finestre, a due stati**: L196 e L197 esistono come `translation.json`, L198…L200 no. Il
controllo somma le **due finestre reali** con le **tre pianificate lette dal database** e pretende:
175 unita', 175 righe distinte, esattamente le righe del DB, nessun buco, `min(line) = 15`, `max(line) = 2067`.

Il **confine** e' misurato: la prima unita' dopo la 967 e' la riga **988**, una `DIALOG` del contesto
`mission:Transport Hai farmers to <planet>`.
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
REAL = [('L196_20261019_200808', 39), ('L197_20261019_202004', 36)]
PLANNED = [('L198', 988, 1565, 51), ('L199', 1579, 1750, 26), ('L200', 1753, 2067, 23)]
su = sorted(json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
fail = []


def ck(n, c, d=''):
    print('%-72s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente (36/36)', not [u for u in su if lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck('unita: 36 righe 492 - 967', len(tu) == 36 and (tu[0]['line'], tu[-1]['line']) == (492, 967))
ck('39 unita prima della 492, coperte da L196', db.execute(
    'select count(*) from units where path=? and line<492', (PATH,)).fetchone()[0] == 39)
ck('100 unita dopo la 967 (136 - 36)', db.execute(
    'select count(*) from units where path=? and line>967', (PATH,)).fetchone()[0] == 100)
nxt = db.execute('select line,kind,context from units where path=? and line>967 order by line limit 1',
                 (PATH,)).fetchone()
ck('confine misurato: riga 988, DIALOG di "Transport Hai farmers to <planet>"',
   nxt == (988, 'DIALOG', 'mission:Transport Hai farmers to <planet>'), nxt)
ck('il file intero: 175 unita, min(line) 15, max(line) 2067',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (175, 15, 2067),
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone())
allu, per_win = [], {}
for w, n in REAL:
    d = json.load(open(os.path.join(ED, w, 'translation.json'), encoding='utf-8'))['units']
    per_win[w] = len(d)
    allu += [(w, u['line']) for u in d if u['path'] == PATH]
ck('due finestre reali: L196 39, L197 36', list(per_win.values()) == [39, 36], per_win)
for w, a, b, n in PLANNED:
    c = db.execute('select count(*) from units where path=? and line between ? and ?', (PATH, a, b)).fetchone()[0]
    allu += [(w, r[0]) for r in db.execute('select line from units where path=? and line between ? and ?', (PATH, a, b))]
    per_win[w] = (c, n)
ck('tre finestre pianificate con le unita dichiarate (988-1565 51, 1579-1750 26, 1753-2067 23)',
   all(per_win[w] == (n, n) for w, a, b, n in PLANNED), {w: per_win[w] for w, a, b, n in PLANNED})
ck('somma delle 5 finestre = 175 unita', len(allu) == 175, len(allu))
ck('175 righe DISTINTE (nessuna riga rivendicata due volte)', len({l for _, l in allu}) == 175,
   len({l for _, l in allu}))
dbl = {r[0] for r in db.execute('select line from units where path=?', (PATH,))}
ck('le 5 finestre coprono ESATTAMENTE le righe del DB (nessun buco)',
   {l for _, l in allu} == dbl, sorted(dbl - {l for _, l in allu})[:5])
ck('tipi del lotto: 12 VALUE, 15 DESCRIPTION, 9 DIALOG',
   collections.Counter(u['kind'] for u in su) == {'VALUE': 12, 'DESCRIPTION': 15, 'DIALOG': 9})
ck('0 tab, 0 virgolette, 0 apici, 81 segnaposto su 11 simboli',
   sum(u['english'].count(TAB) for u in su) == 0
   and sum(u['english'].count('"') for u in su) == 0 == sum(u['italian'].count('"') for u in tu)
   and sum(u['english'].count(chr(39)) for u in su) == 0 == sum(u['italian'].count(chr(39)) for u in tu)
   and sum(u['english'].count('<') for u in su) == 81 == sum(u['italian'].count('<') for u in tu))
ck('12 VALUE restano inglesi alla lettera', all(u['italian'] == u['english'] for u in tu if u['kind'] == 'VALUE'))
ck('PENDING su tutte e 36', not [u['idx'] for u in su
                                 if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('nessun carattere tipografico e nessun non latino',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')
        or any(ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F for c in u['italian'])])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate 0,55-1,90', 0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('APERTO: 75/175 unita del file (42.9%) · 100 dopo la riga 967 · confine riga 988')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L197 superato' if not fail else 'verify L197 fallito')
raise SystemExit(0 if not fail else 1)
