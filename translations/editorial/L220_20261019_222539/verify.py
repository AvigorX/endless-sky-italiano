r"""verify.py — L220 (`data/successors/successor ships.txt`, 26 unita', righe 634-873). Terzo lotto del file.

Terzo lotto: **70** unita' tradotte prima della 634 (L218 45 + L219 25), **26** in questo, **50** dopo la 873.

    70 + 26 + 50 = 146  (le unita' del file)

Confine: riga **904**, contesto `ship:Seiitej`, tipo **`TEXT`** — non un `VALUE`, come nei lotti precedenti. Il controllo
assersce il tipo, perche' «la prima unita' dopo e' un `VALUE`» sarebbe vero in quasi tutti i lotti e falso in questo.

**Coppia 23/25**: stesso testo, differenza di **due virgolette**. Verificata in entrambe le lingue.
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
PATH = 'data/successors/successor ships.txt'
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
ck('unita: 26 righe 634 - 873', len(tu) == 26 and (tu[0]['line'], tu[-1]['line']) == (634, 873))
ck('70 unita tradotte prima della 634 (L218 45 + L219 25)', db.execute(
    'select count(*) from units where path=? and line<634', (PATH,)).fetchone()[0] == 70)
ck('50 unita dopo la 873 (146 - 96)', db.execute(
    'select count(*) from units where path=? and line>873', (PATH,)).fetchone()[0] == 50)
nxt = db.execute('select line,kind,context from units where path=? and line>873 order by line limit 1',
                 (PATH,)).fetchone()
ck('confine misurato: riga 904, TEXT (NON VALUE) di ship:Seiitej, trentuno righe dopo',
   nxt == (904, 'TEXT', 'ship:Seiitej'), nxt)
ck('il file intero: 146 unita, righe 17 - 1338',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (146, 17, 1338))
ck('lotto + residuo = file: 70 + 26 + 50 = 146',
   70 + len(tu) + db.execute('select count(*) from units where path=? and line>873',
                             (PATH,)).fetchone()[0] == 146)
ck('tipi del lotto: 16 TEXT, 6 DESCRIPTION, 4 VALUE',
   collections.Counter(u['kind'] for u in su) == {'TEXT': 16, 'DESCRIPTION': 6, 'VALUE': 4})
ck('20 unita\' IDENTICHE all\'inglese + 6 tradotte = le 6 DESCRIPTION',
   sum(1 for u in tu if u['italian'] == u['english']) == 20
   and sorted(u['idx'] for u in tu if u['italian'] != u['english'])
   == sorted(u['idx'] for u in tu if u['kind'] == 'DESCRIPTION'))
ck('34 virgolette con la stessa distribuzione per unita\', comprese le 2 dell\'unita\' 23',
   sum(u['english'].count(QUOTE) for u in su) == 34 == sum(u['italian'].count(QUOTE) for u in tu)
   and {u['idx']: u['english'].count(QUOTE) for u in su if QUOTE in u['english']}
   == {u['idx']: u['italian'].count(QUOTE) for u in tu if QUOTE in u['italian']})
ck('1 tab (unita\' 24), 0 segnaposto',
   [u['idx'] for u in tu if TAB in u['italian']] == [24]
   and sum(len(TAG.findall(u['english'])) for u in su) == 0
   == sum(len(TAG.findall(u['italian'])) for u in tu))
ck('COPPIA 23/25: togliendo le virgolette i due testi coincidono, in EN e in IT',
   tu[22]['italian'].replace(QUOTE, '') == tu[24]['italian']
   and tu[22]['english'].replace(QUOTE, '') == tu[24]['english']
   and len(tu[22]['italian']) - len(tu[24]['italian']) == 2)
ck('«Bulk Freighter» e «Behemoth» invariati, due volte ciascuno',
   ' '.join(u['italian'] for u in tu).count('Bulk Freighter') == 2
   and ' '.join(u['italian'] for u in tu).count('Behemoth') == 2)
ck('PENDING su tutte e 26', not [u['idx'] for u in su
                                 if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('nessuno spazio finale e nessun doppio spazio (tab iniziale dell\'unita\' 24 ammesso)',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip()
        or '  ' in u['italian'].strip(TAB)])
ck('nessun carattere tipografico e nessun non latino',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')
        or any(ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F for c in u['italian'])])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate 0,55-1,90 (nomi 1,00; DESCRIPTION 1,05-1,16; totale 440 -> 487 parole)',
   0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('APERTO: 96/146 unita\' del file (70 + 26) · restano 50 dopo la 873 · confine riga 904 (TEXT)')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L220 superato' if not fail else 'verify L220 fallito')
raise SystemExit(0 if not fail else 1)
