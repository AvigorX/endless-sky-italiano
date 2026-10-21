r"""check.py — L250 (`data/human/syndicate jobs.txt`, 27 unita', righe 435-678). Quarto lotto del file.

**Lotto «a schede»**: **11 `VALUE`** (nomi di lavoro, copiati) + **11 `DESCRIPTION`** + **5 `DIALOG`**. Un solo `VALUE`,
`Shipment to <planet>`, compare **sei volte** in sei contesti diversi: e' un dato con un segnaposto dentro, e si copia sei
volte.

**Tre gruppi di inglese identico**: `Shipment to <planet>` (6), la richiesta di `Syndicated Shipyards` (3), la consegna a
`Syndicated Systems` (2). Una sola resa per gruppo, con la **molteplicita' massima** asserita.

**46 segnaposto in 6 famiglie** (`<payment>` 16, `<planet>` 11, `<cargo>` 7, `<destination>` 6, `<bunks>` 4, `<origin>` 2),
per famiglia **e** per ordine dentro ogni unita'. **Zero tab**, **4 virgolette** (unita' 5 e 6: «"trattamento"», «"traditori
di classe"»), **zero apici inglesi** e **2 italiani** (`dell'arresto`, `l'ingresso`).
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
PATH = 'data/human/syndicate jobs.txt'
src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
units = sorted(src['units'], key=lambda x: x['line'])
tr = {}
for p in sorted(f for f in os.listdir(os.path.join(HERE, 'parts')) if f.endswith('.json')):
    for k, v in json.load(open(os.path.join(HERE, 'parts', p), encoding='utf-8')).items():
        tr[int(k)] = v
out = {'block': src['block'], 'note': src['note'], 'units': []}
for u in units:
    if u['idx'] in tr:
        it = tr[u['idx']]
        out['units'].append({"idx": u['idx'], "id": u['id'], "path": u['path'], "line": u['line'],
                             "kind": u['kind'], "context": u['context'], "english": u['english'],
                             "italian": it, "ratio": round(len(it) / max(1, len(u['english'])), 3)})
open(os.path.join(HERE, 'translation.json'), 'w', encoding='utf-8').write(
    json.dumps(out, ensure_ascii=False, indent=1))
cov = out['units']
KINDS = collections.Counter(u['kind'] for u in units)
VAL = [v for v in cov if v['kind'] == 'VALUE']
PROSA = [v for v in cov if v['kind'] in ('DESCRIPTION', 'DIALOG')]
TOK_EN = collections.Counter(t for v in cov for t in TAG.findall(v['english']))
TOK_IT = collections.Counter(t for v in cov for t in TAG.findall(v['italian']))
SEQ = [v['idx'] for v in cov if TAG.findall(v['english']) != TAG.findall(v['italian'])]
A_EN = [(v['idx'], v['english'].count(APOS)) for v in cov if APOS in v['english']]
A_IT = [(v['idx'], v['italian'].count(APOS)) for v in cov if APOS in v['italian']]
Q_IT = [(v['idx'], v['italian'].count(QUOTE)) for v in cov if QUOTE in v['italian']]
prosa = ' '.join(v['italian'] for v in PROSA)
ctx = collections.Counter(u['context'] for u in units)
mult = collections.Counter(v['english'] for v in cov)
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 27/27", len(cov) == 27 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna unita\' vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 11 VALUE + 11 DESCRIPTION + 5 DIALOG',
   dict(KINDS) == {'VALUE': 11, 'DESCRIPTION': 11, 'DIALOG': 5}, dict(KINDS))
ck('11 contesti distinti',
   len(ctx) == 11 and set(ctx) == {
       'mission:Syndicate Prisoner Transport [3]', 'mission:Syndicate Prisoner Transport [4]',
       'mission:Return Syndicate Prisoners [0]', 'mission:Return Syndicate Prisoners [1]',
       'mission:Return Syndicate Prisoners [2]', 'mission:Syndicated Shipyards Shipment [0]',
       'mission:Syndicated Shipyards Shipment [1]', 'mission:Syndicated Shipyards Shipment [2]',
       'mission:Syndicated Shipyards Shipment [3]', 'mission:Syndicated Systems Shipment [0]',
       'mission:Syndicated Systems Shipment [1]'}, len(ctx))
ck('righe 435 e 678 (prima e ultima del lotto)',
   (cov[0]['line'], cov[-1]['line']) == (435, 678), (cov[0]['line'], cov[-1]['line']))
ck("gli 11 VALUE sono IDENTICI all'inglese (6 distinti)",
   len(VAL) == 11 and all(v['italian'] == v['english'] for v in VAL)
   and len({v['english'] for v in VAL}) == 6,
   [v['idx'] for v in VAL if v['italian'] != v['english']])
ck('il `VALUE` `Shipment to <planet>` compare SEI volte, identico in tutte',
   mult['Shipment to <planet>'] == 6
   and len({v['italian'] for v in cov if v['english'] == 'Shipment to <planet>'}) == 1)
ck("le 16 unita' di prosa sono TUTTE tradotte (0 identiche)",
   all(v['italian'] != v['english'] for v in PROSA) and len(PROSA) == 16)
ck('3 gruppi di inglese identico, una resa ciascuno: 6, 3 e 2 copie',
   sum(1 for e, n in mult.items() if n > 1) == 3 and max(mult.values()) == 6
   and sorted(n for e, n in mult.items() if n > 1) == [2, 3, 6]
   and all(len({v['italian'] for v in cov if v['english'] == e}) == 1 for e, n in mult.items() if n > 1),
   sorted(n for e, n in mult.items() if n > 1))
ck('46 segnaposto in 6 famiglie, multiset identico',
   TOK_EN == TOK_IT and sum(TOK_EN.values()) == 46 and len(TOK_EN) == 6,
   (dict(TOK_EN), sum(TOK_EN.values())))
ck("l'ORDINE dei segnaposto e' identico dentro ogni unita'", not SEQ, SEQ)
ck('ZERO tab (asserzione negativa scritta)',
   sum(v['english'].count(TAB) for v in cov) == 0 == sum(v['italian'].count(TAB) for v in cov))
ck('4 virgolette nelle unita\' 5 e 6: «"trattamento"» e «"traditori di classe"»',
   Q_IT == [(5, 2), (6, 2)] and '"trattamento"' in cov[4]['italian']
   and '"traditori di classe"' in cov[5]['italian'], Q_IT)
ck("apici: ZERO in inglese, 2 in italiano (unita' 3 e 9: `dell'arresto`, `l'ingresso`)",
   A_EN == [] and A_IT == [(3, 1), (9, 1)], (A_EN, A_IT))
ck('lessico dei prigionieri: «manifestanti», «sindacalisti», «colletti bianchi», «prosciolto»',
   all(t in prosa for t in ('manifestanti', 'sindacalisti', 'colletti bianchi', 'prosciolto')))
ck('la coda fissa delle due schede di detenzione e\' identica («in strutture adatte al trasferimento dei criminali»)',
   [v['idx'] for v in PROSA if 'strutture adatte al trasferimento dei criminali' in v['italian']] == [2, 5])
ck('«Il pagamento è <payment>.» nelle 11 schede',
   sum(1 for v in PROSA if 'Il pagamento è <payment>.' in v['italian']) == 11)
ck('«Ricevi il pagamento di <payment>.» nelle 4 battute (3, 6, 12, 15)',
   [v['idx'] for v in PROSA if 'Ricevi il pagamento di <payment>.' in v['italian']] == [3, 6, 12, 15])
ck('nomi propri invariati: `Syndicated Shipyards` (4 unita\') e `Syndicated Systems` (2)',
   sum(1 for v in cov if 'Syndicated Shipyards' in v['english']) == 4
   and sum(1 for v in cov if 'Syndicated Systems' in v['english']) == 2
   and prosa.count('Syndicated Shipyards') == 4 and prosa.count('Syndicated Systems') == 2)
ck('nessun residuo inglese di struttura (the, and, with, that, from, your)',
   not [w for w in (' the ', ' and ', ' with ', ' that ', ' from ', ' your ') if w in prosa.lower()],
   [w for w in (' the ', ' and ', ' with ', ' that ', ' from ', ' your ') if w in prosa.lower()])
ck('registro: nessun «Lei» e nessuna cortesia',
   not re.search(r'\bLei\b|\bSuo\b|\bSua\b|mi scusi', prosa))
ck('nessun caporale e nessun carattere tipografico',
   not [v['idx'] for v in cov if any(c in v['italian'] for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026')])
rs = [v['ratio'] for v in cov]
ck('rapporto nel gate 0,55-1,90 (0,90-1,26; 432 -> 454 parole)',
   0.55 < min(rs) and max(rs) < 1.90, '%.2f - %.2f' % (min(rs), max(rs)))
ACC = re.compile(r"\b(e|piu|perche|cosi|gia|puo|cioe|percio)'(?![a-z])", re.I)
bad = [(v['idx'], ACC.search(v['italian']).group(0)) for v in cov if ACC.search(v['italian'])]
ck("tipografia (accenti veri, nessun apostrofo al posto dell'accento)", not bad, bad)
nonlat = [v['idx'] for v in cov for c in v['italian'] if ord(c) > 127 and not 0x00C0 <= ord(c) <= 0x024F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio',
   not [v['idx'] for v in cov if v['italian'] != v['italian'].rstrip() or '  ' in v['italian']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("55 unita' prima della 435: L247 (16) + L248 (20) + L249 (19)",
   db.execute('select count(*) from units where path=? and line<435', (PATH,)).fetchone()[0] == 55)
ck("12 unita' dopo la 678: il lotto NON chiude il file",
   db.execute('select count(*) from units where path=? and line>678', (PATH,)).fetchone()[0] == 12)
ck('confine misurato: riga 701, mission:Megaparsec Shipment [0]',
   db.execute('select line,context from units where path=? and line>678 order by line limit 1', (PATH,)).fetchone()
   == (701, 'mission:Megaparsec Shipment [0]'))
ck('il file intero: 94 unita, righe 19 - 814',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (94, 19, 814))
st = dict(db.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('le 27 unita sono PENDING (misurato)',
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
