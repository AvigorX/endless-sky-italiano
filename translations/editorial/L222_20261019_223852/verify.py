r"""verify.py — L222 (`data/successors/successor ships.txt`, 26 unita', righe 1141-1338). **Lotto terminale.**

Non esiste un confine "dopo": la riga **1338** e' l'ultima del file e `line > 1338` vale **0**. L'invariante e' quello di
**FILE CHIUSO**, e questo file **non ha `UI_LABEL`**: tutte le unita' sono traducibili.

    45 (L218) + 25 (L219) + 26 (L220) + 24 (L221) + 26 (L222) = 146
    nessuna label da aggiungere: 146 = 146

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
PATH = 'data/successors/successor ships.txt'
REAL = [('L218_20261019_221520', 45), ('L219_20261019_222027', 25),
        ('L220_20261019_222539', 26), ('L221_20261019_223227', 24),
        ('L222_20261019_223852', 26)]
SHARED = ('una nave da guerra prodotta in serie dalle Alte Case, abbastanza flessibile da ricoprire una varietà di '
          'ruoli leggeri. Essendo abbastanza grande da operare come unità autosufficiente, questi vascelli costituiscono '
          'un ponte utile tra gli intercettori a corto raggio')
su = sorted(json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
fail = []


def ck(n, c, d=''):
    print('%-74s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente (26/26)', not [u for u in su if lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck('unita: 26 righe 1141 - 1338', len(tu) == 26 and (tu[0]['line'], tu[-1]['line']) == (1141, 1338))
ck('120 unita tradotte prima della 1141 (45+25+26+24)', db.execute(
    'select count(*) from units where path=? and line<1141', (PATH,)).fetchone()[0] == 120)
ck('FINE FILE: zero unita dopo la 1338 (invariante di lotto terminale, misurata)',
   db.execute('select count(*) from units where path=? and line>1338', (PATH,)).fetchone()[0] == 0)
ck('la riga 1338 e\' l\'ULTIMA unita\' del percorso nel DB',
   db.execute('select max(line) from units where path=?', (PATH,)).fetchone()[0] == 1338)
ck('il file intero: 146 unita, righe 17 - 1338',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (146, 17, 1338))
ck('il file NON ha UI_LABEL: tutte le unita\' sono traducibili',
   db.execute('select count(*) from units where path=? and kind="UI_LABEL"', (PATH,)).fetchone()[0] == 0)
allu, per_win, wrong = [], {}, []
for w, n in REAL:
    d = json.load(open(os.path.join(ED, w, 'translation.json'), encoding='utf-8'))['units']
    got = [u['line'] for u in d if u['path'] == PATH]
    per_win[w] = len(got)
    if len(got) != n:
        wrong.append((w, n, len(got)))
    allu += got
ck('cinque finestre reali: 45, 25, 26, 24, 26',
   list(per_win.values()) == [45, 25, 26, 24, 26] and not wrong, (per_win, wrong))
dbl = [r[0] for r in db.execute('select line from units where path=? order by line', (PATH,))]
ck('FILE CHIUSO: 146 righe distinte coprono esattamente i 146 del DB',
   len(allu) == 146 == len(set(allu)) and sorted(set(allu)) == dbl,
   (len(allu), len(set(allu)), len(dbl)))
ck('nessuna sovrapposizione fra finestre', len(set(allu)) == len(allu))
ck('tipi del lotto: 18 TEXT, 6 DESCRIPTION, 2 VALUE',
   collections.Counter(u['kind'] for u in su) == {'TEXT': 18, 'DESCRIPTION': 6, 'VALUE': 2})
ck('20 unita\' IDENTICHE all\'inglese + 6 tradotte = le 6 DESCRIPTION',
   sum(1 for u in tu if u['italian'] == u['english']) == 20
   and sorted(u['idx'] for u in tu if u['italian'] != u['english'])
   == sorted(u['idx'] for u in tu if u['kind'] == 'DESCRIPTION'))
ck('36 virgolette (2 x 18 TEXT, nessuna in prosa), 2 tab (13 e 26), 0 segnaposto',
   sum(u['english'].count(QUOTE) for u in su) == 36 == sum(u['italian'].count(QUOTE) for u in tu)
   and {u['idx']: u['english'].count(QUOTE) for u in su if QUOTE in u['english']}
   == {u['idx']: 2 for u in su if u['kind'] == 'TEXT'}
   and [u['idx'] for u in tu if TAB in u['italian']] == [13, 26]
   and sum(len(TAG.findall(u['english'])) for u in su) == 0
   == sum(len(TAG.findall(u['italian'])) for u in tu))
ck('COERENZA 12/14: testo condiviso identico e punteggiatura diversa conservata',
   SHARED in tu[11]['italian'] and SHARED in tu[13]['italian']
   and 'a corto raggio e relativamente vulnerabili' in tu[11]['italian']
   and 'a corto raggio, relativamente vulnerabili' in tu[13]['italian'])
ck('COERENZA con L221: la formula della Veusade usa la resa gia\' fissata',
   "inadatte all'uso polivalente" in tu[0]['italian']
   and 'unità ausiliarie o di polizia' in tu[0]['italian'])
ck('PENDING su tutte e 26', not [u['idx'] for u in su
                                 if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('nessuno spazio finale e nessun doppio spazio (tab iniziali ammessi)',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip()
        or '  ' in u['italian'].strip(TAB)])
ck('nessun carattere tipografico e nessun non latino',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')
        or any(ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F for c in u['italian'])])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate 0,55-1,90 (nomi 1,00; DESCRIPTION 1,06-1,21; totale 431 -> 472 parole)',
   0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('CHIUSO: 146/146 unita\' del file · ultima riga 1338 · nessuna unita dopo · nessun UI_LABEL')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L222 superato (file chiuso)' if not fail else 'verify L222 fallito')
raise SystemExit(0 if not fail else 1)
