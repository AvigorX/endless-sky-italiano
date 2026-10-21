r"""check.py — L187 (`data/gegno/gegno outfits.txt`, 7 unita', righe 459-728).

Terzo lotto dei **Gegno**: i cannoni dei **Vi** (Irate, Choleric, Ballistic, ognuno con la sua torretta) e la batteria
plasma degli **Scin** (`Astuit Battery`). **7 `DESCRIPTION`, zero `VALUE`**, zero tab, zero virgolette, **4 apici** inglesi
(`ship's` e `target's` due volte, `Vi's`). L'ultima unita' del sorgente nomina **`Astuit Blasters`** mentre l'oggetto e'
`Astuit Battery`: incoerenza del gioco, **non** del lotto — si conserva.
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
NAMES = ('Irate Cannon', 'Choleric Cannon', 'Ballistic Cannon', 'Astuit Batteries', 'Astuit Blasters', 'Energy Blasters')
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 7/7", len(cov) == 7 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 7 DESCRIPTION, ZERO VALUE (asserzione scritta)', collections.Counter(u['kind'] for u in units)
   == {'DESCRIPTION': 7})
ck('ZERO UI_LABEL, ZERO token (asserzioni vuote scritte)',
   [u['idx'] for u in units if u['kind'] == 'UI_LABEL'] == []
   and {t for u in units for t in TAGS.findall(u['english'])} == set())
ck('ZERO tab e ZERO virgolette (asserzioni vuote scritte)',
   [v['idx'] for v in cov if '\t' in v['english'] or '\t' in v['italian']] == []
   and sum(v['english'].count('"') for v in cov) == 0 == sum(v['italian'].count('"') for v in cov))
ck('i nomi delle armi restano inglesi in ogni unita che li nomina',
   not [(v['idx'], n) for v in cov for n in NAMES if n in v['english'] and n not in v['italian']],
   [(v['idx'], n) for v in cov for n in NAMES if n in v['english'] and n not in v['italian']])
ck('l\'incoerenza del sorgente si conserva: `Astuit Battery` (contesto) ma `Astuit Blasters` (testo)',
   'Astuit Blasters' in by[7]['english'] and 'Astuit Blasters' in by[7]['italian']
   and by[7]['context'] == 'outfit:Astuit Battery')
ck("4 apici inglesi: `ship's`, `target's` x2, `Vi's`",
   sum(v['english'].count("'") for v in cov) == 4
   and {v['idx']: v['english'].count("'") for v in cov if "'" in v['english']} == {3: 1, 4: 1, 5: 1, 6: 1}
   and sum(v['english'].count("target's") for v in cov) == 2)
ck('nessun possessivo inglese in italiano',
   not [v['idx'] for v in cov if re.search(r"\b[A-Za-z]'s\b", v['italian'])])
ck('la scala dei cannoni Vi sale: rudimentale, calibro superiore, il piu\' alto',
   'rudimentale' in by[1]['italian'] and 'calibro superiore' in by[3]['italian']
   and 'calibro più alto' in by[5]['italian'])
ck('idx 2 spiega perche\' la torretta ha due cannoni (cadenza raddoppiata)',
   'ne monta due' in by[2]['italian'] and 'raddoppiando la cadenza di tiro' in by[2]['italian'])
ck('idx 5 dice che i colpi sono schivabili ma letali in numero',
   'schivati' in by[5]['italian'] and 'muraglia di fuoco' in by[5]['italian'])
ck('idx 6 aggiunge la condizione dell\'equipaggio alla torretta',
   'autosufficiente' in by[6]['italian'] and 'equipaggio' in by[6]['italian'])
ck('7 unita, 7 testi inglesi distinti e 7 contesti (uno per unita)',
   len({v['english'] for v in cov}) == 7 and len({u['context'] for u in units}) == 7
   and sorted(collections.Counter(u['context'] for u in units).values()) == [1] * 7)
ck('prima e ultima unita: righe 459 e 728',
   (cov[0]['line'], cov[-1]['line']) == (459, 728)
   and cov[0]['context'] == 'outfit:Irate Cannon' and cov[-1]['context'] == 'outfit:Astuit Battery')
ck('nessuno spazio finale', not [v['idx'] for v in cov
                                 if v['english'] != v['english'].rstrip() or v['italian'] != v['italian'].rstrip()])
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' you ', ' to the ', ' will be ',
        ' is ', ' are ', ' from the ', ' its ', ' it is ', ' such as ', ' rather than ')
ck('nessun residuo inglese fuori dai nomi delle armi', not [w for w in ENGW if w in IT_ALL.lower()],
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
ck('tutte le 7 unita sono PENDING (misurato)',
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
