r"""check.py — L103 (data/quarg/quarg missions.txt, 42 unita', righe 118-249)

**Quattro tipi**: 28 `MISSION_TEXT`, 8 `DIALOG`, 3 `DESCRIPTION`, 3 `VALUE`.

Regola: i **`VALUE`** (unita' 1, 21, 39) sono nomi di missione e di carico — **riferimenti di dato** — e restano
**identici all'inglese**, asseriti uno per uno. `DESCRIPTION` e `DIALOG` sono tradotti per intero.

**25 tab** (senza tab 1, 2, 3, 16–23, 36, 37, 39–42). **43 virgolette**, con **una citazione aperta e non chiusa**
(unita' 30). **19 token** in sei famiglie. **Cinque ripetizioni**: 8/12, 10/13, 21/39, 22/40, 36/41.
"""
import collections, json, os, re, sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
units = sorted(src['units'], key=lambda x: x['line'])
tr = {}
parts = sorted(f for f in os.listdir(os.path.join(HERE, 'parts')) if f.endswith('.json'))
for p in parts:
    for k, v in json.load(open(os.path.join(HERE, 'parts', p), encoding='utf-8')).items():
        tr[int(k)] = v
TABS = [i for i in range(1, 43) if i not in (1, 2, 3, 16, 17, 18, 19, 20, 21, 22, 23, 36, 37, 39, 40, 41, 42)]
VALUE = [1, 21, 39]
GROUPS = [(8, 12), (10, 13), (21, 39), (22, 40), (36, 41)]
FAM = {'<destination>': 4, '<stopovers>': 3, '<cargo>': 5, '<payment>': 5, '<waypoints>': 1, '<system>': 1}
out = {'block': src['block'], 'note': src['note'], 'units': []}
missing = []
for u in units:
    if u['idx'] not in tr:
        missing.append(u['idx'])
        continue
    it = '\t' * (len(u['english']) - len(u['english'].lstrip('\t'))) + tr[u['idx']]
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


ck("unita' tradotte 42/42", len(cov) == 42 == len(units) and not missing, '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
kk = collections.Counter(u['kind'] for u in units)
ck('tipi: 28 MISSION_TEXT + 8 DIALOG + 3 DESCRIPTION + 3 VALUE',
   dict(kk) == {'MISSION_TEXT': 28, 'DIALOG': 8, 'DESCRIPTION': 3, 'VALUE': 3}, dict(kk))
ck('VALUE nelle unita 1, 21, 39', [i for i in range(1, 43) if by[i]['kind'] == 'VALUE'] == VALUE)
ck('i 3 VALUE restano identici all\'inglese (riferimenti di dato)',
   all(by[i]['italian'].strip() == by[i]['english'].strip() for i in VALUE),
   [(i, by[i]['italian']) for i in VALUE if by[i]['italian'].strip() != by[i]['english'].strip()])
ck('DESCRIPTION tradotte per intero', all(by[i]['italian'].strip() != by[i]['english'].strip() for i in (2, 22, 40)))
ck('DIALOG tradotti per intero',
   all(by[i]['italian'].strip() != by[i]['english'].strip() for i in (16, 17, 18, 19, 20, 36, 41, 42)))
ck('nessuna riga identica salvo i 3 VALUE',
   [v['idx'] for v in cov if v['italian'].strip() == v['english'].strip()] == VALUE,
   [v['idx'] for v in cov if v['italian'].strip() == v['english'].strip()])
for k in ('TEXT', 'LOGBOOK', 'UI_LABEL', 'CONVERSATION'):
    ck('%s assente' % k, not [u for u in cov if u['kind'] == k])
grd = {}
for v in cov:
    grd.setdefault(v['english'], []).append(v['idx'])
dups = sorted(tuple(x) for x in grd.values() if len(x) > 1)
ck('5 ripetizioni: 8/12, 10/13, 21/39, 22/40, 36/41', dups == GROUPS, dups)
ck('ogni gruppo reso identico', all(len({by[i]['italian'] for i in g}) == 1 for g in GROUPS))
odd = [v['idx'] for v in cov if v['english'].count('"') % 2 or v['italian'].count('"') % 2]
ck('una citazione aperta e non chiusa: unita 30', odd == [30], odd)
ck('unita 30: una sola virgoletta, e non finisce con virgoletta',
   by[30]['italian'].count('"') == 1 and not by[30]['italian'].rstrip().endswith('"'))
ctxs = []
for u in units:
    if u['context'] not in ctxs:
        ctxs.append(u['context'])
ck('3 contesti in ordine di riga',
   len(ctxs) == 3 and [c.split(':', 1)[1] for c in ctxs]
   == ['Quarg Satellites', 'Lagrange Ring: Cargo', 'Lagrange Ring: Cargo Job'],
   [c.split(':', 1)[1] for c in ctxs])
ck('tab: 25, nelle unita attese', [v['idx'] for v in cov if v['italian'].startswith('\t')] == TABS,
   [v['idx'] for v in cov if v['italian'].startswith('\t')])
ck('tab per unita', not [v for v in cov if v['english'].count('\t') != v['italian'].count('\t')])
ck('virgolette: 43 = 43',
   sum(v['english'].count('"') for v in cov) == sum(v['italian'].count('"') for v in cov) == 43,
   (sum(v['english'].count('"') for v in cov), sum(v['italian'].count('"') for v in cov)))
ck('virgolette per unita', not [v for v in cov if v['english'].count('"') != v['italian'].count('"')])
tk_e = [t for v in cov for t in TAGS.findall(v['english'])]
tk_i = [t for v in cov for t in TAGS.findall(v['italian'])]
ck('token: 19 = 19 in sei famiglie',
   tk_e == tk_i and collections.Counter(tk_e) == FAM and len(tk_e) == 19,
   (collections.Counter(tk_e), collections.Counter(tk_i)))
ck('token identici per unita e nello stesso ordine',
   all(TAGS.findall(v['english']) == TAGS.findall(v['italian']) for v in cov),
   [(v['idx'], TAGS.findall(v['english']), TAGS.findall(v['italian'])) for v in cov
    if TAGS.findall(v['english']) != TAGS.findall(v['italian'])])
ck('zero quadre, zero backtick',
   not [v for v in cov if any(c in v['italian'] for c in '[]`')])
rs = [v['ratio'] for v in cov]
for v in cov:
    if not 0.55 < v['ratio'] < 1.90:
        print('OUTLIER', v['idx'], v['ratio'], v['english'][:40], '|', v['italian'][:40])
ck('rapporto nel gate', 0.55 < min(rs) and max(rs) < 1.90, '%.2f - %.2f' % (min(rs), max(rs)))
bad = [(v['idx'], n) for v in cov for p, n in ((r"\b(e|piu|perche|cosi|gia|puo|cioe|percio)'", 'accento'),
       ('\u2026', 'ellissi'), ('\u2014', 'em dash'), ('\u2019', 'apostrofo curvo'), ('\u00ab', 'caporale'),
       ('\u00bb', 'caporale')) if re.search(p, v['italian'])]
ck('tipografia', not bad, bad)
nonlat = [v['idx'] for v in cov for c in v['italian'] if ord(c) > 127 and not 0x00C0 <= ord(c) <= 0x024F]
ck('caratteri non latini', not nonlat, nonlat)
c = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
st = dict(c.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ids = [u['id'] for u in units]
ck('unita del lotto in PENDING',
   c.execute('select count(*) from units where id in (%s) and state != "PENDING"' % ','.join('?' * len(ids)), ids).fetchone()[0] == 0)
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, b2, ok in rows:
    print('| %s | %s | %s |' % (n, b2, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d' % (sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('righe %d/%d · parti %d · mancanti %d' % (min(u['line'] for u in units), max(u['line'] for u in units),
      len(parts), len(missing)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
