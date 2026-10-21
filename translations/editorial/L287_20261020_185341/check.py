r"""check.py — L287 (`data/gegno/gegno ships.txt`, righe 303-658). **Secondo lotto del file**.

Nove descrizioni, **tre spezzate su due unita' consecutive** (`Dunite` 417-418, `Augen` 553-554, `Schist` 657-658) e una che
**continua** il `Corundum` iniziato in L286 (riga 302). Il test verifica:

1. **le tre coppie**: stesso contesto, righe consecutive, e la seconda unita' **continua** (non ricomincia con il soggetto);
2. **la continuita' cross-lot del `Corundum`**: l'unita' 1 prosegue la scheda di L286 senza riaprirla;
3. **quattro tab** (unita' 1, 4, 6, 9) come **primo carattere**;
4. **asserzioni vuote**: 0 virgolette, 0 segnaposto, 0 alternative;
5. **registro in terza persona**: nessun «tu», come in L286 (`Augen-Class` e' una nave, `Enbi` un cantiere).
"""
import collections
import glob
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
NAMES = ['Corundum', 'Protolith', 'Dunite', 'Augen', 'Slate', 'Schist', 'Gegno', 'Vi', 'Scin', 'Heutesl', 'Enbi',
         'Gypsum', 'Shale', 'Dolomite', 'Excavator Drill', 'Irate Cannon', 'Ballistic Cannons']
PAIRS = [(3, 4, 'ship:Dunite'), (5, 6, 'ship:Augen'), (8, 9, 'ship:Schist')]
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
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck('unita tradotte 9/9', len(cov) == 9 == len(units), '%d/%d' % (len(cov), len(units)))
ck('tutte DESCRIPTION, sei contesti con le righe dichiarate',
   {u['kind'] for u in cov} == {'DESCRIPTION'}
   and [(u['context'], u['line']) for u in cov]
   == [('ship:Corundum', 303), ('ship:Protolith', 371), ('ship:Dunite', 417), ('ship:Dunite', 418),
       ('ship:Augen', 553), ('ship:Augen', 554), ('ship:Slate', 594), ('ship:Schist', 657), ('ship:Schist', 658)],
   [(u['context'], u['line']) for u in cov])
ck('tutte e 9 le unita sono TRADOTTE, nessuna copiata',
   all(u['italian'] != u['english'] for u in cov), [u['idx'] for u in cov if u['italian'] == u['english']])
ck('TRE coppie spezzate: stesso contesto, righe consecutive',
   all(by[b]['context'] == ctx == by[a]['context'] and by[b]['line'] == by[a]['line'] + 1 for a, b, ctx in PAIRS),
   [(a, b, by[a]['context'], by[b]['context']) for a, b, _ in PAIRS if by[a]['context'] != by[b]['context']])
ck('le seconde meta CONTINUANO la prima (non ricominciano con il soggetto)',
   by[4]['italian'].lstrip(TAB).startswith('Essendo')
   and by[6]['italian'].lstrip(TAB).startswith('Il progetto')
   and by[9]['italian'].lstrip(TAB).startswith('Benché')
   and not by[6]['italian'].lstrip(TAB).startswith('L Augen'),
   [by[i]['italian'][:40] for i in (4, 6, 9)])
ck('il Corundum CONTINUA la scheda di L286 (riga 302) invece di riaprirla',
   by[1]['italian'].lstrip(TAB).startswith('Pur non potendo')
   and not by[1]['italian'].lstrip(TAB).startswith('Il Corundum'),
   by[1]['italian'][:50])
prev = sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L286_*', 'translation.json')))
prev302 = [u for u in json.load(open(prev[-1], encoding='utf-8'))['units']
           if u['path'] == PATH and u['line'] == 302] if prev else []
ck('L286 ha davvero la riga 302 del Corundum, e la sua resa finisce con «avanzati.»',
   len(prev302) == 1 and prev302[0]['context'] == 'ship:Corundum' and prev302[0]['italian'].endswith('avanzati.')
   and not prev302[0]['italian'].endswith('. '),
   prev302[0]['italian'][-60:] if prev302 else 'L286 assente')
ck('TAB: quattro, sulle unita 1, 4, 6, 9, come PRIMO carattere',
   sum(u['english'].count(TAB) for u in cov) == 4 == sum(u['italian'].count(TAB) for u in cov)
   and [u['idx'] for u in cov if TAB in u['english']] == [1, 4, 6, 9] == [u['idx'] for u in cov if TAB in u['italian']]
   and all(u['italian'].startswith(TAB) for u in cov if u['idx'] in (1, 4, 6, 9)))
ck('VIRGOLETTE: zero in inglese e zero in italiano',
   sum(u['english'].count(QUOTE) for u in cov) == 0 == sum(u['italian'].count(QUOTE) for u in cov))
ck('SEGNAPOSTO e ALTERNATIVE: zero', sum(len(TAG.findall(u['english'])) for u in cov) == 0
   == sum(len(TAG.findall(u['italian'])) for u in cov)
   and sum(len(ALT.findall(u['english'])) for u in cov) == 0 == sum(len(ALT.findall(u['italian'])) for u in cov))
ck('APICI: quattro in inglese, dieci in italiano',
   sum(u['english'].count(APOS) for u in cov) == 4 and sum(u['italian'].count(APOS) for u in cov) == 10,
   (sum(u['english'].count(APOS) for u in cov), sum(u['italian'].count(APOS) for u in cov)))
ck('nomi di modello e di luogo INVARIATI',
   all(n in ''.join(u['italian'] for u in cov) for n in NAMES),
   [n for n in NAMES if n not in ''.join(u['italian'] for u in cov)])
ck("l'Augen-Class resta `L'Augen-Class` (elisione, non «La Augen»)",
   by[5]['italian'].startswith("L'Augen-Class") and by[5]['italian'].count("Augen-Class") == 1
   and "La Augen" not in by[5]['italian'])
ck('`Enbi` e `Heutesl` invariati, con il possessivo reso in italiano',
   'canyon di Enbi' in by[5]['italian'] and 'sistema natale dei Gegno, Heutesl' in by[2]['italian'])
ck('registro in terza persona: nessun «tu»/«tuo»',
   not [u['idx'] for u in cov if re.search(r'\b(tu|tuo|tua|tuoi|tue|ti|te)\b', u['italian'])],
   [u['idx'] for u in cov if re.search(r'\b(tu|tuo|tua|tuoi|tue|ti|te)\b', u['italian'])])
ck('lessico: scafo, cuccette, plotone, iperguida, intrastellare, torretta',
   'scafo' in by[7]['italian'] and 'cuccette' in by[8]['italian'] and 'plotone' in by[8]['italian']
   and 'iperguida' in by[2]['italian'] and 'intrastellari' in by[4]['italian'] and 'torretta' in by[9]['italian'])
ck('nessun caporale, nessun carattere tipografico',
   not [u['idx'] for u in cov for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026' if c in u['italian']])
nonlat = [(u['idx'], c) for u in cov for c in u['italian'] if ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']],
   [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90 (0,85-1,06)',
   all(0.55 < u['ratio'] < 1.90 for u in cov),
   [(u['idx'], u['ratio']) for u in cov if not 0.55 < u['ratio'] < 1.90])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("7 unita' prima della 303 (L286)",
   db.execute('select count(*) from units where path=? and line<303', (PATH,)).fetchone()[0] == 7)
ck("21 unita' dopo la 658",
   db.execute('select count(*) from units where path=? and line>658', (PATH,)).fetchone()[0] == 21)
ck('il file ha 37 unita, righe 53-1616',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (37, 53, 1616))
ck('tutte le 9 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · 6 contesti · 3 coppie spezzate · 4 tab · 0 virgolette · 0 alternative' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
