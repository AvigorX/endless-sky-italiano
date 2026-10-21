r"""check.py — L251 (`data/human/syndicate jobs.txt`, 12 unita', righe 701-814). **LOTTO TERMINALE**: chiude il file.

**Invariante di FILE**: dopo questo lotto `syndicate jobs.txt` deve avere **94 unita' distinte su 94**
(`16 + 20 + 19 + 27 + 12`), la riga **814** come ultima e **0** unita' dopo.

**5 `VALUE`** (due distinti: `Shipment to <planet>` ×3, `Transport racer to <planet>`, `Transport team to <planet>`),
**5 `DESCRIPTION`** e **2 `DIALOG`**. Due gruppi di inglese identico (tre copie ciascuno: le spedizioni Megaparsec e il loro
`VALUE`), una resa per gruppo.

**24 segnaposto in 6 famiglie** (`<payment>` 7, `<planet>` 5, `<destination>` 5, `<cargo>` 4, `<date>` 2, `<passengers>` 1),
per famiglia **e** per ordine dentro ogni unita'. **Zero tab, zero virgolette, zero apici** in entrambe le lingue: tre
asserzioni negative scritte.
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
mult = collections.Counter(v['english'] for v in cov)
prosa = ' '.join(v['italian'] for v in PROSA)
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 12/12", len(cov) == 12 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna unita\' vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 5 VALUE + 5 DESCRIPTION + 2 DIALOG',
   dict(KINDS) == {'VALUE': 5, 'DESCRIPTION': 5, 'DIALOG': 2}, dict(KINDS))
ck('5 contesti: Megaparsec [0], [1], [2] + i due trasporti di hovercraft',
   set(u['context'] for u in units) == {
       'mission:Megaparsec Shipment [0]', 'mission:Megaparsec Shipment [1]',
       'mission:Megaparsec Shipment [2]', 'mission:Syndicate Hovercraft Racer Transport',
       'mission:Syndicate Hovercraft Large Racer Transport'}, sorted(set(u['context'] for u in units)))
ck('righe 701 e 814 (prima e ultima del lotto)',
   (cov[0]['line'], cov[-1]['line']) == (701, 814), (cov[0]['line'], cov[-1]['line']))
ck("i 5 VALUE sono IDENTICI all'inglese (3 distinti)",
   len(VAL) == 5 and all(v['italian'] == v['english'] for v in VAL)
   and len({v['english'] for v in VAL}) == 3,
   [v['idx'] for v in VAL if v['italian'] != v['english']])
ck("le 7 unita' di prosa sono TUTTE tradotte (0 identiche)",
   all(v['italian'] != v['english'] for v in PROSA) and len(PROSA) == 7)
ck('2 gruppi di inglese identico, 3 copie ciascuno, una resa per gruppo',
   sum(1 for e, n in mult.items() if n > 1) == 2 and max(mult.values()) == 3
   and all(len({v['italian'] for v in cov if v['english'] == e}) == 1 for e, n in mult.items() if n > 1),
   [(e[:40], n) for e, n in mult.items() if n > 1])
ck('24 segnaposto in 6 famiglie, multiset identico',
   TOK_EN == TOK_IT and sum(TOK_EN.values()) == 24 and len(TOK_EN) == 6,
   (dict(TOK_EN), sum(TOK_EN.values())))
ck("l'ORDINE dei segnaposto e' identico dentro ogni unita'", not SEQ, SEQ)
ck('ZERO tab in entrambe le lingue (asserzione negativa scritta)',
   sum(v['english'].count(TAB) for v in cov) == 0 == sum(v['italian'].count(TAB) for v in cov))
ck('ZERO virgolette in entrambe le lingue (asserzione negativa scritta)',
   sum(v['english'].count(QUOTE) for v in cov) == 0 == sum(v['italian'].count(QUOTE) for v in cov))
ck('ZERO apici in entrambe le lingue (asserzione negativa scritta)',
   sum(v['english'].count(APOS) for v in cov) == 0 == sum(v['italian'].count(APOS) for v in cov))
ck('«Il pagamento è <payment>.» nelle 3 schede Megaparsec',
   [v['idx'] for v in PROSA if 'Il pagamento è <payment>.' in v['italian']] == [2, 4, 6])
ck('`incassi il pagamento di <payment>` nelle 2 battute (9, 12)',
   [v['idx'] for v in PROSA if 'incassi il pagamento di <payment>' in v['italian']] == [9, 12])
ck('«entro il <date>» e «in cambio di <payment>» nelle due schede dei trasporti',
   'entro il <date> in cambio di <payment>' in prosa
   and sum(1 for v in PROSA if 'entro il <date> in cambio di <payment>' in v['italian']) == 2)
ck('`Megaparsec Inc.` invariato (3 volte), `hovercraft` invariato (3 volte, singolare e plurale)',
   prosa.count('Megaparsec Inc.') == 3 and prosa.count('hovercraft') == 3
   and 'i suoi hovercraft' in prosa)
ck('nessun residuo inglese di struttura (the, and, with, that, their, this)',
   not [w for w in (' the ', ' and ', ' with ', ' that ', ' their ', ' this ') if w in prosa.lower()],
   [w for w in (' the ', ' and ', ' with ', ' that ', ' their ', ' this ') if w in prosa.lower()])
ck('registro: nessun «Lei» e nessuna cortesia',
   not re.search(r'\bLei\b|\bSuo\b|\bSua\b|mi scusi', prosa))
ck('nessun caporale e nessun carattere tipografico',
   not [v['idx'] for v in cov if any(c in v['italian'] for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026')])
rs = [v['ratio'] for v in cov]
ck('rapporto nel gate 0,55-1,90 (0,88-1,28; 139 -> 150 parole)',
   0.55 < min(rs) and max(rs) < 1.90, '%.2f - %.2f' % (min(rs), max(rs)))
ACC = re.compile(r"\b(e|piu|perche|cosi|gia|puo|cioe|percio)'(?![a-z])", re.I)
bad = [(v['idx'], ACC.search(v['italian']).group(0)) for v in cov if ACC.search(v['italian'])]
ck("tipografia (accenti veri, nessun apostrofo al posto dell'accento)", not bad, bad)
nonlat = [v['idx'] for v in cov for c in v['italian'] if ord(c) > 127 and not 0x00C0 <= ord(c) <= 0x024F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio',
   not [v['idx'] for v in cov if v['italian'] != v['italian'].rstrip() or '  ' in v['italian']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("82 unita' prima della 701 (16 + 20 + 19 + 27)",
   db.execute('select count(*) from units where path=? and line<701', (PATH,)).fetchone()[0] == 82)
ck("ZERO unita' dopo la 814: il lotto CHIUDE il file",
   db.execute('select count(*) from units where path=? and line>814', (PATH,)).fetchone()[0] == 0)
ck('il file intero: 94 unita, righe 19 - 814',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (94, 19, 814))
ck("INVARIANTE DI FILE: 16 + 20 + 19 + 27 + 12 = 94", 16 + 20 + 19 + 27 + 12 == 94 == len(units) + 82)
st = dict(db.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('le 12 unita sono PENDING (misurato)',
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
