r"""check.py — L139 (`data/starts.txt`, 2 unita', righe 365-366). **CHIUDE IL FILE**.

Le due unita' sono nomi di equipaggiamento: la lista `ID_OK` le dichiara identiche al sorgente e un controllo le
verifica **una per una**, invece di escluderle dal conteggio delle «tradotte».

Tre asserzioni vuote scritte: **zero `VALUE`**, **zero `UI_LABEL`**, **zero token**.
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
ID_OK = {1: '"Benga" Atomic Thruster', 2: '"Biroo" Atomic Steering'}
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 2/2", len(cov) == 2 == len(units) and not missing, '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 2 TEXT', collections.Counter(u['kind'] for u in units) == {'TEXT': 2},
   collections.Counter(u['kind'] for u in units))
ck('ZERO VALUE (asserzione vuota scritta)', [u['idx'] for u in units if u['kind'] == 'VALUE'] == [])
ck('ZERO UI_LABEL (asserzione vuota scritta)', [u['idx'] for u in units if u['kind'] == 'UI_LABEL'] == [])
ck('ZERO token in tutto il file (asserzione vuota scritta)',
   collections.Counter(t for u in units for t in TAGS.findall(u['english'])) == {})
ck('ID_OK: i due nomi di equipaggiamento sono identici al sorgente, uno per uno',
   [(v['idx'], v['italian']) for v in cov] == [(1, '"Benga" Atomic Thruster'),
                                               (2, '"Biroo" Atomic Steering')],
   [(v['idx'], v['italian']) for v in cov])
ck('ID_OK dichiarata e usata (non esclusa dai controlli)',
   all(by[k]['italian'] == ID_OK[k] == by[k]['english'] for k in ID_OK))
ck('0 unita con tab (il tab del raw e fuori dal campo english)',
   [v['idx'] for v in cov if v['english'].startswith('\t')] == []
   and [v['idx'] for v in cov if v['italian'].startswith('\t')] == [])
ck('4 virgolette, due per unita: fanno parte dei nomi',
   sum(v['english'].count('"') for v in cov) == 4 == sum(v['italian'].count('"') for v in cov)
   and [(v['idx'], v['italian'].count('"')) for v in cov] == [(1, 2), (2, 2)])
ck('nessuna unita dispari (asserito: lista vuota)',
   [v['idx'] for v in cov if v['english'].count('"') % 2] == [])
ck('1 contesto: ship:Grasshopper, 2 unita',
   list(collections.Counter(v['context'] for v in cov).items()) == [('ship:Grasshopper', 2)])
ck('prima e ultima unita: righe 365 e 366', (cov[0]['line'], cov[-1]['line']) == (365, 366),
   (cov[0]['line'], cov[-1]['line']))
ck('2 testi distinti', len({v['english'] for v in cov}) == 2)
ck('ZERO quadre, ZERO backtick e zero caratteri tipografici nel testo',
   not [v['idx'] for v in cov if any(c in v['english'] + v['italian']
                                    for c in '[]`\u2019\u2014\u2013\u2026')])
LOW = ' '.join(v['italian'] for v in cov).lower()
ck('i nomi dei produttori restano: Benga, Biroo, e i tipi Thruster, Steering',
   all(t in LOW for t in ('benga', 'biroo', 'thruster', 'steering')))
ck('nessun residuo italiano (i nomi non sono tradotti: nessuna parola italiana)',
   not [w for w in ('motore', 'propulsore', 'sterzo', 'timone') if w in LOW])
rs = [v['ratio'] for v in cov]
ck('rapporto: identico al sorgente, quindi 1.00', all(r == 1.0 for r in rs), rs)
c = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
st = dict(c.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('tutte le 2 unita sono PENDING nel database (misurato)',
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
