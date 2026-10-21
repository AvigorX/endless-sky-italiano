r"""check.py — L112 (data/_ui/tooltips.txt, 120 unita', righe 331-688)

**120 `TUTORIAL_TIP`**, tutte **`PENDING`** (misurato: le 52 approvate del file stanno fra le righe 16 e 172).
**Zero tab**, **zero virgolette**, **zero token**, **zero quadre**, **zero ripetizioni**: cinque assenze verificate
come fatti positivi. **120 contesti**, uno per unità e tutti distinti.

Registro **fissato dal blocco approvato** (L111): «tu», «danni da …» al plurale con «resistiti», «ammiraglia»,
«messa fuori uso», «spazio equipaggiamenti»/«spazio motori», iperguida, ramscoop invariato.
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
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 120/120", len(cov) == 120 == len(units) and not missing, '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
kk = collections.Counter(u['kind'] for u in units)
ck('tipo unico: 120 TUTORIAL_TIP', dict(kk) == {'TUTORIAL_TIP': 120}, dict(kk))
for k in ('VALUE', 'DESCRIPTION', 'MISSION_TEXT', 'TEXT', 'DIALOG', 'LOGBOOK', 'UI_LABEL'):
    ck('%s assente' % k, not [u for u in cov if u['kind'] == k])
ck('nessuna unita identica al sorgente',
   not [v['idx'] for v in cov if v['italian'].strip() == v['english'].strip()],
   [v['idx'] for v in cov if v['italian'].strip() == v['english'].strip()])
ck('ZERO tab, nel sorgente e in traduzione',
   not [u['idx'] for u in units if '\t' in u['english']]
   and not [v['idx'] for v in cov if '\t' in v['italian']])
ck('ZERO virgolette (asserito vuoto)',
   sum(v['english'].count('"') for v in cov) == sum(v['italian'].count('"') for v in cov) == 0,
   (sum(v['english'].count('"') for v in cov), sum(v['italian'].count('"') for v in cov)))
ck('ZERO token (asserito vuoto)',
   not [t for v in cov for t in TAGS.findall(v['english'])]
   and not [t for v in cov for t in TAGS.findall(v['italian'])])
ck('ZERO quadre (asserito vuoto)', not [v['idx'] for v in cov if '[' in v['italian'] or ']' in v['italian']])
ck('stampo unico per le 8 varianti del danno (13-20)',
   all('quando una nave messa fuori uso si ripara da sola' in by[i]['italian'] for i in range(13, 21)),
   [i for i in range(13, 21) if 'quando una nave messa fuori uso si ripara da sola' not in by[i]['italian']])
ck('stampo unico per le 8 varianti della spinta inversa (88-95)',
   all('quando si attivano i propulsori di spinta inversa' in by[i]['italian'] for i in range(88, 96)),
   [i for i in range(88, 96) if 'quando si attivano i propulsori di spinta inversa' not in by[i]['italian']])
ck('le 8 varianti del danno sono tutte distinte fra loro',
   len({by[i]['italian'] for i in range(13, 21)}) == 8)
grd = {}
for u in units:
    grd.setdefault(u['english'], []).append(u['idx'])
ck('ZERO ripetizioni (asserito vuoto)', not [x for x in grd.values() if len(x) > 1])
ck('contesti: 120, uno per unita, tutti distinti',
   len(CTX) == 120 == len(set(CTX)) and all(c.startswith('tip:') for c in CTX), len(CTX))
ck('prima e ultima unita: righe 331 e 688', (cov[0]['line'], cov[-1]['line']) == (331, 688),
   (cov[0]['line'], cov[-1]['line']))
ck('registro approvato: nessun «voi» nelle nuove',
   not [v['idx'] for v in cov if re.search(r'\b(avete|potete|potrete|siete|vostro|vostra|vostri|vostre)\b',
                                           v['italian'])],
   [v['idx'] for v in cov if re.search(r'\b(avete|potete|potrete|siete|vostro|vostra|vostri|vostre)\b',
                                       v['italian'])])
ck('nessun backtick', not [v for v in cov if '`' in v['italian']])
LOW = ' '.join(v['italian'] for v in cov).lower()
TERMS = ('scafo', 'scudi', 'carburante', 'calore', 'energia', 'equipaggiamento', 'cuccette',
         'messa fuori uso', 'danni da', 'occultamento', 'iperguida', 'ramscoop')
ck('terminologia presente: 12 termini chiave', all(t in LOW for t in TERMS),
   [t for t in TERMS if t not in LOW])
ck('nessun residuo inglese comune',
   not [w for w in (' the ', ' of the ', ' per second when', 'damage ', 'hull ', 'shield ', 'outfit ')
        if w in LOW],
   [w for w in (' the ', ' of the ', ' per second when', 'damage ', 'hull ', 'shield ', 'outfit ') if w in LOW])
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
ck('tutte le 120 unita sono PENDING nel database (misurato, non assunto)',
   c.execute('select count(*) from units where id in (%s) and state != "PENDING"'
             % ','.join('?' * len(units)), [u['id'] for u in units]).fetchone()[0] == 0)
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, b2, ok in rows:
    print('| %s | %s | %s |' % (n, b2, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d' % (sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('righe %d/%d · parti %d · mancanti %d' % (min(u['line'] for u in units), max(u['line'] for u in units),
      len(parts), len(missing)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
