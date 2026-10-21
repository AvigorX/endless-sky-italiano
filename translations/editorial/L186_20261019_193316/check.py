r"""check.py — L186 (`data/gegno/gegno outfits.txt`, 14 unita', righe 179-427).

Secondo lotto dei **Gegno**: propulsori e timoni delle due stirpi, **Vi** (ionici, pesanti, antichi) e **Scin** (plasma,
compatti, moderni). 12 `DESCRIPTION` + 2 `VALUE`. Zero tab, zero virgolette (asserzioni vuote), **5 apici** inglesi tutti
possessivi (`Vi's` x2, `Gegno's`, `Scin's`, `Vi's`). I codici `RG*` e `SC-*` non si traducono mai.
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
CODES = ('RG15', 'RG18', 'RG3', 'SC-1', 'SC-12', 'SC-14', 'SC-15')
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


EN_ALL = ' '.join(u['english'] for u in units)
IT_ALL = ' '.join(v['italian'] for v in cov)
ck("unita' tradotte 14/14", len(cov) == 14 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 12 DESCRIPTION + 2 VALUE', collections.Counter(u['kind'] for u in units)
   == {'DESCRIPTION': 12, 'VALUE': 2})
ck('ZERO UI_LABEL, ZERO token (asserzioni vuote scritte)',
   [u['idx'] for u in units if u['kind'] == 'UI_LABEL'] == []
   and {t for u in units for t in TAGS.findall(u['english'])} == set())
ck('ZERO tab e ZERO virgolette (asserzioni vuote scritte)',
   [v['idx'] for v in cov if '\t' in v['english'] or '\t' in v['italian']] == []
   and sum(v['english'].count('"') for v in cov) == 0 == sum(v['italian'].count('"') for v in cov))
ck('i 2 VALUE identici al sorgente', {v['idx']: v['italian'] for v in cov if v['kind'] == 'VALUE'}
   == {7: 'SC-1 Plasma Engines', 13: 'SC-15 Plasma Thrusters'})
ck('i codici presenti nel testo restano invariati',
   not [c for c in CODES if c in EN_ALL and c not in IT_ALL],
   [c for c in CODES if c in EN_ALL and c not in IT_ALL])
ck('`Gegno Vi` e `Gegno Scin` distinti, con `Slate` e `Halite` invariati',
   'Gegno Vi' in IT_ALL and 'Gegno Scin' in IT_ALL and 'Slate' in IT_ALL and 'Halite' in IT_ALL)
ck("5 apici inglesi, tutti possessivi (Vi's tre volte, Gegno's, Scin's)",
   sum(v['english'].count("'") for v in cov) == 5
   and {v['idx']: v['english'].count("'") for v in cov if "'" in v['english']} == {1: 1, 5: 1, 8: 1, 11: 1, 14: 1}
   and sum(v['english'].count("Vi's") for v in cov) == 3)
ck('nessun possessivo inglese in italiano; 6 apici italiani di elisione (misurati)',
   not [v['idx'] for v in cov if re.search(r"\b[A-Za-z]+'s\b", v['italian'])]
   and {v['idx']: v['italian'].count("'") for v in cov if "'" in v['italian']} == {1: 1, 3: 2, 8: 1, 11: 1, 14: 1},
   {v['idx']: v['italian'].count("'") for v in cov if "'" in v['italian']})
ck('idx 3 dice che la torcia ionica scalda di piu\' ma consuma meno',
   'scaldare di più' in by[3]['italian'] and 'meno energia' in by[3]['italian'])
ck('idx 9 rovescia il confronto: gli SC spingono di piu\' ma scaldano di piu\'',
   'spinta decisamente maggiore' in by[9]['italian'] and 'tendono a scaldare di più' in by[9]['italian'])
ck('idx 14 introduce la retromarcia e il progetto "intorno ai propulsori"',
   'spinta inversa' in by[14]['italian'] and 'intorno ai propulsori' in by[14]['italian'])
ck('14 unita, 14 testi inglesi distinti', len({v['english'] for v in cov}) == 14)
ck('12 contesti: SC-1 e SC-15 con 2 unita, dieci con 1',
   len({u['context'] for u in units}) == 12
   and sorted(collections.Counter(u['context'] for u in units).values()) == [1] * 10 + [2, 2],
   collections.Counter(u['context'] for u in units))
ck('prima e ultima unita: righe 179 e 427',
   (cov[0]['line'], cov[-1]['line']) == (179, 427)
   and cov[0]['context'] == 'outfit:RG15 Torch Thruster'
   and cov[-1]['context'] == 'outfit:SC-15 Plasma Thrusters')
ck('nessuno spazio finale', not [v['idx'] for v in cov
                                 if v['english'] != v['english'].rstrip() or v['italian'] != v['italian'].rstrip()])
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' you ', ' to the ', ' will be ',
        ' is ', ' are ', ' from the ', ' its ', ' it is ', ' such as ', ' rather than ')
LONG = IT_ALL.lower()
ck('nessun residuo inglese fuori dai nomi e dai codici', not [w for w in ENGW if w in LONG],
   [w for w in ENGW if w in LONG])
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
ck('tutte le 14 unita sono PENDING (misurato)',
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
