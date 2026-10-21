r"""check.py — L118 (data/human/pirate jobs.txt, 104 unita', righe 1627-2955)

Secondo lotto dello stesso file, **forma diversa dal primo**: **36 `DIALOG`** (L117 ne aveva 5), **33 `VALUE`**,
**33 `DESCRIPTION`**, solo **2 `MISSION_TEXT`**. I **192 token** passano da sei a **nove famiglie** (compaiono
`<system>`, `<day>`, `<npc>`, `<date>`) e non c'è **nessuna virgoletta** — asserzione vuota, non omissione.

- **33 `VALUE` identici al sorgente** (nomi di missione, elencati esplicitamente).
- **39 testi distinti** per 104 unità: la ripetizione è del sorgente e la resa ripete (una resa per testo).
- **Tre testi sono già stati tradotti in L117** (il criminale galattico): la resa è la **stessa**, e il controllo
  lo verifica leggendo il `translation.json` di L117.
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
missing = []
for u in units:
    if u['idx'] not in tr:
        missing.append(u['idx'])
        continue
    it = tr[u['idx']]
    out['units'].append({"idx": u['idx'], "id": u['id'], "path": u['path'], "line": u['line'],
                         "kind": u['kind'], "context": u['context'], "english": u['english'],
                         "italian": it, "ratio": round(len(it) / max(1, len(u['english'])), 3)})
open(os.path.join(HERE, 'translation.json'), 'w', encoding='utf-8').write(json.dumps(out, ensure_ascii=False, indent=1))
cov = out['units']
by = {v['idx']: v for v in cov}
TAGS = re.compile(r'<[^<>]+>')
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 104/104", len(cov) == 104 == len(units) and not missing, '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
kk = collections.Counter(u['kind'] for u in units)
ck('tipi: 36 DIALOG · 33 VALUE · 33 DESCRIPTION · 2 MISSION_TEXT',
   dict(kk) == {'DIALOG': 36, 'VALUE': 33, 'DESCRIPTION': 33, 'MISSION_TEXT': 2}, dict(kk))
VAL = [u['idx'] for u in units if u['kind'] == 'VALUE']
ck('i 33 VALUE sono identici al sorgente (nomi di missione)',
   len(VAL) == 33 and all(by[i]['italian'] == by[i]['english'] for i in VAL),
   [i for i in VAL if by[i]['italian'] != by[i]['english']])
ck('tutte le unita non-VALUE sono tradotte',
   not [v['idx'] for v in cov if v['kind'] != 'VALUE' and v['italian'].strip() == v['english'].strip()])
ck('i 36 DIALOG sono tradotti',
   not [v['idx'] for v in cov if v['kind'] == 'DIALOG' and v['italian'] == v['english']])
ck('ZERO tab, nel sorgente e in traduzione',
   not [u['idx'] for u in units if '\t' in u['english']]
   and not [v['idx'] for v in cov if '\t' in v['italian']])
a = sum(v['english'].count('"') for v in cov)
b = sum(v['italian'].count('"') for v in cov)
ck('ZERO virgolette (asserito: 0 = 0)', a == b == 0, (a, b))
ck('ZERO quadre (asserito vuoto)', not [v['idx'] for v in cov if '[' in v['italian'] or ']' in v['italian']])
ck('ZERO backtick', not [v['idx'] for v in cov if '`' in v['italian']])
# --- token: 192 in nove famiglie -----------------------------------------------------------
TOK = {'<planet>': 53, '<payment>': 52, '<destination>': 33, '<system>': 33, '<day>': 17,
       '<npc>': 9, '<date>': 9, '<bunks>': 5, '<cargo>': 2}
ck('192 token nelle nove famiglie attese',
   collections.Counter(t for v in cov for t in TAGS.findall(v['english'])) == TOK
   == collections.Counter(t for v in cov for t in TAGS.findall(v['italian'])),
   collections.Counter(t for v in cov for t in TAGS.findall(v['italian'])))
ck('token per unita: stessi simboli e stesso ordine',
   not [(v['idx'], TAGS.findall(v['italian']), TAGS.findall(v['english'])) for v in cov
        if TAGS.findall(v['italian']) != TAGS.findall(v['english'])],
   [(v['idx'], TAGS.findall(v['italian']), TAGS.findall(v['english'])) for v in cov
    if TAGS.findall(v['italian']) != TAGS.findall(v['english'])])
# --- contesti: 33 missioni -----------------------------------------------------------------
seen = collections.Counter(u['context'] for u in units)
ck('33 contesti distinti, tutti mission:', len(seen) == 33 and all(c.startswith('mission:') for c in seen),
   len(seen))
ck('distribuzione: 19 contesti con 4 unita, 14 con 2',
   collections.Counter(seen.values()) == {4: 19, 2: 14}, collections.Counter(seen.values()))
ck('prima e ultima unita: righe 1627 e 2955', (cov[0]['line'], cov[-1]['line']) == (1627, 2955),
   (cov[0]['line'], cov[-1]['line']))
ck('primo e ultimo contesto: Highly Wanted Passenger (Core) / Raid on Merchants (Core)',
   (cov[0]['context'], cov[-1]['context'])
   == ('mission:Highly Wanted Passenger (Core)', 'mission:Raid on Merchants (Core)'),
   (cov[0]['context'], cov[-1]['context']))
# --- ripetizioni: 39 testi distinti, una resa per testo ------------------------------------
grd = collections.Counter(u['english'] for u in units)
ck('39 testi inglesi distinti per 104 unita', len(grd) == 39, len(grd))
ck('nessun gruppo con due rese diverse',
   not [k for k in grd if len({by[u['idx']]['italian'] for u in units if u['english'] == k}) > 1])
it_grp = {}
for v in cov:
    it_grp.setdefault(v['italian'], []).append(v)
ck('nessun duplicato italiano non spiegato dal sorgente',
   not [g for g in it_grp.values() if len(g) > 1 and len({v['english'] for v in g}) > 1],
   [[v['idx'] for v in g] for g in it_grp.values() if len(g) > 1 and len({v['english'] for v in g}) > 1])
# --- coerenza con L117 sui testi gia' tradotti --------------------------------------------
prev = {}
for f in glob.glob(os.path.join(L10N, 'staging/editorial/L117_*', 'translation.json')):
    for u in json.load(open(f, encoding='utf-8'))['units']:
        prev[u['english']] = u['italian']
shared = [v for v in cov if v['english'] in prev]
ck('8 unita (4 testi) erano gia in L117 e hanno la stessa resa',
   len(shared) == 8 and all(v['italian'] == prev[v['english']] for v in shared),
   [(v['idx'], v['italian'][:40]) for v in shared if v['italian'] != prev[v['english']]])
ck('registro approvato: nessun «voi»',
   not [v['idx'] for v in cov if re.search(r'\b(avete|potete|potrete|siete|vostro|vostra|vostri|vostre)\b',
                                           v['italian'])])
LOW = ' '.join(v['italian'] for v in cov).lower()
TERMS = ('forze dell\'ordine', 'flotta', 'compenso', 'schiavi', 'banda rivale', 'predoni', 'milizia',
         'sindacato', 'marina', 'mercanti', 'bottino', 'sistema')
ck('terminologia presente: 12 termini chiave', all(t in LOW for t in TERMS),
   [t for t in TERMS if t not in LOW])
# i nomi di missione (`VALUE`) restano in inglese per decisione: si escludono dalla scansione dei residui
NOSCRUB = ' '.join(TAGS.sub('""', v['italian']) for v in cov if v['kind'] != 'VALUE').lower()
ENGWORDS = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' ship ', ' law ')
ck('nessun residuo inglese fuori dai token',
   not [w for w in ENGWORDS if w in NOSCRUB], [w for w in ENGWORDS if w in NOSCRUB])
rs = [v['ratio'] for v in cov]
for v in cov:
    if not 0.55 < v['ratio'] < 1.90:
        print('OUTLIER', v['idx'], v['ratio'], v['english'][:40], '|', v['italian'][:40])
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
ck('tutte le 104 unita sono PENDING nel database (misurato)',
   c.execute('select count(*) from units where id in (%s) and state != "PENDING"'
             % ','.join('?' * len(units)), [u['id'] for u in units]).fetchone()[0] == 0)
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, b2, ok in rows:
    print('| %s | %s | %s |' % (n, b2, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d' % (sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('righe %d/%d · parti %d · mancanti %d' % (min(u['line'] for u in units), max(u['line'] for u in units),
      len(parts), len(missing)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
