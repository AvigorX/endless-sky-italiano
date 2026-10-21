r"""verify.py — L227 (`data/remnant/remnant outfits.txt`, 10 unita', righe 884-979). **Lotto terminale.**

Non esiste un confine "dopo": la riga **979** e' l'ultima del file e `line > 979` vale **0**. L'invariante e' quello di
**FILE CHIUSO**, e questo file **non ha `UI_LABEL`**: tutte le 57 unita' sono traducibili.

    12 (L223) + 13 (L224) + 11 (L225) + 11 (L226) + 10 (L227) = 57
    nessuna label da aggiungere: 57 = 57

Il controllo verifica che le cinque finestre coprano **esattamente** le righe del database, senza buchi ne' sovrapposizioni.
"""
import collections
import hashlib
import json
import os
import re
import sqlite3

TAB = chr(9)
QUOTE = chr(34)
TAG = re.compile(r'<[^<>]+>')
HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
ROOT = os.path.abspath(os.path.join(L10N, '..'))
ED = os.path.join(L10N, 'staging/editorial')
PATH = 'data/remnant/remnant outfits.txt'
REAL = [('L223_20261019_224448', 12), ('L224_20261019_224956', 13),
        ('L225_20261019_225556', 11), ('L226_20261019_230148', 11),
        ('L227_20261019_230743', 10)]
su = sorted(json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
fail = []


def ck(n, c, d=''):
    print('%-74s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente (10/10)', not [u for u in su if lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck('unita: 10 righe 884 - 979', len(tu) == 10 and (tu[0]['line'], tu[-1]['line']) == (884, 979))
ck('47 unita tradotte prima della 884 (12+13+11+11)', db.execute(
    'select count(*) from units where path=? and line<884', (PATH,)).fetchone()[0] == 47)
ck('FINE FILE: zero unita dopo la 979 (invariante di lotto terminale, misurata)',
   db.execute('select count(*) from units where path=? and line>979', (PATH,)).fetchone()[0] == 0)
ck('la riga 979 e\' l\'ULTIMA unita\' del percorso nel DB',
   db.execute('select max(line) from units where path=?', (PATH,)).fetchone()[0] == 979)
ck('il file intero: 57 unita, righe 48 - 979',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (57, 48, 979))
ck('il file NON ha UI_LABEL: tutte le unita\' sono traducibili',
   db.execute('select count(*) from units where path=? and kind="UI_LABEL"', (PATH,)).fetchone()[0] == 0)
ck('il file ha 2 VALUE (righe 224 e 948) e 55 DESCRIPTION',
   db.execute('select kind,count(*) from units where path=? group by kind',
              (PATH,)).fetchall() == [('DESCRIPTION', 55), ('VALUE', 2)])
allu, per_win, wrong = [], {}, []
for w, n in REAL:
    d = json.load(open(os.path.join(ED, w, 'translation.json'), encoding='utf-8'))['units']
    got = [u['line'] for u in d if u['path'] == PATH]
    per_win[w] = len(got)
    if len(got) != n:
        wrong.append((w, n, len(got)))
    allu += got
ck('cinque finestre reali: 12, 13, 11, 11, 10',
   list(per_win.values()) == [12, 13, 11, 11, 10] and not wrong, (per_win, wrong))
dbl = [r[0] for r in db.execute('select line from units where path=? order by line', (PATH,))]
ck('FILE CHIUSO: 57 righe distinte coprono esattamente i 57 del DB',
   len(allu) == 57 == len(set(allu)) and sorted(set(allu)) == dbl,
   (len(allu), len(set(allu)), len(dbl)))
ck('nessuna sovrapposizione fra finestre', len(set(allu)) == len(allu))
ck('tipi del lotto: 9 DESCRIPTION, 1 VALUE',
   collections.Counter(u['kind'] for u in su) == {'DESCRIPTION': 9, 'VALUE': 1})
ck('1 unita\' IDENTICA all\'inglese (il VALUE) e 9 tradotte',
   sum(1 for u in tu if u['italian'] == u['english']) == 1
   and tu[5]['italian'] == tu[5]['english'] == 'Void Sprite Parts'
   and all(u['italian'] != u['english'] for u in tu if u['kind'] == 'DESCRIPTION'))
ck('2 tab (unita\' 5, 8) e ZERO virgolette in entrambe le lingue',
   [u['idx'] for u in tu if TAB in u['italian']] == [5, 8]
   and sum(u['english'].count(QUOTE) for u in su) == 0 == sum(u['italian'].count(QUOTE) for u in tu))
ck('0 segnaposto', sum(len(TAG.findall(u['english'])) for u in su) == 0
   == sum(len(TAG.findall(u['italian'])) for u in tu))
ck('PENDING su tutte e 10', not [u['idx'] for u in su
                                 if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('nessuno spazio finale e nessun doppio spazio (tab iniziali ammessi)',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip()
        or '  ' in u['italian'].strip(TAB)])
ck('nessun carattere tipografico e nessun non latino',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')
        or any(ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F for c in u['italian'])])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate 0,55-1,90 (0,84 - 1,10; 382 -> 376 parole)',
   0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('CHIUSO: 57/57 unita\' del file · ultima riga 979 · nessuna unita dopo · nessun UI_LABEL')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L227 superato (file chiuso)' if not fail else 'verify L227 fallito')
raise SystemExit(0 if not fail else 1)
