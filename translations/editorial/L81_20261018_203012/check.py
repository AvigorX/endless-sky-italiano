r"""check.py — L81 (data/successors/predecessors.txt, 22 unita', righe 1-200)

**Primo lotto su descrizioni di navi**: contesti `ship:Resja, of the Nine Eyes` (17-112) e
`ship:Hasur, Vowsworn` (123-196).

Misure del sorgente (decisione 119):
  - **2 `VALUE`** (1, 15): nomi delle navi — **dati**, restano identici;
  - **15 `TEXT`** (2-9, 16-22): nomi di equipaggiamento mostrati nella scheda (`Hyperdrive`,
    `"Jiita" Heirloom Shielding`, `Multimodal Armor: Regen`...) — **dati definiti altrove**, restano identici;
  - **5 `DESCRIPTION`** (10-14): **prosa**, la poesia di Resja incisa sugli scafi — tradotta (e rimata);
  - **0 tab** (nessuna indentazione), **12 virgolette**, **0 dispari**, **0 token**, **0 duplicati**;
  - tipi: 15 `TEXT` + 5 `DESCRIPTION` + 2 `VALUE`; 0 `MISSION_TEXT`, 0 `UI_LABEL`, 0 `LOGBOOK`,
    0 `DIALOG`, 0 `CONVERSATION`.
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

DATA = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 15, 16, 17, 18, 19, 20, 21, 22])
PROSE = set(range(10, 15))
en_count = collections.Counter(u['english'] for u in units)
DUP_GROUPS = {k: [u['idx'] for u in units if u['english'] == k] for k, v in en_count.items() if v > 1}
DUP_OK = set(i for v in DUP_GROUPS.values() for i in v)
WANT_DUP = {frozenset([3, 17]), frozenset([4, 18]), frozenset([6, 20]),
            frozenset([7, 21]), frozenset([9, 22])}

lo, hi = 1, len(units)
if '--range' in sys.argv:
    i = sys.argv.index('--range')
    lo, hi = int(sys.argv[i + 1]), int(sys.argv[i + 2])
sel = [u for u in units if lo <= u['idx'] <= hi]


def build(it, en):
    return '\t' * (len(en) - len(en.lstrip('\t'))) + it


out = {'block': src['block'], 'note': src['note'], 'units': []}
for u in units:
    if u['idx'] not in tr:
        continue
    it = build(tr[u['idx']], u['english'])
    out['units'].append({
        "idx": u['idx'], "id": u['id'], "path": u['path'], "line": u['line'], "kind": u['kind'],
        "context": u['context'], "english": u['english'], "italian": it,
        "ratio": round(len(it) / max(1, len(u['english'])), 3)})
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

KINDS = {'TEXT': 15, 'DESCRIPTION': 5, 'VALUE': 2}
kk = collections.Counter(u['kind'] for u in units)
rows.append(('distribuzione dei tipi (15 TEXT + 5 DESCRIPTION + 2 VALUE)', dict(kk), dict(kk) == KINDS))
for k in ('MISSION_TEXT', 'UI_LABEL', 'LOGBOOK', 'DIALOG', 'CONVERSATION'):
    got = tuple(sorted(v['idx'] for v in cov if v['kind'] == k))
    rows.append(('%s nel segmento (0 attesi: assenza dichiarata)' % k, got or 0, got == ()))

text_u = sorted(v['idx'] for v in cov if v['kind'] == 'TEXT')
rows.append(('TEXT: 15 unita (2-9, 16-22), controllo positivo', len(text_u), text_u == sorted(DATA - {1, 15})))
same_data = [i for i in DATA if by_idx[i]['italian'] != by_idx[i]['english']]
rows.append(('VALUE e TEXT restano identici (nomi di nave e di equipaggiamento)', same_data or 'ok', not same_data))
prose = sorted(v['idx'] for v in cov if v['kind'] == 'DESCRIPTION')
rows.append(('DESCRIPTION: 5 unita (10-14), la poesia', prose, prose == sorted(PROSE)))
prose_same = [i for i in prose if by_idx[i]['italian'].strip() == by_idx[i]['english'].strip()]
rows.append(('le 5 DESCRIPTION sono tradotte, non lasciate in inglese', prose_same or 'ok', not prose_same))
rim = [by_idx[i]['italian'].rstrip(' ,.').lower()[-3:] for i in range(11, 15)]
rows.append(('le quattro strofe rimano (desinenze: %s)' % ', '.join(sorted(set(rim))), len(set(rim)) == 1,
             len(set(rim)) == 1))

it = collections.Counter(v['italian'] for v in cov)
di = [(k[:40], c, [v['idx'] for v in cov if v['italian'] == k]) for k, c in it.items() if c > 1]
di = [d for d in di if not set(d[2]) <= DUP_OK]
rows.append(('duplicati italiano non spiegati dal sorgente', di or 'ok', not di))
rows.append(('duplicati inglesi: 5 gruppi (stessi nomi su due navi)', len(DUP_GROUPS),
             set(frozenset(v) for v in DUP_GROUPS.values()) == WANT_DUP))
rows.append(('i cinque gruppi hanno resa identica',
             sum(1 for g in DUP_GROUPS.values() if len(set(by_idx[i]['italian'] for i in g)) == 1),
             all(len(set(by_idx[i]['italian'] for i in g)) == 1 for g in DUP_GROUPS.values())))

tab = [(v['idx'], v['english'].count('\t'), v['italian'].count('\t'))
       for v in cov if v['english'].count('\t') != v['italian'].count('\t')]
rows.append(('tab per unita (0 nel sorgente: nessuna indentazione)', tab or 'ok', not tab))
tab_add = [v['idx'] for v in cov if v['italian'].startswith('\t')]
rows.append(('nessun tab aggiunto dalle parti', tab_add or 'ok', not tab_add))
quo = [(v['idx'], v['english'].count('"'), v['italian'].count('"'))
       for v in cov if v['english'].count('"') != v['italian'].count('"')]
rows.append(('virgolette per unita', quo or 'ok', not quo))
odd = tuple(sorted(v['idx'] for v in cov if v['english'].count('"') % 2))
rows.append(('virgolette dispari (0 attese: assenza dichiarata)', odd or 0, odd == ()))
rows.append(('quadre [ ] (0 attese: assenza dichiarata)',
             [v['idx'] for v in cov if '[' in v['italian']] or 'ok',
             not [v['idx'] for v in cov if '[' in v['italian']]))

tag = [v['idx'] for v in cov
       if collections.Counter(TAGS.findall(v['english'])) != collections.Counter(TAGS.findall(v['italian']))]
rows.append(('token <...> per unita', tag or 'ok', not tag))
en_tok = sum(len(TAGS.findall(v['english'])) for v in allcov)
it_tok = sum(len(TAGS.findall(v['italian'])) for v in allcov)
rows.append(('token per simbolo: 0 = 0 (assenza asserita)', (en_tok, it_tok), en_tok == it_tok == 0))
rows.append(('backtick (0 attesi)', [v['idx'] for v in cov if '`' in v['italian']] or 'ok',
             not [v['idx'] for v in cov if '`' in v['italian']]))

rs = [v['ratio'] for v in cov]
for v in cov:
    if not 0.55 < v['ratio'] < 1.90:
        print('OUTLIER ratio:', v['idx'], v['ratio'], v['english'][:40], '|', v['italian'][:40])
rows.append(('rapporto lunghezza (gate 0,55-1,90)',
             '%.2f - %.2f' % (min(rs), max(rs)) if rs else 'nessuna',
             bool(rs) and 0.55 < min(rs) and max(rs) < 1.90))

bad = []
for v in cov:
    for pat, name in ((r"\b(e|piu|perche|cosi|gia|puo|cioe|percio)'", 'accento sostitutivo'),
                      ('\u2026', 'ellissi tipografica'), ('\u2014', 'em dash'),
                      ('\u2019', 'apostrofo curvo')):
        if re.search(pat, v['italian']):
            bad.append((v['idx'], name))
rows.append(('tipografia (accenti/apostrofi/dash)', bad or 'ok', not bad))
nonlat = [(v['idx'], hex(ord(c))) for v in cov for c in v['italian']
          if ord(c) > 127 and not (0x00C0 <= ord(c) <= 0x024F)]
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
print('virgolette IT %d / EN %d' % (sum(v['italian'].count('"') for v in cov),
                                    sum(v['english'].count('"') for v in cov)))
print('prima/ultima riga: %d/%d · parti %d · mancanti %d'
      % (min(u['line'] for u in sel), max(u['line'] for u in sel), len(parts),
         len([u for u in units if u['idx'] not in tr])))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
