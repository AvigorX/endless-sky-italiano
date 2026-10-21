r"""check.py — L136 (`data/starts.txt`, 15 unita', righe 135-171). Secondo inizio: `Birthday Surprise`.

Controlli propri: **1 `VALUE`** identico (`Birthday Surprise`); **2 contesti completi** (3 + 12); **zero token** e
**zero `UI_LABEL`** (due asserzioni vuote); **14 virgolette** con la distribuzione per unita' **6:2, 10:4, 11:2,
12:4, 13:2** e nessuna dispari; **6 unita' con tab**; **5 unita' rilette da L135** (5-9) verificate **identiche** al
lotto precedente, con l'inglese confrontato prima della resa.
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


ck("unita' tradotte 15/15", len(cov) == 15 == len(units) and not missing, '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 8 CONVERSATION, 4 LOGBOOK, 2 DESCRIPTION, 1 VALUE',
   collections.Counter(u['kind'] for u in units)
   == {'CONVERSATION': 8, 'LOGBOOK': 4, 'DESCRIPTION': 2, 'VALUE': 1},
   collections.Counter(u['kind'] for u in units))
ck('ZERO UI_LABEL (asserzione vuota scritta)', [u['idx'] for u in units if u['kind'] == 'UI_LABEL'] == [])
ck('ZERO token in tutto il file (asserzione vuota scritta)',
   collections.Counter(t for u in units for t in TAGS.findall(u['english'])) == {})
ck('1 VALUE identico al sorgente (nome dell\'inizio)',
   [(v['idx'], v['italian']) for v in cov if v['kind'] == 'VALUE'] == [(1, 'Birthday Surprise')],
   [(v['idx'], v['italian']) for v in cov if v['kind'] == 'VALUE'])
ck('tutte le unita di testo sono tradotte (14 su 14)',
   not [v['idx'] for v in cov if v['kind'] != 'VALUE' and v['italian'].strip() == v['english'].strip()])
tabs = [v['idx'] for v in cov if v['english'].startswith('\t')]
ck('6 unita iniziano con tab, le stesse in traduzione',
   len(tabs) == 6 and tabs == [v['idx'] for v in cov if v['italian'].startswith('\t')], len(tabs))
ck('spazi iniziali e finali identici al sorgente (15/15)',
   not [v['idx'] for v in cov
        if len(v['italian']) - len(v['italian'].rstrip()) != len(v['english']) - len(v['english'].rstrip())])
ck('14 virgolette in inglese e in italiano',
   sum(v['english'].count('"') for v in cov) == 14 == sum(v['italian'].count('"') for v in cov),
   (sum(v['english'].count('"') for v in cov), sum(v['italian'].count('"') for v in cov)))
ck('distribuzione delle virgolette per unita: 6:2, 10:4, 11:2, 12:4, 13:2',
   [(v['idx'], v['italian'].count('"')) for v in cov if v['italian'].count('"')]
   == [(6, 2), (10, 4), (11, 2), (12, 4), (13, 2)],
   [(v['idx'], v['italian'].count('"')) for v in cov if v['italian'].count('"')])
ck('nessuna unita dispari (asserito: lista vuota)',
   [v['idx'] for v in cov if v['english'].count('"') % 2] == [])
ck('2 contesti completi: start:paradise 3, conversation:paradise intro 12',
   [(c, n) for c, n in collections.Counter(v['context'] for v in cov).items()]
   == [('start:paradise', 3), ('conversation:paradise intro', 12)],
   dict(collections.Counter(v['context'] for v in cov)))
ck('5 unita rilette da L135 (5-9) identiche, inglese compreso',
   all(by[i]['english'].lstrip('\t') in prev and prev[by[i]['english'].lstrip('\t')] == by[i]['italian']
       for i in (5, 6, 7, 8, 9)),
   [i for i in (5, 6, 7, 8, 9)
    if by[i]['english'].lstrip('\t') not in prev or prev[by[i]['english'].lstrip('\t')] != by[i]['italian']])
ck('15 testi distinti dentro il lotto', len({v['english'] for v in cov}) == 15)
ck('prima e ultima unita: righe 135 e 167', (cov[0]['line'], cov[-1]['line']) == (135, 167),
   (cov[0]['line'], cov[-1]['line']))
ck('ZERO quadre e zero backtick (asserito)',
   not [v['idx'] for v in cov if any(c in v['english'] + v['italian'] for c in '[]`')])
NUM = ' '.join(v['italian'] for v in cov)
ck('numeri in convenzione italiana: 500.000 (unita 4 e 15)',
   NUM.count('500.000') == 2 and '500,000' not in NUM, NUM.count('500.000'))
ck('la battuta troncata resta troncata: «prima di-»',
   'prima di-' in NUM and not re.search(r'prima di\.', NUM))
LOW = NUM.lower()
TERMS = ('mainsail', 'mondo del paradiso', 'finanziere', 'licenza di pilota', 'spazioporto', 'cantiere navale',
         'credito', 'stilo', 'tavoletta', 'compleanno')
ck('terminologia presente: 10 termini chiave', all(t in LOW for t in TERMS),
   [t for t in TERMS if t not in LOW])
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' you ', ' to the ')
LONG = ' '.join(TAGS.sub('""', v['italian']) for v in cov).lower()
for s in ('dirt belt', 'mainsail', 'birthday surprise', 'paradise'):
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
ck('tutte le 15 unita sono PENDING nel database (misurato)',
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
