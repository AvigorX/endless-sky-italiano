r"""check.py — L135 (`data/starts.txt`, 32 unita', righe 18-134). File nuovo: gli inizi di partita.

Due asserzioni vuote scritte: **zero token** e **zero `UI_LABEL`** (il file non ne ha nessuno).

Controlli propri: **4 contesti completi**; **2 `VALUE`** che sono **nomi di inizi** e restano identici; **14 unita' con
tab**; **14 virgolette** senza unita' dispari; **27 testi distinti** con **5 frasi ripetute** fra i due inizi, ciascuna
con la **stessa resa** nei due punti; numeri con la convenzione italiana (480.000 / 0,4% / 2.503 / 433.567).
"""
import collections
import json
import os
import re
import sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
units = sorted(src['units'], key=lambda x: x['line'])
tr = {}
parts = sorted(f for f in os.listdir(os.path.join(HERE, 'parts')) if f.endswith('.json'))
for p in parts:
    for k, v in json.load(open(os.path.join(HERE, 'parts', p), encoding='utf-8')).items():
        tr[int(k)] = v
out = {'block': src['block'], 'note': src['note'], 'units': []}
missing = [u['idx'] for u in units if u['idx'] not in tr]
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
TAGS = re.compile(r'<[^<>]+>')
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 32/32", len(cov) == 32 == len(units) and not missing, '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 18 CONVERSATION, 8 LOGBOOK, 4 DESCRIPTION, 2 VALUE',
   collections.Counter(u['kind'] for u in units)
   == {'CONVERSATION': 18, 'LOGBOOK': 8, 'DESCRIPTION': 4, 'VALUE': 2},
   collections.Counter(u['kind'] for u in units))
ck('ZERO UI_LABEL (asserzione vuota scritta)', [u['idx'] for u in units if u['kind'] == 'UI_LABEL'] == [])
ck('ZERO token in tutto il file (asserzione vuota scritta)',
   collections.Counter(t for u in units for t in TAGS.findall(u['english'])) == {},
   [t for u in units for t in TAGS.findall(u['english'])])
ck('2 VALUE identici al sorgente (nomi di inizi)',
   [(v['idx'], v['italian']) for v in cov if v['kind'] == 'VALUE']
   == [(1, 'Endless Sky'), (17, 'Deep Desire')],
   [(v['idx'], v['italian']) for v in cov if v['kind'] == 'VALUE'])
ck('tutte le unita di testo sono tradotte (30 su 30)',
   not [v['idx'] for v in cov if v['kind'] != 'VALUE' and v['italian'].strip() == v['english'].strip()])
tabs = [v['idx'] for v in cov if v['english'].startswith('\t')]
ck('14 unita iniziano con tab, le stesse in traduzione',
   len(tabs) == 14 and tabs == [v['idx'] for v in cov if v['italian'].startswith('\t')], len(tabs))
ck('spazi iniziali e finali identici al sorgente (32/32)',
   not [v['idx'] for v in cov
        if len(v['italian']) - len(v['italian'].rstrip()) != len(v['english']) - len(v['english'].rstrip())])
ck('14 virgolette in inglese e in italiano',
   sum(v['english'].count('"') for v in cov) == 14 == sum(v['italian'].count('"') for v in cov),
   (sum(v['english'].count('"') for v in cov), sum(v['italian'].count('"') for v in cov)))
ck('virgolette per unita: stesso numero',
   not [v['idx'] for v in cov if v['english'].count('"') != v['italian'].count('"')])
ck('nessuna unita dispari (asserito: lista vuota)',
   [v['idx'] for v in cov if v['english'].count('"') % 2] == [])
ck('4 contesti completi: 3 / 13 / 3 / 13',
   [(c, n) for c, n in collections.Counter(v['context'] for v in cov).items()]
   == [('start:default', 3), ('conversation:default intro', 13), ('start:deep', 3), ('conversation:deep intro', 13)],
   dict(collections.Counter(v['context'] for v in cov)))
ck('27 testi distinti su 32 unita', len({v['english'] for v in cov}) == 27,
   len({v['english'] for v in cov}))
SHARED = [(5, 21), (6, 22), (7, 23), (8, 24), (9, 25)]
ck('5 frasi ripetute fra i due inizi, resa identica nei due punti',
   all(by[a]['english'] == by[b]['english'] and by[a]['italian'] == by[b]['italian'] for a, b in SHARED),
   [(a, b) for a, b in SHARED if by[a]['italian'] != by[b]['italian']])
ck('prima e ultima unita: righe 18 e 130', (cov[0]['line'], cov[-1]['line']) == (18, 130),
   (cov[0]['line'], cov[-1]['line']))
ck('ZERO quadre e zero backtick (asserito)',
   not [v['idx'] for v in cov if any(c in v['english'] + v['italian'] for c in '[]`')])
NUM = ' '.join(v['italian'] for v in cov)
ck('numeri in convenzione italiana: 480.000 / 2.503 / 433.567 / 680.000 / 2.627 / 278.760 / 0,4% / 0,2%',
   all(t in NUM for t in ('480.000', '2.503', '433.567', '680.000', '2.627', '278.760', '0,4%', '0,2%')),
   [t for t in ('480.000', '2.503', '433.567', '680.000', '2.627', '278.760', '0,4%', '0,2%') if t not in NUM])
ck('nessun numero inglese rimasto (480,000 / 0.4% / 2,503)',
   not any(t in NUM for t in ('480,000', '2,503', '433,567', '680,000', '2,627', '278,760', '0.4%', '0.2%')))
LOW = ' '.join(v['italian'] for v in cov).lower()
TERMS = ('deep', 'dirt belt', 'sindacato', 'marina', 'repubblica', 'mondi del paradiso', 'mutuo', 'licenza di pilota',
         'astronave', 'prestito', 'interessi', 'cantiere navale')
ck('terminologia presente: 12 termini chiave', all(t in LOW for t in TERMS),
   [t for t in TERMS if t not in LOW])
ck('i nomi propri di regione restano inglesi: Deep, Dirt Belt',
   'Deep' in NUM and 'Dirt Belt' in NUM and 'Profondo' not in NUM)
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' you ', ' to the ')
LONG = ' '.join(TAGS.sub('""', v['italian']) for v in cov).lower()
for s in ('dirt belt', 'deep desire', 'endless sky', 'new boston', 'midgard', 'aldebaran', 'tarazed'):
    LONG = LONG.replace(s, '@@')
ck('nessun residuo inglese fuori dai nomi propri',
   not [w for w in ENGW if w in LONG], [w for w in ENGW if w in LONG])
CORT = re.findall(r'\bLei\b|(?<![.!?] )\b(?:Suo|Sua|Suoi|Sue)\b', NUM)
ck('nessuna forma di cortesia «Lei»', not CORT, CORT)
rs = [v['ratio'] for v in cov]
ck('rapporto nel gate', 0.55 < min(rs) and max(rs) < 1.90, '%.2f - %.2f' % (min(rs), max(rs)))
bad = [(v['idx'], n) for v in cov for p, n in ((r"\b(e|piu|perche|cosi|gia|puo|cioe|percio|fa)'", 'accento'),
       ('\u2026', 'ellissi'), ('\u2014', 'em dash'), ('\u2013', 'en dash'), ('\u2019', 'apostrofo curvo'),
       ('\u00ab', 'caporale'), ('\u00bb', 'caporale')) if re.search(p, v['italian'])]
ck('tipografia', not bad, bad)
nonlat = [v['idx'] for v in cov for c in v['italian'] if ord(c) > 127 and not 0x00C0 <= ord(c) <= 0x024F]
ck('caratteri non latini', not nonlat, nonlat)
c = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
st = dict(c.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('tutte le 32 unita sono PENDING nel database (misurato)',
   c.execute('select count(*) from units where id in (%s) and state != "PENDING"'
             % ','.join('?' * len(units)), [u['id'] for u in units]).fetchone()[0] == 0)
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d' % (sum(len(v['english'].split()) for v in cov),
                                 sum(len(v['italian'].split()) for v in cov)))
print('righe %d/%d · parti %d · mancanti %d' % (min(u['line'] for u in units), max(u['line'] for u in units),
      len(parts), len(missing)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
