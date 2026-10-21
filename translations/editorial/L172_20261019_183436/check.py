r"""check.py — L172 (`data/human/paradise world jobs.txt`, 12 unita', righe 1230-1336).

Sesto lotto del file, **il piu' regolare**: 6 `VALUE` + 6 `DESCRIPTION`, **18 token su 3 soli simboli** (`<cargo>`,
`<planet>`, `<payment>`), zero tab, zero virgolette. Controlli propri: **la formula deve essere identica** in tutte e sei
le coppie; **due `VALUE` ripetuti** (1/3) e **tre `DESCRIPTION` ripetute** (8/10/12); **8 testi distinti su 12**.
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


TOK = {'<cargo>': 6, '<planet>': 6, '<payment>': 6}
ck("unita' tradotte 12/12", len(cov) == 12 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 6 VALUE + 6 DESCRIPTION', collections.Counter(u['kind'] for u in units)
   == {'VALUE': 6, 'DESCRIPTION': 6})
ck('UN asserzione vuota: ZERO UI_LABEL', [u['idx'] for u in units if u['kind'] == 'UI_LABEL'] == [])
ck('18 token su 3 simboli, stesso multiset in italiano',
   dict(collections.Counter(t for u in units for t in TAGS.findall(u['english']))) == TOK
   == dict(collections.Counter(t for v in cov for t in TAGS.findall(v['italian'])))
   and sum(TOK.values()) == 18 and len(TOK) == 3)
ck('parita per UNITA: stesso ordine di simboli in tutte le 12',
   not [v['idx'] for v in cov if TAGS.findall(v['italian']) != TAGS.findall(v['english'])])
ck('ogni DESCRIPTION ha esattamente cargo + planet + payment',
   all(TAGS.findall(v['english']) == ['<cargo>', '<planet>', '<payment>']
       == TAGS.findall(v['italian']) for v in cov if v['kind'] == 'DESCRIPTION'))
ck('6 VALUE identici al sorgente',
   [v['idx'] for v in cov if v['kind'] == 'VALUE' and v['italian'].rstrip() != v['english'].rstrip()] == [])
ck('1 e 3 sono lo stesso VALUE ("Disaster relief to Martini") con la stessa resa',
   by[1]['english'] == by[3]['english'] == 'Disaster relief to Martini' and by[1]['italian'] == by[3]['italian'])
ck('2 e 4 sono la stessa DESCRIPTION (Medical [0] e [1]) con la stessa resa',
   by[2]['english'] == by[4]['english'] and by[2]['italian'] == by[4]['italian']
   and by[2]['context'] != by[4]['context'])
ck('8, 10 e 12 sono la stessa DESCRIPTION ("keep up supply") con la stessa resa',
   by[8]['english'] == by[10]['english'] == by[12]['english']
   and by[8]['italian'] == by[10]['italian'] == by[12]['italian'])
ck('12 unita, 8 testi inglesi distinti (5 VALUE + 3 DESCRIPTION)', len({v['english'] for v in cov}) == 8,
   len({v['english'] for v in cov}))
ck('tre varianti di DESCRIPTION: feriti / ricostruzione / scorte, mai intercambiabili',
   'curare i feriti' in by[2]['italian'] and 'sforzi di ricostruzione' in by[6]['italian']
   and 'mantenere le scorte' in by[8]['italian']
   and 'curare i feriti' not in by[6]['italian'] and 'sforzi di ricostruzione' not in by[8]['italian'])
ck('la coda «spazioporto» e identica in tutte le 6 DESCRIPTION',
   len({v['italian'].split('Dovrai')[1] for v in cov if v['kind'] == 'DESCRIPTION'}) == 1)
ck('ZERO tab e ZERO virgolette (asserzioni vuote scritte)',
   [v['idx'] for v in cov if '\t' in v['english'] or '\t' in v['italian']] == []
   and sum(v['english'].count('"') for v in cov) == 0 == sum(v['italian'].count('"') for v in cov))
ck('6 contesti distinti', len({u['context'] for u in units}) == 6)
ck('prima e ultima unita: righe 1230 e 1336',
   (cov[0]['line'], cov[-1]['line']) == (1230, 1336)
   and cov[0]['context'] == 'mission:Martini Relief (Medical) [0]'
   and cov[-1]['context'] == 'mission:Martini Relief (Fire Retardant)')
ck('zero spazi iniziali e finali identici al sorgente (12/12)',
   not [v['idx'] for v in cov
        if len(v['italian']) - len(v['italian'].rstrip()) != len(v['english']) - len(v['english'].rstrip())
        or len(v['italian']) - len(v['italian'].lstrip()) != len(v['english']) - len(v['english'].lstrip())])
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' you ', ' to the ', ' will be ',
        ' is ', ' are ', ' from the ', ' due to ')
LONG = ' '.join(TAGS.sub('""', v['italian']) for v in cov if v['kind'] != 'VALUE').lower()
ck('nessun residuo inglese fuori dai VALUE', not [w for w in ENGW if w in LONG], [w for w in ENGW if w in LONG])
CORT = re.findall(r'\bLei\b|(?<![.!?] )\b(?:Suo|Sua|Suoi|Sue)\b', ' '.join(v['italian'] for v in cov))
ck('nessuna forma di cortesia «Lei»', not CORT, CORT)
rs = [v['ratio'] for v in cov]
ck('rapporto nel gate 0,55-1,90', 0.55 < min(rs) and max(rs) < 1.90, '%.2f - %.2f' % (min(rs), max(rs)))
bad = [(v['idx'], n) for v in cov for p, n in ((r"\b(e|piu|perche|cosi|gia|puo|cioe|percio|fa)'", 'accento'),
       ('\u2026', 'ellissi'), ('\u2014', 'em dash'), ('\u2013', 'en dash'), ('\u2019', 'apostrofo curvo'),
       ('\u00ab', 'caporale'), ('\u00bb', 'caporale')) if re.search(p, v['italian'])]
ck('tipografia (accenti veri, nessun carattere tipografico)', not bad, bad)
nonlat = [v['idx'] for v in cov for c in TAGS.sub('', v['italian'])
          if ord(c) > 127 and not 0x00C0 <= ord(c) <= 0x024F]
ck('caratteri non latini (fuori dai token)', not nonlat, nonlat)
c = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
st = dict(c.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('tutte le 12 unita sono PENDING nel database (misurato)',
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
      len(parts), len([u for u in units if u['idx'] not in tr])))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
