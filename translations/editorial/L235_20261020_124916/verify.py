r"""verify.py — L235 (`data/avgi/avgi news.txt`, 15 unita', righe 197-280). Terzo lotto del file.

**Invariante di SEGMENTO**: il lotto non chiude il file (115 unita'). **42** prima (L233 22 + L234 20), **15** qui,
**58** dopo la 280. Copertura **stampata** (57/115, 49,6%), non asserita.

**Il lotto verifica la composizione, non le frasi**: 6 prefissi x 7 messaggi = **42 combinazioni**, controllate una per
una in inglese e in italiano (virgoletta in testa, virgoletta in coda, due virgolette in tutto, nessun doppio spazio,
etichetta chiusa da `. `). E' la regola di `Phrase::Get()` letta nel sorgente del gioco: i blocchi si **concatenano**
senza separatore, quindi lo spazio finale del prefisso e' testo, non impaginazione.

**La lacuna dell'inventario e' verificata qui, sul file del gioco**: fra la riga 231 e la 279 di
`data/avgi/avgi news.txt` ci sono i **tredici** blocchi `word` del `missing advisory` (di cui il database conserva solo il primo e l'ultimo) (`Convoy`, `reported lost`,
`the Demilude system`…), ma il database **non ha nessuna unita'** in quell'intervallo. Le due unita' estratte (la
virgoletta e il punto) sono l'inizio e la fine di un testo che resta quasi tutto in inglese: si dichiara, non si ripara
(`tools/l10n.py` e `state.db` sono protetti).

Indipendente da `check.py`: rilegge `source.json`, il `translation.json`, il database e il sorgente del gioco.
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
PATH = 'data/avgi/avgi news.txt'
PREFIX = list(range(1, 7))
MSG = list(range(7, 14))
su = sorted(json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
raw_lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
by = {u['idx']: u for u in tu}
fail = []


def ck(n, c, d=''):
    print('%-78s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente (15/15)', not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck('unita: 15 righe 197 - 280', len(tu) == 15 and (tu[0]['line'], tu[-1]['line']) == (197, 280))
ck("42 unita' prima della 197 (L233 22 + L234 20)",
   db.execute('select count(*) from units where path=? and line<197', (PATH,)).fetchone()[0] == 42)
ck("58 unita' dopo la 280: il lotto NON chiude il file",
   db.execute('select count(*) from units where path=? and line>280', (PATH,)).fetchone()[0] == 58)
nxt = db.execute('select line,kind,context from units where path=? and line>280 order by line limit 1', (PATH,)).fetchone()
ck('confine misurato: riga 301, NEWS di news:avgi student happy',
   nxt == (301, 'NEWS', 'news:avgi student happy'), nxt)
ck('il file intero: 115 unita, righe 32 - 507',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (115, 32, 507))
per, lines = [], []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    d = json.load(open(f, encoding='utf-8'))
    us = [u for u in d['units'] if u['path'] == PATH]
    if us:
        per.append((os.path.basename(os.path.dirname(f)), len(us)))
        lines += [u['line'] for u in us]
mine = set(u['line'] for u in tu)
overlap = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    lot = os.path.basename(os.path.dirname(f))
    if lot == os.path.basename(HERE):
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH and u['line'] in mine:
            overlap.append((lot, u['line']))
ck("nessun ALTRO lotto rivendica le righe di questo segmento (invariante di segmento: 15 righe distinte)",
   not overlap and len(mine) == 15, (overlap, len(mine)))
ck('tipi del lotto: 15 NEWS', collections.Counter(u['kind'] for u in su) == {'NEWS': 15})
ck("13 unita' tradotte e 2 identiche per necessita' (la virgoletta e il punto)",
   sum(1 for u in tu if u['italian'] != u['english']) == 13
   and [u['idx'] for u in tu if u['italian'] == u['english']] == [14, 15]
   and by[14]['italian'] == '"' and by[15]['italian'] == '.')
ck('14 virgolette, una per unita\' tranne il punto finale, e nessun tab',
   sum(u['english'].count(QUOTE) for u in su) == 14 == sum(u['italian'].count(QUOTE) for u in tu)
   and by[15]['italian'].count(QUOTE) == 0
   and sum(u['english'].count(TAB) for u in su) == 0 == sum(u['italian'].count(TAB) for u in tu))
ck("lo spazio finale e' dei soli 6 prefissi, identico nelle due lingue",
   [i for i in sorted(by) if by[i]['english'].endswith(' ')] == PREFIX
   == [i for i in sorted(by) if by[i]['italian'].endswith(' ')])
EN_COMP = [by[p]['english'] + by[m]['english'] for p in PREFIX for m in MSG]
IT_COMP = [by[p]['italian'] + by[m]['italian'] for p in PREFIX for m in MSG]
ck('42 combinazioni valide in inglese e in italiano (virgolette, punto dell\'etichetta, nessun doppio spazio)',
   len(EN_COMP) == len(IT_COMP) == 42
   and all(s.startswith('"') and s.endswith('"') and s.count('"') == 2 and '  ' not in s and '. ' in s
           for s in EN_COMP + IT_COMP))
ck('nessuna combinazione italiana comincia con minuscola dopo l\'etichetta',
   all(s.split('. ', 1)[1][0].isupper() for s in IT_COMP))
ck('0 segnaposto', sum(len(TAG.findall(u['english'])) for u in su) == 0
   == sum(len(TAG.findall(u['italian'])) for u in tu))
ck('nome invariato con gli stessi conteggi (Tangled Shroud 5, Arche 1)',
   ' '.join(u['italian'] for u in tu).count('Tangled Shroud')
   == ' '.join(u['english'] for u in su).count('Tangled Shroud') == 5
   and ' '.join(u['italian'] for u in tu).count('Arche') == 1)
ck("LACUNA verificata sul sorgente del gioco: fra la 231 e la 279 ci sono i blocchi `word` del "
   "`missing advisory`, ma il database non ha NESSUNA unita' in quell'intervallo",
   db.execute('select count(*) from units where path=? and line between 231 and 279', (PATH,)).fetchone()[0] == 0
   and any('Convoy' in raw_lines[i] for i in range(230, 279))
   and any('the Demilude system' in raw_lines[i] for i in range(230, 279)))
ck('PENDING su tutte e 15', not [u['idx'] for u in su
                                 if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('nessun doppio spazio e nessuno spazio iniziale; spazio finale solo dove e\' struttura',
   not [u['idx'] for u in tu if '  ' in u['italian'] or u['italian'] != u['italian'].lstrip()
        or (u['italian'] != u['italian'].rstrip() and u['idx'] not in PREFIX)])
ck('nessun carattere tipografico e nessun non latino',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')
        or any(ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F for c in u['italian'])])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate 0,55-1,90 (0,69 - 1,30; 72 -> 68 parole)',
   0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('SEGMENTO: 57/115 unita\' del file (%.1f%%) · 42 prima · 15 qui · 58 dopo · confine riga 301'
      % (100.0 * len(lines) / 115))
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L235 superato' if not fail else 'verify L235 fallito')
raise SystemExit(0 if not fail else 1)
