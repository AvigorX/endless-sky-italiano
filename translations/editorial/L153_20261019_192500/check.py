r"""check.py — L153 (`data/coalition/coalition jobs.txt`, 20 unita', righe 1360-1469).

Controlli propri: **l'inversione dell'Arach** e quella del Saryd; le due descrizioni `Contain Criminals` con **rese
diverse** («sul posto» / «sul luogo»); i tre `DIALOG` con esiti diversi; **7 unita' con tab**; **20 virgolette**;
**16 token**; una sola asserzione vuota (`UI_LABEL`).
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


ck("unita' tradotte 20/20", len(cov) == 20 == len(units) and not missing, '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 1 LOGBOOK + 7 MISSION_TEXT + 4 VALUE + 4 DESCRIPTION + 4 DIALOG',
   collections.Counter(u['kind'] for u in units)
   == {'LOGBOOK': 1, 'MISSION_TEXT': 7, 'VALUE': 4, 'DESCRIPTION': 4, 'DIALOG': 4})
ck('UN asserzione vuota: ZERO UI_LABEL', [u['idx'] for u in units if u['kind'] == 'UI_LABEL'] == [])
ck('16 token su 4 simboli, stesso multiset in italiano',
   dict(collections.Counter(t for u in units for t in TAGS.findall(u['english'])))
   == {'<payment>': 7, '<destination>': 3, '<date>': 3, '<bunks>': 3}
   == dict(collections.Counter(t for u in cov for t in TAGS.findall(u['italian']))))
ck('parita per UNITA: stesso ordine di simboli in tutte le 20',
   not [v['idx'] for v in cov if TAGS.findall(v['italian']) != TAGS.findall(v['english'])])
ck('4 VALUE identici al sorgente, uno per uno',
   len(VAL) == 4 and all(by[i]['italian'].rstrip() == by[i]['english'].rstrip() for i in VAL),
   [(i, by[i]['italian']) for i in VAL])
ck('le 16 unita di testo sono tradotte (VALUE a parte)',
   not [v['idx'] for v in cov if v['kind'] != 'VALUE' and v['italian'].strip() == v['english'].strip()])
ck('7 unita con tab, le stesse in traduzione',
   [v['idx'] for v in cov if v['english'].startswith('\t')] == [2, 3, 4, 5, 6, 7, 8]
   == [v['idx'] for v in cov if v['italian'].startswith('\t')])
ck('20 virgolette, nessuna unita dispari, per unita identiche',
   sum(v['english'].count('"') for v in cov) == 20 == sum(v['italian'].count('"') for v in cov)
   and [v['idx'] for v in cov if v['english'].count('"') % 2] == []
   and not [v['idx'] for v in cov if v['english'].count('"') != v['italian'].count('"')])
ck('l Arach inverte: «ancora non possiamo vendere»',
   'ancora non possiamo vendere' in by[4]['italian'])
ck('il Saryd inverte: «per giustizia, è.» e «ogni è impegnato»',
   'per giustizia, è.' in by[7]['italian'] and 'ognuno è impegnato' in by[7]['italian'])
ck('le due descrizioni Contain Criminals hanno rese diverse',
   by[13]['italian'] != by[19]['italian'] and 'sul posto' in by[13]['italian']
   and 'sul luogo' in by[19]['italian'])
ck('i tre DIALOG raccontano esiti diversi (successo, fuga, sorpresa)',
   len({by[14]['italian'], by[17]['italian'], by[20]['italian']}) == 3
   and 'si arrendono' in by[14]['italian'] and 'fuggire' in by[17]['italian']
   and 'sorpresa' in by[20]['italian'])
ck('la descrizione della vendita e quella gia approvata in L152',
   by[10]['italian'] == 'Vendi un motore di salto agli Heliarch per <payment>.')
ck('17 stringhe distinte su 20 unita', len({(v['kind'], v['english'].lstrip('\t')) for v in cov}) == 17)
ck('zero spazi finali (20/20 identici al sorgente)',
   not [v['idx'] for v in cov
        if len(v['italian']) - len(v['italian'].rstrip()) != len(v['english']) - len(v['english'].rstrip())])
ck('prima e ultima unita: righe 1360 e 1469', (cov[0]['line'], cov[-1]['line']) == (1360, 1469),
   (cov[0]['line'], cov[-1]['line']))
LOW = ' '.join(v['italian'] for v in cov).lower()
TERMS = ('arachi', 'case', 'quarg', 'helarch' if False else 'heliarch', 'criminali', 'spazioporto', 'controllo')
ck('terminologia presente: 6 termini chiave',
   all(t in LOW for t in ('arachi', 'quarg', 'heliarch', 'criminali', 'spazioporto', 'scontro a fuoco')))
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' you ', ' to the ', ' will be ')
LONG = ' '.join(TAGS.sub('""', v['italian']) for v in cov if v['kind'] != 'VALUE').lower()
for s in ('arachi', 'arach', 'kimek', 'saryd', 'heliarch', 'quarg'):
    LONG = LONG.replace(s, '@@')
ck('nessun residuo inglese fuori dai nomi propri e dai VALUE',
   not [w for w in ENGW if w in LONG], [w for w in ENGW if w in LONG])
CORT = re.findall(r'\bLei\b|(?<![.!?] )\b(?:Suo|Sua|Suoi|Sue)\b', ' '.join(v['italian'] for v in cov))
ck('nessuna forma di cortesia «Lei»', not CORT, CORT)
rs = [v['ratio'] for v in cov]
ck('rapporto nel gate', 0.55 < min(rs) and max(rs) < 1.90, '%.2f - %.2f' % (min(rs), max(rs)))
bad = [(v['idx'], n) for v in cov for p, n in ((r"\b(e|piu|perche|cosi|gia|puo|cioe|percio|fa)'", 'accento'),
       ('\u2026', 'ellissi'), ('\u2014', 'em dash'), ('\u2013', 'en dash'), ('\u2019', 'apostrofo curvo'),
       ('\u00ab', 'caporale'), ('\u00bb', 'caporale')) if re.search(p, v['italian'])]
ck('tipografia', not bad, bad)
nonlat = [v['idx'] for v in cov for c in TAGS.sub('', v['italian'])
          if ord(c) > 127 and not 0x00C0 <= ord(c) <= 0x024F]
ck('caratteri non latini (fuori dai token)', not nonlat, nonlat)
c = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
st = dict(c.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('tutte le 20 unita sono PENDING nel database (misurato)',
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
