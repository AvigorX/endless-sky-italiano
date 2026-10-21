r"""check.py — L109 (data/korath/korath missions.txt, 33 unita', righe 338-451)

**Quattro contesti**: `Efreti: Distress Call 2` (coda, 338-340), `Distress Call 3` (345-376), `Distress Call 4`
(388-434), `Distress Call 5` (437-451).

**27 `MISSION_TEXT` + 3 `VALUE` + 3 `DESCRIPTION`**. I `VALUE` (4, 16, 29) restano **identici**; le `DESCRIPTION`
(5, 17, 30) sono **tradotte** e distinguono **`<origin>`** (partenza) da **`<destination>`** (arrivo).

**20 tab**, **14 virgolette** tutte binate, **23 token** in sette famiglie (`<EDC-ship>` 11, `<origin>` 2), zero
quadre, zero ripetizioni. I tre quasi-duplicati (20/21/22, 18/19, 24/25) **non** sono identici: differiscono per
soggetto e coda.
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
NOTAB = [1, 4, 5, 6, 16, 17, 18, 19, 26, 29, 30, 31, 32]
TABS = [i for i in range(1, 34) if i not in NOTAB]
VALS = [4, 16, 29]
DESC = [5, 17, 30]
FAM = {'<EDC-ship>': 11, '<destination>': 4, '<origin>': 2, '<planet>': 2, '<bunks>': 2, '<ship>': 1, '<payment>': 1}
CTX = ['mission:Efreti: Distress Call 2', 'mission:Efreti: Distress Call 3',
       'mission:Efreti: Distress Call 4', 'mission:Efreti: Distress Call 5']
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


ck("unita' tradotte 33/33", len(cov) == 33 == len(units) and not missing, '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
kk = collections.Counter(u['kind'] for u in units)
ck('tipi: 27 MISSION_TEXT + 3 VALUE + 3 DESCRIPTION',
   dict(kk) == {'MISSION_TEXT': 27, 'VALUE': 3, 'DESCRIPTION': 3}, dict(kk))
ck('i tre VALUE restano identici',
   [v['idx'] for v in cov if v['italian'].strip() == v['english'].strip()] == VALS
   and by[4]['italian'].strip() == 'Recover the fallen crew of the <EDC-ship>'
   and by[16]['italian'].strip() == 'Recover the fallen of <EDC-ship>'
   and by[29]['italian'].strip() == '<EDC-ship> salvage team')
ck('nessuna altra unita identica al sorgente',
   [v['idx'] for v in cov if v['italian'].strip() == v['english'].strip()] == VALS)
ck('le tre DESCRIPTION sono tradotte',
   all(by[i]['italian'].strip() != by[i]['english'].strip() for i in DESC)
   and by[5]['italian'].startswith('Recupera i corpi')
   and by[17]['italian'].startswith('Riporta i corpi')
   and by[30]['italian'].startswith('Assolda una squadra'))
ck('<origin> e <destination> non sono scambiati',
   TAGS.findall(by[5]['italian']) == ['<EDC-ship>', '<destination>', '<origin>']
   and '<origin>' in by[5]['italian'] and '<destination>' in by[5]['italian']
   and TAGS.findall(by[8]['italian']) == ['<planet>', '<origin>'])
ck('nessun <destination> dove il sorgente ha <origin>',
   not [v['idx'] for v in cov if v['italian'].count('<destination>') != v['english'].count('<destination>')]
   and not [v['idx'] for v in cov if v['italian'].count('<origin>') != v['english'].count('<origin>')])
for k in ('TEXT', 'DIALOG', 'LOGBOOK', 'UI_LABEL', 'CONVERSATION'):
    ck('%s assente' % k, not [u for u in cov if u['kind'] == k])
ck('quattro contesti in ordine di riga', list(dict.fromkeys(u['context'] for u in units)) == CTX,
   list(dict.fromkeys(u['context'] for u in units)))
ck('tab: 20, nelle unita attese', [v['idx'] for v in cov if v['italian'].startswith('\t')] == TABS,
   [v['idx'] for v in cov if v['italian'].startswith('\t')])
ck('tab per unita', not [v for v in cov if v['english'].count('\t') != v['italian'].count('\t')])
ck('virgolette: 14 = 14',
   sum(v['english'].count('"') for v in cov) == sum(v['italian'].count('"') for v in cov) == 14,
   (sum(v['english'].count('"') for v in cov), sum(v['italian'].count('"') for v in cov)))
ck('virgolette per unita', not [v for v in cov if v['english'].count('"') != v['italian'].count('"')])
ck('ZERO citazioni aperte (asserito vuoto)', not [v['idx'] for v in cov if v['italian'].count('"') % 2])
ck('ZERO quadre (asserito vuoto)', not [v['idx'] for v in cov if '[' in v['italian'] or ']' in v['italian']])
tk_e = [t for v in cov for t in TAGS.findall(v['english'])]
tk_i = [t for v in cov for t in TAGS.findall(v['italian'])]
ck('token: 23 = 23 in sette famiglie',
   tk_e == tk_i and collections.Counter(tk_e) == FAM and len(tk_e) == 23,
   (len(tk_e), collections.Counter(tk_e)))
ck('nessun backtick', not [v for v in cov if '`' in v['italian']])
grd = {}
for v in cov:
    grd.setdefault(v['english'], []).append(v['idx'])
ck('ZERO ripetizioni (asserito vuoto)', not [x for x in grd.values() if len(x) > 1])
ck('20/21/22 hanno lo stesso nucleo ma soggetti diversi',
   len({by[20]['italian'], by[21]['italian'], by[22]['italian']}) == 3
   and 'il resto dell\'equipaggio' in by[20]['italian']
   and 'voi raccogliete' in by[21]['italian']
   and by[22]['italian'].strip().startswith('Uno alla volta'))
ck('24 (equipaggio) e 25 (precauzione) divergono in apertura',
   by[24]['italian'].strip().startswith('L\'equipaggio fa un ultimo giro')
   and by[25]['italian'].strip().startswith('Per precauzione'))
ck('18 (con equipaggio) e 19 (da soli) divergono in coda',
   'voi e il vostro equipaggio' in by[18]['italian']
   and 'senza nessuno del vostro equipaggio' in by[19]['italian'])
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
