r"""check.py — L106 (data/korath/korath missions.txt, 25 unita', righe 1-120)

**Quattro tipi**: 22 `MISSION_TEXT`, 1 `LOGBOOK` (unita' 5), 1 `VALUE` (unita' 6: `Supplies to <planet>` —
**identico**, e' il nome della missione) e 1 `DESCRIPTION` (unita' 7, tradotta).

**17 tab** (senza tab 1-8). **45 virgolette** con **una citazione aperta** (unita' 16). **13 token** in sei
famiglie. **16 coppie di quadre** nelle unita' 11 (3), 16 (7), 17 (1), 20 (4), 25 (1): sono la voce dei Wanderer,
che elenca **due rese possibili** — si traducono entrambe, la struttura resta. **Due ripetizioni**: 2/3/4, 15/19.
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
TABS = [i for i in range(1, 26) if i not in (1, 2, 3, 4, 5, 6, 7, 8)]
BR = {11: 3, 16: 7, 17: 1, 20: 4, 25: 1}
GROUPS = [(2, 3, 4), (15, 19)]
FAM = {'<planet>': 4, '<payment>': 4, '<last>': 2, '<cargo>': 1, '<destination>': 1, '<tons>': 1}
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


ck("unita' tradotte 25/25", len(cov) == 25 == len(units) and not missing, '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
kk = collections.Counter(u['kind'] for u in units)
ck('tipi: 22 MISSION_TEXT + 1 LOGBOOK + 1 VALUE + 1 DESCRIPTION',
   dict(kk) == {'MISSION_TEXT': 22, 'LOGBOOK': 1, 'VALUE': 1, 'DESCRIPTION': 1}, dict(kk))
ck('il VALUE (unita 6) resta identico: nome di missione',
   by[6]['kind'] == 'VALUE' and by[6]['italian'].strip() == by[6]['english'].strip() == 'Supplies to <planet>',
   by[6]['italian'])
ck('il LOGBOOK (unita 5) e tradotto per intero',
   by[5]['kind'] == 'LOGBOOK' and by[5]['italian'].strip() != by[5]['english'].strip()
   and by[5]['italian'].startswith('I Korath sono') and len(by[5]['italian']) > 400)
ck('la DESCRIPTION (unita 7) e tradotta', by[7]['kind'] == 'DESCRIPTION'
   and by[7]['italian'].strip() != by[7]['english'].strip())
for k in ('TEXT', 'DIALOG', 'UI_LABEL', 'CONVERSATION'):
    ck('%s assente' % k, not [u for u in cov if u['kind'] == k])
ck('nessuna riga identica salvo il VALUE',
   [v['idx'] for v in cov if v['italian'].strip() == v['english'].strip()] == [6],
   [v['idx'] for v in cov if v['italian'].strip() == v['english'].strip()])
grd = {}
for v in cov:
    grd.setdefault(v['english'], []).append(v['idx'])
dups = sorted(tuple(x) for x in grd.values() if len(x) > 1)
ck('2 ripetizioni: 2/3/4 e 15/19', dups == GROUPS, dups)
ck('ogni gruppo reso identico', all(len({by[i]['italian'] for i in g}) == 1 for g in GROUPS))
ck('la 1 differisce dalle 2/3/4 (stazione, non spazioporto)',
   by[1]['italian'] != by[2]['italian'] and 'stazione' in by[1]['italian'])
odd = [v['idx'] for v in cov if v['english'].count('"') % 2 or v['italian'].count('"') % 2]
ck('una citazione aperta: unita 16', odd == [16], odd)
ck('unita 16: una sola virgoletta e non finisce con virgoletta',
   by[16]['italian'].count('"') == 1 and not by[16]['italian'].rstrip().endswith('"'))
ck('quadre: 16 coppie, nelle unita attese',
   {i: by[i]['italian'].count('[') for i in BR} == BR
   and sum(by[i]['italian'].count('[') for i in BR) == 16
   and [v['idx'] for v in cov if '[' in v['italian']] == sorted(BR),
   {i: by[i]['italian'].count('[') for i in BR})
ck('ogni coppia contiene DUE alternative (virgola o punto interrogativo)',
   all(',' in f or '?' in f for i in BR for f in re.findall(r'\[([^\]]*)\]', by[i]['italian'])),
   [(i, f) for i in BR for f in re.findall(r'\[([^\]]*)\]', by[i]['italian']) if ',' not in f and '?' not in f])
ck('quadre bilanciate', sum(v['italian'].count('[') for v in cov) == sum(v['italian'].count(']') for v in cov) == 16)
ctxs = []
for u in units:
    if u['context'] not in ctxs:
        ctxs.append(u['context'])
ck('6 contesti in ordine di riga',
   len(ctxs) == 6 and len(ctxs) == 5 + 1 and ctxs[-1].endswith('Setar Fort Heating')
   and ctxs[0].endswith('First Contact: Korati Efreti'),
   [c.split(':', 1)[1] for c in ctxs])
ck('tab: 17, nelle unita attese', [v['idx'] for v in cov if v['italian'].startswith('\t')] == TABS,
   [v['idx'] for v in cov if v['italian'].startswith('\t')])
ck('tab per unita', not [v for v in cov if v['english'].count('\t') != v['italian'].count('\t')])
ck('virgolette: 45 = 45',
   sum(v['english'].count('"') for v in cov) == sum(v['italian'].count('"') for v in cov) == 45,
   (sum(v['english'].count('"') for v in cov), sum(v['italian'].count('"') for v in cov)))
ck('virgolette per unita', not [v for v in cov if v['english'].count('"') != v['italian'].count('"')])
tk_e = [t for v in cov for t in TAGS.findall(v['english'])]
tk_i = [t for v in cov for t in TAGS.findall(v['italian'])]
ck('token: 13 = 13 in sei famiglie',
   tk_e == tk_i and collections.Counter(tk_e) == FAM and len(tk_e) == 13,
   (collections.Counter(tk_e), collections.Counter(tk_i)))
ck('token identici per unita e nello stesso ordine',
   all(TAGS.findall(v['english']) == TAGS.findall(v['italian']) for v in cov))
ck('nessun backtick', not [v for v in cov if '`' in v['italian']])
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
