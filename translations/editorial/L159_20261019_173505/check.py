r"""check.py — L159 (`data/human/weapons.txt`, 22 unita', righe 1263-1601).

Controlli propri: **2 VALUE** (`Torpedoes`, `Typhoon Torpedoes`) riprodotti alla lettera; **8 unita' con tab**;
**sei copie** della riga munizioni, identiche fra loro **e a quelle di L157/L158**; 14/16 identiche; la frase iniziale
di 8 e' identica a quella di 6 (sotto-stringa, non stringa: si verifica come tale, non come uguaglianza).
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
EARLIER = {}
for f in sorted(os.listdir(os.path.join(L10N, 'staging/editorial'))):
    p = os.path.join(L10N, 'staging/editorial', f, 'translation.json')
    if f.startswith('L159') or not os.path.exists(p):
        continue
    for u in json.load(open(p, encoding='utf-8'))['units']:
        if u['path'] == 'data/human/weapons.txt':
            EARLIER[u['english']] = u['italian']
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


NAMES = ['Javelin Turret', 'Javelin Pod', 'Javelin Storage Crate', 'Torpedo Storage Rack', 'Torpedo Launcher',
         'Torpedo Pod', 'Typhoon Torpedo', 'Typhoon Storage Tube', 'Typhoon Launcher', 'Typhoon Pod',
         'Heavy Rocket Launcher', 'Heavy Rocket Rack', 'Heavy Rocket']
AMMO = [2, 7, 10, 15, 18, 22]
ck("unita' tradotte 22/22", len(cov) == 22 == len(units) and not missing, '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 20 DESCRIPTION + 2 VALUE', collections.Counter(u['kind'] for u in units)
   == {'DESCRIPTION': 20, 'VALUE': 2})
ck('UN asserzione vuota: ZERO UI_LABEL', [u['idx'] for u in units if u['kind'] == 'UI_LABEL'] == [])
ck('ZERO token nel sorgente e in traduzione (asserzione vuota scritta)',
   [v['idx'] for v in cov if TAGS.findall(v['english'])] == [] == [v['idx'] for v in cov if TAGS.findall(v['italian'])])
ck('2 VALUE identici al sorgente, uno per uno',
   len(VAL) == 2 and all(by[i]['italian'].rstrip() == by[i]['english'].rstrip() for i in VAL),
   [(i, by[i]['italian']) for i in VAL])
ck('8 unita con tab iniziale: idx 2,7,9,10,15,17,18,22, le stesse in traduzione',
   [v['idx'] for v in cov if v['english'].startswith('\t')] == [2, 7, 9, 10, 15, 17, 18, 22]
   == [v['idx'] for v in cov if v['italian'].startswith('\t')])
ck('ZERO virgolette (asserzione vuota scritta)',
   sum(v['english'].count('"') for v in cov) == 0 == sum(v['italian'].count('"') for v in cov))
ck('le sei copie della riga munizioni sono identiche fra loro',
   len({by[i]['italian'] for i in AMMO}) == 1)
ck('la riga munizioni riusa la stessa resa di L157/L158',
   EARLIER.get(by[2]['english'].lstrip('\t')) == by[2]['italian'].lstrip('\t')
   or EARLIER.get(by[2]['english']) == by[2]['italian'],
   (EARLIER.get(by[2]['english']), by[2]['italian']))
ck('14 e 16 identiche in italiano', by[14]['italian'] == by[16]['italian'])
ck('la frase iniziale di 8 e quella di 6 condividono la stessa resa (sotto-stringa)',
   by[6]['italian'].startswith(by[8]['italian']) and by[8]['english'] in by[6]['english'])
ck('22 unita, 16 testi inglesi distinti', len({v['english'] for v in cov}) == 16,
   len({v['english'] for v in cov}))
ck('ogni nome proprio dell inglese resta nell italiano (unita per unita)',
   not [v['idx'] for v in cov for n in NAMES if n in v['english'] and n not in v['italian']],
   [(v['idx'], n) for v in cov for n in NAMES if n in v['english'] and n not in v['italian']])
ck('nessun nome proprio inventato in italiano (insieme uguale)',
   {(v['idx'], n) for v in cov for n in NAMES if n in v['english']}
   == {(v['idx'], n) for v in cov for n in NAMES if n in v['italian']})
ck('glossario: siluri, munizioni, emporio, caccia, navi capitali',
   all(t in ' '.join(v['italian'].lower() for v in cov)
       for t in ('siluri', 'munizion', 'emporio', 'caccia', 'navi capitali')))
ck('prima e ultima unita: righe 1263 e 1601',
   (cov[0]['line'], cov[-1]['line']) == (1263, 1601)
   and cov[0]['context'] == 'outfit:Javelin Turret' and cov[-1]['context'] == 'outfit:Heavy Rocket Launcher',
   (cov[0]['line'], cov[-1]['line']))
ck('zero spazi iniziali e finali identici al sorgente (22/22)',
   not [v['idx'] for v in cov
        if len(v['italian']) - len(v['italian'].rstrip()) != len(v['english']) - len(v['english'].rstrip())
        or len(v['italian']) - len(v['italian'].lstrip()) != len(v['english']) - len(v['english'].lstrip())])
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' you ', ' to the ', ' will be ',
        ' is ', ' are ', ' from the ')
LONG = ' '.join(TAGS.sub('""', v['italian']) for v in cov).lower()
for s in NAMES:
    LONG = LONG.replace(s.lower(), '@@')
ck('nessun residuo inglese fuori dai nomi propri',
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
ck('tutte le 22 unita sono PENDING nel database (misurato)',
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
