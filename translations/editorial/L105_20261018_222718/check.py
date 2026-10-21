r"""check.py — L105 (data/quarg/quarg missions.txt, 61 unita', righe 335-506)

**Ultimo segmento: chiude il file.** Tre tipi in un lotto: **56 `MISSION_TEXT`**, **4 `UI_LABEL`** (unita' 29, 31,
36, 38 — etichette di salto, **identiche**) e **1 `LOGBOOK`** (unita' 58 — prosa, **tradotta per intero**).

**54 tab** (senza tab 1, 5, 29, 31, 36, 38, 58). **99 virgolette** con **una citazione aperta** (unita' 26).
**Sette token** in cinque famiglie: `<origin>` (1), `<first>`+`<last>` (11, 43), `<start planet>`+`<start system>`
(49). **Cinque ripetizioni**: 2/6, 3/7, 4/8, 17/20/24, 21/25.
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
TABS = [i for i in range(1, 62) if i not in (1, 5, 29, 31, 36, 38, 58)]
LABELS = {29: 'heliarch 2', 31: 'heliarch ask', 36: 'lunarium 2', 38: 'lunarium ask'}
GROUPS = [(2, 6), (3, 7), (4, 8), (17, 20, 24), (21, 25)]
FAM = {'<origin>': 1, '<first>': 2, '<last>': 2, '<start planet>': 1, '<start system>': 1}
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


ck("unita' tradotte 61/61", len(cov) == 61 == len(units) and not missing, '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
kk = collections.Counter(u['kind'] for u in units)
ck('tipi: 56 MISSION_TEXT + 4 UI_LABEL + 1 LOGBOOK',
   dict(kk) == {'MISSION_TEXT': 56, 'UI_LABEL': 4, 'LOGBOOK': 1}, dict(kk))
ck('le 4 UI_LABEL restano identiche (etichette di salto)',
   [i for i in LABELS if by[i]['italian'].strip() == LABELS[i]] == list(LABELS)
   and [i for i in range(1, 62) if by[i]['kind'] == 'UI_LABEL'] == list(LABELS),
   [(i, by[i]['italian']) for i in LABELS])
ck('il LOGBOOK (unita 58) e tradotto, non identico',
   by[58]['kind'] == 'LOGBOOK' and by[58]['italian'].strip() != by[58]['english'].strip()
   and by[58]['italian'].startswith('Nome completo: Gohl Salyi Memt-Wrik Laz'))
for k in ('TEXT', 'VALUE', 'DESCRIPTION', 'DIALOG', 'CONVERSATION'):
    ck('%s assente' % k, not [u for u in cov if u['kind'] == k])
ck('nessuna riga identica salvo le 4 etichette',
   [v['idx'] for v in cov if v['italian'].strip() == v['english'].strip()] == list(LABELS),
   [v['idx'] for v in cov if v['italian'].strip() == v['english'].strip()])
grd = {}
for v in cov:
    grd.setdefault(v['english'], []).append(v['idx'])
dups = sorted(tuple(x) for x in grd.values() if len(x) > 1)
ck('5 ripetizioni: 2/6, 3/7, 4/8, 17/20/24, 21/25', dups == GROUPS, dups)
ck('ogni gruppo reso identico', all(len({by[i]['italian'] for i in g}) == 1 for g in GROUPS))
ck('nessun altro duplicato italiano',
   sorted(c for c in collections.Counter(v['italian'] for v in cov).values() if c > 1) == [2, 2, 2, 2, 3],
   sorted(c for c in collections.Counter(v['italian'] for v in cov).values() if c > 1))
odd = [v['idx'] for v in cov if v['english'].count('"') % 2 or v['italian'].count('"') % 2]
ck('una citazione aperta: unita 26', odd == [26], odd)
ck('unita 26: tre virgolette e non finisce con virgoletta',
   by[26]['italian'].count('"') == 3 and not by[26]['italian'].rstrip().endswith('"'),
   (by[26]['italian'].count('"'), by[26]['italian'][-40:]))
ctxs = []
for u in units:
    if u['context'] not in ctxs:
        ctxs.append(u['context'])
ck('un solo contesto, e chiude il file',
   len(ctxs) == 1 and ctxs[0] == 'mission:Ask Quarg About Coalition Late'
   and ctxs[0] == units[-1]['context'], ctxs)
ck('tab: 54, nelle unita attese', [v['idx'] for v in cov if v['italian'].startswith('\t')] == TABS,
   [v['idx'] for v in cov if v['italian'].startswith('\t')])
ck('tab per unita', not [v for v in cov if v['english'].count('\t') != v['italian'].count('\t')])
ck('virgolette: 99 = 99',
   sum(v['english'].count('"') for v in cov) == sum(v['italian'].count('"') for v in cov) == 99,
   (sum(v['english'].count('"') for v in cov), sum(v['italian'].count('"') for v in cov)))
ck('virgolette per unita', not [v for v in cov if v['english'].count('"') != v['italian'].count('"')],
   [(v['idx'], v['english'].count('"'), v['italian'].count('"')) for v in cov
    if v['english'].count('"') != v['italian'].count('"')])
tk_e = [t for v in cov for t in TAGS.findall(v['english'])]
tk_i = [t for v in cov for t in TAGS.findall(v['italian'])]
ck('token: 7 = 7 in cinque famiglie',
   tk_e == tk_i and collections.Counter(tk_e) == FAM and len(tk_e) == 7,
   (collections.Counter(tk_e), collections.Counter(tk_i)))
ck('i due token nuovi sono nell\'unita 49, in ordine',
   TAGS.findall(by[49]['italian']) == ['<start planet>', '<start system>'],
   TAGS.findall(by[49]['italian']))
ck('token identici per unita e nello stesso ordine',
   all(TAGS.findall(v['english']) == TAGS.findall(v['italian']) for v in cov))
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
