r"""check.py — L82 (data/successors/predecessors.txt, 15 unita', righe 201-400)

Secondo lotto sulle schede di navi: **4 contesti** in ordine di riga — `ship:Hasur, Vowsworn` (208),
`ship:Queru, Luminous Gaze` (220-307), `outfit:"Iasa," Lethal Word` (348), `outfit:"Kis," Lethal Wish`
(359-381).

Misure (decisione 119):
  - **10 unita' di dato** identiche: 2 `VALUE` (3 `Querun, Luminous Gazes`; 14 `"Kis," Lethal Wishes`) e
    8 `TEXT` (nomi di equipaggiamento);
  - **5 `DESCRIPTION` tradotte** (1, 2, 12, 13, 15): l'avvertimento dei costrutti, la scheda di Queru,
    quella di Iasa e quella di Kis;
  - **1 tab** (unita' 2), **8 virgolette**, **0 dispari**, **0 token**, **0 duplicati**;
  - tipi: 8 `TEXT` + 5 `DESCRIPTION` + 2 `VALUE`; 0 `MISSION_TEXT`/`UI_LABEL`/`LOGBOOK`/`DIALOG`/`CONVERSATION`.
"""

import collections
import json
import os
import re
import sqlite3
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
units = src['units']
tr = {}
parts = sorted(f for f in os.listdir(os.path.join(HERE, 'parts')) if f.endswith('.json'))
for p in parts:
    for k, v in json.load(open(os.path.join(HERE, 'parts', p), encoding='utf-8')).items():
        tr[int(k)] = v

DATA = {3, 4, 5, 6, 7, 8, 9, 10, 11, 14}
PROSE = {1, 2, 12, 13, 15}
en_count = collections.Counter(u['english'] for u in units)
DUP_GROUPS = {k: [u['idx'] for u in units if u['english'] == k] for k, v in en_count.items() if v > 1}

lo, hi = 1, len(units)
if '--range' in sys.argv:
    i = sys.argv.index('--range')
    lo, hi = int(sys.argv[i + 1]), int(sys.argv[i + 2])
sel = [u for u in units if lo <= u['idx'] <= hi]

out = {'block': src['block'], 'note': src['note'], 'units': []}
for u in units:
    if u['idx'] not in tr:
        continue
    it = '\t' * (len(u['english']) - len(u['english'].lstrip('\t'))) + tr[u['idx']]
    out['units'].append({"idx": u['idx'], "id": u['id'], "path": u['path'], "line": u['line'],
                         "kind": u['kind'], "context": u['context'], "english": u['english'],
                         "italian": it, "ratio": round(len(it) / max(1, len(u['english'])), 3)})
open(os.path.join(HERE, 'translation.json'), 'w', encoding='utf-8').write(
    json.dumps(out, ensure_ascii=False, indent=1))

by_idx = {v['idx']: v for v in out['units']}
cov = [by_idx[u['idx']] for u in sel if u['idx'] in by_idx]
allcov = [by_idx[u['idx']] for u in units if u['idx'] in by_idx]
TAGS = re.compile(r'<[^<>]+>')

rows = []
rows.append(('unita\' tradotte nell\'intervallo', '%d/%d' % (len(cov), len(sel)), len(cov) == len(sel)))
rows.append(('copertura del lotto', '%d/%d' % (len(allcov), len(units)), len(allcov) == len(units)))
rows.append(('traduzioni vuote', [v['idx'] for v in cov if not v['italian'].strip()] or 0,
             all(v['italian'].strip() for v in cov)))
KINDS = {'TEXT': 8, 'DESCRIPTION': 5, 'VALUE': 2}
kk = collections.Counter(u['kind'] for u in units)
rows.append(('distribuzione dei tipi (8 TEXT + 5 DESCRIPTION + 2 VALUE)', dict(kk), dict(kk) == KINDS))
for k in ('MISSION_TEXT', 'UI_LABEL', 'LOGBOOK', 'DIALOG', 'CONVERSATION'):
    got = tuple(sorted(v['idx'] for v in cov if v['kind'] == k))
    rows.append(('%s nel segmento (0 attesi: assenza dichiarata)' % k, got or 0, got == ()))

rows.append(('DATA: 10 unita (3-11, 14) restano identiche',
             [i for i in sorted(DATA) if by_idx[i]['italian'] != by_idx[i]['english']] or 'ok',
             all(by_idx[i]['italian'] == by_idx[i]['english'] for i in DATA)))
rows.append(('PROSE: 5 unita (1, 2, 12, 13, 15) tradotte',
             [i for i in sorted(PROSE) if by_idx[i]['italian'].strip() == by_idx[i]['english'].strip()] or 'ok',
             all(by_idx[i]['italian'].strip() != by_idx[i]['english'].strip() for i in PROSE)))
rows.append(('la nave Queru ha un nome di dato (3) e una scheda di prosa (12)',
             (by_idx[3]['italian'] == by_idx[3]['english'], 12 in PROSE),
             by_idx[3]['italian'] == by_idx[3]['english'] == 'Querun, Luminous Gazes'))

it = collections.Counter(v['italian'] for v in cov)
di = [(k[:40], c, [v['idx'] for v in cov if v['italian'] == k]) for k, c in it.items() if c > 1]
rows.append(('duplicati italiano non spiegati dal sorgente', di or 'ok', not di))
rows.append(('duplicati inglesi: 0 gruppi (controllo negativo)', len(DUP_GROUPS), not DUP_GROUPS))

tab = [(v['idx'], v['english'].count('\t'), v['italian'].count('\t'))
       for v in cov if v['english'].count('\t') != v['italian'].count('\t')]
rows.append(('tab per unita (1 atteso: unita 2)', tab or 'ok', not tab))
rows.append(('tab solo in unita 2', [v['idx'] for v in cov if v['italian'].startswith('\t')], 
             [v['idx'] for v in cov if v['italian'].startswith('\t')] == [2]))
quo = [(v['idx'], v['english'].count('"'), v['italian'].count('"'))
       for v in cov if v['english'].count('"') != v['italian'].count('"')]
rows.append(('virgolette per unita (8 totali)', quo or 'ok', not quo))
rows.append(('virgolette dispari (0 attese)', [v['idx'] for v in cov if v['english'].count('"') % 2] or 0,
             not [v['idx'] for v in cov if v['english'].count('"') % 2]))
rows.append(('quadre e backtick (0 attesi)',
             [v['idx'] for v in cov if '[' in v['italian'] or '`' in v['italian']] or 'ok',
             not [v['idx'] for v in cov if '[' in v['italian'] or '`' in v['italian']]))

tag = [v['idx'] for v in cov
       if collections.Counter(TAGS.findall(v['english'])) != collections.Counter(TAGS.findall(v['italian']))]
rows.append(('token <...> per unita', tag or 'ok', not tag))
tok = sum(len(TAGS.findall(v['english'])) for v in allcov) + sum(len(TAGS.findall(v['italian'])) for v in allcov)
rows.append(('token per simbolo: 0 = 0 (assenza asserita)', str(tok), tok == 0))

rs = [v['ratio'] for v in cov]
for v in cov:
    if not 0.55 < v['ratio'] < 1.90:
        print('OUTLIER ratio:', v['idx'], v['ratio'], v['english'][:40], '|', v['italian'][:40])
rows.append(('rapporto lunghezza (gate 0,55-1,90)',
             '%.2f - %.2f' % (min(rs), max(rs)) if rs else 'nessuna',
             bool(rs) and 0.55 < min(rs) and max(rs) < 1.90))
bad = [(v['idx'], n) for v in cov
       for p, n in ((r"\b(e|piu|perche|cosi|gia|puo|cioe|percio)'", 'accento'),
                    ('\u2026', 'ellissi'), ('\u2014', 'em dash'), ('\u2019', 'apostrofo curvo'))
       if re.search(p, v['italian'])]
rows.append(('tipografia (accenti/apostrofi/dash)', bad or 'ok', not bad))
nonlat = [v['idx'] for v in cov for c in v['italian'] if ord(c) > 127 and not 0x00C0 <= ord(c) <= 0x024F]
rows.append(('caratteri non latini', nonlat or 'ok', not nonlat))

c = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
st = dict(c.execute('select state,count(*) from units group by state').fetchall())
rows.append(('state.db APPROVED/PENDING', '%s/%s' % (st['APPROVED'], st['PENDING']), st['APPROVED'] == 364))
ids = [u['id'] for u in units]
dl = c.execute('select count(*) from units where id in (%s) and state != "PENDING"' % ','.join('?' * len(ids)),
               ids).fetchone()[0]
rows.append(('unita\' del lotto fuori da PENDING', dl, dl == 0))

print('| Controllo | Esito | OK |')
print('|---|---|---|')
for a, b, ok in rows:
    print('| %s | %s | %s |' % (a, b, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d' % (sum(len(v['english'].split()) for v in cov),
                                 sum(len(v['italian'].split()) for v in cov)))
print('prima/ultima riga: %d/%d · parti %d · mancanti %d'
      % (min(u['line'] for u in sel), max(u['line'] for u in sel), len(parts),
         len([u for u in units if u['idx'] not in tr])))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
