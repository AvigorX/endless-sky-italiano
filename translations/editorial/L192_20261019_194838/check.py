r"""check.py — L192 (`data/bunrodea/bunrodea missions.txt`, 12 unita', righe 64-91).

Secondo lotto della missione: l'arrivo sulla superficie, la metropoli, il palazzo e l'attesa. **12 `MISSION_TEXT`**, zero
`VALUE`, **11 tab**, **zero virgolette** (asserzione vuota), **1 segnaposto `<origin>`**. Le tre scelte (idx 4, 5, 7) e le
due varianti di attesa (idx 10, 11) devono restare scelte brevi fra parentesi.
"""
import collections
import json
import os
import re
import sqlite3

TAB = chr(9)
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
IT_ALL = ' '.join(v['italian'] for v in cov)
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 12/12", len(cov) == 12 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 12 MISSION_TEXT, ZERO VALUE, ZERO DESCRIPTION (asserzioni scritte)',
   collections.Counter(u['kind'] for u in units) == {'MISSION_TEXT': 12})
ck('ZERO UI_LABEL (asserzione vuota)', [u['idx'] for u in units if u['kind'] == 'UI_LABEL'] == [])
ck("il segnaposto `<origin>` una volta per lingua, in idx 1",
   {t for u in units for t in TAGS.findall(u['english'])} == {'<origin>'}
   == {t for v in cov for t in TAGS.findall(v['italian'])}
   and [v['idx'] for v in cov if '<origin>' in v['english']] == [1]
   == [v['idx'] for v in cov if '<origin>' in v['italian']])
ck('ZERO virgolette in inglese e in italiano (asserzione vuota scritta)',
   sum(v['english'].count('"') for v in cov) == 0 == sum(v['italian'].count('"') for v in cov))
ck('11 tab iniziali, idx 2-12, in inglese e in italiano',
   [v['idx'] for v in cov if v['english'].startswith(TAB)] == list(range(2, 13))
   == [v['idx'] for v in cov if v['italian'].startswith(TAB)])
ck('le tre scelte sono fra parentesi e brevi (idx 4, 5, 7)',
   [i for i in (4, 5, 7) if by[i]['italian'].strip().startswith('(')] == [4, 5, 7]
   and all(len(by[i]['italian'].split()) <= 8 for i in (4, 5, 7)))
ck('la metropoli ha grattacieli oltre l\'orizzonte e un palazzo con molti gradini (idx 2)',
   'Grattacieli' in by[2]['italian'] and 'palazzo' in by[2]['italian'] and 'gradini' in by[2]['italian'])
ck('il veicolo disattiva i repulsori (idx 6)', 'disattivare tutti i repulsori' in by[6]['italian'])
ck('colpire il veicolo libera la nave ma provoca le navi nemiche (idx 9)',
   'Giri una delle torrette' in by[9]['italian'] and 'ti prendono di mira sul radar' in by[9]['italian'])
ck('idx 10 e 11 sono due varianti dell\'attesa, entrambe sulla rampa d\'imbarco',
   "rampa d'imbarco" in by[10]['italian'] and "rampa d'imbarco" in by[11]['italian']
   and by[10]['italian'] != by[11]['italian'])
ck("l'ultima unita' introduce la creatura a sei arti e le scale (idx 12)",
   'sei arti' in by[12]['italian'] and 'fondo delle scale' in by[12]['italian'])
ck('12 unita, 12 testi inglesi distinti', len({v['english'] for v in cov}) == 12)
ck('un solo contesto', len({u['context'] for u in units}) == 1)
ck('prima e ultima unita: righe 64 e 91', (cov[0]['line'], cov[-1]['line']) == (64, 91))
ck('nessuno spazio finale (tab iniziali ammessi)',
   not [v['idx'] for v in cov if v['english'].rstrip(TAB) != v['english'].rstrip(TAB).rstrip()
        or v['italian'].rstrip(TAB) != v['italian'].rstrip(TAB).rstrip()])
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' you ', ' to the ', ' will be ',
        ' is ', ' are ', ' from the ', ' its ', ' it is ', ' such as ', ' rather than ')
ck('nessun residuo inglese', not [w for w in ENGW if w in IT_ALL.lower()],
   [w for w in ENGW if w in IT_ALL.lower()])
CORT = re.findall(r'\bLei\b|(?<![.!?] )\b(?:Suo|Sua|Suoi|Sue)\b', IT_ALL)
ck('nessuna forma di cortesia «Lei»', not CORT, CORT)
rs = [v['ratio'] for v in cov]
ck('rapporto nel gate 0,55-1,90', 0.55 < min(rs) and max(rs) < 1.90, '%.2f - %.2f' % (min(rs), max(rs)))
bad = [(v['idx'], n) for v in cov for p, n in ((r"\b(e|piu|perche|cosi|gia|puo|cioe|percio|fa)'", 'accento'),
       ('\u2026', 'ellissi'), ('\u2014', 'em dash'), ('\u2013', 'en dash'), ('\u2019', 'apostrofo curvo')) if re.search(p, v['italian'])]
ck('tipografia (accenti veri, nessun carattere tipografico)', not bad, bad)
nonlat = [v['idx'] for v in cov for c in v['italian'] if ord(c) > 127 and not 0x00C0 <= ord(c) <= 0x024F]
ck('caratteri non latini', not nonlat, nonlat)
c = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
st = dict(c.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('tutte le 12 unita sono PENDING (misurato)',
   c.execute('select count(*) from units where id in (%s) and state != "PENDING"'
             % ','.join('?' * len(units)), [u['id'] for u in units]).fetchone()[0] == 0)
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d' % (sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('righe %d/%d · parti %d · mancanti %d' % (min(u['line'] for u in units), max(u['line'] for u in units),
      len(parts), len([u for u in units if u['idx'] not in tr])))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
