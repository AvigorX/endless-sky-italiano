r"""check.py — L124 (`data/human/ships.txt`, 29 unita', righe 2102-3422)

Secondo segmento del file di navi, più leggero: **28 `DESCRIPTION`**, **1 `VALUE`**, **24 contesti** (19 da una sola
nave), **3 unità con tab**, **14 virgolette**, **zero token**. **29 testi distinti**: nessuna ripetizione dentro il
segmento.

Controlli propri del lotto:

- **un solo `VALUE`** (`Modified Argosies`), elencato esattamente e identico al sorgente;
- **due note tecniche vengono da L123** (caccia e droni): resa riletta e confrontata, così la stessa nota non
  cambia forma a un lotto di distanza;
- **tre unità con tab**: poche, quindi facili da dimenticare; il controllo le elenca.
"""
import collections
import glob
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


ck("unita' tradotte 29/29", len(cov) == 29 == len(units) and not missing, '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
kk = collections.Counter(u['kind'] for u in units)
ck('tipi: 28 DESCRIPTION · 1 VALUE', dict(kk) == {'DESCRIPTION': 28, 'VALUE': 1}, dict(kk))
VAL = [u['idx'] for u in units if u['kind'] == 'VALUE']
ck('l\'unico VALUE (unita 18, «Modified Argosies») e identico al sorgente',
   VAL == [18] and by[18]['italian'] == by[18]['english'] == 'Modified Argosies',
   [(i, by[i]['english'], by[i]['italian']) for i in VAL])
ck('tutte le unita non-VALUE sono tradotte',
   not [v['idx'] for v in cov if v['kind'] != 'VALUE' and v['italian'].strip() == v['english'].strip()])
tabs = [v['idx'] for v in cov if v['english'].startswith('\t')]
ck('3 unita iniziano con tab (9, 12, 17), le stesse in traduzione',
   tabs == [9, 12, 17] and tabs == [v['idx'] for v in cov if v['italian'].startswith('\t')], tabs)
ck('conteggio dei tab identico per unita',
   not [v['idx'] for v in cov if v['english'].count('\t') != v['italian'].count('\t')])
ck('14 virgolette in inglese e in italiano',
   sum(v['english'].count('"') for v in cov) == 14 == sum(v['italian'].count('"') for v in cov),
   (sum(v['english'].count('"') for v in cov), sum(v['italian'].count('"') for v in cov)))
ck('virgolette per unita: stesso numero',
   not [v['idx'] for v in cov if v['english'].count('"') != v['italian'].count('"')])
ck('le virgolette stanno nelle unita 8, 9, 10, 20, 23 e 26',
   [v['idx'] for v in cov if '"' in v['english']] == [8, 9, 10, 20, 23, 26],
   [v['idx'] for v in cov if '"' in v['english']])
ck('ZERO token (asserito)', collections.Counter(t for v in cov for t in TAGS.findall(v['english'])) == {}
   == collections.Counter(t for v in cov for t in TAGS.findall(v['italian'])))
ck('ZERO quadre · ZERO backtick (asserito)',
   not [v['idx'] for v in cov if '[' in v['italian'] or ']' in v['italian'] or '`' in v['italian']])
seen = collections.Counter(u['context'] for u in units)
ck('24 contesti distinti, tutti ship:', len(seen) == 24 and all(c.startswith('ship:') for c in seen), len(seen))
ck('distribuzione 19x1 / 5x2', collections.Counter(seen.values()) == {1: 19, 2: 5},
   collections.Counter(seen.values()))
ck('prima e ultima unita: righe 2102 e 3422', (cov[0]['line'], cov[-1]['line']) == (2102, 3422),
   (cov[0]['line'], cov[-1]['line']))
ck('primo e ultimo contesto: Gunboat / Raven',
   (cov[0]['context'], cov[-1]['context']) == ('ship:Gunboat', 'ship:Raven'),
   (cov[0]['context'], cov[-1]['context']))
grd = collections.Counter(u['english'] for u in units)
ck('29 testi inglesi distinti per 29 unita', len(grd) == 29, len(grd))
it_grp = {}
for v in cov:
    it_grp.setdefault(v['italian'], []).append(v)
ck('nessun duplicato italiano non spiegato dal sorgente',
   not [g for g in it_grp.values() if len(g) > 1 and len({v['english'] for v in g}) > 1])
prev = {}
for f in glob.glob(os.path.join(L10N, 'staging/editorial/L123_*', 'translation.json')):
    for u in json.load(open(f, encoding='utf-8'))['units']:
        prev[u['english']] = u['italian']
shared = [v for v in cov if v['english'] in prev]
ck('le 2 note tecniche condivise con L123 hanno la stessa resa',
   len(shared) == 2 and [v['idx'] for v in shared] == [12, 17]
   and all(v['italian'] == prev[v['english']] for v in shared),
   [(v['idx'], v['italian'][:40]) for v in shared if v['italian'] != prev[v['english']]])
ck('registro approvato: nessun «voi»',
   not [v['idx'] for v in cov if re.search(r'\b(avete|potete|potrete|siete|vostro|vostra|vostri|vostre)\b',
                                           v['italian'])])
LOW = ' '.join(v['italian'] for v in cov).lower()
TERMS = ('caccia', 'nave da guerra', 'scafo', 'carico', 'torretta', 'missili', 'equipaggio', 'cantiere',
         'portatrice', 'scudi')
ck('terminologia presente: 10 termini chiave', all(t in LOW for t in TERMS),
   [t for t in TERMS if t not in LOW])
SHIPS = ('Gunboat', 'Hauler', 'Hawk', 'Headhunter', 'Heavy Shuttle', 'Hogshead', 'Jackal', 'Lance', 'Leviathan',
         'Mammoth', 'Manta', 'Mining Drone', 'Modified Argosy', 'Monitor', 'Mule', 'Nest', 'Nighthawk', 'Osprey',
         'Protector', 'Quicksilver', 'Rainmaker', 'Raven', 'Blackbird', 'Berserker', 'Betelgeuse', 'Frigate',
         'Star Queen', 'Finch', 'Sunder', 'Mining Laser', 'Particle Cannons', 'Stars and Starships', 'Deep')
NOSCRUB = ' '.join(v['italian'] for v in cov)
for s in sorted(SHIPS, key=len, reverse=True):
    NOSCRUB = NOSCRUB.replace(s, '@@')
NOSCRUB = NOSCRUB.lower()
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' ship ', ' fighter ')
ck('nessun residuo inglese fuori dai nomi di nave',
   not [w for w in ENGW if w in NOSCRUB], [w for w in ENGW if w in NOSCRUB])
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
ck('tutte le 29 unita sono PENDING nel database (misurato)',
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
