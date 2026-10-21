r"""check.py — L188 (`data/gegno/gegno outfits.txt`, 13 unita', righe 739-1012).

Quarto lotto dei **Gegno**: artiglieria plasma degli **Scin** (`Acuit Artillery`, `Acumen Bolt Cannon`, `Guile Pulse
Laser`), trivelle (`Excavator`, `Burrower`), la torcia ionica e la mazza da duello dei **Vi** (`Savagery Bludgeon`).
11 `DESCRIPTION` + 2 `VALUE`, **4 tab**, zero virgolette, **3 apici** inglesi.

Due unita' (idx 9 e idx 12) hanno lo **stesso testo inglese** («This mining outfit requires a drill spar port...»): la
resa deve essere **identica**, e il controllo lo pretende invece di fidarsi.
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
EN_ALL = ' '.join(u['english'] for u in units)
IT_ALL = ' '.join(v['italian'] for v in cov)
NAMES = ('Acuit Artillery', 'Acumen Bolt Cannon', 'Guile Pulse Laser', 'Guile Lasers', 'Excavator',
         'Burrower Drills', 'Ion Torches', 'Savagery Bludgeon', 'Feldspar Carrier', 'Dunite')
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 13/13", len(cov) == 13 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 11 DESCRIPTION + 2 VALUE', collections.Counter(u['kind'] for u in units)
   == {'DESCRIPTION': 11, 'VALUE': 2})
ck('ZERO UI_LABEL, ZERO token (asserzioni vuote scritte)',
   [u['idx'] for u in units if u['kind'] == 'UI_LABEL'] == []
   and {t for u in units for t in TAGS.findall(u['english'])} == set())
ck('ZERO virgolette (asserzione vuota scritta)',
   sum(v['english'].count('"') for v in cov) == 0 == sum(v['italian'].count('"') for v in cov))
ck('4 tab iniziali, idx 4/6/9/12, in inglese e in italiano',
   [v['idx'] for v in cov if v['english'].startswith('\t')] == [4, 6, 9, 12]
   == [v['idx'] for v in cov if v['italian'].startswith('\t')])
ck('i 2 VALUE identici al sorgente (`Ion Torches` plurale, contesto al singolare)',
   {v['idx']: v['italian'] for v in cov if v['kind'] == 'VALUE'} == {1: 'Acuit Artillery', 10: 'Ion Torches'}
   and by[10]['context'] == 'outfit:Ion Torch')
ck('i nomi restano inglesi in ogni unita che li nomina',
   not [(v['idx'], n) for v in cov for n in NAMES if n in v['english'] and n not in v['italian']],
   [(v['idx'], n) for v in cov for n in NAMES if n in v['english'] and n not in v['italian']])
ck("3 apici inglesi: `Vi's` in idx 2 e 13, `ship's` in idx 13",
   sum(v['english'].count("'") for v in cov) == 3
   and {v['idx']: v['english'].count("'") for v in cov if "'" in v['english']} == {2: 1, 13: 2}
   and sum(v['english'].count("Vi's") for v in cov) == 2)
ck('nessun possessivo inglese in italiano',
   not [v['idx'] for v in cov if re.search(r"\b[A-Za-z]+'s\b", v['italian'])])
ck('idx 9 e idx 12 hanno lo stesso inglese e la STESSA resa italiana',
   by[9]['english'] == by[12]['english'] and by[9]['italian'] == by[12]['italian']
   and '\t' in by[9]['italian'] and '\t' in by[12]['italian'])
ck('idx 2 dice che l\'Acuit supera in gittata quasi tutto (bombardamento)',
   'superano in gittata' in by[2]['italian'] and 'bombardamento' in by[2]['italian'])
ck('idx 6 elenca i difetti del Guile: energia, calore, gittata breve',
   'consumano energia in fretta' in by[6]['italian'] and 'gittata piuttosto breve' in by[6]['italian'])
ck('idx 11 distingue la torcia dalla trivella (precisione vs macinare)',
   'con più accuratezza' in by[11]['italian'] and 'macina gli asteroidi' in by[11]['italian'])
ck('idx 11 aggiunge il propulsore inverso di fortuna',
   'propulsore inverso di fortuna' in by[11]['italian'])
ck('13 unita, 12 testi distinti (idx 9 = idx 12), 7 contesti',
   len({v['english'] for v in cov}) == 12 and len({u['context'] for u in units}) == 7
   and sorted(collections.Counter(u['context'] for u in units).values()) == [1, 1, 2, 2, 2, 2, 3],
   collections.Counter(u['context'] for u in units))
ck('prima e ultima unita: righe 739 e 1012',
   (cov[0]['line'], cov[-1]['line']) == (739, 1012)
   and cov[0]['context'] == 'outfit:Acuit Artillery' and cov[-1]['context'] == 'outfit:Savagery Bludgeon')
ck('nessuno spazio finale (tab iniziali ammessi)',
   not [v['idx'] for v in cov if v['english'].rstrip('\t') != v['english'].rstrip('\t').rstrip()
        or v['italian'].rstrip('\t') != v['italian'].rstrip('\t').rstrip()])
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' you ', ' to the ', ' will be ',
        ' is ', ' are ', ' from the ', ' its ', ' it is ', ' such as ', ' rather than ')
ck('nessun residuo inglese fuori dai nomi', not [w for w in ENGW if w in IT_ALL.lower()],
   [w for w in ENGW if w in IT_ALL.lower()])
CORT = re.findall(r'\bLei\b|(?<![.!?] )\b(?:Suo|Sua|Suoi|Sue)\b', IT_ALL)
ck('nessuna forma di cortesia «Lei»', not CORT, CORT)
rs = [v['ratio'] for v in cov]
ck('rapporto nel gate 0,55-1,90', 0.55 < min(rs) and max(rs) < 1.90, '%.2f - %.2f' % (min(rs), max(rs)))
bad = [(v['idx'], n) for v in cov for p, n in ((r"\b(e|piu|perche|cosi|gia|puo|cioe|percio|fa)'", 'accento'),
       ('\u2026', 'ellissi'), ('\u2014', 'em dash'), ('\u2013', 'en dash'), ('\u2019', 'apostrofo curvo')) if re.search(p, v['italian'])]
ck('tipografia (accenti veri, nessun carattere tipografico)', not bad, bad)
nonlat = [v['idx'] for v in cov for c in v['italian'] if ord(c) > 127 and not 0x00C0 <= ord(c) <= 0x024F]
ck('caratteri non latini', not nonlat, nonlat)
c = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
st = dict(c.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('tutte le 13 unita sono PENDING (misurato)',
   c.execute('select count(*) from units where id in (%s) and state != "PENDING"'
             % ','.join('?' * len(units)), [u['id'] for u in units]).fetchone()[0] == 0)
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d' % (sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('righe %d/%d · parti %d · mancanti %d' % (min(u['line'] for u in units), max(u['line'] for u in units),
      len(parts), len([u for u in units if u['idx'] not in tr])))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
