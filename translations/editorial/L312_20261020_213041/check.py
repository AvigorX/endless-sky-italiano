r"""check.py — L312 (`data/bunrodea/bunrodea outfits.txt`, righe 135-236). **Secondo lotto** del file.

Dodici unita' in **sette contesti**: **1 `VALUE`** (`Solar Batteries`, da **copiare**) e **11 `DESCRIPTION`** da tradurre.

Il lotto e' fatto di **due blocchi** e di **una famiglia**:

| righe | che cosa |
|---|---|
| 135-160 | **batterie e celle solari** (`Solar Battery`, `Solar Cell` + nota di montaggio) |
| 175-188 | **overclocker e limiter** dei reattori: lo stesso scambio di L311, applicato all'energia |
| 203-236 | **tre reattori** (`Quark`, `Electroweak`, `Dark`) ognuno con la **nota degli upgrade** |

La famiglia qui e' l'**opposto** di L311: le tre note (204, 220, 236) sono **tutte identiche** in inglese (`though.`), quindi
devono essere **identiche** in italiano.
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
PATH = 'data/bunrodea/bunrodea outfits.txt'
NOMI = ['Solar Battery', 'Solar Cell', 'Reactor Overclocker', 'Reactor Limiter',
        'Quark Reactor', 'Electroweak Reactor', 'Dark Reactor']
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


kinds = collections.Counter(u['kind'] for u in cov)
ck('unita tradotte 12/12', len(cov) == 12 == len(units), '%d/%d' % (len(cov), len(units)))
ck('1 VALUE + 11 DESCRIPTION', kinds == {'VALUE': 1, 'DESCRIPTION': 11}, dict(kinds))
ck('sette contesti',
   collections.Counter(u['context'] for u in cov) == {
       'outfit:Solar Battery': 2, 'outfit:Solar Cell': 2, 'outfit:Reactor Overclocker': 1,
       'outfit:Reactor Limiter': 1, 'outfit:Quark Reactor': 2, 'outfit:Electroweak Reactor': 2,
       'outfit:Dark Reactor': 2},
   collections.Counter(u['context'] for u in cov))
ck('il VALUE `Solar Batteries` e COPIATO per identita',
   by[1]['italian'] == by[1]['english'] == 'Solar Batteries', repr(by[1]['italian']))
ck('la famiglia delle note: 204 == 220 == 236, in inglese E in italiano',
   by[8]['italian'] == by[10]['italian'] == by[12]['italian']
   and by[8]['english'] == by[10]['english'] == by[12]['english'],
   (by[8]['italian'][-20:], by[10]['italian'][-20:], by[12]['italian'][-20:]))
ck('e tutte e tre finiscono con `though.` -> «però.»',
   all(by[i]['english'].rstrip().endswith('though.') for i in (8, 10, 12))
   and all(by[i]['italian'].rstrip().endswith('però.') for i in (8, 10, 12)),
   [by[i]['italian'][-14:] for i in (8, 10, 12)])
ck('la nota sta dopo la TAB nelle tre unita (204, 220, 236) e nella 160',
   [u['line'] for u in cov if u['italian'].startswith(TAB)] == [160, 204, 220, 236],
   [u['line'] for u in cov if u['italian'].startswith(TAB)])
ck('le 2 virgolette sono UNA coppia nella sola riga 235 (`dark star`)',
   by[11]['italian'].count(QUOTE) == 2
   and sum(u['italian'].count(QUOTE) for u in cov) == 2
   and all(u['italian'].count(QUOTE) == 0 for u in cov if u is not by[11]))
ck('SEGNAPOSTO: nessuno (asserzione vuota)', not TAG.findall(''.join(u['italian'] for u in cov)))
ck('ALTERNATIVE: nessuna (asserzione vuota)', sum(len(ALT.findall(u['italian'])) for u in cov) == 0)
ck('APICI: uno in inglese, dodici in italiano',
   sum(u['english'].count(APOS) for u in cov) == 1 and sum(u['italian'].count(APOS) for u in cov) == 12,
   (sum(u['english'].count(APOS) for u in cov), sum(u['italian'].count(APOS) for u in cov)))
ck('nomi degli oggetti INVARIATI dove compaiono',
   all(n in u['italian'] for u in cov for n in NOMI if n in u['english']),
   [(u['line'], n) for u in cov for n in NOMI if n in u['english'] and n not in u['italian']])
ck('overclocker: piu energia, meno efficienza termica; limiter: il contrario',
   'forza di generazione di energia' in by[5]['italian'] and 'efficienza termica' in by[5]['italian']
   and by[5]['italian'].index('forza di generazione') < by[5]['italian'].index('efficienza termica')
   and by[6]['italian'].index('efficienza termica') < by[6]['italian'].index('forza della sua generazione'))
ck('le due schede dei componenti sono PARALLELE: prima frase identica a meno del NOME',
   by[5]['italian'].split('è un componente', 1)[1].split('.')[0]
   == by[6]['italian'].split('è un componente', 1)[1].split('.')[0]
   and by[5]['english'].split('is a component', 1)[1].split('.')[0]
   == by[6]['english'].split('is a component', 1)[1].split('.')[0]
   and by[5]['italian'].split('è un componente', 1)[1] != by[6]['italian'].split('è un componente', 1)[1],
   (by[5]['italian'][:60], by[6]['italian'][:60]))
ck('le celle solari producono CALORE DI SCARTO che cresce con l energia',
   'calore di scarto' in by[3]['italian'] and 'cresce con' in by[3]['italian'])
ck('i reattori prendono il nome da stelle esotiche; Polaris e il XXVIII secolo',
   'stelle esotiche' in by[7]['italian'] and 'Polaris' in by[7]['italian']
   and 'XXVIII secolo' in by[7]['italian'] and 'quark' in by[7]['italian'])
ck('`stella elettrodebole` e le conversioni quark -> leptoni',
   'elettrodebole' in by[9]['italian'] and 'leptoni' in by[9]['italian'])
ck('`stella oscura` e i siti di nucleazione',
   '"stella oscura"' in by[11]['italian'] and 'nucleazione' in by[11]['italian']
   and 'materia oscura' in by[11]['italian'])
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in cov for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessun doppio spazio (la tab iniziale non conta)',
   not [u['idx'] for u in cov if '  ' in u['italian'].lstrip(TAB)])
ck('rapporto nel gate 0,55-1,90',
   all(0.55 < u['ratio'] < 1.90 for u in cov),
   [(u['idx'], u['ratio']) for u in cov if not 0.55 < u['ratio'] < 1.90])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("SEGMENTO: 12 unita' prima (L311, righe 25-130)",
   db.execute('select count(*) from units where path=? and line<135', (PATH,)).fetchone()[0] == 12)
ck("SEGMENTO: 9 unita' dopo la 236 (il prossimo lotto comincia alla 250)",
   db.execute('select count(*) from units where path=? and line>236', (PATH,)).fetchone()[0] == 9
   and db.execute('select min(line) from units where path=? and line>236', (PATH,)).fetchone()[0] == 250)
ck('FILE: 12 unita qui su 33 del file',
   db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0] == 33)
ck('tutte le 12 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · 1 VALUE + 11 DESCRIPTION in 7 contesti · 4 tab · 2 virgolette' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
