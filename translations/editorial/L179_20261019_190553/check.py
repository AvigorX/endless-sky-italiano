r"""check.py — L179 (`data/avgi/avgi ships.txt`, 5 unita', righe 2716-2770). **Chiude il file.**

Ultimo lotto: 4 `DESCRIPTION` (due delle quali sono il **boilerplate dei droni**, gia' tradotto in L178) e 1 `VALUE`.
Controlli propri: boilerplate **identico a L178** (lettura incrociata del `translation.json` del lotto precedente),
boilerplate **identico fra idx 2 e 5**, **2 tab** (idx 2, 5), **zero virgolette**, nomi invariati (`Optikon`, `Sonikis`,
`Polari`, `Avgi`, `starwisp`), e l'`VALUE` `Sonikis` alla lettera.
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
NAMES = ('Optikon', 'Sonikis', 'Polari', 'Avgi', 'starwisp')
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


# boilerplate dei droni gia' tradotto in L178 (unita' 10 e 14)
PREV = os.path.join(L10N, 'staging/editorial/L178_20261019_190210/translation.json')
prev = {u['english'].lstrip('	'): u['italian'].lstrip('	')
        for u in json.load(open(PREV, encoding='utf-8'))['units']}
DRONE_EN = ('Drones do not come equipped with a hyperdrive. You cannot carry a drone unless you have a ship in '
            'your fleet with a drone bay.')

ck("unita' tradotte 5/5", len(cov) == 5 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 4 DESCRIPTION + 1 VALUE', collections.Counter(u['kind'] for u in units)
   == {'DESCRIPTION': 4, 'VALUE': 1})
ck('UN asserzione vuota: ZERO UI_LABEL', [u['idx'] for u in units if u['kind'] == 'UI_LABEL'] == [])
ck('ZERO token in tutto il lotto (asserzione vuota scritta)',
   {t for u in units for t in TAGS.findall(u['english'])} == set()
   == {t for v in cov for t in TAGS.findall(v['italian'])})
ck('1 VALUE identico al sorgente (Sonikis)',
   [v['idx'] for v in cov if v['kind'] == 'VALUE'] == [3] and by[3]['italian'] == by[3]['english'] == 'Sonikis')
ck('ZERO virgolette in inglese e in italiano (asserzione vuota scritta)',
   sum(v['english'].count('"') for v in cov) == 0 == sum(v['italian'].count('"') for v in cov))
ck('2 tab iniziali: idx 2 e 5, uno solo per unita',
   [v['idx'] for v in cov if v['english'].startswith('\t')] == [2, 5]
   == [v['idx'] for v in cov if v['italian'].startswith('\t')]
   and all(v['italian'].count('\t') == 1 for v in cov if v['italian'].startswith('\t')))
ck('il boilerplate dei droni e quello gia fissato in L178 (lettura incrociata)',
   DRONE_EN in prev
   and by[2]['italian'].lstrip('\t') == prev[DRONE_EN]
   and by[5]['italian'].lstrip('\t') == prev[DRONE_EN],
   (by[2]['italian'][:60], prev.get(DRONE_EN, 'ASSENTE')[:60]))
ck('idx 2 e idx 5 hanno lo stesso boilerplate, identico in inglese e in italiano',
   by[2]['english'] == by[5]['english'] and by[2]['italian'] == by[5]['italian'])
ck('ZERO apici in inglese e nessun possessivo inglese in italiano',
   sum(v['english'].count("'") for v in cov) == 0
   and not [v['idx'] for v in cov if re.search(r"[A-Za-z]+'s\b", v['italian'])])
ck('i nomi restano invariati in ogni unita che li nomina',
   not [(v['idx'], n) for v in cov for n in NAMES if n in v['english'] and n not in v['italian']],
   [(v['idx'], n) for v in cov for n in NAMES if n in v['english'] and n not in v['italian']])
ck('l Optikon e una «piattaforma sensoriale» e il suo nome resta in testa',
   'Optikon Sensor Platform' in by[1]['english'] and by[1]['italian'].startswith("L'Optikon Sensor Platform"))
ck('il Sonikis e un «drone cargo interorbitale»',
   'interorbital cargo drone' in by[4]['english'] and 'drone cargo interorbitale' in by[4]['italian'])
ck('5 unita, 4 testi inglesi distinti (il boilerplate 2 = 5)', len({v['english'] for v in cov}) == 4,
   len({v['english'] for v in cov}))
ck('2 contesti distinti, 2 + 3 unita',
   len({u['context'] for u in units}) == 2
   and sorted(collections.Counter(u['context'] for u in units).values()) == [2, 3],
   collections.Counter(u['context'] for u in units))
ck('prima e ultima unita: righe 2716 e 2770 (fine file)',
   (cov[0]['line'], cov[-1]['line']) == (2716, 2770)
   and cov[0]['context'] == 'ship:Optikon' and cov[-1]['context'] == 'ship:Sonikis')
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
ck('rapporto nel gate 0,55-1,90 (solo DESCRIPTION)', 0.55 < min(rs) and max(rs) < 1.90,
   '%.2f - %.2f' % (min(rs), max(rs)))
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
ck('tutte le 5 unita sono PENDING nel database (misurato)',
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
