r"""check.py — L107 (data/korath/korath missions.txt, 38 unita', righe 121-212)

**Tre contesti**: coda di `Setar Fort Heating` (126-127), `Korath Family to Ringworld` (130-169),
`Korath Livestock` (172-212).

**34 `MISSION_TEXT` + 2 `VALUE` + 2 `DESCRIPTION`**. I `VALUE` (3, 20) restano **identici**: sono nomi di
missione con `<planet>` dentro. Le `DESCRIPTION` (4, 21) sono **tradotte** per intero.

**29 tab** (senza tab 1, 3, 4, 5, 14, 20, 21, 22, 37). **20 virgolette**, tutte binate: **zero citazioni
aperte**. **Zero quadre** e **zero ripetizioni** — asseriti vuoti, non omessi: il lotto precedente aveva 16 coppie
di quadre e una citazione aperta. **21 token** in sei famiglie, fra cui `<bunks>` (nuovo) distinto da `<tons>`.
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
NOTAB = [1, 3, 4, 5, 14, 20, 21, 22, 37]
TABS = [i for i in range(1, 39) if i not in NOTAB]
VALS = [3, 20]
DESC = [4, 21]
FAM = {'<planet>': 12, '<bunks>': 3, '<payment>': 2, '<destination>': 2, '<cargo>': 1, '<tons>': 1}
CTX = ['mission:Setar Fort Heating', 'mission:Korath Family to Ringworld', 'mission:Korath Livestock']
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


ck("unita' tradotte 38/38", len(cov) == 38 == len(units) and not missing, '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
kk = collections.Counter(u['kind'] for u in units)
ck('tipi: 34 MISSION_TEXT + 2 VALUE + 2 DESCRIPTION',
   dict(kk) == {'MISSION_TEXT': 34, 'VALUE': 2, 'DESCRIPTION': 2}, dict(kk))
ck('i due VALUE restano identici, con <planet> dentro',
   [v['idx'] for v in cov if v['italian'].strip() == v['english'].strip() and v['kind'] == 'VALUE'] == VALS
   and by[3]['italian'].strip() == 'Korath to <planet>'
   and by[20]['italian'].strip() == 'Livestock to <planet>', (by[3]['italian'], by[20]['italian']))
ck('le due DESCRIPTION sono tradotte',
   all(by[i]['italian'].strip() != by[i]['english'].strip() for i in DESC)
   and by[4]['italian'].startswith('Una famiglia Korath') and by[21]['italian'].startswith('Trasporta'))
ck('unica altra unita identica: la 10 `(No.)`',
   [v['idx'] for v in cov if v['italian'].strip() == v['english'].strip()] == sorted(VALS + [10])
   and by[10]['italian'].strip() == '(No.)',
   [v['idx'] for v in cov if v['italian'].strip() == v['english'].strip()])
for k in ('TEXT', 'LOGBOOK', 'UI_LABEL', 'DIALOG', 'CONVERSATION'):
    ck('%s assente' % k, not [u for u in cov if u['kind'] == k])
ck('tre contesti in ordine di riga', [c for c in CTX] == list(dict.fromkeys(u['context'] for u in units)),
   [u['context'] for u in units][:3])
ck('tab: 29, nelle unita attese', [v['idx'] for v in cov if v['italian'].startswith('\t')] == TABS,
   [v['idx'] for v in cov if v['italian'].startswith('\t')])
ck('tab per unita', not [v for v in cov if v['english'].count('\t') != v['italian'].count('\t')])
ck('virgolette: 20 = 20',
   sum(v['english'].count('"') for v in cov) == sum(v['italian'].count('"') for v in cov) == 20,
   (sum(v['english'].count('"') for v in cov), sum(v['italian'].count('"') for v in cov)))
ck('virgolette per unita', not [v for v in cov if v['english'].count('"') != v['italian'].count('"')])
ck('ZERO citazioni aperte (asserito vuoto)',
   not [v['idx'] for v in cov if v['italian'].count('"') % 2],
   [v['idx'] for v in cov if v['italian'].count('"') % 2])
ck('ZERO quadre (asserito vuoto)', not [v['idx'] for v in cov if '[' in v['italian'] or ']' in v['italian']])
tk_e = [t for v in cov for t in TAGS.findall(v['english'])]
tk_i = [t for v in cov for t in TAGS.findall(v['italian'])]
ck('token: 21 = 21 in sei famiglie',
   tk_e == tk_i and collections.Counter(tk_e) == FAM and len(tk_e) == 21,
   (len(tk_e), collections.Counter(tk_e)))
ck('<bunks> distinto da <tons>: 3 contro 1, in unita diverse',
   [v['idx'] for v in cov if '<bunks>' in v['english']] == [4, 21, 31]
   and [v['idx'] for v in cov if '<tons>' in v['english']] == [31])
ck('unita 31 ha entrambi i token', '<tons>' in by[31]['italian'] and '<bunks>' in by[31]['italian'])
ck('nessun backtick', not [v for v in cov if '`' in v['italian']])
grd = {}
for v in cov:
    grd.setdefault(v['english'], []).append(v['idx'])
ck('ZERO ripetizioni (asserito vuoto)', not [x for x in grd.values() if len(x) > 1],
   [x for x in grd.values() if len(x) > 1])
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
