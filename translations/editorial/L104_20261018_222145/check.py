r"""check.py — L104 (data/quarg/quarg missions.txt, 27 unita', righe 250-334)

**27 `MISSION_TEXT`**, 0 `UI_LABEL`, 0 `VALUE`. **24 tab** (senza tab 1, 12, 13). **37 virgolette**, con
**cinque citazioni aperte e non chiuse** (unita' 5, 19, 22, 23, 24): il discorso del Quarg continua nell'unita'
successiva. Ogni unita' ha il numero di virgolette del sorgente e **nessuna di quelle cinque finisce con una
virgoletta**. **0 token**, **0 quadre**, **nessuna ripetizione**.

L'unita' 23 conserva il trattino isolato del sorgente (`umano - quale arma`): non e' un em dash.
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
TABS = [i for i in range(1, 28) if i not in (1, 12, 13)]
OPEN = [5, 19, 22, 23, 24]
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


ck("unita' tradotte 27/27", len(cov) == 27 == len(units) and not missing, '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
kk = collections.Counter(u['kind'] for u in units)
ck('tipi: 27 MISSION_TEXT', dict(kk) == {'MISSION_TEXT': 27}, dict(kk))
for k in ('TEXT', 'VALUE', 'DESCRIPTION', 'LOGBOOK', 'UI_LABEL', 'DIALOG', 'CONVERSATION'):
    ck('%s assente' % k, not [u for u in cov if u['kind'] == k])
ck("tutte tradotte salvo l'unita 3, identica per coincidenza linguistica: (No.) = (No.)",
   [v['idx'] for v in cov if v['italian'].strip() == v['english'].strip()] == [3]
   and by[3]['italian'].strip() == '(No.)',
   [v['idx'] for v in cov if v['italian'].strip() == v['english'].strip()])
grd = {}
for v in cov:
    grd.setdefault(v['english'], []).append(v['idx'])
dups = sorted(tuple(x) for x in grd.values() if len(x) > 1)
ck('nessuna ripetizione (asserita vuota)', dups == [], dups)
odd = [v['idx'] for v in cov if v['english'].count('"') % 2 or v['italian'].count('"') % 2]
ck('cinque citazioni aperte: 5, 19, 22, 23, 24', odd == OPEN, odd)
ck('ognuna ha il numero di virgolette del sorgente',
   [by[i]['italian'].count('"') for i in OPEN] == [by[i]['english'].count('"') for i in OPEN] == [3, 1, 1, 1, 1],
   [by[i]['italian'].count('"') for i in OPEN])
ck('nessuna delle cinque finisce con una virgoletta',
   all(not by[i]['italian'].rstrip().endswith('"') for i in OPEN))
ctxs = []
for u in units:
    if u['context'] not in ctxs:
        ctxs.append(u['context'])
ck('2 contesti in ordine di riga',
   len(ctxs) == 2 and [c.split(':', 1)[1] for c in ctxs]
   == ['Ask Quarg About Coalition Early', 'Quarg Pug Arfecta Warning'],
   [c.split(':', 1)[1] for c in ctxs])
ck('tab: 24, nelle unita attese', [v['idx'] for v in cov if v['italian'].startswith('\t')] == TABS,
   [v['idx'] for v in cov if v['italian'].startswith('\t')])
ck('tab per unita', not [v for v in cov if v['english'].count('\t') != v['italian'].count('\t')])
ck('virgolette: 37 = 37',
   sum(v['english'].count('"') for v in cov) == sum(v['italian'].count('"') for v in cov) == 37,
   (sum(v['english'].count('"') for v in cov), sum(v['italian'].count('"') for v in cov)))
ck('virgolette per unita', not [v for v in cov if v['english'].count('"') != v['italian'].count('"')],
   [(v['idx'], v['english'].count('"'), v['italian'].count('"')) for v in cov
    if v['english'].count('"') != v['italian'].count('"')])
ck('unita 23: trattino isolato, non em dash', ' - ' in by[23]['italian'] and '\u2014' not in by[23]['italian'])
ck('zero token (asserito)', not [v for v in cov if TAGS.search(v['english']) or TAGS.search(v['italian'])])
ck('zero quadre e zero backtick', not [v for v in cov if any(c in v['italian'] for c in '[]`')])
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
