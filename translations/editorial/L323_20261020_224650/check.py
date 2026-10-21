r"""check.py — L323 (`data/rulei/rulei.txt`, righe 38-157). **LOTTO TERMINALE, FILE INTERO**.

Quarantuno unita' in **cinque contesti** e **due tipi**, di cui uno nuovo:

| tipo | unita' | registro |
|---|---|---|
| `MISSION_TEXT` | 38 | **seconda persona** (il giocatore) |
| **`LOGBOOK`** | **3** (38, 116, 151) | **prima persona**, diario: «I Rulei **erano**…», «**Scoperta** una regione…» |

Il test difende:

1. **i due registri**: i `LOGBOOK` **non** usano la seconda persona, i `MISSION_TEXT` **si'**;
2. **le 32 tab** con le **nove righe senza** (38, 39, 41, 93, 116, 118, 132, 151, 153): motivo **misto**, verificato **per riga**;
3. **l'indentazione a scala** delle righe 95 / 98 / 99: **11, 21, 23 tab**, cioe' il testo che «scivola» verso il basso mentre la
   mente viene trascinata — i **numeri esatti** sono parte della resa;
4. **le 34 virgolette** in **16 unita'**, con la **151 che ne ha quattro**;
5. **i 12 apici inglesi** in **7 unita'** (6: 3, 32: 2, 40: 3);
6. **zero segnaposto**: asserzione vuota, dichiarata.

E l'invariante di **FILE**: 41 unita', prima 38, ultima 157, zero prima e dopo.
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
PATH = 'data/rulei/rulei.txt'
SENZA_TAB = [38, 39, 41, 93, 116, 118, 132, 151, 153]
SCALA = {95: 11, 98: 21, 99: 23}
VIRG = {47: 2, 48: 2, 49: 2, 51: 2, 54: 2, 55: 2, 58: 2, 60: 2, 61: 2, 64: 2, 66: 2, 67: 2,
        132: 2, 151: 4, 154: 2, 155: 2}
APICI_EN = {45: 3, 69: 1, 95: 1, 103: 2, 118: 1, 132: 1, 156: 3}
SECONDA = re.compile(r'\b(ti|tu|te|tuo|tua|tuoi|tue)\b', re.I)
PRIMA = re.compile(r'\b(io|noi|mio|nostro|scoperta|scoprimmo|notammo)\b', re.I)
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


ck('unita tradotte 41/41', len(cov) == 41 == len(units), '%d/%d' % (len(cov), len(units)))
ck('38 MISSION_TEXT + 3 LOGBOOK',
   collections.Counter(u['kind'] for u in cov) == {'MISSION_TEXT': 38, 'LOGBOOK': 3},
   dict(collections.Counter(u['kind'] for u in cov)))
ck('cinque contesti con cardinalita 24 / 8 / 6 / 2 / 1',
   sorted(collections.Counter(u['context'] for u in cov).values(), reverse=True) == [24, 8, 6, 2, 1],
   collections.Counter(u['context'] for u in cov))
ck('i tre LOGBOOK sono diario di bordo: NESSUN «tu», e il 116 in prima persona implicita',
   [u['line'] for u in cov if u['kind'] == 'LOGBOOK'] == [38, 116, 151]
   and not [u['line'] for u in cov if u['kind'] == 'LOGBOOK' and SECONDA.search(u['italian'])]
   and 'Scoperta una regione' in at[116]['italian']
   and at[38]['italian'].startswith('I Rulei') and at[151]['italian'].startswith('I Rulei'),
   [at[l]['italian'][:40] for l in (38, 116, 151)])
ck('la seconda persona e il registro dei MISSION_TEXT',
   sum(1 for u in cov if u['kind'] == 'MISSION_TEXT' and SECONDA.search(u['italian'])) >= 12,
   sum(1 for u in cov if u['kind'] == 'MISSION_TEXT' and SECONDA.search(u['italian'])))
ck('32 unita con la tab, e le nove senza sono quelle attese',
   [u['line'] for u in cov if u['italian'].startswith(TAB)]
   == [l for l in sorted(at) if l not in SENZA_TAB],
   [u['line'] for u in cov if u['italian'].startswith(TAB)][:5])
ck("l'indentazione a SCALA: 11 tab (95), 21 tab (98), 23 tab (99)",
   {l: len(at[l]['italian']) - len(at[l]['italian'].lstrip(TAB)) for l in SCALA} == SCALA
   and {l: len(at[l]['english']) - len(at[l]['english'].lstrip(TAB)) for l in SCALA} == SCALA,
   {l: len(at[l]['italian']) - len(at[l]['italian'].lstrip(TAB)) for l in SCALA})
ck('le 34 virgolette sono in 16 unita, con la 151 che ne ha QUATTRO',
   {u['line']: u['italian'].count(QUOTE) for u in cov if u['italian'].count(QUOTE)} == VIRG
   and sum(u['italian'].count(QUOTE) for u in cov) == 34,
   {u['line']: u['italian'].count(QUOTE) for u in cov if u['italian'].count(QUOTE)})
ck('i 12 apici inglesi sono distribuiti per unita (6: 3, 32: 2, 40: 3)',
   {u['line']: u['english'].count(APOS) for u in cov if u['english'].count(APOS)} == APICI_EN
   and sum(u['english'].count(APOS) for u in cov) == 12,
   {u['line']: u['english'].count(APOS) for u in cov if u['english'].count(APOS)})
ck('SEGNAPOSTO: nessuno (asserzione vuota)', not TAG.findall(''.join(u['italian'] for u in cov)))
ck('ALTERNATIVE: nessuna (asserzione vuota)', sum(len(ALT.findall(u['italian'])) for u in cov) == 0)
ck('il filo dei sussurri: le battute fra virgolette sono 14',
   sum(1 for u in cov if u['italian'].lstrip(TAB).startswith('"')) == 14,
   [(u['line'], u['italian'].lstrip(TAB)[:22]) for u in cov if u['italian'].lstrip(TAB).startswith('"')])
ck('le due parole chiave dei Rulei: «Precursori» e «Una Fine» restano riconoscibili',
   'Precursori' in at[58]['italian'] and 'Una Fine' in at[64]['italian'])
ck('`Umbral Reach` resta invariato: stesso numero di occorrenze delle due lingue',
   sum(u['italian'].count('Umbral Reach') for u in cov) ==
   sum(u['english'].count('Umbral Reach') for u in cov) == 2,
   (sum(u['italian'].count('Umbral Reach') for u in cov),
    sum(u['english'].count('Umbral Reach') for u in cov)))
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in cov for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessun doppio spazio (la tab iniziale non conta)',
   not [u['idx'] for u in cov if '  ' in u['italian'].lstrip(TAB)])
ck('rapporto nel gate 0,55-1,90',
   all(0.55 < u['ratio'] < 1.90 for u in cov),
   [(u['idx'], u['ratio']) for u in cov if not 0.55 < u['ratio'] < 1.90])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("FILE: ZERO unita' prima della 38 — il lotto APRE il file",
   db.execute('select count(*) from units where path=? and line<38', (PATH,)).fetchone()[0] == 0)
ck("FILE: ZERO unita' dopo la 157 — il lotto CHIUDE il file",
   db.execute('select count(*) from units where path=? and line>157', (PATH,)).fetchone()[0] == 0)
ck('FILE: 41 unita, righe 38-157, 38 MISSION_TEXT + 3 LOGBOOK',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (41, 38, 157)
   and dict(db.execute('select kind,count(*) from units where path=? group by kind', (PATH,)).fetchall())
   == {'MISSION_TEXT': 38, 'LOGBOOK': 3})
ck('FILE: copertura 41/41 — il file e tutto qui',
   db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0] == 41)
ck('tutte le 41 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · 38 MISSION_TEXT + 3 LOGBOOK in 5 contesti · 32 tab · 34 virgolette · FILE 41/41' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
