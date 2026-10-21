r"""check.py — L315 (`data/drak/drak culture conversations.txt`, righe 93-138). **LOTTO TERMINALE**.

Sedici `MISSION_TEXT` in **tre contesti**, con la **stessa struttura di L314** — la **prima** unita' di ogni blocco **senza tab**,
le altre tredici **con**:

| contesto | righe | unita' | la prima |
|---|---|---|---|
| `Drak Revelations: Korath` | 93-98 | 6 | **93, senza tab** |
| `Drak Revelations: Quarg` | 116-120 | 5 | **116, senza tab** |
| `Drak Revelations: Saryds` | 134-138 | 5 | **134, senza tab** |

Rispetto a L314 cambiano **due** cose che il test deve vedere:
- **zero virgolette** (L314 ne aveva una coppia);
- i segnaposto hanno il conteggio **invertito**: `<origin>` ×2 e `<ship>` ×2 (in L314 era `<ship>` ×3, `<origin>` ×1).

E il lotto **chiude il file**: invariante di **FILE**, 32 unita', somma **16 + 16**.
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
SECONDA = re.compile(r'\b(ti|tu|tuo|tua|tuoi|tue|te|hai|vedi|riesci|riapri|apri|trovi|alzi|ritrovi|'
                     r'batti|senti|guardi)\b', re.I)
HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
PATH = 'data/drak/drak culture conversations.txt'
PRIME = (93, 116, 134)
TAB_RIGHE = [94, 95, 96, 97, 98, 117, 118, 119, 120, 135, 136, 137, 138]
APICI_EN = {11: 1, 12: 1, 16: 1}
TOKEN = {'<origin>': 2, '<ship>': 2}
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


ck('unita tradotte 16/16', len(cov) == 16 == len(units), '%d/%d' % (len(cov), len(units)))
ck('tutte e 16 sono MISSION_TEXT',
   collections.Counter(u['kind'] for u in cov) == {'MISSION_TEXT': 16})
ck('tre contesti: 6 + 5 + 5',
   collections.Counter(u['context'] for u in cov) == {
       'mission:Drak Revelations: Korath': 6, 'mission:Drak Revelations: Quarg': 5,
       'mission:Drak Revelations: Saryds': 5},
   collections.Counter(u['context'] for u in cov))
ck('le PRIME unita dei tre blocchi (93, 116, 134) NON hanno la tab',
   not [l for l in PRIME if at[l]['italian'].startswith(TAB)]
   and not [l for l in PRIME if at[l]['english'].startswith(TAB)])
ck('le altre 13 unita hanno la tab come PRIMO carattere, alle righe attese',
   [u['line'] for u in cov if u['italian'].startswith(TAB)] == TAB_RIGHE,
   [u['line'] for u in cov if u['italian'].startswith(TAB)])
ck('i 4 segnaposto sono IDENTICI, con il conteggio INVERTITO rispetto a L314',
   collections.Counter(TAG.findall(''.join(u['italian'] for u in cov))) == TOKEN
   == collections.Counter(TAG.findall(''.join(u['english'] for u in cov))),
   dict(collections.Counter(TAG.findall(''.join(u['italian'] for u in cov)))))
ck('VIRGOLETTE: zero in tutte e 16 (asserzione vuota)',
   sum(u['italian'].count(QUOTE) for u in cov) == 0 == sum(u['english'].count(QUOTE) for u in cov))
ck('gli apici inglesi sono 3, uno in ciascuna delle unita attese',
   {i: by[i]['english'].count(APOS) for i in APICI_EN} == APICI_EN
   and sum(u['english'].count(APOS) for u in cov) == 3,
   {i: by[i]['english'].count(APOS) for i in APICI_EN})
_per = collections.Counter(u['context'] for u in cov if SECONDA.search(u['italian']))
ck('la SECONDA PERSONA e la voce narrante: almeno tre unita per blocco, nove in tutto',
   all(_per[c] >= 3 for c in {u['context'] for u in cov}) and sum(_per.values()) >= 9, dict(_per))
ck('i tre svelamenti: abitacolo della <ship>, luci della nave, porta dell abitacolo',
   'abitacolo della <ship>' in at[98]['italian']
   and 'luci della nave' in at[120]['italian']
   and 'porta del tuo abitacolo' in at[138]['italian'])
ck('Korath: terra e ruggine, torri a cupola, bronzo, il crollo',
   all(k in ''.join(u['italian'] for u in cov if u['context'].endswith('Korath'))
       for k in ('terra e ruggine', 'torre a cupola', 'bronzo', 'crolla')))
ck('Quarg: nebbia, gigante scarno, le TOMBE, le onde',
   all(k in ''.join(u['italian'] for u in cov if u['context'].endswith('Quarg'))
       for k in ('nebbia', 'scarno', 'tombe', 'onde')))
ck('Saryds: radura, cervi d acciaio, argento, gabbie, fulmini',
   all(k in ''.join(u['italian'] for u in cov if u['context'].endswith('Saryds'))
       for k in ('radura', "cervi d'acciaio", 'argento', 'gabbie', 'fulmini')))
ck('la fine dei Saryds: cadaveri e gabbie in frantumi',
   'cadaveri' in at[137]['italian'] and 'gabbie in frantumi' in at[137]['italian'])
ck('ALTERNATIVE: nessuna (asserzione vuota)', sum(len(ALT.findall(u['italian'])) for u in cov) == 0)
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in cov for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessun doppio spazio (la tab iniziale non conta)',
   not [u['idx'] for u in cov if '  ' in u['italian'].lstrip(TAB)])
ck('rapporto nel gate 0,55-1,90',
   all(0.55 < u['ratio'] < 1.90 for u in cov),
   [(u['idx'], u['ratio']) for u in cov if not 0.55 < u['ratio'] < 1.90])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck('FILE: 16 unita prima (L314, righe 26-79)',
   db.execute('select count(*) from units where path=? and line<93', (PATH,)).fetchone()[0] == 16)
ck('FILE: ZERO unita dopo la 138 — il lotto CHIUDE il file',
   db.execute('select count(*) from units where path=? and line>138', (PATH,)).fetchone()[0] == 0)
ck('FILE: 32 unita (16 + 16), righe 26-138',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (32, 26, 138)
   and 16 + 16 == 32)
ck('FILE: copertura 32/32 — il file e tutto qui',
   db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0] == 32)
ck('tutte le 16 unita di questo lotto sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · 16 MISSION_TEXT in 3 contesti · 13 tab · 0 virgolette · FILE 32/32' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
