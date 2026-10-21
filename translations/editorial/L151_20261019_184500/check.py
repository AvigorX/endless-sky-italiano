r"""check.py — L151 (`data/coalition/coalition jobs.txt`, 37 unita', righe 799-1171).

Controlli propri: **81 token su 7 simboli**; **14 stringhe distinte** su 37 unita'; le **8 copie** della `DESCRIPTION`
di Cargo/Bulk hanno **una sola resa**; **17 `VALUE` identici**; il `DIALOG` dei medici tradotto; due asserzioni vuote
(`LOGBOOK`, `UI_LABEL`) più zero tab e zero virgolette.
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


ck("unita' tradotte 37/37", len(cov) == 37 == len(units) and not missing, '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 17 VALUE + 17 DESCRIPTION + 2 TEXT + 1 DIALOG',
   collections.Counter(u['kind'] for u in units) == {'VALUE': 17, 'DESCRIPTION': 17, 'TEXT': 2, 'DIALOG': 1})
ck('il DIALOG dei medici e tradotto (unita 33)',
   by[32]['italian'].strip() != by[32]['english'].strip() and 'medici' in by[32]['italian'].lower())
ck('due asserzioni vuote: ZERO LOGBOOK, ZERO UI_LABEL',
   [u['idx'] for u in units if u['kind'] in ('LOGBOOK', 'UI_LABEL')] == [])
ck('81 token su 7 simboli, stesso multiset in italiano',
   dict(collections.Counter(t for u in units for t in TAGS.findall(u['english'])))
   == {'<planet>': 19, '<payment>': 20, '<destination>': 17, '<cargo>': 14, '<date>': 7, '<bunks>': 3,
       '<commodity>': 1}
   == dict(collections.Counter(t for u in cov for t in TAGS.findall(u['italian']))))
ck('parita per UNITA: stesso ordine di simboli in tutte le 37',
   not [v['idx'] for v in cov if TAGS.findall(v['italian']) != TAGS.findall(v['english'])],
   [(v['idx'], TAGS.findall(v['english']), TAGS.findall(v['italian'])) for v in cov
    if TAGS.findall(v['italian']) != TAGS.findall(v['english'])])
ck('17 VALUE identici al sorgente, uno per uno',
   len(VAL) == 17 and all(by[i]['italian'].rstrip() == by[i]['english'].rstrip() for i in VAL),
   [(i, by[i]['italian']) for i in VAL if by[i]['italian'].rstrip() != by[i]['english'].rstrip()])
ck('i VALUE sono i 6 nomi attesi (Fast courier, Cargo, Bulk cargo, Rush Delivery, Doctors, Cadets)',
   {by[i]['italian'].rstrip() for i in VAL} == {'Fast courier to <planet>', 'Cargo to <planet>',
                                                'Bulk cargo to <planet>', 'Rush Delivery to <planet>',
                                                'Doctors to <planet>', 'Cadets to <planet>'},
   sorted({by[i]['italian'].rstrip() for i in VAL}))
ck('le 20 unita di testo sono tradotte (VALUE a parte)',
   not [v['idx'] for v in cov if v['kind'] != 'VALUE' and v['italian'].strip() == v['english'].strip()])
cargo = [v for v in cov if v['english'] == 'Deliver <cargo> to <destination>. Payment is <payment>.']
ck('le 8 copie di Cargo/Bulk hanno UNA sola resa', len(cargo) == 8
   and len({v['italian'] for v in cargo}) == 1, (len(cargo), len({v['italian'] for v in cargo})))
ck('le 3 copie di Fast Courier hanno UNA sola resa',
   len({v['italian'] for v in cov if v['english'] == 'Deliver <cargo> to <destination> by <date>. '
       'The payment is <payment>.'}) == 1)
ck('le 3 copie di Rush hanno UNA sola resa',
   len({v['italian'] for v in cov if v['english'].startswith('<destination> needs a shipment')}) == 1)
ck('14 stringhe distinte su 37 unita', len({(v['kind'], v['english']) for v in cov}) == 14)
ck('zero tab e zero virgolette (asserite)',
   sum(1 for v in cov if v['english'].startswith('\t')) == 0
   and sum(1 for v in cov if v['italian'].startswith('\t')) == 0
   and sum(v['english'].count('"') for v in cov) == 0 == sum(v['italian'].count('"') for v in cov))
ck('19 contesti', len(set(v['context'] for v in cov)) == 19)
ck('prima e ultima unita: righe 799 e 1171', (cov[0]['line'], cov[-1]['line']) == (799, 1171),
   (cov[0]['line'], cov[-1]['line']))
ck('spazi iniziali e finali identici al sorgente (37/37)',
   not [v['idx'] for v in cov
        if len(v['italian']) - len(v['italian'].rstrip()) != len(v['english']) - len(v['english'].rstrip())])
LOW = ' '.join(v['italian'] for v in cov).lower()
TERMS = ('consegna', 'compenso', 'epidemia virale', 'accademia', 'reclute', 'allievi')
ck('terminologia presente: 6 termini chiave («corriere» NON c e: e solo nel VALUE inglese)',
   all(t in LOW for t in TERMS) and 'corriere' not in LOW,
   [t for t in TERMS if t not in LOW])
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' you ', ' to the ', ' will be ')
LONG = ' '.join(TAGS.sub('""', v['italian']) for v in cov if v['kind'] != 'VALUE').lower()
ck('nessun residuo inglese fuori dai VALUE',
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
ck('tutte le 37 unita sono PENDING nel database (misurato)',
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
