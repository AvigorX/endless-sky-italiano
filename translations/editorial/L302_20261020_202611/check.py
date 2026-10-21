r"""check.py — L302 (`data/remnant/remnant ships.txt`, righe 807-1291). **Secondo lotto del file**.

Dodici unita' in **sei contesti**: la **terzina `Peregrine`** (1289/1290/1291, due tab consecutive), **quattro coppie**
(`Ibis`, `Merganser`, `Penguin`, e `Heron` che pero' e' **spezzata** fra due lotti) e **una singola** (`Pelican`).

Il test verifica:

1. **la formula dell'occultamento e' la FAMIGLIA di quattro frasi**: `Merganser` (982), `Penguin` (1202), `Peregrine` (1291) qui,
   e `Gull` (549) in L301. Si **riapre** `L301/translation.json` e si confronta: la resa deve essere **identica a meno del nome
   della nave**;
2. **la continuita' di `Heron`**: la 807 e' la **seconda** unita' del contesto, la 806 (L301) la **prima**;
3. **il `VALUE` copiato**: `Ibises` resta inglese;
4. **la terzina `Peregrine`** con due tab consecutive.
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
PREV = os.path.join(L10N, 'staging', 'editorial', 'L301_20261020_202040', 'translation.json')
PATH = 'data/remnant/remnant ships.txt'
TERZINA = [1289, 1290, 1291]
COPPIE = [(892, 893), (981, 982), (1201, 1202)]
TABBED = [807, 893, 982, 1202, 1290, 1291]
CLOAK = {982: 'Merganser', 1202: 'Penguin', 1291: 'Peregrine'}
NAMES = ['Remnant', 'Heron', 'Ibis', 'Merganser', 'Pelican', 'Penguin', 'Peregrine', 'Taely',
         'Ember Waste', 'Albatross']
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
prev = {u['line']: u for u in json.load(open(PREV, encoding='utf-8'))['units']}
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


grp = collections.Counter(u['context'] for u in cov)
ck('unita tradotte 12/12', len(cov) == 12 == len(units), '%d/%d' % (len(cov), len(units)))
ck('undici DESCRIPTION + un VALUE, sei contesti',
   collections.Counter(u['kind'] for u in cov) == {'DESCRIPTION': 11, 'VALUE': 1}
   and len(grp) == 6 and sorted(grp.values()) == [1, 1, 2, 2, 3, 3], dict(grp))
ck('TERZINA `Peregrine` 1289/1290/1291, tab sulla seconda e sulla terza',
   [u['line'] for u in cov if u['context'] == 'ship:Peregrine'] == TERZINA
   and at[1290]['english'].startswith(TAB) and at[1291]['english'].startswith(TAB)
   and not at[1289]['english'].startswith(TAB)
   and at[1290]['italian'].startswith(TAB) and at[1291]['italian'].startswith(TAB))
ck('COPPIE `Ibis` 892/893, `Merganser` 981/982, `Penguin` 1201/1202, tab sulla seconda',
   all(at[b]['context'] == at[a]['context'] and at[b]['english'].startswith(TAB) for a, b in COPPIE))
ck('la singola e `Pelican` 1072', grp['ship:Pelican'] == 1 and at[1072]['context'] == 'ship:Pelican')
ck('TAB: esattamente sei unita la portano, alle righe dichiarate',
   sorted(u['line'] for u in cov if u['english'].startswith(TAB)) == TABBED
   and sum(u['italian'].count(TAB) for u in cov) == 6)
ck('CONTINUITA `Heron`: la 807 e la seconda unita, la 806 (L301) la prima',
   at[807]['context'] == 'ship:Heron' and prev[806]['context'] == 'ship:Heron'
   and at[807]['english'].startswith(TAB) and not prev[806]['english'].startswith(TAB))
ck('FORMULA DELL OCCULTAMENTO: tre qui + la `Gull` di L301, identiche a meno del nome',
   all(at[l]['italian'].replace(n, 'X') == prev[549]['italian'].replace('Gull', 'X')
       for l, n in CLOAK.items()),
   [(l, at[l]['italian'][:40]) for l, n in CLOAK.items()
    if at[l]['italian'].replace(n, 'X') != prev[549]['italian'].replace('Gull', 'X')])
ck('VALUE copiato: `Ibises` identico all inglese',
   by[2]['italian'] == 'Ibises' == by[2]['english'])
ck('le 11 DESCRIPTION sono tutte TRADOTTE',
   all(u['italian'] != u['english'] for u in cov if u['kind'] == 'DESCRIPTION'))
ck('VIRGOLETTE, SEGNAPOSTO, ALTERNATIVE: tutti zero (asserzioni vuote)',
   sum(u['english'].count(QUOTE) for u in cov) == 0 == sum(u['italian'].count(QUOTE) for u in cov)
   and sum(len(TAG.findall(u['italian'])) for u in cov) == 0
   and sum(len(ALT.findall(u['italian'])) for u in cov) == 0)
ck('APICI: sei in inglese, quindici in italiano',
   sum(u['english'].count(APOS) for u in cov) == 6 and sum(u['italian'].count(APOS) for u in cov) == 15,
   (sum(u['english'].count(APOS) for u in cov), sum(u['italian'].count(APOS) for u in cov)))
ck('nomi di nave, persone e luoghi INVARIATI',
   all(n in ''.join(u['italian'] for u in cov) for n in NAMES),
   [n for n in NAMES if n not in ''.join(u['italian'] for u in cov)])
ck('REGISTRO: nessuna seconda persona',
   not [u['idx'] for u in cov if re.search(r'\b(tu|tuo|tua|tuoi|tue|ti|te)\b', u['italian'])],
   [u['idx'] for u in cov if re.search(r'\b(tu|tuo|tua|tuoi|tue|ti|te)\b', u['italian'])])
ck('lessico del corpus: «mordi e fuggi» (non «mordi-e-fuggi»), «spiriti del vuoto», «prefetto»',
   'mordi e fuggi' in by[5]['italian'] and 'spiriti del vuoto' in by[8]['italian']
   and 'prefetto' in by[1]['italian'] and 'mordi-e-fuggi' not in ''.join(u['italian'] for u in cov))
ck('`Ember Waste` resta invariato (anomalia aperta, decisione dichiarata)',
   'Ember Waste' in by[7]['italian'] and 'Ember Waste' in by[8]['italian'])
ck('nessun caporale, nessun carattere tipografico',
   not [u['idx'] for u in cov for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026' if c in u['italian']])
nonlat = [(u['idx'], c) for u in cov for c in u['italian'] if ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessun doppio spazio (la tab iniziale non conta)',
   not [u['idx'] for u in cov if '  ' in u['italian'].lstrip(TAB)])
ck('rapporto nel gate 0,55-1,90 (1,00-1,13)',
   all(0.55 < u['ratio'] < 1.90 for u in cov),
   [(u['idx'], u['ratio']) for u in cov if not 0.55 < u['ratio'] < 1.90])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("12 unita' prima della 807 (L301)",
   db.execute('select count(*) from units where path=? and line<807', (PATH,)).fetchone()[0] == 12)
ck("14 unita' dopo la 1291; la prima e `Petrel` alla 1378",
   db.execute('select count(*) from units where path=? and line>1291', (PATH,)).fetchone()[0] == 14
   and db.execute('select line,context from units where path=? and line>1291 order by line limit 1', (PATH,)).fetchone()
   == (1378, 'ship:Petrel'))
ck('il file ha 38 unita, righe 17-1826',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (38, 17, 1826))
ck('tutte le 12 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · 6 contesti · formula occultamento x4 con L301 · file 24/38' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
