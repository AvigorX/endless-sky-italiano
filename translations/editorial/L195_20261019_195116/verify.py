r"""verify.py — L195 (`data/bunrodea/bunrodea missions.txt`, 5 unita', righe 207-219). **CHIUDE IL FILE: 77/77.**

Invariante di **FILE**: le **5 finestre** (L191…L195) devono coprire **tutte e 77** le unita' del database, su **77 righe
distinte**, `min(line) = 16`, `max(line) = 219`. Lotto terminale: **nessuna unita'** dopo la 219.
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
PATH = 'data/bunrodea/bunrodea missions.txt'
WINDOWS = ['L191_20261019_194730', 'L192_20261019_194838', 'L193_20261019_194924',
           'L194_20261019_195024', 'L195_20261019_195116']
su = sorted(json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
by = {u['idx']: u for u in tu}
lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
fail = []


def ck(n, c, d=''):
    print('%-70s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente (5/5)', not [u for u in su if lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck('unita: 5 righe 207 - 219', len(tu) == 5 and (tu[0]['line'], tu[-1]['line']) == (207, 219))
ck('le 72 unita precedenti sono coperte da L191…L194', db.execute(
    'select count(*) from units where path=? and line<207', (PATH,)).fetchone()[0] == 72)

allu, per_win = [], {}
for w in WINDOWS:
    d = json.load(open(os.path.join(ED, w, 'translation.json'), encoding='utf-8'))['units']
    per_win[w] = len(d)
    allu += [(w, u['line']) for u in d if u['path'] == PATH]
ck('5 finestre: L191 12, L192 12, L193 30, L194 18, L195 5',
   list(per_win.values()) == [12, 12, 30, 18, 5], per_win)
ck('somma delle finestre = 77 unita', len(allu) == 77, len(allu))
ck('77 righe DISTINTE (nessuna rivendicata due volte)', len({l for _, l in allu}) == 77,
   len({l for _, l in allu}))
dbl = {r[0] for r in db.execute('select line from units where path=?', (PATH,))}
ck('le 77 righe sono ESATTAMENTE quelle del database (nessun buco)',
   {l for _, l in allu} == dbl, sorted(dbl - {l for _, l in allu})[:5])
ck('min(line) = 16 e max(line) = 219 su tutto il file',
   db.execute('select min(line),max(line) from units where path=?', (PATH,)).fetchone() == (16, 219))
ck("lotto TERMINALE: nessuna unita' dopo la riga 219",
   db.execute('select count(*) from units where path=? and line>219', (PATH,)).fetchone()[0] == 0)
ck('tipi del lotto: 5 MISSION_TEXT', collections.Counter(u['kind'] for u in su) == {'MISSION_TEXT': 5})
ck('5 tab, 10 virgolette, 0 segnaposto',
   [u['idx'] for u in su if u['english'].startswith(TAB)] == list(range(1, 6))
   and sum(u['english'].count('"') for u in su) == 10 == sum(u['italian'].count('"') for u in tu))
ck('le tre varianti condividono la coda della resa',
   len({by[i]['italian'].split('Alle mie guardie')[1] for i in (2, 3, 4)}) == 1)
ck('PENDING su tutte e 5', not [u['idx'] for u in su
                                if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('nessuno spazio finale (tab iniziali ammessi)',
   not [u['idx'] for u in tu if u['english'].rstrip(TAB) != u['english'].rstrip(TAB).rstrip()
        or u['italian'].rstrip(TAB) != u['italian'].rstrip(TAB).rstrip()])
ck('nessun carattere tipografico e nessun non latino',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')
        or any(ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F for c in u['italian'])])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate', 0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('FILE CHIUSO: 77/77 unita (100%) in 5 finestre · 5 nel lotto · 0 dopo la riga 219')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L195 superato' if not fail else 'verify L195 fallito')
raise SystemExit(0 if not fail else 1)
