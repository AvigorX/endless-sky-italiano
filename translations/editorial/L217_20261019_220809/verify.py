r"""verify.py — L217 (`data/human/deep jobs.txt`, 29 unita', righe 935-1234). **Lotto terminale.**

Non esiste un confine "dopo": l'ultima unita' del file e' la **1234** e `line > 1234` vale **0**. L'invariante e' quello di
**FILE CHIUSO**: le sei finestre devono coprire tutte le righe traducibili del database, piu' l'**`UI_LABEL` della riga
683**, che non si traduce.

    45 + 22 + 35 + 25 + 30 + 29 = 186 tradotte
    186 + 1 UI_LABEL (683)      = 187 unita' del file

**56 segnaposto**: il conteggio piu' alto della campagna in un lotto. Il confronto e' **per unita' e nell'ordine**.
"""
import collections
import hashlib
import json
import os
import re
import sqlite3

TAB = chr(9)
TAG = re.compile(r'<[^<>]+>')
HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
ROOT = os.path.abspath(os.path.join(L10N, '..'))
ED = os.path.join(L10N, 'staging/editorial')
PATH = 'data/human/deep jobs.txt'
REAL = [('L212_20261019_213749', 45), ('L213_20261019_214440', 22),
        ('L214_20261019_215024', 35), ('L215_20261019_215631', 25),
        ('L216_20261019_220252', 30), ('L217_20261019_220809', 29)]
UNTRANSLATED = 683
su = sorted(json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
by = {u['idx']: u for u in tu}
fail = []


def ck(n, c, d=''):
    print('%-74s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente (29/29)', not [u for u in su if lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck('unita: 29 righe 935 - 1234', len(tu) == 29 and (tu[0]['line'], tu[-1]['line']) == (935, 1234))
ck('157 unita tradotte prima della 935 (L212-L216)',
   db.execute('select count(*) from units where path=? and line<935', (PATH,)).fetchone()[0] == 158
   and db.execute('select count(*) from units where path=? and line<935 and kind!="UI_LABEL"',
                  (PATH,)).fetchone()[0] == 157)
ck('FINE FILE: zero unita dopo la 1234 (invariante di lotto terminale, misurata)',
   db.execute('select count(*) from units where path=? and line>1234', (PATH,)).fetchone()[0] == 0)
ck('la riga 1234 e\' l\'ULTIMA unita\' del percorso nel DB',
   db.execute('select max(line) from units where path=?', (PATH,)).fetchone()[0] == 1234)
ck('il file intero: 187 unita, min(line) 16, max(line) 1234, di cui 1 UI_LABEL',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (187, 16, 1234)
   and db.execute('select count(*) from units where path=? and kind="UI_LABEL"', (PATH,)).fetchone()[0] == 1)
allu, per_win, wrong = [], {}, []
for w, n in REAL:
    d = json.load(open(os.path.join(ED, w, 'translation.json'), encoding='utf-8'))['units']
    got = [u['line'] for u in d if u['path'] == PATH]
    per_win[w] = len(got)
    if len(got) != n:
        wrong.append((w, n, len(got)))
    allu += got
ck('sei finestre reali: 45, 22, 35, 25, 30, 29',
   list(per_win.values()) == [45, 22, 35, 25, 30, 29] and not wrong, (per_win, wrong))
dbl = [r[0] for r in db.execute('select line from units where path=? order by line', (PATH,))]
ck('FILE CHIUSO: 186 righe tradotte distinte + l\'UI_LABEL della 683 coprono i 187 del DB',
   len(allu) == 186 == len(set(allu)) and sorted(set(allu) | {UNTRANSLATED}) == dbl,
   (len(allu), len(set(allu)), len(dbl)))
ck('l\'UI_LABEL non compare in nessuna finestra (asserzione negativa scritta)',
   UNTRANSLATED not in allu)
ck('tipi del lotto: 12 VALUE, 12 DESCRIPTION, 5 DIALOG',
   collections.Counter(u['kind'] for u in su) == {'VALUE': 12, 'DESCRIPTION': 12, 'DIALOG': 5})
ck("56 segnaposto, identici per unita' e nell'ordine",
   sum(len(TAG.findall(u['english'])) for u in su) == 56
   == sum(len(TAG.findall(u['italian'])) for u in tu)
   and not [u['idx'] for u in tu if TAG.findall(u['english']) != TAG.findall(u['italian'])])
ck('0 tab, 2 virgolette (unita\' 7), 0 apici in inglese / 4 in italiano',
   TAB not in ''.join(u['english'] + u['italian'] for u in tu)
   and sum(u['english'].count('"') for u in su) == 2 == sum(u['italian'].count('"') for u in tu)
   and [u['idx'] for u in tu if '"' in u['italian']] == [7]
   and sum(u['english'].count(chr(39)) for u in su) == 0
   and sum(u['italian'].count(chr(39)) for u in tu) == 4)
ck('i 12 VALUE restano identici all\'inglese',
   all(u['italian'] == u['english'] for u in tu if u['kind'] == 'VALUE'))
ck('PENDING su tutte e 29', not [u['idx'] for u in su
                                 if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('nessun carattere tipografico e nessun non latino',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')
        or any(ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F for c in u['italian'])])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate 0,55-1,90 (italiano piu\' lungo: 398 contro 375 parole)',
   0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('CHIUSO: 186/186 traducibili + 1 UI_LABEL = 187/187 · ultima riga 1234 · nessuna unita dopo')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L217 superato (file chiuso)' if not fail else 'verify L217 fallito')
raise SystemExit(0 if not fail else 1)
