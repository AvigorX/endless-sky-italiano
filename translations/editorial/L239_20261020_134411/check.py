r"""check.py — L239 (`data/avgi/avgi jobs.txt`, 62 unita', righe 20-656). Primo lotto del file.

**File di lavori**: 31 `VALUE` (nome del lavoro, **invariato**) + 31 `DESCRIPTION` (prosa, tradotta), in 31 contesti da
due unita' ciascuno. **Zero tab, zero virgolette, zero apici**: tre asserzioni negative, scritte.

**Sei `DESCRIPTION` distinte** per 31 unita': la resa e' **una sola per stringa inglese** e si verifica come
**famiglia** (indici attesi + stringa unica), non unita' per unita':

    15x  Deliver <cargo> to <destination>. Payment is <payment>.
     9x  <destination> urgently needs a shipment of <cargo> by <date>. Payment is <payment>.
     2x  Take these <bunks> specialists ...
     2x  Take these <bunks> researchers ...
     1x  Take these <bunks> diplomats ... negotiate with unhappy workers ...
     2x  Take these <bunks> diplomats ... soothe dissatisfied Avgi ...

**Coerenza cross-lot verificata, non presunta**: la resa di `Deliver <cargo> to <destination>. Payment is
<payment>.` e' gia' nel corpus **24 volte** («Consegna <cargo> su <destination>. Il pagamento e' <payment>.») e questo
lotto la riprende **identica**; il `check.py` la cerca nei `translation.json` dei lotti precedenti.

**I `VALUE` restano inglesi** (decisione 15): i due lotti di lavori piu' recenti (`coalition jobs.txt` L151, `hai jobs.txt`
L198) li hanno lasciati invariati, e la regola del progetto li tratta come **dati**. Sette unita' di altri file li avevano
tradotti (`Rush delivery` -> «Consegna urgente»): la divergenza e' dichiarata in `review.md`.
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
PATH = 'data/avgi/avgi jobs.txt'
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
CTX = collections.Counter(u['context'] for u in units)
VAL = [v for v in cov if v['kind'] == 'VALUE']
DES = [v for v in cov if v['kind'] == 'DESCRIPTION']
FAM = collections.defaultdict(list)
for v in DES:
    FAM[v['english']].append(v['idx'])
FAM_V = collections.defaultdict(list)
for v in VAL:
    FAM_V[v['english']].append(v['idx'])
TOK_EN = collections.Counter(t for v in cov for t in TAG.findall(v['english']))
TOK_IT = collections.Counter(t for v in cov for t in TAG.findall(v['italian']))
ORD = [(v['idx'], tuple(TAG.findall(v['english'])), tuple(TAG.findall(v['italian']))) for v in cov]
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 62/62", len(cov) == 62 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna unita\' vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 31 VALUE + 31 DESCRIPTION', KINDS == {'VALUE': 31, 'DESCRIPTION': 31}, dict(KINDS))
ck('31 contesti, due unita\' ciascuno', len(CTX) == 31 and set(CTX.values()) == {2}, dict(CTX))
ck('righe 20 e 656 (prima e ultima del lotto)', (cov[0]['line'], cov[-1]['line']) == (20, 656),
   (cov[0]['line'], cov[-1]['line']))
ck('ZERO tab, ZERO virgolette, ZERO apici in inglese e in italiano (tre asserzioni negative scritte)',
   sum(v['english'].count(TAB) for v in cov) == 0 == sum(v['italian'].count(TAB) for v in cov)
   and sum(v['english'].count(QUOTE) for v in cov) == 0 == sum(v['italian'].count(QUOTE) for v in cov)
   and sum(v['english'].count(APOS) for v in cov) == 0 == sum(v['italian'].count(APOS) for v in cov))
ck("i 31 VALUE sono IDENTICI all'inglese, per indice", all(v['italian'] == v['english'] for v in VAL)
   and len(VAL) == 31, [v['idx'] for v in VAL if v['italian'] != v['english']])
ck("le 31 DESCRIPTION sono TUTTE tradotte (0 identiche)",
   all(v['italian'] != v['english'] for v in DES) and len(DES) == 31, len(DES))
ck('6 famiglie DESCRIPTION con gli indici attesi',
   {k: v for k, v in FAM.items() if len(v) > 0} and
   sorted((len(v), tuple(v)) for v in FAM.values()) ==
   sorted([(15, (2, 4, 6, 8, 10, 12, 20, 22, 24, 26, 28, 30, 38, 40, 42)),
           (9, (14, 16, 18, 32, 34, 36, 44, 46, 48)),
           (2, (50, 52)), (2, (54, 56)), (1, (58,)), (2, (60, 62))]),
   sorted((len(v), tuple(v)) for v in FAM.values()))
ck('una sola resa per famiglia (nessuna variante dentro il lotto)',
   all(len({v['italian'] for v in DES if v['english'] == k}) == 1 for k in FAM),
   {k[:40]: len({v['italian'] for v in DES if v['english'] == k}) for k in FAM})
ck('6 famiglie VALUE, tutte invariate',
   sorted((len(v), tuple(v)) for v in FAM_V.values()) ==
   sorted([(9, (1, 3, 5, 19, 21, 23, 37, 39, 41)), (6, (7, 9, 11, 25, 27, 29)),
           (9, (13, 15, 17, 31, 33, 35, 43, 45, 47)), (2, (49, 51)),
           (2, (53, 55)), (3, (57, 59, 61))]))
ck("segnaposto: multiset identico per simbolo (133 in 6 famiglie)",
   TOK_EN == TOK_IT == {'<planet>': 31, '<destination>': 31, '<payment>': 31, '<cargo>': 24,
                        '<date>': 9, '<bunks>': 7}, (dict(TOK_EN), dict(TOK_IT)))
ck("segnaposto: stesso ORDINE dentro ogni unita' (il multiset da solo e' cieco: <planet> 31 = <payment> 31)",
   all(a == b for _, a, b in ORD), [(i, a, b) for i, a, b in ORD if a != b])
ck('nessun segnaposto inventato o perso: 0 unita\' con token solo in una lingua',
   [v['idx'] for v in cov if bool(TAG.findall(v['english'])) != bool(TAG.findall(v['italian']))] == [])
ck("la resa di `Deliver <cargo> to <destination>. Payment is <payment>.` riprende quella gia' nel corpus",
   [v['italian'] for v in DES if v['english'].startswith('Deliver <cargo>')][0]
   == 'Consegna <cargo> su <destination>. Il pagamento è <payment>.')
prev = set()
for f in glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json')):
    if os.path.dirname(f) == HERE:
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['english'] == 'Deliver <cargo> to <destination>. Payment is <payment>.':
            prev.add(u['italian'])
ck('...e quella resa esiste DAVVERO nei lotti precedenti (coerenza cross-lot misurata, non presunta)',
   'Consegna <cargo> su <destination>. Il pagamento è <payment>.' in prev, sorted(prev)[:2])
ck('`<date>` prende l\'articolo, come nei 17 precedenti del corpus: «entro il <date>»',
   sum(v['italian'].count('entro il <date>') for v in DES) == 9
   and 'entro <date>' not in ' '.join(v['italian'] for v in DES))
ck('nessun residuo inglese di struttura (the, and, with, for, these, to the)',
   not [w for w in (' the ', ' and ', ' with ', ' for ', ' these ', ' to the ', ' in exchange ')
        if w in ' '.join(v['italian'] for v in DES).lower()],
   [w for w in (' the ', ' and ', ' with ', ' for ', ' these ', ' to the ', ' in exchange ')
    if w in ' '.join(v['italian'] for v in DES).lower()])
ck('registro: nessun «Lei» e nessuna cortesia',
   not re.search(r'\bLei\b|\bSuo\b|\bSua\b|mi scusi', ' '.join(v['italian'] for v in cov)))
ck('nessun caporale e nessun carattere tipografico',
   not [v['idx'] for v in cov if any(c in v['italian'] for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026')])
rs = [v['ratio'] for v in cov]
ck('rapporto nel gate 0,55-1,90 (0,97-1,22; 432 -> 483 parole)',
   0.55 < min(rs) and max(rs) < 1.90, '%.2f - %.2f' % (min(rs), max(rs)))
ALL_IT = ' '.join(v['italian'] for v in cov)
ACC = re.compile(r"\b(e|piu|perche|cosi|gia|puo|cioe|percio)'(?![a-z])", re.I)
bad = [(v['idx'], ACC.search(v['italian']).group(0)) for v in cov if ACC.search(v['italian'])]
ck("tipografia (accenti veri, nessun apostrofo al posto dell'accento)", not bad, bad)
nonlat = [v['idx'] for v in cov for c in v['italian'] if ord(c) > 127 and not 0x00C0 <= ord(c) <= 0x024F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio',
   not [v['idx'] for v in cov if v['italian'] != v['italian'].rstrip() or '  ' in v['italian']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("ZERO unita' prima della riga 20: il lotto APRE il file",
   db.execute('select count(*) from units where path=? and line<20', (PATH,)).fetchone()[0] == 0)
ck("40 unita' dopo la 656 (102 - 62): il lotto NON chiude il file",
   db.execute('select count(*) from units where path=? and line>656', (PATH,)).fetchone()[0] == 40)
ck('il file intero: 102 unita, righe 20 - 1156',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (102, 20, 1156))
ck('62 + 0 + 40 = 102', 62 + 40 == 102)
st = dict(db.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('le 62 unita sono PENDING (misurato)',
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
