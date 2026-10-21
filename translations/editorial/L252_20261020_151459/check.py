r"""check.py — L252 (`data/wanderer/wanderer jobs.txt`, 26 unita', righe 15-261). **Primo lotto del file.**

**Ogni stringa compare due volte** tranne una: le cinque missioni hanno ciascuna due contesti (`[0]` e `[1]`) con la stessa
prosa, e la battuta degli scienziati compare **quattro** volte (due tipi di missione × due contesti). In tutto **12 gruppi
di inglese identico**: 11 con due copie, 1 con quattro, **una sola resa per gruppo**.

**10 `VALUE`** (5 distinti, nomi di lavoro) + **10 `DESCRIPTION`** + **6 `DIALOG`**.

**58 segnaposto in 6 famiglie** (`<payment>` 16, `<planet>` 14, `<bunks>` 10, `<destination>` 10, `<cargo>` 4, `<date>` 4):
`<bunks>` e `<destination>` hanno **lo stesso conteggio**, quindi il multiset da solo sarebbe cieco a uno scambio — il
confronto e' anche **per ordine**. **Zero tab, zero virgolette**, **zero apici inglesi** contro **4 italiani** (elisioni).
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
PATH = 'data/wanderer/wanderer jobs.txt'
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
prosa = ' '.join(v['italian'] for v in PROSA)
ctx = collections.Counter(u['context'] for u in units)
mult = collections.Counter(v['english'] for v in cov)
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 26/26", len(cov) == 26 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna unita\' vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 10 VALUE + 10 DESCRIPTION + 6 DIALOG',
   dict(KINDS) == {'VALUE': 10, 'DESCRIPTION': 10, 'DIALOG': 6}, dict(KINDS))
# Ogni contesto ha le parentesi quadre del contatore; i due degli scienziati hanno anche le tonde (Phenomenon/Pollution).
ck('10 contesti distinti: quadre in tutti, tonde nei quattro degli scienziati',
   len(ctx) == 10 and all('[' in c for c in ctx)
   and sum(1 for c in ctx if '(' in c) == 4, (len(ctx), sorted(ctx)[:3]))
ck('righe 15 e 261 (prima e ultima del lotto)',
   (cov[0]['line'], cov[-1]['line']) == (15, 261), (cov[0]['line'], cov[-1]['line']))
ck("i 10 VALUE sono IDENTICI all'inglese (5 distinti)",
   len(VAL) == 10 and all(v['italian'] == v['english'] for v in VAL)
   and len({v['english'] for v in VAL}) == 5,
   [v['idx'] for v in VAL if v['italian'] != v['english']])
ck("le 16 unita' di prosa sono TUTTE tradotte (0 identiche)",
   all(v['italian'] != v['english'] for v in PROSA) and len(PROSA) == 16)
ck('12 gruppi di inglese identico: 11 con 2 copie e 1 con 4, una resa ciascuno',
   sum(1 for e, n in mult.items() if n > 1) == 12
   and sorted(n for e, n in mult.items() if n > 1) == [2] * 11 + [4]
   and all(len({v['italian'] for v in cov if v['english'] == e}) == 1 for e, n in mult.items() if n > 1),
   sorted(n for e, n in mult.items() if n > 1))
ck('58 segnaposto in 6 famiglie, multiset identico',
   TOK_EN == TOK_IT and sum(TOK_EN.values()) == 58 and len(TOK_EN) == 6,
   (dict(TOK_EN), sum(TOK_EN.values())))
ck("`<bunks>` e `<destination>` hanno lo stesso conteggio (10): l'ordine li distingue",
   TOK_EN['<bunks>'] == TOK_EN['<destination>'] == 10)
ck("l'ORDINE dei segnaposto e' identico dentro ogni unita'", not SEQ, SEQ)
ck('ZERO tab (asserzione negativa scritta)',
   sum(v['english'].count(TAB) for v in cov) == 0 == sum(v['italian'].count(TAB) for v in cov))
ck('ZERO virgolette (asserzione negativa scritta)',
   sum(v['english'].count(QUOTE) for v in cov) == 0 == sum(v['italian'].count(QUOTE) for v in cov))
ck("apici: ZERO in inglese, 4 in italiano (unita' 10, 11, 13, 14)",
   A_EN == [] and A_IT == [(10, 1), (11, 2), (13, 1), (14, 2)], (A_EN, A_IT))
ck('`Wanderer` resta invariato, al singolare e al plurale',
   prosa.count('Wanderer') >= 8 and 'Wanderers' not in prosa)
ck('«Il pagamento sarà <payment>.» nelle 4 schede degli scienziati (16, 19, 22, 25)',
   [v['idx'] for v in PROSA if 'Il pagamento sarà <payment>.' in v['italian']] == [16, 19, 22, 25])
ck('«ti pagheranno <payment> per portarli fin là» nelle 4 schede di trasporto (2, 4, 6, 8)',
   [v['idx'] for v in PROSA if 'per portarli fin là' in v['italian']] == [2, 4, 6, 8])
ck('«entro il <date>» due volte per famiglia (cargo e data insieme)',
   prosa.count('con il loro <cargo> entro il <date>') == 4)
ck('lessico: «lavoratori», «agricoltori», «piccoli», «scienziati», «inquinanti atmosferici», «fenomeno naturale»',
   all(t in prosa for t in ('lavoratori', 'agricoltori', 'piccoli', 'scienziati',
                            'inquinanti atmosferici', 'fenomeno naturale')))
ck('nessun residuo inglese di struttura (the, and, with, their, these)',
   not [w for w in (' the ', ' and ', ' with ', ' their ', ' these ') if w in prosa.lower()],
   [w for w in (' the ', ' and ', ' with ', ' their ', ' these ') if w in prosa.lower()])
ck('registro: nessun «Lei» e nessuna cortesia',
   not re.search(r'\bLei\b|\bSuo\b|\bSua\b|mi scusi', prosa))
ck('nessun caporale e nessun carattere tipografico',
   not [v['idx'] for v in cov if any(c in v['italian'] for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026')])
rs = [v['ratio'] for v in cov]
ck('rapporto nel gate 0,55-1,90 (0,93-1,12; 430 -> 426 parole)',
   0.55 < min(rs) and max(rs) < 1.90, '%.2f - %.2f' % (min(rs), max(rs)))
ACC = re.compile(r"\b(e|piu|perche|cosi|gia|puo|cioe|percio)'(?![a-z])", re.I)
bad = [(v['idx'], ACC.search(v['italian']).group(0)) for v in cov if ACC.search(v['italian'])]
ck("tipografia (accenti veri, nessun apostrofo al posto dell'accento)", not bad, bad)
nonlat = [v['idx'] for v in cov for c in v['italian'] if ord(c) > 127 and not 0x00C0 <= ord(c) <= 0x024F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio',
   not [v['idx'] for v in cov if v['italian'] != v['italian'].rstrip() or '  ' in v['italian']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("ZERO unita' prima della riga 15: il lotto APRE il file",
   db.execute('select count(*) from units where path=? and line<15', (PATH,)).fetchone()[0] == 0)
ck("66 unita' dopo la 261 (92 - 26): il lotto NON chiude il file",
   db.execute('select count(*) from units where path=? and line>261', (PATH,)).fetchone()[0] == 66)
ck('confine misurato: riga 264, mission:Wanderer Biologists [0]',
   db.execute('select line,context from units where path=? and line>261 order by line limit 1', (PATH,)).fetchone()
   == (264, 'mission:Wanderer Biologists [0]'))
ck('il file intero: 92 unita, righe 15 - 891',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (92, 15, 891))
st = dict(db.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('le 26 unita sono PENDING (misurato)',
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
