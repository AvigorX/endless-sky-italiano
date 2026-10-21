r"""check.py — L249 (`data/human/syndicate jobs.txt`, 19 unita', righe 291-431). Terzo lotto del file.

**Nove unita' sono una RIPETIZIONE di L248** (la missione `Syndicate target practice` in `[3]`, e in `[2]` la coda che L248
aveva lasciato aperta). Il controllo piu' importante di questo lotto e' quindi **cross-lot**: per ogni stringa inglese che
compare in L248, la resa qui deve essere **identica**, carattere per carattere. Una variante «migliorata» diventa rossa.

**4 `VALUE`** (nomi di lavoro, copiati) + **11 `DIALOG`** + **4 `DESCRIPTION`**. **4 gruppi interni** di inglese identico
(le quattro battute ripetute in `[2]` e `[3]`), una sola resa ciascuno.

**22 segnaposto in 5 famiglie** (`<payment>` 11, `<planet>` 6, `<system>` 3, `<cargo>` 1, `<bunks>` 1), per famiglia **e**
per ordine dentro ogni unita'. **Zero tab**, **2 virgolette** (unita' 12: «"arresti domiciliari"»), **2 apici inglesi**
(`You'll`, unita' 2 e 8) e **0 italiani**: la resa italiana di `You'll` e' «Dovrai», senza apostrofo.
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
PREV = os.path.join(L10N, 'staging', 'editorial', 'L248_20261020_145616', 'translation.json')
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
prev = {u['english']: u['italian'] for u in json.load(open(PREV, encoding='utf-8'))['units']}
riuso = [v for v in cov if v['english'] in prev]
diversi = [(v['idx'], v['italian'], prev[v['english']]) for v in riuso if v['italian'] != prev[v['english']]]
groupi = collections.Counter(v['english'] for v in cov)
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 19/19", len(cov) == 19 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna unita\' vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 4 VALUE + 11 DIALOG + 4 DESCRIPTION',
   dict(KINDS) == {'VALUE': 4, 'DIALOG': 11, 'DESCRIPTION': 4}, dict(KINDS))
ck("5 contesti: target practice [2] e [3], Prisoner Transport [0], [1], [2]",
   dict(ctx) == {'mission:Syndicate target practice [2]': 4, 'mission:Syndicate target practice [3]': 6,
                 'mission:Syndicate Prisoner Transport [0]': 3,
                 'mission:Syndicate Prisoner Transport [1]': 3,
                 'mission:Syndicate Prisoner Transport [2]': 3}, dict(ctx))
ck('righe 291 e 431 (prima e ultima del lotto)',
   (cov[0]['line'], cov[-1]['line']) == (291, 431), (cov[0]['line'], cov[-1]['line']))
ck('COERENZA CROSS-LOT: le 10 unita\' che ripetono l\'inglese di L248 hanno la STESSA resa',
   len(riuso) == 10 and not diversi, (len(riuso), diversi[:1]))
ck("i 4 VALUE sono IDENTICI all'inglese (nomi di lavoro)",
   len(VAL) == 4 and all(v['italian'] == v['english'] for v in VAL),
   [v['idx'] for v in VAL if v['italian'] != v['english']])
ck("le 15 unita' di prosa sono TUTTE tradotte (0 identiche)",
   all(v['italian'] != v['english'] for v in PROSA) and len(PROSA) == 15)
ck('4 gruppi interni di inglese identico, ognuno con una sola resa',
   sum(1 for e, n in groupi.items() if n > 1) == 4
   and all(len({v['italian'] for v in cov if v['english'] == e}) == 1 for e, n in groupi.items() if n > 1)
   and max(groupi.values()) == 2, [(e[:28], n) for e, n in groupi.items() if n > 1])
ck('22 segnaposto in 5 famiglie, multiset identico',
   TOK_EN == TOK_IT and sum(TOK_EN.values()) == 22 and len(TOK_EN) == 5,
   (dict(TOK_EN), sum(TOK_EN.values())))
ck("l'ORDINE dei segnaposto e' identico dentro ogni unita'", not SEQ, SEQ)
ck('ZERO tab (asserzione negativa scritta)',
   sum(v['english'].count(TAB) for v in cov) == 0 == sum(v['italian'].count(TAB) for v in cov))
ck('2 virgolette nella sola unita\' 12: «"arresti domiciliari"»',
   Q_IT == [(12, 2)] and '"arresti domiciliari"' in cov[11]['italian'], Q_IT)
ck("apici: 2 in inglese (unita' 2 e 8, `You'll`) e ZERO in italiano (`You'll` -> «Dovrai»)",
   A_EN == [(2, 1), (8, 1)] and A_IT == [], (A_EN, A_IT))
ck("nessun possessivo inglese sopravvissuto ('s o s')",
   not [v['idx'] for v in cov if "'s " in v['italian'] or "s' " in v['italian']])
ck('lessico: «arresti domiciliari», «colletti bianchi», «sabotatore», «spie aziendali», «incatenati»',
   all(t in prosa for t in ('arresti domiciliari', 'colletti bianchi', 'sabotatore', 'spie aziendali',
                            'incatenati'))
   and not re.search(r'\bSyndicate\b', prosa))
ck('«Ricevi il pagamento di <payment>.» nelle 2 unita\' attese (16, 19)',
   [v['idx'] for v in PROSA if 'Ricevi il pagamento di <payment>.' in v['italian']] == [16, 19])
# 6 e' la scheda ripresa da L248 (che contiene gia' la formula): le altre tre sono le schede nuove.
ck("«Il pagamento è <payment>.» nelle 3 schede nuove (12, 15, 18) piu' quella ripresa da L248 (6)",
   [v['idx'] for v in PROSA if 'Il pagamento è <payment>.' in v['italian']] == [6, 12, 15, 18])
ck('`<bunks>` con l\'accordo al femminile plurale («spie … condannate … tenute»)',
   'spie aziendali condannate' in prosa and 'tenute in strutture' in prosa)
ck('nessun residuo inglese di struttura (the, and, with, that, from, your)',
   not [w for w in (' the ', ' and ', ' with ', ' that ', ' from ', ' your ') if w in prosa.lower()],
   [w for w in (' the ', ' and ', ' with ', ' that ', ' from ', ' your ') if w in prosa.lower()])
ck('registro: nessun «Lei» e nessuna cortesia',
   not re.search(r'\bLei\b|\bSuo\b|\bSua\b|mi scusi', prosa))
ck('nessun caporale e nessun carattere tipografico',
   not [v['idx'] for v in cov if any(c in v['italian'] for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026')])
rs = [v['ratio'] for v in cov]
ck('rapporto nel gate 0,55-1,90 (0,93-1,18; 438 -> 419 parole)',
   0.55 < min(rs) and max(rs) < 1.90, '%.2f - %.2f' % (min(rs), max(rs)))
ACC = re.compile(r"\b(e|piu|perche|cosi|gia|puo|cioe|percio)'(?![a-z])", re.I)
bad = [(v['idx'], ACC.search(v['italian']).group(0)) for v in cov if ACC.search(v['italian'])]
ck("tipografia (accenti veri, nessun apostrofo al posto dell'accento)", not bad, bad)
nonlat = [v['idx'] for v in cov for c in v['italian'] if ord(c) > 127 and not 0x00C0 <= ord(c) <= 0x024F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio',
   not [v['idx'] for v in cov if v['italian'] != v['italian'].rstrip() or '  ' in v['italian']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("36 unita' prima della 291: L247 (16) + L248 (20)",
   db.execute('select count(*) from units where path=? and line<291', (PATH,)).fetchone()[0] == 36)
ck("39 unita' dopo la 431: il lotto NON chiude il file",
   db.execute('select count(*) from units where path=? and line>431', (PATH,)).fetchone()[0] == 39)
ck("confine misurato: riga 435, mission:Syndicate Prisoner Transport [3] (STESSO contesto, parentesi quadre)",
   db.execute('select line,context from units where path=? and line>431 order by line limit 1', (PATH,)).fetchone()
   == (435, 'mission:Syndicate Prisoner Transport [3]')
   and cov[-1]['context'] == 'mission:Syndicate Prisoner Transport [2]')
ck('il file intero: 94 unita, righe 19 - 814',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (94, 19, 814))
st = dict(db.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('le 19 unita sono PENDING (misurato)',
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
