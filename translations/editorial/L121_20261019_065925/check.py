r"""check.py — L121 (`data/human/campaign events.txt`, 56 unita', righe 282-1332)

Secondo segmento del file. Forma: **41 `DESCRIPTION`**, **14 `MISSION_TEXT`**, **1 `UI_LABEL`**, **12 contesti**
molto sbilanciati (15 / 10 / 5 / 4×3 / 3×2 / 2×4), **28 unita' con tab**, **46 virgolette** di dialogo, **1
token** (`<origin>`).

Controlli propri del lotto:

- **la `UI_LABEL` (unita' 20, `new stock`) e' identica al sorgente** — e' esclusa da «tutte tradotte» e verificata
  in un controllo suo, perché e' un nome di nodo, non prosa;
- **le 4 coppie ripetute** (`(Move on.)`, il primo paragrafo di Zug, quello di Poseidon Industries, l'apertura di
  Greenrock) hanno **una sola resa**;
- **le virgolette sbilanciate del sorgente** (unita' 22 e 24, che aprono una battuta e non la chiudono) sono
  riprodotte, non «corrette».
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


ck("unita' tradotte 56/56", len(cov) == 56 == len(units) and not missing, '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
kk = collections.Counter(u['kind'] for u in units)
ck('tipi: 41 DESCRIPTION · 14 MISSION_TEXT · 1 UI_LABEL',
   dict(kk) == {'DESCRIPTION': 41, 'MISSION_TEXT': 14, 'UI_LABEL': 1}, dict(kk))
LAB = [u['idx'] for u in units if u['kind'] == 'UI_LABEL']
ck('la UI_LABEL (unita 20, «new stock») e identica al sorgente',
   LAB == [20] and by[20]['italian'] == by[20]['english'] == 'new stock',
   [(i, by[i]['english'], by[i]['italian']) for i in LAB])
ck('tutte le unita prosaiche sono tradotte',
   not [v['idx'] for v in cov if v['kind'] != 'UI_LABEL' and v['italian'].strip() == v['english'].strip()],
   [v['idx'] for v in cov if v['kind'] != 'UI_LABEL' and v['italian'].strip() == v['english'].strip()])
# --- tab e virgolette ---------------------------------------------------------------------
te = [v['idx'] for v in cov if v['english'].startswith('\t')]
ck('28 unita iniziano con tab, le stesse in traduzione',
   len(te) == 28 and te == [v['idx'] for v in cov if v['italian'].startswith('\t')], len(te))
ck('conteggio dei tab identico per unita',
   not [v['idx'] for v in cov if v['english'].count('\t') != v['italian'].count('\t')])
ck('46 virgolette in inglese e in italiano',
   sum(v['english'].count('"') for v in cov) == 46 == sum(v['italian'].count('"') for v in cov),
   (sum(v['english'].count('"') for v in cov), sum(v['italian'].count('"') for v in cov)))
ck('virgolette per unita: stesso numero',
   not [v['idx'] for v in cov if v['english'].count('"') != v['italian'].count('"')],
   [(v['idx'], v['english'].count('"'), v['italian'].count('"')) for v in cov
    if v['english'].count('"') != v['italian'].count('"')])
ck('le due battute lasciate aperte dal sorgente (unita 22 e 24) hanno una sola virgoletta',
   [v['idx'] for v in cov if v['english'].count('"') == 1] == [22, 24],
   [v['idx'] for v in cov if v['english'].count('"') == 1])
ck('ZERO quadre · ZERO backtick',
   not [v['idx'] for v in cov if '[' in v['italian'] or ']' in v['italian'] or '`' in v['italian']])
ck('1 token <origin>, al suo posto',
   collections.Counter(t for v in cov for t in TAGS.findall(v['english'])) == {'<origin>': 1}
   == collections.Counter(t for v in cov for t in TAGS.findall(v['italian'])))
ck('token per unita: stessi simboli e stesso ordine',
   not [v['idx'] for v in cov if TAGS.findall(v['italian']) != TAGS.findall(v['english'])])
# --- contesti -----------------------------------------------------------------------------
seen = collections.Counter(u['context'] for u in units)
ck('12 contesti distinti', len(seen) == 12, len(seen))
ck('distribuzione 15 / 10 / 5 / 4x3 / 3x2 / 2x4',
   collections.Counter(seen.values()) == {15: 1, 10: 1, 5: 1, 4: 3, 3: 2, 2: 4},
   collections.Counter(seen.values()))
ck('prima e ultima unita: righe 282 e 1332', (cov[0]['line'], cov[-1]['line']) == (282, 1332),
   (cov[0]['line'], cov[-1]['line']))
ck('primo e ultimo contesto: initial deployment 1 / Greenrock recovered',
   (cov[0]['context'], cov[-1]['context'])
   == ('event:initial deployment 1', 'event:Greenrock recovered'),
   (cov[0]['context'], cov[-1]['context']))
# --- ripetizioni --------------------------------------------------------------------------
grd = collections.Counter(u['english'] for u in units)
ck('52 testi inglesi distinti per 56 unita', len(grd) == 52, len(grd))
ck('4 coppie ripetute, nessuna con due rese',
   collections.Counter(grd.values()) == {1: 48, 2: 4}
   and not [k for k in grd if len({by[u['idx']]['italian'] for u in units if u['english'] == k}) > 1],
   collections.Counter(grd.values()))
it_grp = {}
for v in cov:
    it_grp.setdefault(v['italian'], []).append(v)
ck('nessun duplicato italiano non spiegato dal sorgente',
   not [g for g in it_grp.values() if len(g) > 1 and len({v['english'] for v in g}) > 1],
   [[v['idx'] for v in g] for g in it_grp.values() if len(g) > 1 and len({v['english'] for v in g}) > 1])
# --- registro, terminologia, tipografia ---------------------------------------------------
ck('registro approvato: nessun «voi»',
   not [v['idx'] for v in cov if re.search(r'\b(avete|potete|potrete|siete|vostro|vostra|vostri|vostre)\b',
                                           v['italian'])])
ck('nessuna forma di cortesia «lei» (un registro solo)',
   not [v['idx'] for v in cov if re.search(r'\b(Pensi quello|la sua nave|la farò|Senta, capitano)\b',
                                           v['italian'])])
LOW = ' '.join(v['italian'] for v in cov).lower()
TERMS = ('bordo meridionale', 'mondi liberi', 'secessionisti', 'spazioporto', 'miniera', 'cantiere',
         'schiavi', 'contrabbandieri', 'terraformazione', 'emporio')
ck('terminologia presente: 10 termini chiave', all(t in LOW for t in TERMS),
   [t for t in TERMS if t not in LOW])
NOSCRUB = ' '.join(TAGS.sub('""', v['italian']) for v in cov if v['kind'] != 'UI_LABEL').lower()
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' shipyard ', ' refinery ')
ck('nessun residuo inglese fuori dai nomi propri e dai token',
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
ck('tutte le 56 unita sono PENDING nel database (misurato)',
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
