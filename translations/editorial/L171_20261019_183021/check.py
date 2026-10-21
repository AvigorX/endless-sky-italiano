r"""check.py — L171 (`data/human/paradise world jobs.txt`, 24 unita', righe 719-987).

Quinto lotto del file, **anomalo**: 12 `VALUE` e 12 `DESCRIPTION`, zero `DIALOG`. Controlli propri: **`<planet>` 28
volte** (massimo della campagna) su **soli 5 simboli**; **10 `VALUE` distinti su 12** (due coppie ripetute da
individuare); `<martini house>` 4 volte; e il possessivo inglese `Martini's` (idx 24) che **sparisce** in italiano — gli
apici NON si contano fra le lingue (trappola pagata in L169).
"""
import collections
import json
import os
import re
import sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
units = sorted(src['units'], key=lambda x: x['line'])
tr = {}
parts = sorted(f for f in os.listdir(os.path.join(HERE, 'parts')) if f.endswith('.json'))
for p in parts:
    for k, v in json.load(open(os.path.join(HERE, 'parts', p), encoding='utf-8')).items():
        tr[int(k)] = v
out = {'block': src['block'], 'note': src['note'], 'units': []}
for u in units:
    if u['idx'] not in tr:
        continue
    it = tr[u['idx']]
    out['units'].append({"idx": u['idx'], "id": u['id'], "path": u['path'], "line": u['line'],
                         "kind": u['kind'], "context": u['context'], "english": u['english'],
                         "italian": it, "ratio": round(len(it) / max(1, len(u['english'])), 3)})
open(os.path.join(HERE, 'translation.json'), 'w', encoding='utf-8').write(
    json.dumps(out, ensure_ascii=False, indent=1))
cov = out['units']
by = {v['idx']: v for v in cov}
TAGS = re.compile(r'<[^<>]+>')
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


TOK = {'<planet>': 28, '<payment>': 12, '<bunks>': 7, '<martini house>': 4, '<cargo>': 4}
ck("unita' tradotte 24/24", len(cov) == 24 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 12 VALUE + 12 DESCRIPTION, nessun DIALOG',
   collections.Counter(u['kind'] for u in units) == {'VALUE': 12, 'DESCRIPTION': 12})
ck('UN asserzione vuota: ZERO UI_LABEL', [u['idx'] for u in units if u['kind'] == 'UI_LABEL'] == [])
ck('55 token su 5 simboli, con <planet> 28 volte (massimo della campagna)',
   dict(collections.Counter(t for u in units for t in TAGS.findall(u['english']))) == TOK
   == dict(collections.Counter(t for v in cov for t in TAGS.findall(v['italian'])))
   and sum(TOK.values()) == 55 and len(TOK) == 5 and TOK['<planet>'] == 28)
ck('parita per UNITA: stesso ordine di simboli in tutte le 24',
   not [v['idx'] for v in cov if TAGS.findall(v['italian']) != TAGS.findall(v['english'])],
   [(v['idx'], TAGS.findall(v['english']), TAGS.findall(v['italian']))
    for v in cov if TAGS.findall(v['italian']) != TAGS.findall(v['english'])])
ck('`<martini house>` intero 4 volte (idx 2, 4, 6, 8), mai spezzato',
   [v['idx'] for v in cov if '<martini house>' in v['english']] == [2, 4, 6, 8]
   == [v['idx'] for v in cov if '<martini house>' in v['italian']]
   and not [v['idx'] for v in cov if re.search(r'<martini>[\s-]+house', v['italian'])])
ck('idx 10/12/14/16 hanno DUE <planet> nell ordine giusto',
   all(TAGS.findall(by[i]['english']) == (['<bunks>', '<planet>', '<planet>', '<payment>'] if i in (14, 16)
       else ['<planet>', '<planet>', '<payment>']) for i in (10, 12, 14, 16)))
ck('12 VALUE identici al sorgente',
   len([v for v in cov if v['kind'] == 'VALUE']) == 12
   and [v['idx'] for v in cov if v['kind'] == 'VALUE' and v['italian'].rstrip() != v['english'].rstrip()] == [])
ck('10 VALUE distinti su 12: le coppie sono 1/5 e 3/7, e la resa e la stessa',
   len({v['english'] for v in cov if v['kind'] == 'VALUE'}) == 10
   and by[1]['english'] == by[5]['english'] and by[3]['english'] == by[7]['english']
   and by[1]['italian'] == by[5]['italian'] and by[3]['italian'] == by[7]['italian']
   and by[1]['english'] != by[3]['english'])
ck('24 unita, 22 testi inglesi distinti (le 2 coppie di VALUE)',
   len({v['english'] for v in cov}) == 22, len({v['english'] for v in cov}))
ck('le 12 DESCRIPTION sono tutte distinte',
   len({v['english'] for v in cov if v['kind'] == 'DESCRIPTION'}) == 12)
ck('le due missioni di lusso 6/8 dicono «nave di lusso»',
   'nave di lusso' in by[6]['italian'] and 'nave di lusso' in by[8]['italian']
   and 'nave di lusso' not in by[2]['italian'] and 'nave di lusso' not in by[4]['italian'])
ck('idx 4/8 (singolare) usano il singolare, 2/6 (plurale) il plurale',
   'Questo residente' in by[4]['italian'] and 'Questo residente' in by[8]['italian']
   and 'Questi <bunks> residenti' in by[2]['italian']
   and 'Trasportalo' in by[4]['italian'] and 'Trasportali' in by[2]['italian'])
ck('idx 16/18 dicono «alle loro case», 22/24 «a casa loro» (singolare/plurale del sorgente)',
   'alle loro case' in by[16]['italian'] and 'alle loro case' in by[18]['italian']
   and 'a casa loro' in by[22]['italian'] and 'a casa loro' in by[24]['italian'])
ck('apici: il possessivo Martini\'s (idx 24) sparisce, ma l italiano ne aggiunge 2 in «uomini d\'affari»',
   sum(v['english'].count("'") for v in cov) == 1 and "Martini's" in by[24]['english']
   and by[24]['italian'].count("'") == 0
   and [v['idx'] for v in cov if "'" in v['italian']] == [18, 20]
   and [v['idx'] for v in cov if "d'affari" in v['italian']] == [18, 20]
   and sum(v['italian'].count("'") for v in cov) == 2)
ck('ZERO tab e ZERO virgolette (asserzioni vuote scritte)',
   [v['idx'] for v in cov if '\t' in v['english'] or '\t' in v['italian']] == []
   and sum(v['english'].count('"') for v in cov) == 0 == sum(v['italian'].count('"') for v in cov))
ck('12 contesti distinti', len({u['context'] for u in units}) == 12)
ck('prima e ultima unita: righe 719 e 987',
   (cov[0]['line'], cov[-1]['line']) == (719, 987)
   and cov[0]['context'] == 'mission:Martini Evacuation (Resident Group)'
   and cov[-1]['context'] == 'mission:Martini Evacuation (Exhausted Search and Rescue Team)')
ck('zero spazi iniziali e finali identici al sorgente (24/24)',
   not [v['idx'] for v in cov
        if len(v['italian']) - len(v['italian'].rstrip()) != len(v['english']) - len(v['english'].rstrip())
        or len(v['italian']) - len(v['italian'].lstrip()) != len(v['english']) - len(v['english'].lstrip())])
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' you ', ' to the ', ' will be ',
        ' is ', ' are ', ' from the ', ' their ', ' they ', ' was on ', ' wishes to ')
LONG = ' '.join(TAGS.sub('""', v['italian']) for v in cov if v['kind'] != 'VALUE').lower()
ck('nessun residuo inglese fuori dai VALUE', not [w for w in ENGW if w in LONG], [w for w in ENGW if w in LONG])
CORT = re.findall(r'\bLei\b|(?<![.!?] )\b(?:Suo|Sua|Suoi|Sue)\b', ' '.join(v['italian'] for v in cov))
ck('nessuna forma di cortesia «Lei»', not CORT, CORT)
rs = [v['ratio'] for v in cov]
ck('rapporto nel gate 0,55-1,90', 0.55 < min(rs) and max(rs) < 1.90, '%.2f - %.2f' % (min(rs), max(rs)))
bad = [(v['idx'], n) for v in cov for p, n in ((r"\b(e|piu|perche|cosi|gia|puo|cioe|percio|fa)'", 'accento'),
       ('\u2026', 'ellissi'), ('\u2014', 'em dash'), ('\u2013', 'en dash'), ('\u2019', 'apostrofo curvo'),
       ('\u00ab', 'caporale'), ('\u00bb', 'caporale')) if re.search(p, v['italian'])]
ck('tipografia (accenti veri, nessun carattere tipografico)', not bad, bad)
nonlat = [v['idx'] for v in cov for c in TAGS.sub('', v['italian'])
          if ord(c) > 127 and not 0x00C0 <= ord(c) <= 0x024F]
ck('caratteri non latini (fuori dai token)', not nonlat, nonlat)
c = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
st = dict(c.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('tutte le 24 unita sono PENDING nel database (misurato)',
   c.execute('select count(*) from units where id in (%s) and state != "PENDING"'
             % ','.join('?' * len(units)), [u['id'] for u in units]).fetchone()[0] == 0)
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d' % (sum(len(v['english'].split()) for v in cov),
                                 sum(len(v['italian'].split()) for v in cov)))
print('righe %d/%d · parti %d · mancanti %d' % (min(u['line'] for u in units), max(u['line'] for u in units),
      len(parts), len([u for u in units if u['idx'] not in tr])))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
