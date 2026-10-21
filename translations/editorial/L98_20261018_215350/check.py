r"""check.py — L98 (data/hai/hai culture conversations.txt, 39 unita', righe 1-105)

Primo lotto di un **file nuovo**. **39 `MISSION_TEXT`**, 0 `UI_LABEL` (premessa asserita). **36 tab** (senza
tab 1, 9, 25). **58 virgolette**. **1 token**: `<destination>` (unita' 7). **6 quadre = 3 coppie** nell'unita' 30,
la voce del dispositivo di traduzione: si riproducono, non si tolgono. **3 ripetizioni**: 20/37, 27/31, 29/39.
Le unita' 28 e 32 differiscono per **una virgola**. **3 contesti** in ordine di riga.
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
TABS = [i for i in range(1, 40) if i not in (1, 9, 25)]
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


ck("unita' tradotte 39/39", len(cov) == 39 == len(units) and not missing, '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
kk = collections.Counter(u['kind'] for u in units)
ck('tipi: 39 MISSION_TEXT', dict(kk) == {'MISSION_TEXT': 39}, dict(kk))
ck('0 UI_LABEL nel sorgente (premessa)', not [u for u in units if u['kind'] == 'UI_LABEL'],
   [u['idx'] for u in units if u['kind'] == 'UI_LABEL'])
for k in ('TEXT', 'VALUE', 'DESCRIPTION', 'UI_LABEL', 'LOGBOOK', 'DIALOG', 'CONVERSATION'):
    ck('%s assente' % k, not [u for u in cov if u['kind'] == k])
ck('tutte tradotte (nessuna identica)', all(v['italian'].strip() != v['english'].strip() for v in cov),
   [v['idx'] for v in cov if v['italian'].strip() == v['english'].strip()])
grd = {}
for v in cov:
    grd.setdefault(v['english'], []).append(v['idx'])
dups = sorted(tuple(x) for x in grd.values() if len(x) > 1)
ck('3 ripetizioni: 20/37, 27/31, 29/39', dups == [(20, 37), (27, 31), (29, 39)], dups)
ck('ogni gruppo reso identico',
   by[20]['italian'] == by[37]['italian'] and by[27]['italian'] == by[31]['italian']
   and by[29]['italian'] == by[39]['italian'])
ck('nessun altro duplicato italiano',
   sorted(c for c in collections.Counter(v['italian'] for v in cov).values() if c > 1) == [2, 2, 2],
   sorted(c for c in collections.Counter(v['italian'] for v in cov).values() if c > 1))
ck('28 e 32 differiscono per una virgola',
   by[32]['italian'].count(',') == by[28]['italian'].count(',') + 1
   and 'meme e nessuno' in by[28]['italian'] and 'meme, e nessuno' in by[32]['italian'])
ctxs = []
for u in units:
    if u['context'] not in ctxs:
        ctxs.append(u['context'])
ck('3 contesti in ordine di riga', len(ctxs) == 3 and ctxs[0].endswith('Theater Chat')
   and ctxs[1].endswith('Musical Entertainment Expo') and ctxs[2].endswith('The Meme Wars 1'),
   [c.split(':', 1)[1] for c in ctxs])
ck('tab: 36, nelle unita attese', [v['idx'] for v in cov if v['italian'].startswith('\t')] == TABS,
   [v['idx'] for v in cov if v['italian'].startswith('\t')])
ck('tab per unita', not [v for v in cov if v['english'].count('\t') != v['italian'].count('\t')],
   [(v['idx'], v['english'].count('\t'), v['italian'].count('\t')) for v in cov
    if v['english'].count('\t') != v['italian'].count('\t')])
ck('virgolette: 58 = 58',
   sum(v['english'].count('"') for v in cov) == sum(v['italian'].count('"') for v in cov) == 58,
   (sum(v['english'].count('"') for v in cov), sum(v['italian'].count('"') for v in cov)))
ck('virgolette per unita', not [v for v in cov if v['english'].count('"') != v['italian'].count('"')])
ck('nessuna virgoletta dispari', [v['idx'] for v in cov if v['italian'].count('"') % 2] == [])
tk_e = [t for v in cov for t in TAGS.findall(v['english'])]
tk_i = [t for v in cov for t in TAGS.findall(v['italian'])]
ck('token: 1 = 1 (<destination>, unita 7)',
   tk_e == tk_i == ['<destination>'] and '<destination>' in by[7]['italian'],
   (collections.Counter(tk_e), collections.Counter(tk_i)))
ck('quadre: 3 coppie nell\'unita 30 (voce del traduttore)',
   sum(v['english'].count('[') for v in cov) == sum(v['italian'].count('[') for v in cov) == 3
   and sum(v['english'].count(']') for v in cov) == sum(v['italian'].count(']') for v in cov) == 3
   and [v['idx'] for v in cov if '[' in v['italian']] == [30],
   (sum(v['italian'].count('[') for v in cov), [v['idx'] for v in cov if '[' in v['italian']]))
ck('backtick: 0', not [v for v in cov if '`' in v['italian']])
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
