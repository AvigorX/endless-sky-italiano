r"""check.py — L286 (`data/gegno/gegno ships.txt`, righe 53-302). **Primo lotto del file**.

Sette descrizioni di nave della fazione **Gegno**, in **prosa tecnica in terza persona**. Il lotto non ha ne' virgolette ne'
segnaposto ne' alternative: il test lo **dichiara con asserzioni vuote**, che sono controlli come gli altri. Verifica:

1. **`Gypsum` spezzato su due unita'** (243 e 244): stesso contesto, righe consecutive, la seconda **continua** la prima;
2. **un solo tab**, sulla seconda meta' del `Gypsum`, come primo carattere;
3. **i nomi di modello invariati**: `Shale`, `Dolomite`, `Conglomerate`, `Granofel`, `Gypsum`, `Corundum`, `Gegno`, `Vi`,
   `Scin`, `Shuttle`, `Excavator Drill`;
4. **il refuso del sorgente**: l'inglese scrive `Gypusm's` (unita' 7), l'italiano usa il nome corretto `Gypsum`;
5. **le asserzioni vuote**: 0 virgolette, 0 segnaposto, 0 alternative, in entrambe le lingue.
"""
import collections
import json
import os
import re
import sqlite3

TAB = chr(9)
QUOTE = chr(34)
APOS = chr(39)
TAG = re.compile(r'<[^<>]+>')
ALT = re.compile(r'\[[^\]]*\]')
HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
PATH = 'data/gegno/gegno ships.txt'
NAMES = ['Shale', 'Dolomite', 'Conglomerate', 'Granofel', 'Gypsum', 'Corundum', 'Gegno', 'Shuttle', 'Excavator Drill']
src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
units = sorted(src['units'], key=lambda x: x['line'])
tr = {}
for p in sorted(f for f in os.listdir(os.path.join(HERE, 'parts')) if f.endswith('.json')):
    for k, v in json.load(open(os.path.join(HERE, 'parts', p), encoding='utf-8')).items():
        tr[int(k)] = v
out = {'block': src['block'], 'note': src['note'], 'units': []}
for u in units:
    if u['idx'] in tr:
        it = tr[u['idx']]
        out['units'].append({"idx": u['idx'], "id": u['id'], "path": u['path'], "line": u['line'],
                             "kind": u['kind'], "context": u['context'], "english": u['english'],
                             "italian": it, "ratio": round(len(it) / max(1, len(u['english'])), 3)})
open(os.path.join(HERE, 'translation.json'), 'w', encoding='utf-8').write(
    json.dumps(out, ensure_ascii=False, indent=1))
cov = out['units']
by = {u['idx']: u for u in cov}
CTX = [('ship:Shale', 53), ('ship:Dolomite', 97), ('ship:Conglomerate', 146), ('ship:Granofel', 194),
       ('ship:Gypsum', 243), ('ship:Gypsum', 244), ('ship:Corundum', 302)]
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck('unita tradotte 7/7', len(cov) == 7 == len(units), '%d/%d' % (len(cov), len(units)))
ck('tutte DESCRIPTION, un solo tipo', {u['kind'] for u in units} == {'DESCRIPTION'})
ck('sei contesti, con le righe dichiarate (53, 97, 146, 194, 243, 244, 302)',
   [(u['context'], u['line']) for u in cov] == CTX, [(u['context'], u['line']) for u in cov])
ck('tutte e 7 le unita sono TRADOTTE, nessuna copiata',
   all(u['italian'] != u['english'] for u in cov), [u['idx'] for u in cov if u['italian'] == u['english']])
ck('`Gypsum` spezzato: due unita consecutive nello stesso contesto (243, 244)',
   by[5]['context'] == by[6]['context'] == 'ship:Gypsum' and by[6]['line'] == by[5]['line'] + 1
   and 'Gypsum' in by[5]['italian'] and 'Gypsum' in by[6]['italian'])
ck('la seconda meta del Gypsum CONTINUA la prima (nessun riavvio della descrizione)',
   not by[6]['italian'].lstrip(TAB).startswith(('Il Gypsum', 'Gypsum'))
   and by[6]['italian'].lstrip(TAB).startswith('Poiché'))
ck('TAB: uno solo, sull unita 6 (seconda meta del Gypsum), come PRIMO carattere',
   sum(u['english'].count(TAB) for u in cov) == 1 == sum(u['italian'].count(TAB) for u in cov)
   and [u['idx'] for u in cov if TAB in u['english']] == [6] == [u['idx'] for u in cov if TAB in u['italian']]
   and by[6]['italian'].startswith(TAB) and not by[5]['italian'].startswith(TAB))
ck('VIRGOLETTE: zero in inglese e zero in italiano (nessun dialogo)',
   sum(u['english'].count(QUOTE) for u in cov) == 0 == sum(u['italian'].count(QUOTE) for u in cov))
ck('SEGNAPOSTO: zero token', sum(len(TAG.findall(u['english'])) for u in cov) == 0
   == sum(len(TAG.findall(u['italian'])) for u in cov))
ck('ALTERNATIVE: zero parentesi quadre', sum(len(ALT.findall(u['english'])) for u in cov) == 0
   == sum(len(ALT.findall(u['italian'])) for u in cov))
ck('PARENTESI TONDE: una sola coppia, nell unita 1, conservata',
   [u['idx'] for u in cov if '(' in u['english']] == [1] == [u['idx'] for u in cov if '(' in u['italian']]
   and '(e costose)' in by[1]['italian'])
ck('nomi di modello INVARIATI in ogni unita in cui compaiono',
   all(by[i]['italian'].count(n) >= 1 for i, n in [(1, 'Shale'), (2, 'Dolomite'), (3, 'Conglomerate'),
                                                   (4, 'Granofel'), (5, 'Gypsum'), (7, 'Corundum')])
   and 'Gegno' in by[1]['italian'] and 'Shuttle' in by[1]['italian']
   and 'Vi' in by[2]['italian'] and 'Scin' in by[2]['italian'] and 'Excavator Drill' in by[6]['italian'])
ck('nessuno dei nomi e stato tradotto o storpiato',
   not [n for u in cov for n in NAMES if u['english'].count(n) != u['italian'].count(n)]
   or [n for u in cov for n in NAMES if u['english'].count(n) != u['italian'].count(n)]
   == ['Gypsum'],  # solo il refuso `Gypusm's` -> `Gypsum`
   [n for u in cov for n in NAMES if u['english'].count(n) != u['italian'].count(n)])
ck("REFUSO del sorgente: l'inglese scrive `Gypusm's`, l'italiano usa `Gypsum`",
   "Gypusm's" in by[7]['english'] and 'Gypusm' not in by[7]['italian'] and 'del Gypsum' in by[7]['italian'])
ck('APICI: quattro in inglese (possessivi), sei in italiano (possessivi + elisioni)',
   sum(u['english'].count(APOS) for u in cov) == 4 and sum(u['italian'].count(APOS) for u in cov) == 6,
   (sum(u['english'].count(APOS) for u in cov), sum(u['italian'].count(APOS) for u in cov)))
ck('registro: terza persona, NESSUN «tu» e nessun «tuo»',
   not [u['idx'] for u in cov if re.search(r'\b(tu|tuo|tua|tuoi|tue|ti|te)\b', u['italian'])],
   [u['idx'] for u in cov if re.search(r'\b(tu|tuo|tua|tuoi|tue|ti|te)\b', u['italian'])])
ck('lessico: cuccette, minerale grezzo e raffinato, ponte di comando, trivellazione',
   'cuccette' in by[4]['italian'] and 'grezzo e raffinato' in by[4]['italian']
   and 'ponte di comando' in by[5]['italian'] and 'trivellazione' in by[7]['italian'])
ck('nessun caporale, nessun carattere tipografico',
   not [u['idx'] for u in cov for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026' if c in u['italian']])
nonlat = [(u['idx'], c) for u in cov for c in u['italian'] if ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']],
   [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90 (1,01-1,11)',
   all(0.55 < u['ratio'] < 1.90 for u in cov),
   [(u['idx'], u['ratio']) for u in cov if not 0.55 < u['ratio'] < 1.90])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("ZERO unita' prima della 53: il lotto APRE il file",
   db.execute('select count(*) from units where path=? and line<53', (PATH,)).fetchone()[0] == 0)
ck("30 unita' dopo la 302",
   db.execute('select count(*) from units where path=? and line>302', (PATH,)).fetchone()[0] == 30)
ck('il file ha 37 unita, righe 53-1616, 36 DESCRIPTION + 1 VALUE',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (37, 53, 1616)
   and dict(db.execute('select kind,count(*) from units where path=? group by kind', (PATH,)).fetchall())
   == {'DESCRIPTION': 36, 'VALUE': 1})
ck('tutte le 7 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · 6 contesti · 1 tab · 0 virgolette · 0 segnaposto · 0 alternative' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
