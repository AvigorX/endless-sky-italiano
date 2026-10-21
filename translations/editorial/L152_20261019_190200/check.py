r"""check.py — L152 (`data/coalition/coalition jobs.txt`, 21 unita', righe 1191-1359).

Controlli propri: **34 token su 6 simboli**; **2 unita' con tab** e **1 con le virgolette** (la battuta dell'Arach);
**3 `LOGBOOK`** e **3 `MISSION_TEXT`** tradotti (cambio di carattere del file); la resa dell'Arach conserva
l'**inversione** della sua specie; **7 `VALUE` identici**; una sola asserzione vuota (`UI_LABEL`).
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


ck("unita' tradotte 21/21", len(cov) == 21 == len(units) and not missing, '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 7 VALUE + 7 DESCRIPTION + 3 MISSION_TEXT + 3 LOGBOOK + 1 TEXT',
   collections.Counter(u['kind'] for u in units)
   == {'VALUE': 7, 'DESCRIPTION': 7, 'MISSION_TEXT': 3, 'LOGBOOK': 3, 'TEXT': 1})
ck('LOGBOOK e MISSION_TEXT tradotti (6 unita, il cambio di carattere del file)',
   not [v['idx'] for v in cov if v['kind'] in ('LOGBOOK', 'MISSION_TEXT')
        and v['italian'].strip() == v['english'].strip()])
ck('UN asserzione vuota: ZERO UI_LABEL', [u['idx'] for u in units if u['kind'] == 'UI_LABEL'] == [])
ck('34 token su 6 simboli, stesso multiset in italiano',
   dict(collections.Counter(t for u in units for t in TAGS.findall(u['english'])))
   == {'<planet>': 10, '<payment>': 9, '<bunks>': 6, '<date>': 3, '<origin>': 3, '<destination>': 3}
   == dict(collections.Counter(t for u in cov for t in TAGS.findall(u['italian']))))
ck('parita per UNITA: stesso ordine di simboli in tutte le 21',
   not [v['idx'] for v in cov if TAGS.findall(v['italian']) != TAGS.findall(v['english'])],
   [(v['idx'], TAGS.findall(v['english']), TAGS.findall(v['italian'])) for v in cov
    if TAGS.findall(v['italian']) != TAGS.findall(v['english'])])
ck('7 VALUE identici al sorgente, uno per uno',
   len(VAL) == 7 and all(by[i]['italian'].rstrip() == by[i]['english'].rstrip() for i in VAL),
   [(i, by[i]['italian']) for i in VAL if by[i]['italian'].rstrip() != by[i]['english'].rstrip()])
ck('le 14 unita di testo sono tradotte (VALUE a parte)',
   not [v['idx'] for v in cov if v['kind'] != 'VALUE' and v['italian'].strip() == v['english'].strip()])
ck('2 unita con tab (17, 18), le stesse in traduzione',
   [v['idx'] for v in cov if v['english'].startswith('\t')] == [17, 18]
   == [v['idx'] for v in cov if v['italian'].startswith('\t')])
ck('1 unita con 2 virgolette (17), la stessa in traduzione',
   [v['idx'] for v in cov if v['english'].count('"')] == [17]
   and by[17]['italian'].count('"') == 2)
ck('l Arach conserva l inversione della sua specie',
   'Enormemente prezioso è' in by[17]['italian']
   and 'ancora incapaci di crearne uno nostro siamo' in by[17]['italian'],
   by[17]['italian'][-160:])
ck('13 stringhe distinte su 21 unita', len({(v['kind'], v['english']) for v in cov}) == 13)
ck('zero spazi finali (21/21 identici al sorgente)',
   not [v['idx'] for v in cov
        if len(v['italian']) - len(v['italian'].rstrip()) != len(v['english']) - len(v['english'].rstrip())])
ck('8 contesti', len(set(v['context'] for v in cov)) == 8)
ck('prima e ultima unita: righe 1191 e 1359', (cov[0]['line'], cov[-1]['line']) == (1191, 1359),
   (cov[0]['line'], cov[-1]['line']))
LOW = ' '.join(v['italian'] for v in cov).lower()
TERMS = ('giochi della coalizione', 'motore di salto', 'anello', 'ingegneri', 'saryd', 'kimek', 'centauri',
         'insettoidi')
ck('terminologia presente: 8 termini chiave', all(t in LOW for t in TERMS), [t for t in TERMS if t not in LOW])
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' you ', ' to the ', ' will be ')
LONG = ' '.join(TAGS.sub('""', v['italian']) for v in cov if v['kind'] != 'VALUE').lower()
for s in ('saryd', 'kimek', 'arach', 'heliarch'):
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
ck('tutte le 21 unita sono PENDING nel database (misurato)',
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
