r"""check.py — L310 (`data/korath/korath culture conversations.txt`, righe 26-75). **LOTTO TERMINALE, FILE INTERO**.

Ventisette unita' che sono **tutto il file**: **24 `MISSION_TEXT`** da tradurre e **3 `UI_LABEL`** da copiare, in **un solo
contesto** (`mission:Korath Far'en Lai Prayer`).

Il test verifica:

1. **`UI_LABEL` copiati** (`small credits`, `medium credits`, `large credits`): sono le etichette dei pulsanti di scelta;
2. **le 14 virgolette** in **6 unita'** (33: 2, 35: 2, 37: 2, 39: 2, 40: **4**, 56: 2) e **per unita'**;
3. **i 3 segnaposto** (`<origin>` ×2, `<home planet>` ×1) **identici**;
4. **23 tab**: tutte le `MISSION_TEXT` tranne la **26**, nessuna `UI_LABEL`;
5. **la seconda persona E' il registro** del racconto («ti avvicini», «il tuo intento»): il test verifica che **ci sia**, invece
   di vietarla;
6. **i numeri delle offerte** in forma italiana (`10.000`, `10.000.000`) e le **scelte fra parentesi** conservate.
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
PATH = 'data/korath/korath culture conversations.txt'
CONTEXT = "mission:Korath Far'en Lai Prayer"
UI = {21: 'small credits', 23: 'medium credits', 25: 'large credits'}
QUOTED = {8: 2, 9: 2, 11: 2, 12: 2, 13: 4, 19: 2}
OFFERTE = {15: '100 crediti', 16: '10.000 crediti', 17: '10.000.000 crediti', 18: 'una fotografia'}
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
ck('unita tradotte 27/27', len(cov) == 27 == len(units), '%d/%d' % (len(cov), len(units)))
ck('24 MISSION_TEXT + 3 UI_LABEL', kinds == {'MISSION_TEXT': 24, 'UI_LABEL': 3}, dict(kinds))
ck('UN SOLO contesto per tutto il file',
   {u['context'] for u in cov} == {CONTEXT}, {u['context'] for u in cov})
ck('UI_LABEL copiati: `small/medium/large credits`',
   all(by[i]['italian'] == v == by[i]['english'] for i, v in UI.items()),
   {i: by[i]['italian'] for i in UI})
ck('le 14 virgolette sono in 6 unita, nella quantita giusta per unita',
   sum(u['italian'].count(QUOTE) for u in cov) == 14
   and {i: by[i]['italian'].count(QUOTE) for i in QUOTED} == QUOTED,
   {i: by[i]['italian'].count(QUOTE) for i in QUOTED})
ck('i 3 segnaposto sono IDENTICI (`<origin>` x2, `<home planet>` x1)',
   collections.Counter(TAG.findall(''.join(u['italian'] for u in cov)))
   == collections.Counter(TAG.findall(''.join(u['english'] for u in cov)))
   == {'<origin>': 2, '<home planet>': 1})
ck('23 tab: tutte le MISSION_TEXT tranne la 26, nessuna UI_LABEL',
   sum(u['italian'].count(TAB) for u in cov) == 23
   and not [u['idx'] for u in cov if u['kind'] == 'UI_LABEL' and u['italian'].startswith(TAB)]
   and not at[26]['italian'].startswith(TAB)
   and all(at[u['line']]['italian'].startswith(TAB) for u in cov
           if u['kind'] == 'MISSION_TEXT' and u['line'] != 26))
_tp = [u['idx'] for u in cov if u['kind'] == 'MISSION_TEXT'
       and re.search(r'\b(tu|tuo|tua|tuoi|tue|ti|te)\b', u['italian'])]
ck('la SECONDA PERSONA e il registro narrante: pronomi in almeno 10 unita, verbi ovunque',
   len(_tp) >= 10 and 'ti serve' in by[1]['italian'] and 'noti' in by[2]['italian']
   and 'Ti ricordi' in by[20]['italian'],
   len(_tp))
ck('le quattro scelte di offerta conservano parentesi e valori italiani',
   all(v in by[i]['italian'] and by[i]['italian'].lstrip(TAB).startswith('(') for i, v in OFFERTE.items()),
   {i: by[i]['italian'] for i in OFFERTE})
ck('il nome della missione e del pianeta restano INVARIATI',
   "Far'en Lai" in ''.join(u['italian'] for u in cov)
   and 'Korath' in ''.join(u['italian'] for u in cov)
   and 'humani efreti' in at[33]['italian'])
ck('le 24 MISSION_TEXT sono tutte TRADOTTE',
   all(u['italian'] != u['english'] for u in cov if u['kind'] == 'MISSION_TEXT'))
ck('ALTERNATIVE: zero (asserzione vuota)',
   sum(len(ALT.findall(u['italian'])) for u in cov) == 0)
ck('APICI: dieci in inglese, dodici in italiano',
   sum(u['english'].count(APOS) for u in cov) == 10 and sum(u['italian'].count(APOS) for u in cov) == 12,
   (sum(u['english'].count(APOS) for u in cov), sum(u['italian'].count(APOS) for u in cov)))
ck('lessico della scena: santuario, offerte, pastelli, candela, spazioporto',
   'santuario' in by[3]['italian'] and 'offerte' in by[14]['italian']
   and 'pastelli' in by[2]['italian'] and 'candela' in by[6]['italian']
   and 'spazioporto' in by[1]['italian'])
ck('nessun caporale, nessun carattere tipografico',
   not [u['idx'] for u in cov for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026' if c in u['italian']])
nonlat = [(u['idx'], c) for u in cov for c in u['italian'] if ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessun doppio spazio (la tab iniziale non conta)',
   not [u['idx'] for u in cov if '  ' in u['italian'].lstrip(TAB)])
ck('rapporto nel gate 0,55-1,90',
   all(0.55 < u['ratio'] < 1.90 for u in cov),
   [(u['idx'], u['ratio']) for u in cov if not 0.55 < u['ratio'] < 1.90])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("FILE: ZERO unita' prima della 26 — il lotto APRE il file",
   db.execute('select count(*) from units where path=? and line<26', (PATH,)).fetchone()[0] == 0)
ck("FILE: ZERO unita' dopo la 75 — il lotto CHIUDE il file",
   db.execute('select count(*) from units where path=? and line>75', (PATH,)).fetchone()[0] == 0)
ck('FILE: 27 unita (24 MISSION_TEXT + 3 UI_LABEL), righe 26-75',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (27, 26, 75)
   and dict(db.execute('select kind,count(*) from units where path=? group by kind', (PATH,)).fetchall())
   == {'MISSION_TEXT': 24, 'UI_LABEL': 3})
ck('FILE: copertura 27/27 (il file e tutto qui)',
   db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0] == 27)
ck('tutte le 27 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · 24 MISSION_TEXT + 3 UI_LABEL · 23 tab · 14 virgolette · FILE 27/27' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
