r"""verify.py — L216 (`data/human/deep jobs.txt`, 30 unita', righe 866-929). Quinto lotto del file.

Cinque finestre reali (L212 45, L213 22, L214 35, L215 25, L216 30 = **157**) piu' **1 `UI_LABEL`** (riga 683) e **29
unita' residue**:

    157 + 1 + 29 = 187

**Confine**: riga **935**, un **`VALUE`** (`Transport Deep Security consultants`), **sei righe dopo** l'ultima unita' del
lotto. Fra la 929 e la 935 non ci sono unita': il controllo misura riga, tipo e contesto, e non assume che il confine sia
adiacente.
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
PATH = 'data/human/deep jobs.txt'
REAL = [('L212_20261019_213749', 45), ('L213_20261019_214440', 22),
        ('L214_20261019_215024', 35), ('L215_20261019_215631', 25),
        ('L216_20261019_220252', 30)]
UNTRANSLATED = 683
TAG = re.compile(r'<[^<>]+>')
su = sorted(json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
by = {u['idx']: u for u in tu}
fail = []


def ck(n, c, d=''):
    print('%-74s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente (30/30)', not [u for u in su if lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck('unita: 30 righe 866 - 929', len(tu) == 30 and (tu[0]['line'], tu[-1]['line']) == (866, 929))
ck('128 unita prima della 866 = 127 tradotte + 1 UI_LABEL (riga 683)',
   db.execute('select count(*) from units where path=? and line<866', (PATH,)).fetchone()[0] == 128)
ck('29 unita dopo la 929 (187 - 158)', db.execute(
    'select count(*) from units where path=? and line>929', (PATH,)).fetchone()[0] == 29)
nxt = db.execute('select line,kind,context from units where path=? and line>929 order by line limit 1',
                 (PATH,)).fetchone()
ck('confine misurato: riga 935, VALUE di mission:Transport Consultants (Deep Security) [0], sei righe dopo',
   nxt == (935, 'VALUE', 'mission:Transport Consultants (Deep Security) [0]'), nxt)
ck('fra la 929 e la 935 non ci sono unita\' (il confine non e\' adiacente)',
   db.execute('select count(*) from units where path=? and line>929 and line<935', (PATH,)).fetchone()[0] == 0)
ck('il file intero: 187 unita, min(line) 16, max(line) 1234',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (187, 16, 1234))
allu, per_win, wrong = [], {}, []
for w, n in REAL:
    d = json.load(open(os.path.join(ED, w, 'translation.json'), encoding='utf-8'))['units']
    got = [u['line'] for u in d if u['path'] == PATH]
    per_win[w] = len(got)
    if len(got) != n:
        wrong.append((w, n, len(got)))
    allu += got
ck('cinque finestre reali: 45, 22, 35, 25, 30', list(per_win.values()) == [45, 22, 35, 25, 30] and not wrong,
   (per_win, wrong))
rest = {r[0] for r in db.execute('select line from units where path=? and line>929', (PATH,))}
ck('INVARIANTE: 157 tradotte + 1 UI_LABEL (683) + 29 residue = 187',
   len(allu) == 157 and (len(allu) + 1 + len(rest)) == 187 and UNTRANSLATED not in allu,
   (len(allu), len(rest)))
dbl = {r[0] for r in db.execute('select line from units where path=?', (PATH,))}
ck('nessuna riga persa: finestre + UI_LABEL + residuo coprono esattamente il DB',
   (set(allu) | rest | {UNTRANSLATED}) == dbl and len(dbl) == 187)
ck('nessuna sovrapposizione fra finestre', len(set(allu)) == len(allu))
ck('tipi del lotto: 15 TEXT, 14 MISSION_TEXT, 1 LOGBOOK',
   collections.Counter(u['kind'] for u in su) == {'TEXT': 15, 'MISSION_TEXT': 14, 'LOGBOOK': 1})
ck("13 tab (1-12 e 15), 26 virgolette (2 x 13), 7 segnaposto su 3 simboli",
   sum(u['english'].count(TAB) for u in su) == 13 == sum(u['italian'].count(TAB) for u in tu)
   and sum(u['english'].count('"') for u in su) == 26 == sum(u['italian'].count('"') for u in tu)
   and sum(len(TAG.findall(u['english'])) for u in su) == 7
   == sum(len(TAG.findall(u['italian'])) for u in tu)
   and not [u['idx'] for u in tu if TAG.findall(u['english']) != TAG.findall(u['italian'])])
ck('composizione: apertura con «tu», quattro prese distinte, tre luoghi distinti, chiusura con «e li accompagni»',
   by[16]['italian'].endswith(', tu') and by[17]['italian'].endswith(', tu')
   and len({by[i]['italian'] for i in (18, 19, 20, 21)}) == 4
   and len({by[i]['italian'] for i in (22, 23, 24)}) == 3
   and by[25]['italian'].startswith('e li accompagni'))
ck('PENDING su tutte e 30', not [u['idx'] for u in su
                                 if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('nessuno spazio finale e nessun doppio spazio (tab iniziali ammessi)',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip()
        or '  ' in u['italian'].strip(TAB)])
ck('nessun carattere tipografico e nessun non latino',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')
        or any(ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F for c in u['italian'])])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate 0,55-1,90 (italiano leggermente piu\' lungo: 443 contro 439 parole)',
   0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('APERTO: 157/187 tradotte + 1 UI_LABEL (683) · 29 dopo la riga 929 · confine riga 935 (VALUE)')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L216 superato' if not fail else 'verify L216 fallito')
raise SystemExit(0 if not fail else 1)
