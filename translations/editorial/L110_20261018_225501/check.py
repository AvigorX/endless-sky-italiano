r"""check.py — L110 (data/korath/korath missions.txt, 26 unita', righe 474-580) — CHIUDE il file

**Tre contesti**: `Efreti: Distress Call 6` (474-479), `Distress Call 7` (508-558), `Distress Call 8` (570-580).

**21 `MISSION_TEXT` + 2 `VALUE` + 2 `DESCRIPTION` + 1 `DIALOG`**. I `VALUE` (1, 4) sono **lo stesso testo** e
restano identici; le `DESCRIPTION` (2, 5) sono **identiche fra loro** e tradotte.

**Due coppie di ripetizioni** rese identiche: 1/4 e 2/5. È il primo lotto del file in cui il criterio «zero
ripetizioni» va **rovesciato**: il controllo verifica che le coppie siano davvero uguali e che **non** ce ne siano
altre.

**17 tab** (senza tab 1, 2, 3, 4, 5, 6, 11, 12, 20). **8 virgolette**, tutte binate. **19 token** in sette famiglie:
`<EDC-ship>` 12, `<planet>` 2, `<bunks>` 1, `<ship>` 1, `<destination>` 1, `<first>` 1, `<last>` 1.
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
NOTAB = [1, 2, 3, 4, 5, 6, 11, 12, 20]
TABS = [i for i in range(1, 27) if i not in NOTAB]
VALS = [1, 4]
DESC = [2, 5]
DIAL = [11]
GROUPS = [(1, 4), (2, 5)]
FAM = {'<EDC-ship>': 12, '<planet>': 2, '<bunks>': 1, '<ship>': 1, '<destination>': 1, '<first>': 1, '<last>': 1}
CTX = ['mission:Efreti: Distress Call 6', 'mission:Efreti: Distress Call 7', 'mission:Efreti: Distress Call 8']
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


ck("unita' tradotte 26/26", len(cov) == 26 == len(units) and not missing, '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
kk = collections.Counter(u['kind'] for u in units)
ck('tipi: 21 MISSION_TEXT + 2 VALUE + 2 DESCRIPTION + 1 DIALOG',
   dict(kk) == {'MISSION_TEXT': 21, 'VALUE': 2, 'DESCRIPTION': 2, 'DIALOG': 1}, dict(kk))
ck('i due VALUE sono lo stesso testo e restano identici',
   by[1]['italian'].strip() == by[4]['italian'].strip() == 'Salvage the <EDC-ship>'
   and [v['idx'] for v in cov if v['italian'].strip() == v['english'].strip()] == VALS,
   [v['idx'] for v in cov if v['italian'].strip() == v['english'].strip()])
ck('le due DESCRIPTION sono identiche fra loro e tradotte',
   by[2]['italian'].strip() == by[5]['italian'].strip()
   and by[2]['italian'].strip() != by[2]['english'].strip()
   and by[2]['italian'].startswith('Recupera la <EDC-ship>'))
ck('nessun altra unita identica al sorgente',
   [v['idx'] for v in cov if v['italian'].strip() == v['english'].strip()] == VALS)
ck('il DIALOG (11) e tradotto', by[11]['italian'].strip() != by[11]['english'].strip()
   and 'la <EDC-ship> non c\'è' in by[11]['italian'])
for k in ('TEXT', 'LOGBOOK', 'UI_LABEL', 'CONVERSATION'):
    ck('%s assente' % k, not [u for u in cov if u['kind'] == k])
ck('tre contesti in ordine di riga', list(dict.fromkeys(u['context'] for u in units)) == CTX,
   list(dict.fromkeys(u['context'] for u in units)))
ck('tab: 17, nelle unita attese', [v['idx'] for v in cov if v['italian'].startswith('\t')] == TABS,
   [v['idx'] for v in cov if v['italian'].startswith('\t')])
ck('tab per unita', not [v for v in cov if v['english'].count('\t') != v['italian'].count('\t')])
ck('virgolette: 8 = 8',
   sum(v['english'].count('"') for v in cov) == sum(v['italian'].count('"') for v in cov) == 8,
   (sum(v['english'].count('"') for v in cov), sum(v['italian'].count('"') for v in cov)))
ck('virgolette per unita', not [v for v in cov if v['english'].count('"') != v['italian'].count('"')])
ck('ZERO citazioni aperte (asserito vuoto)', not [v['idx'] for v in cov if v['italian'].count('"') % 2])
ck('ZERO quadre (asserito vuoto)', not [v['idx'] for v in cov if '[' in v['italian'] or ']' in v['italian']])
tk_e = [t for v in cov for t in TAGS.findall(v['english'])]
tk_i = [t for v in cov for t in TAGS.findall(v['italian'])]
ck('token: 19 = 19 in sette famiglie',
   tk_e == tk_i and collections.Counter(tk_e) == FAM and len(tk_e) == 19,
   (len(tk_e), collections.Counter(tk_e)))
ck('<first> e <last> insieme, solo nell unita 25',
   [v['idx'] for v in cov if '<first>' in v['english']] == [25]
   and [v['idx'] for v in cov if '<last>' in v['english']] == [25]
   and TAGS.findall(by[25]['italian']) == ['<EDC-ship>', '<first>', '<last>', '<EDC-ship>'])
ck('nessun backtick', not [v for v in cov if '`' in v['italian']])
grd = {}
for v in cov:
    grd.setdefault(v['english'], []).append(v['idx'])
dups = sorted(tuple(x) for x in grd.values() if len(x) > 1)
ck('ESATTAMENTE 2 ripetizioni, 1/4 e 2/5 (criterio rovesciato)', dups == GROUPS, dups)
ck('ogni ripetizione resa identica', all(len({by[i]['italian'] for i in g}) == 1 for g in GROUPS))
ck('la dedica nomina il giocatore una volta sola',
   by[25]['italian'].count('<first> <last>') == 1)
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
