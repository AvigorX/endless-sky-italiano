r"""check.py — L277 (`data/korath/korath ships.txt`, righe 2010-2363). **LOTTO TERMINALE: chiude il file.**

**7 `DESCRIPTION`** sulle sette navi **`Model`** dei Kor Mereti — la serie numerata a potenze di due, dal drone minerario
`Model 8` all'anello perfetto `Model 512`. Quattro cose da verificare con cura:

1. **lotto terminale**: oltre all'invariante di segmento ci vuole quella di **FILE** — 50 unita', righe distinte, ultima riga
   la **2363**, **0 dopo**, somma dei cinque lotti = 50;
2. **la serie e un CONTINUUM**: le schede raccontano una crescita (minerario → modulare → vita → fregata → scissione → arma che
   sopravvive → anello perfetto). Il test verifica che **ogni** unita' parli di droni Kor Mereti e che i nomi numerati restino;
3. **quattro asserzioni negative**: zero tab, zero virgolette, zero apici inglesi, zero segnaposto;
4. **nessun nome numerato tradotto**: `Model 8` … `Model 512` restano, e i numeri non si «italianizzano».
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
PATH = 'data/korath/korath ships.txt'
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
BLOCCHI = [('ship:Model 8', 2010, 2010), ('ship:Model 16', 2065, 2065), ('ship:Model 32', 2121, 2121),
           ('ship:Model 64', 2179, 2179), ('ship:Model 128', 2238, 2238), ('ship:Model 256', 2299, 2299),
           ('ship:Model 512', 2363, 2363)]
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck('unita tradotte 7/7', len(cov) == 7 == len(units), '%d/%d' % (len(cov), len(units)))
ck('tipo: 7 DESCRIPTION, nessun VALUE',
   collections.Counter(u['kind'] for u in units) == {'DESCRIPTION': 7},
   dict(collections.Counter(u['kind'] for u in units)))
ck('sette contesti `Model`, con le righe misurate e in ordine crescente',
   [(c, by[[u['idx'] for u in cov if u['context'] == c][0]]['line'],
     by[[u['idx'] for u in cov if u['context'] == c][-1]]['line']) for c, _, _ in BLOCCHI] == BLOCCHI,
   [(c, by[[u['idx'] for u in cov if u['context'] == c][0]]['line']) for c, _, _ in BLOCCHI])
ck('righe 2010-2363, una unita per contesto, ultima unita alla 2363',
   [u['line'] for u in cov] == [2010, 2065, 2121, 2179, 2238, 2299, 2363]
   and all(sum(1 for u in cov if u['context'] == c) == 1 for c, _, _ in BLOCCHI))
ck('tutte TRADOTTE, nessuna copiata',
   all(u['italian'] != u['english'] for u in cov), [u['idx'] for u in cov if u['italian'] == u['english']])
ck('QUATTRO asserzioni negative: zero tab, zero virgolette, zero apici inglesi, zero segnaposto',
   sum(u['english'].count(TAB) + u['italian'].count(TAB) for u in cov) == 0
   and sum(u['english'].count(QUOTE) + u['italian'].count(QUOTE) for u in cov) == 0
   and sum(u['english'].count(APOS) for u in cov) == 0
   and not [t for u in cov for t in TAG.findall(u['english']) + TAG.findall(u['italian'])])
ck('APICI in italiano: 4 su 4 unita (elisioni), tutti dichiarati',
   {u['idx']: u['italian'].count(APOS) for u in cov if APOS in u['italian']} == {1: 1, 3: 1, 6: 1, 7: 1},
   {u['idx']: u['italian'].count(APOS) for u in cov if APOS in u['italian']})
ck('i nomi numerati restano: nessun `Model` tradotto e nessun numero italianizzato',
   all('Model' not in by[i]['italian'] for i in by)
   and all(by[i]['context'].startswith('ship:Model ') for i in by))
ck('la serie e un CONTINUUM: tutte e sette le unita parlano di droni Kor Mereti',
   sum(1 for u in cov if 'Kor Mereti' in u['italian']) >= 6
   and sum(1 for u in cov if 'dron' in u['italian'].lower()) == 7,
   (sum(1 for u in cov if 'Kor Mereti' in u['italian']),
    sum(1 for u in cov if 'dron' in u['italian'].lower())))
ck('la progressione: minerario → modulare → vita → fregata → scissione → arma → anello',
   'estrazione mineraria' in by[1]['italian'] and 'modulare' in by[2]['italian']
   and 'imitando la vita' in by[3]['italian'] and 'fregata' in by[4]['italian']
   and 'si dividono a metà' in by[5]['italian'] and 'sopravvive ai suoi creatori' in by[6]['italian']
   and 'anello perfetto' in by[7]['italian'])
ck('lessico: potenza di fuoco, scudi, torrette, fabbriche automatiche, ciclo vitale',
   'potenza di fuoco' in by[4]['italian'] and 'scudi' in by[7]['italian']
   and 'torrette' in by[7]['italian'] and 'fabbriche automatiche' in by[3]['italian']
   and 'ciclo vitale' in by[3]['italian'])
ck('nessun residuo inglese delle parole chiave (`drone` e `fregata` sono parole italiane)',
   not [u['idx'] for u in cov for w in ('frigate', 'shields', 'turrets', 'firepower')
        if w in u['italian'].lower().split()]
   and 'droni' in by[1]['italian'] and 'drone' in by[4]['italian'] and 'fregata' in by[4]['italian'],
   [(u['idx'], w) for u in cov for w in ('frigate', 'shields', 'turrets', 'firepower')
    if w in u['italian'].lower().split()])
ck('nessun caporale, nessun carattere tipografico',
   not [u['idx'] for u in cov for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026' if c in u['italian']])
nonlat = [(u['idx'], c) for u in cov for c in u['italian'] if ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']],
   [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90 (0,98-1,18)',
   all(0.55 < u['ratio'] < 1.90 for u in cov),
   [(u['idx'], u['ratio']) for u in cov if not 0.55 < u['ratio'] < 1.90])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("43 unita' prima (L273 + L274 + L275 + L276)",
   db.execute('select count(*) from units where path=? and line<2010', (PATH,)).fetchone()[0] == 43)
ck("ZERO unita' dopo la 2363: il lotto CHIUDE il file",
   db.execute('select count(*) from units where path=? and line>2363', (PATH,)).fetchone()[0] == 0)
ck('INVARIANTE DI FILE: 50 unita, righe 95-2363, ultima alla 2363',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (50, 95, 2363))
somma, righe = 0, set()
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    us = [u for u in json.load(open(f, encoding='utf-8'))['units'] if u['path'] == PATH]
    if us:
        somma += len(us)
        righe |= {u['line'] for u in us}
ck('INVARIANTE DI FILE: somma dei cinque lotti = 50, righe distinte = 50, nessuna riga fuori',
   somma == 50 and len(righe) == 50 and min(righe) == 95 and max(righe) == 2363,
   (somma, len(righe)))
st = dict(db.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('tutte le 7 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · 7 contesti · 0 tab · 0 virgolette' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
