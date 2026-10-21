r"""check.py — L102 (data/quarg/quarg missions.txt, 48 unita', righe 1-117)

Primo lotto del file e **primo `LOGBOOK` della campagna**: le unita' 1 e 2 sono le schede dei **Quarg** e dei
**Drak**. Il controllo qui e' **rovesciato** rispetto a L101: il tipo **deve essere presente**, elencato per
indice, tradotto per intero e non identico al sorgente.

**46 `MISSION_TEXT` + 2 `LOGBOOK`**. **44 tab** (senza tab 1, 2, 3, 28). **98 virgolette**. **2 token** nella
stessa unita' (42): `<first>` e `<last>`. **0 quadre**. **3 ripetizioni**: 17/20, 35/40, 37/38.
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
TABS = [i for i in range(1, 49) if i not in (1, 2, 3, 28)]
GROUPS = [(17, 20), (35, 40), (37, 38)]
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


ck("unita' tradotte 48/48", len(cov) == 48 == len(units) and not missing, '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
kk = collections.Counter(u['kind'] for u in units)
ck('tipi: 46 MISSION_TEXT + 2 LOGBOOK', dict(kk) == {'MISSION_TEXT': 46, 'LOGBOOK': 2}, dict(kk))
ck('i due LOGBOOK sono le unita 1 e 2', [i for i in range(1, 49) if by[i]['kind'] == 'LOGBOOK'] == [1, 2],
   [i for i in range(1, 49) if by[i]['kind'] == 'LOGBOOK'])
ck('LOGBOOK tradotti per intero (non identici, prosa lunga)',
   all(by[i]['italian'].strip() != by[i]['english'].strip() and len(by[i]['italian']) > 200 for i in (1, 2)),
   [(i, len(by[i]['italian'])) for i in (1, 2)])
ck('LOGBOOK: schede di Quarg e Drak',
   by[1]['italian'].startswith('I Quarg sono') and by[2]['italian'].startswith('I Drak sarebbero'))
for k in ('TEXT', 'VALUE', 'DESCRIPTION', 'UI_LABEL', 'DIALOG', 'CONVERSATION'):
    ck('%s assente' % k, not [u for u in cov if u['kind'] == k])
ck('nessuna riga tradotta identica', [v['idx'] for v in cov if v['italian'].strip() == v['english'].strip()] == [],
   [v['idx'] for v in cov if v['italian'].strip() == v['english'].strip()])
grd = {}
for v in cov:
    grd.setdefault(v['english'], []).append(v['idx'])
dups = sorted(tuple(x) for x in grd.values() if len(x) > 1)
ck('3 ripetizioni: 17/20, 35/40, 37/38', dups == GROUPS, dups)
ck('ogni gruppo reso identico', all(len({by[i]['italian'] for i in g}) == 1 for g in GROUPS))
ck('nessun altro duplicato italiano',
   sorted(c for c in collections.Counter(v['italian'] for v in cov).values() if c > 1) == [2, 2, 2],
   sorted(c for c in collections.Counter(v['italian'] for v in cov).values() if c > 1))
ck('nessuna virgoletta dispari', [v['idx'] for v in cov if v['italian'].count('"') % 2] == []
   and [v['idx'] for v in cov if v['english'].count('"') % 2] == [])
ctxs = []
for u in units:
    if u['context'] not in ctxs:
        ctxs.append(u['context'])
ck('2 contesti in ordine di riga',
   len(ctxs) == 2 and [c.split(':', 1)[1] for c in ctxs] == ['First Contact: Quarg', 'First Contact: Kuwaru Efreti'],
   [c.split(':', 1)[1] for c in ctxs])
ck('tab: 44, nelle unita attese', [v['idx'] for v in cov if v['italian'].startswith('\t')] == TABS)
ck('tab per unita', not [v for v in cov if v['english'].count('\t') != v['italian'].count('\t')])
ck('virgolette: 98 = 98',
   sum(v['english'].count('"') for v in cov) == sum(v['italian'].count('"') for v in cov) == 98,
   (sum(v['english'].count('"') for v in cov), sum(v['italian'].count('"') for v in cov)))
ck('virgolette per unita', not [v for v in cov if v['english'].count('"') != v['italian'].count('"')],
   [(v['idx'], v['english'].count('"'), v['italian'].count('"')) for v in cov
    if v['english'].count('"') != v['italian'].count('"')])
tk_e = [t for v in cov for t in TAGS.findall(v['english'])]
tk_i = [t for v in cov for t in TAGS.findall(v['italian'])]
ck('token: 2 = 2 (<first>, <last> nell\'unita 42)', tk_e == tk_i == ['<first>', '<last>']
   and '<first> <last>' in by[42]['italian'], (collections.Counter(tk_e), collections.Counter(tk_i)))
ck('zero quadre (asserite)', not [v for v in cov if any(c in v['italian'] for c in '[]')])
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
