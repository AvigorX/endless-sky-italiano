r"""check.py — L197 (`data/hai/hai jobs.txt`, 36 unita', righe 492-967). Secondo lotto del file.

Nessun `TEXT`: qui i dialoghi sono **`DIALOG`** (9), con contesto proprio. **12 `VALUE`** copiati alla lettera,
**15 `DESCRIPTION`** e 9 `DIALOG` tradotti. **Zero tab, zero virgolette, zero apici** in entrambe le lingue:
tre asserzioni **vuote**, scritte comunque.

**81 segnaposto su 11 simboli**, tre dei quali nuovi in questo file: `<stopovers>` (3), `<planet stopovers>` (3),
`<fare>` (3). `<planet stopovers>` contiene uno **spazio**: il regex e' `<[^<>]+>` e il confronto e' per
**multiset di unita'**, non per totale.

**Coerenza cross-lot**: due stringhe di questo lotto (`Bring <fare> to <destination>…` e `This human wishes for
<cargo>…`) esistono gia' in staging. La resa deve essere **quella gia' usata**, non una variante nuova: il
controllo la confronta con i lotti precedenti.
"""
import collections
import glob
import json
import os
import re
import sqlite3

TAB = chr(9)
QUOTE = chr(34)
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
KINDS = collections.Counter(u['kind'] for u in units)
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


def prior_italians(english):
    """Rese gia' presenti in staging per la stessa stringa inglese (lotti precedenti, non VALUE)."""
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


ck("unita' tradotte 36/36", len(cov) == 36 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 12 VALUE, 15 DESCRIPTION, 9 DIALOG (asserzione scritta)',
   KINDS == {'VALUE': 12, 'DESCRIPTION': 15, 'DIALOG': 9}, dict(KINDS))
ck('ZERO UI_LABEL, ZERO tab, ZERO TEXT (asserzioni vuote scritte)',
   [u['idx'] for u in units if u['kind'] == 'UI_LABEL'] == []
   and [u['idx'] for u in units if u['kind'] == 'TEXT'] == []
   and [u['idx'] for u in units if u['english'].startswith(TAB)] == []
   and [v['idx'] for v in cov if v['italian'].startswith(TAB)] == [])
ctx = [u['context'].replace('mission:', '') for u in units]
ck('15 contesti distinti, da Delivery to Human Space [2] a Transport Hai farmers to <planet>',
   len(set(ctx)) == 15 and (ctx[0], ctx[-1]) == ('Delivery to Human Space [2]', 'Transport Hai farmers to <planet>'),
   '%d · %s · %s' % (len(set(ctx)), ctx[0], ctx[-1]))
ck('righe 492 e 967 (prima e ultima del lotto)',
   (cov[0]['line'], cov[-1]['line']) == (492, 967), (cov[0]['line'], cov[-1]['line']))
EN_T = collections.Counter(t for u in units for t in TAGS.findall(u['english']))
IT_T = collections.Counter(t for v in cov for t in TAGS.findall(v['italian']))
ck('81 segnaposto su 11 simboli, stesso multiset in inglese e italiano',
   sum(EN_T.values()) == 81 and len(EN_T) == 11 and EN_T == IT_T, (sum(EN_T.values()), len(EN_T), dict(EN_T)))
ck('i tre simboli nuovi del file: <stopovers> 3, <planet stopovers> 3, <fare> 3',
   EN_T['<stopovers>'] == 3 and EN_T['<planet stopovers>'] == 3 and EN_T['<fare>'] == 3,
   {k: EN_T[k] for k in ('<stopovers>', '<planet stopovers>', '<fare>')})
bad_tags = [(v['idx'], sorted(TAGS.findall(v['english'])), sorted(TAGS.findall(v['italian'])))
            for v in cov
            if collections.Counter(TAGS.findall(v['english'])) != collections.Counter(TAGS.findall(v['italian']))]
ck('nessuna unita\' perde, duplica o sposta un segnaposto', not bad_tags, bad_tags)
ck('12 VALUE identici all\'inglese, uno per uno',
   [v['idx'] for v in cov if v['kind'] == 'VALUE'] == [2, 6, 10, 14, 16, 18, 20, 22, 24, 26, 28, 31]
   and all(v['italian'] == v['english'] for v in cov if v['kind'] == 'VALUE'))
ck('9 DIALOG tradotti (nessuno lasciato in inglese)',
   [v['idx'] for v in cov if v['kind'] == 'DIALOG'] == [4, 5, 8, 9, 12, 13, 30, 33, 35]
   and all(v['italian'] != v['english'] for v in cov if v['kind'] == 'DIALOG'))
ck('zero virgolette in entrambe le lingue (asserzione vuota scritta)', EN_Q == 0 == IT_Q, (EN_Q, IT_Q))
ck("zero apici in entrambe le lingue (asserzione vuota scritta)",
   sum(v['english'].count(chr(39)) for v in cov) == 0
   and sum(v['italian'].count(chr(39)) for v in cov) == 0)
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
TAIL_R = 'Vuole <cargo> da <stopovers> entro il <date>. Il pagamento è <payment>.'
ck('famiglia Escort (15, 17, 19, 21): quattro taglie, una sola resa',
   len({by[i]['italian'] for i in (15, 17, 19, 21)}) == 1
   and len({by[i]['english'] for i in (15, 17, 19, 21)}) == 1)
ck('famiglia Retrieve (3, 7, 11): stessa coda, soggetto e movente diversi',
   all(by[i]['italian'].endswith(TAIL_R) for i in (3, 7, 11))
   and len({by[i]['italian'][:-len(TAIL_R)] for i in (3, 7, 11)}) == 3
   and all(by[i]['italian'].count(TAIL_R) == 1 for i in (3, 7, 11))
   and 'della buona società' in by[3]['italian'] and 'gourmet' in by[7]['italian']
   and 'smanettatore' in by[11]['italian'])
ck('famiglia "Raccogli ... e lo carichi" (4, 8, 12): una sola resa',
   len({by[i]['italian'] for i in (4, 8, 12)}) == 1)
ck('famiglia Passengers (23, 25, 27) e Family (29/32, 30/33): rese uniche dentro la famiglia',
   len({by[i]['italian'] for i in (23, 25, 27)}) == 1
   and by[29]['italian'] == by[32]['italian'] and by[30]['italian'] == by[33]['italian'])
ck('minatori (34) e contadini (36): differiscono solo nel mestiere',
   by[34]['italian'].replace('minatori', 'X') == by[36]['italian'].replace('contadini', 'X'))
FARE = 'Porta <fare> su <destination>. Il pagamento è <payment>.'
ck('coerenza cross-lot: `Bring <fare> to <destination>…` usa la resa gia\' in staging',
   by[23]['italian'] == FARE == by[25]['italian'] == by[27]['italian']
   and FARE in prior_italians(by[23]['english']))
WISH = 'Questo umano chiede che <cargo> venga consegnato a <destination>, nello spazio umano. Il pagamento è <payment>.'
ck('coerenza cross-lot: `This human wishes for <cargo>…` usa la resa gia\' in staging',
   by[1]['italian'] == WISH and WISH in prior_italians(by[1]['english']))
c = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
st = dict(c.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('tutte le 36 unita sono PENDING (misurato)',
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
