r"""check.py — L270 (`data/human/engines.txt`, righe 488-717). **LOTTO TERMINALE: chiude il file.**

**17 `DESCRIPTION`, nessun `VALUE`**: la serie **Atomica** della Deep Sky (dieci modelli), `Tyrant` steering e due propulsori
inversi (`Capybara`, `AR120`). Quattro cose da verificare con cura:

1. **quattro tab** (unita' 1, 3, 5, 17): la nota del plasma e la nota del propulsore inverso sono **rientrate**;
2. **due stringhe ripetute** e riprese **alla lettera** dai lotti precedenti: la nota del plasma (L269) e la nota del
   montaggio del propulsore inverso (L268) — qui compare **due volte** (unita' 5 e 17);
3. **lotto terminale**: oltre all'invariante di segmento serve quella di **FILE** — 61 unita', righe distinte, ultima riga
   la **717**, **0 dopo**, e la somma dei lotti del file uguale a 61;
4. **sette apici inglesi** (`you're`, `Deep Sky's` ×4, `ship's`) e **otto italiani**.
"""
import collections
import glob
import json
import os
import re
import sqlite3

TAB = chr(9)
QUOTE = chr(34)
APOS = chr(39)
TAG = re.compile(r'<[^<>]+>')
HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
PREV269 = os.path.join(L10N, 'staging', 'editorial', 'L269_20261020_171905', 'translation.json')
PREV268 = os.path.join(L10N, 'staging', 'editorial', 'L268_20261020_171323', 'translation.json')
PATH = 'data/human/engines.txt'
src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
units = sorted(src['units'], key=lambda x: x['line'])
tr = {}
for p in sorted(f for f in os.listdir(os.path.join(HERE, 'parts')) if f.endswith('.json')):
    for k, v in json.load(open(os.path.join(HERE, 'parts', p), encoding='utf-8')).items():
        tr[int(k)] = v
out = {'block': src['block'], 'note': src['note'], 'units': []}
for u in units:
    if u['idx'] in tr:
        it = tr[u['idx']]
        out['units'].append({"idx": u['idx'], "id": u['id'], "path": u['path'], "line": u['line'],
                             "kind": u['kind'], "context": u['context'], "english": u['english'],
                             "italian": it, "ratio": round(len(it) / max(1, len(u['english'])), 3)})
open(os.path.join(HERE, 'translation.json'), 'w', encoding='utf-8').write(
    json.dumps(out, ensure_ascii=False, indent=1))
cov = out['units']
by = {u['idx']: u for u in cov}
BLOCCHI = [('outfit:Orca Plasma Steering', 488, 488), ('outfit:Tyrant Plasma Steering', 505, 506),
           ('outfit:Capybara Reverse Thruster', 524, 525), ('outfit:A120 Atomic Thruster', 544, 544),
           ('outfit:A250 Atomic Thruster', 561, 561), ('outfit:A370 Atomic Thruster', 578, 578),
           ('outfit:A520 Atomic Thruster', 595, 595), ('outfit:A860 Atomic Thruster', 612, 612),
           ('outfit:A125 Atomic Steering', 630, 630), ('outfit:A255 Atomic Steering', 647, 647),
           ('outfit:A375 Atomic Steering', 664, 664), ('outfit:A525 Atomic Steering', 681, 681),
           ('outfit:A865 Atomic Steering', 698, 698), ('outfit:AR120 Reverse Thruster', 716, 717)]
ATOMICI = [4, 6, 8, 10, 12, 14, 16]
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck('unita tradotte 17/17', len(cov) == 17 == len(units), '%d/%d' % (len(cov), len(units)))
ck('tipo: 17 DESCRIPTION, nessun VALUE',
   collections.Counter(u['kind'] for u in units) == {'DESCRIPTION': 17},
   dict(collections.Counter(u['kind'] for u in units)))
ck('quattordici contesti, con le righe misurate',
   [(c, by[[u['idx'] for u in cov if u['context'] == c][0]]['line'],
     by[[u['idx'] for u in cov if u['context'] == c][-1]]['line']) for c, _, _ in BLOCCHI] == BLOCCHI,
   [(c, by[[u['idx'] for u in cov if u['context'] == c][0]]['line']) for c, _, _ in BLOCCHI])
ck('righe 488-717, nessun buco interno, ultima unita del lotto alla 717',
   [u['line'] for u in cov] == sorted({u['line'] for u in cov})
   and cov[0]['line'] == 488 and cov[-1]['line'] == 717)
ck('tutte TRADOTTE, nessuna copiata',
   all(u['italian'] != u['english'] for u in cov), [u['idx'] for u in cov if u['italian'] == u['english']])
ck('TAB: quattro in inglese e quattro in italiano, sulle stesse unita, come PRIMO carattere',
   sum(u['english'].count(TAB) for u in cov) == 4 == sum(u['italian'].count(TAB) for u in cov)
   and [u['idx'] for u in cov if TAB in u['english']] == [1, 3, 5, 17]
   == [u['idx'] for u in cov if TAB in u['italian']]
   and all(u['italian'].startswith(TAB) for u in cov if TAB in u['italian']))
ck('la nota del plasma (unita 1, 3) e IDENTICA a quella di L269, riletto il suo translation.json',
   len({by[1]['italian'], by[3]['italian']}) == 1
   and {by[1]['italian']}
   == {u['italian'] for u in json.load(open(PREV269, encoding='utf-8'))['units']
       if u['english'] == by[1]['english']})
ck('la nota del montaggio (unita 5, 17) e IDENTICA a quella di L268 e ripetuta due volte',
   len({by[5]['italian'], by[17]['italian']}) == 1
   and {by[5]['italian']}
   == {u['italian'] for u in json.load(open(PREV268, encoding='utf-8'))['units']
       if u['english'] == by[5]['english']})
ck('APICI in inglese: 7 (unita 6 x2, 7, 9, 10, 11, 15)',
   {u['idx']: u['english'].count(APOS) for u in cov if APOS in u['english']}
   == {6: 2, 7: 1, 9: 1, 10: 1, 11: 1, 15: 1},
   {u['idx']: u['english'].count(APOS) for u in cov if APOS in u['english']})
ck('APICI in italiano: 8 su 6 unita (unita 9 con tre)',
   sum(u['italian'].count(APOS) for u in cov) == 8
   and {u['idx']: u['italian'].count(APOS) for u in cov if APOS in u['italian']}
   == {1: 1, 3: 1, 4: 1, 6: 1, 9: 3, 16: 1},
   (sum(u['italian'].count(APOS) for u in cov),
    {u['idx']: u['italian'].count(APOS) for u in cov if APOS in u['italian']}))
ck('ZERO virgolette e ZERO segnaposto (due asserzioni negative)',
   sum(u['english'].count(QUOTE) + u['italian'].count(QUOTE) for u in cov) == 0
   and not [t for u in cov for t in TAG.findall(u['english']) + TAG.findall(u['italian'])])
ck('lessico: propulsore atomico / motori atomici, sterzata, propulsore inverso, sezione delle armi',
   'propulsori atomici' in by[6]['italian'] and 'motori atomici' in by[9]['italian']
   and 'sterzata' in by[2]['italian'] and 'propulsore inverso' in by[4]['italian']
   and 'sezione delle armi' in by[5]['italian'])
ck('Deep Sky invariato, e i dieci numeri dei modelli restano nei CONTESTI (non tradotti)',
   'Deep Sky' in by[6]['italian']
   and all(any(n in u['context'] for u in cov) for n in
           ('A120', 'A250', 'A370', 'A520', 'A860', 'A125', 'A255', 'A375', 'A525', 'A865')),
   [n for n in ('A120', 'A250', 'A370', 'A520', 'A860', 'A125', 'A255', 'A375', 'A525', 'A865')
    if not any(n in u['context'] for u in cov)])
ck('un solo numero compare nel TESTO inglese (A860) e resta in quello italiano',
   [(u['idx'], n) for u in cov for n in ('A120', 'A250', 'A370', 'A520', 'A860', 'A125', 'A255', 'A375', 'A525', 'A865')
    if n in u['english']] == [(10, 'A860')] and 'A860' in by[10]['italian'])
ck('le due navi dei propulsori inversi restano: Capybara, AR120',
   'Capybara' in by[4]['context'] and 'AR120' in by[16]['context'])
ck('nessun residuo inglese delle parole chiave',
   not [u['idx'] for u in cov for w in ('thruster', 'steering', 'atomic engines', 'freighter', 'warship', 'reverse')
        if w in u['italian'].lower()],
   [(u['idx'], w) for u in cov for w in ('thruster', 'steering', 'atomic engines', 'freighter', 'warship', 'reverse')
    if w in u['italian'].lower()])
ck('nessun caporale, nessun carattere tipografico',
   not [u['idx'] for u in cov for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026' if c in u['italian']])
nonlat = [(u['idx'], c) for u in cov for c in u['italian'] if ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']],
   [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90 (0,81-1,24)',
   all(0.55 < u['ratio'] < 1.90 for u in cov),
   [(u['idx'], u['ratio']) for u in cov if not 0.55 < u['ratio'] < 1.90])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("44 unita' prima (L267 + L268 + L269)",
   db.execute('select count(*) from units where path=? and line<488', (PATH,)).fetchone()[0] == 44)
ck("ZERO unita' dopo la 717: il lotto CHIUDE il file",
   db.execute('select count(*) from units where path=? and line>717', (PATH,)).fetchone()[0] == 0)
ck('INVARIANTE DI FILE: 61 unita, righe 27-717, ultima unita alla 717',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (61, 27, 717))
somma, righe = 0, set()
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    us = [u for u in json.load(open(f, encoding='utf-8'))['units'] if u['path'] == PATH]
    if us:
        somma += len(us)
        righe |= {u['line'] for u in us}
ck('INVARIANTE DI FILE: somma dei quattro lotti = 61, righe distinte = 61, nessuna riga fuori dal file',
   somma == 61 and len(righe) == 61 and min(righe) == 27 and max(righe) == 717,
   (somma, len(righe), min(righe) if righe else None, max(righe) if righe else None))
st = dict(db.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('tutte le 17 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · 14 contesti' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
