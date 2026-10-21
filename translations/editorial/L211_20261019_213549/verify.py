r"""verify.py — L211 (`data/coalition/coalition news.txt`, 16 unita', righe 401-496). **Lotto terminale.**

Non esiste un confine "dopo": l'ultima unita' e' la **496** e `line > 496` vale **0**. L'invariante e' quello di
**FILE CHIUSO**: le sei finestre devono coprire tutte le **112** righe del database, senza buchi e senza sovrapposizioni.

Finestre: L206 20, L207 17, L208 19, L209 21, L210 19, L211 16 = **112**.

Le unita' **6** e **11** sono una sola virgoletta ciascuna (citazione spezzata): il controllo lo verifica in entrambe le
lingue, perche' e' una proprieta' del file, non del testo.
"""
import collections
import hashlib
import json
import os
import re
import sqlite3

TAB = chr(9)
QUOTE = chr(34)
HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
ROOT = os.path.abspath(os.path.join(L10N, '..'))
ED = os.path.join(L10N, 'staging/editorial')
PATH = 'data/coalition/coalition news.txt'
REAL = [('L206_20261019_211311', 20), ('L207_20261019_211444', 17), ('L208_20261019_212349', 19),
        ('L209_20261019_212543', 21), ('L210_20261019_213332', 19), ('L211_20261019_213549', 16)]
DIST = [2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2]
WORDS = re.compile(r"[A-Za-z\u00C0-\u024F']+")
VEND = ('sono', 'facciano', 'faccio', 'fatto', 'stato', 'sei', 'puoi', 'fanno', 'è', 'possiamo', "l'ho")
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


ck('riga grezza identica al sorgente (16/16)', not [u for u in su if lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck('unita: 16 righe 401 - 496', len(tu) == 16 and (tu[0]['line'], tu[-1]['line']) == (401, 496))
ck('96 unita prima della 401 (20 + 17 + 19 + 21 + 19)', db.execute(
    'select count(*) from units where path=? and line<401', (PATH,)).fetchone()[0] == 96)
ck('FINE FILE: zero unita dopo la 496 (invariante di lotto terminale, misurata)',
   db.execute('select count(*) from units where path=? and line>496', (PATH,)).fetchone()[0] == 0)
ck('la riga 496 e\' l\'ULTIMA unita\' del percorso nel DB',
   db.execute('select max(line) from units where path=?', (PATH,)).fetchone()[0] == 496)
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
ck('sei finestre reali: 20, 17, 19, 21, 19, 16',
   list(per_win.values()) == [20, 17, 19, 21, 19, 16] and not wrong, (per_win, wrong))
dbl = [r[0] for r in db.execute('select line from units where path=? order by line', (PATH,))]
ck('FILE CHIUSO: 112 righe, tutte quelle del DB, nessun buco',
   len(allu) == 112 == len(dbl) and set(dbl) - set(allu) == set(),
   (len(allu), len(dbl), sorted(set(dbl) - set(allu))[:5]))
ck('nessuna sovrapposizione fra finestre (112 righe DISTINTE)',
   len(set(allu)) == 112 == len(allu), len(set(allu)))
ck('tipi del lotto: 16 NEWS', collections.Counter(u['kind'] for u in su) == {'NEWS': 16})
ck('22 virgolette con distribuzione per unita\' (2,2,2,2,2,1,0,0,0,0,1,2,2,2,2,2) in entrambe le lingue',
   sum(u['english'].count('"') for u in su) == 22 == sum(u['italian'].count('"') for u in tu)
   and [u['english'].count('"') for u in tu] == DIST == [u['italian'].count('"') for u in tu], DIST)
ck("CITAZIONE SPEZZATA: le unita' 6 e 11 sono esattamente una virgoletta in inglese e in italiano",
   all(by[i]['english'] == QUOTE and by[i]['italian'] == QUOTE for i in (6, 11)))
ck('0 segnaposto, 0 tab, 6 apici EN / 14 IT',
   sum(u['english'].count('<') for u in su) == 0 == sum(u['italian'].count('<') for u in tu)
   and TAB not in ''.join(u['english'] + u['italian'] for u in tu)
   and sum(u['english'].count(chr(39)) for u in su) == 6
   and sum(u['italian'].count(chr(39)) for u in tu) == 14)
ck('registro: 13 chiusure verbali; eccezioni 6 e 11 (strutturali) e 9 («gioia» / «joy»)',
   len([i for i in by if tail(i) in VEND]) == 13
   and [i for i in by if tail(i) not in VEND] == [6, 9, 11],
   [i for i in by if tail(i) not in VEND])
ck('PENDING su tutte e 16', not [u['idx'] for u in su
                                 if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('nessun carattere tipografico e nessun non latino',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')
        or any(ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F for c in u['italian'])])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate 0,55-1,90 (italiano piu\' corto: 352 contro 378 parole)',
   0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('CHIUSO: 112/112 unita del file (100%) · ultima riga 496 · nessuna unita dopo')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L211 superato (file chiuso)' if not fail else 'verify L211 fallito')
raise SystemExit(0 if not fail else 1)
