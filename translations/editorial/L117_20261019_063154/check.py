r"""check.py — L117 (data/human/pirate jobs.txt, 98 unita', righe 20-1624)

**Primo lotto su un file di lavori**: la tassonomia cambia rispetto ai sei lotti di tooltip.

- **98 unità, 31 contesti** (26 con tre unità, 5 con quattro): ogni contesto è una **missione** con nome,
  descrizione e messaggio di fallimento; cinque hanno anche il `DIALOG` di consegna.
- **31 `VALUE`** sono **nomi di missione** (`Smuggling to <planet>`, …): restano **identici** al sorgente,
  elencati esplicitamente e **esclusi** dal controllo «nessuna unità identica al sorgente».
- **108 token** in sei famiglie: `<payment>` 36, `<planet>` 31, `<cargo>` 31, `<destination>` 31,
  `<passengers>` 4, `<bunks>` 3 — parità per simbolo **e per unità**.
- **26 testi distinti** per **98 unità**: la ripetizione è del sorgente, la resa ripete e il controllo verifica
  che ogni gruppo di inglese identico abbia **una sola** resa italiana.
- **2 virgolette**, solo nell'unità 81 (l'urlo del criminale). Zero tab, zero quadre, zero backtick.
"""
import collections
import json
import os
import re
import sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
units = sorted(src['units'], key=lambda x: x['line'])
tr = {}
parts = sorted(f for f in os.listdir(os.path.join(HERE, 'parts')) if f.endswith('.json'))
for p in parts:
    for k, v in json.load(open(os.path.join(HERE, 'parts', p), encoding='utf-8')).items():
        tr[int(k)] = v
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


ck("unita' tradotte 98/98", len(cov) == 98 == len(units) and not missing, '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
kk = collections.Counter(u['kind'] for u in units)
ck('tipi: 31 VALUE · 31 DESCRIPTION · 31 MISSION_TEXT · 5 DIALOG',
   dict(kk) == {'VALUE': 31, 'DESCRIPTION': 31, 'MISSION_TEXT': 31, 'DIALOG': 5}, dict(kk))
ck('nessun tipo estraneo (TUTORIAL_TIP, TEXT, LOGBOOK…)',
   not [u for u in cov if u['kind'] not in ('VALUE', 'DESCRIPTION', 'MISSION_TEXT', 'DIALOG')])
VAL = [u['idx'] for u in units if u['kind'] == 'VALUE']
ck('i 31 VALUE sono identici al sorgente (nomi di missione)',
   len(VAL) == 31 and all(by[i]['italian'] == by[i]['english'] for i in VAL),
   [i for i in VAL if by[i]['italian'] != by[i]['english']])
NONVAL = [u['idx'] for u in units if u['kind'] != 'VALUE']
ck('tutte le unita non-VALUE sono tradotte',
   not [i for i in NONVAL if by[i]['italian'].strip() == by[i]['english'].strip()],
   [i for i in NONVAL if by[i]['italian'].strip() == by[i]['english'].strip()])
ck('i 5 DIALOG sono tradotti',
   not [i for i in NONVAL if by[i]['kind'] == 'DIALOG' and by[i]['italian'] == by[i]['english']])
ck('ZERO tab, nel sorgente e in traduzione',
   not [u['idx'] for u in units if '\t' in u['english']]
   and not [v['idx'] for v in cov if '\t' in v['italian']])
a = sum(v['english'].count('"') for v in cov)
b = sum(v['italian'].count('"') for v in cov)
ck('virgolette: %d = %d (2)' % (a, b), a == b == 2, (a, b))
ck('le due virgolette stanno nell\'unita 81',
   [v['idx'] for v in cov if v['italian'].count('"')] == [81]
   and by[81]['italian'].count('"') == 2)
ck('ZERO quadre (asserito vuoto)', not [v['idx'] for v in cov if '[' in v['italian'] or ']' in v['italian']])
ck('ZERO backtick', not [v['idx'] for v in cov if '`' in v['italian']])
# --- token: 108 in sei famiglie, per simbolo e per unita' --------------------------------
TOK = {'<payment>': 36, '<planet>': 31, '<cargo>': 31, '<destination>': 31, '<passengers>': 4, '<bunks>': 3}
ck('108 token nelle sei famiglie attese',
   collections.Counter(t for v in cov for t in TAGS.findall(v['english'])) == TOK
   == collections.Counter(t for v in cov for t in TAGS.findall(v['italian'])),
   collections.Counter(t for v in cov for t in TAGS.findall(v['italian'])))
ck('token per unita: stessi simboli e stesso ordine',
   not [(v['idx'], TAGS.findall(v['italian']), TAGS.findall(v['english'])) for v in cov
        if TAGS.findall(v['italian']) != TAGS.findall(v['english'])],
   [(v['idx'], TAGS.findall(v['italian']), TAGS.findall(v['english'])) for v in cov
    if TAGS.findall(v['italian']) != TAGS.findall(v['english'])])
# --- contesti: 31 missioni -----------------------------------------------------------------
seen = collections.Counter(u['context'] for u in units)
ck('31 contesti distinti, tutti mission:', len(seen) == 31 and all(c.startswith('mission:') for c in seen),
   len(seen))
ck('distribuzione: 26 contesti con 3 unita, 5 con 4',
   collections.Counter(seen.values()) == {3: 26, 4: 5}, collections.Counter(seen.values()))
ck('prima e ultima unita: righe 20 e 1624', (cov[0]['line'], cov[-1]['line']) == (20, 1624),
   (cov[0]['line'], cov[-1]['line']))
ck('primo e ultimo contesto: Cargo Smuggling [0] / Highly Wanted Passenger (North)',
   (cov[0]['context'], cov[-1]['context'])
   == ('mission:Cargo Smuggling [0]', 'mission:Highly Wanted Passenger (North)'),
   (cov[0]['context'], cov[-1]['context']))
# --- ripetizioni: 26 testi distinti, una resa per testo -----------------------------------
grd = collections.Counter(u['english'] for u in units)
ck('26 testi inglesi distinti per 98 unita', len(grd) == 26, len(grd))
ck('nessun gruppo con due rese diverse',
   not [k for k in grd if len({by[u['idx']]['italian'] for u in units if u['english'] == k}) > 1])
it_grp = {}
for v in cov:
    it_grp.setdefault(v['italian'], []).append(v)
ck('nessun duplicato italiano non spiegato dal sorgente',
   not [g for g in it_grp.values() if len(g) > 1 and len({v['english'] for v in g}) > 1],
   [[v['idx'] for v in g] for g in it_grp.values() if len(g) > 1 and len({v['english'] for v in g}) > 1])
ck('registro approvato: nessun «voi»',
   not [v['idx'] for v in cov if re.search(r'\b(avete|potete|potrete|siete|vostro|vostra|vostri|vostre)\b',
                                           v['italian'])])
LOW = ' '.join(v['italian'] for v in cov).lower()
TERMS = ('contrabbando', 'carico', 'compenso', 'multa', 'criminale', 'ricercato', 'passeggero',
         'spazioporto', 'forze dell\'ordine')
# 'droga' non compare nella prosa di questo segmento: i nomi con «drug» restano in inglese (VALUE)
ck('terminologia presente: 9 termini chiave', all(t in LOW for t in TERMS),
   [t for t in TERMS if t not in LOW])
NOSCRUB = ' '.join(TAGS.sub('""', v['italian']) for v in cov).lower()
ENGWORDS = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' ship ', ' law ')
ck('nessun residuo inglese fuori dai token',
   not [w for w in ENGWORDS if w in NOSCRUB], [w for w in ENGWORDS if w in NOSCRUB])
rs = [v['ratio'] for v in cov]
for v in cov:
    if not 0.55 < v['ratio'] < 1.90:
        print('OUTLIER', v['idx'], v['ratio'], v['english'][:40], '|', v['italian'][:40])
ck('rapporto nel gate', 0.55 < min(rs) and max(rs) < 1.90, '%.2f - %.2f' % (min(rs), max(rs)))
bad = [(v['idx'], n) for v in cov for p, n in ((r"\b(e|piu|perche|cosi|gia|puo|cioe|percio|fa)'", 'accento'),
       ('\u2026', 'ellissi'), ('\u2014', 'em dash'), ('\u2019', 'apostrofo curvo'), ('\u00ab', 'caporale'),
       ('\u00bb', 'caporale')) if re.search(p, v['italian'])]
ck('tipografia', not bad, bad)
nonlat = [v['idx'] for v in cov for c in v['italian'] if ord(c) > 127 and not 0x00C0 <= ord(c) <= 0x024F]
ck('caratteri non latini', not nonlat, nonlat)
c = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
st = dict(c.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('tutte le 98 unita sono PENDING nel database (misurato)',
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
