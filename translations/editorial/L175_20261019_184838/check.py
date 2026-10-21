r"""check.py — L175 (`data/avgi/avgi ships.txt`, 10 unita', righe 526-885).

Secondo lotto del file. Controlli propri: **le due unita' `TEXT` sono un NOME** (`Z-333 "Spark" Fusion Torch`) e devono
restare **identiche al sorgente** — comprese le **4 virgolette**, che sono tutte li'; **3 tab iniziali** (idx 3, 8, 10);
**3 apici inglesi, tutti in idx 5** (`fleet's`, `bay's`, `can't`) che in italiano **non** diventano possessivi; nomi di
astronavi, fazioni e veicoli **invariati**.
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
NAMES = ('Phononos', 'Photikon', 'Frequentia', 'Polari', 'Entasi', 'Avlaki', 'Harmonikos', 'Optikon',
         'Akoustiki Excursion Vehicle', 'Sonikis', 'Dissonance', 'Aberrant', 'Twilight Guard', 'Avgi')
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 10/10", len(cov) == 10 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 7 DESCRIPTION + 2 TEXT + 1 VALUE', collections.Counter(u['kind'] for u in units)
   == {'DESCRIPTION': 7, 'TEXT': 2, 'VALUE': 1})
ck('UN asserzione vuota: ZERO UI_LABEL', [u['idx'] for u in units if u['kind'] == 'UI_LABEL'] == [])
ck('ZERO token in tutto il lotto (asserzione vuota scritta)',
   {t for u in units for t in TAGS.findall(u['english'])} == set()
   == {t for v in cov for t in TAGS.findall(v['italian'])})
ck('i due TEXT sono un NOME e restano identici al sorgente (idx 4 e 6)',
   [v['idx'] for v in cov if v['kind'] == 'TEXT'] == [4, 6]
   and by[4]['italian'] == by[4]['english'] == by[6]['italian'] == by[6]['english']
   == 'Z-333 "Spark" Fusion Torch')
ck('4 virgolette, tutte nei due TEXT (2 + 2)',
   sum(v['english'].count('"') for v in cov) == 4 == sum(v['italian'].count('"') for v in cov)
   and [v['idx'] for v in cov if '"' in v['italian']] == [4, 6])
ck('1 VALUE identico al sorgente (Phononos)',
   [v['idx'] for v in cov if v['kind'] == 'VALUE'] == [1] and by[1]['italian'] == by[1]['english'] == 'Phononos')
ck('3 tab iniziali, idx 3, 8, 10 — uno solo per unita',
   [v['idx'] for v in cov if v['english'].startswith('\t')] == [3, 8, 10]
   == [v['idx'] for v in cov if v['italian'].startswith('\t')]
   and all(v['italian'].count('\t') == 1 for v in cov if v['italian'].startswith('\t')))
ck('3 apici inglesi, tutti in idx 5 (fleet\'s, bay\'s, can\'t)',
   sum(v['english'].count("'") for v in cov) == 3
   and by[5]['english'].count("'") == 3
   and all(w in by[5]['english'] for w in ("fleet's", "bay's", "can't"))
   and [v['idx'] for v in cov if "'" in v['english']] == [5])
ck("nessun possessivo inglese residuo in italiano (niente apici alla inglese)",
   not [v['idx'] for v in cov if re.search(r"[A-Za-z]+'s\b", v['italian'])])
ck('i nomi restano invariati in ogni unita che li nomina',
   not [(v['idx'], n) for v in cov for n in NAMES if n in v['english'] and n not in v['italian']],
   [(v['idx'], n) for v in cov for n in NAMES if n in v['english'] and n not in v['italian']])
ck('la classe e una sola parola: «classe Frequentia» e «classe Polari»',
   'classe Frequentia' in by[5]['italian'] and 'classe Polari' in by[7]['italian'])
ck('10 unita, 9 testi inglesi distinti (i due TEXT coincidono)',
   len({v['english'] for v in cov}) == 9, len({v['english'] for v in cov}))
ck('4 contesti distinti, 2+2+3+3 unita',
   len({u['context'] for u in units}) == 4
   and sorted(collections.Counter(u['context'] for u in units).values()) == [2, 2, 3, 3],
   collections.Counter(u['context'] for u in units))
ck('prima e ultima unita: righe 526 e 885',
   (cov[0]['line'], cov[-1]['line']) == (526, 885)
   and cov[0]['context'] == 'ship:Phononos' and cov[-1]['context'] == 'ship:Entasi')
ck('nessuno spazio finale, tab iniziale ammesso',
   not [v['idx'] for v in cov
        if v['english'].rstrip('\t') != v['english'].rstrip('\t').rstrip()
        or v['italian'].rstrip('\t') != v['italian'].rstrip('\t').rstrip()])
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' you ', ' to the ', ' will be ',
        ' is ', ' are ', ' from the ', ' its ', ' it is ', ' such as ')
LONG = ' '.join(v['italian'] for v in cov if v['kind'] == 'DESCRIPTION').lower()
ck('nessun residuo inglese nelle DESCRIPTION', not [w for w in ENGW if w in LONG], [w for w in ENGW if w in LONG])
CORT = re.findall(r'\bLei\b|(?<![.!?] )\b(?:Suo|Sua|Suoi|Sue)\b', ' '.join(v['italian'] for v in cov))
ck('nessuna forma di cortesia «Lei»', not CORT, CORT)
rs = [v['ratio'] for v in cov if v['kind'] == 'DESCRIPTION']
ck('rapporto nel gate 0,55-1,90 (solo DESCRIPTION: i nomi hanno rapporto 1)',
   0.55 < min(rs) and max(rs) < 1.90, '%.2f - %.2f' % (min(rs), max(rs)))
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
      len(parts), len([u for u in units if u['idx'] not in tr])))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
