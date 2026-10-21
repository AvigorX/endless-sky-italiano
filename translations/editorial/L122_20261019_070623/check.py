r"""check.py — L122 (`data/human/campaign events.txt`, 42 unita', righe 1338-3468, **chiude il file**)

Coda del file: **41 `DESCRIPTION`**, **1 `MISSION_TEXT`**, **18 contesti**, **21 unita' con tab**, **8
virgolette**, **zero token**, **zero quadre**.

Controlli propri del lotto:

- **zero token e zero quadre sono asserzioni** (`== {}`, `not [...]`), non omissioni: sono tre `== {}` su quattro
  controlli di forma;
- **3 testi vengono da L120/L121** e la resa è la stessa, verificata leggendo i loro `translation.json`;
- **36 testi distinti per 42 unità**: tre testi compaiono tre volte (il porto di Deep, l'apertura di Bloodsea) e due
  due volte (New Iceland, le maschere antipolvere).
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


ck("unita' tradotte 42/42", len(cov) == 42 == len(units) and not missing, '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
kk = collections.Counter(u['kind'] for u in units)
ck('tipi: 41 DESCRIPTION · 1 MISSION_TEXT', dict(kk) == {'DESCRIPTION': 41, 'MISSION_TEXT': 1}, dict(kk))
ck('nessun VALUE e nessuna UI_LABEL (asserzione vuota, dichiarata)',
   not [u['idx'] for u in units if u['kind'] in ('VALUE', 'UI_LABEL')])
ck('tutte le unita sono tradotte',
   not [v['idx'] for v in cov if v['italian'].strip() == v['english'].strip()])
tabs = [v['idx'] for v in cov if v['english'].startswith('\t')]
ck('21 unita iniziano con tab, le stesse in traduzione',
   len(tabs) == 21 and tabs == [v['idx'] for v in cov if v['italian'].startswith('\t')], len(tabs))
ck('conteggio dei tab identico per unita',
   not [v['idx'] for v in cov if v['english'].count('\t') != v['italian'].count('\t')])
ck('8 virgolette in inglese e in italiano',
   sum(v['english'].count('"') for v in cov) == 8 == sum(v['italian'].count('"') for v in cov),
   (sum(v['english'].count('"') for v in cov), sum(v['italian'].count('"') for v in cov)))
ck('virgolette per unita: stesso numero',
   not [v['idx'] for v in cov if v['english'].count('"') != v['italian'].count('"')])
ck('le virgolette stanno solo nelle unita 19, 21 e 32',
   [v['idx'] for v in cov if '"' in v['english']] == [19, 21, 32],
   [v['idx'] for v in cov if '"' in v['english']])
ck('ZERO token (asserito)', collections.Counter(t for v in cov for t in TAGS.findall(v['english'])) == {}
   == collections.Counter(t for v in cov for t in TAGS.findall(v['italian'])))
ck('ZERO quadre · ZERO backtick (asserito)',
   not [v['idx'] for v in cov if '[' in v['italian'] or ']' in v['italian'] or '`' in v['italian']])
seen = collections.Counter(u['context'] for u in units)
ck('18 contesti distinti', len(seen) == 18, len(seen))
ck('distribuzione 8x2 / 4x1 / 4x4 / 2x3',
   collections.Counter(seen.values()) == {2: 8, 1: 4, 4: 4, 3: 2}, collections.Counter(seen.values()))
ck('prima e ultima unita: righe 1338 e 3468', (cov[0]['line'], cov[-1]['line']) == (1338, 3468),
   (cov[0]['line'], cov[-1]['line']))
ck('primo e ultimo contesto: memorial on Deep / martini recovers',
   (cov[0]['context'], cov[-1]['context']) == ('event:memorial on Deep', 'event:martini recovers'),
   (cov[0]['context'], cov[-1]['context']))
ck('3468 e l\'ultima riga del file (fine file)',
   cov[-1]['line'] == max(u['line'] for u in units))
grd = collections.Counter(u['english'] for u in units)
ck('36 testi inglesi distinti per 42 unita', len(grd) == 36, len(grd))
ck('due testi tre volte e due testi due volte (3+3+2+2 = 12 unita)',
   sorted(grd.values()) == [1] * 32 + [2, 2] + [3, 3], sorted(grd.values()))
ck('nessun gruppo con due rese diverse',
   not [k for k in grd if len({by[u['idx']]['italian'] for u in units if u['english'] == k}) > 1])
it_grp = {}
for v in cov:
    it_grp.setdefault(v['italian'], []).append(v)
ck('nessun duplicato italiano non spiegato dal sorgente',
   not [g for g in it_grp.values() if len(g) > 1 and len({v['english'] for v in g}) > 1])
prev = {}
for lot in ('L120_*', 'L121_*'):
    for f in glob.glob(os.path.join(L10N, 'staging/editorial', lot, 'translation.json')):
        for u in json.load(open(f, encoding='utf-8'))['units']:
            prev[u['english']] = u['italian']
shared = [v for v in cov if v['english'] in prev]
ck('le 5 unita condivise con L120/L121 hanno la stessa resa',
   len(shared) == 5 and [v['idx'] for v in shared] == [1, 6, 9, 29, 33]
   and all(v['italian'] == prev[v['english']] for v in shared),
   [(v['idx'], v['italian'][:40]) for v in shared if v['italian'] != prev[v['english']]])
ck('registro approvato: nessun «voi»',
   not [v['idx'] for v in cov if re.search(r'\b(avete|potete|potrete|siete|vostro|vostra|vostri|vostre)\b',
                                           v['italian'])])
ck('nessuna forma di cortesia «lei» (un registro solo)',
   not [v['idx'] for v in cov if re.search(r'\b(Pensi quello|la sua nave|la farò|Senta, capitano)\b',
                                           v['italian'])])
LOW = ' '.join(v['italian'] for v in cov).lower()
TERMS = ('memoriale', 'mondi liberi', 'spazioporto', 'cantiere navale', 'colonia penale', 'cartello',
         'schiavo', 'milizia', 'anarchici', 'capitale')
ck('terminologia presente: 10 termini chiave', all(t in LOW for t in TERMS),
   [t for t in TERMS if t not in LOW])
# i nomi propri restano inglesi: si neutralizzano prima della scansione dei residui
NOSCRUB = ' '.join(v['italian'] for v in cov).replace('The Parting Glass', '@@').lower()
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' spaceport ', ' shipyard ')
ck('nessun residuo inglese fuori dai nomi propri',
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
ck('tutte le 42 unita sono PENDING nel database (misurato)',
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
