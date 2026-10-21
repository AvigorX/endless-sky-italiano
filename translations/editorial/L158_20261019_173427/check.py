r"""check.py — L158 (`data/human/weapons.txt`, 18 unita', righe 1015-1228).

Lotto ripetitivo: **quattro testi ripetuti** nel sorgente (3/6, 4/7, 5/9/14/18, 12/15, 13/16) che devono restare
identici in italiano; due di essi sono **la stessa stringa di L157** (8 e 5) e si verificano anche contro il lotto
precedente. **10 unita' con tab**, zero token, zero virgolette, zero VALUE.
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
EARLIER = {}
for f in sorted(os.listdir(os.path.join(L10N, 'staging/editorial'))):
    p = os.path.join(L10N, 'staging/editorial', f, 'translation.json')
    if f.startswith('L158') or not os.path.exists(p):
        continue
    for u in json.load(open(p, encoding='utf-8'))['units']:
        if u['path'] == 'data/human/weapons.txt':
            EARLIER[u['english']] = u['italian']
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


NAMES = ['Sidewinder Missile Launcher', 'Sidewinder Missile Rack', 'Sidewinder Missile Pod', 'Sidewinder Missile',
         'Anti-Missile Turret', 'Meteor Missiles', 'Javelin Storage Crate', 'Javelin Pod', 'Javelin Mini Pod',
         'Javelin', 'Lovelace Labs']
ck("unita' tradotte 18/18", len(cov) == 18 == len(units) and not missing, '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 18 DESCRIPTION, ZERO VALUE e ZERO token',
   collections.Counter(u['kind'] for u in units) == {'DESCRIPTION': 18}
   and [v['idx'] for v in cov for t in TAGS.findall(v['english'])] == []
   and [v['idx'] for v in cov for t in TAGS.findall(v['italian'])] == [])
ck('UN asserzione vuota: ZERO UI_LABEL', [u['idx'] for u in units if u['kind'] == 'UI_LABEL'] == [])
ck('10 unita con tab iniziale: idx 4,5,7,8,9,13,14,16,17,18, le stesse in traduzione',
   [v['idx'] for v in cov if v['english'].startswith('\t')] == [4, 5, 7, 8, 9, 13, 14, 16, 17, 18]
   == [v['idx'] for v in cov if v['italian'].startswith('\t')])
ck('ZERO virgolette (asserzione vuota scritta)',
   sum(v['english'].count('"') for v in cov) == 0 == sum(v['italian'].count('"') for v in cov))
ck('coppie 3/6 e 4/7 identiche anche in italiano',
   by[3]['italian'] == by[6]['italian'] and by[4]['italian'] == by[7]['italian'])
ck('le quattro copie di 5/9/14/18 identiche in italiano',
   len({by[i]['italian'] for i in (5, 9, 14, 18)}) == 1)
ck('coppie 12/15 e 13/16 identiche in italiano',
   by[12]['italian'] == by[15]['italian'] and by[13]['italian'] == by[16]['italian'])
ck('18 unita, 11 testi inglesi distinti',
   len({v['english'] for v in cov}) == 11, len({v['english'] for v in cov}))
ck('la resa riusa L157 per le due stringhe identiche (idx 8 e 5)',
   EARLIER.get(by[8]['english']) == by[8]['italian'] and EARLIER.get(by[5]['english']) == by[5]['italian'],
   (EARLIER.get(by[8]['english']), by[8]['italian']))
ck('ogni nome proprio dell inglese resta nell italiano (unita per unita)',
   not [v['idx'] for v in cov for n in NAMES if n in v['english'] and n not in v['italian']],
   [(v['idx'], n) for v in cov for n in NAMES if n in v['english'] and n not in v['italian']])
ck('nessun nome proprio inventato in italiano (insieme uguale)',
   {(v['idx'], n) for v in cov for n in NAMES if n in v['english']}
   == {(v['idx'], n) for v in cov for n in NAMES if n in v['italian']})
ck('glossario: munizioni, emporio, cannone, gittata, scafo (temi)',
   all(t in ' '.join(v['italian'].lower() for v in cov)
       for t in ('munizion', 'emporio', 'cannon', 'gittat')))
ck('prima e ultima unita: righe 1015 e 1228',
   (cov[0]['line'], cov[-1]['line']) == (1015, 1228)
   and cov[0]['context'] == 'outfit:Sidewinder Missile' and cov[-1]['context'] == 'outfit:Javelin Mini Pod',
   (cov[0]['line'], cov[-1]['line']))
ck('zero spazi iniziali e finali identici al sorgente (18/18)',
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
ck('tutte le 18 unita sono PENDING nel database (misurato)',
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
