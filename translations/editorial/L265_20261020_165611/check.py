r"""check.py — L265 (`data/kahet/aberrant ships.txt`, righe 16-685). Primo lotto del file.

**Lotto di navi**: 26 `VALUE` (sigle e nomi: `K-IA "Latte"`, `Lattes`, `K-IB "Chomper"`, …) si **copiano**, 17
`DESCRIPTION` si **traducono**. Le **32 virgolette** del lotto stanno tutte nelle designazioni, e la riga **15** (unita'
`K-IC Pileup`) e' l'unica **senza virgolette**: il sorgente varia, e la resa non-uniforma va conservata.

Le 17 schede sono **9 stringhe distinte**: una nota organo-metallica ripetuta **9 volte** e otto frasi sulla variante. Il
controllo verifica che i gruppi identici abbiano **una sola resa**.
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
PATH = 'data/kahet/aberrant ships.txt'
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
BLOCCHI = [('Aberrant Latte', 16, 82), ('Aberrant Chomper', 87, 160), ('Aberrant Pileup', 165, 232),
           ('Aberrant Hugger', 237, 306), ('Aberrant Longfellow', 311, 386), ('Aberrant Dancer', 391, 464),
           ('Aberrant Junior', 469, 539), ('Aberrant Icebreaker', 544, 615), ('Aberrant Pike', 620, 685)]
NOTE = [3, 8, 13, 18, 23, 28, 33, 38, 43]
VARIANTI = [4, 9, 14, 19, 24, 29, 34, 39]
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck('unita tradotte 43/43', len(cov) == 43 == len(units), '%d/%d' % (len(cov), len(units)))
ck('tipi: 26 VALUE + 17 DESCRIPTION',
   collections.Counter(u['kind'] for u in units) == {'VALUE': 26, 'DESCRIPTION': 17},
   dict(collections.Counter(u['kind'] for u in units)))
ck('nove contesti, uno per nave, con le righe misurate',
   [(c, by[[u['idx'] for u in cov if u['context'] == 'ship:' + c][0]]['line'],
     by[[u['idx'] for u in cov if u['context'] == 'ship:' + c][-1]]['line']) for c, _, _ in BLOCCHI] == BLOCCHI,
   [(c, by[[u['idx'] for u in cov if u['context'] == 'ship:' + c][0]]['line']) for c, _, _ in BLOCCHI])
ck('righe 16-685, nessun buco interno',
   [u['line'] for u in cov] == sorted({u['line'] for u in cov})
   and cov[0]['line'] == 16 and cov[-1]['line'] == 685)
ck('i 26 VALUE sono COPIATI, identici per indice (sigle e nomi)',
   [u['idx'] for u in cov if u['kind'] == 'VALUE'] ==
   [1, 2, 5, 6, 7, 10, 11, 12, 15, 16, 17, 20, 21, 22, 25, 26, 27, 30, 31, 32, 35, 36, 37, 40, 41, 42]
   and all(u['italian'] == u['english'] for u in cov if u['kind'] == 'VALUE'),
   [u['idx'] for u in cov if u['kind'] == 'VALUE' and u['italian'] != u['english']])
ck('le 17 DESCRIPTION sono TRADOTTE, nessuna copiata',
   all(u['italian'] != u['english'] for u in cov if u['kind'] == 'DESCRIPTION'),
   [u['idx'] for u in cov if u['kind'] == 'DESCRIPTION' and u['italian'] == u['english']])
ck('le 9 note organo-metalliche hanno UNA sola resa',
   len({by[i]['italian'] for i in NOTE}) == 1
   and len({by[i]['english'] for i in NOTE}) == 1
   and 'organo-metallica' in by[3]['italian'],
   len({by[i]['italian'] for i in NOTE}))
ck('le 8 frasi sulla variante sono distinte, ognuna con la sua resa',
   len({by[i]['italian'] for i in VARIANTI}) == 8 and len({by[i]['english'] for i in VARIANTI}) == 8
   and all('variante' in by[i]['italian'] for i in VARIANTI))
ck('VIRGOLETTE: 32 in inglese e 32 in italiano, per unita identiche',
   sum(u['english'].count(QUOTE) for u in cov) == 32 == sum(u['italian'].count(QUOTE) for u in cov)
   and {u['idx']: u['english'].count(QUOTE) for u in cov if QUOTE in u['english']}
   == {u['idx']: u['italian'].count(QUOTE) for u in cov if QUOTE in u['italian']},
   ({u['idx']: u['english'].count(QUOTE) for u in cov if QUOTE in u['english']},
    {u['idx']: u['italian'].count(QUOTE) for u in cov if QUOTE in u['italian']}))
ck('i 10 VALUE senza virgolette sono i 9 plurali e la sigla nuda `K-IC Pileup` (unita 15)',
   [u['idx'] for u in cov if u['kind'] == 'VALUE' and QUOTE not in u['english']] == [2, 7, 12, 15, 17, 22, 27, 32, 37, 42]
   and [u['idx'] for u in cov if u['kind'] == 'VALUE' and QUOTE not in u['english']
        and u['english'].startswith('K-')] == [15]
   and by[15]['italian'] == by[15]['english'] == 'K-IC Pileup',
   [u['idx'] for u in cov if u['kind'] == 'VALUE' and QUOTE not in u['english']])
ck('ZERO tab e ZERO segnaposto (asserzioni negative)',
   sum(u['english'].count(TAB) + u['italian'].count(TAB) for u in cov) == 0
   and not [t for u in cov for t in TAG.findall(u['english']) + TAG.findall(u['italian'])])
ck('APICI: ZERO in inglese; in italiano solo le elisioni (elencate)',
   sum(u['english'].count(APOS) for u in cov) == 0
   and {u['idx']: u['italian'].count(APOS) for u in cov if APOS in u['italian']}
   == {3: 1, 8: 1, 13: 1, 14: 1, 18: 1, 23: 1, 28: 1, 33: 1, 38: 1, 43: 1},
   {u['idx']: u['italian'].count(APOS) for u in cov if APOS in u['italian']})
ck('lessico: organo-metallica, variante, fusoliera, punti di attacco, scafo',
   'organo-metallica' in by[3]['italian'] and 'fusoliera' in by[24]['italian']
   and 'punti di attacco' in by[29]['italian'] and 'scafo' in by[39]['italian']
   and 'torrette' in by[29]['italian'])
ck('`Aberrant` resta invariato nella prosa (come `Ka\'het` nel corpus)',
   'navi Aberrant' in by[19]['italian'] and 'Aberrant' not in ' '.join(
       u['italian'] for u in cov if u['kind'] == 'VALUE'))
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
ck("ZERO unita' prima della 16: il lotto APRE il file",
   db.execute('select count(*) from units where path=? and line<16', (PATH,)).fetchone()[0] == 0)
ck("22 unita' dopo la 685",
   db.execute('select count(*) from units where path=? and line>685', (PATH,)).fetchone()[0] == 22)
ck('il file ha 65 unita, righe 16-1007',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (65, 16, 1007))
st = dict(db.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('tutte le 43 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · 9 contesti · 32 virgolette' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
