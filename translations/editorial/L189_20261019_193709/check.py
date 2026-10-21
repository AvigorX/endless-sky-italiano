r"""check.py — L189 (`data/gegno/gegno outfits.txt`, 12 unita', righe 1034-1130).

Quinto lotto dei **Gegno**: armi da abbordaggio e da duello (`Savagery Pike`, `Irate Carronade`, `Plasmasickle`,
`Plasma Grenades`) e poi **sei licenze** che salgono di rango — civile, trivellatore, `Vi Lord`, `Vi Centurion`,
`Vi Evocati`, `Scin Hoplologist`, `Scin Architect`. 11 `DESCRIPTION` + 1 `VALUE`, zero tab, zero virgolette, **6 apici**
inglesi (2 elisioni, 4 possessivi). Le licenze usano la **seconda persona maschile** («Sei stato accettato…»), coerente
con il resto della campagna.
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
IT_ALL = ' '.join(v['italian'] for v in cov)
NAMES = ('Savagery Pike', 'Irate Carronades', 'Plasmasickles', 'Plasma Grenades')
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 12/12", len(cov) == 12 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 11 DESCRIPTION + 1 VALUE', collections.Counter(u['kind'] for u in units)
   == {'DESCRIPTION': 11, 'VALUE': 1})
ck('ZERO UI_LABEL, ZERO token (asserzioni vuote scritte)',
   [u['idx'] for u in units if u['kind'] == 'UI_LABEL'] == []
   and {t for u in units for t in TAGS.findall(u['english'])} == set())
ck('ZERO tab e ZERO virgolette (asserzioni vuote scritte)',
   [v['idx'] for v in cov if '\t' in v['english'] or '\t' in v['italian']] == []
   and sum(v['english'].count('"') for v in cov) == 0 == sum(v['italian'].count('"') for v in cov))
ck("l'unico VALUE e' identico al sorgente (`Plasma Grenades`)",
   [v['idx'] for v in cov if v['kind'] == 'VALUE'] == [4]
   and by[4]['italian'] == by[4]['english'] == 'Plasma Grenades')
ck('i nomi delle armi restano inglesi',
   not [(v['idx'], n) for v in cov for n in NAMES if n in v['english'] and n not in v['italian']],
   [(v['idx'], n) for v in cov for n in NAMES if n in v['english'] and n not in v['italian']])
ck("6 apici inglesi: `isn't`, `Scin's` x2, `Vi's` x3",
   sum(v['english'].count("'") for v in cov) == 6
   and {v['idx']: v['english'].count("'") for v in cov if "'" in v['english']} == {2: 1, 3: 1, 8: 1, 9: 2, 12: 1}
   and sum(v['english'].count("Vi's") for v in cov) == 3)
ck('nessun possessivo inglese in italiano',
   not [v['idx'] for v in cov if re.search(r"\b[A-Za-z]+'s\b", v['italian'])])
ck('idx 2 chiude con l\'immagine dello strato di vernice',
   'strato di vernice' in by[2]['italian'] and 'alla bell\'e meglio' in by[2]['italian'])
ck('idx 5 spiega il vantaggio sulle granate a frammentazione',
   'granate a frammentazione' in by[5]['italian'] and 'dispositivi magnetici' in by[5]['italian'])
ck('le sei licenze usano la seconda persona («Sei stato…», «Ti è stato…», «tuo»)',
   'Sei stato accettato' in by[6]['italian'] and 'Ti è stato conferito' in by[7]['italian']
   and 'alla tua portata' in by[8]['italian'] and 'i tuoi interessi' in by[9]['italian']
   and 'il tuo piacere' in by[10]['italian'] and 'la tua ricompensa' in by[11]['italian']
   and 'hai il permesso' in by[12]['italian'])
ck('la scala dei ranghi Vi: Lord, Centurion (Evocati), Evocati',
   'gerarchia militare' in by[8]['italian'] and 'Evocati' in by[9]['italian']
   and 'guerriero devoto' in by[10]['italian'])
ck('12 unita, 12 testi distinti, 11 contesti (Plasma Grenades con 2)',
   len({v['english'] for v in cov}) == 12 and len({u['context'] for u in units}) == 11
   and sorted(collections.Counter(u['context'] for u in units).values()) == [1] * 10 + [2])
ck('prima e ultima unita: righe 1034 e 1130',
   (cov[0]['line'], cov[-1]['line']) == (1034, 1130)
   and cov[0]['context'] == 'outfit:Savagery Pike' and cov[-1]['context'] == 'outfit:Scin Architect License')
ck('nessuno spazio finale', not [v['idx'] for v in cov
                                 if v['english'] != v['english'].rstrip() or v['italian'] != v['italian'].rstrip()])
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
ck('tutte le 12 unita sono PENDING (misurato)',
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
