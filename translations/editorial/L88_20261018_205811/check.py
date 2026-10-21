r"""check.py — L88 (data/successors/successor outfits.txt, 10 unita', righe 421-560)

**10 `DESCRIPTION`, nessun dato.** Il messaggio «Because a reverse thruster must be facing forwards...» e'
identico alle unita' **2, 6, 10**: duplicato legittimo, reso identico di proposito. **3 tab** (2, 6, 10),
**0 virgolette**, 0 token, 7 contesti.
"""
import collections, json, os, re, sqlite3, sys

HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
units = sorted(src['units'], key=lambda x: x['line'])
tr = {}
parts = sorted(f for f in os.listdir(os.path.join(HERE, 'parts')) if f.endswith('.json'))
for p in parts:
    for k, v in json.load(open(os.path.join(HERE, 'parts', p), encoding='utf-8')).items():
        tr[int(k)] = v
TABS, DUPOK = [2, 6, 10], [2, 6, 10]
lo, hi = 1, len(units)
out = {'block': src['block'], 'note': src['note'], 'units': []}
for u in units:
    if u['idx'] not in tr:
        continue
    it = '\t' * (len(u['english']) - len(u['english'].lstrip('\t'))) + tr[u['idx']]
    out['units'].append({"idx": u['idx'], "id": u['id'], "path": u['path'], "line": u['line'],
                         "kind": u['kind'], "context": u['context'], "english": u['english'],
                         "italian": it, "ratio": round(len(it) / max(1, len(u['english'])), 3)})
open(os.path.join(HERE, 'translation.json'), 'w', encoding='utf-8').write(json.dumps(out, ensure_ascii=False, indent=1))
by = {v['idx']: v for v in out['units']}
cov = out['units']
TAGS = re.compile(r'<[^<>]+>')
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 10/10", len(cov) == 10 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
kk = collections.Counter(u['kind'] for u in units)
ck('tipi: 10 DESCRIPTION, nessun dato', dict(kk) == {'DESCRIPTION': 10}, dict(kk))
for k in ('TEXT', 'VALUE', 'MISSION_TEXT', 'UI_LABEL', 'LOGBOOK', 'DIALOG', 'CONVERSATION'):
    ck('%s assente' % k, not [u for u in cov if u['kind'] == k])
ck('le 10 DESCRIPTION sono tradotte',
   all(v['italian'].strip() != v['english'].strip() for v in cov),
   [v['idx'] for v in cov if v['italian'].strip() == v['english'].strip()])
grp = {}
for v in cov:
    grp.setdefault(v['english'], []).append(v['idx'])
dups = [tuple(x) for x in grp.values() if len(x) > 1]
ck('unica ripetizione inglese: 2/6/10', dups == [(2, 6, 10)], dups)
ck('la ripetizione e resa identica',
   by[2]['italian'] == by[6]['italian'] == by[10]['italian']
   and by[2]['english'] == by[6]['english'] == by[10]['english'])
ctxs = []
for u in units:
    if u['context'] not in ctxs:
        ctxs.append(u['context'])
ck('7 contesti in ordine di riga', len(ctxs) == 7 and ctxs[0] == 'outfit:"Aqra" Inductive Reverser'
   and ctxs[-1] == 'outfit:"Veusa" Inductive Reverser', '%d · %s' % (len(ctxs), ctxs[0]))
ck('tab: solo unita 2, 6, 10', [v['idx'] for v in cov if v['italian'].startswith('\t')] == TABS)
ck('tab per unita', not [v for v in cov if v['english'].count('\t') != v['italian'].count('\t')])
a = sum(v['english'].count('"') for v in cov)
b = sum(v['italian'].count('"') for v in cov)
ck('virgolette: 0 = 0 (il sorgente non ne ha)', a == b == 0, '%d/%d' % (a, b))
ck('virgolette dispari: 0', not [v for v in cov if v['english'].count('"') % 2])
ck('quadre/backtick: 0', not [v for v in cov if '[' in v['italian'] or '`' in v['italian']])
ck('token: 0 = 0', not [v for v in cov if TAGS.search(v['english']) or TAGS.search(v['italian'])])
rs = [v['ratio'] for v in cov]
for v in cov:
    if not 0.55 < v['ratio'] < 1.90:
        print('OUTLIER', v['idx'], v['ratio'], v['english'][:40], '|', v['italian'][:40])
ck('rapporto nel gate', 0.55 < min(rs) and max(rs) < 1.90, '%.2f - %.2f' % (min(rs), max(rs)))
bad = [(v['idx'], n) for v in cov for p, n in ((r"\b(e|piu|perche|cosi|gia|puo|cioe|percio)'", 'accento'),
       ('\u2026', 'ellissi'), ('\u2014', 'em dash'), ('\u2019', 'apostrofo curvo')) if re.search(p, v['italian'])]
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
      len(parts), len([u for u in units if u['idx'] not in tr])))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
