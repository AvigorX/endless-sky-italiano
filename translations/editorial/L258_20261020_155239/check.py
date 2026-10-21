r"""check.py — L258 (`data/human/post-war reactions.txt`, righe 152-215). Terzo lotto del file.

**Due contesti**, con il **secondo cambio di missione** del file: le unita' 1-11 chiudono `Navy and Free Worlds Captains`,
la **12** (senza tab, descrizione d'ambiente) apre `Syndicate Orphan`.

Da verificare **per unita'**:
- **19 tab** su 20 unita': la **12** e' l'unica non rientrata;
- **45 virgolette**, e la **5 ne ha TRE**: `Rain adds, "Only metaphorically up in arms, this time.` — citazione aperta e
  **non chiusa** nel sorgente, riprodotta com'e' (secondo caso dopo L257);
- **18 apici** inglesi contro **12** italiani;
- **zero segnaposto**: asserzione negativa scritta.

Il testo introduce navi e istituzioni nuove per il file: `Dreadnought` -> «corazzata», `Auxiliary` -> «ausiliaria»,
`Cruiser` -> «incrociatore», `Navy Academy` -> «Accademia della Marina», `Republic Parliament` -> «Parlamento della
Repubblica».
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
PATH = 'data/human/post-war reactions.txt'
CTX_A = 'mission:War Reactions: Navy and Free Worlds Captains'
CTX_B = 'mission:War Reactions: Syndicate Orphan'
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
QUOTES = {1: 2, 2: 2, 3: 4, 4: 2, 5: 3, 6: 2, 7: 4, 8: 2, 9: 4, 10: 2, 11: 4, 13: 2, 16: 4,
          17: 2, 18: 2, 19: 2, 20: 2}
TABBED = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20]
APOS_EN = {6: 1, 7: 2, 8: 1, 9: 1, 11: 1, 12: 2, 16: 4, 18: 1, 19: 2, 20: 3}
APOS_IT = {1: 1, 3: 2, 10: 1, 12: 3, 15: 1, 16: 2, 18: 2}
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck('unita tradotte 20/20', len(cov) == 20 == len(units), '%d/%d' % (len(cov), len(units)))
ck('tipo: 20 MISSION_TEXT', collections.Counter(u['kind'] for u in units) == {'MISSION_TEXT': 20},
   dict(collections.Counter(u['kind'] for u in units)))
ck('DUE contesti: 11 unita poi 9, con il cambio esatto alla 12',
   [(u['idx'], u['context']) for u in cov if u['idx'] in (11, 12)] == [(11, CTX_A), (12, CTX_B)]
   and collections.Counter(u['context'] for u in cov) == {CTX_A: 11, CTX_B: 9},
   dict(collections.Counter(u['context'] for u in cov)))
ck('righe 152-215, nessun buco interno',
   [u['line'] for u in cov] == sorted({u['line'] for u in cov})
   and cov[0]['line'] == 152 and cov[-1]['line'] == 215)
ck('tutte TRADOTTE, nessuna copiata', not [u for u in cov if u['italian'] == u['english']],
   [u['idx'] for u in cov if u['italian'] == u['english']])
ck('TAB: 19 in inglese, 19 in italiano, stesse unita; la 12 e l\'unica senza',
   sum(u['english'].count(TAB) for u in cov) == 19 == sum(u['italian'].count(TAB) for u in cov)
   and [u['idx'] for u in cov if TAB in u['english']] == TABBED
   == [u['idx'] for u in cov if TAB in u['italian']]
   and not by[12]['italian'].startswith(TAB),
   ([u['idx'] for u in cov if TAB in u['english']], [u['idx'] for u in cov if TAB in u['italian']]))
ck('il tab e il PRIMO carattere dove c\'e\'',
   all(u['italian'].startswith(TAB) for u in cov if u['idx'] in TABBED))
ck('VIRGOLETTE: 45 in inglese, 45 in italiano, mappa per unita identica',
   {u['idx']: u['english'].count(QUOTE) for u in cov if QUOTE in u['english']} == QUOTES
   == {u['idx']: u['italian'].count(QUOTE) for u in cov if QUOTE in u['italian']},
   ({u['idx']: u['english'].count(QUOTE) for u in cov if QUOTE in u['english']},
    {u['idx']: u['italian'].count(QUOTE) for u in cov if QUOTE in u['italian']}))
ck('la 5 ha TRE virgolette in entrambe le lingue: citazione aperta e non chiusa, riprodotta',
   by[5]['english'].count(QUOTE) == 3 == by[5]['italian'].count(QUOTE)
   and by[5]['english'].rstrip().endswith('.') and by[5]['italian'].rstrip().endswith('.'),
   (by[5]['english'].count(QUOTE), by[5]['italian'].count(QUOTE)))
ck('APICI: 18 in inglese (10 unita), 12 in italiano (7 unita), mappe dichiarate',
   {u['idx']: u['english'].count(APOS) for u in cov if APOS in u['english']} == APOS_EN
   and {u['idx']: u['italian'].count(APOS) for u in cov if APOS in u['italian']} == APOS_IT,
   ({u['idx']: u['english'].count(APOS) for u in cov if APOS in u['english']},
    {u['idx']: u['italian'].count(APOS) for u in cov if APOS in u['italian']}))
ck('ZERO segnaposto in inglese e in italiano (asserzione negativa)',
   not [t for u in cov for t in TAG.findall(u['english']) + TAG.findall(u['italian'])])
ck('navi e istituzioni: corazzata, ausiliaria, incrociatore, Accademia della Marina',
   'corazzata' in by[1]['italian'] and 'ausiliaria' in by[1]['italian']
   and 'incrociatore' in by[7]['italian'] and 'Accademia della Marina' in by[10]['italian']
   and 'Dreadnought' not in by[1]['italian'] and 'Auxiliary' not in by[1]['italian'])
ck('istituzioni tradotte: Senato dei Free Worlds, Parlamento della Repubblica',
   'Senato dei Free Worlds' in by[5]['italian'] and 'Parlamento della Repubblica' in by[5]['italian'])
ck('nomi propri invariati: Rain, Fiona, Longjump, Gus, Free Worlds, Repubblica, Terra',
   all(w in ' '.join(u['italian'] for u in cov)
       for w in ('Rain', 'Fiona', 'Longjump', 'Gus', 'Free Worlds', 'Repubblica', 'Terra')))
ck('nessun caporale, nessun carattere tipografico',
   not [u['idx'] for u in cov for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026' if c in u['italian']])
nonlat = [(u['idx'], c) for u in cov for c in u['italian'] if ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']],
   [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90 (0,81-1,26)',
   all(0.55 < u['ratio'] < 1.90 for u in cov),
   [(u['idx'], u['ratio']) for u in cov if not 0.55 < u['ratio'] < 1.90])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("45 unita' prima (L256 + L257), quindi la 152 prosegue il contesto aperto alla 110",
   db.execute('select count(*) from units where path=? and line<152', (PATH,)).fetchone()[0] == 45
   and db.execute('select context from units where path=? and line<152 order by line desc limit 1', (PATH,)).fetchone()
   == (CTX_A,))
ck("22 unita' dopo la 215",
   db.execute('select count(*) from units where path=? and line>215', (PATH,)).fetchone()[0] == 22)
ck('il file ha 87 unita, righe 40-264',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (87, 40, 264))
st = dict(db.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('tutte le 20 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · contesti 11 + 9' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
