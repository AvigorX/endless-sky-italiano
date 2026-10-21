r"""verify.py — L200 (`data/hai/hai jobs.txt`, 23 unita', righe 1753-2067). **LOTTO TERMINALE: CHIUDE IL FILE.**

Invariante di **FILE**: le **5 finestre** (L196…L200) devono coprire **tutte e 175** le unita' del database, su **175
righe distinte**, `min(line) = 15`, `max(line) = 2067`. Lotto terminale: **nessuna unita'** dopo la 2067.

Le altre quattro finestre sono lette dal loro `translation.json` (non dai numeri del contratto): se una finestra
precedente fosse stata alterata, la somma non tornerebbe.
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
WINDOWS = ['L196_20261019_200808', 'L197_20261019_202004', 'L198_20261019_202701',
           'L199_20261019_203531', 'L200_20261019_204235']
su = sorted(json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
fail = []


def ck(n, c, d=''):
    print('%-72s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente (23/23)', not [u for u in su if lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck('unita: 23 righe 1753 - 2067', len(tu) == 23 and (tu[0]['line'], tu[-1]['line']) == (1753, 2067))
ck('152 unita prima della 1753, coperte da L196…L199', db.execute(
    'select count(*) from units where path=? and line<1753', (PATH,)).fetchone()[0] == 152)
ck("lotto TERMINALE: nessuna unita' dopo la riga 2067", db.execute(
    'select count(*) from units where path=? and line>2067', (PATH,)).fetchone()[0] == 0)
ck('il file intero: 175 unita, min(line) 15, max(line) 2067',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (175, 15, 2067),
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone())

allu, per_win = [], {}
for w in WINDOWS:
    d = json.load(open(os.path.join(ED, w, 'translation.json'), encoding='utf-8'))['units']
    per_win[w] = len(d)
    allu += [(w, u['line']) for u in d if u['path'] == PATH]
ck('5 finestre: L196 39, L197 36, L198 51, L199 26, L200 23',
   list(per_win.values()) == [39, 36, 51, 26, 23], per_win)
ck('somma delle finestre = 175 unita', len(allu) == 175, len(allu))
ck('175 righe DISTINTE (nessuna rivendicata due volte)', len({l for _, l in allu}) == 175,
   len({l for _, l in allu}))
dbl = {r[0] for r in db.execute('select line from units where path=?', (PATH,))}
ck('le 175 righe sono ESATTAMENTE quelle del database (nessun buco)',
   {l for _, l in allu} == dbl, sorted(dbl - {l for _, l in allu})[:5])
ck('tipi del lotto: 11 VALUE, 12 DESCRIPTION, 0 DIALOG',
   collections.Counter(u['kind'] for u in su) == {'VALUE': 11, 'DESCRIPTION': 12})
ck('0 tab, 0 virgolette, 0 apici, 57 segnaposto su 5 simboli',
   sum(u['english'].count(TAB) for u in su) == 0
   and sum(u['english'].count('"') for u in su) == 0 == sum(u['italian'].count('"') for u in tu)
   and sum(u['english'].count(chr(39)) for u in su) == 0 == sum(u['italian'].count(chr(39)) for u in tu)
   and sum(u['english'].count('<') for u in su) == 57 == sum(u['italian'].count('<') for u in tu))
ck('11 VALUE restano inglesi alla lettera', all(u['italian'] == u['english'] for u in tu if u['kind'] == 'VALUE'))
ck('PENDING su tutte e 23', not [u['idx'] for u in su
                                 if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('nessun carattere tipografico e nessun non latino',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')
        or any(ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F for c in u['italian'])])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate 0,55-1,90', 0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('FILE CHIUSO: 175/175 unita (100%) in 5 finestre · 23 nel lotto · 0 dopo la riga 2067')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L200 superato' if not fail else 'verify L200 fallito')
raise SystemExit(0 if not fail else 1)
