r"""check.py — L221 (`data/successors/successor ships.txt`, 24 unita', righe 904-1137). Quarto lotto del file.

**17 unita' su 24 identiche all'inglese** (15 `TEXT` + 2 `VALUE`), **7 `DESCRIPTION`** tradotte. I nomi sono **generati dal
sorgente**, non trascritti (regola introdotta in L220 dopo 11 unita' sbagliate su 20).

**Il tratto del lotto: tre schede quasi parallele.** Le `DESCRIPTION` di Stolsaqra (15 e 17) condividono tre formule, e la
17 le condivide in parte con la 16:

| formula inglese | resa unica |
|---|---|
| *sports a surprising amount of firepower for a ship of its size* | «sfoggia una potenza di fuoco sorprendente per una nave delle sue dimensioni» |
| *plagued with power and propulsion issues* | «afflitto da problemi di energia e propulsione» |
| *albeit with significantly downgraded systems compared to the military-exclusive model* | «anche se con sistemi notevolmente depotenziati rispetto al modello riservato ai militari» |

**I 3 tab stanno tutti in `DESCRIPTION`** (unita' 7, 16, 24), non in `TEXT`: e' l'opposto del lotto precedente, dove il tab
era in una sola unita'. **Le 30 virgolette sono 2 x 15 `TEXT`** e nessuna in prosa: misurato, non dedotto.
"""
import collections
import json
import os
import re
import sqlite3

TAB = chr(9)
QUOTE = chr(34)
APOS = chr(39)
TAG = re.compile(r'<[^<>]+>')
HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
PATH = 'data/successors/successor ships.txt'
FIREPOWER = 'una potenza di fuoco sorprendente per una nave delle sue dimensioni'
PLAGUE = 'afflitto da problemi di energia e propulsione'
DOWNGRADED = 'sistemi notevolmente depotenziati rispetto al modello riservato ai militari'
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
IT_ALL = ' '.join(v['italian'] for v in cov)
KINDS = collections.Counter(u['kind'] for u in units)
CTX = collections.Counter(u['context'] for u in units)
TEXTS = [u['idx'] for u in units if u['kind'] == 'TEXT']
VALS = [u['idx'] for u in units if u['kind'] == 'VALUE']
DESCS = [u['idx'] for u in units if u['kind'] == 'DESCRIPTION']
EN_Q = {v['idx']: v['english'].count(QUOTE) for v in cov if QUOTE in v['english']}
IT_Q = {v['idx']: v['italian'].count(QUOTE) for v in cov if QUOTE in v['italian']}
EN_A = [(v['idx'], v['english'].count(APOS)) for v in cov if APOS in v['english']]
IT_A = [(v['idx'], v['italian'].count(APOS)) for v in cov if APOS in v['italian']]
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 24/24", len(cov) == 24 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 15 TEXT, 7 DESCRIPTION, 2 VALUE (asserzione scritta)',
   KINDS == {'TEXT': 15, 'DESCRIPTION': 7, 'VALUE': 2}, dict(KINDS))
ck('ZERO DIALOG, MISSION_TEXT, LOGBOOK, NEWS, UI_LABEL (asserzioni vuote scritte)',
   [u['idx'] for u in units if u['kind'] not in ('TEXT', 'DESCRIPTION', 'VALUE')] == [])
ck('3 contesti con le dimensioni misurate: Stolsaqra 10, Seiitej 7, Veusade 7',
   CTX == {'ship:Seiitej': 7, 'ship:Stolsaqra': 10, 'ship:Veusade': 7}, dict(CTX))
ck('righe 904 e 1137 (prima e ultima del lotto)',
   (cov[0]['line'], cov[-1]['line']) == (904, 1137), (cov[0]['line'], cov[-1]['line']))
ck('3 tab, tutti in DESCRIPTION (unita\' 7, 16, 24), identici nelle due lingue',
   [v['idx'] for v in cov if TAB in v['english']] == [7, 16, 24]
   == [v['idx'] for v in cov if TAB in v['italian']]
   and all(v['kind'] == 'DESCRIPTION' for v in cov if TAB in v['italian'])
   and all(by[i]['italian'].startswith(TAB) and not by[i]['italian'].startswith(TAB + TAB) for i in (7, 16, 24)))
ck('30 virgolette: 2 per ognuna delle 15 TEXT e NESSUNA in prosa (misurato)',
   sum(EN_Q.values()) == 30 == sum(IT_Q.values()) and EN_Q == IT_Q
   and EN_Q == {i: 2 for i in TEXTS} and len(EN_Q) == 15, (EN_Q, IT_Q))
ck('NESSUN segnaposto (asserzione negativa scritta)',
   sum(len(TAG.findall(v['english'])) for v in cov) == 0
   == sum(len(TAG.findall(v['italian'])) for v in cov))
ck('17 unita\' IDENTICHE all\'inglese (15 TEXT + 2 VALUE) e 7 tradotte: sono esattamente le DESCRIPTION',
   sum(1 for v in cov if v['italian'] == v['english']) == 17
   and sorted(v['idx'] for v in cov if v['italian'] != v['english']) == DESCS,
   (sum(1 for v in cov if v['italian'] == v['english']),
    sorted(v['idx'] for v in cov if v['italian'] != v['english'])))
ck('i nomi sono COPIATI dal sorgente: 15 TEXT e 2 VALUE identici carattere per carattere',
   all(by[i]['italian'] == by[i]['english'] for i in TEXTS + VALS))
ck('COERENZA 15/17: stessa resa della potenza di fuoco e dei problemi di propulsione',
   FIREPOWER in by[15]['italian'] and FIREPOWER in by[17]['italian']
   and PLAGUE in by[15]['italian'] and PLAGUE in by[17]['italian'])
ck('COERENZA 16/17: stessa resa della versione depotenziata per il pubblico',
   DOWNGRADED in by[16]['italian'] and DOWNGRADED in by[17]['italian'])
ck('COERENZA 15/17: «intercettore» e «per una nave delle sue dimensioni» in entrambe',
   'intercettore' in by[15]['italian'] and 'intercettore' in by[17]['italian'])
ck('terminologia: «Alte Case», «Predecessori», «Successori»; «High Houses» assente',
   'Alte Case' in IT_ALL and 'Predecessori' in IT_ALL and 'Successori' in IT_ALL
   and 'High Houses' not in IT_ALL)
ck('le 7 DESCRIPTION sono tutte tradotte e tutte distinte',
   len(DESCS) == 7 and all(by[i]['italian'] != by[i]['english'] for i in DESCS)
   and len({by[i]['italian'] for i in DESCS}) == 7)
ck("apici: 5 in inglese (6 High Houses', 7 Houses', 17 Successors', 23 ship's, 24 Predecessors') "
   "e 2 in italiano (16 l'unica, 24 all'uso): distribuzione diversa, totale diverso",
   sum(n for _, n in EN_A) == 5 and sum(n for _, n in IT_A) == 2
   and EN_A == [(6, 1), (7, 1), (17, 1), (23, 1), (24, 1)] and IT_A == [(16, 1), (24, 1)], (EN_A, IT_A))
ck('registro: nessun «Lei» e nessun «mi scusi»',
   not re.search(r'\bLei\b|mi scusi', IT_ALL))
ck('nessun caporale e nessun carattere tipografico',
   not [v['idx'] for v in cov if any(c in v['italian'] for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026')])
DESC_TXT = ' '.join(by[i]['italian'] for i in DESCS)
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' you ', ' to the ', ' will be ',
        ' is ', ' are ', ' from the ', ' its ', ' it is ', ' such as ', ' rather than ', ' for a ', ' that ',
        ' have ', ' they ', ' their ', ' while ')
ck('nessun residuo inglese nelle DESCRIPTION (i nomi sono esclusi perche\' identici)',
   not [w for w in ENGW if w in DESC_TXT.lower()], [w for w in ENGW if w in DESC_TXT.lower()])
rs = [v['ratio'] for v in cov]
ck('rapporto nel gate 0,55-1,90 (nomi 1,00; DESCRIPTION 0,99-1,21)',
   0.55 < min(rs) and max(rs) < 1.90, '%.2f - %.2f' % (min(rs), max(rs)))
ACC = re.compile(r"\b(e|piu|perche|cosi|gia|puo|cioe|percio|fa)'", re.I)
bad = [(v['idx'], ACC.search(v['italian']).group(0)) for v in cov if ACC.search(v['italian'])]
ck('tipografia (accenti veri, nessun apostrofo al posto dell\'accento)', not bad, bad)
nonlat = [v['idx'] for v in cov for c in v['italian'] if ord(c) > 127 and not 0x00C0 <= ord(c) <= 0x024F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio (tab iniziali delle 7, 16, 24 ammessi)',
   not [v['idx'] for v in cov if v['italian'] != v['italian'].rstrip()
        or '  ' in v['italian'].strip(TAB) or v['english'] != v['english'].rstrip()])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck('96 unita tradotte prima della 904 (L218 45 + L219 25 + L220 26)',
   db.execute('select count(*) from units where path=? and line<904', (PATH,)).fetchone()[0] == 96)
ck('lotto + residuo = file: 96 + 24 + 26 = 146',
   96 + 24 + db.execute('select count(*) from units where path=? and line>1137', (PATH,)).fetchone()[0] == 146)
st = dict(db.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('le 24 unita sono PENDING (misurato)',
   db.execute('select count(*) from units where id in (%s) and state != "PENDING"'
              % ','.join('?' * len(units)), [u['id'] for u in units]).fetchone()[0] == 0)
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d' % (sum(len(v['english'].split()) for v in cov),
                                sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
