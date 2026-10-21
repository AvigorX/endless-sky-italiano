r"""check.py — L90 (data/successors/successor culture conversations.txt, 34 unita', righe 1-142)

**34 `MISSION_TEXT`**, nessun altro tipo. **28 tab** (3-10, 13-16, 19-34), **2 virgolette** (unita' 23),
**3 token** `<ship>` (1, 10, 18), 6 contesti. Finestra ridotta rispetto a HANDOFF_L90 (76 unita' / 2583
parole): un lotto verificabile a quattro parti avrebbe superato il budget di questa sessione; il resto e'
dichiarato in HANDOFF_L91.
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
TABS = [i for i in range(3, 11)] + [13, 14, 15, 16] + list(range(19, 35))
out = {'block': src['block'], 'note': src['note'], 'units': []}
for u in units:
    if u['idx'] not in tr:
        continue
    it = '\t' * (len(u['english']) - len(u['english'].lstrip('\t'))) + tr[u['idx']]
    out['units'].append({"idx": u['idx'], "id": u['id'], "path": u['path'], "line": u['line'],
                         "kind": u['kind'], "context": u['context'], "english": u['english'],
                         "italian": it, "ratio": round(len(it) / max(1, len(u['english'])), 3)})
open(os.path.join(HERE, 'translation.json'), 'w', encoding='utf-8').write(json.dumps(out, ensure_ascii=False, indent=1))
cov = out['units']
TAGS = re.compile(r'<[^<>]+>')
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 34/34", len(cov) == 34 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
kk = collections.Counter(u['kind'] for u in units)
ck('tipi: 34 MISSION_TEXT', dict(kk) == {'MISSION_TEXT': 34}, dict(kk))
for k in ('TEXT', 'VALUE', 'DESCRIPTION', 'UI_LABEL', 'LOGBOOK', 'DIALOG', 'CONVERSATION'):
    ck('%s assente' % k, not [u for u in cov if u['kind'] == k])
ck('tutte tradotte (nessuna identica)', all(v['italian'].strip() != v['english'].strip() for v in cov),
   [v['idx'] for v in cov if v['italian'].strip() == v['english'].strip()])
grd = {}
for v in cov:
    grd.setdefault(v['english'], []).append(v['idx'])
dups = [tuple(x) for x in grd.values() if len(x) > 1]
ck('ripetizioni inglesi: 3/13 e 26/31', dups == [(3, 13), (26, 31)], dups)
ck('3/13: stesso inglese, genere diverso (bastone/nave-sfera)',
   cov[2]['italian'][:-3] == cov[12]['italian'][:-3] and (cov[2]['italian'][-3], cov[12]['italian'][-3]) == ('o', 'a'),
   (cov[2]['italian'], cov[12]['italian']))
ck('26/31: rese identiche', cov[25]['italian'] == cov[30]['italian'])
ck('nessun altro duplicato italiano',
   [c for c in collections.Counter(v['italian'] for v in cov).values() if c > 1] == [2])
ck('6 contesti', len(set(u['context'] for u in units)) == 6)
ck('tab: 28, nelle unita attese', [v['idx'] for v in cov if v['italian'].startswith('\t')] == TABS)
ck('tab per unita', not [v for v in cov if v['english'].count('\t') != v['italian'].count('\t')],
   [(v['idx'], v['english'].count('\t'), v['italian'].count('\t')) for v in cov
    if v['english'].count('\t') != v['italian'].count('\t')])
ck('virgolette: 2 = 2 (unita 23)',
   sum(v['english'].count('"') for v in cov) == sum(v['italian'].count('"') for v in cov) == 2)
ck('la virgoletta si apre e chiude nella stessa unita',
   [v['idx'] for v in cov if v['italian'].count('"') % 2] == [])
ck('token <ship>: 3 = 3', sum(len(TAGS.findall(v['english'])) for v in cov) == 3
   and sum(len(TAGS.findall(v['italian'])) for v in cov) == 3,
   (sum(len(TAGS.findall(v['english'])) for v in cov), sum(len(TAGS.findall(v['italian'])) for v in cov)))
ck('il token resta il segnaposto originale',
   all(TAGS.findall(v['english']) == TAGS.findall(v['italian']) for v in cov),
   [(v['idx'], TAGS.findall(v['english']), TAGS.findall(v['italian'])) for v in cov
    if TAGS.findall(v['english']) != TAGS.findall(v['italian'])])
ck('quadre/backtick: 0', not [v for v in cov if '[' in v['italian'] or '`' in v['italian']])
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
