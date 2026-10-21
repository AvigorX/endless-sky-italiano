r"""check.py — L314 (`data/drak/drak culture conversations.txt`, righe 26-79). **Primo lotto** del file.

Sedici `MISSION_TEXT` in **tre contesti** — tre **visioni**:

| contesto | righe | unita' | la prima unita' |
|---|---|---|---|
| `Drak Revelations: Arachi` | 26-30 | 5 | **26, senza tab** |
| `Drak Revelations: Hai` | 43-47 | 5 | **43, senza tab** |
| `Drak Revelations: Humanity` | 74-79 | 6 | **74, senza tab** |

Il test verifica:

1. **i tre blocchi**: la **prima** unita' di ognuno **non** ha la tab, tutte le altre **si'** (13 tab in tutto);
2. **i 4 segnaposto** (`<ship>` ×3, `<origin>` ×1) **identici**, con il **conteggio per tipo**;
3. **le 2 virgolette**: **una coppia**, nella sola riga 44 (`"islands"` -> «"isole"»);
4. **gli apici**: 6 in inglese (26, 27, 30, 43, 75, 77), misurati **per unita'**;
5. **la seconda persona** come voce narrante della visione: il test pretende che **ci sia**;
6. **lo svelamento**: le tre visioni finiscono con il **ritorno alla realta'** (dall'atmosfera, la pozzanghera normale, il letto).
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
PATH = 'data/drak/drak culture conversations.txt'
BLOCCHI = {26: 30, 43: 47, 74: 79}
PRIME = (26, 43, 74)
APICI_EN = {1: 1, 2: 1, 5: 1, 6: 1, 12: 1, 14: 1}
TOKEN = {'<ship>': 3, '<origin>': 1}
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
ck('TRE contesti: 5 + 5 + 6 unita',
   collections.Counter(u['context'] for u in cov) == {
       'mission:Drak Revelations: Arachi': 5, 'mission:Drak Revelations: Hai': 5,
       'mission:Drak Revelations: Humanity': 6},
   collections.Counter(u['context'] for u in cov))
ck('le PRIME unita dei tre blocchi (26, 43, 74) NON hanno la tab',
   not [l for l in PRIME if at[l]['italian'].startswith(TAB)]
   and not [l for l in PRIME if at[l]['english'].startswith(TAB)])
ck('le altre 13 unita HANNO la tab come primo carattere',
   [u['line'] for u in cov if u['italian'].startswith(TAB)] ==
   [27, 28, 29, 30, 44, 45, 46, 47, 75, 76, 77, 78, 79],
   [u['line'] for u in cov if u['italian'].startswith(TAB)])
ck('i 4 segnaposto sono IDENTICI e con lo stesso conteggio per tipo',
   collections.Counter(TAG.findall(''.join(u['italian'] for u in cov))) == TOKEN
   == collections.Counter(TAG.findall(''.join(u['english'] for u in cov))),
   dict(collections.Counter(TAG.findall(''.join(u['italian'] for u in cov)))))
ck('le 2 virgolette sono UNA coppia nella sola riga 44',
   by[7]['italian'].count(QUOTE) == 2
   and sum(u['italian'].count(QUOTE) for u in cov) == 2,
   {u['line']: u['italian'].count(QUOTE) for u in cov if u['italian'].count(QUOTE)})
ck('gli apici inglesi sono 6, uno in ciascuna delle unita attese',
   {i: by[i]['english'].count(APOS) for i in APICI_EN} == APICI_EN
   and sum(u['english'].count(APOS) for u in cov) == 6,
   {i: by[i]['english'].count(APOS) for i in APICI_EN})
SECONDA = re.compile(r'\b(ti|tu|tuo|tua|tuoi|tue|te|riesci|vedi|scendi|batti|riapri|noti|guardi|'
                     r'ritrovi|assopisco|sorprendi)\b')
_per_blocco = collections.Counter(u['context'] for u in cov if SECONDA.search(u['italian']))
ck('la SECONDA PERSONA e la voce narrante: almeno tre unita per blocco, dodici in tutto',
   all(_per_blocco[c] >= 3 for c in {u['context'] for u in cov}) and sum(_per_blocco.values()) >= 12
   and 'Scendi' in at[43]['italian'] and 'ti ritiri' in at[74]['italian'],
   dict(_per_blocco))
ck('il primo svelamento: fuori dalla nave, SOTTOTERRA (riga 26)',
   'fuori dalla nave' in at[26]['italian'] and 'sottoterra' in at[26]['italian'])
ck('il secondo: la pozzanghera torna NORMALE (riga 47)',
   'normale' in at[47]['italian'] and 'pozzanghera' in at[47]['italian'])
ck('il terzo: il risveglio NEL LETTO (riga 79)',
   'letto' in at[79]['italian'] and 'sdraiato' in at[79]['italian'])
ck('le immagini della visione Humanity: culla, masso, fiamme, entita senza forma',
   all(k in ''.join(u['italian'] for u in cov if u['context'].endswith('Humanity'))
       for k in ('culla', 'masso', 'fiamme', 'entità senza forma')))
ck('la batosta su Hai: onde che inghiottono navi e isole',
   'inghiottono' in at[45]['italian'] and 'arcipelago' in at[45]['italian'])
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
ck("SEGMENTO: zero unita' prima della 26 — il lotto APRE il file",
   db.execute('select count(*) from units where path=? and line<26', (PATH,)).fetchone()[0] == 0)
ck("SEGMENTO: 16 unita' dopo la 79 (la prossima alla 93)",
   db.execute('select count(*) from units where path=? and line>79', (PATH,)).fetchone()[0] == 16
   and db.execute('select min(line) from units where path=? and line>79', (PATH,)).fetchone()[0] == 93)
ck('FILE: 16 unita qui su 32 del file',
   db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0] == 32)
ck('tutte le 16 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · 16 MISSION_TEXT in 3 contesti · 13 tab · 2 virgolette · 4 segnaposto' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
