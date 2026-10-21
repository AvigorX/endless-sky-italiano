r"""check.py — L176 (`data/avgi/avgi ships.txt`, 20 unita', righe 930-1399). **Il lotto dei nomi.**

**10 `TEXT` su 20 unita' sono nomi di equipaggiamento** e vanno copiati alla lettera: `Z-333 "Spark" Fusion Torch` (6),
`"Nettle" KKV` (2), `A-3600 "Beam" Amat Drive`, `"Orchid" Nuclear Missile`. Tutte e **20 le virgolette** sono li'.
Restano **8 `DESCRIPTION`** da tradurre e **2 `VALUE`** da lasciare inglesi. Controlli propri: **ogni `TEXT` identico al
sorgente uno per uno**, virgolette **solo** nei `TEXT`, **4 tab** (idx 3, 4, 9, 13), i **2 refusi del sorgente**
(`habitatation`, `Undsyni's`) che **non** si propagano, e i decimali resi con la **virgola** italiana (0,25c / 0,4c).
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
NAMES = ('Undsyni', 'Avlaki', 'Harmonikos', 'Plasmadyne Scoop', 'Tachytia', 'Tremoros', 'Prismaios',
         'Twilight Guard', 'Aberrant', 'Avgi')
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 20/20", len(cov) == 20 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 10 TEXT + 8 DESCRIPTION + 2 VALUE', collections.Counter(u['kind'] for u in units)
   == {'TEXT': 10, 'DESCRIPTION': 8, 'VALUE': 2})
ck('UN asserzione vuota: ZERO UI_LABEL', [u['idx'] for u in units if u['kind'] == 'UI_LABEL'] == [])
ck('ZERO token in tutto il lotto (asserzione vuota scritta)',
   {t for u in units for t in TAGS.findall(u['english'])} == set()
   == {t for v in cov for t in TAGS.findall(v['italian'])})
ck('i 10 TEXT sono identici al sorgente, uno per uno',
   [v['idx'] for v in cov if v['kind'] == 'TEXT'] == [1, 5, 6, 7, 11, 15, 16, 18, 19, 20]
   and not [v['idx'] for v in cov if v['kind'] == 'TEXT' and v['italian'] != v['english']],
   [(v['idx'], v['italian']) for v in cov if v['kind'] == 'TEXT' and v['italian'] != v['english']])
ck('i nomi dei 10 TEXT, contati per nome',
   collections.Counter(v['english'] for v in cov if v['kind'] == 'TEXT')
   == {'Z-333 "Spark" Fusion Torch': 6, '"Nettle" KKV': 2, 'A-3600 "Beam" Amat Drive': 1,
       '"Orchid" Nuclear Missile': 1},
   collections.Counter(v['english'] for v in cov if v['kind'] == 'TEXT'))
ck('20 virgolette, tutte nei 10 TEXT (2 ciascuno)',
   sum(v['english'].count('"') for v in cov) == 20 == sum(v['italian'].count('"') for v in cov)
   and [v['idx'] for v in cov if '"' in v['italian']] == [1, 5, 6, 7, 11, 15, 16, 18, 19, 20]
   and all(v['italian'].count('"') == 2 for v in cov if v['kind'] == 'TEXT'))
ck('i 2 VALUE identici al sorgente (Tremoros, Prismaios)',
   [v['idx'] for v in cov if v['kind'] == 'VALUE'] == [10, 14]
   and by[10]['italian'] == by[10]['english'] == 'Tremoros'
   and by[14]['italian'] == by[14]['english'] == 'Prismaios')
ck('4 tab iniziali, idx 3, 4, 9, 13 — uno solo per unita',
   [v['idx'] for v in cov if v['english'].startswith('\t')] == [3, 4, 9, 13]
   == [v['idx'] for v in cov if v['italian'].startswith('\t')]
   and all(v['italian'].count('\t') == 1 for v in cov if v['italian'].startswith('\t')))
ck('3 apici inglesi, uno in idx 2, uno in idx 3 e uno in idx 4',
   sum(v['english'].count("'") for v in cov) == 3
   and [v['idx'] for v in cov if "'" in v['english']] == [2, 3, 4]
   and all(v['english'].count("'") == 1 for v in cov if "'" in v['english']))
ck('nessun possessivo inglese residuo in italiano',
   not [v['idx'] for v in cov if re.search(r"[A-Za-z]+'s\b", v['italian'])])
ck('il refuso del sorgente `habitatation` non si propaga: in italiano «cilindri abitativi»',
   'habitatation' in by[9]['english'] and 'habitatation' not in by[9]['italian']
   and 'cilindri abitativi' in by[9]['italian'])
ck('i decimali usano la virgola italiana (0,25c e 0,4c), non il punto',
   '0.25c' in by[8]['english'] and '0,25c' in by[8]['italian']
   and '0.4c' in by[8]['english'] and '0,4c' in by[8]['italian']
   and '0.25' not in by[8]['italian'] and '0.4c' not in by[8]['italian'])
ck('le classi si nominano «classe X»: Undsyni, Tachytia, Tremoros, Prismaios',
   all('classe ' + n in by[i]['italian'] for i, n in
       ((2, 'Undsyni'), (8, 'Tachytia'), (12, 'Tremoros'), (17, 'Prismaios'))))
ck('i nomi restano invariati in ogni unita che li nomina',
   not [(v['idx'], n) for v in cov for n in NAMES if n in v['english'] and n not in v['italian']],
   [(v['idx'], n) for v in cov for n in NAMES if n in v['english'] and n not in v['italian']])
ck('20 unita, 14 testi inglesi distinti (i nomi si ripetono)',
   len({v['english'] for v in cov}) == 14, len({v['english'] for v in cov}))
ck('4 contesti distinti, 6+3+4+7 unita',
   len({u['context'] for u in units}) == 4
   and sorted(collections.Counter(u['context'] for u in units).values()) == [3, 4, 6, 7],
   collections.Counter(u['context'] for u in units))
ck('prima e ultima unita: righe 930 e 1399',
   (cov[0]['line'], cov[-1]['line']) == (930, 1399)
   and cov[0]['context'] == 'ship:Undsyni' and cov[-1]['context'] == 'ship:Prismaios')
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
ck('tutte le 20 unita sono PENDING nel database (misurato)',
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
