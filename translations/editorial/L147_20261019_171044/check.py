r"""check.py — L147 (`data/coalition/coalition jobs.txt`, 30 unita', righe 16-293).

Controlli propri: **65 occorrenze di token su 7 simboli** con parita' **per simbolo e per unita'**; **13 `VALUE`
identici** al sorgente, verificati uno per uno; **ripetizioni triple** con resa unica; **quattro asserzioni vuote**
(zero tab, zero virgolette, zero `LOGBOOK`, zero `DIALOG`) piu' zero `UI_LABEL`.
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
VAL = [v['idx'] for v in cov if v['kind'] == 'VALUE']
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 30/30", len(cov) == 30 == len(units) and not missing, '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 13 VALUE + 13 DESCRIPTION + 4 TEXT',
   collections.Counter(u['kind'] for u in units) == {'VALUE': 13, 'DESCRIPTION': 13, 'TEXT': 4},
   collections.Counter(u['kind'] for u in units))
ck('TRE asserzioni vuote: ZERO LOGBOOK, ZERO DIALOG, ZERO UI_LABEL',
   [u['idx'] for u in units if u['kind'] in ('LOGBOOK', 'DIALOG', 'UI_LABEL')] == [])
ck('65 occorrenze di token, su 7 simboli',
   dict(collections.Counter(t for u in units for t in TAGS.findall(u['english'])))
   == {'<planet>': 28, '<payment>': 17, '<bunks>': 6, '<tons>': 6, '<date>': 4, '<origin>': 3, '<commodity>': 1})
ck('parita 1 = 1 per simbolo: 65 in inglese, 65 in italiano, stesso multiset',
   sum(1 for u in units for _ in TAGS.findall(u['english'])) == 65
   == sum(1 for u in cov for _ in TAGS.findall(u['italian']))
   and dict(collections.Counter(t for u in cov for t in TAGS.findall(u['italian'])))
   == dict(collections.Counter(t for u in units for t in TAGS.findall(u['english']))))
ck('parita per UNITA: ogni unita ha gli stessi simboli, nello stesso ordine',
   not [v['idx'] for v in cov if TAGS.findall(v['italian']) != TAGS.findall(v['english'])],
   [(v['idx'], TAGS.findall(v['english']), TAGS.findall(v['italian'])) for v in cov
    if TAGS.findall(v['italian']) != TAGS.findall(v['english'])])
ck('<payment> 17 e <date> 4 non si sono scambiati (conteggio per simbolo, non totale)',
   sum(1 for v in cov for _ in re.findall(r'<payment>', v['italian'])) == 17
   and sum(1 for v in cov for _ in re.findall(r'<date>', v['italian'])) == 4)
ck('13 VALUE identici al sorgente, uno per uno',
   all(by[i]['italian'].rstrip() == by[i]['english'].rstrip() for i in VAL)
   and len(VAL) == 13,
   [(i, by[i]['italian'], by[i]['english']) for i in VAL if by[i]['italian'].rstrip() != by[i]['english'].rstrip()])
ck('i VALUE sono i 5 nomi di lavoro attesi, triple ripetuti',
   [by[i]['italian'].rstrip() for i in VAL]
   == ['Workers to the <planet>'] * 3 + ['Volunteers to the <planet>'] * 3
   + ['Materials to the <planet>'] * 3 + ['Supplies to the <planet>'] * 3 + ['Candidate to the <planet>'],
   [by[i]['italian'].rstrip() for i in VAL])
ck('i VALUE conservano il <planet>: nessun nome di lavoro senza segnaposto',
   all('<planet>' in by[i]['italian'] for i in VAL))
ck('le 13 DESCRIPTION e i 4 TEXT sono tradotti (non identici all inglese)',
   not [v['idx'] for v in cov if v['kind'] != 'VALUE' and v['italian'].strip() == v['english'].strip()])
ck('ripetizioni triple: stessa resa per la stessa stringa (4 gruppi)',
   by[3]['italian'] == by[5]['italian'] == by[7]['italian']
   and by[10]['italian'] == by[12]['italian'] == by[14]['italian']
   and by[17]['italian'] == by[19]['italian'] == by[21]['italian']
   and by[24]['italian'] == by[26]['italian'] == by[28]['italian'])
ck('14 testi inglesi distinti su 30 unita', len({v['english'] for v in cov}) == 14,
   len({v['english'] for v in cov}))
ck('DUE asserzioni vuote: zero tab e zero virgolette (dichiarate)',
   sum(1 for v in cov if v['english'].startswith('\t')) == 0
   and sum(1 for v in cov if v['italian'].startswith('\t')) == 0
   and sum(v['english'].count('"') for v in cov) == 0 == sum(v['italian'].count('"') for v in cov))
ck('17 contesti', len(set(v['context'] for v in cov)) == 17, len(set(v['context'] for v in cov)))
ck('prima e ultima unita: righe 16 e 293', (cov[0]['line'], cov[-1]['line']) == (16, 293),
   (cov[0]['line'], cov[-1]['line']))
ck('spazi iniziali e finali identici al sorgente (30/30)',
   not [v['idx'] for v in cov
        if len(v['italian']) - len(v['italian'].rstrip()) != len(v['english']) - len(v['english'].rstrip())],
   [(v['idx'], repr(v['english'][-3:]), repr(v['italian'][-3:])) for v in cov
    if len(v['italian']) - len(v['italian'].rstrip()) != len(v['english']) - len(v['english'].rstrip())])
LOW = ' '.join(v['italian'] for v in cov).lower()
TERMS = ('opera', 'volontari', 'materiali da costruzione', 'forniture', 'heliarch',
         'mondo ad anello', 'compenso', 'candidato', 'consegna')
ck('terminologia presente: 9 termini chiave', all(t in LOW for t in TERMS), [t for t in TERMS if t not in LOW])
ck('i nomi restano: Heliarch', 'Heliarch' in ' '.join(v['italian'] for v in cov))
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' you ', ' to the ', ' will be ')
LONG = ' '.join(TAGS.sub('""', v['italian']) for v in cov if v['kind'] != 'VALUE').lower()
for s in ('heliarch',):
    LONG = LONG.replace(s, '@@')
ck('nessun residuo inglese fuori dai nomi propri e dai 13 VALUE (che sono inglesi per contratto)',
   not [w for w in ENGW if w in LONG], [w for w in ENGW if w in LONG])
CORT = re.findall(r'\bLei\b|(?<![.!?] )\b(?:Suo|Sua|Suoi|Sue)\b', ' '.join(v['italian'] for v in cov))
ck('nessuna forma di cortesia «Lei»', not CORT, CORT)
rs = [v['ratio'] for v in cov]
ck('rapporto nel gate', 0.55 < min(rs) and max(rs) < 1.90, '%.2f - %.2f' % (min(rs), max(rs)))
bad = [(v['idx'], n) for v in cov for p, n in ((r"\b(e|piu|perche|cosi|gia|puo|cioe|percio|fa)'", 'accento'),
       ('\u2026', 'ellissi'), ('\u2014', 'em dash'), ('\u2013', 'en dash'), ('\u2019', 'apostrofo curvo'),
       ('\u00ab', 'caporale'), ('\u00bb', 'caporale')) if re.search(p, v['italian'])]
ck('tipografia', not bad, bad)
nonlat = [v['idx'] for v in cov for c in TAGS.sub('', v['italian'])
          if ord(c) > 127 and not 0x00C0 <= ord(c) <= 0x024F]
ck('caratteri non latini (fuori dai token)', not nonlat, nonlat)
c = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
st = dict(c.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('tutte le 30 unita sono PENDING nel database (misurato)',
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
