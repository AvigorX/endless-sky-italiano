r"""check.py — L108 (data/korath/korath missions.txt, 36 unita', righe 216-335)

**Quattro contesti**: `phrase:kor efret small package offer` (216-241), `Small Scale Delivery` (244-260),
`Efreti: Distress Call 1` (269-303), `Efreti: Distress Call 2` (309-326).

**Cinque tipi**: 14 `TEXT` (**frammenti composti a runtime**), 15 `MISSION_TEXT`, 3 `VALUE` (identici),
3 `DESCRIPTION` e 1 `DIALOG` (tradotti).

**12 tab** (unita' 21-28, 33-36). **18 virgolette**, tutte binate. **23 token** in sei famiglie, fra cui
`<EDC-ship>` x8 (nuovo). **Zero quadre**, **zero ripetizioni**.

Il controllo centrale e' quello dei **vincoli di composizione** delle unita' 1-14, casella per casella.
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
NOTAB = list(range(1, 21)) + [29, 30, 31, 32]
TABS = [i for i in range(1, 37) if i not in NOTAB]
VALS = [15, 18, 29]
DESC = [16, 19, 30]
DIAL = [17]
SUBJ, VERB, OBJ, DEST, TAIL = [1, 2, 3], [4, 5], [6, 7, 8, 9], [10], [11, 12, 13, 14]
FAM = {'<EDC-ship>': 8, '<planet>': 4, '<destination>': 3, '<payment>': 3, '<ship>': 3, '<bunks>': 2}
CTX = ['phrase:kor efret small package offer', 'mission:Small Scale Delivery',
       'mission:Efreti: Distress Call 1', 'mission:Efreti: Distress Call 2']
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


ck("unita' tradotte 36/36", len(cov) == 36 == len(units) and not missing, '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
kk = collections.Counter(u['kind'] for u in units)
ck('tipi: 14 TEXT + 15 MISSION_TEXT + 3 VALUE + 3 DESCRIPTION + 1 DIALOG',
   dict(kk) == {'TEXT': 14, 'MISSION_TEXT': 15, 'VALUE': 3, 'DESCRIPTION': 3, 'DIALOG': 1}, dict(kk))
ck('i tre VALUE restano identici, coi token dentro',
   [v['idx'] for v in cov if v['italian'].strip() == v['english'].strip()] == VALS
   and by[15]['italian'].strip() == 'Package to <planet>'
   and by[18]['italian'].strip() == 'Distress call from the <EDC-ship>'
   and by[29]['italian'].strip() == 'Return the <EDC-ship> survivors')
ck('nessuna altra unita identica al sorgente',
   [v['idx'] for v in cov if v['italian'].strip() == v['english'].strip()] == VALS,
   [v['idx'] for v in cov if v['italian'].strip() == v['english'].strip()])
ck('DESCRIPTION e DIALOG tradotti',
   all(by[i]['italian'].strip() != by[i]['english'].strip() for i in DESC + DIAL)
   and by[16]['italian'].startswith('Porta una piccola consegna')
   and by[19]['italian'].startswith('I Quarg vi hanno chiesto')
   and by[30]['italian'].startswith('Trasporta i <bunks> superstiti')
   and by[17]['italian'].startswith('Trovate un Korath'))
for k in ('LOGBOOK', 'UI_LABEL', 'CONVERSATION'):
    ck('%s assente' % k, not [u for u in cov if u['kind'] == k])
ck('le 14 TEXT sono tutte unita 1-14', [v['idx'] for v in cov if v['kind'] == 'TEXT'] == list(range(1, 15)))
# --- composizione dei frammenti -----------------------------------------------------------
ck('soggetto (1-3): maiuscola, nessun punto finale',
   all(by[i]['italian'][0].isupper() and not by[i]['italian'].endswith('.') for i in SUBJ),
   [(i, by[i]['italian']) for i in SUBJ])
ck('verbo (4-5): minuscola, regge un infinito, nessun punto',
   all(by[i]['italian'][0].islower() and not by[i]['italian'].endswith('.')
       and by[i]['italian'].split()[-1] in ('devi', 'di') for i in VERB),
   [(i, by[i]['italian']) for i in VERB])
ck('oggetto (6-9): minuscola, prima parola infinito (-are), nessun punto',
   all(by[i]['italian'][0].islower() and by[i]['italian'].split()[0].endswith('are')
       and not by[i]['italian'].endswith('.') for i in OBJ),
   [(i, by[i]['italian']) for i in OBJ])
ck('destinazione (10): inizia con "a " e chiude col punto',
   by[10]['italian'].startswith('a ') and by[10]['italian'].endswith('.'), by[10]['italian'])
ck('frase finale (11-14): maiuscola e punto',
   all(by[i]['italian'][0].isupper() and by[i]['italian'].endswith('.') for i in TAIL),
   [(i, by[i]['italian']) for i in TAIL])
probe = ' '.join([by[1]['italian'], by[5]['italian'], by[7]['italian'], by[10]['italian'], by[11]['italian']])
ck('una combinazione compone una frase leggibile',
   'chiede di portare un pacco a <destination> per <payment>. Non dovrebbe' in probe and '  ' not in probe, probe)
ck('ogni soggetto x oggetto compone senza doppie maiuscole',
   not [x for x in (' '.join([by[s]['italian'], by[v]['italian'], by[o]['italian'], by[10]['italian']])
                    for s in SUBJ for v in VERB for o in OBJ) if '  ' in x or '..' in x])
# ----------------------------------------------------------------------------------------
ck('quattro contesti in ordine di riga', list(dict.fromkeys(u['context'] for u in units)) == CTX,
   list(dict.fromkeys(u['context'] for u in units)))
ck('tab: 12, nelle unita attese', [v['idx'] for v in cov if v['italian'].startswith('\t')] == TABS,
   [v['idx'] for v in cov if v['italian'].startswith('\t')])
ck('tab per unita', not [v for v in cov if v['english'].count('\t') != v['italian'].count('\t')])
ck('virgolette: 18 = 18',
   sum(v['english'].count('"') for v in cov) == sum(v['italian'].count('"') for v in cov) == 18,
   (sum(v['english'].count('"') for v in cov), sum(v['italian'].count('"') for v in cov)))
ck('virgolette per unita', not [v for v in cov if v['english'].count('"') != v['italian'].count('"')])
ck('ZERO citazioni aperte (asserito vuoto)', not [v['idx'] for v in cov if v['italian'].count('"') % 2])
ck('ZERO quadre (asserito vuoto)', not [v['idx'] for v in cov if '[' in v['italian'] or ']' in v['italian']])
tk_e = [t for v in cov for t in TAGS.findall(v['english'])]
tk_i = [t for v in cov for t in TAGS.findall(v['italian'])]
ck('token: 23 = 23 in sei famiglie',
   tk_e == tk_i and collections.Counter(tk_e) == FAM and len(tk_e) == 23,
   (len(tk_e), collections.Counter(tk_e)))
ck('<EDC-ship> in 8 unita attese',
   [v['idx'] for v in cov if '<EDC-ship>' in v['english']] == [18, 19, 21, 25, 29, 30, 31, 32],
   [v['idx'] for v in cov if '<EDC-ship>' in v['english']])
ck('nessun backtick', not [v for v in cov if '`' in v['italian']])
grd = {}
for v in cov:
    grd.setdefault(v['english'], []).append(v['idx'])
ck('ZERO ripetizioni (asserito vuoto)', not [x for x in grd.values() if len(x) > 1])
ck('35 e 36 divergono solo in coda (non identiche)',
   by[35]['italian'].split(' in fretta. ')[0] == by[36]['italian'].split(' in fretta. ')[0]
   and by[35]['italian'] != by[36]['italian'])
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
