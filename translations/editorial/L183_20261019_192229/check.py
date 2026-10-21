r"""check.py — L183 (`data/human/outfits.txt`, 15 unita', righe 390-514).

Quarto lotto del file: **11 `DESCRIPTION` + 4 `VALUE`** (il massimo di `VALUE` finora), **1 tab** (idx 14), zero
virgolette, **3 apici inglesi** tutti di elisione (`you're`, `you've`, `don't`) e **nessun apice in un nome** in questo
lotto — `Old Man's Sword` e' il *contesto* di idx 15, non il testo. Controlli propri: i 4 `VALUE` identici al sorgente
(`Antigrav Glasses` e' **plurale** nel nome e singolare nel contesto), la voce comica del `Mug` (idx 11) e il finale
sospeso del gas nervino (`...`, non `…`).
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
VALUE = {1: 'Luxury Accommodations', 6: 'Fragmentation Grenades', 9: 'Nerve Gas', 12: 'Antigrav Glasses'}
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 15/15", len(cov) == 15 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 11 DESCRIPTION + 4 VALUE', collections.Counter(u['kind'] for u in units)
   == {'DESCRIPTION': 11, 'VALUE': 4})
ck('UN asserzione vuota: ZERO UI_LABEL', [u['idx'] for u in units if u['kind'] == 'UI_LABEL'] == [])
ck('ZERO token in tutto il lotto (asserzione vuota scritta)',
   {t for u in units for t in TAGS.findall(u['english'])} == set()
   == {t for v in cov for t in TAGS.findall(v['italian'])})
ck('ZERO virgolette in inglese e in italiano (asserzione vuota scritta)',
   sum(v['english'].count('"') for v in cov) == 0 == sum(v['italian'].count('"') for v in cov))
ck('i 4 VALUE identici al sorgente, uno per uno',
   {v['idx']: v['italian'] for v in cov if v['kind'] == 'VALUE'} == VALUE)
ck('`Antigrav Glasses` e\' PLURALE nel nome e singolare nel contesto (non si "corregge")',
   by[12]['english'] == 'Antigrav Glasses' and 'Antigrav Glass' == by[13]['context'].split(':')[1]
   and by[12]['italian'].endswith('Glasses'))
ck('1 tab iniziale, idx 14, in inglese e in italiano',
   [v['idx'] for v in cov if v['english'].startswith('\t')] == [14]
   == [v['idx'] for v in cov if v['italian'].startswith('\t')])
ck("3 apici inglesi, tutti di elisione (`you're`, `you've`, `don't`): nessun possessivo in prosa",
   sum(v['english'].count("'") for v in cov) == 3
   and {v['idx']: v['english'].count("'") for v in cov if "'" in v['english']} == {4: 1, 14: 1, 15: 1}
   and not re.search(r"[A-Za-z]+'s\b", ' '.join(v['english'] for v in cov)))
ck('nessun possessivo inglese sopravvissuto in italiano e nessun apice inventato',
   not [v['idx'] for v in cov if re.search(r"\b[A-Za-z]+'s\b", v['italian'])])
ck('la voce comica del Mug (idx 11) resta comica e breve',
   'lanciarlo' in by[11]['italian'] and 'supponi' in by[11]['italian']
   and len(by[11]['italian'].split()) <= 10)
ck('il gas nervino chiude con i tre punti, non con il carattere ellissi (idx 10)',
   by[10]['english'].endswith('...') and by[10]['italian'].endswith('...')
   and '\u2026' not in by[10]['italian'])
ck('`Nerve Gas` nella prosa diventa «gas nervino»', 'gas nervino' in by[10]['italian'])
ck('idx 15 nomina la polvere da sparo e le iscrizioni illeggibili',
   'polvere da sparo' in by[15]['italian'] and 'iscrizioni' in by[15]['italian']
   and 'nessuna lingua umana' in by[15]['italian'])
ck('la coppia Antigrav Glass: idx 13 spiega la levitazione, idx 14 il peso',
   'levitazione' in by[13]['italian'] and 'più pesante' in by[14]['italian'])
ck('15 unita, 15 testi inglesi distinti', len({v['english'] for v in cov}) == 15,
   len({v['english'] for v in cov}))
ck('10 contesti: Antigrav Glass con 3 unita, altri tre con 2, sei con 1',
   len({u['context'] for u in units}) == 10
   and sorted(collections.Counter(u['context'] for u in units).values()) == [1] * 6 + [2, 2, 2, 3],
   collections.Counter(u['context'] for u in units))
ck('prima e ultima unita: righe 390 e 514',
   (cov[0]['line'], cov[-1]['line']) == (390, 514)
   and cov[0]['context'] == 'outfit:Luxury Accommodations' and cov[-1]['context'] == "outfit:Old Man's Sword")
ck('nessuno spazio finale, tab iniziale ammesso',
   not [v['idx'] for v in cov
        if v['english'].rstrip('\t') != v['english'].rstrip('\t').rstrip()
        or v['italian'].rstrip('\t') != v['italian'].rstrip('\t').rstrip()])
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' you ', ' to the ', ' will be ',
        ' is ', ' are ', ' from the ', ' its ', ' it is ', ' such as ', ' rather than ')
LONG = ' '.join(v['italian'] for v in cov).lower()
ck('nessun residuo inglese fuori dai nomi', not [w for w in ENGW if w in LONG],
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
ck('tutte le 15 unita sono PENDING nel database (misurato)',
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
