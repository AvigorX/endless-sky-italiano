r"""check.py — L267 (`data/human/engines.txt`, righe 27-194). Primo lotto del file: **equipaggiamento umano**.

11 `DESCRIPTION` (postbruciatori e propulsori ionici) e **1 `VALUE`** (nome di equipaggiamento, da copiare). Tre cose da
verificare con cura:

1. **tre tab**, alle righe **141, 159, 177** — le tre copie della stessa scheda sui motori ionici: il tab e' il **primo
   carattere** e va conservato in tutte e tre;
2. **due virgolette** alla riga **121**, e sono **dritte** (`"adequate"`): la resa italiana le tiene dritte, non come
   caporali, altrimenti il conteggio cambia e il testo del gioco cambia con lui;
3. **terminologia**: postbruciatore, propulsore, spinta, carburante per l'iperspazio, motori ionici, motori al plasma, nave
   capitale, mercantile, batterie — tutte forme gia' presenti nel corpus (`tooltips.txt` in testa).
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
PATH = 'data/human/engines.txt'
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
BLOCCHI = [('outfit:Volcano Afterburner', 27, 27), ('outfit:Caldera Afterburner', 54, 54),
           ('outfit:Ionic Afterburner', 83, 83), ('outfit:X1050 Ion Engines', 100, 121),
           ('outfit:X1700 Ion Thruster', 140, 141), ('outfit:X2700 Ion Thruster', 158, 159),
           ('outfit:X3700 Ion Thruster', 176, 177), ('outfit:X4700 Ion Thruster', 194, 194)]
IONICA = [7, 9, 11]
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck('unita tradotte 12/12', len(cov) == 12 == len(units), '%d/%d' % (len(cov), len(units)))
ck('tipi: 11 DESCRIPTION + 1 VALUE',
   collections.Counter(u['kind'] for u in units) == {'DESCRIPTION': 11, 'VALUE': 1},
   dict(collections.Counter(u['kind'] for u in units)))
ck('otto contesti, con le righe misurate',
   [(c, by[[u['idx'] for u in cov if u['context'] == c][0]]['line'],
     by[[u['idx'] for u in cov if u['context'] == c][-1]]['line']) for c, _, _ in BLOCCHI] == BLOCCHI,
   [(c, by[[u['idx'] for u in cov if u['context'] == c][0]]['line']) for c, _, _ in BLOCCHI])
ck('righe 27-194, nessun buco interno',
   [u['line'] for u in cov] == sorted({u['line'] for u in cov})
   and cov[0]['line'] == 27 and cov[-1]['line'] == 194)
ck('il VALUE e COPIATO (nome di equipaggiamento)',
   by[4]['kind'] == 'VALUE' and by[4]['italian'] == by[4]['english'] == 'X1050 Ion Engines')
ck('le 11 DESCRIPTION sono TRADOTTE, nessuna copiata',
   all(u['italian'] != u['english'] for u in cov if u['kind'] == 'DESCRIPTION'),
   [u['idx'] for u in cov if u['kind'] == 'DESCRIPTION' and u['italian'] == u['english']])
ck('TAB: tre in inglese e tre in italiano, alle righe 141, 159, 177, come PRIMO carattere',
   sum(u['english'].count(TAB) for u in cov) == 3 == sum(u['italian'].count(TAB) for u in cov)
   and [u['line'] for u in cov if TAB in u['english']] == [141, 159, 177]
   == [u['line'] for u in cov if TAB in u['italian']]
   and all(u['italian'].startswith(TAB) for u in cov if TAB in u['italian']))
ck('le tre copie della scheda ionica hanno UNA sola resa',
   len({by[i]['italian'] for i in IONICA}) == 1 and len({by[i]['english'] for i in IONICA}) == 1,
   len({by[i]['italian'] for i in IONICA}))
ck('VIRGOLETTE: 2 in inglese e 2 in italiano, entrambe all unita 5 (riga 121) e DRITTE',
   sum(u['english'].count(QUOTE) for u in cov) == 2 == sum(u['italian'].count(QUOTE) for u in cov)
   and [u['idx'] for u in cov if QUOTE in u['italian']] == [5]
   and '"adeguato"' in by[5]['italian'],
   (sum(u['italian'].count(QUOTE) for u in cov), by[5]['italian'][:80]))
ck('APICI: 1 in inglese (unita 3), 6 in italiano su 5 unita, mappa dichiarata',
   {u['idx']: u['english'].count(APOS) for u in cov if APOS in u['english']} == {3: 1}
   and {u['idx']: u['italian'].count(APOS) for u in cov if APOS in u['italian']}
   == {1: 2, 3: 1, 5: 1, 6: 1, 12: 1},
   ({u['idx']: u['english'].count(APOS) for u in cov if APOS in u['english']},
    {u['idx']: u['italian'].count(APOS) for u in cov if APOS in u['italian']}))
ck('ZERO segnaposto (asserzione negativa)',
   not [t for u in cov for t in TAG.findall(u['english']) + TAG.findall(u['italian'])])
ck('terminologia del corpus: postbruciatore, propulsore, spinta, carburante per l\'iperspazio',
   'postbruciatore' in by[1]['italian'] and 'propulsore' in by[6]['italian']
   and 'spinta' in by[1]['italian'] and "carburante per l'iperspazio" in by[1]['italian']
   and 'afterburner' not in ' '.join(u['italian'] for u in cov if u['kind'] == 'DESCRIPTION'),
   [u['idx'] for u in cov if 'afterburner' in u['italian']])
ck('terminologia: motori ionici / motori al plasma / nave capitale / mercantile / batterie',
   'motori ionici' in by[7]['italian'] and 'motori al plasma' in by[7]['italian']
   and 'nave capitale' in by[12]['italian'] and 'mercantili' in by[8]['italian']
   and 'batterie' in by[3]['italian'])
ck('i nomi dei modelli restano invariati: Caldera, Ionic, X1050, X2700, X3700, X4700',
   all(nome in ' '.join(u['italian'] for u in cov)
       for nome in ('Caldera', 'Ionic', 'X1050', 'X2700', 'X3700', 'X4700')))
ck('nessun caporale, nessun carattere tipografico',
   not [u['idx'] for u in cov for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026' if c in u['italian']])
nonlat = [(u['idx'], c) for u in cov for c in u['italian'] if ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']],
   [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90',
   all(0.55 < u['ratio'] < 1.90 for u in cov),
   [(u['idx'], u['ratio']) for u in cov if not 0.55 < u['ratio'] < 1.90])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("ZERO unita' prima della 27: il lotto APRE il file",
   db.execute('select count(*) from units where path=? and line<27', (PATH,)).fetchone()[0] == 0)
ck("49 unita' dopo la 194",
   db.execute('select count(*) from units where path=? and line>194', (PATH,)).fetchone()[0] == 49)
ck('il file ha 61 unita, righe 27-717',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (61, 27, 717))
st = dict(db.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('tutte le 12 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · 8 contesti' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
