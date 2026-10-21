r"""check.py — L313 (`data/bunrodea/bunrodea outfits.txt`, righe 250-402). **LOTTO TERMINALE**.

Nove `DESCRIPTION`, **un contesto per unita'**: il `Lasher Pistol` e le **otto unita' `Rift`** — quattro propulsori (`Chiisana`,
`Nami`, `Ookii`, `Subarashii`) e quattro timoni con gli **stessi quattro nomi giapponesi**.

Il test verifica:

1. **la scala dei nomi**: i quattro prefissi compaiono **due volte**, una per i propulsori e una per i timoni, e restano
   **invariati**;
2. **zero tab e zero virgolette**: asserzioni vuote, dichiarate;
3. **due apici inglesi** (327 `aren't`, 402 `Bunrodea's`), misurati per unita';
4. **il confronto con i Korath**, che e' il filo delle prime cinque unita';
5. **l'invariante di FILE**: 33 unita', prima 25, ultima 402, **zero dopo** — il lotto chiude il file.
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
PREFISSI = ['Chiisana', 'Nami', 'Ookii', 'Subarashii']
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


ck('unita tradotte 9/9', len(cov) == 9 == len(units), '%d/%d' % (len(cov), len(units)))
ck('tutte e 9 sono DESCRIPTION',
   collections.Counter(u['kind'] for u in cov) == {'DESCRIPTION': 9})
ck('nove contesti, UNO per unita (struttura piatta)',
   len({u['context'] for u in cov}) == 9
   and all(len([x for x in cov if x['context'] == u['context']]) == 1 for u in cov),
   collections.Counter(u['context'] for u in cov).most_common(3))
ck('i quattro prefissi giapponesi compaiono DUE volte: propulsori e timoni',
   collections.Counter(p for u in cov for p in PREFISSI if p in u['context']) ==
   {'Chiisana': 2, 'Nami': 2, 'Ookii': 2, 'Subarashii': 2},
   collections.Counter(p for u in cov for p in PREFISSI if p in u['context']))
ck('i nomi restano INVARIATI: `rift` non diventa «frattura», i prefissi giapponesi non sono tradotti',
   all('frattura' not in u['italian'] and 'spaccatura' not in u['italian'] for u in cov)
   and 'rift' in ''.join(u['italian'] for u in cov)
   and all(u['context'].startswith('outfit:') for u in cov))
ck('VIRGOLETTE: zero (asserzione vuota)',
   sum(u['italian'].count(QUOTE) for u in cov) == 0 == sum(u['english'].count(QUOTE) for u in cov))
ck('TAB: zero (asserzione vuota)',
   sum(u['italian'].count(TAB) for u in cov) == 0 == sum(u['english'].count(TAB) for u in cov))
ck('SEGNAPOSTO: nessuno (asserzione vuota)', not TAG.findall(''.join(u['italian'] for u in cov)))
ck('ALTERNATIVE: nessuna (asserzione vuota)', sum(len(ALT.findall(u['italian'])) for u in cov) == 0)
ck('APICI: due in inglese (327 `aren\'t`, 402 `Bunrodea\'s`), sei in italiano',
   sum(u['english'].count(APOS) for u in cov) == 2 and sum(u['italian'].count(APOS) for u in cov) == 6
   and by[5]['english'].count(APOS) == 1 and by[9]['english'].count(APOS) == 1,
   (sum(u['english'].count(APOS) for u in cov), sum(u['italian'].count(APOS) for u in cov)))
ck('il filo del lotto: il confronto con i KORATH nelle prime unita',
   sum(1 for u in cov if 'Korath' in u['italian']) >= 4,
   [u['idx'] for u in cov if 'Korath' in u['italian']])
ck('la pistola: abbordaggi, predoni, armi leggere, equipaggio',
   all(k in by[1]['italian'] for k in ('abbordate', 'predoni', 'armi leggere', 'equipaggio')))
ck('la scala dei propulsori: efficienza contro POTENZA BRUTA dei Korath',
   'potenza bruta' in by[2]['italian'] and 'efficienza' in by[2]['italian']
   and 'fabbisogno' in by[3]['italian'] and 'per unità di spinta' in by[4]['italian'])
ck('la voce della riserva antica: cometa e inseguimento',
   'riserva antica' in by[5]['italian'] and 'cometa' in by[5]['italian']
   and 'bersaglio' in by[5]['italian'])
ck('i timoni: velocita di VIRATA invece della velocita, cannoni frontali',
   'velocità di virata' in by[6]['italian'] and 'cannoni frontali' in by[6]['italian'])
ck('il calore: pochissimo, e niente raffreddamento',
   'pochissimo calore' in by[7]['italian'] and 'raffreddamento' in by[7]['italian'])
ck('la cannocchiera finale: i cannoni puntati sul bersaglio',
   'cannoniere' in by[9]['italian'] and 'malcapitato bersaglio' in by[9]['italian'])
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in cov for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessun doppio spazio', not [u['idx'] for u in cov if '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90',
   all(0.55 < u['ratio'] < 1.90 for u in cov),
   [(u['idx'], u['ratio']) for u in cov if not 0.55 < u['ratio'] < 1.90])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck('FILE: 24 unita prima (L311 + L312)',
   db.execute('select count(*) from units where path=? and line<250', (PATH,)).fetchone()[0] == 24)
ck('FILE: ZERO unita dopo la 402 — il lotto CHIUDE il file',
   db.execute('select count(*) from units where path=? and line>402', (PATH,)).fetchone()[0] == 0)
ck('FILE: 33 unita (12 + 12 + 9), righe 25-402',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (33, 25, 402)
   and 12 + 12 + 9 == 33)
ck('FILE: copertura 33/33 — il file e tutto qui',
   db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0] == 33)
ck('tutte le 9 unita di questo lotto sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · 9 DESCRIPTION, 9 contesti, 0 tab, 0 virgolette · FILE 33/33' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
