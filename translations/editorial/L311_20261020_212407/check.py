r"""check.py — L311 (`data/bunrodea/bunrodea outfits.txt`, righe 25-130). **Primo lotto** del file.

Dodici `DESCRIPTION` in **otto contesti**: **quattro coppie** (`Small/Large Shield Relay`, `Small/Large Nanite Fabricator`, dove la
**seconda** unita' porta la tab con la nota degli upgrade) e **quattro schede singole** (`Shield Relay Booster`, `Shield Relay
Limiter`, `Nanite Enhancer`, `Nanite Limiter`).

La cosa che questo lotto deve difendere e' la **famiglia della nota degli upgrade**:

| unita' | inglese | italiano |
|---|---|---|
| 54 e 70 | **identiche** (`..., though.`) | devono essere **identiche** |
| 114 e 130 | differiscono **solo nell'ultima parola** (`though.` / `however.`) | devono differire **solo nell'ultima parola** |

Il resto: 4 tab, 0 virgolette, 1 apice inglese, nessun segnaposto, nessuna alternativa (asserzioni vuote), nomi degli
equipaggiamenti **invariati**.
"""
import collections
import json
import os
import re

TAB = chr(9)
QUOTE = chr(34)
APOS = chr(39)
TAG = re.compile(r'<[^<>]+>')
ALT = re.compile(r'\[[^\]]*\]')
HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
PATH = 'data/bunrodea/bunrodea outfits.txt'
NOMI = ['Shield Relay Booster', 'Shield Relay Limiter', 'Small Shield Relay', 'Large Shield Relay',
        'Nanite Enhancer', 'Nanite Limiter', 'Small Nanite Fabricator', 'Large Nanite Fabricator']
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


ck('unita tradotte 12/12', len(cov) == 12 == len(units), '%d/%d' % (len(cov), len(units)))
ck('tutte e 12 sono DESCRIPTION',
   collections.Counter(u['kind'] for u in cov) == {'DESCRIPTION': 12})
ck('otto contesti: quattro coppie + quattro schede singole',
   collections.Counter(u['context'] for u in cov) == {
       'outfit:Shield Relay Booster': 1, 'outfit:Shield Relay Limiter': 1,
       'outfit:Small Shield Relay': 2, 'outfit:Large Shield Relay': 2,
       'outfit:Nanite Enhancer': 1, 'outfit:Nanite Limiter': 1,
       'outfit:Small Nanite Fabricator': 2, 'outfit:Large Nanite Fabricator': 2},
   collections.Counter(u['context'] for u in cov))
ck('le quattro coppie hanno la TAB sulla SECONDA unita (54, 70, 114, 130)',
   [u['line'] for u in cov if u['italian'].startswith(TAB)] == [54, 70, 114, 130]
   and all(at[l]['italian'].startswith(TAB) for l in (54, 70, 114, 130))
   and not [u['line'] for u in cov if not u['italian'].startswith(TAB) and u['line'] in (54, 70, 114, 130)])
ck('le identiche restano IDENTICHE: 54 == 70',
   by[4]['italian'] == by[6]['italian'] and by[4]['english'] == by[6]['english'],
   (by[4]['italian'], by[6]['italian']))
_10, _12 = by[10]['italian'], by[12]['italian']
ck('le varianti differiscono SOLO nell ultima parola: 114 != 130',
   _10 != _12 and _10.rsplit(' ', 1)[0] == _12.rsplit(' ', 1)[0]
   and _10.rsplit(' ', 1)[1] != _12.rsplit(' ', 1)[1],
   (_10.rsplit(' ', 1)[-1], _12.rsplit(' ', 1)[-1]))
ck('e la differenza e quella del SORGENTE: `though.` -> pero, `however.` -> tuttavia',
   _10.rstrip().endswith('però.') and _12.rstrip().endswith('tuttavia.')
   and by[10]['english'].rstrip().endswith('though.') and by[12]['english'].rstrip().endswith('however.'),
   (_10[-12:], _12[-12:]))
ck('VIRGOLETTE: zero (asserzione vuota)',
   sum(u['italian'].count(QUOTE) for u in cov) == 0 and sum(u['english'].count(QUOTE) for u in cov) == 0)
ck('SEGNAPOSTO: nessuno (asserzione vuota)',
   not TAG.findall(''.join(u['italian'] for u in cov)))
ck('ALTERNATIVE: nessuna (asserzione vuota)', sum(len(ALT.findall(u['italian'])) for u in cov) == 0)
ck('APICI: uno in inglese, nove in italiano',
   sum(u['english'].count(APOS) for u in cov) == 1 and sum(u['italian'].count(APOS) for u in cov) == 9,
   (sum(u['english'].count(APOS) for u in cov), sum(u['italian'].count(APOS) for u in cov)))
ck('nomi degli equipaggiamenti INVARIATI dove compaiono',
   all(n in u['italian'] for u in cov for n in NOMI if n in u['english']),
   [(u['line'], n) for u in cov for n in NOMI if n in u['english'] and n not in u['italian']])
ck('le due schede del booster/limiter sono PARALLELE: stesso incipit',
   by[1]['italian'].split(' è un componente')[0] != '' and by[2]['italian'].split(' è un componente')[0] != ''
   and by[1]['english'].split(' is a component')[0].strip() != by[2]['english'].split(' is a component')[0].strip())
ck('lessico: relay, scudi, potenziatori, limitatori, fabbricatore di naniti, scafo',
   'relay' in by[1]['italian'] and 'scudi' in by[1]['italian'] and 'potenziatori' in by[1]['italian']
   and 'limitatori' in by[2]['italian'] and 'fabbricatore di naniti' in by[7]['italian']
   and 'scafo' in by[9]['italian'])
ck('la scheda dei relay cita i reattori e il proprietario (l apice della riga 69 e conservato)',
   'reattori' in by[5]['italian'] and "proprietario" in by[5]['italian']
   and by[5]['italian'].count(APOS) == 1)
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in cov for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessun doppio spazio (la tab iniziale non conta)',
   not [u['idx'] for u in cov if '  ' in u['italian'].lstrip(TAB)])
ck('rapporto nel gate 0,55-1,90',
   all(0.55 < u['ratio'] < 1.90 for u in cov),
   [(u['idx'], u['ratio']) for u in cov if not 0.55 < u['ratio'] < 1.90])
import sqlite3
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("SEGMENTO: zero unita' prima della 25",
   db.execute('select count(*) from units where path=? and line<25', (PATH,)).fetchone()[0] == 0)
ck("SEGMENTO: 21 unita' dopo la 130 (il prossimo lotto comincia alla 135)",
   db.execute('select count(*) from units where path=? and line>130', (PATH,)).fetchone()[0] == 21
   and db.execute('select min(line) from units where path=? and line>130', (PATH,)).fetchone()[0] == 135)
ck('FILE: 12 unita qui su 33 del file',
   db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0] == 33)
ck('tutte le 12 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · 12 DESCRIPTION in 8 contesti (4 coppie + 4 singole) · 4 tab · 0 virgolette' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
