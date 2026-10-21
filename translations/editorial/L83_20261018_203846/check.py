r"""check.py — L83 (data/successors/predecessors.txt, 11 unita', righe 401-520)

Terzo lotto sulle schede: 4 contesti (`outfit:"Torji," Lethal Sight`, `outfit:Crimson Halo`,
`outfit:Visions of Rime`, `ship:Valkkyiara-Khorasaqra`). **7 `TEXT` + 3 `DESCRIPTION` + 1 `VALUE`**;
**8 unita' di dato** identiche (4-11), **3 di prosa** tradotte (1-3); 0 tab, 12 virgolette, 0 dispari,
0 token, 0 duplicati.
"""
import collections, json, os, re, sqlite3, sys

HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
units = src['units']
tr = {}
parts = sorted(f for f in os.listdir(os.path.join(HERE, 'parts')) if f.endswith('.json'))
for p in parts:
    for k, v in json.load(open(os.path.join(HERE, 'parts', p), encoding='utf-8')).items():
        tr[int(k)] = v
DATA, PROSE = {4, 5, 6, 7, 8, 9, 10, 11}, {1, 2, 3}
en = collections.Counter(u['english'] for u in units)
DUP = {k: [u['idx'] for u in units if u['english'] == k] for k, v in en.items() if v > 1}

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
allc = list(by.values())
TAGS = re.compile(r'<[^<>]+>')
rows = []
rows.append(('unita\' tradotte', '%d/%d' % (len(cov), len(units)), len(cov) == len(units)))
rows.append(('traduzioni vuote', [v['idx'] for v in cov if not v['italian'].strip()] or 0,
             all(v['italian'].strip() for v in cov)))
K = {'TEXT': 7, 'DESCRIPTION': 3, 'VALUE': 1}
kk = collections.Counter(u['kind'] for u in units)
rows.append(('tipi (7 TEXT + 3 DESCRIPTION + 1 VALUE)', dict(kk), dict(kk) == K))
for k in ('MISSION_TEXT', 'UI_LABEL', 'LOGBOOK', 'DIALOG', 'CONVERSATION'):
    g = tuple(sorted(v['idx'] for v in cov if v['kind'] == k))
    rows.append(('%s (0 attesi)' % k, g or 0, g == ()))
rows.append(('8 unita di dato identiche (4-11)',
             [i for i in sorted(DATA) if by[i]['italian'] != by[i]['english']] or 'ok',
             all(by[i]['italian'] == by[i]['english'] for i in DATA)))
rows.append(('3 unita di prosa tradotte (1-3)',
             [i for i in sorted(PROSE) if by[i]['italian'].strip() == by[i]['english'].strip()] or 'ok',
             all(by[i]['italian'].strip() != by[i]['english'].strip() for i in PROSE)))
di = [(k[:40], c) for k, c in collections.Counter(v['italian'] for v in cov).items() if c > 1]
rows.append(('duplicati italiano non spiegati', di or 'ok', not di))
rows.append(('duplicati inglesi (0 attesi)', len(DUP), not DUP))
rows.append(('tab (0 attesi)', [v['idx'] for v in cov if '\t' in v['italian']] or 0,
             not [v['idx'] for v in cov if '\t' in v['italian']]))
rows.append(('virgolette per unita', [(v['idx'], v['english'].count('"'), v['italian'].count('"'))
             for v in cov if v['english'].count('"') != v['italian'].count('"')] or 'ok',
             not [v['idx'] for v in cov if v['english'].count('"') != v['italian'].count('"')]))
rows.append(('virgolette dispari (0 attese)', [v['idx'] for v in cov if v['english'].count('"') % 2] or 0,
             not [v['idx'] for v in cov if v['english'].count('"') % 2]))
rows.append(('quadre/backtick (0 attesi)',
             [v['idx'] for v in cov if '[' in v['italian'] or '`' in v['italian']] or 'ok',
             not [v['idx'] for v in cov if '[' in v['italian'] or '`' in v['italian']]))
tok = sum(len(TAGS.findall(v['english'])) + len(TAGS.findall(v['italian'])) for v in allc)
rows.append(('token: 0 = 0', str(tok), tok == 0))
rs = [v['ratio'] for v in cov]
for v in cov:
    if not 0.55 < v['ratio'] < 1.90:
        print('OUTLIER', v['idx'], v['ratio'])
rows.append(('rapporto nel gate 0,55-1,90', '%.2f - %.2f' % (min(rs), max(rs)),
             0.55 < min(rs) and max(rs) < 1.90))
bad = [(v['idx'], n) for v in cov for p, n in ((r"\b(e|piu|perche|cosi|gia|puo|cioe|percio)'", 'accento'),
       ('\u2026', 'ellissi'), ('\u2014', 'em dash'), ('\u2019', 'apostrofo curvo')) if re.search(p, v['italian'])]
rows.append(('tipografia', bad or 'ok', not bad))
nonlat = [v['idx'] for v in cov for c in v['italian'] if ord(c) > 127 and not 0x00C0 <= ord(c) <= 0x024F]
rows.append(('caratteri non latini', nonlat or 'ok', not nonlat))
c = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
st = dict(c.execute('select state,count(*) from units group by state').fetchall())
rows.append(('state.db APPROVED/PENDING', '%s/%s' % (st['APPROVED'], st['PENDING']), st['APPROVED'] == 364))
ids = [u['id'] for u in units]
dl = c.execute('select count(*) from units where id in (%s) and state != "PENDING"' % ','.join('?' * len(ids)), ids).fetchone()[0]
rows.append(('unita del lotto fuori da PENDING', dl, dl == 0))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for a, b, ok in rows:
    print('| %s | %s | %s |' % (a, b, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d' % (sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('virgolette IT %d / EN %d' % (sum(v['italian'].count('"') for v in cov), sum(v['english'].count('"') for v in cov)))
print('righe %d/%d · parti %d · mancanti %d' % (min(u['line'] for u in units), max(u['line'] for u in units),
      len(parts), len([u for u in units if u['idx'] not in tr])))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
