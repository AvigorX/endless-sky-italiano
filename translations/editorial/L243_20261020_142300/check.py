r"""check.py — L243 (`data/hai/hai ships.txt`, 29 unita', righe 15-332). Primo lotto del file.

**File MISTO** (come `successor ships.txt`, L218–L222): **1 `VALUE`** (`Anomalocarises`, nome di nave al plurale),
**23 `TEXT`** che sono **nomi di equipaggiamento con le virgolette dentro** (`"Biroo" Atomic Thruster`) e **5
`DESCRIPTION`** che sono prosa. Si copiano i primi due tipi e si traduce solo la prosa.

**Le 48 virgolette stanno nei nomi e in un motto**: 2 per ciascuna delle 23 `TEXT` (46) piu' le 2 del motto
`"Service for Life."` nella scheda della Cicada (unita' 29). Il confronto e' **per unita'**: una virgoletta spostata
dentro un nome darebbe lo stesso totale.

**Gli apici sono 4 in inglese e 19 in italiano**: gli inglesi sono i possessivi `Hai's` (4, 7), `project's` (20) e
`shipyard's` (29); in italiano il possessivo sparisce e restano **elisioni** (`l'Anomalocaris`, `dell'economia`,
`l'hanno`), piu' due in una unita' che in inglese non ne aveva nessuna (10, `L'Aphid`).
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
PATH = 'data/hai/hai ships.txt'
src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
units = sorted(src['units'], key=lambda x: x['line'])
tr = {}
for p in sorted(f for f in os.listdir(os.path.join(HERE, 'parts')) if f.endswith('.json')):
    for k, v in json.load(open(os.path.join(HERE, 'parts', p), encoding='utf-8')).items():
        tr[int(k)] = v
out = {'block': src['block'], 'note': src['note'], 'units': []}
for u in units:
    if u['idx'] in tr:
        it = tr[u['idx']]
        out['units'].append({"idx": u['idx'], "id": u['id'], "path": u['path'], "line": u['line'],
                             "kind": u['kind'], "context": u['context'], "english": u['english'],
                             "italian": it, "ratio": round(len(it) / max(1, len(u['english'])), 3)})
open(os.path.join(HERE, 'translation.json'), 'w', encoding='utf-8').write(
    json.dumps(out, ensure_ascii=False, indent=1))
cov = out['units']
DATA = [v for v in cov if v['kind'] in ('VALUE', 'TEXT')]
DES = [v for v in cov if v['kind'] == 'DESCRIPTION']
Q_EN = [(v['idx'], v['english'].count(QUOTE)) for v in cov if QUOTE in v['english']]
Q_IT = [(v['idx'], v['italian'].count(QUOTE)) for v in cov if QUOTE in v['italian']]
A_EN = [(v['idx'], v['english'].count(APOS)) for v in cov if APOS in v['english']]
A_IT = [(v['idx'], v['italian'].count(APOS)) for v in cov if APOS in v['italian']]
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 29/29", len(cov) == 29 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna unita\' vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 1 VALUE + 23 TEXT + 5 DESCRIPTION',
   collections.Counter(u['kind'] for u in units) == {'VALUE': 1, 'TEXT': 23, 'DESCRIPTION': 5},
   dict(collections.Counter(u['kind'] for u in units)))
ck('4 contesti: Anomalocaris, Aphid, Centipede, Cicada',
   set(u['context'] for u in units) == {'ship:Anomalocaris', 'ship:Aphid', 'ship:Centipede', 'ship:Cicada'},
   sorted(set(u['context'] for u in units)))
ck('righe 15 e 332 (prima e ultima del lotto)',
   (cov[0]['line'], cov[-1]['line']) == (15, 332), (cov[0]['line'], cov[-1]['line']))
ck('ZERO tab (asserzione negativa scritta)',
   sum(v['english'].count(TAB) for v in cov) == 0 == sum(v['italian'].count(TAB) for v in cov))
ck("i 24 dati (1 VALUE + 23 TEXT) sono IDENTICI all'inglese, per indice",
   all(v['italian'] == v['english'] for v in DATA) and len(DATA) == 24,
   [v['idx'] for v in DATA if v['italian'] != v['english']])
ck("le 5 DESCRIPTION sono TUTTE tradotte (0 identiche)",
   all(v['italian'] != v['english'] for v in DES) and len(DES) == 5)
ck('i 23 nomi di equipaggiamento hanno le virgolette: il controllo e\' per unita\'',
   Q_EN == Q_IT == [(i, 2) for i in [2, 3, 5, 6, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19,
                                     21, 22, 23, 24, 25, 26, 27, 28, 29]], (Q_EN, Q_IT))
ck('48 virgolette in tutto: 46 nei 23 nomi + 2 nel motto della Cicada',
   sum(n for _, n in Q_IT) == 48
   and sum(1 for v in cov if v['kind'] == 'TEXT' and v['italian'].count(QUOTE) == 2) == 23
   and sum(1 for v in cov if v['kind'] == 'DESCRIPTION' and v['italian'].count(QUOTE) == 2) == 1,
   sum(n for _, n in Q_IT))
ck('il motto `"Service for Life."` e\' tradotto, fra virgolette e col punto dentro',
   '"Al servizio per tutta la vita."' in [v['italian'] for v in DES if v['line'] == 332][0]
   and 'Service for Life' not in ' '.join(v['italian'] for v in cov))
ck("apici: 4 in inglese (possessivi) su 4 unita' e 19 in italiano su 5",
   sum(n for _, n in A_EN) == 4 and A_EN == [(4, 1), (7, 1), (20, 1), (29, 1)]
   and sum(n for _, n in A_IT) == 19 and A_IT == [(4, 5), (7, 6), (10, 2), (20, 3), (29, 3)], (A_EN, A_IT))
ck("il possessivo inglese sparisce: `Hai's` -> «degli Hai», `project's` -> «il suo», `shipyard's` -> «del cantiere»",
   "Hai's" not in ' '.join(v['italian'] for v in cov)
   and "project's" not in ' '.join(v['italian'] for v in cov)
   and "shipyard's" not in ' '.join(v['italian'] for v in cov)
   and 'degli Hai' in ' '.join(v['italian'] for v in DES) and 'del cantiere' in ' '.join(v['italian'] for v in DES))
ck('stesso inglese => stessa resa, nei 7 gruppi di duplicati',
   all(len({v['italian'] for v in cov if v['english'] == k}) == 1
       for k, n in collections.Counter(v['english'] for v in cov).items() if n > 1)
   and sum(1 for k, n in collections.Counter(v['english'] for v in cov).items() if n > 1) == 7)
ck("NESSUN segnaposto (asserzione negativa scritta)",
   sum(len(TAG.findall(v['english'])) for v in cov) == 0 == sum(len(TAG.findall(v['italian'])) for v in cov))
ck('nomi propri invariati nella prosa: Sheragi, Anomalocaris, Aphid, Centipede, Cicada, Scarab, Yeer e Ki',
   all(n in ' '.join(v['italian'] for v in DES) for n in
       ('Sheragi', 'Anomalocaris', 'Aphid', 'Centipede', 'Cicada', 'Scarab', 'Yeer e Ki')))
ck('parole comuni tradotte: «navi da guerra», «mercantile», «capacità di carico», «spazio per i motori», «spina dorsale»',
   all(t in ' '.join(v['italian'] for v in DES) for t in
       ('navi da guerra', 'mercantile', 'capacità di carico', 'spazio per i motori', 'spina dorsale')))
ck('nessun residuo inglese di struttura (the, and, with, for, from, that)',
   not [w for w in (' the ', ' and ', ' with ', ' for ', ' from ', ' that ')
        if w in ' '.join(v['italian'] for v in DES).lower()],
   [w for w in (' the ', ' and ', ' with ', ' for ', ' from ', ' that ')
    if w in ' '.join(v['italian'] for v in DES).lower()])
ck('registro: nessun «Lei» e nessuna cortesia',
   not re.search(r'\bLei\b|\bSuo\b|\bSua\b|mi scusi', ' '.join(v['italian'] for v in cov)))
ck('nessun caporale e nessun carattere tipografico',
   not [v['idx'] for v in cov if any(c in v['italian'] for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026')])
rs = [v['ratio'] for v in cov]
ck('rapporto nel gate 0,55-1,90 (1,00-1,09; 451 -> 456 parole)',
   0.55 < min(rs) and max(rs) < 1.90, '%.2f - %.2f' % (min(rs), max(rs)))
ACC = re.compile(r"\b(e|piu|perche|cosi|gia|puo|cioe|percio)'(?![a-z])", re.I)
bad = [(v['idx'], ACC.search(v['italian']).group(0)) for v in cov if ACC.search(v['italian'])]
ck("tipografia (accenti veri, nessun apostrofo al posto dell'accento)", not bad, bad)
nonlat = [v['idx'] for v in cov for c in v['italian'] if ord(c) > 127 and not 0x00C0 <= ord(c) <= 0x024F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio',
   not [v['idx'] for v in cov if v['italian'] != v['italian'].rstrip() or '  ' in v['italian']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("ZERO unita' prima della riga 15: il lotto APRE il file",
   db.execute('select count(*) from units where path=? and line<15', (PATH,)).fetchone()[0] == 0)
ck("128 unita' dopo la 332 (157 - 29): il lotto NON chiude il file",
   db.execute('select count(*) from units where path=? and line>332', (PATH,)).fetchone()[0] == 128)
ck('confine misurato: riga 362, ship:Flea',
   db.execute('select line,context from units where path=? and line>332 order by line limit 1', (PATH,)).fetchone()
   == (362, 'ship:Flea'))
ck('il file intero: 157 unita, righe 15 - 1860',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (157, 15, 1860))
st = dict(db.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('le 29 unita sono PENDING (misurato)',
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
