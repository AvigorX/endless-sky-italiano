r"""check.py — L181 (`data/human/outfits.txt`, 9 unita', righe 158-233).

Secondo lotto del file: **9 `DESCRIPTION` e nessun `VALUE`** (niente da copiare), **2 tab** (idx 4, 7), zero virgolette,
**1 apice** (idx 2, `ship's`). Controlli propri: i nomi tecnici restano inglesi (`Sidewinders`, `ramscoop`,
`scram drive`, `jump drive`, `Free Worlds`, `Deep`), `hyperdrive` diventa **iperguida** (coerente con i lotti
precedenti), e la metafora della vespa (idx 6) non si perde.
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
NAMES = ('Sidewinders', 'ramscoop', 'scram drive', 'jump drive', 'Free Worlds', 'Deep')
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 9/9", len(cov) == 9 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 9 DESCRIPTION, ZERO VALUE', collections.Counter(u['kind'] for u in units) == {'DESCRIPTION': 9})
ck('UN asserzione vuota: ZERO UI_LABEL', [u['idx'] for u in units if u['kind'] == 'UI_LABEL'] == [])
ck('ZERO VALUE: nessun nome da copiare in questo lotto (asserzione vuota scritta)',
   [u['idx'] for u in units if u['kind'] == 'VALUE'] == [])
ck('ZERO token in tutto il lotto (asserzione vuota scritta)',
   {t for u in units for t in TAGS.findall(u['english'])} == set()
   == {t for v in cov for t in TAGS.findall(v['italian'])})
ck('ZERO virgolette in inglese e in italiano (asserzione vuota scritta)',
   sum(v['english'].count('"') for v in cov) == 0 == sum(v['italian'].count('"') for v in cov))
ck('2 tab iniziali: idx 4 e 7, uno solo per unita',
   [v['idx'] for v in cov if v['english'].startswith('\t')] == [4, 7]
   == [v['idx'] for v in cov if v['italian'].startswith('\t')]
   and all(v['italian'].count('\t') == 1 for v in cov if v['italian'].startswith('\t')))
ck('1 apice inglese, in idx 2 (`ship\'s`), e nessun possessivo inglese in italiano',
   sum(v['english'].count("'") for v in cov) == 1
   and [v['idx'] for v in cov if "'" in v['english']] == [2]
   and not [v['idx'] for v in cov if re.search(r"[A-Za-z]+'s\b", v['italian'])])
ck('i nomi tecnici restano inglesi in ogni unita che li nomina',
   not [(v['idx'], n) for v in cov for n in NAMES if n in v['english'] and n not in v['italian']],
   [(v['idx'], n) for v in cov for n in NAMES if n in v['english'] and n not in v['italian']])
ck('`hyperdrive` diventa «iperguida» (idx 7), e idx 6 non lo nomina affatto',
   'hyperdrive' in by[7]['english'] and 'iperguida' in by[7]['italian']
   and 'hyperdrive' not in by[7]['italian']
   and 'hyperdrive' not in by[6]['english'] and 'iperguida' not in by[6]['italian']
   and 'iperguida' in by[8]['italian'])
ck('idx 4 spiega il vento solare e la vicinanza alla stella',
   'vento solare' in by[4]['italian'] and 'più sei vicino alla stella' in by[4]['italian'])
ck('idx 5 nomina il Deep e i Free Worlds senza tradurli',
   'Deep' in by[5]['italian'] and 'Free Worlds' in by[5]['italian'])
ck('la metafora della vespa (idx 6) resta una metafora',
   'vespa' in by[6]['italian'] and 'foglia di quercia' in by[6]['italian']
   and 'uova' in by[6]['italian'])
ck('9 unita, 9 testi inglesi distinti', len({v['english'] for v in cov}) == 9,
   len({v['english'] for v in cov}))
ck('7 contesti: Ramscoop e Hyperdrive con 2 unita, cinque con 1',
   len({u['context'] for u in units}) == 7
   and sorted(collections.Counter(u['context'] for u in units).values()) == [1, 1, 1, 1, 1, 2, 2],
   collections.Counter(u['context'] for u in units))
ck('prima e ultima unita: righe 158 e 233',
   (cov[0]['line'], cov[-1]['line']) == (158, 233)
   and cov[0]['context'] == 'outfit:Small Radar Jammer' and cov[-1]['context'] == 'outfit:Jump Drive')
ck('nessuno spazio finale, tab iniziale ammesso',
   not [v['idx'] for v in cov
        if v['english'].rstrip('\t') != v['english'].rstrip('\t').rstrip()
        or v['italian'].rstrip('\t') != v['italian'].rstrip('\t').rstrip()])
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' you ', ' to the ', ' will be ',
        ' is ', ' are ', ' from the ', ' its ', ' it is ', ' such as ', ' rather than ')
LONG = ' '.join(v['italian'] for v in cov).lower()
ck('nessun residuo inglese fuori dai nomi tecnici', not [w for w in ENGW if w in LONG],
   [w for w in ENGW if w in LONG])
CORT = re.findall(r'\bLei\b|(?<![.!?] )\b(?:Suo|Sua|Suoi|Sue)\b', ' '.join(v['italian'] for v in cov))
ck('nessuna forma di cortesia «Lei»', not CORT, CORT)
rs = [v['ratio'] for v in cov]
ck('rapporto nel gate 0,55-1,90', 0.55 < min(rs) and max(rs) < 1.90, '%.2f - %.2f' % (min(rs), max(rs)))
bad = [(v['idx'], n) for v in cov for p, n in ((r"\b(e|piu|perche|cosi|gia|puo|cioe|percio|fa)'", 'accento'),
       ('\u2026', 'ellissi'), ('\u2014', 'em dash'), ('\u2013', 'en dash'), ('\u2019', 'apostrofo curvo'),
       ('\u00ab', 'caporale'), ('\u00bb', 'caporale')) if re.search(p, v['italian'])]
ck('tipografia (accenti veri, nessun carattere tipografico)', not bad, bad)
nonlat = [v['idx'] for v in cov for c in v['italian']
          if ord(c) > 127 and not 0x00C0 <= ord(c) <= 0x024F]
ck('caratteri non latini', not nonlat, nonlat)
c = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
st = dict(c.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('tutte le 9 unita sono PENDING nel database (misurato)',
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
