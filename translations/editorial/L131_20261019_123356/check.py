r"""check.py — L131 (`data/human/boarding missions.txt`, 76 unita', righe 695-959). **CHIUDE IL FILE.**

Coda del file: **2 contesti** (`Turn in Tarquin` 1, `Boarding Derelict` 75), **75 `MISSION_TEXT`**, **1
`DESCRIPTION`**, **zero `VALUE`**, **zero `UI_LABEL`**.

Controlli propri:

- **due asserzioni vuote scritte** (`VALUE` e `UI_LABEL`): `== []`, non omissioni;
- **52 testi distinti su 76 unita'** (24 ripetizioni): stesso inglese ⇒ stessa resa, su tutti i rami;
- **74 unita' con tab**, **2 virgolette** (unita' 60), **22 token in 2 famiglie**;
- la ripetizione e' la struttura del lotto: le stesse frasi di riparazione tornano su rami diversi.
"""
import collections
import json
import os
import re
import sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
units = sorted(src['units'], key=lambda x: x['line'])
tr = {}
parts = sorted(f for f in os.listdir(os.path.join(HERE, 'parts')) if f.endswith('.json'))
for p in parts:
    for k, v in json.load(open(os.path.join(HERE, 'parts', p), encoding='utf-8')).items():
        tr[int(k)] = v
out = {'block': src['block'], 'note': src['note'], 'units': []}
missing = [u['idx'] for u in units if u['idx'] not in tr]
for u in units:
    if u['idx'] not in tr:
        continue
    it = tr[u['idx']]
    out['units'].append({"idx": u['idx'], "id": u['id'], "path": u['path'], "line": u['line'],
                         "kind": u['kind'], "context": u['context'], "english": u['english'],
                         "italian": it, "ratio": round(len(it) / max(1, len(u['english'])), 3)})
open(os.path.join(HERE, 'translation.json'), 'w', encoding='utf-8').write(
    json.dumps(out, ensure_ascii=False, indent=1))
cov = out['units']
by = {v['idx']: v for v in cov}
TAGS = re.compile(r'<[^<>]+>')
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 76/76", len(cov) == 76 == len(units) and not missing, '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
kk = collections.Counter(u['kind'] for u in units)
ck('tipi: 75 MISSION_TEXT · 1 DESCRIPTION', dict(kk) == {'MISSION_TEXT': 75, 'DESCRIPTION': 1}, dict(kk))
ck('ZERO VALUE (asserzione vuota scritta)', [u['idx'] for u in units if u['kind'] == 'VALUE'] == [])
ck('ZERO UI_LABEL (asserzione vuota scritta)', [u['idx'] for u in units if u['kind'] == 'UI_LABEL'] == [])
ck('tutte le unita sono tradotte',
   not [v['idx'] for v in cov if v['italian'].strip() == v['english'].strip()],
   [v['idx'] for v in cov if v['italian'].strip() == v['english'].strip()])
tabs = [v['idx'] for v in cov if v['english'].startswith('\t')]
ck('74 unita iniziano con tab, le stesse in traduzione',
   len(tabs) == 74 and tabs == [v['idx'] for v in cov if v['italian'].startswith('\t')], len(tabs))
ck('spazi iniziali e finali identici al sorgente (76/76)',
   not [v['idx'] for v in cov
        if len(v['italian']) - len(v['italian'].rstrip()) != len(v['english']) - len(v['english'].rstrip())])
ck('2 virgolette in inglese e in italiano',
   sum(v['english'].count('"') for v in cov) == 2 == sum(v['italian'].count('"') for v in cov),
   (sum(v['english'].count('"') for v in cov), sum(v['italian'].count('"') for v in cov)))
ck('le virgolette stanno nella sola unita 60 ("astronavi ostili")',
   [v['idx'] for v in cov if '"' in v['english']] == [60]
   and '"astronavi ostili"' in by[60]['italian'], by[60]['italian'][:80])
tok = collections.Counter(t for v in cov for t in TAGS.findall(v['english']))
ck('22 token in 2 famiglie', dict(tok) == {'<origin>': 14, '<payment>': 8}, dict(tok))
ck('token per unita: sequenza identica',
   not [v['idx'] for v in cov if TAGS.findall(v['english']) != TAGS.findall(v['italian'])],
   [(v['idx'], TAGS.findall(v['english']), TAGS.findall(v['italian'])) for v in cov
    if TAGS.findall(v['english']) != TAGS.findall(v['italian'])])
ck('ZERO quadre e zero backtick (asserito)',
   not [v['idx'] for v in cov if any(c in v['english'] + v['italian'] for c in '[]`')])
seen = collections.OrderedDict()
for u in units:
    seen[u['context']] = seen.get(u['context'], 0) + 1
ck('2 contesti: 1 / 75',
   list(seen.items()) == [('mission:Turn in Tarquin', 1), ('mission:Boarding Derelict', 75)], list(seen.items()))
ck('prima e ultima unita: righe 695 e 959', (cov[0]['line'], cov[-1]['line']) == (695, 959),
   (cov[0]['line'], cov[-1]['line']))
grp = {}
for v in cov:
    grp.setdefault(v['english'].lstrip('\t'), set()).add(v['italian'])
ck('52 testi distinti su 76 unita (24 ripetizioni)', len(grp) == 52, len(grp))
ck('stesso inglese => stessa resa su tutti i rami',
   not [(k, v) for k, v in grp.items() if len(v) > 1], [(k[:40], v) for k, v in grp.items() if len(v) > 1])
rep = collections.Counter(v['english'].lstrip('\t') for v in cov)
ck('la frase di riparazione dello scafo ricorre 4 volte, quella dell alimentazione 4',
   rep['It takes a while but you manage to stabilize the ship\'s hull. While doing so you managed to find and fix '
       'some broken wiring embedded in the hull, which could have caused a powersurge.'] == 4
   and rep['With a few simple repairs you manage to get the ship\'s power systems operational and running '
           'smoothly.'] == 4, [k[:40] for k, v in rep.items() if v == 4])
LOW = ' '.join(v['italian'] for v in cov).lower()
TERMS = ('relitto', 'scafo', 'motori', 'alimentazione', 'portello', 'cabina di pilotaggio', 'refrigerante',
         'valvola', 'rottame', 'moduli', 'sovratensione', 'pirati')
ck('terminologia presente: 12 termini chiave', all(t in LOW for t in TERMS), [t for t in TERMS if t not in LOW])
ck('le tre fughe sono identiche e il testo lo dice',
   len({v['italian'] for v in cov if 'Fuggi dalla nave' in v['italian']}) == 1)
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' ship ', ' you ', ' it ')
LONG = ' '.join(TAGS.sub('""', v['italian']) for v in cov).lower()
ck('nessun residuo inglese', not [w for w in ENGW if w in LONG], [w for w in ENGW if w in LONG])
CORT = re.findall(r'\bLei\b|(?<![.!?] )\b(?:Suo|Sua|Suoi|Sue)\b', ' '.join(v['italian'] for v in cov))
ck('nessuna forma di cortesia «Lei»', not CORT, CORT)
rs = [v['ratio'] for v in cov]
ck('rapporto nel gate', 0.55 < min(rs) and max(rs) < 1.90, '%.2f - %.2f' % (min(rs), max(rs)))
bad = [(v['idx'], n) for v in cov for p, n in ((r"\b(e|piu|perche|cosi|gia|puo|cioe|percio|fa)'", 'accento'),
       ('\u2026', 'ellissi'), ('\u2014', 'em dash'), ('\u2019', 'apostrofo curvo'), ('\u00ab', 'caporale'),
       ('\u00bb', 'caporale')) if re.search(p, v['italian'])]
ck('tipografia', not bad, bad)
nonlat = [v['idx'] for v in cov for c in v['italian'] if ord(c) > 127 and not 0x00C0 <= ord(c) <= 0x024F]
ck('caratteri non latini', not nonlat, nonlat)
c = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
st = dict(c.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('tutte le 76 unita sono PENDING nel database (misurato)',
   c.execute('select count(*) from units where id in (%s) and state != "PENDING"'
             % ','.join('?' * len(units)), [u['id'] for u in units]).fetchone()[0] == 0)
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d' % (sum(len(v['english'].split()) for v in cov),
                                 sum(len(v['italian'].split()) for v in cov)))
print('righe %d/%d · parti %d · mancanti %d' % (min(u['line'] for u in units), max(u['line'] for u in units),
      len(parts), len(missing)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
