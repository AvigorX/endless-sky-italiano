r"""verify.py — L215 (`data/human/deep jobs.txt`, 25 unita', righe 684-864). Quarto lotto del file.

Quattro finestre reali (L212 45, L213 22, L214 35, L215 25 = **127**) e **59 unita' residue**.

**La complicazione nuova**: fra le finestre c'e' **una** unita' che non entra in nessuna — la riga **683**, un
`UI_LABEL`, che non si traduce. Il conto dell'invariante e' quindi:

    127 (tradotte) + 1 (UI_LABEL) + 59 (residuo) = 187

Le unita' prima della 684 sono **103**, non 102: chi somma solo le finestre trova un buco di uno e sbaglia a
diagnosticarlo. Il controllo lo dichiara con un'asserzione esplicita.

**Confine**: riga **866**, `MISSION_TEXT` di `mission:Deep Consultants` — **lo stesso contesto** dell'ultima unita' (864),
e a due righe di distanza.
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
        ('L214_20261019_215024', 35), ('L215_20261019_215631', 25)]
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


ck('riga grezza identica al sorgente (25/25)', not [u for u in su if lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck('unita: 25 righe 684 - 864', len(tu) == 25 and (tu[0]['line'], tu[-1]['line']) == (684, 864))
ck('103 unita prima della 684 = 102 tradotte + 1 UI_LABEL (riga 683)',
   db.execute('select count(*) from units where path=? and line<684', (PATH,)).fetchone()[0] == 103
   and db.execute('select count(*) from units where path=? and line=683 and kind="UI_LABEL"',
                  (PATH,)).fetchone()[0] == 1)
ck('59 unita dopo la 864 (187 - 128)', db.execute(
    'select count(*) from units where path=? and line>864', (PATH,)).fetchone()[0] == 59)
nxt = db.execute('select line,kind,context from units where path=? and line>864 order by line limit 1',
                 (PATH,)).fetchone()
ck('confine misurato: riga 866, MISSION_TEXT di mission:Deep Consultants (stesso contesto, due righe dopo)',
   nxt == (866, 'MISSION_TEXT', 'mission:Deep Consultants')
   and tu[-1]['context'] == 'mission:Deep Consultants', (nxt, tu[-1]['context']))
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
ck('quattro finestre reali: 45, 22, 35, 25', list(per_win.values()) == [45, 22, 35, 25] and not wrong,
   (per_win, wrong))
rest = {r[0] for r in db.execute('select line from units where path=? and line>864', (PATH,))}
ck('INVARIANTE CON L\'UI_LABEL: 127 tradotte + 1 UI_LABEL (683) + 59 residue = 187',
   len(allu) == 127 and (len(allu) + 1 + len(rest)) == 187 and UNTRANSLATED not in allu,
   (len(allu), len(rest)))
dbl = {r[0] for r in db.execute('select line from units where path=?', (PATH,))}
ck('nessuna riga persa: finestre + UI_LABEL + residuo coprono esattamente il DB',
   (set(allu) | rest | {UNTRANSLATED}) == dbl and len(dbl) == 187,
   sorted(dbl - (set(allu) | rest | {UNTRANSLATED}))[:5])
ck('nessuna sovrapposizione fra finestre', len(set(allu)) == len(allu))
ck('tipi del lotto: 15 MISSION_TEXT, 5 VALUE, 5 DESCRIPTION',
   collections.Counter(u['kind'] for u in su) == {'MISSION_TEXT': 15, 'VALUE': 5, 'DESCRIPTION': 5})
ck("14 tab (uno per unita' nelle 1-12 e 24-25), 29 virgolette per unita', 15 segnaposto",
   sum(u['english'].count(TAB) for u in su) == 14 == sum(u['italian'].count(TAB) for u in tu)
   and sum(u['english'].count('"') for u in su) == 29 == sum(u['italian'].count('"') for u in tu)
   and sum(len(TAG.findall(u['english'])) for u in su) == 15
   == sum(len(TAG.findall(u['italian'])) for u in tu))
ck('citazione su due paragrafi: unita\' 1 con una sola virgoletta, la 2 con due',
   by[1]['italian'].count('"') == 1 and by[2]['italian'].count('"') == 2
   and by[1]['italian'].startswith(TAB + '"') and not by[1]['italian'].endswith('"'))
ck("la battuta «in ogni caso» compare tre volte in entrambe le lingue (1, 2, 6)",
   " ".join(u['english'] for u in tu).count('at any rate') == 3
   == " ".join(u['italian'] for u in tu).count('in ogni caso'))
ck('PENDING su tutte e 25', not [u['idx'] for u in su
                                 if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('nessuno spazio finale e nessun doppio spazio (tab iniziali ammessi)',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip()
        or '  ' in u['italian'].strip(TAB)])
ck('nessun carattere tipografico e nessun non latino',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')
        or any(ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F for c in u['italian'])])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate 0,55-1,90 (italiano piu\' corto: 427 contro 431 parole)',
   0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('APERTO: 127/187 tradotte + 1 UI_LABEL (683) · 59 dopo la riga 864 · confine riga 866')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L215 superato' if not fail else 'verify L215 fallito')
raise SystemExit(0 if not fail else 1)
