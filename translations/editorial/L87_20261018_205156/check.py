r"""check.py — L87 (data/successors/successor outfits.txt, 13 unita', righe 241-420)

Tipi: **12 `DESCRIPTION` + 1 `VALUE`** (unita' 10, `"Niis" Inductive Engines`: dato, identico).
**3 tab** (unita' 2, 7, 9), 2 virgolette, 0 dispari, 0 token, 0 duplicati.
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
DATA, PROSE, TABS = {10}, {1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13}, [2, 7, 9]
lo, hi = 1, len(units)
if '--range' in sys.argv:
    i = sys.argv.index('--range')
    lo, hi = int(sys.argv[i + 1]), int(sys.argv[i + 2])

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
cov = [by[u['idx']] for u in units if lo <= u['idx'] <= hi and u['idx'] in by]
TAGS = re.compile(r'<[^<>]+>')
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 13/13", len(cov) == 13 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
kk = collections.Counter(u['kind'] for u in units)
ck('tipi: 12 DESCRIPTION + 1 VALUE', dict(kk) == {'DESCRIPTION': 12, 'VALUE': 1}, dict(kk))
for k in ('TEXT', 'MISSION_TEXT', 'UI_LABEL', 'LOGBOOK', 'DIALOG', 'CONVERSATION'):
    ck('%s assenti' % k, not [u for u in cov if u['kind'] == k])
ck('il VALUE resta identico', by[10]['italian'] == by[10]['english'] == '"Niis" Inductive Engines')
ck('le 12 DESCRIPTION sono tradotte',
   all(by[i]['italian'].strip() != by[i]['english'].strip() for i in PROSE),
   [i for i in sorted(PROSE) if by[i]['italian'].strip() == by[i]['english'].strip()])
ctxs = []
for u in units:
    if u['context'] not in ctxs:
        ctxs.append(u['context'])
ck('9 contesti in ordine di riga', ctxs[0] == 'outfit:"Ryuit" Fusion Core'
   and ctxs[-1] == 'outfit:"Aqra" Inductive Steering' and len(ctxs) == 9, '%d · %s' % (len(ctxs), ctxs[0]))
ck('nessun duplicato italiano', not [c for c in collections.Counter(v['italian'] for v in cov).values() if c > 1])
ck('tab: solo unita 2, 7, 9', [v['idx'] for v in cov if v['italian'].startswith('\t')] == TABS)
ck('tab per unita', not [v for v in cov if v['english'].count('\t') != v['italian'].count('\t')])
ck('virgolette: 2 = 2',
   sum(v['english'].count('"') for v in cov) == sum(v['italian'].count('"') for v in cov) == 2)
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
for n, b, ok in rows:
    print('| %s | %s | %s |' % (n, b, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d' % (sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('righe %d/%d · parti %d · mancanti %d' % (min(u['line'] for u in units), max(u['line'] for u in units),
      len(parts), len([u for u in units if u['idx'] not in tr])))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
