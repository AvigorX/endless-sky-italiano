r"""verify.py — L210 (`data/coalition/coalition news.txt`, 19 unita', righe 309-400). Quinto lotto del file.

Cinque finestre reali (20 + 17 + 19 + 21 + 19 = 96) e **16 unita' residue**: L211 chiudera' il file.

**Confine**: riga **401**, `NEWS` di `news:coalition games planet heliarch` — lo **stesso contesto** dell'ultima unita'
del lotto.

**Registro**: 18 unita' su 19 chiudono con un verbo; l'eccezione e' l'unita' 1, che chiude con «acquisto» come il
sorgente chiude con *purchase*.
"""
import collections
import hashlib
import json
import os
import re
import sqlite3

TAB = chr(9)
HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
ROOT = os.path.abspath(os.path.join(L10N, '..'))
ED = os.path.join(L10N, 'staging/editorial')
PATH = 'data/coalition/coalition news.txt'
REAL = [('L206_20261019_211311', 20), ('L207_20261019_211444', 17), ('L208_20261019_212349', 19),
        ('L209_20261019_212543', 21), ('L210_20261019_213332', 19)]
WORDS = re.compile(r"[A-Za-z\u00C0-\u024F']+")
VEND = ('ho', 'essere', 'è', 'chiedo', 'fatto', 'stati', 'aspettavano', 'hanno', 'abbiamo',
        'sta', 'ero', 'riuscito', 'farò')
su = sorted(json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
by = {u['idx']: u for u in tu}
fail = []


def ck(n, c, d=''):
    print('%-74s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


def tail(i):
    w = WORDS.findall(by[i]['italian'].rstrip('."!?'))
    return w[-1] if w else ''


ck('riga grezza identica al sorgente (19/19)', not [u for u in su if lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck('unita: 19 righe 309 - 400', len(tu) == 19 and (tu[0]['line'], tu[-1]['line']) == (309, 400))
ck('77 unita prima della 309 (20 + 17 + 19 + 21)', db.execute(
    'select count(*) from units where path=? and line<309', (PATH,)).fetchone()[0] == 77)
ck('16 unita dopo la 400 (35 - 19): restano solo L211', db.execute(
    'select count(*) from units where path=? and line>400', (PATH,)).fetchone()[0] == 16)
nxt = db.execute('select line,kind,context from units where path=? and line>400 order by line limit 1',
                 (PATH,)).fetchone()
ck('confine misurato: riga 401, NEWS di news:coalition games planet heliarch (stesso contesto)',
   nxt == (401, 'NEWS', 'news:coalition games planet heliarch')
   and tu[-1]['context'] == 'news:coalition games planet heliarch', (nxt, tu[-1]['context']))
ck('il file intero: 112 unita, min(line) 28, max(line) 496',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (112, 28, 496),
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone())
allu, per_win, wrong = [], {}, []
for w, n in REAL:
    d = json.load(open(os.path.join(ED, w, 'translation.json'), encoding='utf-8'))['units']
    got = [u['line'] for u in d if u['path'] == PATH]
    per_win[w] = len(got)
    if len(got) != n:
        wrong.append((w, n, len(got)))
    allu += got
ck('cinque finestre reali: 20, 17, 19, 21, 19',
   list(per_win.values()) == [20, 17, 19, 21, 19] and not wrong, (per_win, wrong))
rest = {r[0] for r in db.execute('select line from units where path=? and line>400', (PATH,))}
ck('somma: 20 + 17 + 19 + 21 + 19 + residuo 16 = 112 unita', len(allu) + len(rest) == 112, (len(allu), len(rest)))
ck('nessuna sovrapposizione fra finestre e residuo',
   len(set(allu) & rest) == 0 and len(set(allu)) == len(allu))
ck('tipi del lotto: 19 NEWS', collections.Counter(u['kind'] for u in su) == {'NEWS': 19})
ck('38 virgolette (2 per unita\'), 0 segnaposto, 0 tab, 4 apici EN / 24 IT',
   sum(u['english'].count('"') for u in su) == 38 == sum(u['italian'].count('"') for u in tu)
   and sum(u['english'].count('<') for u in su) == 0 == sum(u['italian'].count('<') for u in tu)
   and TAB not in ''.join(u['english'] + u['italian'] for u in tu)
   and sum(u['english'].count(chr(39)) for u in su) == 4
   and sum(u['italian'].count(chr(39)) for u in tu) == 24)
ck('registro: 18 chiusure verbali, eccezione l\'unita\' 1 («acquisto» / «purchase»)',
   len([i for i in by if tail(i) in VEND]) == 18 and [i for i in by if tail(i) not in VEND] == [1],
   [i for i in by if tail(i) not in VEND])
ck('PENDING su tutte e 19', not [u['idx'] for u in su
                                 if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('nessun carattere tipografico e nessun non latino',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')
        or any(ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F for c in u['italian'])])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate 0,55-1,90 (italiano piu\' corto: 437 contro 458 parole)',
   0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('APERTO: 96/112 unita del file (85.7%) · 16 dopo la riga 400 · L211 chiudera\' il file')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L210 superato' if not fail else 'verify L210 fallito')
raise SystemExit(0 if not fail else 1)
