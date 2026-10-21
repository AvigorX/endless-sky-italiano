r"""check.py — L257 (`data/human/post-war reactions.txt`, righe 76-151). Secondo lotto del file.

**Due contesti**: le unita' 1-9 chiudono `War Reactions: Asteroid Miners`, le 10-23 aprono
`War Reactions: Navy and Free Worlds Captains`. Il `check.py` non assume un contesto unico.

Tre cose vanno verificate **per unita'**, non sul totale:
- **22 tab** di rientro (tutte tranne la 10, che e' la descrizione d'ambiente che apre la nuova missione);
- **45 virgolette** — e la **12 ne ha TRE**, non quattro: il sorgente apre una citazione lunga e **non la chiude**.
  La resa lo riproduce **com'è**: chiuderla sarebbe un «miglioramento» che altera il testo del gioco;
- **17 apici** inglesi contro **5** italiani.

I segnaposto sono **nomi del giocatore** (`<first>`, `<last>`, `<ship>`): invariati, nello **stesso ordine per unita'**.
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
CTX_A = 'mission:War Reactions: Asteroid Miners'
CTX_B = 'mission:War Reactions: Navy and Free Worlds Captains'
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
QUOTES = {1: 2, 2: 2, 3: 2, 4: 2, 5: 2, 7: 2, 11: 4, 12: 3, 13: 2, 14: 2, 15: 2, 16: 2, 17: 2, 18: 2,
          19: 2, 20: 2, 21: 4, 22: 4, 23: 2}
TABBED = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
APOS_EN = {1: 1, 3: 1, 4: 1, 9: 2, 11: 1, 12: 2, 13: 2, 19: 1, 20: 1, 21: 2, 22: 1, 23: 2}
APOS_IT = {10: 1, 12: 1, 22: 1, 23: 2}
TOK_EN = {'<first>': 1, '<last>': 3, '<ship>': 1}
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck('unita tradotte 23/23', len(cov) == 23 == len(units), '%d/%d' % (len(cov), len(units)))
ck('tipo: 23 MISSION_TEXT', collections.Counter(u['kind'] for u in units) == {'MISSION_TEXT': 23},
   dict(collections.Counter(u['kind'] for u in units)))
ck('DUE contesti: 9 Asteroid Miners (1-9) poi 14 Navy and Free Worlds (10-23)',
   [(u['idx'], u['context']) for u in cov if u['idx'] == 9 or u['idx'] == 10]
   == [(9, CTX_A), (10, CTX_B)]
   and collections.Counter(u['context'] for u in cov) == {CTX_A: 9, CTX_B: 14},
   dict(collections.Counter(u['context'] for u in cov)))
ck('righe 76-151, nessun buco interno',
   [u['line'] for u in cov] == sorted({u['line'] for u in cov}) and cov[0]['line'] == 76 and cov[-1]['line'] == 151)
ck('tutte TRADOTTE, nessuna copiata', not [u for u in cov if u['italian'] == u['english']],
   [u['idx'] for u in cov if u['italian'] == u['english']])
ck('TAB: 22 in inglese, 22 in italiano, sulle stesse unita, e la 10 e l\'unica senza',
   sum(u['english'].count(TAB) for u in cov) == 22 == sum(u['italian'].count(TAB) for u in cov)
   and [u['idx'] for u in cov if TAB in u['english']] == TABBED
   == [u['idx'] for u in cov if TAB in u['italian']],
   ([u['idx'] for u in cov if TAB in u['english']], [u['idx'] for u in cov if TAB in u['italian']]))
ck('il tab e il PRIMO carattere dove c\'e\'',
   all(u['italian'].startswith(TAB) for u in cov if u['idx'] in TABBED)
   and not by[10]['italian'].startswith(TAB))
ck('VIRGOLETTE: 45 in inglese, 45 in italiano, mappa per unita identica',
   {u['idx']: u['english'].count(QUOTE) for u in cov if QUOTE in u['english']} == QUOTES
   == {u['idx']: u['italian'].count(QUOTE) for u in cov if QUOTE in u['italian']},
   ({u['idx']: u['english'].count(QUOTE) for u in cov if QUOTE in u['english']},
    {u['idx']: u['italian'].count(QUOTE) for u in cov if QUOTE in u['italian']}))
ck("la 12 ha TRE virgolette in entrambe le lingue: citazione aperta e non chiusa, riprodotta come sta",
   by[12]['english'].count(QUOTE) == 3 == by[12]['italian'].count(QUOTE)
   and by[12]['english'].rstrip().endswith('!') and by[12]['italian'].rstrip().endswith('!'))
ck('APICI: 17 in inglese (12 unita), 5 in italiano (4 unita), mappe dichiarate',
   {u['idx']: u['english'].count(APOS) for u in cov if APOS in u['english']} == APOS_EN
   and {u['idx']: u['italian'].count(APOS) for u in cov if APOS in u['italian']} == APOS_IT,
   ({u['idx']: u['english'].count(APOS) for u in cov if APOS in u['english']},
    {u['idx']: u['italian'].count(APOS) for u in cov if APOS in u['italian']}))
ck('SEGNAPOSTO: <first> 1, <last> 3, <ship> 1, e ORDINE identico per unita',
   collections.Counter(t for u in cov for t in TAG.findall(u['english'])) == TOK_EN
   == collections.Counter(t for u in cov for t in TAG.findall(u['italian']))
   and not [u['idx'] for u in cov
            if TAG.findall(u['english']) != TAG.findall(u['italian'])],
   ([u['idx'] for u in cov if TAG.findall(u['english']) != TAG.findall(u['italian'])],
    dict(collections.Counter(t for u in cov for t in TAG.findall(u['italian'])))))
ck('lessico: Marina, Free Worlds, Pug invariati; «capitano» per Captain',
   'Marina' in by[10]['italian'] and 'Free Worlds' in by[10]['italian']
   and 'Pug' in by[12]['italian'] and 'capitano' in by[11]['italian'].lower()
   and 'Navy' not in by[10]['italian'])
ck('nomi propri invariati: Rain, Fiona, Camuy, Baobab, Spider Funk',
   all(w in ' '.join(u['italian'] for u in cov)
       for w in ('Rain', 'Fiona', 'R.N.S. Camuy', 'F.S. Baobab', 'Spider Funk')))
ck('nessun caporale, nessun carattere tipografico',
   not [u['idx'] for u in cov for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026' if c in u['italian']])
nonlat = [(u['idx'], c) for u in cov for c in u['italian'] if ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']],
   [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90 (0,82-1,30)',
   all(0.55 < u['ratio'] < 1.90 for u in cov),
   [(u['idx'], u['ratio']) for u in cov if not 0.55 < u['ratio'] < 1.90])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("22 unita' prima (L256), quindi la 76 prosegue lo stesso contesto",
   db.execute('select count(*) from units where path=? and line<76', (PATH,)).fetchone()[0] == 22
   and db.execute('select context from units where path=? and line<76 order by line desc limit 1', (PATH,)).fetchone()
   == (CTX_A,))
ck("42 unita' dopo la 151",
   db.execute('select count(*) from units where path=? and line>151', (PATH,)).fetchone()[0] == 42)
ck('il file ha 87 unita, righe 40-264',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (87, 40, 264))
st = dict(db.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('tutte le 23 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · contesti 9 + 14' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
