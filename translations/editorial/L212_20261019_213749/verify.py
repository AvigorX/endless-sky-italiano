r"""verify.py — L212 (`data/human/deep jobs.txt`, 45 unita', righe 16-322). **Primo lotto del file.**

Non ci sono finestre precedenti: le unita' prima della 16 sono **zero**, misurato. Dopo la 322 restano **142** unita'
(187 - 45), di cui **1 `UI_LABEL`** che non si traduce.

**Confine**: riga **333**, `DIALOG` di `mission:Transport scientists` — **dodici righe dopo** la 322, perche' fra le due
c'e' un blocco `LOGBOOK`/`MISSION_TEXT` che entra nel lotto successivo. Il tipo cambia (`DESCRIPTION` -> `DIALOG`), quindi
il controllo misura tipo e contesto.

**Segnaposto**: 31 su 6 simboli, confrontati **per unita'**.
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
REAL = [('L212_20261019_213749', 45)]
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


ck('riga grezza identica al sorgente (45/45)', not [u for u in su if lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck('unita: 45 righe 16 - 322', len(tu) == 45 and (tu[0]['line'], tu[-1]['line']) == (16, 322))
ck('ZERO unita prima della 16 (primo lotto del file, misurato)',
   db.execute('select count(*) from units where path=? and line<16', (PATH,)).fetchone()[0] == 0)
ck('142 unita dopo la 322 (187 - 45)', db.execute(
    'select count(*) from units where path=? and line>322', (PATH,)).fetchone()[0] == 142)
nxt = db.execute('select line,kind,context from units where path=? and line>322 order by line limit 1',
                 (PATH,)).fetchone()
ck('confine misurato: riga 333, DIALOG di mission:Transport scientists (il tipo cambia)',
   nxt == (333, 'DIALOG', 'mission:Transport scientists'), nxt)
ck('il file intero: 187 unita, min(line) 16, max(line) 1234, di cui 1 UI_LABEL',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (187, 16, 1234)
   and db.execute('select count(*) from units where path=? and kind="UI_LABEL"', (PATH,)).fetchone()[0] == 1,
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone())
allu, per_win = [], {}
for w, n in REAL:
    d = json.load(open(os.path.join(ED, w, 'translation.json'), encoding='utf-8'))['units']
    got = [u['line'] for u in d if u['path'] == PATH]
    per_win[w] = len(got)
    allu += got
ck('una finestra reale: 45 unita', list(per_win.values()) == [45], per_win)
rest = {r[0] for r in db.execute('select line from units where path=? and line>322', (PATH,))}
ck('somma: 45 + residuo 142 = 187 unita', len(allu) + len(rest) == 187, (len(allu), len(rest)))
ck('nessuna sovrapposizione fra finestra e residuo', len(set(allu) & rest) == 0)
ck('tipi del lotto: 28 TEXT, 8 VALUE, 9 DESCRIPTION',
   collections.Counter(u['kind'] for u in su) == {'TEXT': 28, 'VALUE': 8, 'DESCRIPTION': 9})
ck('31 segnaposto, identici per unita\' (multiset, non totale)',
   sum(len(TAG.findall(u['english'])) for u in su) == 31
   == sum(len(TAG.findall(u['italian'])) for u in tu)
   and not [u['idx'] for u in tu
            if collections.Counter(TAG.findall(u['english'])) != collections.Counter(TAG.findall(u['italian']))])
ck('8 VALUE identici all\'inglese; 4 virgolette in 19 e 27; spazio iniziale conservato in 19 e 27',
   all(u['italian'] == u['english'] for u in tu if u['kind'] == 'VALUE')
   and sum(u['english'].count('"') for u in su) == 4 == sum(u['italian'].count('"') for u in tu)
   and [u['idx'] for u in tu if u['italian'].startswith(' ')] == [19, 27])
ck('composizione: i 28 frammenti `phrase:` conservano la maiuscola iniziale dell\'inglese',
   not [u['idx'] for u in tu if u['idx'] in PHRASE
        and u['english'][0].isupper() != u['italian'][0].isupper()])
ck('PENDING su tutte e 45', not [u['idx'] for u in su
                                 if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('nessun carattere tipografico e nessun non latino',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')
        or any(ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F for c in u['italian'])])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate 0,55-1,90', 0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('APERTO: 45/187 unita del file (24.1%) · 142 dopo la riga 322 · confine riga 333 (DIALOG)')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L212 superato' if not fail else 'verify L212 fallito')
raise SystemExit(0 if not fail else 1)
