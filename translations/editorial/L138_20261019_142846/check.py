r"""check.py — L138 (`data/starts.txt`, 47 unita', righe 215-358). Quarto inizio: gli Hai.

Controlli propri: **due `VALUE` identici** (`Hai Origins`, unita' 1 e 5) elencati come coppie, non contati; **32 tab**;
**56 virgolette** con **quattro unita' dispari** (26, 36, 37, 38: una ciascuna) riprodotte; **cinque unita' rilette da
L135** (10-14) verificate identiche; **zero token** e **zero `UI_LABEL`**; due inizi distinti con testi diversi
(«Questo inizio è bloccato» contro «Per sbloccare questo inizio...»).
"""
import collections
import json
import os
import re
import sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
PREV = os.path.join(L10N, 'staging/editorial/L135_20261019_131024/translation.json')
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
prev = {u['english']: u['italian'] for u in json.load(open(PREV, encoding='utf-8'))['units']}
TAGS = re.compile(r'<[^<>]+>')
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 47/47", len(cov) == 47 == len(units) and not missing, '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 32 CONVERSATION, 7 LOGBOOK, 6 DESCRIPTION, 2 VALUE',
   collections.Counter(u['kind'] for u in units)
   == {'CONVERSATION': 32, 'LOGBOOK': 7, 'DESCRIPTION': 6, 'VALUE': 2},
   collections.Counter(u['kind'] for u in units))
ck('ZERO UI_LABEL (asserzione vuota scritta)', [u['idx'] for u in units if u['kind'] == 'UI_LABEL'] == [])
ck('ZERO token in tutto il file (asserzione vuota scritta)',
   collections.Counter(t for u in units for t in TAGS.findall(u['english'])) == {})
ck('DUE VALUE identici, entrambi Hai Origins (unita 1 e 5)',
   [(v['idx'], v['italian']) for v in cov if v['kind'] == 'VALUE'] == [(1, 'Hai Origins'), (5, 'Hai Origins')],
   [(v['idx'], v['italian']) for v in cov if v['kind'] == 'VALUE'])
ck('i due inizi sono diversi: «Questo inizio è bloccato» contro «Per sbloccare questo inizio»',
   by[4]['italian'] == 'Questo inizio è bloccato.'
   and by[8]['italian'].lstrip('	').startswith('Per sbloccare questo inizio'),
   (by[4]['italian'], by[8]['italian'][:40]))
ck('le due DESCRIPTION iniziali differiscono solo per la coda',
   by[2]['italian'].startswith('Sei cresciuto su Greenwater') and by[6]['italian'].startswith('Sei cresciuto su '
                                                                                            'Greenwater')
   and by[2]['italian'] != by[6]['italian'])
ck('tutte le unita di testo sono tradotte (45 su 45)',
   not [v['idx'] for v in cov if v['kind'] != 'VALUE' and v['italian'].strip() == v['english'].strip()])
tabs = [v['idx'] for v in cov if v['english'].startswith('\t')]
ck('32 unita iniziano con tab, le stesse in traduzione',
   len(tabs) == 32 and tabs == [v['idx'] for v in cov if v['italian'].startswith('\t')], len(tabs))
ck('spazi iniziali e finali identici al sorgente (47/47)',
   not [v['idx'] for v in cov
        if len(v['italian']) - len(v['italian'].rstrip()) != len(v['english']) - len(v['english'].rstrip())])
ck('56 virgolette in inglese e in italiano',
   sum(v['english'].count('"') for v in cov) == 56 == sum(v['italian'].count('"') for v in cov),
   (sum(v['english'].count('"') for v in cov), sum(v['italian'].count('"') for v in cov)))
ck('virgolette per unita: stesso numero in tutte',
   not [v['idx'] for v in cov if v['english'].count('"') != v['italian'].count('"')],
   [(v['idx'], v['english'].count('"'), v['italian'].count('"')) for v in cov
    if v['english'].count('"') != v['italian'].count('"')])
ck('quattro unita dispari, una virgoletta ciascuna: 26, 36, 37, 38',
   [(v['idx'], v['italian'].count('"')) for v in cov if v['italian'].count('"') % 2] == [(26, 1), (36, 1), (37, 1),
                                                                                        (38, 1)],
   [(v['idx'], v['italian'].count('"')) for v in cov if v['italian'].count('"') % 2])
ck('nessuna battuta «riparata»: le quattro dispari non chiudono le virgolette',
   all(v['italian'].count('"') == 1 and not v['italian'].rstrip().endswith('"') for v in cov
       if v['idx'] in (26, 36, 37, 38)))
ck('2 contesti completi: start:hai space 8, conversation:hai intro 39',
   [(c, n) for c, n in collections.Counter(v['context'] for v in cov).items()]
   == [('start:hai space', 8), ('conversation:hai intro', 39)],
   dict(collections.Counter(v['context'] for v in cov)))
ck('5 unita rilette da L135 (10-14) identiche, inglese compreso',
   all(by[i]['english'].lstrip('\t') in prev and prev[by[i]['english'].lstrip('\t')] == by[i]['italian']
       for i in (10, 11, 12, 13, 14)),
   [i for i in (10, 11, 12, 13, 14)
    if by[i]['english'].lstrip('\t') not in prev or prev[by[i]['english'].lstrip('\t')] != by[i]['italian']])
ck('45 testi distinti su 47 unita (i due VALUE coincidono)', len({v['english'] for v in cov}) == 45,
   len({v['english'] for v in cov}))
ck('prima e ultima unita: righe 215 e 358', (cov[0]['line'], cov[-1]['line']) == (215, 358),
   (cov[0]['line'], cov[-1]['line']))
ck('ZERO quadre e zero backtick (asserito)',
   not [v['idx'] for v in cov if any(c in v['english'] + v['italian'] for c in '[]`')])
NUM = ' '.join(v['italian'] for v in cov)
KEYS = ('1,431 milioni', '0,3%', '4.836', '1,132 milioni')
ck('numeri in convenzione italiana: 1,431 milioni / 0,3% / 4.836 / 1,132 milioni',
   all(t in NUM for t in KEYS), [t for t in KEYS if t not in NUM])
ck('nessun numero inglese rimasto (1.431 million / 0.3% / 4,836 / 1.132 million)',
   not any(t in NUM for t in ('1.431 million', '0.3%', '4,836', '1.132 million')))
LOW = NUM.lower()
TERMS = ('hai', 'greenwater', 'polo nord', 'unfettered', 'sheragi', 'grasshopper', 'pristine jewel', 'aphid',
         'cantiere navale', 'mutuo', 'crediti')
ck('terminologia presente: 11 termini chiave', all(t in LOW for t in TERMS),
   [t for t in TERMS if t not in LOW])
ck('i nomi restano: Greenwater, Pristine Jewel, Grasshopper, Aphid, Sheragi, Drak',
   all(t in NUM for t in ('Greenwater', 'Pristine Jewel', 'Grasshopper', 'Aphid', 'Sheragi', 'Drak')))
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' you ', ' to the ', ' from the ')
LONG = ' '.join(TAGS.sub('""', v['italian']) for v in cov).lower()
for s in ('dirt belt', 'hai origins', 'pristine jewel', 'greenwater', 'grasshopper', 'aphid', 'sheragi'):
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
ck('tutte le 47 unita sono PENDING nel database (misurato)',
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
