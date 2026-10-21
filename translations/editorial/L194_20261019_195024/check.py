r"""check.py — L194 (`data/bunrodea/bunrodea missions.txt`, 18 unita', righe 152-203).

Quarto lotto: le risposte al trono, i tre ranghi offesi (`Erabu`, `Megasa`, guardia reale) e la clemenza della Regina.
**18 `MISSION_TEXT`**, **18 tab**, **48 virgolette** (24 coppie). Controlli propri: quattro battute sono **ripetizioni
testuali dal lotto precedente** (L193) e devono avere la stessa resa — il `check.py` **legge il `translation.json` di
L193** e confronta, invece di fidarsi della memoria.
"""
import collections
import json
import os
import re
import sqlite3

TAB = chr(9)
QUOTE = chr(34)
HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
PREV = os.path.join(L10N, 'staging/editorial/L193_20261019_194924/translation.json')
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
IT_ALL = ' '.join(v['italian'] for v in cov)
EN_Q = sum(v['english'].count(QUOTE) for v in cov)
IT_Q = sum(v['italian'].count(QUOTE) for v in cov)
prev = {u['english']: u['italian'] for u in json.load(open(PREV, encoding='utf-8'))['units']}
repeats = [(i, by[i]['english']) for i in (1, 3, 4, 6, 7, 8, 9) if by[i]['english'] in prev]
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 18/18", len(cov) == 18 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 18 MISSION_TEXT, ZERO VALUE (asserzione scritta)',
   collections.Counter(u['kind'] for u in units) == {'MISSION_TEXT': 18})
ck('ZERO UI_LABEL e ZERO token (asserzioni vuote scritte)',
   [u['idx'] for u in units if u['kind'] == 'UI_LABEL'] == []
   and {t for u in units for t in TAGS.findall(u['english'])} == set())
ck('18 tab e 48 virgolette (24 coppie) in entrambe le lingue',
   [v['idx'] for v in cov if v['english'].startswith(TAB)] == list(range(1, 19))
   and EN_Q == 48 == IT_Q, (EN_Q, IT_Q))
ck('nessun caporale in italiano',
   not [v['idx'] for v in cov if any(c in v['italian'] for c in '\u00ab\u00bb\u201c\u201d')])
ck('le battute ripetute da L193 hanno la STESSA resa (confronto con il lotto precedente)',
   len(repeats) >= 6 and all(by[i]['italian'] == prev[by[i]['english']] for i, _ in repeats),
   [(i, by[i]['italian'], prev.get(by[i]['english'])) for i, _ in repeats
    if by[i]['italian'] != prev.get(by[i]['english'])])
ck("i tre ranghi si distinguono: `Erabu` aristocratici, `Megasa` gli ultimi, la guardia reale",
   'aristocratici' in by[10]['italian'] and 'i più umili del mio popolo' in by[11]['italian']
   and 'guardia reale' in by[15]['italian'])
ck('idx 15 e 16 condividono la seconda parte del discorso della Regina',
   'farebbe davvero il proprio dovere' in by[15]['italian']
   and 'farebbe davvero il proprio dovere' in by[16]['italian']
   and 'chi ti ha offeso' in by[15]['italian'] and 'chi ti ha offeso' in by[16]['italian'])
ck('idx 17 e 18 differiscono in un punto (mentire / parlare) e sono identici altrove',
   'mentire così' in by[17]['italian'] and 'parlare così' in by[18]['italian']
   and ('torreggiare su di te' in by[17]['italian']) == ('torreggiare su di te' in by[18]['italian'])
   and 'Mostrerò clemenza' in by[17]['italian'] and 'Mostrerò clemenza' in by[18]['italian'])
ck('la Regina scende dal trono e torreggia (idx 17-18)',
   'scende dal trono' in by[17]['italian'] and 'doppio della tua altezza' in by[18]['italian'])
ck('18 unita, 14 testi distinti: 1=7, 3=8 e «Okay, and?» tre volte (4, 9, 14)',
   len({v['english'] for v in cov}) == 14
   and by[1]['english'] == by[7]['english'] and by[3]['english'] == by[8]['english']
   and by[4]['english'] == by[9]['english'] == by[14]['english'])
ck('un solo contesto, righe 152 e 203', len({u['context'] for u in units}) == 1
   and (cov[0]['line'], cov[-1]['line']) == (152, 203))
ck('nessuno spazio finale (tab iniziali ammessi)',
   not [v['idx'] for v in cov if v['english'].rstrip(TAB) != v['english'].rstrip(TAB).rstrip()
        or v['italian'].rstrip(TAB) != v['italian'].rstrip(TAB).rstrip()])
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' you ', ' to the ', ' will be ',
        ' is ', ' are ', ' from the ', ' its ', ' it is ', ' such as ', ' rather than ')
ck('nessun residuo inglese', not [w for w in ENGW if w in IT_ALL.lower()],
   [w for w in ENGW if w in IT_ALL.lower()])
CORT = re.findall(r'\bLei\b|(?<![.!?] )\b(?:Suo|Sua|Suoi|Sue)\b', IT_ALL)
ck('nessuna forma di cortesia «Lei»', not CORT, CORT)
rs = [v['ratio'] for v in cov]
ck('rapporto nel gate 0,55-1,90', 0.55 < min(rs) and max(rs) < 1.90, '%.2f - %.2f' % (min(rs), max(rs)))
bad = [(v['idx'], n) for v in cov for p, n in ((r"\b(e|piu|perche|cosi|gia|puo|cioe|percio|fa)'", 'accento'),
       ('\u2026', 'ellissi'), ('\u2014', 'em dash'), ('\u2013', 'en dash'), ('\u2019', 'apostrofo curvo')) if re.search(p, v['italian'])]
ck('tipografia (accenti veri, nessun carattere tipografico)', not bad, bad)
nonlat = [v['idx'] for v in cov for c in v['italian'] if ord(c) > 127 and not 0x00C0 <= ord(c) <= 0x024F]
ck('caratteri non latini', not nonlat, nonlat)
c = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
st = dict(c.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('tutte le 18 unita sono PENDING (misurato)',
   c.execute('select count(*) from units where id in (%s) and state != "PENDING"'
             % ','.join('?' * len(units)), [u['id'] for u in units]).fetchone()[0] == 0)
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d' % (sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('battute ripetute verificate contro L193: %d' % len(repeats))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
