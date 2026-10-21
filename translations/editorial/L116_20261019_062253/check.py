r"""check.py — L116 (data/_ui/tooltips.txt, 133 unita', righe 1569-1865) — **chiude il file**

**133 `TUTORIAL_TIP`**, tutte **`PENDING`** (misurato e asserito in `mkparts.py`). Sono **tutte** le unità che
restavano: dopo questo lotto il file è al 100%.

**Forma dei contesti**: **80 per 133 unità** — 62 singole, 1 coppia, 4 terne, 8 quaterne, 5 gruppi da cinque.
I primi nomi hanno **tre spazi iniziali** (`tip:   Show flagship overlay`).

**144 virgolette** in 66 unità (61 con due, 4 con quattro, una con sei): sono **chiavi e valori di
`Preferences`** e nomi di gamerule (`"ship cap,"`, `"off"`, `"Restricted save loading"`), quindi restano
identici all'inglese — **compresa la virgola interna** di `"ship cap,"`, che il sorgente mette dentro le
virgolette (unità 122-124) e che si riproduce. **1 token** `<shift>`. Zero tab, zero quadre, zero backtick.
**Zero ripetizioni**: nessuna coppia di unità ha lo stesso inglese.
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
CTX = [u['context'] for u in units]
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
QUOTED = re.compile(r'"([^"]*)"')
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 133/133", len(cov) == 133 == len(units) and not missing, '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
kk = collections.Counter(u['kind'] for u in units)
ck('tipo unico: 133 TUTORIAL_TIP', dict(kk) == {'TUTORIAL_TIP': 133}, dict(kk))
for k in ('VALUE', 'DESCRIPTION', 'MISSION_TEXT', 'TEXT', 'DIALOG', 'LOGBOOK', 'UI_LABEL', 'CONVERSATION'):
    ck('%s assente' % k, not [u for u in cov if u['kind'] == k])
ck('nessuna unita identica al sorgente',
   not [v['idx'] for v in cov if v['italian'].strip() == v['english'].strip()])
ck('ZERO tab, nel sorgente e in traduzione',
   not [u['idx'] for u in units if '\t' in u['english']]
   and not [v['idx'] for v in cov if '\t' in v['italian']])
a = sum(v['english'].count('"') for v in cov)
b = sum(v['italian'].count('"') for v in cov)
ck('virgolette: %d = %d (144)' % (a, b), a == b == 144, (a, b))
ck('virgolette per unita', not [v for v in cov if v['english'].count('"') != v['italian'].count('"')],
   [(v['idx'], v['english'].count('"'), v['italian'].count('"'))
    for v in cov if v['english'].count('"') != v['italian'].count('"')])
ck('66 unita citano: 61 con due, 4 con quattro, una con sei',
   collections.Counter(v['italian'].count('"') for v in cov if v['italian'].count('"'))
   == {2: 61, 4: 4, 6: 1},
   collections.Counter(v['italian'].count('"') for v in cov if v['italian'].count('"')))
ck('le citazioni sono chiavi/valori/gamerule identici all\'inglese (nessuna eccezione)',
   not [(v['idx'], QUOTED.findall(v['italian']), QUOTED.findall(v['english'])) for v in cov
        if QUOTED.findall(v['italian']) != QUOTED.findall(v['english'])],
   [(v['idx'], QUOTED.findall(v['italian']), QUOTED.findall(v['english'])) for v in cov
    if QUOTED.findall(v['italian']) != QUOTED.findall(v['english'])])
ck('le tre virgole interne sono riprodotte ("ship cap," ecc.)',
   QUOTED.findall(by[122]['italian'])[0] == 'ship cap,' and QUOTED.findall(by[123]['italian'])[0] == 'crew cap,'
   and QUOTED.findall(by[124]['italian'])[0] == 'admin cap,',
   [QUOTED.findall(by[i]['italian'])[0] for i in (122, 123, 124)])
ck('UN token: <shift> (1 = 1)',
   collections.Counter(t for v in cov for t in TAGS.findall(v['english']))
   == collections.Counter(t for v in cov for t in TAGS.findall(v['italian'])) == {'<shift>': 1},
   collections.Counter(t for v in cov for t in TAGS.findall(v['italian'])))
ck('il token sta nella stessa unita',
   [v['idx'] for v in cov if '<shift>' in v['italian']] == [v['idx'] for v in cov if '<shift>' in v['english']]
   == [55], [v['idx'] for v in cov if '<shift>' in v['italian']])
ck('ZERO quadre (asserito vuoto)', not [v['idx'] for v in cov if '[' in v['italian'] or ']' in v['italian']])
ck('ZERO backtick', not [v['idx'] for v in cov if '`' in v['italian']])
# --- contesti: 80 per 133 unita' ----------------------------------------------------------
seen = collections.Counter(CTX)
ck('80 contesti distinti, tutti tip:', len(seen) == 80 and all(c.startswith('tip:') for c in seen), len(seen))
ck('distribuzione dei contesti 62/1/4/8/5',
   collections.Counter(seen.values()) == {1: 62, 2: 1, 3: 4, 4: 8, 5: 5},
   collections.Counter(seen.values()))
ck('nessun contesto oltre cinque unita', max(seen.values()) == 5, seen.most_common(2))
ck('prima e ultima unita: righe 1569 e 1865', (cov[0]['line'], cov[-1]['line']) == (1569, 1865),
   (cov[0]['line'], cov[-1]['line']))
ck('i primi contesti hanno tre spazi iniziali, come il sorgente',
   cov[0]['context'] == 'tip:   Show flagship overlay' and cov[3]['context'] == 'tip:   Show neutral overlays',
   (cov[0]['context'], cov[3]['context']))
ck('ultimo contesto: boarding: installed', cov[-1]['context'] == 'tip:boarding: installed', cov[-1]['context'])
# --- ripetizioni: nessuna ----------------------------------------------------------------
grd = collections.Counter(u['english'] for u in units)
ck('ZERO ripetizioni (asserito vuoto)', not [k for k, v in grd.items() if v > 1],
   [k[:40] for k, v in grd.items() if v > 1])
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
TERMS = ('ammiraglia', 'scorte', 'flotta', 'detrito', 'munizioni', 'carburante', 'scudi', 'scafo',
         'sovrapposizione', 'impostazione', 'regola di gioco', 'salvataggio', 'pilota', 'nave personaggio',
         'mini-mappa', 'radar')
# 'energia' non compare in questa finestra (misurato): non si pretende un termine che il blocco non usa.
ck('terminologia presente: 16 termini chiave', all(t in LOW for t in TERMS),
   [t for t in TERMS if t not in LOW])
NOSCRUB = ' '.join(QUOTED.sub('""', v['italian']) for v in cov).lower()
ENGWORDS = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' ship ', ' game ', ' from ')
ck('nessun residuo inglese fuori dalle citazioni',
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
ck('tutte le 133 unita sono PENDING nel database (misurato)',
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
