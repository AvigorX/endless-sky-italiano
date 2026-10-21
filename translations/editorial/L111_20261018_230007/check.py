r"""check.py — L111 (data/_ui/tooltips.txt, 104 unita', righe 16-328)

**Primo lotto del file**: suggerimenti dell'interfaccia, uno per contesto (`tip:...`).

**104 `TUTORIAL_TIP`**, nient'altro. **Zero tab**, **14 virgolette** (tutte doppie, interne al testo: nomi di
attributo e di categoria), **zero token**, **zero quadre**, **zero ripetizioni**. I **contesti sono 104**, uno per
unità e tutti distinti.

Le asserzioni sono **rovesciate** rispetto ai lotti narrativi: qui l'assenza di tab, token, quadre e ripetizioni è
verificata come fatto positivo, non omessa.
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
FAM = {}
CTX = []
for u in units:
    if u['context'] not in CTX:
        CTX.append(u['context'])
out = {'block': src['block'], 'note': src['note'], 'units': []}
missing = []
for u in units:
    if u['idx'] not in tr:
        missing.append(u['idx'])
        continue
    it = tr[u['idx']]
    out['units'].append({"idx": u['idx'], "id": u['id'], "path": u['path'], "line": u['line'],
                         "kind": u['kind'], "context": u['context'], "english": u['english'],
                         "italian": it, "ratio": round(len(it) / max(1, len(u['english'])), 3)})
open(os.path.join(HERE, 'translation.json'), 'w', encoding='utf-8').write(json.dumps(out, ensure_ascii=False, indent=1))
cov = out['units']
by = {v['idx']: v for v in cov}
TAGS = re.compile(r'<[^<>]+>')
# --- split APPROVED/PENDING: serve prima del gate di lunghezza -----------------------------
_c0 = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
dbst, dbit = {}, {}
for _u in units:
    _r = _c0.execute('select state, italian from units where id=?', (_u['id'],)).fetchone()
    dbst[_u['idx']], dbit[_u['idx']] = _r[0], _r[1]
appr = sorted(i for i in dbst if dbst[i] == 'APPROVED')
pend = sorted(i for i in dbst if dbst[i] == 'PENDING')
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 104/104", len(cov) == 104 == len(units) and not missing, '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
kk = collections.Counter(u['kind'] for u in units)
ck('tipo unico: 104 TUTORIAL_TIP', dict(kk) == {'TUTORIAL_TIP': 104}, dict(kk))
for k in ('VALUE', 'DESCRIPTION', 'MISSION_TEXT', 'TEXT', 'DIALOG', 'LOGBOOK', 'UI_LABEL'):
    ck('%s assente' % k, not [u for u in cov if u['kind'] == k])
ck('nessuna unita identica al sorgente',
   not [v['idx'] for v in cov if v['italian'].strip() == v['english'].strip()],
   [v['idx'] for v in cov if v['italian'].strip() == v['english'].strip()])
ck('ZERO tab, nel sorgente e in traduzione',
   not [u['idx'] for u in units if u['english'].startswith('\t')]
   and not [v['idx'] for v in cov if v['italian'].startswith('\t') or '\t' in v['italian']])
ck('ZERO token (asserito vuoto)',
   not [t for v in cov for t in TAGS.findall(v['italian'])]
   and not [t for u in units for t in TAGS.findall(u['english'])])
ck('ZERO quadre (asserito vuoto)', not [v['idx'] for v in cov if '[' in v['italian'] or ']' in v['italian']])
grd = {}
for u in units:
    grd.setdefault(u['english'], []).append(u['idx'])
ck('ZERO ripetizioni (asserito vuoto)', not [x for x in grd.values() if len(x) > 1])
ck('contesti: 104, uno per unita, tutti distinti',
   len(CTX) == 104 == len(units) and len(set(CTX)) == 104, len(CTX))
ck('ogni contesto inizia con tip:',
   all(c.startswith('tip:') for c in CTX) and all(u['context'].startswith('tip:') for u in units))
ck('prima e ultima unita: righe 16 e 328', (cov[0]['line'], cov[-1]['line']) == (16, 328),
   (cov[0]['line'], cov[-1]['line']))
a = sum(u['english'].count('"') for u in units)
b = sum(v['italian'].count('"') for v in cov)
ck('virgolette: %d = %d (14)' % (a, b), a == b == 14, (a, b))
ck('virgolette per unita', not [v for v in cov if v['english'].count('"') != v['italian'].count('"')])
ck('le virgolette sono pari in ogni unita', not [v['idx'] for v in cov if v['italian'].count('"') % 2])
ck('nessun backtick', not [v for v in cov if '`' in v['italian']])
# terminologia: un termine, una resa
LOW = ' '.join(v['italian'] for v in cov).lower()
TERMS = ('massa', 'accelerazione', 'energia', 'calore', 'raffreddamento', 'carburante', 'scafo',
         'scudi', 'occultamento', 'equipaggiamento', 'tonnellate', 'equipaggio')
ck('terminologia presente: 12 termini chiave', all(t in LOW for t in TERMS),
   [t for t in TERMS if t not in LOW])
ck('nessun termine inglese lasciato in italiano',
   not [w for w in ('mass ', 'acceleration', 'energy ', 'fuel ', 'hull ', 'shield ', 'cloak ', 'cooling ')
        if w in LOW],
   [w for w in ('mass ', 'acceleration', 'energy ', 'fuel ', 'hull ', 'shield ', 'cloak ', 'cooling ') if w in LOW])
rs = [by[i]['ratio'] for i in pend]
for i in pend:
    if not 0.55 < by[i]['ratio'] < 1.90:
        print('OUTLIER', i, by[i]['ratio'], by[i]['english'][:40], '|', by[i]['italian'][:40])
ck('rapporto nel gate (sole unita PENDING: le approvate non si toccano)',
   0.55 < min(rs) and max(rs) < 1.90, '%.2f - %.2f' % (min(rs), max(rs)))
bad = [(i, n) for i in pend for pat, n in ((r"\b(e|piu|perche|cosi|gia|puo|cioe|percio)'", 'accento'),
       ('\u2026', 'ellissi'), ('\u2014', 'em dash'), ('\u2019', 'apostrofo curvo'), ('\u00ab', 'caporale'),
       ('\u00bb', 'caporale')) if re.search(pat, by[i]['italian'])]
ck('tipografia (sole unita PENDING)', not bad, bad)
nonlat = [v['idx'] for v in cov for c in v['italian'] if ord(c) > 127 and not 0x00C0 <= ord(c) <= 0x024F]
ck('caratteri non latini', not nonlat, nonlat)
c = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
st = dict(c.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
# --- il lotto attraversa DUE stati: 52 APPROVED (testo esistente) e 52 PENDING -------------------
ck('52 APPROVED e 52 PENDING, contigui (1-52, 53-104)',
   appr == list(range(1, 53)) and pend == list(range(53, 105)),
   (len(appr), len(pend), appr[:1], pend[:1]))
ck('le 52 APPROVED riproducono il testo del database alla lettera',
   all(by[i]['italian'].strip() == dbit[i].strip() for i in appr)
   and all(dbit[i] for i in appr),
   [i for i in appr if by[i]['italian'].strip() != dbit[i].strip()])
ck('le 52 PENDING sono tradotte (diverse dal sorgente)',
   all(by[i]['italian'].strip() != by[i]['english'].strip() for i in pend),
   [i for i in pend if by[i]['italian'].strip() == by[i]['english'].strip()])
ck('le PENDING usano il «tu», come il blocco approvato (nessun «voi»)',
   not [i for i in pend if re.search(r'\b(avete|potete|potrete|siete|vostro|vostra|vostri|vostre)\b',
                                     by[i]['italian'])],
   [i for i in pend if re.search(r'\b(avete|potete|potrete|siete|vostro|vostra|vostri|vostre)\b',
                                 by[i]['italian'])])
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, b2, ok in rows:
    print('| %s | %s | %s |' % (n, b2, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d' % (sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('righe %d/%d · parti %d · mancanti %d' % (min(u['line'] for u in units), max(u['line'] for u in units),
      len(parts), len(missing)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
