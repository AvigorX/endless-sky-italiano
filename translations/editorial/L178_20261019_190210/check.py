r"""check.py — L178 (`data/avgi/avgi ships.txt`, 14 unita', righe 2424-2667).

Quinto lotto del file: **10 `DESCRIPTION`** (di cui **due coppie di boilerplate identiche**: «Fighters» in idx 2/5 e
«Drones» in idx 10/14), **3 `TEXT`** da copiare e **1 `VALUE`**. Controlli propri: **6 tab** (idx 2, 4, 5, 10, 13, 14), **6
virgolette** (2 per `TEXT`), il **boilerplate identico tradotto identico** e la differenza **caccia/drone** che non si può
confondere, i nomi dei mezzi (`Akoustiki Excursion Vehicle`, `Photikon`, `Vibratia`, `Undulon`, `Speckle Turret`,
`Ophrys`) invariati.
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
NAMES = ('Akoustiki Excursion Vehicle', 'Photikon', 'Vibratia', 'Undulon', 'Speckle Turret', 'Ophrys', 'Avgi')
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 14/14", len(cov) == 14 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 10 DESCRIPTION + 3 TEXT + 1 VALUE',
   collections.Counter(u['kind'] for u in units) == {'DESCRIPTION': 10, 'TEXT': 3, 'VALUE': 1})
ck('UN asserzione vuota: ZERO UI_LABEL', [u['idx'] for u in units if u['kind'] == 'UI_LABEL'] == [])
ck('ZERO token in tutto il lotto (asserzione vuota scritta)',
   {t for u in units for t in TAGS.findall(u['english'])} == set()
   == {t for v in cov for t in TAGS.findall(v['italian'])})
ck('i 3 TEXT sono identici al sorgente ("Nettle" KKV, "Ophrys" Nuclear Torpedo, "Orchid" Nuclear Missile)',
   [v['idx'] for v in cov if v['kind'] == 'TEXT'] == [6, 7, 11]
   and not [v['idx'] for v in cov if v['kind'] == 'TEXT' and v['italian'] != v['english']])
ck('6 virgolette, 2 per TEXT, nessuna fuori dai TEXT',
   sum(v['english'].count('"') for v in cov) == 6 == sum(v['italian'].count('"') for v in cov)
   and all(v['italian'].count('"') == 2 for v in cov if v['kind'] == 'TEXT'))
ck('1 VALUE identico al sorgente (Vibratia)',
   [v['idx'] for v in cov if v['kind'] == 'VALUE'] == [8] and by[8]['italian'] == by[8]['english'])
ck('6 tab iniziali: idx 2, 4, 5, 10, 13, 14 — uno solo per unita',
   [v['idx'] for v in cov if v['english'].startswith('\t')] == [2, 4, 5, 10, 13, 14]
   == [v['idx'] for v in cov if v['italian'].startswith('\t')]
   and all(v['italian'].count('\t') == 1 for v in cov if v['italian'].startswith('\t')))
ck('boilerplate «Fighters» (idx 2 e 5) identico in inglese e in italiano',
   by[2]['english'] == by[5]['english'] and by[2]['italian'] == by[5]['italian']
   and 'baia per caccia' in by[2]['italian'])
ck('boilerplate «Drones» (idx 10 e 14) identico in inglese e in italiano',
   by[10]['english'] == by[14]['english'] and by[10]['italian'] == by[14]['italian']
   and 'baia per droni' in by[10]['italian'])
ck('i due boilerplate NON si confondono: «caccia» compare solo nelle unita dei caccia',
   'caccia' in by[2]['italian'] and 'caccia' in by[5]['italian']
   and 'caccia' not in by[10]['italian'] and 'caccia' not in by[14]['italian']
   and 'droni' in by[10]['italian'] and 'droni' not in by[2]['italian'])
ck('ZERO apici in inglese e nessun possessivo inglese in italiano',
   sum(v['english'].count("'") for v in cov) == 0
   and not [v['idx'] for v in cov if re.search(r"[A-Za-z]+'s\b", v['italian'])])
ck('i nomi dei mezzi restano invariati in ogni unita che li nomina',
   not [(v['idx'], n) for v in cov for n in NAMES if n in v['english'] and n not in v['italian']],
   [(v['idx'], n) for v in cov for n in NAMES if n in v['english'] and n not in v['italian']])
ck('14 unita, 12 testi inglesi distinti (le due coppie di boilerplate)',
   len({v['english'] for v in cov}) == 12, len({v['english'] for v in cov}))
ck('4 contesti distinti, 2+5+3+4 unita',
   len({u['context'] for u in units}) == 4
   and sorted(collections.Counter(u['context'] for u in units).values()) == [2, 3, 4, 5],
   collections.Counter(u['context'] for u in units))
ck('prima e ultima unita: righe 2424 e 2667',
   (cov[0]['line'], cov[-1]['line']) == (2424, 2667)
   and cov[0]['context'] == 'ship:Akoustiki' and cov[-1]['context'] == 'ship:Undulon')
ck('nessuno spazio finale, tab iniziale ammesso',
   not [v['idx'] for v in cov
        if v['english'].rstrip('\t') != v['english'].rstrip('\t').rstrip()
        or v['italian'].rstrip('\t') != v['italian'].rstrip('\t').rstrip()])
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' you ', ' to the ', ' will be ',
        ' is ', ' are ', ' from the ', ' its ', ' it is ', ' such as ', ' rather than ')
LONG = ' '.join(v['italian'] for v in cov if v['kind'] == 'DESCRIPTION').lower()
ck('nessun residuo inglese nelle DESCRIPTION', not [w for w in ENGW if w in LONG], [w for w in ENGW if w in LONG])
CORT = re.findall(r'\bLei\b|(?<![.!?] )\b(?:Suo|Sua|Suoi|Sue)\b', ' '.join(v['italian'] for v in cov))
ck('nessuna forma di cortesia «Lei»', not CORT, CORT)
rs = [v['ratio'] for v in cov if v['kind'] == 'DESCRIPTION']
ck('rapporto nel gate 0,55-1,90 (solo DESCRIPTION: i nomi valgono 1)',
   0.55 < min(rs) and max(rs) < 1.90, '%.2f - %.2f' % (min(rs), max(rs)))
bad = [(v['idx'], n) for v in cov for p, n in ((r"\b(e|piu|perche|cosi|gia|puo|cioe|percio|fa)'", 'accento'),
       ('\u2026', 'ellissi'), ('\u2014', 'em dash'), ('\u2013', 'en dash'), ('\u2019', 'apostrofo curvo'),
       ('\u00ab', 'caporale'), ('\u00bb', 'caporale')) if re.search(p, v['italian'])]
ck('tipografia (accenti veri, nessun carattere tipografico)', not bad, bad)
nonlat = [v['idx'] for v in cov for c in v['italian']
          if ord(c) > 127 and not 0x00C0 <= ord(c) <= 0x024F]
ck('caratteri non latini', not nonlat, nonlat)
c = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
st = dict(c.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('tutte le 14 unita sono PENDING nel database (misurato)',
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
