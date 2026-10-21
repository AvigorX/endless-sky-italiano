r"""verify.py — L209 (`data/coalition/coalition news.txt`, 21 unita', righe 247-308). Quarto lotto del file.

Quattro finestre reali (L206 20, L207 17, L208 19, L209 21 = 77) e **35 unita' residue**.

**Confine**: riga **309**, `NEWS` di `news:coalition vendor` — lo **stesso contesto** dell'ultima unita' del lotto.

**Famiglie ripetute**: le unita' 4/9/14, 5/10/15 e 6/11/16 sono lo stesso testo sotto tre contesti civilian. Il controllo
verifica che in **entrambe** le lingue le famiglie siano le stesse tre e che dentro ogni famiglia la resa sia identica.
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
REAL = [('L206_20261019_211311', 20), ('L207_20261019_211444', 17),
        ('L208_20261019_212349', 19), ('L209_20261019_212543', 21)]
FAMILIES = [[4, 9, 14], [5, 10, 15], [6, 11, 16]]
WORDS = re.compile(r"[A-Za-z\u00C0-\u024F']+")
VEND = ('guadagnerei', 'stato', 'è', 'fatto', 'fanno', 'sta', 'essere', 'provano', 'ho', 'sono', 'fare')
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


def fam(lang):
    d = {}
    for i in sorted(by):
        d.setdefault(by[i][lang], []).append(i)
    return sorted([v for v in d.values() if len(v) > 1])


ck('riga grezza identica al sorgente (21/21)', not [u for u in su if lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck('unita: 21 righe 247 - 308', len(tu) == 21 and (tu[0]['line'], tu[-1]['line']) == (247, 308))
ck('56 unita prima della 247 (20 + 17 + 19)', db.execute(
    'select count(*) from units where path=? and line<247', (PATH,)).fetchone()[0] == 56)
ck('35 unita dopo la 308 (56 - 21)', db.execute(
    'select count(*) from units where path=? and line>308', (PATH,)).fetchone()[0] == 35)
nxt = db.execute('select line,kind,context from units where path=? and line>308 order by line limit 1',
                 (PATH,)).fetchone()
ck('confine misurato: riga 309, NEWS di news:coalition vendor (stesso contesto dell\'ultima unita\')',
   nxt == (309, 'NEWS', 'news:coalition vendor') and tu[-1]['context'] == 'news:coalition vendor',
   (nxt, tu[-1]['context']))
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
ck('quattro finestre reali: 20, 17, 19, 21', list(per_win.values()) == [20, 17, 19, 21] and not wrong,
   (per_win, wrong))
rest = {r[0] for r in db.execute('select line from units where path=? and line>308', (PATH,))}
ck('somma: 20 + 17 + 19 + 21 + residuo 35 = 112 unita', len(allu) + len(rest) == 112, (len(allu), len(rest)))
ck('nessuna sovrapposizione fra finestre e residuo',
   len(set(allu) & rest) == 0 and len(set(allu)) == len(allu))
ck('tipi del lotto: 21 NEWS', collections.Counter(u['kind'] for u in su) == {'NEWS': 21})
ck('42 virgolette (2 per unita\'), 0 segnaposto, 0 tab, 2 apici EN / 7 IT',
   sum(u['english'].count('"') for u in su) == 42 == sum(u['italian'].count('"') for u in tu)
   and sum(u['english'].count('<') for u in su) == 0 == sum(u['italian'].count('<') for u in tu)
   and TAB not in ''.join(u['english'] + u['italian'] for u in tu)
   and sum(u['english'].count(chr(39)) for u in su) == 2
   and sum(u['italian'].count(chr(39)) for u in tu) == 7)
ck('famiglie ripetute identiche in inglese e in italiano (4/9/14, 5/10/15, 6/11/16)',
   fam('english') == FAMILIES and fam('italian') == FAMILIES, (fam('english'), fam('italian')))
ck('nessuna copia divergente dentro le famiglie',
   all(len({by[i]['italian'] for i in f}) == 1 for f in FAMILIES))
ck('registro: 17 chiusure verbali, 4 eccezioni (5/10/15 con «mai...», 21 con «crediti!»)',
   len([i for i in by if tail(i) in VEND]) == 17
   and [i for i in by if tail(i) not in VEND] == [5, 10, 15, 21],
   [i for i in by if tail(i) not in VEND])
ck('PENDING su tutte e 21', not [u['idx'] for u in su
                                 if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('nessun carattere tipografico e nessun non latino',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')
        or any(ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F for c in u['italian'])])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate 0,55-1,90 (italiano piu\' lungo: 450 contro 432 parole)',
   0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('APERTO: 77/112 unita del file (68.8%) · 35 dopo la riga 308 · confine riga 309 (stesso contesto)')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L209 superato' if not fail else 'verify L209 fallito')
raise SystemExit(0 if not fail else 1)
