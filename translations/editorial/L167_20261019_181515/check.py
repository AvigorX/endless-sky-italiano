r"""check.py — L167 (`data/human/paradise world jobs.txt`, 28 unita', righe 16-221).

Primo lotto del file (lo **apre**). Controlli propri: **62 token su 9 simboli**, verificati come **multiset** e come
**ordine per unita'**; **9 `VALUE`** riprodotti alla lettera; **2 virgolette** in idx 21 (la frase «completely legal
pharmaceuticals»); **idx 19 e 23 sono lo stesso `VALUE`** e devono restare identici; zero tab.
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
missing = [u['idx'] for u in units if u['idx'] not in tr]
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
VAL = [v['idx'] for v in cov if v['kind'] == 'VALUE']
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


TOK = {'<payment>': 18, '<planet>': 10, '<destination>': 9, '<commodity>': 7, '<date>': 6, '<tons>': 5,
       '<cargo>': 4, '<bunks>': 2, '<origin>': 1}
ck("unita' tradotte 28/28", len(cov) == 28 == len(units) and not missing, '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 9 VALUE + 9 DESCRIPTION + 9 DIALOG + 1 MISSION_TEXT',
   collections.Counter(u['kind'] for u in units)
   == {'VALUE': 9, 'DESCRIPTION': 9, 'DIALOG': 9, 'MISSION_TEXT': 1})
ck('UN asserzione vuota: ZERO UI_LABEL', [u['idx'] for u in units if u['kind'] == 'UI_LABEL'] == [])
ck('62 token su 9 simboli, stesso multiset in italiano',
   dict(collections.Counter(t for u in units for t in TAGS.findall(u['english']))) == TOK
   == dict(collections.Counter(t for v in cov for t in TAGS.findall(v['italian'])))
   and sum(TOK.values()) == 62 and len(TOK) == 9)
ck('parita per UNITA: stesso ordine di simboli in tutte le 28',
   not [v['idx'] for v in cov if TAGS.findall(v['italian']) != TAGS.findall(v['english'])],
   [(v['idx'], TAGS.findall(v['english']), TAGS.findall(v['italian']))
    for v in cov if TAGS.findall(v['italian']) != TAGS.findall(v['english'])])
ck('assenza incrociata: nessuna unita con <planet> ha <destination> e viceversa',
   not [v['idx'] for v in cov if ('<planet>' in v['english']) == ('<destination>' in v['english'])
        and ('<planet>' in v['english'] or '<destination>' in v['english'])])
ck('9 VALUE identici al sorgente, uno per uno',
   len(VAL) == 9 and all(by[i]['italian'].rstrip() == by[i]['english'].rstrip() for i in VAL),
   [(i, by[i]['italian']) for i in VAL])
ck('idx 19 e 23 sono lo stesso VALUE e restano identici',
   by[19]['english'] == by[23]['english'] and by[19]['italian'] == by[23]['italian'])
ck('28 unita, 27 testi inglesi distinti (la coppia 19/23)', len({v['english'] for v in cov}) == 27,
   len({v['english'] for v in cov}))
ck('le 20 e 24 differiscono solo per la coda (farmaci / snack)', by[20]['english'] != by[24]['english']
   and 'farmaci del tutto legali' in by[20]['italian'] and 'snack' in by[24]['italian']
   and 'farmaci' not in by[24]['italian'])
ck('2 virgolette, in idx 21, e la frase citata resta citata',
   sum(v['english'].count('"') for v in cov) == 2 == sum(v['italian'].count('"') for v in cov)
   and by[21]['english'].count('"') == 2 == by[21]['italian'].count('"')
   and '"farmaci del tutto legali"' in by[21]['italian'])
ck('ZERO tab nel sorgente e in traduzione (asserzione vuota scritta)',
   [v['idx'] for v in cov if '\t' in v['english']] == [] == [v['idx'] for v in cov if '\t' in v['italian']])
ck('9 contesti, tre unita ciascuno (VALUE + DESCRIPTION + DIALOG)',
   len({u['context'] for u in units}) == 9
   and sorted(collections.Counter(u['context'] for u in units).values()) == [3, 3, 3, 3, 3, 3, 3, 3, 4],
   collections.Counter(u['context'] for u in units))
ck('prima e ultima unita: righe 16 e 221, contesti del contratto',
   (cov[0]['line'], cov[-1]['line']) == (16, 221)
   and cov[0]['context'] == 'mission:Paradise Job: Care Package'
   and cov[-1]['context'] == 'mission:Paradise Job: Food Donations',
   (cov[0]['line'], cov[-1]['line']))
ck('zero spazi iniziali e finali identici al sorgente (28/28)',
   not [v['idx'] for v in cov
        if len(v['italian']) - len(v['italian'].rstrip()) != len(v['english']) - len(v['english'].rstrip())
        or len(v['italian']) - len(v['italian'].lstrip()) != len(v['english']) - len(v['english'].lstrip())])
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' you ', ' to the ', ' will be ',
        ' is ', ' are ', ' from the ')
LONG = ' '.join(TAGS.sub('""', v['italian']) for v in cov if v['kind'] != 'VALUE').lower()
ck('nessun residuo inglese fuori dai VALUE',
   not [w for w in ENGW if w in LONG], [w for w in ENGW if w in LONG])
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
ck('tutte le 28 unita sono PENDING nel database (misurato)',
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
      len(parts), len(missing)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
