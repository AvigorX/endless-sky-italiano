r"""check.py — L269 (`data/human/engines.txt`, righe 342-487). Terzo lotto del file.

**17 `DESCRIPTION`, nessun `VALUE`**: cinque propulsori e quattro sterzate **al plasma**, piu' la nota che li accompagna.
Tre cose da verificare con cura:

1. **otto tab** sulle unita' pari (2, 4, 6, 8, 10, 12, 14, 16): la nota e' sempre **rientrata**, la scheda del modello no;
   l'ultimo blocco (Orca steering, riga 487) ha **solo** la nota, senza la scheda del modello;
2. **la nota del plasma si ripete otto volte** ed e' **una sola stringa**: una sola resa, verificata come insieme;
3. **un apice in inglese** (`Delta V's`, unita' 13) e **dieci in italiano** (otto `un po'` nella nota, `L'enorme`,
   `un'ampia`).
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
BLOCCHI = [('outfit:Chipmunk Plasma Thruster', 342, 343), ('outfit:Greyhound Plasma Thruster', 360, 361),
           ('outfit:Impala Plasma Thruster', 378, 379), ('outfit:Orca Plasma Thruster', 396, 397),
           ('outfit:Tyrant Plasma Thruster', 414, 415), ('outfit:Chipmunk Plasma Steering', 433, 434),
           ('outfit:Greyhound Plasma Steering', 451, 452), ('outfit:Impala Plasma Steering', 469, 470),
           ('outfit:Orca Plasma Steering', 487, 487)]
NOTA = [2, 4, 6, 8, 10, 12, 14, 16]
MODELLI = [1, 3, 5, 7, 9, 11, 13, 15, 17]
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck('unita tradotte 17/17', len(cov) == 17 == len(units), '%d/%d' % (len(cov), len(units)))
ck('tipo: 17 DESCRIPTION, nessun VALUE',
   collections.Counter(u['kind'] for u in units) == {'DESCRIPTION': 17},
   dict(collections.Counter(u['kind'] for u in units)))
ck('nove contesti, con le righe misurate',
   [(c, by[[u['idx'] for u in cov if u['context'] == c][0]]['line'],
     by[[u['idx'] for u in cov if u['context'] == c][-1]]['line']) for c, _, _ in BLOCCHI] == BLOCCHI,
   [(c, by[[u['idx'] for u in cov if u['context'] == c][0]]['line']) for c, _, _ in BLOCCHI])
ck('righe 342-487, nessun buco interno',
   [u['line'] for u in cov] == sorted({u['line'] for u in cov})
   and cov[0]['line'] == 342 and cov[-1]['line'] == 487)
ck('tutte TRADOTTE, nessuna copiata',
   all(u['italian'] != u['english'] for u in cov), [u['idx'] for u in cov if u['italian'] == u['english']])
ck('TAB: otto in inglese e otto in italiano, sulle sole unita della NOTA, come PRIMO carattere',
   sum(u['english'].count(TAB) for u in cov) == 8 == sum(u['italian'].count(TAB) for u in cov)
   and [u['idx'] for u in cov if TAB in u['english']] == NOTA
   == [u['idx'] for u in cov if TAB in u['italian']]
   and all(u['italian'].startswith(TAB) for u in cov if u['idx'] in NOTA))
ck('nessun tab nelle nove schede di modello',
   not [i for i in MODELLI if TAB in by[i]['italian']])
ck("la nota del plasma (8 copie) ha UNA sola resa", len({by[i]['italian'] for i in NOTA}) == 1,
   len({by[i]['italian'] for i in NOTA}))
ck("l'ottava copia (riga 487) e una nota SENZA scheda di modello: e' l'ultima unita del lotto",
   by[17]['context'] == 'outfit:Orca Plasma Steering' and by[17]['line'] == 487
   and not by[17]['italian'].startswith(TAB) and by[16]['line'] == 470)
ck('APICI in inglese: 1, all unita 13 (`Delta V\'s`)',
   {u['idx']: u['english'].count(APOS) for u in cov if APOS in u['english']} == {13: 1},
   {u['idx']: u['english'].count(APOS) for u in cov if APOS in u['english']})
ck("APICI in italiano: 11 (otto `un po'` + `L'enorme` e `l'immagine` + `un'ampia`)",
   sum(u['italian'].count(APOS) for u in cov) == 11
   and {u['idx']: u['italian'].count(APOS) for u in cov if APOS in u['italian']}
   == dict([(i, 1) for i in NOTA] + [(9, 2), (13, 1)]),
   (sum(u['italian'].count(APOS) for u in cov),
    {u['idx']: u['italian'].count(APOS) for u in cov if APOS in u['italian']}))
ck('ZERO virgolette e ZERO segnaposto (due asserzioni negative)',
   sum(u['english'].count(QUOTE) + u['italian'].count(QUOTE) for u in cov) == 0
   and not [t for u in cov for t in TAG.findall(u['english']) + TAG.findall(u['italian'])])
ck('lessico: propulsore al plasma, sterzata al plasma, motori al plasma, motori ionici',
   'propulsione al plasma' in by[1]['italian'] and 'sterzata al plasma' in by[11]['italian']
   and 'motori al plasma' in by[2]['italian'] and 'motori ionici' in by[2]['italian'])
ck('Delta V, Sindacato e i modelli restano riconoscibili dove l inglese li nomina',
   'Delta V' in by[1]['italian'] and 'Sindacato' in by[15]['italian']
   and not [(u['idx'], n) for u in cov for n in ('Greyhound', 'Impala', 'Orca', 'Tyrant', 'Chipmunk')
            if n in u['english'] and n not in u['italian']],
   [(u['idx'], n) for u in cov for n in ('Greyhound', 'Impala', 'Orca', 'Tyrant', 'Chipmunk')
    if n in u['english'] and n not in u['italian']])
ck('i tre nomi generici NON sono nomi di modello: `greyhound` (il cane), `Tyrannosaurus Rex`, `rodent`',
   'levriero' in by[3]['italian'] and 'Tyrannosaurus Rex' in by[9]['italian']
   and 'roditore' in by[11]['italian'] and 'Greyhound' not in by[3]['italian'])
ck('nessun residuo inglese delle parole chiave',
   not [u['idx'] for u in cov for w in ('thruster', 'steering', 'plasma engines', 'freighter', 'warship')
        if w in u['italian'].lower()],
   [(u['idx'], w) for u in cov for w in ('thruster', 'steering', 'plasma engines', 'freighter', 'warship')
    if w in u['italian'].lower()])
ck('nessun caporale, nessun carattere tipografico',
   not [u['idx'] for u in cov for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026' if c in u['italian']])
nonlat = [(u['idx'], c) for u in cov for c in u['italian'] if ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']],
   [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90',
   all(0.55 < u['ratio'] < 1.90 for u in cov),
   [(u['idx'], u['ratio']) for u in cov if not 0.55 < u['ratio'] < 1.90])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("27 unita' prima (L267 + L268)",
   db.execute('select count(*) from units where path=? and line<342', (PATH,)).fetchone()[0] == 27)
ck("17 unita' dopo la 487, e la prima resta in `Orca Plasma Steering`",
   db.execute('select count(*) from units where path=? and line>487', (PATH,)).fetchone()[0] == 17
   and db.execute('select context from units where path=? and line>487 order by line limit 1', (PATH,)).fetchone()
   == ('outfit:Orca Plasma Steering',))
ck('il file ha 61 unita, righe 27-717',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (61, 27, 717))
st = dict(db.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('tutte le 17 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · 9 contesti' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
