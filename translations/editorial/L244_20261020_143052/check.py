r"""check.py — L244 (`data/hai/hai ships.txt`, 45 unita', righe 362-885). Secondo lotto del file.

**File MISTO** (regola di L243): **1 `VALUE`** (`Geocoris`), **36 `TEXT`** (nomi di equipaggiamento con le virgolette
dentro) e **8 `DESCRIPTION`** (prosa). Si copiano i primi due tipi, si traduce solo la prosa.

**Il tab e' uno solo e sta all'inizio della unita' 3** (`\tDrones do not come equipped with a hyperdrive...`): e' un
rientro di nota a pie' di scheda, e va conservato **come primo carattere**. Il `check.py` lo verifica **per unita'**,
non sul totale.

**Le 72 virgolette** sono 2 per ciascuno dei 36 nomi; **nel lotto non c'e' nessun altro uso delle virgolette** (ne' citazioni
ne' motti: le 8 schede non ne contengono). Il confronto e' per unita'.

**Gli apici sono 0 in inglese e 3 in italiano**: tre elisioni, una per scheda — «l'umanita'» (9), «un'epoca» (34),
«l'autonomia» (35). In inglese nessuna delle 45 unita' ne contiene uno.
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
TAB_UNITS = [(v['idx'], v['english'].count(TAB), v['italian'].count(TAB)) for v in cov if TAB in v['english'] or TAB in v['italian']]
Q_EN = [(v['idx'], v['english'].count(QUOTE)) for v in cov if QUOTE in v['english']]
Q_IT = [(v['idx'], v['italian'].count(QUOTE)) for v in cov if QUOTE in v['italian']]
A_IT = [(v['idx'], v['italian'].count(APOS)) for v in cov if APOS in v['italian']]
prosa = ' '.join(v['italian'] for v in DES)
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 45/45", len(cov) == 45 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna unita\' vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 1 VALUE + 36 TEXT + 8 DESCRIPTION',
   collections.Counter(u['kind'] for u in units) == {'VALUE': 1, 'TEXT': 36, 'DESCRIPTION': 8},
   dict(collections.Counter(u['kind'] for u in units)))
ctx = set(u['context'] for u in units)
ck('6 contesti: Flea, Geocoris, Grasshopper, Lightning Bug, Ladybug, Pond Strider',
   ctx == {'ship:Flea', 'ship:Geocoris', 'ship:Grasshopper', 'ship:Lightning Bug', 'ship:Ladybug',
           'ship:Pond Strider'} and len(ctx) == 6, sorted(ctx))
ck('righe 362 e 885 (prima e ultima del lotto)',
   (cov[0]['line'], cov[-1]['line']) == (362, 885), (cov[0]['line'], cov[-1]['line']))
ck('il tab e\' UNO e sta all\'inizio della unita\' 3, in entrambe le lingue',
   TAB_UNITS == [(3, 1, 1)] and cov[2]['italian'].startswith(TAB) and cov[2]['english'].startswith(TAB),
   TAB_UNITS)
ck("la nota col tab e' tradotta e non identica all'inglese",
   cov[2]['italian'] != cov[2]['english'] and 'Drones' not in cov[2]['italian'])
ck("i 37 dati (1 VALUE + 36 TEXT) sono IDENTICI all'inglese, per indice",
   all(v['italian'] == v['english'] for v in DATA) and len(DATA) == 37,
   [v['idx'] for v in DATA if v['italian'] != v['english']])
ck("le 8 DESCRIPTION sono TUTTE tradotte (0 identiche)",
   all(v['italian'] != v['english'] for v in DES) and len(DES) == 8)
ck('72 virgolette: 2 per ciascuno dei 36 nomi, per unita\'',
   Q_EN == Q_IT and len(Q_IT) == 36 and set(n for _, n in Q_IT) == {2}
   and sum(n for _, n in Q_IT) == 72, (len(Q_EN), len(Q_IT)))
ck("nessuna virgoletta nella prosa (le 8 schede non citano nulla)",
   all(v['italian'].count(QUOTE) == 0 for v in DES) and all(v['english'].count(QUOTE) == 0 for v in DES))
ck("apici: 0 in inglese, 3 in italiano (unita' 9, 34, 35), tutti elisioni",
   sum(v['english'].count(APOS) for v in cov) == 0 and A_IT == [(9, 1), (34, 1), (35, 1)], A_IT)
ck("nessun possessivo inglese ('s) in nessuna delle 45 unita'",
   "'s " not in ' '.join(v['italian'] for v in cov))
NAMES = ('Flea', 'Geocoris', 'Grasshopper', 'Lightning Bug', 'Ladybug', 'Pond Strider',
         'Skipper Railgun', 'Hai', 'Sheragi')
lost = [(v['idx'], n) for v in DES for n in NAMES if n in v['english'] and n not in v['italian']]
ck("ogni nome proprio presente in inglese resta in italiano, unita' per unita'",
   not lost and sum(1 for v in DES for n in NAMES if n in v['english']) >= 8,
   (lost, sum(1 for v in DES for n in NAMES if n in v['english'])))
ck("`ramscoop` resta invariato (nome di equipaggiamento, come nel corpus)",
   prosa.count('ramscoop') == 2 and 'ramscoop' in prosa)
ck('«baia per droni» e «danni ionici» e «riparazione dello scafo» (lessico consolidato)',
   all(t in ' '.join(v['italian'] for v in cov) for t in
       ('baia per droni', 'danni ionici', 'riparazione dello scafo', 'cannoni ionici', 'scorta ai convogli')))
ck('`Unfettered` reso «Slegati» (lessico consolidato del corpus)',
   'Slegati' in prosa and 'Unfettered' not in ' '.join(v['italian'] for v in cov))
ck("il plurale inglese `Fleas` non si replica: «i Flea»",
   'i Flea' in prosa and 'Fleas' not in ' '.join(v['italian'] for v in cov))
ck('stesso inglese => stessa resa, negli 8 gruppi di nomi ripetuti',
   all(len({v['italian'] for v in cov if v['english'] == k}) == 1
       for k, n in collections.Counter(v['english'] for v in cov).items() if n > 1)
   and sum(1 for k, n in collections.Counter(v['english'] for v in cov).items() if n > 1) == 8)
ck("NESSUN segnaposto (asserzione negativa scritta)",
   sum(len(TAG.findall(v['english'])) for v in cov) == 0 == sum(len(TAG.findall(v['italian'])) for v in cov))
ck('nessun residuo inglese di struttura (the, and, with, that, from)',
   not [w for w in (' the ', ' and ', ' with ', ' that ', ' from ')
        if w in prosa.lower()],
   [w for w in (' the ', ' and ', ' with ', ' that ', ' from ') if w in prosa.lower()])
ck('registro: nessun «Lei» e nessuna cortesia',
   not re.search(r'\bLei\b|\bSuo\b|\bSua\b|mi scusi', ' '.join(v['italian'] for v in cov)))
ck('nessun caporale e nessun carattere tipografico',
   not [v['idx'] for v in cov if any(c in v['italian'] for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026')])
rs = [v['ratio'] for v in cov]
ck('rapporto nel gate 0,55-1,90 (1,00-1,21; 466 -> 498 parole)',
   0.55 < min(rs) and max(rs) < 1.90, '%.2f - %.2f' % (min(rs), max(rs)))
ACC = re.compile(r"\b(e|piu|perche|cosi|gia|puo|cioe|percio)'(?![a-z])", re.I)
bad = [(v['idx'], ACC.search(v['italian']).group(0)) for v in cov if ACC.search(v['italian'])]
ck("tipografia (accenti veri, nessun apostrofo al posto dell'accento)", not bad, bad)
nonlat = [v['idx'] for v in cov for c in v['italian'] if ord(c) > 127 and not 0x00C0 <= ord(c) <= 0x024F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio',
   not [v['idx'] for v in cov if v['italian'] != v['italian'].rstrip() or '  ' in v['italian']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("29 unita' prima della 362: e' L243",
   db.execute('select count(*) from units where path=? and line<362', (PATH,)).fetchone()[0] == 29)
ck("83 unita' dopo la 885: il lotto NON chiude il file",
   db.execute('select count(*) from units where path=? and line>885', (PATH,)).fetchone()[0] == 83)
ck('confine misurato: riga 901, ship:Pond Strider (STESSO contesto dell\'ultima unita\')',
   db.execute('select line,context from units where path=? and line>885 order by line limit 1', (PATH,)).fetchone()
   == (901, 'ship:Pond Strider') and cov[-1]['context'] == 'ship:Pond Strider')
ck('il file intero: 157 unita, righe 15 - 1860',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (157, 15, 1860))
st = dict(db.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('le 45 unita sono PENDING (misurato)',
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
