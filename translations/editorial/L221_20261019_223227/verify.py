r"""verify.py — L221 (`data/successors/successor ships.txt`, 24 unita', righe 904-1137). Quarto lotto del file.

Quarto lotto: **96** unita' prima (L218 45 + L219 25 + L220 26), **24** in questo, **26** dopo la 1137.

    96 + 24 + 26 = 146  (le unita' del file)

Confine: riga **1141**, contesto `ship:Veusade`, tipo **`DESCRIPTION`**. Terzo tipo diverso in tre lotti (`VALUE` in L220,
`TEXT` in L219... qui una descrizione): il controllo asserisce tipo e contesto, non solo la riga.

Dopo la 1137 restano **26** unita': **L222 chiudera' il file** con l'invariante di file (96 + 24 + 26 = 146).
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
FIREPOWER = 'una potenza di fuoco sorprendente per una nave delle sue dimensioni'
PLAGUE = 'afflitto da problemi di energia e propulsione'
su = sorted(json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
fail = []


def ck(n, c, d=''):
    print('%-74s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente (24/24)', not [u for u in su if lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck('unita: 24 righe 904 - 1137', len(tu) == 24 and (tu[0]['line'], tu[-1]['line']) == (904, 1137))
ck('96 unita tradotte prima della 904 (L218 45 + L219 25 + L220 26)', db.execute(
    'select count(*) from units where path=? and line<904', (PATH,)).fetchone()[0] == 96)
ck('26 unita dopo la 1137 (146 - 120)', db.execute(
    'select count(*) from units where path=? and line>1137', (PATH,)).fetchone()[0] == 26)
nxt = db.execute('select line,kind,context from units where path=? and line>1137 order by line limit 1',
                 (PATH,)).fetchone()
ck('confine misurato: riga 1141, DESCRIPTION di ship:Veusade, quattro righe dopo',
   nxt == (1141, 'DESCRIPTION', 'ship:Veusade'), nxt)
ck('il file intero: 146 unita, righe 17 - 1338',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (146, 17, 1338))
ck('lotto + residuo = file: 96 + 24 + 26 = 146',
   96 + len(tu) + db.execute('select count(*) from units where path=? and line>1137',
                             (PATH,)).fetchone()[0] == 146)
ck('tipi del lotto: 15 TEXT, 7 DESCRIPTION, 2 VALUE',
   collections.Counter(u['kind'] for u in su) == {'TEXT': 15, 'DESCRIPTION': 7, 'VALUE': 2})
ck('17 unita\' IDENTICHE all\'inglese + 7 tradotte = le 7 DESCRIPTION',
   sum(1 for u in tu if u['italian'] == u['english']) == 17
   and sorted(u['idx'] for u in tu if u['italian'] != u['english'])
   == sorted(u['idx'] for u in tu if u['kind'] == 'DESCRIPTION'))
ck('30 virgolette (2 x 15 TEXT, nessuna in prosa) e 3 tab (unita\' 7, 16, 24, tutte DESCRIPTION)',
   sum(u['english'].count(QUOTE) for u in su) == 30 == sum(u['italian'].count(QUOTE) for u in tu)
   and {u['idx']: u['english'].count(QUOTE) for u in su if QUOTE in u['english']} == {u['idx']: 2 for u in su if u['kind'] == 'TEXT'}
   and [u['idx'] for u in tu if TAB in u['italian']] == [7, 16, 24]
   and all(u['kind'] == 'DESCRIPTION' for u in tu if TAB in u['italian']))
ck('0 segnaposto', sum(len(TAG.findall(u['english'])) for u in su) == 0
   == sum(len(TAG.findall(u['italian'])) for u in tu))
ck('COERENZA 15/17: potenza di fuoco e problemi di propulsione resi allo stesso modo',
   FIREPOWER in tu[14]['italian'] and FIREPOWER in tu[16]['italian']
   and PLAGUE in tu[14]['italian'] and PLAGUE in tu[16]['italian'])
ck('COERENZA 16/17: «modello riservato ai militari» identico',
   'modello riservato ai militari' in tu[15]['italian']
   and 'modello riservato ai militari' in tu[16]['italian'])
ck('PENDING su tutte e 24', not [u['idx'] for u in su
                                 if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('nessuno spazio finale e nessun doppio spazio (tab iniziali ammessi)',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip()
        or '  ' in u['italian'].strip(TAB)])
ck('nessun carattere tipografico e nessun non latino',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')
        or any(ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F for c in u['italian'])])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate 0,55-1,90 (nomi 1,00; DESCRIPTION 0,99-1,21; totale 451 -> 481 parole)',
   0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('APERTO: 120/146 unita\' del file (96 + 24) · restano 26 dopo la 1137 · L222 chiude il file')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L221 superato' if not fail else 'verify L221 fallito')
raise SystemExit(0 if not fail else 1)
