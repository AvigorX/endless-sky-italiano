r"""check.py — L248 (`data/human/syndicate jobs.txt`, 20 unita', righe 157-275). Secondo lotto del file.

**Cinque `VALUE`** (tre distinti: `Rush fuel delivery to <planet>`, `Rush equipment delivery to <planet>`, `Syndicate
target practice` ×3): sono nomi di lavoro e si **copiano**.

**Sette gruppi di inglese identico** — la missione «Syndicate target practice» ha **tre contesti** (`[0]`, `[1]`, `[2]`)
con la **stessa** prosa, e la consegna urgente compare in due missioni. Una sola resa per gruppo.

**32 segnaposto in 8 famiglie** (`<payment>` 11, `<planet>` 7, `<system>` 5, `<commodity>` 3, `<destination>` 2, `<date>`
2, `<cargo>` 1, `<tons>` 1), confrontati per **famiglia** e per **ordine dentro ogni unita'**.

**Zero tab e zero virgolette**: due asserzioni negative scritte. **2 apici inglesi** (unita' 10 e 16, `You'll`) contro
**1 italiano** (unita' 2, `d'emergenza`).

`<commodity>` non prende aggettivi concordati: la resa usa «per uso specialistico», che non concorda col nome inserito dal
motore (stessa cautela di L242 con `<tons>`).
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
prosa = ' '.join(v['italian'] for v in PROSA)
ctx = collections.Counter(u['context'] for u in units)
groupi = collections.Counter(v['english'] for v in cov)
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 20/20", len(cov) == 20 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna unita\' vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 5 VALUE + 10 DIALOG + 5 DESCRIPTION',
   dict(KINDS) == {'VALUE': 5, 'DIALOG': 10, 'DESCRIPTION': 5}, dict(KINDS))
ck("5 contesti, con le parentesi quadre nei nomi: …practice [0], [1], [2]",
   dict(ctx) == {'mission:Rush fuel Delivery': 3, 'mission:Rush equipment Delivery': 3,
                 'mission:Syndicate target practice [0]': 6,
                 'mission:Syndicate target practice [1]': 6,
                 'mission:Syndicate target practice [2]': 2}, dict(ctx))
ck('righe 157 e 275 (prima e ultima del lotto)',
   (cov[0]['line'], cov[-1]['line']) == (157, 275), (cov[0]['line'], cov[-1]['line']))
ck("i 5 VALUE sono IDENTICI all'inglese, per indice (3 distinti)",
   len(VAL) == 5 and all(v['italian'] == v['english'] for v in VAL)
   and len({v['english'] for v in VAL}) == 3, [v['idx'] for v in VAL if v['italian'] != v['english']])
ck("le 15 unita' di prosa sono TUTTE tradotte (0 identiche)",
   all(v['italian'] != v['english'] for v in PROSA) and len(PROSA) == 15)
ck('7 gruppi di inglese identico, OGNUNO con una sola resa',
   sum(1 for e, n in groupi.items() if n > 1) == 7
   and all(len({v['italian'] for v in cov if v['english'] == e}) == 1 for e, n in groupi.items() if n > 1),
   [(e[:30], n) for e, n in groupi.items() if n > 1])
ck('32 segnaposto in 8 famiglie, multiset identico',
   TOK_EN == TOK_IT and sum(TOK_EN.values()) == 32 and len(TOK_EN) == 8,
   (dict(TOK_EN), sum(TOK_EN.values())))
ck("l'ORDINE dei segnaposto e' identico dentro ogni unita'", not SEQ, SEQ)
ck('ZERO tab (asserzione negativa scritta)',
   sum(v['english'].count(TAB) for v in cov) == 0 == sum(v['italian'].count(TAB) for v in cov))
ck('ZERO virgolette (asserzione negativa scritta)',
   sum(v['english'].count(QUOTE) for v in cov) == 0 == sum(v['italian'].count(QUOTE) for v in cov))
ck("apici: 2 in inglese (unita' 10 e 16, `You'll`) e 1 in italiano (unita' 2, `d'emergenza`)",
   A_EN == [(10, 1), (16, 1)] and A_IT == [(2, 1)], (A_EN, A_IT))
ck("nessun possessivo inglese sopravvissuto",
   not [v['idx'] for v in cov if "'s " in v['italian'] or "s' " in v['italian']])
ck('residuo fisso del corpus: «Il pagamento è <payment>.» nelle 5 unita\' attese (2, 5, 8, 14, 20)',
   [v['idx'] for v in PROSA if 'Il pagamento è <payment>.' in v['italian']] == [2, 5, 8, 14, 20])
ck('«Incassi il pagamento di <payment>.» nelle 4 unita\' attese (3, 6, 12, 18)',
   [v['idx'] for v in PROSA if 'incassi il pagamento di <payment>.' in v['italian']] == [3, 6, 12, 18])
ck('«Scarichi il tuo carico di <commodity>» (consegna urgente, 2 unita\')',
   sum(1 for v in PROSA if 'Scarichi il tuo carico di <commodity>' in v['italian']) == 2)
ck('`<tons>` senza articolo e seguito da «di»',
   not re.search(r'\b(il|lo|la|i|gli|le|un|uno|una)\s+<tons>', prosa)
   and set(re.findall(r'<tons>\s+(\w+)', prosa)) == {'di'},
   re.findall(r'.{12}<tons>\s+\w+', prosa))
# Il nome che il motore inserisce non ha genere noto: dopo `<commodity>` non segue un aggettivo ma una preposizione
# articolata o semplice. Le tre forme sono misurate e asserite una per una.
ck("`<commodity>` non prende aggettivi concordati (segue «alla» o «per», mai un aggettivo)",
   'per uso specialistico' in prosa
   and re.findall(r'<commodity>\s+(\w+)', prosa) == ['alla', 'per', 'alla'],
   re.findall(r'<commodity>\s+\w+', prosa))
ck('lessico: «Sindacato», «nave-bersaglio», «dati di collaudo», «baia di carico», «simulazione realistica»',
   all(t in prosa for t in ('Sindacato', 'nave-bersaglio', 'dati di collaudo', 'baia di carico',
                            'simulazione realistica'))
   and not re.search(r'\bSyndicate\b', prosa))
ck('nessun residuo inglese di struttura (the, and, with, that, from, your)',
   not [w for w in (' the ', ' and ', ' with ', ' that ', ' from ', ' your ') if w in prosa.lower()],
   [w for w in (' the ', ' and ', ' with ', ' that ', ' from ', ' your ') if w in prosa.lower()])
ck('registro: nessun «Lei» e nessuna cortesia',
   not re.search(r'\bLei\b|\bSuo\b|\bSua\b|mi scusi', prosa))
ck('nessun caporale e nessun carattere tipografico',
   not [v['idx'] for v in cov if any(c in v['italian'] for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026')])
rs = [v['ratio'] for v in cov]
ck('rapporto nel gate 0,55-1,90 (0,93-1,32; 430 -> 422 parole)',
   0.55 < min(rs) and max(rs) < 1.90, '%.2f - %.2f' % (min(rs), max(rs)))
ACC = re.compile(r"\b(e|piu|perche|cosi|gia|puo|cioe|percio)'(?![a-z])", re.I)
bad = [(v['idx'], ACC.search(v['italian']).group(0)) for v in cov if ACC.search(v['italian'])]
ck("tipografia (accenti veri, nessun apostrofo al posto dell'accento)", not bad, bad)
nonlat = [v['idx'] for v in cov for c in v['italian'] if ord(c) > 127 and not 0x00C0 <= ord(c) <= 0x024F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio',
   not [v['idx'] for v in cov if v['italian'] != v['italian'].rstrip() or '  ' in v['italian']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("16 unita' prima della 157: e' L247",
   db.execute('select count(*) from units where path=? and line<157', (PATH,)).fetchone()[0] == 16)
ck("58 unita' dopo la 275: il lotto NON chiude il file",
   db.execute('select count(*) from units where path=? and line>275', (PATH,)).fetchone()[0] == 58)
ck("confine misurato: riga 291, mission:Syndicate target practice [2] (STESSO contesto, parentesi quadre)",
   db.execute('select line,context from units where path=? and line>275 order by line limit 1', (PATH,)).fetchone()
   == (291, 'mission:Syndicate target practice [2]') and cov[-1]['context'] == 'mission:Syndicate target practice [2]')
ck('il file intero: 94 unita, righe 19 - 814',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (94, 19, 814))
st = dict(db.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('le 20 unita sono PENDING (misurato)',
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
