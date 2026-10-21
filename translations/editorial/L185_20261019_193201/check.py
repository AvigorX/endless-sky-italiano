r"""check.py — L185 (`data/gegno/gegno outfits.txt`, 13 unita', righe 17-157). **Apre il file.**

Primo lotto dei **Gegno**: 4 `VALUE` + 9 `DESCRIPTION`. I 4 `VALUE` sono **plurali** (`R01 Skirmish Batteries`) mentre i
contesti sono **singolari** (`outfit:R01 Skirmish Battery`) — il nome si copia com'e'. I **codici** (`R01`, `C3`, `C7`,
`C17`, `C27`, `I70`) non si traducono **mai**, nemmeno in prosa. Zero tab, zero virgolette (asserzioni vuote), **5 apici**
inglesi: quattro possessivi `Gegno's` e un `It's`.
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
VALUE = {1: 'R01 Skirmish Batteries', 3: 'R02 Battlezone Batteries',
         5: 'R03 Warforge Batteries', 7: 'R04 Crusade Batteries'}
CODES = ('R01', 'R02', 'R03', 'R04', 'C3', 'C7', 'C17', 'C27', 'I70')
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 13/13", len(cov) == 13 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 9 DESCRIPTION + 4 VALUE', collections.Counter(u['kind'] for u in units)
   == {'DESCRIPTION': 9, 'VALUE': 4})
ck('UN asserzione vuota: ZERO UI_LABEL', [u['idx'] for u in units if u['kind'] == 'UI_LABEL'] == [])
ck('ZERO token in tutto il lotto (asserzione vuota scritta)',
   {t for u in units for t in TAGS.findall(u['english'])} == set()
   == {t for v in cov for t in TAGS.findall(v['italian'])})
ck('ZERO tab in inglese e in italiano (asserzione vuota scritta)',
   [v['idx'] for v in cov if '\t' in v['english']] == []
   == [v['idx'] for v in cov if '\t' in v['italian']])
ck('ZERO virgolette in inglese e in italiano (asserzione vuota scritta)',
   sum(v['english'].count('"') for v in cov) == 0 == sum(v['italian'].count('"') for v in cov))
ck('i 4 VALUE identici al sorgente: PLURALI nel nome, singolare nel contesto',
   {v['idx']: v['italian'] for v in cov if v['kind'] == 'VALUE'} == VALUE
   and all(u['context'].split(':')[1].endswith('Battery') for u in units if u['kind'] == 'VALUE'))
ck('i codici restano invariati in ogni unita che li nomina',
   not [(v['idx'], c) for v in cov for c in CODES if c in v['english'] and c not in v['italian']],
   [(v['idx'], c) for v in cov for c in CODES if c in v['english'] and c not in v['italian']])
ck('`Gegno`, `Scin`, `Halite` restano invariati (fazioni e classi)',
   all(n in ' '.join(v['italian'] for v in cov) for n in ('Gegno', 'Scin', 'Halite')))
ck("5 apici inglesi: tre `Gegno's`, un `It's` e un `Halite's`",
   sum(v['english'].count("'") for v in cov) == 5
   and {v['idx']: v['english'].count("'") for v in cov if "'" in v['english']} == {4: 1, 9: 1, 11: 1, 12: 1, 13: 1}
   and sum(v['english'].count("Gegno's") for v in cov) == 3
   and sum(v['english'].count("Halite's") for v in cov) == 1
   and sum(v['english'].count("It's") for v in cov) == 1)
ck('nessun possessivo inglese sopravvissuto in italiano',
   not [v['idx'] for v in cov if re.search(r"\b[A-Za-z]+'s\b", v['italian'])])
ck('la scala delle batterie sale: comune, medio raggio, raffiche grandi, immensa',
   'molto comuni' in by[2]['italian'] and 'medio raggio' in by[4]['italian']
   and 'grandi e robusti' in by[6]['italian'] and 'immensa' in by[8]['italian'])
ck('idx 8 distingue la Crusade dalle altre: riserva dedicata vs batterie impilate',
   'riserva di energia' in by[8]['italian'] and 'impilare più batterie piccole' in by[8]['italian'])
ck('idx 10 racconta il problema di altezza della C7 (girata di lato)',
   'così alto' in by[10]['italian'] and 'girare completamente di lato' in by[10]['italian'])
ck('idx 13 e\' tecnologia degli Scin, non dei Gegno',
   'dagli Scin' in by[13]['italian'] and 'caccia Halite' in by[13]['italian'])
ck('13 unita, 13 testi inglesi distinti', len({v['english'] for v in cov}) == 13,
   len({v['english'] for v in cov}))
ck('9 contesti: quattro famiglie con 2 unita (VALUE + DESCRIPTION), cinque con 1',
   len({u['context'] for u in units}) == 9
   and sorted(collections.Counter(u['context'] for u in units).values()) == [1] * 5 + [2, 2, 2, 2],
   collections.Counter(u['context'] for u in units))
ck('prima e ultima unita: righe 17 e 157',
   (cov[0]['line'], cov[-1]['line']) == (17, 157)
   and cov[0]['context'] == 'outfit:R01 Skirmish Battery'
   and cov[-1]['context'] == 'outfit:I70 Ameliorate Cell')
ck('nessuno spazio finale (nessun tab in questo lotto)',
   not [v['idx'] for v in cov
        if v['english'] != v['english'].rstrip() or v['italian'] != v['italian'].rstrip()])
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' you ', ' to the ', ' will be ',
        ' is ', ' are ', ' from the ', ' its ', ' it is ', ' such as ', ' rather than ')
LONG = ' '.join(v['italian'] for v in cov).lower()
ck('nessun residuo inglese fuori dai nomi e dai codici', not [w for w in ENGW if w in LONG],
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
ck('tutte le 13 unita sono PENDING nel database (misurato)',
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
