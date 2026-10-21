r"""check.py — L317 (`data/coalition/coalition ships.txt`, righe 1141-2195). **LOTTO TERMINALE**.

Diciassette `DESCRIPTION` in **13 contesti** — `Heliarch` (`Neutralizer`, `Punisher`, `Pursuer` x3, `Rover` x2, `Stalker` x2),
**Kimek** (`Briar`, `Spire`, `Thistle`, `Thorn`) e **Saryd** (`Runabout`, `Sojourner`, `Traveler`, `Visitor`).

Il punto delicato, **misurato prima di tradurre**:

| riga | che cosa |
|---|---|
| 1504 | nota **del `Pursuer`**: progetto Kimek piu' economico e piu' veloce (una sola volta) |
| 1505, 1564, 1621 | la **stessa** nota «Fighters do not come equipped with a hyperdrive…», **identica in TRE unita'** |

Quindi la famiglia e' **tre volte la stessa frase** (l'opposto di L312, dove erano tre identiche della stessa nave): qui sono tre
**navi diverse** che condividono **la stessa nota**. La resa deve essere identica **in tutte e tre**, e diversa dalla 1504.

La nota usa la **seconda persona** («You cannot carry a fighter»): in un file impersonale e' l'unica, e il test la **elenca** invece di
lasciarla passare.
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
PATH = 'data/coalition/coalition ships.txt'
NOTE = (1505, 1564, 1621)
TAB_RIGHE = [1504, 1505, 1564, 1621]
NAVI = ['Neutralizer', 'Punisher', 'Pursuer', 'Rover', 'Stalker', 'Briar', 'Spire', 'Thistle', 'Thorn',
        'Runabout', 'Sojourner', 'Traveler', 'Visitor', 'Skylance']
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
    rows.append((n, d if d else ('OK' if c else 'FAIL'), c))


ck('unita tradotte 17/17', len(cov) == 17 == len(units), '%d/%d' % (len(cov), len(units)))
ck('tutte e 17 sono DESCRIPTION',
   collections.Counter(u['kind'] for u in cov) == {'DESCRIPTION': 17})
ck('13 contesti: Pursuer 3, Rover 2, Stalker 2, dieci singoli',
   collections.Counter(u['context'] for u in cov) == {
       'ship:Heliarch Neutralizer': 1, 'ship:Heliarch Punisher': 1, 'ship:Heliarch Pursuer': 3,
       'ship:Heliarch Rover': 2, 'ship:Heliarch Stalker': 2, 'ship:Kimek Briar': 1,
       'ship:Kimek Spire': 1, 'ship:Kimek Thistle': 1, 'ship:Kimek Thorn': 1,
       'ship:Saryd Runabout': 1, 'ship:Saryd Sojourner': 1, 'ship:Saryd Traveler': 1,
       'ship:Saryd Visitor': 1},
   collections.Counter(u['context'] for u in cov))
ck('la nota del hyperdrive e IDENTICA nelle TRE unita (1505, 1564, 1621)',
   by[5]['italian'] == by[7]['italian'] == by[9]['italian']
   and by[5]['english'] == by[7]['english'] == by[9]['english'],
   (by[5]['italian'][:40], by[7]['italian'][:40], by[9]['italian'][:40]))
ck('e la 1504 (altra nota del Pursuer) e DIVERSA dalle tre',
   by[4]['italian'] != by[5]['italian'] and by[4]['english'] != by[5]['english'])
ck('la nota dice «baia di caccia» e «motore iperspaziale»',
   'baia di caccia' in by[5]['italian'] and 'motore iperspaziale' in by[5]['italian'])
ck('la seconda persona e SOLO nelle tre note (unica del file)',
   [u['line'] for u in cov if re.search(r'\b(puoi|tuo|tua|ti)\b', u['italian'])] == list(NOTE),
   [u['line'] for u in cov if re.search(r'\b(puoi|tuo|tua|ti)\b', u['italian'])])
ck('le quattro tab sono alle righe attese, come primo carattere',
   [u['line'] for u in cov if u['italian'].startswith(TAB)] == TAB_RIGHE,
   [u['line'] for u in cov if u['italian'].startswith(TAB)])
ck('nomi delle navi INVARIATI dove compaiono (incluse le armi rubate ai Quarg)',
   all(n in u['italian'] for u in cov for n in NAVI if n in u['english']),
   [(u['line'], n) for u in cov for n in NAVI if n in u['english'] and n not in u['italian']])
ck('`Coalition` resta «Coalizione» anche qui',
   'Coalition' not in ''.join(u['italian'] for u in cov)
   and 'Coalizione' in by[11]['italian'] and 'Coalition' in by[11]['english'])
ck('i tre popoli: Kimek, Saryd, Arachi, Heliarch',
   all(k in ''.join(u['italian'] for u in cov) for k in ('Kimek', 'Saryd', 'Arachi', 'Heliarch')))
ck('lo Spire: cabine per un Kimek, soffitti bassi per un Saryd, letti piccoli per un Arach',
   'cabine a cuccette' in by[11]['italian'] and 'soffitti' in by[11]['italian']
   and 'letti' in by[11]['italian'])
ck('il Visitor: lavoro diverso ogni settimana',
   'ogni settimana' in by[17]['italian'] and 'versatili' in by[17]['italian'])
ck('il Traveler: navi scientifiche e vita a bordo',
   'navi scientifiche' in by[16]['italian'] and 'mettere radici' in by[16]['italian'])
ck('VIRGOLETTE: zero · SEGNAPOSTO: nessuno · ALTERNATIVE: nessuna (asserzioni vuote)',
   sum(u['italian'].count(QUOTE) for u in cov) == 0
   and not TAG.findall(''.join(u['italian'] for u in cov))
   and sum(len(ALT.findall(u['italian'])) for u in cov) == 0)
ck('APICI: uno in inglese (1753), sette in italiano',
   [u['line'] for u in cov if u['english'].count(APOS)] == [1753]
   and sum(u['italian'].count(APOS) for u in cov) == 7,
   (sum(u['english'].count(APOS) for u in cov), sum(u['italian'].count(APOS) for u in cov)))
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in cov for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessun doppio spazio (la tab iniziale non conta)',
   not [u['idx'] for u in cov if '  ' in u['italian'].lstrip(TAB)])
ck('rapporto nel gate 0,55-1,90',
   all(0.55 < u['ratio'] < 1.90 for u in cov),
   [(u['idx'], u['ratio']) for u in cov if not 0.55 < u['ratio'] < 1.90])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck('FILE: 10 unita prima (L316, righe 59-969)',
   db.execute('select count(*) from units where path=? and line<1141', (PATH,)).fetchone()[0] == 10)
ck('FILE: ZERO unita dopo la 2195 — il lotto CHIUDE il file',
   db.execute('select count(*) from units where path=? and line>2195', (PATH,)).fetchone()[0] == 0)
ck('FILE: 27 unita (10 + 17), righe 59-2195',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (27, 59, 2195)
   and 10 + 17 == 27)
ck('FILE: copertura 27/27 — il file e tutto qui',
   db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0] == 27)
ck('tutte le 17 unita di questo lotto sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · 17 DESCRIPTION in 13 contesti · 4 tab · 0 virgolette · FILE 27/27' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
