r"""check.py — L274 (`data/korath/korath ships.txt`, righe 364-602). Secondo lotto del file.

**8 `DESCRIPTION` + 1 `VALUE`** su **quattro navi/stazioni Korath**: `'olofez` (caccia imbarcato), `Kas'ik Tek 7` (sonde),
`Rai'alorej` (rifugio-ospedale), `Ikatila'ej` (fabbrica volante). Quattro cose da verificare con cura:

1. **il `VALUE`** e `"olofezes"`, il **plurale** del nome di nave: si **copia**, e il test lo distingue dagli altri otto;
2. **le unita' 3 e 5 sono stringhe GIA' TRADOTTE** nel corpus (caccia e droni senza iperguida): si riprendono **alla lettera**
   e il test le confronta con la resa **piu' frequente** di tutti i `translation.json` dello staging;
3. **quattro tab** sulle unita' dispari (3, 5, 7, 9);
4. **cinque apici inglesi** e **tredici italiani**: mappe diverse, entrambe dichiarate.
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
BLOCCHI = [("ship:'olofez", 364, 401), ("ship:Kas'ik Tek 7", 442, 443),
           ('ship:Rai\'alorej', 524, 525), ("ship:Ikatila'ej", 601, 602)]
TABBED = [3, 5, 7, 9]
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


def corpus_rese(english):
    """Tutte le rese italiane gia' presenti nello staging per la stessa stringa inglese."""
    c = collections.Counter()
    for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
        for u in json.load(open(f, encoding='utf-8'))['units']:
            if u['english'] == english:
                c[u['italian']] += 1
    return c


ck('unita tradotte 9/9', len(cov) == 9 == len(units), '%d/%d' % (len(cov), len(units)))
ck('tipi: 8 DESCRIPTION + 1 VALUE',
   collections.Counter(u['kind'] for u in units) == {'DESCRIPTION': 8, 'VALUE': 1},
   dict(collections.Counter(u['kind'] for u in units)))
ck("il VALUE e COPIATO (`'olofezes`, il plurale del nome di nave)",
   by[1]['kind'] == 'VALUE' and by[1]['italian'] == by[1]['english'] == "'olofezes")
ck('le 8 DESCRIPTION sono TRADOTTE, nessuna copiata',
   all(u['italian'] != u['english'] for u in cov if u['kind'] == 'DESCRIPTION'),
   [u['idx'] for u in cov if u['kind'] == 'DESCRIPTION' and u['italian'] == u['english']])
ck("quattro contesti, con le righe misurate (`olofez` ne occupa tre)",
   [(c, by[min(i for i in by if by[i]['context'] == c)]['line'],
     by[max(i for i in by if by[i]['context'] == c)]['line']) for c, _, _ in BLOCCHI] == BLOCCHI,
   [(c, by[min(i for i in by if by[i]['context'] == c)]['line']) for c, _, _ in BLOCCHI])
ck('righe 364-602, nessun buco interno, ultima unita alla 602',
   [u['line'] for u in cov] == sorted({u['line'] for u in cov})
   and cov[0]['line'] == 364 and cov[-1]['line'] == 602)
ck('TAB: quattro in inglese e quattro in italiano, sulle unita dispari, come PRIMO carattere',
   sum(u['english'].count(TAB) for u in cov) == 4 == sum(u['italian'].count(TAB) for u in cov)
   and [u['idx'] for u in cov if TAB in u['english']] == TABBED == [u['idx'] for u in cov if TAB in u['italian']]
   and all(u['italian'].startswith(TAB) for u in cov if u['idx'] in TABBED))
c3, c5 = corpus_rese(by[3]['english']), corpus_rese(by[5]['english'])
ck('unita 3: la resa e quella PIU FREQUENTE del corpus, ripresa alla lettera',
   by[3]['italian'] in c3 and c3[by[3]['italian']] == max(c3.values()), dict(c3))
ck('unita 5: la resa e quella PIU FREQUENTE del corpus, ripresa alla lettera',
   by[5]['italian'] in c5 and c5[by[5]['italian']] == max(c5.values()), dict(c5))
ck('APICI in inglese: 5 (unita 1, 2, 7, 8, 9), tutti nei nomi Korath',
   {u['idx']: u['english'].count(APOS) for u in cov if APOS in u['english']}
   == {1: 1, 2: 1, 7: 1, 8: 1, 9: 1},
   {u['idx']: u['english'].count(APOS) for u in cov if APOS in u['english']})
ck('APICI in italiano: 13 su 7 unita, mappa dichiarata',
   {u['idx']: u['italian'].count(APOS) for u in cov if APOS in u['italian']}
   == {1: 1, 2: 2, 4: 2, 6: 2, 7: 1, 8: 3, 9: 2},
   {u['idx']: u['italian'].count(APOS) for u in cov if APOS in u['italian']})
ck('i nomi Korath restano dove l inglese li nomina',
   not [(u['idx'], n) for u in cov
        for n in ("'olofez", "Kas'ik Tek 7", "Rai'alorej", "Ikatila'ej")
        if n in u['english'] and n not in u['italian']],
   [(u['idx'], n) for u in cov for n in ("'olofez", "Kas'ik Tek 7", "Rai'alorej", "Ikatila'ej")
    if n in u['english'] and n not in u['italian']])
ck('la stazione e una STAZIONE, non una nave: «stazioni spaziali», «a bordo di una stazione»',
   'stazioni spaziali' in by[8]['italian'] and 'bordo di una stazione' in by[8]['italian'])
ck('lessico: iperguida, baia di caccia, baia per droni, microbot, navi ospedale, nave-mondo',
   'iperguida' in by[3]['italian'] and 'baia di caccia' in by[3]['italian']
   and 'baia per droni' in by[5]['italian'] and 'microbot' in by[4]['italian']
   and 'navi ospedale' in by[6]['italian'] and 'nave-mondo' in by[8]['italian'])
ck('i Systems Core restano invariati, come nel corpus',
   'Systems Core' in by[8]['italian'])
ck('ZERO virgolette e ZERO segnaposto (due asserzioni negative)',
   sum(u['english'].count(QUOTE) + u['italian'].count(QUOTE) for u in cov) == 0
   and not [t for u in cov for t in TAG.findall(u['english']) + TAG.findall(u['italian'])])
ck('nessun caporale, nessun carattere tipografico',
   not [u['idx'] for u in cov for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026' if c in u['italian']])
nonlat = [(u['idx'], c) for u in cov for c in u['italian'] if ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']],
   [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90 (1,00-1,31)',
   all(0.55 < u['ratio'] < 1.90 for u in cov),
   [(u['idx'], u['ratio']) for u in cov if not 0.55 < u['ratio'] < 1.90])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("8 unita' prima (L273)",
   db.execute('select count(*) from units where path=? and line<364', (PATH,)).fetchone()[0] == 8)
ck("33 unita' dopo la 602",
   db.execute('select count(*) from units where path=? and line>602', (PATH,)).fetchone()[0] == 33)
ck('il file ha 50 unita, righe 95-2363',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (50, 95, 2363))
st = dict(db.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('tutte le 9 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · 4 contesti · 4 tab' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
