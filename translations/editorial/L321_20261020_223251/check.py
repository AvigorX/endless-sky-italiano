r"""check.py — L321 (`data/wanderer/wanderer outfits.txt`, righe 463-659). **LOTTO TERMINALE**.

Tredici `DESCRIPTION`, **un contesto per unita'**, in **due blocchi**:

| righe | blocco |
|---|---|
| 463-638 | **motori e radiatori**: `Ramscoop`, `Heat Sink`, **due scale di quattro** (`Type 1..4 Radiant Thruster`, `Type 1..4 Radiant Steering`) |
| 645-659 | **tre licenze**: `Outfits`, `Wanderer`, `Military` |

Il test difende:

1. **i numeri delle scale** `Type 1 → Type 4`, sia per i propulsori sia per i timoni: non «piccolo/medio/grande/massimo»;
2. **le tre licenze sono OGGETTI** (un piatto con semi, un ramo in ambra, un ramo in bronzo), non autorizzazioni astratte;
3. **la seconda persona e' solo nelle schede dei motori** («la tua nave»), e va **elencata**;
4. **tre apici inglesi su due unita'** (645 x1, 652 x2);
5. **zero tab, zero virgolette, zero segnaposto**: asserzioni vuote, dichiarate.

E l'invariante di **FILE**: 31 unita', somma lotti **18 + 13**, prima riga **40**, ultima **659**, **zero dopo**.
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
PATH = 'data/wanderer/wanderer outfits.txt'
NOMI = ['Ramscoop', 'Heat Sink', 'Type 1 Radiant', 'Type 2 Radiant', 'Type 3 Radiant', 'Type 4 Radiant',
        'Sentinel Skirtgrass', 'Noble Watchwood', 'Wanderer']
SECONDA = [498, 558, 598, 618]
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


ck('unita tradotte 13/13', len(cov) == 13 == len(units), '%d/%d' % (len(cov), len(units)))
ck('tutte e 13 sono DESCRIPTION',
   collections.Counter(u['kind'] for u in cov) == {'DESCRIPTION': 13})
ck('13 contesti, UNO per unita (struttura piatta)',
   len({u['context'] for u in cov}) == 13
   and all(n == 1 for n in collections.Counter(u['context'] for u in cov).values()))
ck('due scale di quattro con i NUMERI conservati (Thruster e Steering)',
   [u['context'] for u in cov if 'Thruster' in u['context']] ==
   ['outfit:Type %d Radiant Thruster' % i for i in (1, 2, 3, 4)]
   and [u['context'] for u in cov if 'Steering' in u['context']] ==
   ['outfit:Type %d Radiant Steering' % i for i in (1, 2, 3, 4)]
   and all(re.search(r'Type \d', u['context']) for u in cov if 'Radiant' in u['context']))
ck('la scala CRESCE: il Type 1 e «il più piccolo», il Type 4 «il più grande»',
   'più piccolo motore' in at[498]['italian'] and 'più grande motore' in at[558]['italian']
   and 'più grande sistema di timone' in at[638]['italian'])
ck('le tre licenze sono OGGETTI: piatto con semi, ramo in ambra, ramo in bronzo',
   'piatto di forma bizzarra' in at[645]['italian']
   and "guscio d'ambra" in at[652]['italian']
   and 'stampo di bronzo' in at[659]['italian'])
ck('le tre licenze concedono tre cose DIVERSE',
   'equipaggiamenti Wanderer' in at[645]['italian']
   and 'navi Wanderer non militari' in at[652]['italian']
   and 'più grandi navi da guerra' in at[659]['italian'])
ck('la seconda persona e SOLO nelle schede dei motori («la tua nave»)',
   [u['line'] for u in cov if 'tua nave' in u['italian']] == SECONDA,
   [u['line'] for u in cov if 'tua nave' in u['italian']])
ck('il calore e il filo dei motori: irradiare, trasferire, espellere',
   'irradiando il calore' in at[498]['italian'] and 'plasma di scarico' in at[518]['italian']
   and 'espellere il calore in eccesso' in at[538]['italian'])
ck('i timoni citano i droni senza pilota e le navi di medie dimensioni',
   'senza pilota' in at[578]['italian'] and 'medie dimensioni' in at[618]['italian'])
ck('VIRGOLETTE: zero · TAB: zero · SEGNAPOSTO: nessuno · ALTERNATIVE: nessuna (asserzioni vuote)',
   sum(u['italian'].count(QUOTE) for u in cov) == 0
   and sum(u['italian'].count(TAB) for u in cov) == 0
   and not TAG.findall(''.join(u['italian'] for u in cov))
   and sum(len(ALT.findall(u['italian'])) for u in cov) == 0)
ck('APICI: tre caratteri in inglese su DUE unita (645 x1, 652 x2)',
   [(u['line'], u['english'].count(APOS)) for u in cov if u['english'].count(APOS)]
   == [(645, 1), (652, 2)],
   [(u['line'], u['english'].count(APOS)) for u in cov if u['english'].count(APOS)])
ck('nomi INVARIATI dove compaiono (motori, specie, albero)',
   all(n in u['italian'] for u in cov for n in NOMI if n in u['english']),
   [(u['line'], n) for u in cov for n in NOMI if n in u['english'] and n not in u['italian']])
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in cov for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessun doppio spazio', not [u['idx'] for u in cov if '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90',
   all(0.55 < u['ratio'] < 1.90 for u in cov),
   [(u['idx'], u['ratio']) for u in cov if not 0.55 < u['ratio'] < 1.90])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck('FILE: 18 unita prima (L320, righe 40-450)',
   db.execute('select count(*) from units where path=? and line<463', (PATH,)).fetchone()[0] == 18)
ck('FILE: ZERO unita dopo la 659 — il lotto CHIUDE il file',
   db.execute('select count(*) from units where path=? and line>659', (PATH,)).fetchone()[0] == 0)
ck('FILE: 31 unita (18 + 13), righe 40-659',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (31, 40, 659)
   and 18 + 13 == 31)
ck('FILE: copertura 31/31 — il file e tutto qui',
   db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0] == 31)
ck('tutte le 13 unita di questo lotto sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · 13 DESCRIPTION, 13 contesti, 0 tab, 0 virgolette · FILE 31/31' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
