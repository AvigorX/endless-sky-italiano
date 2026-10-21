r"""check.py — L217 (`data/human/deep jobs.txt`, 29 unita', righe 935-1234). **Lotto terminale del file.**

Porta `deep jobs.txt` a **186/187 tradotte + 1 `UI_LABEL`**: le sei finestre (L212 45, L213 22, L214 35, L215 25, L216 30,
L217 29) sommano **186**, e con la riga 683 si arriva a **187**.

**56 segnaposto su 9 simboli**, il numero piu' alto della campagna in un lotto: `<destination>` 15, `<payment>` 12,
`<date>` 8, `<planet>` 7, `<cargo>` 6, `<bunks>` 4, `<fare>` 2, `<last>` 1, `<passengers>` 1. Il controllo confronta
**l'ordine**, non solo il multiset: con 15 `<destination>` un riordino silenzioso e' possibile.

**12 `VALUE`** restano inglesi, anche quelli che contengono `<planet>`; **12 `DESCRIPTION`** usano le rese fissate;
**5 `DIALOG`** sono prosa parlata.
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
ED = os.path.join(L10N, 'staging/editorial')
PATH = 'data/human/deep jobs.txt'
WINDOWS = [('L212_20261019_213749', 45), ('L213_20261019_214440', 22),
           ('L214_20261019_215024', 35), ('L215_20261019_215631', 25),
           ('L216_20261019_220252', 30), ('L217_20261019_220809', 29)]
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
EN_ALL = ' '.join(v['english'] for v in cov)
EN_T = sum(len(TAG.findall(v['english'])) for v in cov)
IT_T = sum(len(TAG.findall(v['italian'])) for v in cov)
EN_Q = sum(v['english'].count(QUOTE) for v in cov)
IT_Q = sum(v['italian'].count(QUOTE) for v in cov)
EN_A = sum(v['english'].count(APOS) for v in cov)
IT_A = sum(v['italian'].count(APOS) for v in cov)
KINDS = collections.Counter(u['kind'] for u in units)
CTX = collections.Counter(u['context'] for u in units)
VALS = [u['idx'] for u in units if u['kind'] == 'VALUE']
DESCS = [u['idx'] for u in units if u['kind'] == 'DESCRIPTION']
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 29/29", len(cov) == 29 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 12 VALUE, 12 DESCRIPTION, 5 DIALOG (asserzione scritta)',
   KINDS == {'VALUE': 12, 'DESCRIPTION': 12, 'DIALOG': 5}, dict(KINDS))
ck('ZERO TEXT, MISSION_TEXT, LOGBOOK, UI_LABEL (asserzioni vuote scritte)',
   [u['idx'] for u in units if u['kind'] not in ('VALUE', 'DESCRIPTION', 'DIALOG')] == [])
ck('12 contesti, dal primo Transport Consultants (Deep Security) [0] a Deep Hovercraft Large Racer Transport',
   len(CTX) == 12 and list(CTX)[0] == 'mission:Transport Consultants (Deep Security) [0]'
   and list(CTX)[-1] == 'mission:Deep Hovercraft Large Racer Transport', '%d · %s' % (len(CTX), list(CTX)[-1]))
ck('righe 935 e 1234 (prima e ultima del lotto e del file)',
   (cov[0]['line'], cov[-1]['line']) == (935, 1234), (cov[0]['line'], cov[-1]['line']))
ck('ZERO tab (asserzione negativa scritta)',
   [v['idx'] for v in cov if TAB in v['english'] or TAB in v['italian']] == [])
ck('2 virgolette, entrambe nell\'unita\' 7 (il corriere con il tesserino)',
   EN_Q == 2 == IT_Q and [v['idx'] for v in cov if QUOTE in v['english']] == [7]
   and [v['idx'] for v in cov if QUOTE in v['italian']] == [7])
ck('56 segnaposto su 9 simboli, identici per unita\' E NELLO STESSO ORDINE',
   EN_T == 56 == IT_T
   and not [v['idx'] for v in cov if TAG.findall(v['english']) != TAG.findall(v['italian'])],
   (EN_T, IT_T))
ck('la distribuzione dei simboli e\' quella misurata all\'export',
   collections.Counter(t for v in cov for t in TAG.findall(v['english']))
   == {'<destination>': 15, '<payment>': 12, '<date>': 8, '<planet>': 7, '<cargo>': 6,
       '<bunks>': 4, '<fare>': 2, '<last>': 1, '<passengers>': 1},
   collections.Counter(t for v in cov for t in TAG.findall(v['english'])))
ck('12 VALUE identici all\'inglese, anche quelli con <planet>',
   VALS == [1, 3, 5, 8, 11, 14, 16, 18, 20, 22, 24, 27]
   and all(by[i]['italian'] == by[i]['english'] for i in VALS))
ck("FAMIGLIE VALUE: 6 testi con dimensioni [1, 1, 1, 2, 2, 5] («Shipment to <planet>» cinque volte)",
   sorted(collections.Counter(by[i]['english'] for i in VALS).values()) == [1, 1, 1, 2, 2, 5]
   and sorted(collections.Counter(by[i]['italian'] for i in VALS).values()) == [1, 1, 1, 2, 2, 5],
   (sorted(collections.Counter(by[i]['english'] for i in VALS).values()),
    sorted(collections.Counter(by[i]['italian'] for i in VALS).values())))
ck('FAMIGLIE DESCRIPTION: 7 testi con dimensioni [1, 1, 1, 2, 2, 2, 3] nelle due lingue',
   sorted(collections.Counter(by[i]['english'] for i in DESCS).values()) == [1, 1, 1, 2, 2, 2, 3]
   and sorted(collections.Counter(by[i]['italian'] for i in DESCS).values()) == [1, 1, 1, 2, 2, 2, 3])
ck('i due DIALOG gemelli (10 e 13) hanno la stessa resa',
   by[10]['english'] == by[13]['english'] and by[10]['italian'] == by[13]['italian'])
ck('coerenza: «Il pagamento è <payment>» e «su <destination>» in tutte le DESCRIPTION che li portano',
   all(by[i]['italian'].endswith('Il pagamento è <payment>.') for i in DESCS
       if '<payment>' in by[i]['english']))
ck("apici: 0 in inglese e 4 in italiano (unita' 10, 13 per «dall'aria»; 21, 23 per «all'avanguardia»)",
   EN_A == 0 and IT_A == 4
   and [v['idx'] for v in cov if APOS in v['english']] == []
   and [v['idx'] for v in cov if APOS in v['italian']] == [10, 13, 21, 23], (EN_A, IT_A))
ck('registro unico «tu»: nessun «Lei» e nessun «mi scusi»',
   not re.search(r'\bLei\b|mi scusi', IT_ALL))
ck('nessun caporale e nessun carattere tipografico',
   not [v['idx'] for v in cov if any(c in v['italian'] for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026')])
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' you ', ' to the ', ' will be ',
        ' is ', ' are ', ' from the ', ' its ', ' it is ', ' such as ', ' rather than ', ' for a ', ' that ')
IT_SCAN = IT_ALL
for v in cov:
    if v['kind'] == 'VALUE':
        IT_SCAN = IT_SCAN.replace(v['italian'], '')
ck('nessun residuo inglese (i 12 VALUE restano inglesi e sono esclusi)',
   not [w for w in ENGW if w in IT_SCAN.lower()], [w for w in ENGW if w in IT_SCAN.lower()])
rs = [v['ratio'] for v in cov]
ck('rapporto nel gate 0,55-1,90', 0.55 < min(rs) and max(rs) < 1.90, '%.2f - %.2f' % (min(rs), max(rs)))
ACC = re.compile(r"\b(e|piu|perche|cosi|gia|puo|cioe|percio|fa)'", re.I)
bad = [(v['idx'], ACC.search(v['italian']).group(0)) for v in cov if ACC.search(v['italian'])]
ck('tipografia (accenti veri, nessun apostrofo al posto dell\'accento)', not bad, bad)
nonlat = [v['idx'] for v in cov for c in v['italian'] if ord(c) > 127 and not 0x00C0 <= ord(c) <= 0x024F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio',
   not [v['idx'] for v in cov if v['italian'] != v['italian'].rstrip()
        or '  ' in v['italian'] or v['english'] != v['english'].rstrip()])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
lines, per_win, wrong = [], {}, []
for w, n in WINDOWS:
    d = json.load(open(os.path.join(ED, w, 'translation.json'), encoding='utf-8'))['units']
    got = [u['line'] for u in d if u['path'] == PATH]
    per_win[w] = len(got)
    if len(got) != n:
        wrong.append((w, n, len(got)))
    lines += got
ck('sei finestre reali: 45, 22, 35, 25, 30, 29',
   list(per_win.values()) == [45, 22, 35, 25, 30, 29] and not wrong, (per_win, wrong))
dbl = [r[0] for r in db.execute('select line from units where path=? order by line', (PATH,))]
ck('FILE CHIUSO: 186 righe tradotte distinte, piu\' l\'UI_LABEL della 683, coprono i 187 del DB',
   len(lines) == 186 == len(set(lines)) and sorted(set(lines) | {683}) == dbl,
   (len(lines), len(set(lines)), len(dbl)))
st = dict(db.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('le 29 unita sono PENDING (misurato)',
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
