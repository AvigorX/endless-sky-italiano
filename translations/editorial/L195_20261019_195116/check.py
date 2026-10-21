r"""check.py — L195 (`data/bunrodea/bunrodea missions.txt`, 5 unita', righe 207-219). **CHIUDE IL FILE: 77/77.**

Ultimo lotto della missione: l'udienza si chiude con la clemenza della Regina e l'uscita dal palazzo. **5 `MISSION_TEXT`**,
**5 tab**, **10 virgolette**. Controlli propri: idx 2, 3 e 4 differiscono **solo nella prima frase** («Since you have
apologized» / «Since I have shown you mercy» / «Since it is my guards…»); il resto deve essere **identico**, e il
`check.py` confronta le code delle tre stringhe.
"""
import collections
import json
import os
import re
import sqlite3

TAB = chr(9)
QUOTE = chr(34)
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
EN_Q = sum(v['english'].count(QUOTE) for v in cov)
IT_Q = sum(v['italian'].count(QUOTE) for v in cov)
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 5/5", len(cov) == 5 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 5 MISSION_TEXT, ZERO VALUE (asserzione scritta)',
   collections.Counter(u['kind'] for u in units) == {'MISSION_TEXT': 5})
ck('ZERO UI_LABEL e ZERO token (asserzioni vuote scritte)',
   [u['idx'] for u in units if u['kind'] == 'UI_LABEL'] == []
   and {t for u in units for t in TAGS.findall(u['english'])} == set())
ck('5 tab e 10 virgolette in entrambe le lingue',
   [v['idx'] for v in cov if v['english'].startswith(TAB)] == list(range(1, 6))
   and EN_Q == 10 == IT_Q, (EN_Q, IT_Q))
ck('nessun caporale in italiano',
   not [v['idx'] for v in cov if any(c in v['italian'] for c in '\u00ab\u00bb\u201c\u201d')])
ta = "ti sarà permesso vivere. Alle mie guardie è stato ordinato di lasciarti in pace"
ck('idx 2, 3 e 4 condividono la coda (dalla concessione della vita alla cacciata)',
   all(ta in by[i]['italian'] for i in (2, 3, 4))
   and all('lascia la mia corte' in by[i]['italian'] for i in (2, 3, 4))
   and len({by[i]['italian'].split(ta)[1] for i in (2, 3, 4)}) == 1)
ck('le tre aperture sono diverse: scuse, clemenza, guardie',
   'Poiché ti sei scusato' in by[2]['italian'] and 'Poiché ti ho mostrato clemenza' in by[3]['italian']
   and 'Poiché sono le mie guardie' in by[4]['italian'])
ck("l'apertura accetta le scuse e nota la risposta inattesa (idx 1)",
   'Le tue scuse sono accettate' in by[1]['italian'] and 'inattesa' in by[1]['italian'])
ck('il congedo chiude sulle scale e sulla discesa (idx 5)',
   'affrontare di nuovo le scale' in by[5]['italian'] and 'lunga discesa' in by[5]['italian'])
ck('5 unita, 5 testi inglesi distinti', len({v['english'] for v in cov}) == 5)
ck('un solo contesto, righe 207 e 219', len({u['context'] for u in units}) == 1
   and (cov[0]['line'], cov[-1]['line']) == (207, 219))
ck('nessuno spazio finale (tab iniziali ammessi)',
   not [v['idx'] for v in cov if v['english'].rstrip(TAB) != v['english'].rstrip(TAB).rstrip()
        or v['italian'].rstrip(TAB) != v['italian'].rstrip(TAB).rstrip()])
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' you ', ' to the ', ' will be ',
        ' is ', ' are ', ' from the ', ' its ', ' it is ', ' such as ', ' rather than ')
ck('nessun residuo inglese', not [w for w in ENGW if w in IT_ALL.lower()],
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
ck('tutte le 5 unita sono PENDING (misurato)',
   c.execute('select count(*) from units where id in (%s) and state != "PENDING"'
             % ','.join('?' * len(units)), [u['id'] for u in units]).fetchone()[0] == 0)
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d' % (sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
