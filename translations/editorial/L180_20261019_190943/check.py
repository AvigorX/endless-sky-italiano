r"""check.py — L180 (`data/human/outfits.txt`, 12 unita', righe 15-146). **Apre il file.**

Primo lotto di `outfits.txt`: **11 contesti per 12 unita'**, quindi una sola famiglia (`Cooling Ducts`) ha due unita' e
tutte le altre una. Controlli propri: **zero tab e zero virgolette** (asserzioni vuote scritte), **1 apice** inglese in
idx 3 (`ship's`), i **nomi degli equipaggiamenti invariati** (sono `VALUE` o nomi citati nel testo), il termine
**«spazio umano»** per `human space` (coerente con i lotti precedenti) e la catena di potenza degli scudi.
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
NAMES = ('Cooling Ducts', 'Water Coolant System', 'Liquid Nitrogen Cooler', 'Liquid Helium Cooler',
         'D14-RN', 'D23-QP', 'D41-HY', 'D67-TM', 'D94-YV', 'Shield Generator', 'S-270', 'S-970', 'Regenerator')
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 12/12", len(cov) == 12 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 11 DESCRIPTION + 1 VALUE', collections.Counter(u['kind'] for u in units)
   == {'DESCRIPTION': 11, 'VALUE': 1})
ck('UN asserzione vuota: ZERO UI_LABEL', [u['idx'] for u in units if u['kind'] == 'UI_LABEL'] == [])
ck('ZERO token in tutto il lotto (asserzione vuota scritta)',
   {t for u in units for t in TAGS.findall(u['english'])} == set()
   == {t for v in cov for t in TAGS.findall(v['italian'])})
ck('1 VALUE identico al sorgente (Cooling Ducts)',
   [v['idx'] for v in cov if v['kind'] == 'VALUE'] == [1] and by[1]['italian'] == by[1]['english'] == 'Cooling Ducts')
ck('ZERO tab e ZERO virgolette (asserzioni vuote scritte)',
   [v['idx'] for v in cov if '\t' in v['english'] or '\t' in v['italian']] == []
   and sum(v['english'].count('"') for v in cov) == 0 == sum(v['italian'].count('"') for v in cov))
ck('1 apice inglese, in idx 3 (`ship\'s`), e nessun possessivo inglese in italiano',
   sum(v['english'].count("'") for v in cov) == 1
   and [v['idx'] for v in cov if "'" in v['english']] == [3]
   and not [v['idx'] for v in cov if re.search(r"[A-Za-z]+'s\b", v['italian'])])
ck('i nomi degli equipaggiamenti restano invariati in ogni unita che li nomina',
   not [(v['idx'], n) for v in cov for n in NAMES if n in v['english'] and n not in v['italian']],
   [(v['idx'], n) for v in cov for n in NAMES if n in v['english'] and n not in v['italian']])
ck('`human space` diventa «spazio umano» (coerenza con i lotti precedenti)',
   'human space' in by[10]['english'] and 'spazio umano' in by[10]['italian']
   and 'human space' not in by[10]['italian'])
ck('la catena dei refrigeranti: azoto liquido, poi elio liquido come «massimo»',
   'azoto liquido' in by[4]['italian'] and 'elio liquido' in by[5]['italian']
   and 'massimo della tecnologia di raffreddamento' in by[5]['italian'])
ck('la catena degli scudi: standard, più potente, frequente combattimento, il più potente',
   'standard' in by[6]['italian'] and 'leggermente più potente' in by[7]['italian']
   and 'combattimenti frequenti' in by[8]['italian'] and 'così potente' in by[9]['italian']
   and 'più potente disponibile' in by[10]['italian'])
ck('i due rigeneratori si distinguono: S-270 parla di efficienza, S-970 di fabbisogno energetico',
   'meno efficienti' in by[11]['italian'] and 'fabbisogno energetico è piuttosto alto' in by[12]['italian'])
ck('12 unita, 12 testi inglesi distinti', len({v['english'] for v in cov}) == 12,
   len({v['english'] for v in cov}))
ck('11 contesti distinti: uno con 2 unita (Cooling Ducts), dieci con 1',
   len({u['context'] for u in units}) == 11
   and sorted(collections.Counter(u['context'] for u in units).values()) == [1] * 10 + [2],
   collections.Counter(u['context'] for u in units))
ck('prima e ultima unita: righe 15 e 146',
   (cov[0]['line'], cov[-1]['line']) == (15, 146)
   and cov[0]['context'] == 'outfit:Cooling Ducts' and cov[-1]['context'] == 'outfit:S-970 Regenerator')
ck('nessuno spazio finale (nessun tab da preservare in questo lotto)',
   not [v['idx'] for v in cov
        if v['english'] != v['english'].rstrip() or v['italian'] != v['italian'].rstrip()])
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
