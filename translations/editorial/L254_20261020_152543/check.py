r"""check.py — L254 (`data/wanderer/wanderer jobs.txt`, 41 unita', righe 458-888). Terzo lotto del file.

**Il lotto piu' denso di nomi**: **18 `VALUE`** (nomi di lavoro, copiati) + **18 `DESCRIPTION`** + **4 `DIALOG`** +
**1 `TEXT`**. Il `TEXT` e' un blocco `phrase:` (`wanderer cargo delivery payment`): e' prosa, quindi si **traduce**, e il
controllo lo verifica separatamente dagli altri tipi.

**17 stringhe distinte** e **6 gruppi** di inglese identico con molteplicita' **8, 8, 4, 4, 3, 3**: le schede generiche
(`Deliver <cargo> to <destination>…`) si ripetono molte volte e devono avere **una sola resa**.

**Due di queste stringhe esistono gia' nel corpus** e la resa e' **calcolata a runtime**: la forma piu' frequente nei
`translation.json` precedenti deve coincidere con quella usata qui (39 e 17 occorrenze).

**83 segnaposto in 9 famiglie**: `<cargo>` e `<destination>` sono **15 e 15**, quindi il confronto e' anche **per ordine**.
**Zero tab, zero virgolette**, **3 apici inglesi** (unita' 29 e 41) contro **1 italiano** (unita' 1, `un'ora`).
"""
import collections
import glob
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
GENERICHE = ('Deliver <cargo> to <destination>. Payment is <payment>.',
             'Deliver <cargo> to <destination> by <date>. Payment is <payment>.')
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
TXT = [v for v in cov if v['kind'] == 'TEXT']
TOK_EN = collections.Counter(t for v in cov for t in TAG.findall(v['english']))
TOK_IT = collections.Counter(t for v in cov for t in TAG.findall(v['italian']))
SEQ = [v['idx'] for v in cov if TAG.findall(v['english']) != TAG.findall(v['italian'])]
A_EN = [(v['idx'], v['english'].count(APOS)) for v in cov if APOS in v['english']]
A_IT = [(v['idx'], v['italian'].count(APOS)) for v in cov if APOS in v['italian']]
prosa = ' '.join(v['italian'] for v in PROSA)
mult = collections.Counter(v['english'] for v in cov)
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


def corpus(english):
    c = collections.Counter()
    for f in glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json')):
        if os.path.basename(os.path.dirname(f)) == os.path.basename(HERE):
            continue
        for u in json.load(open(f, encoding='utf-8'))['units']:
            if u['english'] == english:
                c[u['italian']] += 1
    return c


ck("unita' tradotte 41/41", len(cov) == 41 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna unita\' vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 18 VALUE + 18 DESCRIPTION + 4 DIALOG + 1 TEXT',
   dict(KINDS) == {'VALUE': 18, 'DESCRIPTION': 18, 'DIALOG': 4, 'TEXT': 1}, dict(KINDS))
ck('20 contesti distinti', len(set(u['context'] for u in units)) == 20,
   sorted(set(u['context'] for u in units)))
ck('righe 458 e 888 (prima e ultima del lotto)',
   (cov[0]['line'], cov[-1]['line']) == (458, 888), (cov[0]['line'], cov[-1]['line']))
ck("i 18 VALUE sono IDENTICI all'inglese (6 distinti)",
   len(VAL) == 18 and all(v['italian'] == v['english'] for v in VAL)
   and len({v['english'] for v in VAL}) == 6,
   [v['idx'] for v in VAL if v['italian'] != v['english']])
ck("le 22 unita' di prosa (DESCRIPTION + DIALOG) sono TUTTE tradotte",
   all(v['italian'] != v['english'] for v in PROSA) and len(PROSA) == 22)
ck('il TEXT (blocco `phrase`, unita\' 3) e\' TRADOTTO, non copiato',
   len(TXT) == 1 and TXT[0]['italian'] != TXT[0]['english']
   and TXT[0]['italian'].startswith('Scarichi il tuo carico di'))
ck('17 stringhe distinte e 6 gruppi con molteplicita\' 8, 8, 4, 4, 3, 3',
   len(mult) == 17
   and sorted(n for e, n in mult.items() if n > 1) == [3, 3, 4, 4, 8, 8]
   and all(len({v['italian'] for v in cov if v['english'] == e}) == 1 for e, n in mult.items() if n > 1),
   (len(mult), sorted(n for e, n in mult.items() if n > 1)))
ck('COERENZA CROSS-LOT: le 8 schede generiche usano la resa DOMINANTE del corpus (39 occorrenze)',
   len({v['italian'] for v in cov if v['english'] == GENERICHE[0]}) == 1
   and corpus(GENERICHE[0]).most_common(1)[0][0] == [v['italian'] for v in cov if v['english'] == GENERICHE[0]][0]
   and sum(corpus(GENERICHE[0]).values()) >= 39,
   corpus(GENERICHE[0]).most_common(2))
ck('COERENZA CROSS-LOT: le 4 schede «rush» usano la resa dominante (17 occorrenze)',
   corpus(GENERICHE[1]).most_common(1)[0][0] == [v['italian'] for v in cov if v['english'] == GENERICHE[1]][0]
   and sum(corpus(GENERICHE[1]).values()) >= 17,
   corpus(GENERICHE[1]).most_common(2))
ck('83 segnaposto in 9 famiglie, multiset identico',
   TOK_EN == TOK_IT and sum(TOK_EN.values()) == 83 and len(TOK_EN) == 9,
   (dict(TOK_EN), sum(TOK_EN.values())))
ck("`<cargo>` e `<destination>` sono 15 e 15: il confronto per ordine e' necessario",
   TOK_EN['<cargo>'] == TOK_EN['<destination>'] == 15)
ck("l'ORDINE dei segnaposto e' identico dentro ogni unita'", not SEQ, SEQ)
ck('ZERO tab (asserzione negativa scritta)',
   sum(v['english'].count(TAB) for v in cov) == 0 == sum(v['italian'].count(TAB) for v in cov))
ck('ZERO virgolette (asserzione negativa scritta)',
   sum(v['english'].count(QUOTE) for v in cov) == 0 == sum(v['italian'].count(QUOTE) for v in cov))
ck("apici: 3 in inglese (29: 1, 41: 2) e 1 in italiano (unita' 1, `un'ora`)",
   A_EN == [(29, 1), (41, 2)] and A_IT == [(1, 1)], (A_EN, A_IT))
# `Unfettered` resta **solo** nel `VALUE` copiato (`Captured Unfettered to <planet>`): nella prosa e' «Slegati».
ck('lessico: «Slegati» nella prosa (il `VALUE` copiato conserva `Unfettered`), «governatore», «Kor Efreti», «Korath», «stiva»',
   all(t in prosa for t in ('Slegati', 'governatore', 'Kor Efreti', 'Korath', 'stiva'))
   and 'Unfettered' not in prosa
   and 'Unfettered' in ' '.join(v['italian'] for v in VAL))
ck('`Wanderer` invariato al plurale (`Wanderers` non compare)',
   prosa.count('Wanderer') >= 6 and 'Wanderers' not in prosa)
ck('nessun residuo inglese di struttura (the, and, with, their, these, any)',
   not [w for w in (' the ', ' and ', ' with ', ' their ', ' these ', ' any ') if w in prosa.lower()],
   [w for w in (' the ', ' and ', ' with ', ' their ', ' these ', ' any ') if w in prosa.lower()])
ck('registro: nessun «Lei» e nessuna cortesia',
   not re.search(r'\bLei\b|\bSuo\b|\bSua\b|mi scusi', prosa))
ck('nessun caporale e nessun carattere tipografico',
   not [v['idx'] for v in cov if any(c in v['italian'] for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026')])
rs = [v['ratio'] for v in cov]
ck('rapporto nel gate 0,55-1,90 (0,94-1,17; 426 -> 434 parole)',
   0.55 < min(rs) and max(rs) < 1.90, '%.2f - %.2f' % (min(rs), max(rs)))
ACC = re.compile(r"\b(e|piu|perche|cosi|gia|puo|cioe|percio)'(?![a-z])", re.I)
bad = [(v['idx'], ACC.search(v['italian']).group(0)) for v in cov if ACC.search(v['italian'])]
ck("tipografia (accenti veri, nessun apostrofo al posto dell'accento)", not bad, bad)
nonlat = [v['idx'] for v in cov for c in v['italian'] if ord(c) > 127 and not 0x00C0 <= ord(c) <= 0x024F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio',
   not [v['idx'] for v in cov if v['italian'] != v['italian'].rstrip() or '  ' in v['italian']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("50 unita' prima della 458: L252 (26) + L253 (24)",
   db.execute('select count(*) from units where path=? and line<458', (PATH,)).fetchone()[0] == 50)
ck("1 unita' dopo la 888: il lotto NON chiude il file, ne resta una",
   db.execute('select count(*) from units where path=? and line>888', (PATH,)).fetchone()[0] == 1)
ck('confine misurato: riga 891, mission:Wanderers to Kor Efreti (STESSO contesto)',
   db.execute('select line,context from units where path=? and line>888 order by line limit 1', (PATH,)).fetchone()
   == (891, 'mission:Wanderers to Kor Efreti'))
ck('il file intero: 92 unita, righe 15 - 891',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (92, 15, 891))
st = dict(db.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('le 41 unita sono PENDING (misurato)',
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
