r"""verify.py — L206 (`data/coalition/coalition news.txt`, 20 unita', righe 28-94). **Primo lotto del file.**

Non ci sono finestre precedenti: le unita' prima della 28 sono **zero**, e il controllo lo misura invece di
assumerlo. Dopo la 94 restano **92** unita' (112 - 20).

Il **confine** e' misurato: riga **95**, `NEWS` del contesto `news:heliarch agent` — lo stesso contesto dell'ultima
unita' del lotto, quindi il confine **non separa due voci**: e' un confine interno allo stesso contesto, come in
L199 e L203.

Il **registro Saryd** e' verificato anche qui: la narrazione non finisce con un verbo, il discorso citato si'.
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
REAL = [('L206_20261019_211311', 20)]
WORDS = re.compile(r"[A-Za-z\u00C0-\u024F']+")
VERBS = ('dovresti', 'sono', 'devi', 'siamo', 'sto', 'torno', 'trovo', 'ho')
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


ck('riga grezza identica al sorgente (20/20)', not [u for u in su if lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck('unita: 20 righe 28 - 94', len(tu) == 20 and (tu[0]['line'], tu[-1]['line']) == (28, 94))
ck('ZERO unita prima della 28 (primo lotto del file, misurato)',
   db.execute('select count(*) from units where path=? and line<28', (PATH,)).fetchone()[0] == 0)
ck('92 unita dopo la 94 (112 - 20)', db.execute(
    'select count(*) from units where path=? and line>94', (PATH,)).fetchone()[0] == 92)
nxt = db.execute('select line,kind,context from units where path=? and line>94 order by line limit 1',
                 (PATH,)).fetchone()
ck('confine misurato: riga 95, NEWS di news:heliarch agent (stesso contesto dell\'ultima unita\')',
   nxt == (95, 'NEWS', 'news:heliarch agent')
   and tu[-1]['context'] == 'news:heliarch agent', (nxt, tu[-1]['context']))
ck('il file intero: 112 unita, min(line) 28, max(line) 496',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (112, 28, 496),
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone())
allu, per_win = [], {}
for w, n in REAL:
    d = json.load(open(os.path.join(ED, w, 'translation.json'), encoding='utf-8'))['units']
    got = [u['line'] for u in d if u['path'] == PATH]
    per_win[w] = len(got)
    allu += got
ck('una finestra reale: 20 unita', list(per_win.values()) == [20], per_win)
rest = {r[0] for r in db.execute('select line from units where path=? and line>94', (PATH,))}
ck('somma: 20 + residuo 92 = 112 unita', len(allu) + len(rest) == 112, (len(allu), len(rest)))
ck('nessuna sovrapposizione fra finestra e residuo', len(set(allu) & rest) == 0)
ck('tipi del lotto: 20 NEWS', collections.Counter(u['kind'] for u in su) == {'NEWS': 20})
ck('40 virgolette (2 per unita\'), 0 segnaposto, 0 tab, 5 apici EN / 9 IT',
   sum(u['english'].count('"') for u in su) == 40 == sum(u['italian'].count('"') for u in tu)
   and sum(u['english'].count('<') for u in su) == 0 == sum(u['italian'].count('<') for u in tu)
   and TAB not in ''.join(u['english'] + u['italian'] for u in tu)
   and sum(u['english'].count(chr(39)) for u in su) == 5
   and sum(u['italian'].count(chr(39)) for u in tu) == 9)
ck('registro Saryd: 9 unita citate finiscono con un verbo, la narrazione no',
   len([i for i in by if i not in (1, 10) and tail(i) in VERBS]) == 9
   and [i for i in (1, 10) if tail(i) in VERBS] == [])
ck('PENDING su tutte e 20', not [u['idx'] for u in su
                                 if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('nessun carattere tipografico e nessun non latino',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')
        or any(ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F for c in u['italian'])])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate 0,55-1,90 (il testo italiano e\' piu\' corto: 415 contro 440 parole)',
   0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('APERTO: 20/112 unita del file (17.9%) · 92 dopo la riga 94 · confine riga 95 (stesso contesto)')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L206 superato' if not fail else 'verify L206 fallito')
raise SystemExit(0 if not fail else 1)
