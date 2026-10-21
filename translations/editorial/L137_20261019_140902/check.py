r"""check.py — L137 (`data/starts.txt`, 17 unita', righe 172-214). Terzo inizio: `Escaping Squalor`.

Controlli propri: **1 `VALUE`** identico; **2 contesti completi** (3 + 14); **zero token** e **zero `UI_LABEL`**;
**12 virgolette** con distribuzione **6:2, 11:2, 13:2, 14:4, 17:2** e nessuna dispari; **8 unita' con tab**; **cinque
unita' rilette da L135** (5-9) verificate identiche, inglese compreso; numeri italiani su cinque cifre chiave.
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


ck("unita' tradotte 17/17", len(cov) == 17 == len(units) and not missing, '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 10 CONVERSATION, 4 LOGBOOK, 2 DESCRIPTION, 1 VALUE',
   collections.Counter(u['kind'] for u in units)
   == {'CONVERSATION': 10, 'LOGBOOK': 4, 'DESCRIPTION': 2, 'VALUE': 1},
   collections.Counter(u['kind'] for u in units))
ck('ZERO UI_LABEL (asserzione vuota scritta)', [u['idx'] for u in units if u['kind'] == 'UI_LABEL'] == [])
ck('ZERO token in tutto il file (asserzione vuota scritta)',
   collections.Counter(t for u in units for t in TAGS.findall(u['english'])) == {})
ck('1 VALUE identico al sorgente (nome dell\'inizio)',
   [(v['idx'], v['italian']) for v in cov if v['kind'] == 'VALUE'] == [(1, 'Escaping Squalor')],
   [(v['idx'], v['italian']) for v in cov if v['kind'] == 'VALUE'])
ck('tutte le unita di testo sono tradotte (16 su 16)',
   not [v['idx'] for v in cov if v['kind'] != 'VALUE' and v['italian'].strip() == v['english'].strip()])
tabs = [v['idx'] for v in cov if v['english'].startswith('\t')]
ck('8 unita iniziano con tab, le stesse in traduzione',
   len(tabs) == 8 and tabs == [v['idx'] for v in cov if v['italian'].startswith('\t')], len(tabs))
ck('spazi iniziali e finali identici al sorgente (17/17)',
   not [v['idx'] for v in cov
        if len(v['italian']) - len(v['italian'].rstrip()) != len(v['english']) - len(v['english'].rstrip())])
ck('12 virgolette in inglese e in italiano',
   sum(v['english'].count('"') for v in cov) == 12 == sum(v['italian'].count('"') for v in cov),
   (sum(v['english'].count('"') for v in cov), sum(v['italian'].count('"') for v in cov)))
ck('distribuzione delle virgolette: 6:2, 11:2, 13:2, 14:4, 17:2',
   [(v['idx'], v['italian'].count('"')) for v in cov if v['italian'].count('"')]
   == [(6, 2), (11, 2), (13, 2), (14, 4), (17, 2)],
   [(v['idx'], v['italian'].count('"')) for v in cov if v['italian'].count('"')])
ck('nessuna unita dispari (asserito: lista vuota)',
   [v['idx'] for v in cov if v['english'].count('"') % 2] == [])
ck('2 contesti completi: start:syndicate 3, conversation:syndicate intro 14',
   [(c, n) for c, n in collections.Counter(v['context'] for v in cov).items()]
   == [('start:syndicate', 3), ('conversation:syndicate intro', 14)],
   dict(collections.Counter(v['context'] for v in cov)))
ck('5 unita rilette da L135 (5-9) identiche, inglese compreso',
   all(by[i]['english'].lstrip('\t') in prev and prev[by[i]['english'].lstrip('\t')] == by[i]['italian']
       for i in (5, 6, 7, 8, 9)),
   [i for i in (5, 6, 7, 8, 9)
    if by[i]['english'].lstrip('\t') not in prev or prev[by[i]['english'].lstrip('\t')] != by[i]['italian']])
ck('17 testi distinti dentro il lotto', len({v['english'] for v in cov}) == 17)
ck('prima e ultima unita: righe 172 e 210', (cov[0]['line'], cov[-1]['line']) == (172, 210),
   (cov[0]['line'], cov[-1]['line']))
ck('ZERO quadre e zero backtick (asserito)',
   not [v['idx'] for v in cov if any(c in v['english'] + v['italian'] for c in '[]`')])
NUM = ' '.join(v['italian'] for v in cov)
KEYS = ('600.000', '0,5%', '3.580', '706.571', '480.000')
ck('numeri in convenzione italiana: 600.000 / 0,5% / 3.580 / 706.571 / 480.000',
   all(t in NUM for t in KEYS), [t for t in KEYS if t not in NUM])
ck('nessun numero inglese rimasto (600,000 / 0.5% / 3,580 / 706,571 / 480,000)',
   not any(t in NUM for t in ('600,000', '0.5%', '3,580', '706,571', '480,000')))
LOW = NUM.lower()
TERMS = ('terra', 'sindacato', 'antipode', 'delve', 'cantiere navale', 'licenza di pilota', 'mutuo', 'prestito',
         'crediti', 'interessi', 'gettone di credito')
ck('terminologia presente: 11 termini chiave', all(t in LOW for t in TERMS),
   [t for t in TERMS if t not in LOW])
ck('i nomi restano: Delve, Antipode, Terra, Syndicated Systems',
   all(t in NUM for t in ('Delve', 'Antipode', 'Terra', 'Syndicated Systems')))
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' you ', ' to the ')
LONG = ' '.join(TAGS.sub('""', v['italian']) for v in cov).lower()
for s in ('dirt belt', 'escaping squalor', 'syndicated systems', 'antipode', 'delve'):
    LONG = LONG.replace(s, '@@')
ck('nessun residuo inglese fuori dai nomi propri',
   not [w for w in ENGW if w in LONG], [w for w in ENGW if w in LONG])
CORT = re.findall(r'\bLei\b|(?<![.!?] )\b(?:Suo|Sua|Suoi|Sue)\b', NUM)
ck('cortesia solo dentro le battute del cassiere (nessuna forma fuori dai dialoghi)',
   len(CORT) <= 1, CORT)
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
ck('tutte le 17 unita sono PENDING nel database (misurato)',
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
