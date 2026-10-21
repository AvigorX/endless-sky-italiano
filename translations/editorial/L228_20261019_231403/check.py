r"""check.py — L228 (`data/korath/korath outfits.txt`, 20 unita', righe 16-195). **Primo lotto del file.**

**File misto**: 29 `VALUE` e 63 `DESCRIPTION` in tutto; la finestra ne prende **7 + 13**, quindi il confronto e' **7
identiche / 13 tradotte**. Non e' ne' un file di soli nomi (`successor ships.txt`) ne' di sola prosa (`remnant outfits.txt`):
e' la prima volta che i due tipi convivono in un lotto in proporzione simile, e il controllo li distingue uno per uno.

**Due primati negativi, entrambi asseriti**:
- **zero tab** — ogni lotto della campagna finora ne aveva almeno uno;
- **zero virgolette** — terzo lotto consecutivo.

Un controllo che tace su uno zero non distingue «non ce ne sono» da «non li ho guardati».

**La linea fra nome e parola comune**: `Systems Core`, `Plasma Core`, `Fusion Reactor` (maiuscolo, nome di equipaggiamento
presente anche nel database) restano inglesi; `fusion reactor` minuscolo dell'unita' 9 e' una parola comune e si traduce
(«reattore a fusione»). Il controllo verifica **entrambe** le forme.
"""
import collections
import json
import os
import re
import sqlite3

TAB = chr(9)
QUOTE = chr(34)
APOS = chr(39)
TAG = re.compile(r'<[^<>]+>')
HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
PATH = 'data/korath/korath outfits.txt'
src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
units = sorted(src['units'], key=lambda x: x['line'])
tr = {}
parts = sorted(f for f in os.listdir(os.path.join(HERE, 'parts')) if f.endswith('.json'))
for p in parts:
    for k, v in json.load(open(os.path.join(HERE, 'parts', p), encoding='utf-8')).items():
        tr[int(k)] = v
out = {'block': src['block'], 'note': src['note'], 'units': []}
for u in units:
    if u['idx'] not in tr:
        continue
    it = tr[u['idx']]
    out['units'].append({"idx": u['idx'], "id": u['id'], "path": u['path'], "line": u['line'],
                         "kind": u['kind'], "context": u['context'], "english": u['english'],
                         "italian": it, "ratio": round(len(it) / max(1, len(u['english'])), 3)})
open(os.path.join(HERE, 'translation.json'), 'w', encoding='utf-8').write(
    json.dumps(out, ensure_ascii=False, indent=1))
cov = out['units']
by = {v['idx']: v for v in cov}
IT_ALL = ' '.join(v['italian'] for v in cov)
KINDS = collections.Counter(u['kind'] for u in units)
CTX = collections.Counter(u['context'] for u in units)
VALS = [u['idx'] for u in units if u['kind'] == 'VALUE']
DESCS = [u['idx'] for u in units if u['kind'] == 'DESCRIPTION']
EN_A = [(v['idx'], v['english'].count(APOS)) for v in cov if APOS in v['english']]
IT_A = [(v['idx'], v['italian'].count(APOS)) for v in cov if APOS in v['italian']]
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 20/20", len(cov) == 20 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 7 VALUE e 13 DESCRIPTION (file misto, asserzione scritta)',
   KINDS == {'VALUE': 7, 'DESCRIPTION': 13}, dict(KINDS))
ck('ZERO TEXT, DIALOG, MISSION_TEXT, LOGBOOK, NEWS, UI_LABEL (asserzioni vuote scritte)',
   [u['idx'] for u in units if u['kind'] not in ('VALUE', 'DESCRIPTION')] == [])
ck('13 contesti: i tre Generator e i quattro Systems Core hanno 2 unita\', gli altri 1',
   len(CTX) == 13 and CTX == {'outfit:Generator (Candle Class)': 2, 'outfit:Generator (Furnace Class)': 2,
                              'outfit:Generator (Inferno Class)': 2, 'outfit:Plasma Core': 1,
                              'outfit:Double Plasma Core': 1, 'outfit:Triple Plasma Core': 1,
                              'outfit:Small Heat Shunt': 1, 'outfit:Large Heat Shunt': 1,
                              'outfit:Liquid Sodium Cooler': 1, 'outfit:Systems Core (Tiny)': 2,
                              'outfit:Systems Core (Small)': 2, 'outfit:Systems Core (Medium)': 2,
                              'outfit:Systems Core (Large)': 2}, dict(CTX))
ck('righe 16 e 195 (prima e ultima del lotto)',
   (cov[0]['line'], cov[-1]['line']) == (16, 195), (cov[0]['line'], cov[-1]['line']))
ck('PRIMO LOTTO DEL FILE: 0 unita prima della 16', not [u for u in units if u['line'] < 16])
ck('ZERO tab nel lotto, in inglese e in italiano: primato della campagna, asserito',
   sum(v['english'].count(TAB) for v in cov) == 0 == sum(v['italian'].count(TAB) for v in cov))
ck('ZERO virgolette nel lotto, in inglese e in italiano: terzo lotto consecutivo',
   sum(v['english'].count(QUOTE) for v in cov) == 0 == sum(v['italian'].count(QUOTE) for v in cov))
ck('NESSUN segnaposto (asserzione negativa scritta)',
   sum(len(TAG.findall(v['english'])) for v in cov) == 0 == sum(len(TAG.findall(v['italian'])) for v in cov))
ck('7 unita\' IDENTICHE all\'inglese (tutti e soli i VALUE) e 13 tradotte (tutte e sole le DESCRIPTION)',
   sum(1 for v in cov if v['italian'] == v['english']) == 7
   and sorted(v['idx'] for v in cov if v['italian'] == v['english']) == VALS
   and sorted(v['idx'] for v in cov if v['italian'] != v['english']) == DESCS,
   (sorted(v['idx'] for v in cov if v['italian'] == v['english']), VALS))
ck('i 7 VALUE sono copiati alla lettera («Generators (Candle Class)», «Systems Cores (Tiny)»…)',
   VALS == [1, 3, 5, 13, 15, 17, 19]
   and all(by[i]['italian'] == by[i]['english'] for i in VALS)
   and by[1]['italian'] == 'Generators (Candle Class)' and by[13]['italian'] == 'Systems Cores (Tiny)')
ck('i nomi restano inglesi nella prosa (Systems Core, Plasma Core, Fusion Reactor)',
   'Systems Core' in IT_ALL and 'Plasma Core' in IT_ALL and 'Fusion Reactor' in IT_ALL)
ck('ma «fusion reactor» minuscolo dell\'unita\' 9 e\' parola comune e si traduce',
   'reattore a fusione' in by[9]['italian'] and 'fusion reactor' in by[9]['english'].lower()
   and 'reattore a fusione' not in by[7]['italian'])
ck('terminologia: «generatore radiotermico», «calore disperso», «microbot», «condensatore», «navi capitali»',
   'generatore radiotermico' in IT_ALL and 'calore disperso' in IT_ALL and 'microbot' in IT_ALL
   and 'condensatore' in IT_ALL and 'navi capitali' in IT_ALL)
ck('nessun residuo inglese di struttura (the, of the, and, with, their)',
   not [w for w in (' the ', ' of the ', ' and ', ' with ', ' their ', ' while ', ' that they ')
        if w in IT_ALL.lower()],
   [w for w in (' the ', ' of the ', ' and ', ' with ', ' their ', ' while ', ' that they ') if w in IT_ALL.lower()])
ck("apici: 3 in inglese (12 ship's, 16 ship's, 18 ship's) e 3 in italiano (6 l'impatto, 16 l'energia, 18 sull'esterno)",
   sum(n for _, n in EN_A) == 3 and sum(n for _, n in IT_A) == 3
   and EN_A == [(12, 1), (16, 1), (18, 1)] and IT_A == [(6, 1), (16, 1), (18, 1)], (EN_A, IT_A))
ck('registro: nessun «Lei» e nessun «mi scusi»', not re.search(r'\bLei\b|mi scusi', IT_ALL))
ck('nessun caporale e nessun carattere tipografico',
   not [v['idx'] for v in cov if any(c in v['italian'] for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026')])
rs = [v['ratio'] for v in cov]
ck('rapporto nel gate 0,55-1,90 (1,00 per i nomi, 1,03-1,26 per le DESCRIPTION)',
   0.55 < min(rs) and max(rs) < 1.90, '%.2f - %.2f' % (min(rs), max(rs)))
ACC = re.compile(r"\b(e|piu|perche|cosi|gia|puo|cioe|percio|fa)'", re.I)
bad = [(v['idx'], ACC.search(v['italian']).group(0)) for v in cov if ACC.search(v['italian'])]
ck('tipografia (accenti veri, nessun apostrofo al posto dell\'accento)', not bad, bad)
nonlat = [v['idx'] for v in cov for c in v['italian'] if ord(c) > 127 and not 0x00C0 <= ord(c) <= 0x024F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio',
   not [v['idx'] for v in cov if v['italian'] != v['italian'].rstrip()
        or '  ' in v['italian'] or v['english'] != v['english'].rstrip()])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck('il file ha 92 unita, 29 VALUE e 63 DESCRIPTION',
   db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0] == 92
   and db.execute('select kind,count(*) from units where path=? group by kind',
                  (PATH,)).fetchall() == [('DESCRIPTION', 63), ('VALUE', 29)])
ck('lotto + residuo = file: 20 + 72 = 92',
   20 + db.execute('select count(*) from units where path=? and line>195', (PATH,)).fetchone()[0] == 92)
st = dict(db.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('le 20 unita sono PENDING (misurato)',
   db.execute('select count(*) from units where id in (%s) and state != "PENDING"'
              % ','.join('?' * len(units)), [u['id'] for u in units]).fetchone()[0] == 0)
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d' % (sum(len(v['english'].split()) for v in cov),
                                sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
