r"""check.py — L273 (`data/korath/korath ships.txt`, righe 95-360). **Primo lotto del file**.

**8 `DESCRIPTION` lunghe** (media 57 parole) su **quattro navi Korath**: `Rano'erek` (nave dragante per asteroidi), `Palavret`
(nave da razzia), `Tubfalet` (razziatore nuovo) e `'nra'ret` (cacciatore). Tre cose da verificare con cura:

1. **quattro tab** sulle unita' pari (2, 4, 6, 8): la seconda scheda di ogni nave e' rientrata;
2. **i nomi Korath hanno apostrofi** (`Rano'erek`, `'olofez`, `'nra'ret`, `Ik'atilajej`, `Korsmanath A'awoj`): restano
   **invariati** e vanno verificati **dove compaiono**, non globalmente;
3. **nove apici in inglese** (tutti nei nomi) e **quindici in italiano** (i nomi piu' le elisioni): le due mappe sono diverse e
   vanno dichiarate.
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
HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
PATH = 'data/korath/korath ships.txt'
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
BLOCCHI = [("ship:Rano'erek", 95, 96), ('ship:Palavret', 170, 171),
           ('ship:Tubfalet', 285, 286), ("ship:'nra'ret", 359, 360)]
TABBED = [2, 4, 6, 8]
NOMI = ['Rano\'erek', 'Palavret', 'Tubfalet', 'nra\'ret', 'olofez', 'Ik\'atilajej', 'Korsmanath A\'awoj']
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck('unita tradotte 8/8', len(cov) == 8 == len(units), '%d/%d' % (len(cov), len(units)))
ck('tipo: 8 DESCRIPTION, nessun VALUE ne TEXT',
   collections.Counter(u['kind'] for u in units) == {'DESCRIPTION': 8},
   dict(collections.Counter(u['kind'] for u in units)))
ck('quattro contesti, con le righe misurate',
   [(c, by[[u['idx'] for u in cov if u['context'] == c][0]]['line'],
     by[[u['idx'] for u in cov if u['context'] == c][-1]]['line']) for c, _, _ in BLOCCHI] == BLOCCHI,
   [(c, by[[u['idx'] for u in cov if u['context'] == c][0]]['line']) for c, _, _ in BLOCCHI])
ck('righe 95-360, nessun buco interno, due unita per nave',
   [u['line'] for u in cov] == sorted({u['line'] for u in cov})
   and cov[0]['line'] == 95 and cov[-1]['line'] == 360
   and all(sum(1 for u in cov if u['context'] == c) == 2 for c, _, _ in BLOCCHI))
ck('tutte TRADOTTE, nessuna copiata',
   all(u['italian'] != u['english'] for u in cov), [u['idx'] for u in cov if u['italian'] == u['english']])
ck('TAB: quattro in inglese e quattro in italiano, sulle unita pari, come PRIMO carattere',
   sum(u['english'].count(TAB) for u in cov) == 4 == sum(u['italian'].count(TAB) for u in cov)
   and [u['idx'] for u in cov if TAB in u['english']] == TABBED == [u['idx'] for u in cov if TAB in u['italian']]
   and all(u['italian'].startswith(TAB) for u in cov if u['idx'] in TABBED))
ck('i nomi Korath restano dove l inglese li nomina',
   not [(u['idx'], n) for u in cov for n in NOMI if n in u['english'] and n not in u['italian']],
   [(u['idx'], n) for u in cov for n in NOMI if n in u['english'] and n not in u['italian']])
ck("l'apostrofo dei nomi non si normalizza: `'nra'ret` e `'olofez` cominciano con apostrofo",
   "'nra'ret" in by[7]['italian'] and "'olofez" in by[7]['italian']
   and "'nra'ret" in by[8]['italian'])
ck('APICI in inglese: 9 (unita 1: 1, 4: 1, 7: 5, 8: 2), tutti nei nomi o nei possessivi',
   {u['idx']: u['english'].count(APOS) for u in cov if APOS in u['english']} == {1: 1, 4: 1, 7: 5, 8: 2},
   {u['idx']: u['english'].count(APOS) for u in cov if APOS in u['english']})
ck('APICI in italiano: 15 (nomi + elisioni), mappa dichiarata',
   {u['idx']: u['italian'].count(APOS) for u in cov if APOS in u['italian']}
   == {1: 2, 3: 1, 4: 1, 5: 1, 7: 6, 8: 4},
   {u['idx']: u['italian'].count(APOS) for u in cov if APOS in u['italian']})
ck('ZERO virgolette e ZERO segnaposto (due asserzioni negative)',
   sum(u['english'].count(QUOTE) + u['italian'].count(QUOTE) for u in cov) == 0
   and not [t for u in cov for t in TAG.findall(u['english']) + TAG.findall(u['italian'])])
ck('lessico Korath dal corpus: Esiliati, razziatori, navi-mondo, nave da razzia, cacciatore imbarcato',
   'Esiliati' in by[7]['italian'] and "dell'Esilio" in by[4]['italian']
   and 'razziatori' in by[1]['italian'] and 'navi-mondo' in by[1]['italian']
   and 'nave da razzia' in by[3]['italian'] and 'cacciatore imbarcato' in by[7]['italian'])
ck('i quattro tipi di nave sono distinti: dragante, da razzia, cacciatore, razziatore',
   'nave dragante per asteroidi' in by[1]['italian']
   and 'nave da razzia di classe Palavret' in by[3]['italian']
   and 'cacciatore di classe' in by[7]['italian']
   and 'razziatore per affrontare bersagli moderni' in by[6]['italian'])
ck('armamento: portelli lanciamissili, lanciatori di mitraglia, Lance di fuoco',
   'portelli lanciamissili' in by[8]['italian'] and 'lanciatori di mitraglia' in by[8]['italian']
   and 'Lance di fuoco' in by[8]['italian'])
ck('Remnant invariato; nessun termine inglese residuo delle parole chiave',
   'Remnant' in by[6]['italian']
   and not [u['idx'] for u in cov for w in ('raider', 'warship', 'chaser', 'dredging', 'flagship')
            if w in u['italian'].lower()],
   [(u['idx'], w) for u in cov for w in ('raider', 'warship', 'chaser', 'dredging', 'flagship')
    if w in u['italian'].lower()])
ck('nessun caporale, nessun carattere tipografico',
   not [u['idx'] for u in cov for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026' if c in u['italian']])
nonlat = [(u['idx'], c) for u in cov for c in u['italian'] if ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']],
   [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90 (1,05-1,20)',
   all(0.55 < u['ratio'] < 1.90 for u in cov),
   [(u['idx'], u['ratio']) for u in cov if not 0.55 < u['ratio'] < 1.90])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("ZERO unita' prima della 95: il lotto APRE il file",
   db.execute('select count(*) from units where path=? and line<95', (PATH,)).fetchone()[0] == 0)
ck("42 unita' dopo la 360",
   db.execute('select count(*) from units where path=? and line>360', (PATH,)).fetchone()[0] == 42)
ck('il file ha 50 unita, righe 95-2363',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (50, 95, 2363),
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone())
st = dict(db.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('tutte le 8 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · 4 contesti · 4 tab' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
