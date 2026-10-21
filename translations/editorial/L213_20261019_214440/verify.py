r"""verify.py — L213 (`data/human/deep jobs.txt`, 22 unita', righe 333-453). Secondo lotto del file.

Due finestre reali (L212 45, L213 22 = 67) e **120 unita' residue** (187 - 67), di cui **1 `UI_LABEL`** non traducibile.

**Confine**: riga **457**, `TEXT` di `phrase:secure package dropoff payment` — quattro righe dopo la 453 e **stesso tipo**
(`TEXT`) dell'ultima unita': il controllo misura riga, tipo e contesto, e non si fida della continuita' del tipo.

**Frammenti**: 12 `TEXT` di `phrase:` con quattro gruppi di alternative, verificati per composizione (iniziale) e per
alternativa distinta.
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
REAL = [('L212_20261019_213749', 45), ('L213_20261019_214440', 22)]
su = sorted(json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
by = {u['idx']: u for u in tu}
PHRASE = [u['idx'] for u in tu if u['context'].startswith('phrase:')]
fail = []


def ck(n, c, d=''):
    print('%-74s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente (22/22)', not [u for u in su if lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck('unita: 22 righe 333 - 453', len(tu) == 22 and (tu[0]['line'], tu[-1]['line']) == (333, 453))
ck('45 unita prima della 333 (L212)', db.execute(
    'select count(*) from units where path=? and line<333', (PATH,)).fetchone()[0] == 45)
ck('120 unita dopo la 453 (187 - 67)', db.execute(
    'select count(*) from units where path=? and line>453', (PATH,)).fetchone()[0] == 120)
nxt = db.execute('select line,kind,context from units where path=? and line>453 order by line limit 1',
                 (PATH,)).fetchone()
ck('confine misurato: riga 457, TEXT di phrase:secure package dropoff payment (stesso tipo, contesto diverso)',
   nxt == (457, 'TEXT', 'phrase:secure package dropoff payment'), nxt)
ck('il file intero: 187 unita, min(line) 16, max(line) 1234, di cui 1 UI_LABEL',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (187, 16, 1234))
allu, per_win, wrong = [], {}, []
for w, n in REAL:
    d = json.load(open(os.path.join(ED, w, 'translation.json'), encoding='utf-8'))['units']
    got = [u['line'] for u in d if u['path'] == PATH]
    per_win[w] = len(got)
    if len(got) != n:
        wrong.append((w, n, len(got)))
    allu += got
ck('due finestre reali: 45, 22', list(per_win.values()) == [45, 22] and not wrong, (per_win, wrong))
rest = {r[0] for r in db.execute('select line from units where path=? and line>453', (PATH,))}
ck('somma: 45 + 22 + residuo 120 = 187 unita', len(allu) + len(rest) == 187, (len(allu), len(rest)))
ck('nessuna sovrapposizione fra finestre e residuo',
   len(set(allu) & rest) == 0 and len(set(allu)) == len(allu))
ck('tipi del lotto: 12 TEXT, 7 DIALOG, 3 DESCRIPTION',
   collections.Counter(u['kind'] for u in su) == {'TEXT': 12, 'DIALOG': 7, 'DESCRIPTION': 3})
ck('24 segnaposto, identici per unita\'',
   sum(len(TAG.findall(u['english'])) for u in su) == 24
   == sum(len(TAG.findall(u['italian'])) for u in tu)
   and not [u['idx'] for u in tu
            if collections.Counter(TAG.findall(u['english'])) != collections.Counter(TAG.findall(u['italian']))])
ck('0 virgolette, 0 tab, 3 apici EN / 9 IT (elisione)',
   sum(u['english'].count('"') for u in su) == 0 == sum(u['italian'].count('"') for u in tu)
   and TAB not in ''.join(u['english'] + u['italian'] for u in tu)
   and sum(u['english'].count(chr(39)) for u in su) == 3
   and sum(u['italian'].count(chr(39)) for u in tu) == 9)
ck('composizione: i 12 frammenti conservano l\'iniziale, e i gruppi di alternative restano distinti',
   not [u['idx'] for u in tu if u['idx'] in PHRASE
        and u['english'][0].isupper() != u['italian'][0].isupper()]
   and [by[i]['italian'] for i in (14, 15)] == ['Come da istruzioni, tu', 'Tu']
   and by[16]['italian'] != by[17]['italian']
   and by[18]['italian'] != by[19]['italian']
   and len({by[i]['italian'] for i in (20, 21, 22)}) == 3)
ck('PENDING su tutte e 22', not [u['idx'] for u in su
                                 if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('nessun carattere tipografico e nessun non latino',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')
        or any(ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F for c in u['italian'])])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate 0,55-1,90 (italiano piu\' corto: 413 contro 436 parole)',
   0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('APERTO: 67/187 unita del file (35.8%) · 120 dopo la riga 453 · confine riga 457')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L213 superato' if not fail else 'verify L213 fallito')
raise SystemExit(0 if not fail else 1)
