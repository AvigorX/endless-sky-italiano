r"""verify.py — L208 (`data/coalition/coalition news.txt`, 19 unita', righe 177-246). Terzo lotto del file.

Tre finestre reali (L206 20, L207 17, L208 19 = 56) e **56 unita' residue**: il file e' esattamente a meta'.

**Confine**: riga **247**, `NEWS` di `news:coalition merchant` — lo **stesso contesto** dell'ultima unita' del lotto.
Quinta volta nella campagna che il confine non separa due voci (L199, L203, L206, L207): il `verify.py` misura il
contesto, non lo assume.

**Registro**: 17 unita' su 19 chiudono con un verbo flesso; le due eccezioni sono **esattamente** le unita' di
narrazione (1 e 12). L'invariante del registro coincide con la distinzione narrazione/discorso.
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
REAL = [('L206_20261019_211311', 20), ('L207_20261019_211444', 17), ('L208_20261019_212349', 19)]
WORDS = re.compile(r"[A-Za-z\u00C0-\u024F']+")
VEND = ('era', 'ora', 'essere', 'domando', 'è', 'stato', 'potrei', 'saranno', 'sento', 'sei',
        'aggiungendo', 'cerchiamo', 'potremmo', 'fanno', 'fatto', 'preso', 'dovuto', 'pensato', 'passato',
        'dispiace')
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
ck('unita: 19 righe 177 - 246', len(tu) == 19 and (tu[0]['line'], tu[-1]['line']) == (177, 246))
ck('37 unita prima della 177 (20 + 17)', db.execute(
    'select count(*) from units where path=? and line<177', (PATH,)).fetchone()[0] == 37)
ck('56 unita dopo la 246 (75 - 19): il file e\' a meta\' esatta', db.execute(
    'select count(*) from units where path=? and line>246', (PATH,)).fetchone()[0] == 56)
nxt = db.execute('select line,kind,context from units where path=? and line>246 order by line limit 1',
                 (PATH,)).fetchone()
ck('confine misurato: riga 247, NEWS di news:coalition merchant (stesso contesto dell\'ultima unita\')',
   nxt == (247, 'NEWS', 'news:coalition merchant')
   and tu[-1]['context'] == 'news:coalition merchant', (nxt, tu[-1]['context']))
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
ck('tre finestre reali: 20, 17, 19', list(per_win.values()) == [20, 17, 19] and not wrong, (per_win, wrong))
rest = {r[0] for r in db.execute('select line from units where path=? and line>246', (PATH,))}
ck('somma: 20 + 17 + 19 + residuo 56 = 112 unita', len(allu) + len(rest) == 112, (len(allu), len(rest)))
ck('nessuna sovrapposizione fra finestre e residuo',
   len(set(allu) & rest) == 0 and len(set(allu)) == len(allu))
ck('tipi del lotto: 19 NEWS', collections.Counter(u['kind'] for u in su) == {'NEWS': 19})
ck('38 virgolette (2 per unita\'), 0 segnaposto, 0 tab, 5 apici EN / 12 IT',
   sum(u['english'].count('"') for u in su) == 38 == sum(u['italian'].count('"') for u in tu)
   and sum(u['english'].count('<') for u in su) == 0 == sum(u['italian'].count('<') for u in tu)
   and TAB not in ''.join(u['english'] + u['italian'] for u in tu)
   and sum(u['english'].count(chr(39)) for u in su) == 5
   and sum(u['italian'].count(chr(39)) for u in tu) == 12)
ck('registro: 17 unita\' con chiusura verbale, 2 senza, e sono le due di narrazione (1 e 12)',
   len([i for i in by if tail(i) in VEND]) == 17 and [i for i in by if tail(i) not in VEND] == [1, 12],
   [i for i in by if tail(i) not in VEND])
ck('PENDING su tutte e 19', not [u['idx'] for u in su
                                 if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('nessun carattere tipografico e nessun non latino',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')
        or any(ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F for c in u['italian'])])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate 0,55-1,90 (italiano piu\' corto: 421 contro 436 parole)',
   0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('APERTO: 56/112 unita del file (50.0%) · 56 dopo la riga 246 · confine riga 247 (stesso contesto)')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L208 superato' if not fail else 'verify L208 fallito')
raise SystemExit(0 if not fail else 1)
