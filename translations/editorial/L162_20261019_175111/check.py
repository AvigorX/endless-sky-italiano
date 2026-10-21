r"""check.py — L162 (`data/avgi/avgi outfits.txt`, 10 unita', righe 112-193).

Controlli propri: **10 DESCRIPTION e zero VALUE**; **4 unita' con tab** (4, 6, 8, 10); **zero token, zero virgolette**
(asserzioni vuote scritte); **zero ripetizioni** (10 testi distinti su 10); i due generatori di scudi (Diffuse e
Specular) restano distinti; nomi propri (`Avgi`, `Deep`, oggetti) invariati.
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


NAMES = ['Cryogenic Deuterium Tank', 'Heatsink Partition', 'Multispectral Scanner', 'Spectrometer Array',
         'Diffuse Deflector', 'Specular Deflector', 'Avgi', 'Deep']
ck("unita' tradotte 10/10", len(cov) == 10 == len(units) and not missing, '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 10 DESCRIPTION, zero VALUE', collections.Counter(u['kind'] for u in units) == {'DESCRIPTION': 10})
ck('il lotto non ha VALUE: asserzione vuota scritta', [v['idx'] for v in cov if v['kind'] == 'VALUE'] == [])
ck('UN asserzione vuota: ZERO UI_LABEL', [u['idx'] for u in units if u['kind'] == 'UI_LABEL'] == [])
ck('ZERO token nel sorgente e in traduzione (asserzione vuota scritta)',
   [v['idx'] for v in cov if TAGS.findall(v['english'])] == [] == [v['idx'] for v in cov if TAGS.findall(v['italian'])])
ck('4 unita con tab iniziale: idx 4, 6, 8, 10, le stesse in traduzione',
   [v['idx'] for v in cov if v['english'].startswith('\t')] == [4, 6, 8, 10]
   == [v['idx'] for v in cov if v['italian'].startswith('\t')])
ck('ZERO virgolette (asserzione vuota scritta)',
   sum(v['english'].count('"') for v in cov) == 0 == sum(v['italian'].count('"') for v in cov))
ck('10 testi distinti su 10 unita (nessuna ripetizione)', len({v['english'] for v in cov}) == 10)
ck('ogni nome proprio dell inglese resta nell italiano (unita per unita)',
   not [v['idx'] for v in cov for n in NAMES if n in v['english'] and n not in v['italian']],
   [(v['idx'], n) for v in cov for n in NAMES if n in v['english'] and n not in v['italian']])
ck('nessun nome proprio inventato in italiano (insieme uguale)',
   {(v['idx'], n) for v in cov for n in NAMES if n in v['english']}
   == {(v['idx'], n) for v in cov for n in NAMES if n in v['italian']})
ck("i due generatori restano distinti per contenuto (anemico / il piu' grande)",
   len({by[i]['italian'] for i in (7, 8, 9, 10)}) == 4
   and 'anemico' in by[8]['italian'] and 'anemico' not in by[7]['italian']
   and 'di quanto non sia in realtà' in by[8]['italian']
   and 'Il più grande generatore di scudi' in by[9]['italian'])
ck('glossario: scudi, calore, energia, superconduttrici, carburante, sensori',
   all(t in ' '.join(v['italian'].lower() for v in cov)
       for t in ('scudi', 'calore', 'energia', 'superconduttrici', 'carburante', 'sensori')))
ck('termini di L161 riusati: poltiglia di deuterio, criorefrigeratori',
   'poltiglia di deuterio' in by[1]['italian'] and 'criorefrigeratori' in by[1]['italian'])
ck('prima e ultima unita: righe 112 e 193, contesti del contratto',
   (cov[0]['line'], cov[-1]['line']) == (112, 193)
   and cov[0]['context'] == 'outfit:Cryogenic Deuterium Tank' and cov[-1]['context'] == 'outfit:Specular Deflector',
   (cov[0]['line'], cov[-1]['line']))
ck('6 contesti distinti: due unita ciascuno tranne Heatsink e Cryogenic',
   len({u['context'] for u in units}) == 6
   and [collections.Counter(u['context'] for u in units)[c] for c in
        ('outfit:Cryogenic Deuterium Tank', 'outfit:Heatsink Partition', 'outfit:Multispectral Scanner',
         'outfit:Spectrometer Array', 'outfit:Diffuse Deflector', 'outfit:Specular Deflector')] == [1, 1, 2, 2, 2, 2],
   collections.Counter(u['context'] for u in units))
ck('zero spazi iniziali e finali identici al sorgente (10/10)',
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
ck('tutte le 10 unita sono PENDING nel database (misurato)',
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
