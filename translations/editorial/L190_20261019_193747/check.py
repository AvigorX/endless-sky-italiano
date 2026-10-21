r"""check.py — L190 (`data/gegno/gegno outfits.txt`, 1 unita', riga 1137). **CHIUDE IL FILE: 60/60.**

Ultimo lotto del file, ridotto a una sola unita' perche' L189 si e' chiuso a 1130: la licenza `Scin Adjutant License`.
Una sola `DESCRIPTION`, zero tab, zero virgolette, zero apici. Le asserzioni «vuote» sono scritte comunque.
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


ck("unita' tradotta 1/1", len(cov) == 1 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 1 DESCRIPTION, ZERO VALUE (asserzione scritta)',
   collections.Counter(u['kind'] for u in units) == {'DESCRIPTION': 1})
ck('ZERO UI_LABEL, ZERO token (asserzioni vuote scritte)',
   [u['idx'] for u in units if u['kind'] == 'UI_LABEL'] == []
   and {t for u in units for t in TAGS.findall(u['english'])} == set())
ck('zero tab e zero virgolette; 0 apici inglesi, 1 italiano (elisione)',
   [v['idx'] for v in cov if chr(9) in v['english'] or chr(9) in v['italian']] == []
   and sum(v['english'].count(chr(34)) for v in cov) == 0 == sum(v['italian'].count(chr(34)) for v in cov)
   and sum(v['english'].count(chr(39)) for v in cov) == 0
   and sum(v['italian'].count(chr(39)) for v in cov) == 1)
ck('«Gegno Scin» resta invariato e la frase parla di acquisto',
   'Gegno Scin' in by[1]['italian'] and 'acquistare' in by[1]['italian'])
ck('la licenza e\' quella di livello piu\' basso («tecnologia più elementare»)',
   'più elementare' in by[1]['italian'] and 'Adjutant' in by[1]['context'])
ck('una sola unita: riga 1137, contesto `Scin Adjutant License`',
   cov[0]['line'] == 1137 and cov[0]['context'] == 'outfit:Scin Adjutant License')
ck('nessuno spazio finale (asserzione scritta)', not [v['idx'] for v in cov
                                                      if v['english'] != v['english'].rstrip() or v['italian'] != v['italian'].rstrip()])
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' you ', ' to the ', ' will be ',
        ' is ', ' are ', ' from the ', ' its ', ' it is ', ' such as ', ' rather than ')
ck('nessun residuo inglese fuori dai nomi', not [w for w in ENGW if w in ' '.join(v['italian'] for v in cov).lower()],
   [w for w in ENGW if w in ' '.join(v['italian'] for v in cov).lower()])
CORT = re.findall(r'\bLei\b|(?<![.!?] )\b(?:Suo|Sua|Suoi|Sue)\b', ' '.join(v['italian'] for v in cov))
ck('nessuna forma di cortesia «Lei»', not CORT, CORT)
rs = [v['ratio'] for v in cov]
ck('rapporto nel gate 0,55-1,90', 0.55 < min(rs) and max(rs) < 1.90, '%.2f' % min(rs))
bad = [(v['idx'], n) for v in cov for p, n in ((r"\b(e|piu|perche|cosi|gia|puo|cioe|percio|fa)'", 'accento'),
       ('\u2026', 'ellissi'), ('\u2014', 'em dash'), ('\u2013', 'en dash'), ('\u2019', 'apostrofo curvo')) if re.search(p, v['italian'])]
ck('tipografia (accenti veri, nessun carattere tipografico)', not bad, bad)
nonlat = [v['idx'] for v in cov for c in v['italian'] if ord(c) > 127 and not 0x00C0 <= ord(c) <= 0x024F]
ck('caratteri non latini', not nonlat, nonlat)
c = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
st = dict(c.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('l\'unica unita e\' PENDING (misurato)',
   c.execute('select count(*) from units where id in (%s) and state != "PENDING"'
             % ','.join('?' * len(units)), [u['id'] for u in units]).fetchone()[0] == 0)
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d' % (sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('righe %d/%d · parti %d · mancanti %d' % (min(u['line'] for u in units), max(u['line'] for u in units),
      len(parts), len([u for u in units if u['idx'] not in tr])))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
