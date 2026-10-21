r"""check.py — L316 (`data/coalition/coalition ships.txt`, righe 59-969). **Primo lotto** del file.

Dieci `DESCRIPTION` in **nove contesti**: cinque navi **Arach** (`Courier`, `Freighter`, `Hulk`, `Spindle`, `Transport`) e cinque
**Heliarch** (`Breacher`, `Hunter`, `Interdictor`, `Judicator` ×2).

Il test difende **tre cose che il contratto ha dichiarato**:

1. **la riga 275 e' il `Arach Spindle` ma parla del `Hulk`**: la relazione e' fra **contesti**, non dentro il testo — e il test la
   verifica leggendo il contesto dell'unita' che cita il `Hulk` (la 200) e quello che lo descrive (la 275);
2. **il `Judicator` ha DUE unita'** (968 scheda + 969 nota con tab) e **entrambe stanno dentro** il lotto: nessuna nave spezzata;
3. **una sola tab**, riga 969, come **primo carattere**.

Poi: 9 contesti su 10 unita', 0 virgolette, 0 segnaposto, 0 alternative, 2 apici inglesi (461, 968), nomi invariati e
`Coalition` → **«Coalizione»** (corpus: 291 contro 3).
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
NAVI = ['Arach Courier', 'Arach Freighter', 'Arach Hulk', 'Arach Spindle', 'Arach Transport',
        'Breacher', 'Hunter', 'Interdictor', 'Judicator']
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


ck('unita tradotte 10/10', len(cov) == 10 == len(units), '%d/%d' % (len(cov), len(units)))
ck('tutte e 10 sono DESCRIPTION',
   collections.Counter(u['kind'] for u in cov) == {'DESCRIPTION': 10})
ck('nove contesti: cinque navi Arach + quattro Heliarch, con il Judicator doppio',
   collections.Counter(u['context'] for u in cov) == {
       'ship:Arach Courier': 1, 'ship:Arach Freighter': 1, 'ship:Arach Hulk': 1,
       'ship:Arach Spindle': 1, 'ship:Arach Transport': 1, 'ship:Heliarch Breacher': 1,
       'ship:Heliarch Hunter': 1, 'ship:Heliarch Interdictor': 1, 'ship:Heliarch Judicator': 2},
   collections.Counter(u['context'] for u in cov))
ck('il Judicator ha DUE unita (968 + 969) e sta tutto dentro il lotto',
   [u['line'] for u in cov if u['context'].endswith('Judicator')] == [968, 969])
ck('una sola tab: riga 969, come PRIMO carattere',
   [u['line'] for u in cov if u['italian'].startswith(TAB)] == [969]
   and at[969]['english'].startswith(TAB))
ck('la riga 275 e il contesto `Arach Spindle` ma parla del HULK',
   at[275]['context'].endswith('Arach Spindle') and 'Hulk' in at[275]['english']
   and at[275]['context'] != at[200]['context']
   and 'Spindle' in at[275]['italian'] and 'Hulk' in at[275]['italian'],
   (at[275]['context'], at[200]['context']))
ck('il Transport cita la Coalizione e i mondi ad anello dei Quarg',
   'Coalizione' in at[383]['italian'] and 'Quarg' in at[383]['italian']
   and 'mondi ad anello' in at[383]['italian'])
ck('`Coalition` -> «Coalizione» (corpus: 291 contro 3)',
   'Coalition' not in at[383]['italian'] and 'Coalition' in at[383]['english'])
ck('nomi delle navi INVARIATI dove compaiono',
   all(n in u['italian'] for u in cov for n in NAVI if n in u['english']),
   [(u['line'], n) for u in cov for n in NAVI if n in u['english'] and n not in u['italian']])
ck('il Hulk: pod laterali staccabili in pochi minuti',
   'pod laterali' in at[200]['italian'] and 'staccabili' in at[200]['italian'])
ck('lo Spindle: colossi goffi e pod tolti',
   'goffo' in at[275]['italian'] and 'pod laterali' in at[275]['italian'])
ck('il Breacher: velocita in avanti e volo radente',
   'velocità in avanti' in at[461]['italian'] and 'volo radente' in at[461]['italian'])
ck('l Interdictor: raggi attrattori e repulsori, aggancio iperspaziale',
   'attrattori' in at[779]['italian'] and 'repulsori' in at[779]['italian']
   and 'aggancio iperspaziale' in at[779]['italian'])
ck('il Judicator: sei baie di caccia, cuccette, nave logistica',
   'sei baie di caccia' in at[969]['italian'] and 'cuccette' in at[969]['italian']
   and 'nave logistica' in at[969]['italian'])
ck('VIRGOLETTE: zero · SEGNAPOSTO: nessuno · ALTERNATIVE: nessuna (asserzioni vuote)',
   sum(u['italian'].count(QUOTE) for u in cov) == 0
   and not TAG.findall(''.join(u['italian'] for u in cov))
   and sum(len(ALT.findall(u['italian'])) for u in cov) == 0)
ck('APICI: due in inglese (461, 968), nove in italiano',
   [u['line'] for u in cov if u['english'].count(APOS)] == [461, 968]
   and sum(u['italian'].count(APOS) for u in cov) == 9,
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
ck("SEGMENTO: zero unita' prima della 59 — il lotto APRE il file",
   db.execute('select count(*) from units where path=? and line<59', (PATH,)).fetchone()[0] == 0)
ck("SEGMENTO: 17 unita' dopo la 969 (la prossima alla 1141)",
   db.execute('select count(*) from units where path=? and line>969', (PATH,)).fetchone()[0] == 17
   and db.execute('select min(line) from units where path=? and line>969', (PATH,)).fetchone()[0] == 1141)
ck('FILE: 10 unita qui su 27 del file',
   db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0] == 27)
ck('tutte le 10 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · 10 DESCRIPTION in 9 contesti · 1 tab · 0 virgolette' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
