r"""verify.py — L205 (`data/hai/hai outfits.txt`, 13 unita', righe 805-984). **Lotto terminale.**

Non esiste un confine "dopo": l'ultima unita' del file e' la **984**, e il controllo lo misura
(`line > 984` = 0). L'invariante qui e' quello di **FILE CHIUSO**: le cinque finestre reali devono coprire
**tutte** le righe del database per questo percorso, senza buchi e senza sovrapposizioni.

Finestre: L201 8, L202 16, L203 9, L204 19, L205 13 = **65**.
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
PATH = 'data/hai/hai outfits.txt'
REAL = [('L201_20261019_204959', 8), ('L202_20261019_205624', 16), ('L203_20261019_210258', 9),
        ('L204_20261019_210851', 19), ('L205_20261019_211129', 13)]
su = sorted(json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
fail = []


def ck(n, c, d=''):
    print('%-74s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente (13/13)', not [u for u in su if lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck('unita: 13 righe 805 - 984', len(tu) == 13 and (tu[0]['line'], tu[-1]['line']) == (805, 984))
ck('52 unita prima della 805 (8 + 16 + 9 + 19)', db.execute(
    'select count(*) from units where path=? and line<805', (PATH,)).fetchone()[0] == 52)
ck('FINE FILE: zero unita dopo la 984 (invariante di lotto terminale, misurata)',
   db.execute('select count(*) from units where path=? and line>984', (PATH,)).fetchone()[0] == 0)
ck('la riga 984 e\' l\'ULTIMA unita\' del percorso nel DB',
   db.execute('select max(line) from units where path=?', (PATH,)).fetchone()[0] == 984)
ck('il file intero: 65 unita, min(line) 27, max(line) 984',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (65, 27, 984),
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone())
allu, per_win, wrong = [], {}, []
for w, n in REAL:
    d = json.load(open(os.path.join(ED, w, 'translation.json'), encoding='utf-8'))['units']
    got = [u['line'] for u in d if u['path'] == PATH]
    per_win[w] = len(got)
    if len(got) != n:
        wrong.append((w, n, len(got)))
    allu += got
ck('cinque finestre reali: 8, 16, 9, 19, 13', list(per_win.values()) == [8, 16, 9, 19, 13] and not wrong, (per_win, wrong))
dbl = [r[0] for r in db.execute('select line from units where path=? order by line', (PATH,))]
ck('FILE CHIUSO: 65 righe, tutte quelle del DB, nessun buco',
   len(allu) == 65 == len(dbl) and set(dbl) - set(allu) == set(),
   (len(allu), len(dbl), sorted(set(dbl) - set(allu))[:5]))
ck('nessuna sovrapposizione fra finestre (65 righe DISTINTE)',
   len(set(allu)) == 65 == len(allu), len(set(allu)))
ck('tipi del lotto: 13 DESCRIPTION', collections.Counter(u['kind'] for u in su) == {'DESCRIPTION': 13})
ck('0 segnaposto, 1 tab, 2 virgolette, 1 apice EN / 4 IT',
   sum(u['english'].count('<') for u in su) == 0 == sum(u['italian'].count('<') for u in tu)
   and [u['idx'] for u in su if u['english'].startswith(TAB)] == [13]
   and sum(u['english'].count('"') for u in su) == 2 == sum(u['italian'].count('"') for u in tu)
   and sum(u['english'].count(chr(39)) for u in su) == 1
   and sum(u['italian'].count(chr(39)) for u in tu) == 4)
ck('PENDING su tutte e 13', not [u['idx'] for u in su
                                 if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('nessuno spazio finale e nessun doppio spazio (tab iniziale ammesso)',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip()
        or '  ' in u['italian'].strip('\t') or u['english'] != u['english'].rstrip()])
ck('nessun carattere tipografico e nessun non latino',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')
        or any(ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F for c in u['italian'])])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate 0,55-1,90', 0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('CHIUSO: 65/65 unita del file (100%) · ultima riga 984 · nessuna unita dopo')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L205 superato (file chiuso)' if not fail else 'verify L205 fallito')
raise SystemExit(0 if not fail else 1)
