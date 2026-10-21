r"""check.py — L94 (data/coalition/coalition culture conversations.txt, 36 unita', righe 81-133)

Secondo lotto del file, contesto `Coalition Folklore: Arach`. **36 `MISSION_TEXT`**, **0 `UI_LABEL`** in questa
finestra. **35 tab** (tutte tranne la 1). **64 virgolette** (l'unita' 1 e la 7 ne hanno 6; 4, 12, 15, 19, 20,
33 ne hanno 4). **0 token** `<…>`: asserzione `tok == 0`.

**Due gruppi di ripetizioni inglesi**, resi identici: `(Stay for the next play.)` (16, 22) e `(Leave.)`
(17, 23, 29). Il parlato degli Arach ha **sintassi invertita** ed e' riprodotto con ordine marcato italiano.
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
TABS = list(range(2, 37))
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


ck("unita' tradotte 36/36", len(cov) == 36 == len(units) and not missing, '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
kk = collections.Counter(u['kind'] for u in units)
ck('tipi: 36 MISSION_TEXT', dict(kk) == {'MISSION_TEXT': 36}, dict(kk))
ck('0 UI_LABEL nella finestra (premessa)', not [u for u in units if u['kind'] == 'UI_LABEL'],
   [u['idx'] for u in units if u['kind'] == 'UI_LABEL'])
for k in ('TEXT', 'VALUE', 'DESCRIPTION', 'UI_LABEL', 'LOGBOOK', 'DIALOG', 'CONVERSATION'):
    ck('%s assente' % k, not [u for u in cov if u['kind'] == k])
ck('tutte tradotte (nessuna identica)', all(v['italian'].strip() != v['english'].strip() for v in cov),
   [v['idx'] for v in cov if v['italian'].strip() == v['english'].strip()])
grd = {}
for v in cov:
    grd.setdefault(v['english'], []).append(v['idx'])
dups = sorted(tuple(x) for x in grd.values() if len(x) > 1)
ck('ripetizioni inglesi: 16/22 e 17/23/29', dups == [(16, 22), (17, 23, 29)], dups)
ck('16/22 resa identica', by[16]['italian'] == by[22]['italian'])
ck('17/23/29 resa identica', by[17]['italian'] == by[23]['italian'] == by[29]['italian'])
ck('nessun altro duplicato italiano',
   sorted(c for c in collections.Counter(v['italian'] for v in cov).values() if c > 1) == [2, 3],
   sorted(c for c in collections.Counter(v['italian'] for v in cov).values() if c > 1))
ck('1 contesto (Arach)', len(set(u['context'] for u in units)) == 1
   and units[0]['context'].endswith('Arach'), units[0]['context'])
ck('tab: 35, nelle unita attese', [v['idx'] for v in cov if v['italian'].startswith('\t')] == TABS,
   [v['idx'] for v in cov if v['italian'].startswith('\t')])
ck('tab per unita', not [v for v in cov if v['english'].count('\t') != v['italian'].count('\t')],
   [(v['idx'], v['english'].count('\t'), v['italian'].count('\t')) for v in cov
    if v['english'].count('\t') != v['italian'].count('\t')])
ck('virgolette: 64 = 64',
   sum(v['english'].count('"') for v in cov) == sum(v['italian'].count('"') for v in cov) == 64,
   (sum(v['english'].count('"') for v in cov), sum(v['italian'].count('"') for v in cov)))
ck('virgolette per unita (6 nelle unita 1 e 7)',
   [v['idx'] for v in cov if v['english'].count('"') != v['italian'].count('"')] == []
   and [v['idx'] for v in cov if v['english'].count('"') == 6] == [1, 7])
ck('nessuna virgoletta dispari', [v['idx'] for v in cov if v['italian'].count('"') % 2] == [])
ck('token: 0 = 0 (asserzione)', sum(len(TAGS.findall(v['english'])) for v in cov) == 0
   and sum(len(TAGS.findall(v['italian'])) for v in cov) == 0,
   (sum(len(TAGS.findall(v['english'])) for v in cov), sum(len(TAGS.findall(v['italian'])) for v in cov)))
ck('quadre/backtick: 0', not [v for v in cov if '[' in v['italian'] or ']' in v['italian'] or '`' in v['italian']])
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
