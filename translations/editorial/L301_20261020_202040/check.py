r"""check.py — L301 (`data/remnant/remnant ships.txt`, righe 17-806). **PRIMO lotto del file**.

Dodici unita' in **quattro contesti**, di cui **due gruppi da tre** (`Modified Dromedary` 350/351/352 e `Gull` 547/548/549) e
**due `VALUE`** che sono **plurali di nomi di nave** da **copiare**.

Il test verifica:

1. **i `VALUE` copiati**: `Albatrosses` e `Modified Dromedaries` restano **identici** all'inglese;
2. **la ripetizione del sorgente**: le unita' **4 e 7** (righe 350 e 474) hanno **lo stesso testo inglese** — la 474 e' la
   variante «relitto» di una nave che esiste in due stati — e devono avere la **stessa resa**;
3. **le due terzine con due tab consecutive** e la **coppia** 474/475;
4. **le quattro virgolette dritte** di «dream cells» -> "celle del sogno" (due per unita', nelle 4 e 7);
5. **il confine che NON chiude il contesto `Heron`**: la 806 e' l'**unica** unita' `Heron` del lotto e la 807 (fuori segmento) e'
   la **seconda** dello stesso contesto — e' un taglio **voluto**, non una coppia spezzata dentro il lotto.
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
PATH = 'data/remnant/remnant ships.txt'
TRIPLE1 = [350, 351, 352]
TRIPLE2 = [547, 548, 549]
PAIR = (474, 475)
TABBED = [351, 352, 475, 548, 549]
VALUES = {1: 'Albatrosses', 3: 'Modified Dromedaries'}
NAMES = ['Remnant', 'Alphas', 'Korath', 'Starling', 'Gull', 'Heron', 'Albatross', 'Dromedary',
         'Tycho Crater Cooperative', 'Shattered Light']
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
at = {u['line']: u for u in cov}
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


grp = collections.Counter(u['context'] for u in cov)
ck('unita tradotte 12/12', len(cov) == 12 == len(units), '%d/%d' % (len(cov), len(units)))
ck('dieci DESCRIPTION + due VALUE, quattro contesti (6 + 3 + 2 + 1)',
   collections.Counter(u['kind'] for u in cov) == {'DESCRIPTION': 10, 'VALUE': 2}
   and dict(grp) == {'ship:Modified Dromedary': 6, 'ship:Gull': 3, 'ship:Albatross': 2, 'ship:Heron': 1}, dict(grp))
ck('VALUE copiati: `Albatrosses` e `Modified Dromedaries` identici all inglese',
   all(by[i]['italian'] == VALUES[i] == by[i]['english'] for i in VALUES),
   {i: by[i]['italian'] for i in VALUES})
ck('TERZINE: 350/351/352 e 547/548/549, stesso contesto, tab sulla seconda e sulla terza',
   [u['line'] for u in cov if u['context'] == 'ship:Modified Dromedary'
    and u['kind'] == 'DESCRIPTION' and u['line'] < 400] == TRIPLE1
   and [u['line'] for u in cov if u['context'] == 'ship:Gull'] == TRIPLE2
   and all(at[l]['english'].startswith(TAB) and at[l]['italian'].startswith(TAB) for l in (351, 352, 548, 549))
   and not at[350]['english'].startswith(TAB) and not at[547]['english'].startswith(TAB))
ck('COPPIA 474/475: stesso contesto, tab sulla seconda',
   at[475]['context'] == at[474]['context'] and at[475]['english'].startswith(TAB))
ck('TAB: esattamente cinque unita la portano, alle righe dichiarate',
   sorted(u['line'] for u in cov if u['english'].startswith(TAB)) == TABBED
   and sum(u['italian'].count(TAB) for u in cov) == 5)
ck('RIPETIZIONE: le unita 4 e 7 (350 e 474) identiche in inglese E in italiano',
   by[4]['english'] == by[7]['english'] and by[4]['italian'] == by[7]['italian'])
ck('le unita 10 sono tutte TRADOTTE (i 2 VALUE sono copiati ed esclusi dal conteggio)',
   all(u['italian'] != u['english'] for u in cov if u['kind'] == 'DESCRIPTION'))
ck('VIRGOLETTE: quattro in inglese e quattro in italiano, tutte dritte, su «dream cells» / "celle del sogno"',
   sum(u['english'].count(QUOTE) for u in cov) == 4 == sum(u['italian'].count(QUOTE) for u in cov)
   and by[4]['italian'].count(QUOTE) == 2 and by[7]['italian'].count(QUOTE) == 2
   and 'celle del sogno' in by[4]['italian'])
ck('SEGNAPOSTO e ALTERNATIVE: zero (asserzioni vuote)',
   sum(len(TAG.findall(u['italian'])) for u in cov) == 0
   and sum(len(ALT.findall(u['italian'])) for u in cov) == 0)
ck('APICI: sei in inglese, quattordici in italiano',
   sum(u['english'].count(APOS) for u in cov) == 6 and sum(u['italian'].count(APOS) for u in cov) == 14,
   (sum(u['english'].count(APOS) for u in cov), sum(u['italian'].count(APOS) for u in cov)))
ck('nomi di nave, fazioni e luoghi INVARIATI',
   all(n in ''.join(u['italian'] for u in cov) for n in NAMES),
   [n for n in NAMES if n not in ''.join(u['italian'] for u in cov)])
ck('REGISTRO: nessuna seconda persona',
   not [u['idx'] for u in cov if re.search(r'\b(tu|tuo|tua|tuoi|tue|ti|te)\b', u['italian'])],
   [u['idx'] for u in cov if re.search(r'\b(tu|tuo|tua|tuoi|tue|ti|te)\b', u['italian'])])
ck('terminologia: navi-città, serre idroponiche, spazioporti mobili, occultamento',
   'navi-città' in by[4]['italian'] and 'serre idroponiche' in by[4]['italian']
   and 'spazioporti mobili' in by[12]['italian'] and 'occultamento' in by[11]['italian'])
ck('nessun caporale, nessun carattere tipografico',
   not [u['idx'] for u in cov for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026' if c in u['italian']])
nonlat = [(u['idx'], c) for u in cov for c in u['italian'] if ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessun doppio spazio (la tab iniziale non conta)',
   not [u['idx'] for u in cov if '  ' in u['italian'].lstrip(TAB)])
ck('rapporto nel gate 0,55-1,90 (0,91-1,17)',
   all(0.55 < u['ratio'] < 1.90 for u in cov),
   [(u['idx'], u['ratio']) for u in cov if not 0.55 < u['ratio'] < 1.90])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("ZERO unita' prima della 17: il lotto APRE il file",
   db.execute('select count(*) from units where path=? and line<17', (PATH,)).fetchone()[0] == 0)
ck("26 unita' dopo la 806; la 807 e la SECONDA unita del contesto `Heron`",
   db.execute('select count(*) from units where path=? and line>806', (PATH,)).fetchone()[0] == 26
   and db.execute('select line,context from units where path=? and line>806 order by line limit 1', (PATH,)).fetchone()
   == (807, 'ship:Heron'))
ck('il file ha 38 unita (35 DESCRIPTION + 3 VALUE), righe 17-1826',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (38, 17, 1826)
   and dict(db.execute('select kind,count(*) from units where path=? group by kind', (PATH,)).fetchall())
   == {'DESCRIPTION': 35, 'VALUE': 3})
ck('tutte le 12 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · 4 contesti · 2 terzine + 1 coppia · 5 tab · file 12/38' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
