r"""check.py — L266 (`data/kahet/aberrant ships.txt`, righe 686-1007). **LOTTO TERMINALE**: chiude il file a 65/65.

Cinque navi (**Pike** in coda, **Mole**, **Whiskers**, **Trip**, **Triplet**): 13 `VALUE` copiati, 9 `DESCRIPTION`
tradotte. La formula organo-metallica ricorre **4 volte** ed e' **ripresa alla lettera da L265**: il `check.py` rilegge quel
`translation.json` e pretendere l'identita' e' l'unico modo per impedire due rese divergenti della stessa stringa.

La scheda di **Trip** e' anomala: racconta un **difetto di germinazione** («Qualcosa sembra essere andato terribilmente
storto…»), e il controllo verifica che la resa non la presenti come una variante riuscita.

**Invariante di FILE**: `43 + 22 = 65` unita', 65 righe distinte, **1007** ultima riga, **0** dopo.
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
PREV = os.path.join(L10N, 'staging', 'editorial', 'L265_20261020_165611', 'translation.json')
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
NAVI = ['Aberrant Pike', 'Aberrant Mole', 'Aberrant Whiskers', 'Aberrant Trip', 'Aberrant Triplet']
NOTE = [5, 10, 15, 20]
VARIANTI = [1, 6, 11, 16, 21]
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck('unita tradotte 22/22', len(cov) == 22 == len(units), '%d/%d' % (len(cov), len(units)))
ck('tipi: 13 VALUE + 9 DESCRIPTION',
   collections.Counter(u['kind'] for u in units) == {'VALUE': 13, 'DESCRIPTION': 9},
   dict(collections.Counter(u['kind'] for u in units)))
ck('cinque contesti, uno per nave, nell ordine misurato',
   [c.replace('ship:', '') for c in dict.fromkeys(u['context'] for u in cov)] == NAVI,
   [c.replace('ship:', '') for c in dict.fromkeys(u['context'] for u in cov)])
ck('righe 686-1007, la 1007 e l ultima del lotto',
   [u['line'] for u in cov] == sorted({u['line'] for u in cov})
   and cov[0]['line'] == 686 and cov[-1]['line'] == 1007)
ck('i 13 VALUE sono COPIATI, identici per indice',
   [u['idx'] for u in cov if u['kind'] == 'VALUE'] == [2, 3, 4, 7, 8, 9, 12, 13, 14, 17, 18, 19, 22]
   and all(u['italian'] == u['english'] for u in cov if u['kind'] == 'VALUE'),
   [u['idx'] for u in cov if u['kind'] == 'VALUE' and u['italian'] != u['english']])
ck('le 9 DESCRIPTION sono TRADOTTE, nessuna copiata',
   all(u['italian'] != u['english'] for u in cov if u['kind'] == 'DESCRIPTION'),
   [u['idx'] for u in cov if u['kind'] == 'DESCRIPTION' and u['italian'] == u['english']])
ck("le 4 note organo-metalliche sono IDENTICHE alla resa di L265 (riletto il suo translation.json)",
   len({by[i]['italian'] for i in NOTE}) == 1
   and {by[i]['italian'] for i in NOTE} == {u['italian'] for u in
                                            json.load(open(PREV, encoding='utf-8'))['units']
                                            if u['english'] == by[5]['english']},
   {by[i]['italian'][:60] for i in NOTE})
ck('le 5 frasi sulla variante sono distinte, ognuna con la sua resa',
   len({by[i]['italian'] for i in VARIANTI}) == 5 and len({by[i]['english'] for i in VARIANTI}) == 5
   and all('variante' in by[i]['italian'] for i in VARIANTI))
ck('la scheda di Trip racconta un DIFETTO, non una variante riuscita',
   'andato terribilmente storto' in by[16]['italian'] and 'germinazione' in by[16]['italian']
   and 'deforme' in by[16]['italian'] and 'sopravvive' in by[16]['italian'])
ck('VIRGOLETTE: 18 in inglese e 18 in italiano, per unita identiche',
   sum(u['english'].count(QUOTE) for u in cov) == 18 == sum(u['italian'].count(QUOTE) for u in cov)
   and {u['idx']: u['english'].count(QUOTE) for u in cov if QUOTE in u['english']}
   == {u['idx']: u['italian'].count(QUOTE) for u in cov if QUOTE in u['italian']},
   ({u['idx']: u['english'].count(QUOTE) for u in cov if QUOTE in u['english']},
    {u['idx']: u['italian'].count(QUOTE) for u in cov if QUOTE in u['italian']}))
ck('i 4 plurali restano senza virgolette, e nessuna sigla nuda in questo lotto',
   [u['idx'] for u in cov if u['kind'] == 'VALUE' and QUOTE not in u['english']] == [4, 9, 14, 19]
   and not [u for u in cov if u['kind'] == 'VALUE' and QUOTE not in u['english'] and u['english'].startswith('K-')])
ck('ZERO tab e ZERO segnaposto (asserzioni negative)',
   sum(u['english'].count(TAB) + u['italian'].count(TAB) for u in cov) == 0
   and not [t for u in cov for t in TAG.findall(u['english']) + TAG.findall(u['italian'])])
ck('APICI: ZERO in inglese; 6 in italiano (4 da «analisi», più «agilità» e «un\'unica»), elencati',
   sum(u['english'].count(APOS) for u in cov) == 0
   and {u['idx']: u['italian'].count(APOS) for u in cov if APOS in u['italian']}
   == {5: 1, 10: 1, 11: 1, 15: 1, 20: 1, 21: 1},
   {u['idx']: u['italian'].count(APOS) for u in cov if APOS in u['italian']})
ck('lessico: prua a lama, struttura a coda, germinazione, massa, composto',
   'prua affilata a lama' in by[6]['italian'] and 'struttura a coda' in by[11]['italian']
   and 'germinazione' in by[16]['italian'] and 'massa' in by[21]['italian']
   and 'composto' in by[21]['italian'])
ck('`Aberrant` non compare nei VALUE (sono sigle e nomi)',
   not [u['idx'] for u in cov if u['kind'] == 'VALUE' and 'Aberrant' in u['italian']])
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
ck("43 unita' prima (L265), e l'ultima prima della 686 e nella stessa nave (Pike)",
   db.execute('select count(*) from units where path=? and line<686', (PATH,)).fetchone()[0] == 43
   and db.execute('select context from units where path=? and line<686 order by line desc limit 1', (PATH,)).fetchone()
   == ('ship:Aberrant Pike',))
ck("ZERO unita' dopo la 1007: il lotto CHIUDE il file",
   db.execute('select count(*) from units where path=? and line>1007', (PATH,)).fetchone()[0] == 0)
ck("la 1007 e la riga massima del file, che ha 65 unita' fra la 16 e la 1007",
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (65, 16, 1007))
righe, lotti = set(), []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    us = [u for u in json.load(open(f, encoding='utf-8'))['units'] if u['path'] == PATH]
    if us:
        lotti.append((os.path.basename(os.path.dirname(f)), len(us)))
        righe |= {u['line'] for u in us}
ck('INVARIANTE DI FILE: 43 + 22 = 65 unita in 2 lotti',
   [n for _, n in lotti] == [43, 22] and sum(n for _, n in lotti) == 65 == len(righe),
   (lotti, len(righe)))
ck('le 65 righe dei lotti sono esattamente quelle del database (nessun buco)',
   righe == {l for l, in db.execute('select line from units where path=?', (PATH,))})
st = dict(db.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('tutte le 22 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d' % (sum(len(v['english'].split()) for v in cov),
                                sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
