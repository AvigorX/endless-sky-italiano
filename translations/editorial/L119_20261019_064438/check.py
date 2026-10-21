r"""check.py — L119 (data/human/pirate jobs.txt, 77 unita', righe 2958-3706, chiude il file)

Terza forma dello stesso file e **prima con `CONVERSATION`**: **12** scene in tre blocchi (`northern`, `core`,
`southern pirate defense`), ognuna con **tre opzioni che iniziano con tab** — **9 unità** in totale — e **due
virgolette** nella battuta d'apertura, **6** in tutto il lotto.

Controlli propri di questo lotto:
- **9 unità che iniziano con tab**, con il **numero di tab identico** a quello del sorgente, per unità;
- **6 virgolette**, due per ciascuna scena, e nessuna altrove;
- **20 contesti**: 19 missioni da quattro unità e **un contesto da una sola unità** (`outfit:Secret Cargo`);
- **47 testi distinti** per 77 unità; una sola coppia di rese identiche, **dichiarata** (unità 73: refuso del
  sorgente «eliminating the politician **pays** you», manca «and»);
- **2 testi condivisi con L118**, con la resa riletta e confrontata;
- `verify.py` a parte usa l'**invariante di file**: qui il controllo resta di segmento.
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


ck("unita' tradotte 77/77", len(cov) == 77 == len(units) and not missing, '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
kk = collections.Counter(u['kind'] for u in units)
ck('tipi: 32 DIALOG · 17 DESCRIPTION · 16 VALUE · 12 CONVERSATION',
   dict(kk) == {'DIALOG': 32, 'DESCRIPTION': 17, 'VALUE': 16, 'CONVERSATION': 12}, dict(kk))
VAL = [u['idx'] for u in units if u['kind'] == 'VALUE']
ck('i 16 VALUE sono identici al sorgente (4 nomi di missione)',
   len(VAL) == 16 and all(by[i]['italian'] == by[i]['english'] for i in VAL),
   [i for i in VAL if by[i]['italian'] != by[i]['english']])
ck('tutte le unita non-VALUE sono tradotte',
   not [v['idx'] for v in cov if v['kind'] != 'VALUE' and v['italian'].strip() == v['english'].strip()])
ck('le 12 CONVERSATION sono tradotte',
   not [v['idx'] for v in cov if v['kind'] == 'CONVERSATION' and v['italian'] == v['english']])
# --- tab: 9 unita' ------------------------------------------------------------------------
tabs_en = [v['idx'] for v in cov if v['english'].startswith('\t')]
tabs_it = [v['idx'] for v in cov if v['italian'].startswith('\t')]
ck('9 unita iniziano con tab, e sono le stesse in inglese e in italiano',
   len(tabs_en) == 9 and tabs_en == tabs_it, (len(tabs_en), len(tabs_it)))
ck('numero di tab identico per unita (nessun tab doppio)',
   not [v['idx'] for v in cov if v['english'].count('\t') != v['italian'].count('\t')])
ck('le 9 unita con tab sono le opzioni delle tre scene',
   [v['kind'] for v in cov if v['idx'] in tabs_en] == ['CONVERSATION'] * 9)
# --- virgolette: 6, due per scena ---------------------------------------------------------
q = [(v['idx'], v['english'].count('"'), v['italian'].count('"')) for v in cov if '"' in v['english']]
ck('6 virgolette, tutte nel primo verso di ciascuna scena',
   sum(x[1] for x in q) == 6 and sum(x[2] for x in q) == 6 and [x[0] for x in q] == [13, 25, 37], q)
ck('nessuna virgoletta in piu ne in meno per unita',
   not [v['idx'] for v in cov if v['english'].count('"') != v['italian'].count('"')])
ck('ZERO quadre · ZERO backtick',
   not [v['idx'] for v in cov if '[' in v['italian'] or ']' in v['italian'] or '`' in v['italian']])
# --- token --------------------------------------------------------------------------------
TOK = {'<planet>': 28, '<payment>': 23, '<destination>': 19, '<system>': 14, '<npc>': 12, '<day>': 10}
ck('106 token nelle sei famiglie attese',
   collections.Counter(t for v in cov for t in TAGS.findall(v['english'])) == TOK
   == collections.Counter(t for v in cov for t in TAGS.findall(v['italian'])),
   collections.Counter(t for v in cov for t in TAGS.findall(v['italian'])))
ck('token per unita: stessi simboli e stesso ordine',
   not [v['idx'] for v in cov if TAGS.findall(v['italian']) != TAGS.findall(v['english'])],
   [(v['idx'], TAGS.findall(v['italian']), TAGS.findall(v['english'])) for v in cov
    if TAGS.findall(v['italian']) != TAGS.findall(v['english'])])
# --- contesti -----------------------------------------------------------------------------
seen = collections.Counter(u['context'] for u in units)
ck('20 contesti distinti', len(seen) == 20, len(seen))
ck('19 contesti da quattro unita e uno da una (outfit:Secret Cargo)',
   collections.Counter(seen.values()) == {4: 19, 1: 1}
   and seen['outfit:Secret Cargo'] == 1, collections.Counter(seen.values()))
ck('prima e ultima unita: righe 2958 e 3706', (cov[0]['line'], cov[-1]['line']) == (2958, 3706),
   (cov[0]['line'], cov[-1]['line']))
ck('primo e ultimo contesto: Raid on Merchants (South) / Republic Assassination [2]',
   (cov[0]['context'], cov[-1]['context'])
   == ('mission:Raid on Merchants (South)', 'mission:Republic Assassination [2]'),
   (cov[0]['context'], cov[-1]['context']))
# --- ripetizioni e deroga dichiarata ------------------------------------------------------
grd = collections.Counter(u['english'] for u in units)
ck('47 testi inglesi distinti per 77 unita', len(grd) == 47, len(grd))
ck('nessun gruppo con due rese diverse',
   not [k for k in grd if len({by[u['idx']]['italian'] for u in units if u['english'] == k}) > 1])
it_grp = {}
for v in cov:
    it_grp.setdefault(v['italian'], []).append(v)
dup = [g for g in it_grp.values() if len(g) > 1 and len({v['english'] for v in g}) > 1]
ck('un solo doppio di resa, quello dichiarato (unita 65 e 73, refuso del sorgente)',
   len(dup) == 1 and sorted(v['idx'] for v in dup[0]) == [65, 73],
   [[v['idx'] for v in g] for g in dup])
ck('il refuso del sorgente e dichiarato: unita 73 senza «and»',
   'and' not in by[73]['english'].split('politician')[1] and by[73]['italian'] == by[65]['italian'])
prev = {}
for lot in ('L117_*', 'L118_*'):
    for f in glob.glob(os.path.join(L10N, 'staging/editorial', lot, 'translation.json')):
        for u in json.load(open(f, encoding='utf-8'))['units']:
            prev[u['english']] = u['italian']
shared = [v for v in cov if v['english'] in prev]
ck('le 3 unita condivise con L118 (1 nome + 2 dialoghi) hanno la stessa resa',
   len(shared) == 3 and [v['idx'] for v in shared] == [1, 3, 4]
   and all(v['italian'] == prev[v['english']] for v in shared),
   [(v['idx'], v['italian'][:40]) for v in shared if v['italian'] != prev[v['english']]])
# --- registro, terminologia, tipografia ---------------------------------------------------
ck('registro approvato: nessun «voi»',
   not [v['idx'] for v in cov if re.search(r'\b(avete|potete|potrete|siete|vostro|vostra|vostri|vostre)\b',
                                           v['italian'])])
LOW = ' '.join(v['italian'] for v in cov).lower()
TERMS = ('anarchia', 'politico', 'assassinalo', 'convoglio', 'carico segreto', 'trafficanti di schiavi',
         'signore della guerra', 'flotta di difesa', 'compenso', 'obiettivo')
ck('terminologia presente: 10 termini chiave', all(t in LOW for t in TERMS),
   [t for t in TERMS if t not in LOW])
NOSCRUB = ' '.join(TAGS.sub('""', v['italian']) for v in cov if v['kind'] != 'VALUE').lower()
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' ship ', ' fleet ', ' target ')
ck('nessun residuo inglese fuori dai token e dai nomi',
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
ck('tutte le 77 unita sono PENDING nel database (misurato)',
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
