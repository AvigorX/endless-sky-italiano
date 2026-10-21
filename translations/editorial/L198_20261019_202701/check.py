r"""check.py — L198 (`data/hai/hai jobs.txt`, 51 unita', righe 988-1565). Terzo lotto, il piu' grande dei cinque.

**22 `VALUE`** copiati alla lettera, **24 `DESCRIPTION`** e **5 `DIALOG`** tradotti. **Zero tab**, **2 virgolette**
(entrambe nel `VALUE` `Hai "prison" cruise to <planet>`), **1 apice** inglese (`it's`) contro **3** italiani
(`l'esperienza`, `d'affari` x2): l'apice si lega alla causa, non si conserva.

**112 segnaposto su 7 simboli** (nessuno nuovo rispetto a L197), confrontati per **multiset di unita'**.

Due template dominano il lotto e si verificano come **famiglie**:
- `Deliver <cargo> to <destination>. Payment is <payment>.` — **11 copie** (idx 7…27 dispari), una sola resa;
- `Deliver <cargo> to <destination> by <date>. Payment is <payment>.` — **8 copie** (idx 29…43 dispari), una sola resa.

**Coerenza cross-lot**: entrambe le stringhe hanno rese precedenti **concorrenti** in staging (`a`/`su <destination>`,
`pagamento`/`compenso`). La scelta (`su <destination>`, `Il pagamento è`) e' dichiarata, e' una delle rese esistenti e
coincide con quella usata nei lotti L196-L197 dello stesso file. Per `operai tessili` esiste **una sola** resa
precedente e si riusa alla lettera.
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
HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
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
TAGS = re.compile(r'<[^<>]+>')
NON_VALUE = ' '.join(v['italian'] for v in cov if v['kind'] != 'VALUE')
IT_ALL = ' '.join(v['italian'] for v in cov)
EN_Q = sum(v['english'].count(QUOTE) for v in cov)
IT_Q = sum(v['italian'].count(QUOTE) for v in cov)
EN_A = sum(v['english'].count(APOS) for v in cov)
IT_A = sum(v['italian'].count(APOS) for v in cov)
KINDS = collections.Counter(u['kind'] for u in units)
CARGO = 'Consegna <cargo> su <destination>. Il pagamento è <payment>.'
RUSH = 'Consegna <cargo> su <destination> entro il <date>. Il pagamento è <payment>.'
WORK = 'Auguri agli operai ogni fortuna su <planet>, e incassi il pagamento di <payment>.'
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


def prior_italians(english):
    found = set()
    for f in glob.glob(os.path.join(L10N, 'staging/editorial/L*/translation.json')):
        if os.path.dirname(f) == HERE:
            continue
        try:
            d = json.load(open(f, encoding='utf-8'))
        except Exception:
            continue
        for u in d.get('units', []):
            if u.get('english') == english and u.get('italian'):
                found.add(u['italian'])
    return found


ck("unita' tradotte 51/51", len(cov) == 51 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 22 VALUE, 24 DESCRIPTION, 5 DIALOG (asserzione scritta)',
   KINDS == {'VALUE': 22, 'DESCRIPTION': 24, 'DIALOG': 5}, dict(KINDS))
ck('ZERO UI_LABEL, ZERO tab, ZERO TEXT (asserzioni vuote scritte)',
   [u['idx'] for u in units if u['kind'] == 'UI_LABEL'] == []
   and [u['idx'] for u in units if u['kind'] == 'TEXT'] == []
   and [u['idx'] for u in units if u['english'].startswith(TAB)] == []
   and [v['idx'] for v in cov if v['italian'].startswith(TAB)] == [])
ctx = [u['context'].replace('mission:', '') for u in units]
ck('25 contesti distinti, da Transport Hai farmers to <planet> a Swiftsong Business Convention [2]',
   len(set(ctx)) == 25 and (ctx[0], ctx[-1]) == ('Transport Hai farmers to <planet>', 'Swiftsong Business Convention [2]'),
   '%d · %s · %s' % (len(set(ctx)), ctx[0], ctx[-1]))
ck('righe 988 e 1565 (prima e ultima del lotto)',
   (cov[0]['line'], cov[-1]['line']) == (988, 1565), (cov[0]['line'], cov[-1]['line']))
EN_T = collections.Counter(t for u in units for t in TAGS.findall(u['english']))
IT_T = collections.Counter(t for v in cov for t in TAGS.findall(v['italian']))
ck('112 segnaposto su 7 simboli, stesso multiset in inglese e italiano',
   sum(EN_T.values()) == 112 and len(EN_T) == 7 and EN_T == IT_T, (sum(EN_T.values()), len(EN_T), dict(EN_T)))
bad_tags = [(v['idx'], sorted(TAGS.findall(v['english'])), sorted(TAGS.findall(v['italian'])))
            for v in cov
            if collections.Counter(TAGS.findall(v['english'])) != collections.Counter(TAGS.findall(v['italian']))]
ck('nessuna unita\' perde, duplica o sposta un segnaposto', not bad_tags, bad_tags)
ck('22 VALUE identici all\'inglese, uno per uno',
   [v['idx'] for v in cov if v['kind'] == 'VALUE']
   == [6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 47, 50]
   and all(v['italian'] == v['english'] for v in cov if v['kind'] == 'VALUE'))
ck('5 DIALOG tradotti (nessuno lasciato in inglese)',
   [v['idx'] for v in cov if v['kind'] == 'DIALOG'] == [1, 3, 5, 46, 49]
   and all(v['italian'] != v['english'] for v in cov if v['kind'] == 'DIALOG'))
ck('2 virgolette in entrambe le lingue, entrambe nel VALUE `Hai "prison" cruise` (idx 44)',
   EN_Q == 2 == IT_Q
   and [v['idx'] for v in cov if QUOTE in v['english']] == [44]
   and [v['idx'] for v in cov if QUOTE in v['italian']] == [44], (EN_Q, IT_Q))
ck("apici: 1 inglese (it's, idx 45) e 3 italiani (l'esperienza 45, d'affari 48/51), causa misurata",
   EN_A == 1 and IT_A == 3
   and [v['idx'] for v in cov if APOS in v['english']] == [45]
   and [v['idx'] for v in cov if APOS in v['italian']] == [45, 48, 51], (EN_A, IT_A))
ck('nessun caporale e nessun carattere tipografico',
   not [v['idx'] for v in cov if any(c in v['italian'] for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026')])
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' you ', ' to the ', ' will be ',
        ' is ', ' are ', ' from the ', ' its ', ' it is ', ' such as ', ' rather than ', ' for a ')
ck('nessun residuo inglese fuori dai VALUE (che restano inglesi per convenzione)',
   not [w for w in ENGW if w in NON_VALUE.lower()], [w for w in ENGW if w in NON_VALUE.lower()])
CORT = re.findall(r'\bLei\b|(?<![.!?] )\b(?:Suo|Sua|Suoi|Sue)\b', IT_ALL)
ck('nessuna forma di cortesia «Lei»', not CORT, CORT)
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
ck('famiglia cargo (11 copie, idx 7...27 dispari): una sola resa',
   [v['idx'] for v in cov if v['english'] == 'Deliver <cargo> to <destination>. Payment is <payment>.']
   == [7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27]
   and len({by[i]['italian'] for i in (7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27)}) == 1
   and by[7]['italian'] == CARGO)
ck('famiglia rush (8 copie, idx 29...43 dispari): una sola resa',
   [v['idx'] for v in cov if v['english'] == 'Deliver <cargo> to <destination> by <date>. Payment is <payment>.']
   == [29, 31, 33, 35, 37, 39, 41, 43]
   and len({by[i]['italian'] for i in (29, 31, 33, 35, 37, 39, 41, 43)}) == 1
   and by[29]['italian'] == RUSH)
ck('famiglia "operai" (3 e 5): resa unica e identica al precedente L22',
   by[3]['italian'] == by[5]['italian'] == WORK and WORK in prior_italians(by[3]['english']))
ck('famiglia "convention" (48 e 51): resa unica',
   by[48]['italian'] == by[51]['italian'] and by[48]['english'] == by[51]['english'])
ck('operai tessili (2) usa la resa gia\' in staging; operai di fabbrica (4) la stessa cornice',
   by[2]['italian'] in prior_italians(by[2]['english'])
   and by[2]['italian'].replace('operai tessili', 'X') == by[4]['italian'].replace('operai di fabbrica', 'X'))
ck('contadini (1) e operai (3): stessa coda, soggetto diverso',
   by[1]['italian'].endswith('ogni fortuna su <planet>, e incassi il pagamento di <payment>.')
   and by[3]['italian'].endswith('ogni fortuna su <planet>, e incassi il pagamento di <payment>.')
   and by[1]['italian'] != by[3]['italian'])
ck('coerenza cross-lot: la resa del cargo e\' UNA di quelle gia\' in staging (non inventata)',
   CARGO in prior_italians(by[7]['english']) and RUSH in prior_italians(by[29]['english']),
   (sorted(prior_italians(by[7]['english'])), sorted(prior_italians(by[29]['english']))))
ck('VALUE per famiglia: 5 "Delivery", 3 "Bulk", 3 "Large bulk", 4 "Rush", 4 "Large rush", 2 "convention"',
   collections.Counter(v['english'] for v in cov if v['kind'] == 'VALUE') == {
       'Delivery to <planet>': 5, 'Bulk delivery to <planet>': 3, 'Large bulk delivery to <planet>': 3,
       'Rush delivery to <planet>': 4, 'Large rush delivery to <planet>': 4, 'Hai "prison" cruise to <planet>': 1,
       '<planet> business convention': 2})
c = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
st = dict(c.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('tutte le 51 unita sono PENDING (misurato)',
   c.execute('select count(*) from units where id in (%s) and state != "PENDING"'
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
