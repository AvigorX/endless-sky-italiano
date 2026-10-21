r"""check.py — L268 (`data/human/engines.txt`, righe 195-323). Secondo lotto del file.

**15 `DESCRIPTION`, nessun `VALUE`**: propulsori ionici grossi, sei sistemi di sterzata e un **propulsore inverso**.
Tre cose da verificare con cura:

1. **otto tab**, uno per blocco (unita' 1, 3, 5, 7, 9, 11, 13, 15): il tab e' il primo carattere e va conservato;
2. **la scheda ionica si ripete sette volte** (1, 3, 5, 7, 9, 11, 13) ed e' **identica a quella di L267**: si riprende alla
   lettera rileggendo quel `translation.json`;
3. **«propulsore inverso»** e' nuova: `reverse thruster` non esisteva nel corpus, e la scelta va dichiarata (e' fissata qui).
"""
import collections
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
PREV = os.path.join(L10N, 'staging', 'editorial', 'L267_20261020_170814', 'translation.json')
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
BLOCCHI = [('outfit:X4700 Ion Thruster', 195, 195), ('outfit:X5700 Ion Thruster', 212, 213),
           ('outfit:X1200 Ion Steering', 231, 232), ('outfit:X2200 Ion Steering', 249, 250),
           ('outfit:X3200 Ion Steering', 267, 268), ('outfit:X4200 Ion Steering', 285, 286),
           ('outfit:X5200 Ion Steering', 303, 304), ('outfit:X1100 Ion Reverse Thruster', 322, 323)]
IONICA = [1, 3, 5, 7, 9, 11, 13]
TABBED = [1, 3, 5, 7, 9, 11, 13, 15]
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck('unita tradotte 15/15', len(cov) == 15 == len(units), '%d/%d' % (len(cov), len(units)))
ck('tipo: 15 DESCRIPTION, nessun VALUE',
   collections.Counter(u['kind'] for u in units) == {'DESCRIPTION': 15},
   dict(collections.Counter(u['kind'] for u in units)))
ck('otto contesti, con le righe misurate',
   [(c, by[[u['idx'] for u in cov if u['context'] == c][0]]['line'],
     by[[u['idx'] for u in cov if u['context'] == c][-1]]['line']) for c, _, _ in BLOCCHI] == BLOCCHI,
   [(c, by[[u['idx'] for u in cov if u['context'] == c][0]]['line']) for c, _, _ in BLOCCHI])
ck('righe 195-323, nessun buco interno',
   [u['line'] for u in cov] == sorted({u['line'] for u in cov})
   and cov[0]['line'] == 195 and cov[-1]['line'] == 323)
ck('tutte TRADOTTE, nessuna copiata',
   all(u['italian'] != u['english'] for u in cov if u['kind'] == 'DESCRIPTION'),
   [u['idx'] for u in cov if u['italian'] == u['english']])
ck('TAB: otto in inglese e otto in italiano, sulle stesse unita, come PRIMO carattere',
   sum(u['english'].count(TAB) for u in cov) == 8 == sum(u['italian'].count(TAB) for u in cov)
   and [u['idx'] for u in cov if TAB in u['english']] == TABBED == [u['idx'] for u in cov if TAB in u['italian']]
   and all(u['italian'].startswith(TAB) for u in cov if u['idx'] in TABBED))
ck("la scheda ionica (7 copie) e IDENTICA a quella di L267, riletto il suo translation.json",
   len({by[i]['italian'] for i in IONICA}) == 1
   and {by[i]['italian'] for i in IONICA}
   == {u['italian'] for u in json.load(open(PREV, encoding='utf-8'))['units']
       if u['english'] == by[1]['english']},
   {by[i]['italian'][:60] for i in IONICA})
ck('ZERO virgolette, ZERO apici in inglese, ZERO segnaposto (tre asserzioni negative)',
   sum(u['english'].count(QUOTE) + u['italian'].count(QUOTE) for u in cov) == 0
   and sum(u['english'].count(APOS) for u in cov) == 0
   and not [t for u in cov for t in TAG.findall(u['english']) + TAG.findall(u['italian'])])
ck('APICI in italiano: 6, uno per unita, tutti elisioni dichiarate',
   {u['idx']: u['italian'].count(APOS) for u in cov if APOS in u['italian']}
   == {2: 1, 4: 1, 6: 1, 10: 1, 12: 1, 14: 1},
   {u['idx']: u['italian'].count(APOS) for u in cov if APOS in u['italian']})
ck('lessico: sterzata, propulsore inverso, nave capitale, mercantili, droni, caccia',
   'sterzata' in by[4]['italian'] and 'propulsore inverso' in by[14]['italian']
   and 'navi capitali' in by[2]['italian'] and 'mercantili' in by[8]['italian']
   and 'droni' in by[4]['italian'] and 'caccia' in by[6]['italian'])
ck('il propulsore inverso spiega il montaggio nella sezione delle armi',
   'sezione delle armi' in by[15]['italian'] and 'dei motori' in by[15]['italian']
   and 'anziché' in by[15]['italian'])
ck('nessun residuo inglese delle parole chiave nelle rese',
   not [u['idx'] for u in cov for w in ('thruster', 'steering', 'reverse', 'warship', 'freighter')
        if w in u['italian'].lower()],
   [(u['idx'], w) for u in cov for w in ('thruster', 'steering', 'reverse', 'warship', 'freighter')
    if w in u['italian'].lower()])
ck('nessun caporale, nessun carattere tipografico',
   not [u['idx'] for u in cov for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026' if c in u['italian']])
nonlat = [(u['idx'], c) for u in cov for c in u['italian'] if ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']],
   [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90 (0,96-1,28)',
   all(0.55 < u['ratio'] < 1.90 for u in cov),
   [(u['idx'], u['ratio']) for u in cov if not 0.55 < u['ratio'] < 1.90])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("12 unita' prima (L267), e l'ultima prima della 195 e lo stesso equipaggiamento (X4700)",
   db.execute('select count(*) from units where path=? and line<195', (PATH,)).fetchone()[0] == 12
   and db.execute('select context from units where path=? and line<195 order by line desc limit 1', (PATH,)).fetchone()
   == ('outfit:X4700 Ion Thruster',))
ck("34 unita' dopo la 323",
   db.execute('select count(*) from units where path=? and line>323', (PATH,)).fetchone()[0] == 34)
ck('il file ha 61 unita, righe 27-717',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (61, 27, 717))
st = dict(db.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('tutte le 15 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · 8 contesti' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
