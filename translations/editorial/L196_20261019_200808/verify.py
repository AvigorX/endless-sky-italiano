r"""verify.py — L196 (`data/hai/hai jobs.txt`, 39 unita', righe 15-489). **APRE IL FILE: non lo chiude.**

Non e' un lotto terminale, quindi l'invariante di FILE non si applica ancora: le altre 4 finestre
(L197…L200) non esistono. Al suo posto si verificano **tre invarianti misurate sul database**:

1. **0 unita' prima della riga 15** — il lotto apre davvero il file (nessuna unita' orfana a monte);
2. **136 unita' dopo la riga 489** — il residuo del file e' quello dichiarato (175 - 15_righe - 39);
3. **il piano a 5 finestre copre il file senza buchi ne' sovrapposizioni**: le 5 finestre dichiarate nel
   contratto sommano **175** unita' su righe distinte, `min(line) = 15`, `max(line) = 2067`, contate sul DB.

Il **confine** e' misurato: la prima unita' dopo la 489 deve essere la riga **492**, un `DESCRIPTION` del
contesto `mission:Delivery to Human Space [2]`.
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
PATH = 'data/hai/hai jobs.txt'
# finestre dichiarate nel contratto (L196_... md, §3) — misurate qui contro il DB, non copiate come vere
PLAN = [('L196', 15, 489, 39), ('L197', 492, 967, 36), ('L198', 988, 1565, 51),
        ('L199', 1579, 1750, 26), ('L200', 1753, 2067, 23)]
su = sorted(json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
fail = []


def ck(n, c, d=''):
    print('%-72s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente (39/39)', not [u for u in su if lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck('unita: 39 righe 15 - 489', len(tu) == 39 and (tu[0]['line'], tu[-1]['line']) == (15, 489))
ck('il lotto APRE il file: 0 unita prima della riga 15',
   db.execute('select count(*) from units where path=? and line<15', (PATH,)).fetchone()[0] == 0)
ck('136 unita dopo la riga 489 (175 - 39)', db.execute(
    'select count(*) from units where path=? and line>489', (PATH,)).fetchone()[0] == 136)
nxt = db.execute('select line,kind,context from units where path=? and line>489 order by line limit 1',
                 (PATH,)).fetchone()
ck('confine misurato: riga 492, DESCRIPTION di "Delivery to Human Space [2]"',
   nxt == (492, 'DESCRIPTION', 'mission:Delivery to Human Space [2]'), nxt)
ck('il file intero: 175 unita, min(line) 15, max(line) 2067',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (175, 15, 2067),
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone())
per = [(w, db.execute('select count(*) from units where path=? and line between ? and ?', (PATH, a, b)).fetchone()[0], n)
       for w, a, b, n in PLAN]
ck('piano a 5 finestre: ogni finestra ha le unita dichiarate (15-489 39, 492-967 36, 988-1565 51, 1579-1750 26, 1753-2067 23)',
   [c for _, c, _ in per] == [n for *_, n in PLAN], [(w, c, n) for w, c, n in per])
ck('somma delle 5 finestre = 175 unita (tutto il file)',
   sum(c for _, c, _ in per) == 175, sum(c for _, c, _ in per))
rows = []
for w, a, b, n in PLAN:
    rows += [(r[0], w) for r in db.execute('select line from units where path=? and line between ? and ?', (PATH, a, b))]
ck('175 righe DISTINTE (nessuna riga rivendicata da due finestre)', len({l for l, _ in rows}) == 175,
   len({l for l, _ in rows}))
ck('le 5 finestre coprono ESATTAMENTE le righe del DB (nessun buco)',
   {l for l, _ in rows} == {r[0] for r in db.execute('select line from units where path=?', (PATH,))})
ck('tipi del lotto: 17 VALUE, 16 DESCRIPTION, 6 TEXT',
   collections.Counter(u['kind'] for u in su) == {'VALUE': 17, 'DESCRIPTION': 16, 'TEXT': 6})
ck('0 tab, 6 virgolette in inglese e 6 in italiano, 72 segnaposto',
   sum(u['english'].count(TAB) for u in su) == 0
   and sum(u['english'].count('"') for u in su) == 6 == sum(u['italian'].count('"') for u in tu)
   and sum(u['english'].count('<') for u in su) == 72
   and sum(u['italian'].count('<') for u in tu) == 72)
ck('17 VALUE restano inglesi alla lettera', all(u['italian'] == u['english'] for u in tu if u['kind'] == 'VALUE'))
ck('PENDING su tutte e 39', not [u['idx'] for u in su
                                 if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('nessun carattere tipografico e nessun non latino',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')
        or any(ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F for c in u['italian'])])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate 0,55-1,90', 0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('APERTO: 39/175 unita del file (22.3%) · 136 dopo la riga 489 · confine riga 492')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L196 superato' if not fail else 'verify L196 fallito')
raise SystemExit(0 if not fail else 1)
