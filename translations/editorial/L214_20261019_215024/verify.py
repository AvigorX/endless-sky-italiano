r"""verify.py — L214 (`data/human/deep jobs.txt`, 35 unita', righe 457-682). Terzo lotto del file.

Tre finestre reali (L212 45, L213 22, L214 35 = 102) e **85 unita' residue** (187 - 102).

**Confine**: riga **683**, un **`UI_LABEL`** di `mission:Deep Security Package Reveal`. E' il primo confine della campagna
su un tipo che **non entra mai in staging**: il `verify.py` lo misura e lo dichiara, cosi' il lotto successivo sa che
quell'unita' non comparira' in nessun `translation.json`.

**Tab**: 15, uno in ognuna delle unita' 21-35, in entrambe le lingue.
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
PATH = 'data/human/deep jobs.txt'
REAL = [('L212_20261019_213749', 45), ('L213_20261019_214440', 22), ('L214_20261019_215024', 35)]
su = sorted(json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
by = {u['idx']: u for u in tu}
fail = []


def ck(n, c, d=''):
    print('%-74s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente (35/35)', not [u for u in su if lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck('unita: 35 righe 457 - 682', len(tu) == 35 and (tu[0]['line'], tu[-1]['line']) == (457, 682))
ck('67 unita prima della 457 (45 + 22)', db.execute(
    'select count(*) from units where path=? and line<457', (PATH,)).fetchone()[0] == 67)
ck('85 unita dopo la 682 (187 - 102)', db.execute(
    'select count(*) from units where path=? and line>682', (PATH,)).fetchone()[0] == 85)
nxt = db.execute('select line,kind,context from units where path=? and line>682 order by line limit 1',
                 (PATH,)).fetchone()
ck('confine misurato: riga 683, UI_LABEL di mission:Deep Security Package Reveal (tipo che non entra in staging)',
   nxt == (683, 'UI_LABEL', 'mission:Deep Security Package Reveal'), nxt)
ck('quell\'UI_LABEL non compare nel lotto (asserzione negativa scritta)',
   [u['idx'] for u in tu if u['kind'] == 'UI_LABEL'] == [])
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
ck('tre finestre reali: 45, 22, 35', list(per_win.values()) == [45, 22, 35] and not wrong, (per_win, wrong))
rest = {r[0] for r in db.execute('select line from units where path=? and line>682', (PATH,))}
ck('somma: 45 + 22 + 35 + residuo 85 = 187 unita', len(allu) + len(rest) == 187, (len(allu), len(rest)))
ck('nessuna sovrapposizione fra finestre e residuo',
   len(set(allu) & rest) == 0 and len(set(allu)) == len(allu))
ck('tipi del lotto: 16 MISSION_TEXT, 8 TEXT, 5 VALUE, 5 DESCRIPTION, 1 LOGBOOK',
   collections.Counter(u['kind'] for u in su)
   == {'MISSION_TEXT': 16, 'TEXT': 8, 'VALUE': 5, 'DESCRIPTION': 5, 'LOGBOOK': 1})
ck("TAB: 15 in entrambe le lingue, uno per unita' nelle 21-35, e sempre iniziale",
   sum(u['english'].count(TAB) for u in su) == 15 == sum(u['italian'].count(TAB) for u in tu)
   and [u['idx'] for u in tu if TAB in u['italian']] == list(range(21, 36))
   and all(u['english'].startswith(TAB) == u['italian'].startswith(TAB) for u in tu))
ck('22 virgolette (2 per unita\' di dialogo), 16 segnaposto su 3 simboli, identici per unita\'',
   sum(u['english'].count('"') for u in su) == 22 == sum(u['italian'].count('"') for u in tu)
   and sum(len(TAG.findall(u['english'])) for u in su) == 16
   == sum(len(TAG.findall(u['italian'])) for u in tu)
   and not [u['idx'] for u in tu
            if collections.Counter(TAG.findall(u['english'])) != collections.Counter(TAG.findall(u['italian']))])
ck('5 VALUE identici all\'inglese e 5 DESCRIPTION identiche fra loro',
   all(u['italian'] == u['english'] for u in tu if u['kind'] == 'VALUE')
   and len({u['italian'] for u in tu if u['kind'] == 'DESCRIPTION'}) == 1)
ck('composizione: apertura senza preposizione, alternative con preposizione, iniziali coerenti',
   by[1]['italian'] == 'Come da istruzioni, consegni il pacco'
   and all(by[i]['italian'].startswith(('a ', 'al ', 'alla ')) for i in range(2, 8))
   and len({by[i]['italian'] for i in range(2, 8)}) == 6)
ck('PENDING su tutte e 35', not [u['idx'] for u in su
                                 if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('nessuno spazio finale e nessun doppio spazio (tab iniziali ammessi)',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip()
        or '  ' in u['italian'].strip(TAB)])
ck('nessun carattere tipografico e nessun non latino',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')
        or any(ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F for c in u['italian'])])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate 0,55-1,90 (italiano quasi identico: 430 contro 431 parole)',
   0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('APERTO: 102/187 unita del file (54.5%) · 85 dopo la riga 682 · confine riga 683 (UI_LABEL)')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L214 superato' if not fail else 'verify L214 fallito')
raise SystemExit(0 if not fail else 1)
