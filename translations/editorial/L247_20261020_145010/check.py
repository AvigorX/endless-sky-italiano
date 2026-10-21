r"""check.py — L247 (`data/human/syndicate jobs.txt`, 16 unita', righe 19-153). **Primo lotto del file.**

**Primo lotto con `DIALOG`**: 9 battute oltre a 6 `DESCRIPTION` (schede del lavoro) e **1 `VALUE`** (il nome del lavoro,
copiato). Le 16 unita' contengono **3 coppie di inglese identico** (3/7, 4/8, 5/9): una sola resa per coppia.

**39 segnaposto in 11 famiglie** (`<payment>` 12, `<origin>` 5, `<destination>` 4, `<date>` 4, `<planet>` 3, `<bunks>` 2,
`<stopovers>` 2, `<npc>` 2, `<tons>` 2, `<commodity>` 2, `<planet stopovers>` 1). Si confrontano per **famiglia** e per
**ordine dentro ogni unita'**: `<planet stopovers>` e' un simbolo **intero** con uno spazio dentro e non va spezzato.

**0 tab, 2 virgolette** (unica unita' 12, una citazione), **6 apici inglesi** su 6 unita' contro **5 italiani** su 4:
i possessivi inglesi (`You're`, `team's`, `<npc>'s`) non si replicano, le elisioni italiane (`un po'`, `nell'ambito`,
`dall'odore`) compaiono dove l'inglese non ne aveva.

Le rese fisse del corpus sono rispettate: «Il pagamento è `<payment>`.» (56 occorrenze), «Incassi il pagamento di
`<payment>`.», `<tons>` **senza articolo**.
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
SEQ = all([TAG.findall(v['english'])] == [TAG.findall(v['italian'])] for v in cov)
A_EN = [(v['idx'], v['english'].count(APOS)) for v in cov if APOS in v['english']]
A_IT = [(v['idx'], v['italian'].count(APOS)) for v in cov if APOS in v['italian']]
Q_IT = [(v['idx'], v['italian'].count(QUOTE)) for v in cov if QUOTE in v['italian']]
prosa = ' '.join(v['italian'] for v in PROSA)
ctx = collections.Counter(u['context'] for u in units)
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 16/16", len(cov) == 16 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna unita\' vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 1 VALUE + 9 DIALOG + 6 DESCRIPTION',
   dict(KINDS) == {'VALUE': 1, 'DIALOG': 9, 'DESCRIPTION': 6}, dict(KINDS))
ck('6 contesti distinti', len(ctx) == 6, dict(ctx))
ck('righe 19 e 153 (prima e ultima del lotto)',
   (cov[0]['line'], cov[-1]['line']) == (19, 153), (cov[0]['line'], cov[-1]['line']))
ck("il VALUE e' IDENTICO all'inglese (nome del lavoro: si copia)",
   len(VAL) == 1 and VAL[0]['italian'] == VAL[0]['english'] == 'Corporate retreat to <planet stopovers>')
ck("le 15 unita' di prosa sono TUTTE tradotte (0 identiche)",
   all(v['italian'] != v['english'] for v in PROSA) and len(PROSA) == 15)
ck('le 3 coppie di inglese identico (3/7, 4/8, 5/9) hanno UNA sola resa',
   all({v['italian'] for v in cov if v['english'] == e} ==
       {next(v['italian'] for v in cov if v['idx'] == primo)}
       for e, primo in [(cov[2]['english'], 3), (cov[3]['english'], 4), (cov[4]['english'], 5)])
   and sum(1 for e, n in collections.Counter(v['english'] for v in cov).items() if n > 1) == 3)
ck('39 segnaposto in 11 famiglie, identici per famiglia',
   TOK_EN == TOK_IT and sum(TOK_EN.values()) == 39 and len(TOK_EN) == 11, (dict(TOK_EN), sum(TOK_EN.values())))
ck("l'ORDINE dei segnaposto e' identico dentro ogni unita'",
   SEQ, [v['idx'] for v in cov if TAG.findall(v['english']) != TAG.findall(v['italian'])])
ck('`<planet stopovers>` e\' un simbolo intero (uno spazio dentro) e non si spezza',
   TOK_IT.get('<planet stopovers>') == 1 and TOK_IT.get('<stopovers>') == 2
   and '<planet stopovers>' not in ' '.join(t for t in TOK_IT if t != '<planet stopovers>'))
# `<tons>` e' una quantita' del motore: nessun articolo davanti e, nel corpus, sempre seguita da «di».
ck('`<tons>` senza articolo e sempre seguito da «di»',
   not re.search(r'\b(il|lo|la|i|gli|le|un|uno|una|dei|delle)\s+<tons>', prosa)
   and set(re.findall(r'<tons>\s+(\w+)', prosa)) == {'di'},
   re.findall(r'.{10}<tons>\s+\w+', prosa))
ck('residuo fisso del corpus: «Il pagamento è <payment>.» (5 unita\': 1, 3, 7, 13, 15)',
   [v['idx'] for v in PROSA if 'Il pagamento è <payment>.' in v['italian']] == [1, 3, 7, 13, 15])
ck('«Incassi il pagamento di <payment>.» (2 unita\': 2 e 14)',
   [v['idx'] for v in PROSA if 'Incassi il pagamento di <payment>.' in v['italian']] == [2, 14])
ck('ZERO tab (asserzione negativa scritta)',
   sum(v['english'].count(TAB) for v in cov) == 0 == sum(v['italian'].count(TAB) for v in cov))
ck('2 virgolette, entrambe nella unita\' 12 (una citazione)',
   Q_IT == [(12, 2)] and '"Ci farà risparmiare mesi!"' in cov[11]['italian'], Q_IT)
ck("apici: 6 in inglese (possessivi, unita' 4, 5, 8, 9, 11, 14) e 5 in italiano (4, 8, 15, 16)",
   A_EN == [(4, 1), (5, 1), (8, 1), (9, 1), (11, 1), (14, 1)] and A_IT == [(4, 1), (8, 1), (15, 1), (16, 2)],
   (A_EN, A_IT))
ck("nessun possessivo inglese sopravvissuto ('s o s')",
   not [v['idx'] for v in cov if "'s " in v['italian'] or "s' " in v['italian']])
# `Syndicate` non compare mai come fazione (resa «Sindacato»), ma `Syndicated Systems` e' un nome proprio e resta.
ck('nomi propri invariati: `Syndicated Systems` e `Iniziativa Verde` presenti, `Syndicate` reso «Sindacato»',
   'Sindacato' in prosa and 'Syndicated Systems' in prosa and 'Iniziativa Verde' in prosa
   and not re.search(r'\bSyndicate\b', prosa), re.findall(r'\bSyndicate\w*', prosa))
ck('nessun residuo inglese di struttura (the, and, with, that, from, your)',
   not [w for w in (' the ', ' and ', ' with ', ' that ', ' from ', ' your ') if w in prosa.lower()],
   [w for w in (' the ', ' and ', ' with ', ' that ', ' from ', ' your ') if w in prosa.lower()])
ck('registro: nessun «Lei» e nessuna cortesia',
   not re.search(r'\bLei\b|\bSuo\b|\bSua\b|mi scusi', prosa))
ck('nessun caporale e nessun carattere tipografico',
   not [v['idx'] for v in cov if any(c in v['italian'] for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026')])
rs = [v['ratio'] for v in cov]
ck('rapporto nel gate 0,55-1,90 (0,97-1,23; 488 -> 510 parole)',
   0.55 < min(rs) and max(rs) < 1.90, '%.2f - %.2f' % (min(rs), max(rs)))
ACC = re.compile(r"\b(e|piu|perche|cosi|gia|puo|cioe|percio)'(?![a-z])", re.I)
bad = [(v['idx'], ACC.search(v['italian']).group(0)) for v in cov if ACC.search(v['italian'])]
ck("tipografia (accenti veri, nessun apostrofo al posto dell'accento)", not bad, bad)
nonlat = [v['idx'] for v in cov for c in v['italian'] if ord(c) > 127 and not 0x00C0 <= ord(c) <= 0x024F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio',
   not [v['idx'] for v in cov if v['italian'] != v['italian'].rstrip() or '  ' in v['italian']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("ZERO unita' prima della riga 19: il lotto APRE il file",
   db.execute('select count(*) from units where path=? and line<19', (PATH,)).fetchone()[0] == 0)
ck("78 unita' dopo la 153 (94 - 16): il lotto NON chiude il file",
   db.execute('select count(*) from units where path=? and line>153', (PATH,)).fetchone()[0] == 78)
ck('confine misurato: riga 157, mission:Rush fuel Delivery',
   db.execute('select line,context from units where path=? and line>153 order by line limit 1', (PATH,)).fetchone()
   == (157, 'mission:Rush fuel Delivery'))
ck('il file intero: 94 unita, righe 19 - 814',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (94, 19, 814))
st = dict(db.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('le 16 unita sono PENDING (misurato)',
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
