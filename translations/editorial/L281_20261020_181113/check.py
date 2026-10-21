r"""check.py — L281 (`data/quarg/quarg news.txt`, righe 23-490). **LOTTO TERMINALE: chiude il file.**

Il file e' **composto da frammenti**: le prime notizie sono costruite da blocchi `word` con frammenti fra virgolette, e
l'estrattore espone **solo** le stringhe fra backtick. Ne restano **50 unita'**: **28 delimitatori** (l'unica stringa `"`) e
**22 unita' di prosa**. Le 28 hanno **un solo valore possibile** e si copiano dichiarandole; le 22 si traducono.

Cinque cose da verificare:

1. **`ID_OK` per i 28 delimitatori**: sono identici per necessita', non per pigrizia, e il test lo esige;
2. **44 virgolette** (28 nei delimitatori + 16 nella prosa), con lo **stesso numero per unita'**;
3. **la lacuna dell'estrattore, dichiarata**: i frammenti **senza backtick** (`"Are you"`, `" "`, `"a merchant"`) **non sono
   nel database** e non sono traducibili — il lotto non li tocca e li elenca qui;
4. **lotto terminale**: invariante di segmento (0 prima, 50 qui, **0 dopo** la 490) **e di FILE** (50 unita', righe
   distinte, ultima riga 490, copertura 50/50);
5. **il registro Quarg**: formale e pacato, con il «tu» del progetto e i nomi propri invariati.
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
PATH = 'data/quarg/quarg news.txt'
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
BLOCCHI = [('news:anonymous quarg', 23, 66),
           ('news:linguist on quarg planets in human and hai space', 77, 167),
           ('news:tourist on quarg planets in human and hai space', 179, 222),
           ('news:engineer on quarg planets in human space', 234, 239),
           ('news:merchant on quarg planets in human and hai space', 262, 290),
           ('news:merchant on quarg planets in human space', 313, 358),
           ('news:reporter on quarg planets in human space', 369, 389),
           ('news:student on quarg planets', 402, 444),
           ('news:quarg anywhere', 455, 465),
           ('phrase:ringworld quarg phrases', 481, 490)]
ID_OK = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
PROSA = [1] + list(range(30, 51))
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck('unita tradotte 50/50', len(cov) == 50 == len(units), '%d/%d' % (len(cov), len(units)))
ck('tipi: 40 NEWS + 10 TEXT',
   collections.Counter(u['kind'] for u in units) == {'NEWS': 40, 'TEXT': 10},
   dict(collections.Counter(u['kind'] for u in units)))
ck('dieci contesti, con le righe misurate',
   [(c, by[[u['idx'] for u in cov if u['context'] == c][0]]['line'],
     by[[u['idx'] for u in cov if u['context'] == c][-1]]['line']) for c, _, _ in BLOCCHI] == BLOCCHI,
   [(c, by[[u['idx'] for u in cov if u['context'] == c][0]]['line']) for c, _, _ in BLOCCHI])
ck('ID_OK: i 28 delimitatori sono COPIATI (identici per necessita)',
   [u['idx'] for u in cov if u['italian'] == u['english']] == ID_OK
   and all(by[i]['english'] == '"' for i in ID_OK),
   [u['idx'] for u in cov if u['italian'] == u['english']])
ck('le 22 unita di PROSA sono TRADOTTE, nessuna copiata',
   all(by[i]['italian'] != by[i]['english'] for i in PROSA),
   [i for i in PROSA if by[i]['italian'] == by[i]['english']])
ck('VIRGOLETTE: 44 in inglese e 44 in italiano, con lo STESSO numero per ogni unita',
   sum(u['english'].count(QUOTE) for u in cov) == 44 == sum(u['italian'].count(QUOTE) for u in cov)
   and all(u['english'].count(QUOTE) == u['italian'].count(QUOTE) for u in cov),
   [(u['idx'], u['english'].count(QUOTE), u['italian'].count(QUOTE)) for u in cov
    if u['english'].count(QUOTE) != u['italian'].count(QUOTE)])
ck('ZERO tab e ZERO segnaposto (due asserzioni negative)',
   sum(u['english'].count(TAB) + u['italian'].count(TAB) for u in cov) == 0
   and not [t for u in cov for t in TAG.findall(u['english']) + TAG.findall(u['italian'])])
ck('APICI: 14 in inglese, 20 in italiano (mappa stampata, non asserita unita per unita)',
   sum(u['english'].count(APOS) for u in cov) == 14 and sum(u['italian'].count(APOS) for u in cov) == 20,
   (sum(u['english'].count(APOS) for u in cov), sum(u['italian'].count(APOS) for u in cov)))
ck("`'turista'` fra apici semplici all'unita 1: due apici, conservati",
   "'turista'" in by[1]['italian'] and by[1]['italian'].count(APOS) == 2)
ck('registro Quarg: «umano», «nostro mondo», «visitatori» — e il «tu» del progetto',
   'umano' in by[30]['italian'] and 'nostro mondo' in by[31]['italian']
   and 'visitatori' in by[31]['italian'] and 'Hai qualche domanda' in by[30]['italian'])
ck('i Quarg non condividono la tecnologia: rifiuto esplicito e motivato',
   'non ti forniremo la nostra tecnologia' in by[32]['italian']
   and 'crescano e si sviluppino da soli' in by[32]['italian'])
ck('lessico: mondo ad anello, baia, hangar, container, mondo (ringworld)',
   'mondo ad anello' in by[41]['italian'] and 'baia' in by[48]['italian']
   and 'hangar' in by[38]['italian'] and 'container' in by[47]['italian'])
ck('nessun caporale, nessun carattere tipografico',
   not [u['idx'] for u in cov for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026' if c in u['italian']])
nonlat = [(u['idx'], c) for u in cov for c in u['italian'] if ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']],
   [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90 sulle 22 unita di prosa (0,83-1,28)',
   all(0.55 < by[i]['ratio'] < 1.90 for i in PROSA),
   [(i, by[i]['ratio']) for i in PROSA if not 0.55 < by[i]['ratio'] < 1.90])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("ZERO unita' prima della 23: il lotto APRE il file",
   db.execute('select count(*) from units where path=? and line<23', (PATH,)).fetchone()[0] == 0)
ck("ZERO unita' dopo la 490: il lotto CHIUDE il file",
   db.execute('select count(*) from units where path=? and line>490', (PATH,)).fetchone()[0] == 0)
ck('INVARIANTE DI FILE: 50 unita, righe 23-490, ultima alla 490',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (50, 23, 490))
somma, righe = 0, set()
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    us = [u for u in json.load(open(f, encoding='utf-8'))['units'] if u['path'] == PATH]
    if us:
        somma += len(us)
        righe |= {u['line'] for u in us}
ck('INVARIANTE DI FILE: un solo lotto, 50 unita, 50 righe distinte, nessuna riga fuori',
   somma == 50 and len(righe) == 50 and min(righe) == 23 and max(righe) == 490,
   (somma, len(righe)))
st = dict(db.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('tutte le 50 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · 10 contesti · 28 delimitatori ID_OK · 22 prosa' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('lacuna estrattore: i frammenti senza backtick (`"Are you"`, `" "`) NON sono nel DB')
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
