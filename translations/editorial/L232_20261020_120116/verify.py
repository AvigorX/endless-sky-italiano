r"""verify.py — L232 (`data/korath/korath outfits.txt`, 10 unita', righe 809-908). Quinto e ULTIMO lotto: **chiude il file**.

Invariante **di FILE**, letto da tutti e cinque i `translation.json` che coprono il path:

    20 (L228) + 15 (L229) + 26 (L230) + 21 (L231) + 10 (L232) = 92

Il controllo somma le unita' dei cinque lotti, pretende **92 righe distinte**, `sovrapposti = 0`, `min(line) = 16`,
`max(line) = 908`, e verifica che la riga **908** sia l'ultima riga di contenuto del file (la 909 e' vuota).

Confine: **fine file** — dopo la 908 il database non ha nessuna unita' di questo path, e la riga grezza della 908 e'
l'ultima riga non vuota di `data/korath/korath outfits.txt`.

Indipendente da `check.py`: rilegge `source.json`, il `translation.json`, il database e il sorgente del gioco; non
importa niente dal lotto e ricalcola ogni numero dal dato.
"""
import collections
import glob
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
PATH = 'data/korath/korath outfits.txt'
su = sorted(json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
raw_lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
fail = []


def ck(n, c, d=''):
    print('%-76s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente (10/10)', not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck('unita: 10 righe 809 - 908', len(tu) == 10 and (tu[0]['line'], tu[-1]['line']) == (809, 908))
ck('82 unita tradotte prima della 809 (20 + 15 + 26 + 21)',
   db.execute('select count(*) from units where path=? and line<809', (PATH,)).fetchone()[0] == 82)
ck('ZERO unita dopo la 908: il lotto chiude il file',
   db.execute('select count(*) from units where path=? and line>908', (PATH,)).fetchone()[0] == 0)
ck('la riga 908 e\' l\'ultima riga di CONTENUTO del file (la 909 e\' vuota)',
   raw_lines[907].startswith('\tdescription `') and raw_lines[907] == su[-1]['raw']
   and [x for x in raw_lines[908:] if x.strip()] == [])
ck('il file intero: 92 unita, righe 16 - 908',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (92, 16, 908))
# invariante di FILE: tutti i lotti che coprono il path
per = []
alllines = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    d = json.load(open(f, encoding='utf-8'))
    us = [u for u in d['units'] if u['path'] == PATH]
    if us:
        per.append((os.path.basename(os.path.dirname(f)), len(us)))
        alllines += [u['line'] for u in us]
ck('cinque lotti coprono il file (L228 20, L229 15, L230 26, L231 21, L232 10)',
   per == [('L228_20261019_231403', 20), ('L229_20261019_231932', 15), ('L230_20261019_232459', 26),
           ('L231_20261019_233054', 21), ('L232_20261020_120116', 10)], per)
ck('invariante di file: 20 + 15 + 26 + 21 + 10 = 92 unita\' su 92 righe distinte, sovrapposti 0',
   sum(n for _, n in per) == 92 and len(alllines) == 92 and len(set(alllines)) == 92
   and collections.Counter(alllines).most_common(1)[0][1] == 1,
   (sum(n for _, n in per), len(alllines), len(set(alllines))))
ck('copertura esatta: min(line) 16, max(line) 908, nessun buco nel conto del database',
   (min(alllines), max(alllines)) == (16, 908)
   and len(set(alllines)) == db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0])
ck('tipi del lotto: 10 DESCRIPTION', collections.Counter(u['kind'] for u in su) == {'DESCRIPTION': 10})
ck('ZERO unita identiche all\'inglese, 10 tradotte (primo lotto di sola prosa)',
   sum(1 for u in tu if u['italian'] == u['english']) == 0
   and sum(1 for u in tu if u['italian'] != u['english']) == 10)
ck('4 tab e 2 virgolette, per unita\' uguali in inglese e italiano',
   [(u['line'], u['english'].count(TAB)) for u in su if TAB in u['english']]
   == [(u['line'], u['italian'].count(TAB)) for u in tu if TAB in u['italian']]
   and sum(u['english'].count(TAB) for u in su) == 4 == sum(u['italian'].count(TAB) for u in tu)
   and sum(u['english'].count(QUOTE) for u in su) == 2 == sum(u['italian'].count(QUOTE) for u in tu)
   and [u['idx'] for u in tu if QUOTE in u['italian']] == [10])
ck('0 segnaposto', sum(len(TAG.findall(u['english'])) for u in su) == 0
   == sum(len(TAG.findall(u['italian'])) for u in tu))
ck('nomi di scena: Quarg, Efreti, Korath con gli stessi conteggi dell\'inglese',
   ' '.join(u['italian'] for u in tu).count('Quarg') == ' '.join(u['english'] for u in su).count('Quarg')
   and ' '.join(u['italian'] for u in tu).count('Efreti') == ' '.join(u['english'] for u in su).count('Efreti')
   and ' '.join(u['italian'] for u in tu).count('Korath') == ' '.join(u['english'] for u in su).count('Korath'))
ck('PENDING su tutte e 10', not [u['idx'] for u in su
                                 if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('nessun carattere tipografico e nessun non latino',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')
        or any(ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F for c in u['italian'])])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate 0,55-1,90 (1,04 - 1,25; 454 -> 508 parole)',
   0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('FILE CHIUSO: 92/92 unita\' di `%s` (5 lotti: 20+15+26+21+10) · max(line) 908' % PATH)
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L232 superato' if not fail else 'verify L232 fallito')
raise SystemExit(0 if not fail else 1)
