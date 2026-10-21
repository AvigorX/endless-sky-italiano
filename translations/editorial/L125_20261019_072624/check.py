r"""check.py — L125 (`data/human/ships.txt`, 20 unita', righe 3491-4266, **chiude il file**)

Coda del file di navi: **20 `DESCRIPTION`**, **nessun `VALUE`**, **15 contesti** (10×1, 5×2), **5 unità con tab**,
**14 virgolette**, **zero token**, **20 testi distinti**.

Controlli propri del lotto:

- **zero `VALUE`**: l'asserzione «i `VALUE` sono identici al sorgente» è **vuota** e viene scritta (`not [...]`), non
  omessa;
- **zero token**: `Counter(...) == {}` su entrambi i lati;
- **la nota sui droni** (unità 17) viene da L123/L124: resa riletta e confrontata;
- **6 virgolette nell'unità 1, 2 nell'unità 6, 6 nell'unità 7**: i nomi dei pod e dei modelli restano inglesi.
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


ck("unita' tradotte 20/20", len(cov) == 20 == len(units) and not missing, '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
kk = collections.Counter(u['kind'] for u in units)
ck('tipi: 20 DESCRIPTION', dict(kk) == {'DESCRIPTION': 20}, dict(kk))
ck('ZERO VALUE nel segmento (asserzione vuota, dichiarata)',
   not [u['idx'] for u in units if u['kind'] == 'VALUE'])
ck('tutte le unita sono tradotte',
   not [v['idx'] for v in cov if v['italian'].strip() == v['english'].strip()])
tabs = [v['idx'] for v in cov if v['english'].startswith('\t')]
ck('5 unita iniziano con tab (6, 9, 12, 14, 17), le stesse in traduzione',
   tabs == [6, 9, 12, 14, 17] and tabs == [v['idx'] for v in cov if v['italian'].startswith('\t')], tabs)
ck('conteggio dei tab identico per unita',
   not [v['idx'] for v in cov if v['english'].count('\t') != v['italian'].count('\t')])
ck('14 virgolette in inglese e in italiano',
   sum(v['english'].count('"') for v in cov) == 14 == sum(v['italian'].count('"') for v in cov),
   (sum(v['english'].count('"') for v in cov), sum(v['italian'].count('"') for v in cov)))
ck('virgolette per unita: stesso numero',
   not [v['idx'] for v in cov if v['english'].count('"') != v['italian'].count('"')])
ck('le virgolette sono 6 nell unita 1, 2 nell unita 6, 6 nell unita 7',
   [(v['idx'], v['english'].count('"')) for v in cov if '"' in v['english']] == [(1, 6), (6, 2), (7, 6)],
   [(v['idx'], v['english'].count('"')) for v in cov if '"' in v['english']])
ck('ZERO token (asserito)', collections.Counter(t for v in cov for t in TAGS.findall(v['english'])) == {}
   == collections.Counter(t for v in cov for t in TAGS.findall(v['italian'])))
ck('ZERO quadre · ZERO backtick (asserito)',
   not [v['idx'] for v in cov if '[' in v['italian'] or ']' in v['italian'] or '`' in v['italian']])
seen = collections.Counter(u['context'] for u in units)
ck('15 contesti distinti, tutti ship:', len(seen) == 15 and all(c.startswith('ship:') for c in seen), len(seen))
ck('distribuzione 10x1 / 5x2', collections.Counter(seen.values()) == {1: 10, 2: 5},
   collections.Counter(seen.values()))
ck('prima e ultima unita: righe 3491 e 4266', (cov[0]['line'], cov[-1]['line']) == (3491, 4266),
   (cov[0]['line'], cov[-1]['line']))
ck('primo e ultimo contesto: Roost / Wasp',
   (cov[0]['context'], cov[-1]['context']) == ('ship:Roost', 'ship:Wasp'),
   (cov[0]['context'], cov[-1]['context']))
grd = collections.Counter(u['english'] for u in units)
ck('20 testi inglesi distinti per 20 unita', len(grd) == 20, len(grd))
it_grp = {}
for v in cov:
    it_grp.setdefault(v['italian'], []).append(v)
ck('nessun duplicato italiano non spiegato dal sorgente',
   not [g for g in it_grp.values() if len(g) > 1 and len({v['english'] for v in g}) > 1])
prev = {}
for lot in ('L123_*', 'L124_*'):
    for f in glob.glob(os.path.join(L10N, 'staging/editorial', lot, 'translation.json')):
        for u in json.load(open(f, encoding='utf-8'))['units']:
            prev[u['english']] = u['italian']
shared = [v for v in cov if v['english'] in prev]
ck('la nota sui droni (unita 17) ha la stessa resa di L123/L124',
   len(shared) == 1 and shared[0]['idx'] == 17 and shared[0]['italian'] == prev[shared[0]['english']],
   [(v['idx'], v['italian'][:40]) for v in shared if v['italian'] != prev[v['english']]])
ck('registro approvato: nessun «voi»',
   not [v['idx'] for v in cov if re.search(r'\b(avete|potete|potrete|siete|vostro|vostra|vostri|vostre)\b',
                                           v['italian'])])
LOW = ' '.join(v['italian'] for v in cov).lower()
TERMS = ('portatrice', 'baie di caccia', 'nave da guerra', 'abitacolo', 'carico', 'cantiere', 'scudi', 'droni',
         'mineraria', 'intercettore', 'abitacolo')
ck('terminologia presente: 10 termini chiave', all(t in LOW for t in TERMS),
   [t for t in TERMS if t not in LOW])
SHIPS = ('Southbound', 'Hauler II', 'Hauler III', 'Nest', 'Roost', 'Saber', 'Firebird', 'Scoutship', 'Scout',
         'Scrapper', 'Shuttle', 'Skein', 'Sparrow', 'Splinter', 'Megaparsec', 'Syndicate', 'CT-50', 'Star Barge',
         'Star Queen', 'Sunder', 'Mining Drone', 'Valkyrie', 'Aerie', 'Vanguard', 'Wasp', 'Deep', 'Sol',
         'Syndicated Shipyards', 'Syndicated Systems')
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
ck('tutte le 20 unita sono PENDING nel database (misurato)',
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
