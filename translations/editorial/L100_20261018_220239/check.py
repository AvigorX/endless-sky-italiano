r"""check.py — L100 (data/hai/hai culture conversations.txt, 44 unita', righe 212-320)

**41 `MISSION_TEXT` + 3 `UI_LABEL`**: `field trip` (5), `pleasant lunch` (12), `finishing chat` (14), lasciate
**identiche** al sorgente e asserite una per una. **39 tab** (senza tab 1, 5, 12, 14, 28). **40 virgolette**, con
**quattro citazioni aperte e non chiuse** (unita' 23, 24, 39, 41): il discorso continua nell'unita' successiva.
**1 token**: `<last>` (unita' 40). **Zero quadre**. **Nessuna ripetizione** (asserita vuota). **2 contesti**.
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
TABS = [i for i in range(1, 45) if i not in (1, 5, 12, 14, 28)]
LABELS = {5: 'field trip', 12: 'pleasant lunch', 14: 'finishing chat'}
OPEN = [23, 24, 39, 41]
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


ck("unita' tradotte 44/44", len(cov) == 44 == len(units) and not missing, '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
kk = collections.Counter(u['kind'] for u in units)
ck('tipi: 41 MISSION_TEXT + 3 UI_LABEL', dict(kk) == {'MISSION_TEXT': 41, 'UI_LABEL': 3}, dict(kk))
ck('le 3 UI_LABEL restano identiche (etichette di salto)',
   [i for i in LABELS if by[i]['italian'] == by[i]['english']] == list(LABELS)
   and all(by[i]['italian'].strip() == LABELS[i] for i in LABELS),
   [(i, by[i]['italian']) for i in LABELS])
for k in ('TEXT', 'VALUE', 'DESCRIPTION', 'LOGBOOK', 'DIALOG', 'CONVERSATION'):
    ck('%s assente' % k, not [u for u in cov if u['kind'] == k])
ck('nessuna riga tradotta identica salvo le 3 etichette',
   [v['idx'] for v in cov if v['italian'].strip() == v['english'].strip()] == list(LABELS),
   [v['idx'] for v in cov if v['italian'].strip() == v['english'].strip()])
grd = {}
for v in cov:
    grd.setdefault(v['english'], []).append(v['idx'])
dups = sorted(tuple(x) for x in grd.values() if len(x) > 1)
ck('nessuna ripetizione (asserita vuota)', dups == [], dups)
odd = [v['idx'] for v in cov if v['english'].count('"') % 2 or v['italian'].count('"') % 2]
ck('citazioni aperte e non chiuse: 23, 24, 39, 41', odd == OPEN, odd)
ck('le quattro unita hanno lo stesso numero di virgolette del sorgente (1, 1, 3, 1)',
   [by[i]['italian'].count('"') for i in OPEN] == [by[i]['english'].count('"') for i in OPEN] == [1, 1, 3, 1],
   [by[i]['italian'].count('"') for i in OPEN])
ck('le quattro citazioni restano aperte a fine unita',
   all(not by[i]['italian'].rstrip().endswith('"') for i in OPEN),
   [(i, by[i]['italian'][-30:]) for i in OPEN])
ck('unita 25 e 43: virgolette pari al sorgente (4 e 2)',
   by[25]['italian'].count('"') == by[25]['english'].count('"') == 4
   and by[43]['italian'].count('"') == by[43]['english'].count('"') == 2,
   (by[25]['italian'].count('"'), by[43]['italian'].count('"')))
ctxs = []
for u in units:
    if u['context'] not in ctxs:
        ctxs.append(u['context'])
ck('2 contesti in ordine di riga',
   len(ctxs) == 2 and [c.split(':', 1)[1] for c in ctxs] == ['Academy Motto', 'Robotic Musical 1'],
   [c.split(':', 1)[1] for c in ctxs])
ck('tab: 39, nelle unita attese', [v['idx'] for v in cov if v['italian'].startswith('\t')] == TABS,
   [v['idx'] for v in cov if v['italian'].startswith('\t')])
ck('tab per unita', not [v for v in cov if v['english'].count('\t') != v['italian'].count('\t')])
ck('virgolette: 40 = 40',
   sum(v['english'].count('"') for v in cov) == sum(v['italian'].count('"') for v in cov) == 40,
   (sum(v['english'].count('"') for v in cov), sum(v['italian'].count('"') for v in cov)))
ck('virgolette per unita', not [v for v in cov if v['english'].count('"') != v['italian'].count('"')],
   [(v['idx'], v['english'].count('"'), v['italian'].count('"')) for v in cov
    if v['english'].count('"') != v['italian'].count('"')])
tk_e = [t for v in cov for t in TAGS.findall(v['english'])]
tk_i = [t for v in cov for t in TAGS.findall(v['italian'])]
ck('token: 1 = 1 (<last>, unita 40)', tk_e == tk_i == ['<last>'] and '<last>' in by[40]['italian'],
   (collections.Counter(tk_e), collections.Counter(tk_i)))
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
