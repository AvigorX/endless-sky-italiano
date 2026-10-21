r"""check.py — L177 (`data/avgi/avgi ships.txt`, 39 unita', righe 1415-2337).

Quarto lotto del file, il piu' **nominale**: 29 `TEXT` (nomi di equipaggiamento) + 3 `VALUE` + **7 `DESCRIPTION`**.
Controlli propri: ogni `TEXT` **identico al sorgente**, contato **per nome** (5 nomi distinti), **58 virgolette**
(= 2 per `TEXT`), **2 tab** (idx 19 e 20), zero apici inglesi, «classe X» nelle quattro classi, e i **nomi di fazione**
invariati (`Consonance`, `Tangles`, `Avgi`, `Diaspora`, `Guard`).
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


ck("unita' tradotte 39/39", len(cov) == 39 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 29 TEXT + 7 DESCRIPTION + 3 VALUE',
   collections.Counter(u['kind'] for u in units) == {'TEXT': 29, 'DESCRIPTION': 7, 'VALUE': 3})
ck('UN asserzione vuota: ZERO UI_LABEL', [u['idx'] for u in units if u['kind'] == 'UI_LABEL'] == [])
ck('ZERO token in tutto il lotto (asserzione vuota scritta)',
   {t for u in units for t in TAGS.findall(u['english'])} == set()
   == {t for v in cov for t in TAGS.findall(v['italian'])})
ck('i 29 TEXT sono identici al sorgente, uno per uno',
   not [v['idx'] for v in cov if v['kind'] == 'TEXT' and v['italian'] != v['english']],
   [(v['idx'], v['italian']) for v in cov if v['kind'] == 'TEXT' and v['italian'] != v['english']])
ck('i nomi dei TEXT, contati per nome (11 + 6 + 5 + 5 + 2)',
   collections.Counter(v['english'] for v in cov if v['kind'] == 'TEXT')
   == {'Z-333 "Spark" Fusion Torch': 11, '"Nettle" KKV': 6, '"Orchid" Nuclear Missile': 5,
       'Z-666 "Zap" Fusion Torch': 5, '"Ophrys" Nuclear Torpedo': 2},
   collections.Counter(v['english'] for v in cov if v['kind'] == 'TEXT'))
ck('58 virgolette: esattamente 2 per TEXT, in entrambe le lingue',
   sum(v['english'].count('"') for v in cov) == 58 == sum(v['italian'].count('"') for v in cov)
   and all(v['italian'].count('"') == 2 for v in cov if v['kind'] == 'TEXT')
   and sum(v['italian'].count('"') for v in cov if v['kind'] != 'TEXT') == 0)
ck('i 3 VALUE identici al sorgente (Interferos, Refraktos, Difraktos)',
   [v['idx'] for v in cov if v['kind'] == 'VALUE'] == [1, 16, 23]
   and [v['idx'] for v in cov if v['kind'] == 'VALUE' and v['italian'] != v['english']] == [])
ck('2 tab iniziali: idx 19 e 20, uno solo per unita',
   [v['idx'] for v in cov if v['english'].startswith('\t')] == [19, 20]
   == [v['idx'] for v in cov if v['italian'].startswith('\t')]
   and all(v['italian'].count('\t') == 1 for v in cov if v['italian'].startswith('\t')))
ck('ZERO apici in inglese e nessun possessivo inglese in italiano',
   sum(v['english'].count("'") for v in cov) == 0
   and not [v['idx'] for v in cov if re.search(r"[A-Za-z]+'s\b", v['italian'])])
ck('le quattro classi si nominano «classe X»',
   all('classe ' + n in by[i]['italian'] for i, n in
       ((3, 'Interferos'), (10, 'Diaspersi'), (18, 'Refraktos'), (26, 'Difraktos'))))
PAIRS = ((3, 'Consonance'), (3, 'Tangles'), (18, 'Diaspora'), (20, 'Avgi'), (10, 'Guard'))
ck('i nomi di fazione e regione restano in inglese (Consonance, Tangles, Diaspora, Avgi, Guard)',
   all(w in by[i]['english'] and w in by[i]['italian'] for i, w in PAIRS))
ck('39 unita, 15 testi inglesi distinti (3 VALUE + 5 nomi + 7 DESCRIPTION)',
   len({v['english'] for v in cov}) == 15, len({v['english'] for v in cov}))
ck('5 contesti distinti, 7+8+7+11+6 unita',
   len({u['context'] for u in units}) == 5
   and sorted(collections.Counter(u['context'] for u in units).values()) == [6, 7, 7, 8, 11],
   collections.Counter(u['context'] for u in units))
ck('prima e ultima unita: righe 1415 e 2337',
   (cov[0]['line'], cov[-1]['line']) == (1415, 2337)
   and cov[0]['context'] == 'ship:Interferos' and cov[-1]['context'] == 'ship:Atenuatia')
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
ck('tutte le 39 unita sono PENDING nel database (misurato)',
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
