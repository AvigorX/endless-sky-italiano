r"""check.py — L166 (`data/avgi/avgi outfits.txt`, 6 unita', righe 616-654). **Chiude il file.**

Controlli propri: **6 DESCRIPTION e zero VALUE** (assert vuota scritta); **2 unita' con tab** (2, 4); **zero virgolette
doppie** (l'apostrofo interno di `'outfit.'` e' ASCII, non un carattere tipografico); `Trefoil`, `Integral Wood`,
`Speaker Wisteria`, `Avgi` invariati; 6 testi distinti su 6.
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
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


NAMES = ['Optical Laser Rifle', 'Trefoil', 'Integral Wood', 'Speaker Wisteria', 'Avgi']
ck("unita' tradotte 6/6", len(cov) == 6 == len(units) and not missing, '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 6 DESCRIPTION, zero VALUE (asserzione vuota scritta)',
   collections.Counter(u['kind'] for u in units) == {'DESCRIPTION': 6}
   and [v['idx'] for v in cov if v['kind'] == 'VALUE'] == [])
ck('UN asserzione vuota: ZERO UI_LABEL e ZERO token',
   [u['idx'] for u in units if u['kind'] == 'UI_LABEL'] == []
   and [v['idx'] for v in cov if TAGS.findall(v['english'])] == [] == [v['idx'] for v in cov if TAGS.findall(v['italian'])])
ck('ZERO virgolette doppie nel sorgente e in traduzione',
   sum(v['english'].count('"') for v in cov) == 0 == sum(v['italian'].count('"') for v in cov))
ck('2 unita con tab iniziale: idx 2 e 4, le stesse in traduzione',
   [v['idx'] for v in cov if v['english'].startswith('\t')] == [2, 4]
   == [v['idx'] for v in cov if v['italian'].startswith('\t')])
ck('6 testi distinti su 6 unita', len({v['english'] for v in cov}) == 6)
ck('ogni nome proprio dell inglese resta nell italiano (unita per unita)',
   not [v['idx'] for v in cov for n in NAMES if n in v['english'] and n not in v['italian']],
   [(v['idx'], n) for v in cov for n in NAMES if n in v['english'] and n not in v['italian']])
ck('nessun nome proprio inventato in italiano (insieme uguale)',
   {(v['idx'], n) for v in cov for n in NAMES if n in v['english']}
   == {(v['idx'], n) for v in cov for n in NAMES if n in v['italian']})
ck("l'apostrofo di 'outfit.' resta ASCII, non un apostrofo curvo",
   "'outfit.'" in by[5]['english'] and "'equipaggiamento'" in by[5]['italian']
   and '\u2019' not in by[5]['italian'])
ck('glossario: laser, fascio, occhiali, arma contundente, tavola, lancia',
   all(t in ' '.join(v['italian'].lower() for v in cov)
       for t in ('laser', 'fascio', 'occhiali', 'arma contundente', 'tavola', 'lancia')))
ck('prima e ultima unita: righe 616 e 654, contesti del contratto',
   (cov[0]['line'], cov[-1]['line']) == (616, 654)
   and cov[0]['context'] == 'outfit:Optical Laser Rifle' and cov[-1]['context'] == 'outfit:Lancet Adamant',
   (cov[0]['line'], cov[-1]['line']))
ck('4 contesti distinti: Optical 2, Trefoil 2, Damselflyman 1, Lancet 1',
   len({u['context'] for u in units}) == 4
   and [collections.Counter(u['context'] for u in units)[c] for c in
        ('outfit:Optical Laser Rifle', 'outfit:Trefoil Board', 'outfit:Damselflyman',
         'outfit:Lancet Adamant')] == [2, 2, 1, 1],
   collections.Counter(u['context'] for u in units))
ck('zero spazi iniziali e finali identici al sorgente (6/6)',
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
ck('tutte le 6 unita sono PENDING nel database (misurato)',
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
