r"""check.py — L215 (`data/human/deep jobs.txt`, 25 unita', righe 684-864). Quarto lotto del file.

**Dialogo di Wayde** (unita' 1-12, 14 tab): 23 virgolette, di cui **una sola in apertura** all'unita' 1 — la citazione
continua nel paragrafo successivo, come nel file originale. Il controllo verifica la **distribuzione per unita'**:
`1` all'unita' 1, `2` nelle altre, `4` all'unita' 10.

**La battuta**: Wayde dice *at any rate* due volte (fine dell'unita' 1 e inizio della 2) e il giocatore glielo fa notare
nell'unita' 6, che **cita la frase fra apici singoli**. La resa deve usare **la stessa espressione** nei tre punti,
altrimenti la battuta non funziona: «in ogni caso».

**10 unita' di missione**: 5 `VALUE` (3 testi distinti) e 5 `DESCRIPTION` (3 testi distinti), con `<date>` all'unita' 22.
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
EN_TAB = sum(v['english'].count(TAB) for v in cov)
IT_TAB = sum(v['italian'].count(TAB) for v in cov)
KINDS = collections.Counter(u['kind'] for u in units)
CTX = collections.Counter(u['context'] for u in units)
VALS = [u['idx'] for u in units if u['kind'] == 'VALUE']
DESCS = [u['idx'] for u in units if u['kind'] == 'DESCRIPTION']
TAB_UNITS = list(range(1, 13)) + [24, 25]
QDIST = [1, 2, 2, 2, 2, 2, 2, 2, 2, 4, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 2, 0]
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 25/25", len(cov) == 25 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 15 MISSION_TEXT, 5 VALUE, 5 DESCRIPTION (asserzione scritta)',
   KINDS == {'MISSION_TEXT': 15, 'VALUE': 5, 'DESCRIPTION': 5}, dict(KINDS))
ck('ZERO TEXT, DIALOG, LOGBOOK, UI_LABEL (asserzioni vuote scritte)',
   [u['idx'] for u in units if u['kind'] not in ('MISSION_TEXT', 'VALUE', 'DESCRIPTION')] == [])
ck('6 contesti, dal primo Deep Security Package Reveal a Deep Consultants',
   len(CTX) == 6 and list(CTX)[0] == 'mission:Deep Security Package Reveal'
   and list(CTX)[-1] == 'mission:Deep Consultants', '%d · %s' % (len(CTX), list(CTX)[-1]))
ck('righe 684 e 864 (prima e ultima del lotto)',
   (cov[0]['line'], cov[-1]['line']) == (684, 864), (cov[0]['line'], cov[-1]['line']))
ck("TAB: 14 in entrambe le lingue, uno per unita' nelle 1-12 e 24-25, sempre iniziale",
   EN_TAB == 14 == IT_TAB
   and [v['idx'] for v in cov if TAB in v['english']] == TAB_UNITS
   and [v['idx'] for v in cov if TAB in v['italian']] == TAB_UNITS
   and all(v['english'].startswith(TAB) == v['italian'].startswith(TAB) for v in cov))
ck('CITAZIONE SU DUE PARAGRAFI: 29 virgolette con distribuzione per unita\' identica alle due lingue',
   EN_Q == 29 == IT_Q
   and [v['english'].count(QUOTE) for v in cov] == QDIST
   and [v['italian'].count(QUOTE) for v in cov] == QDIST, (EN_Q, [v['italian'].count(QUOTE) for v in cov]))
ck("l'unita' 1 apre la citazione SENZA chiuderla (1 virgoletta), la 2 la apre e la chiude",
   by[1]['italian'].count(QUOTE) == 1 and by[1]['italian'].startswith(TAB + QUOTE)
   and not by[1]['italian'].endswith(QUOTE)
   and by[2]['italian'].startswith(TAB + QUOTE) and by[2]['italian'].endswith(QUOTE))
ck('15 segnaposto su 4 simboli, identici per unita\' e nello stesso ordine',
   EN_T == 15 == IT_T
   and not [v['idx'] for v in cov if TAG.findall(v['english']) != TAG.findall(v['italian'])]
   and collections.Counter(t for v in cov for t in TAG.findall(v['english']))
   == {'<planet>': 5, '<destination>': 5, '<payment>': 4, '<date>': 1},
   (EN_T, IT_T))
ck('<date> compare solo nell\'unita\' 22 (la scadenza della missione)',
   [v['idx'] for v in cov if '<date>' in v['english']] == [22]
   and [v['idx'] for v in cov if '<date>' in v['italian']] == [22])
ck('5 VALUE identici all\'inglese (3 testi distinti)',
   VALS == [13, 15, 17, 19, 21] and all(by[i]['italian'] == by[i]['english'] for i in VALS)
   and len({by[i]['english'] for i in VALS}) == 3)
ck('FAMIGLIE: 3 testi di VALUE e 3 di DESCRIPTION, con le stesse dimensioni nelle due lingue',
   sorted(collections.Counter(' '.join(by[i]['english'].split()) for i in VALS).values()) == [1, 2, 2]
   and sorted(collections.Counter(' '.join(by[i]['italian'].split()) for i in VALS).values()) == [1, 2, 2]
   and sorted(collections.Counter(' '.join(by[i]['english'].split()) for i in DESCS).values()) == [1, 2, 2]
   and sorted(collections.Counter(' '.join(by[i]['italian'].split()) for i in DESCS).values()) == [1, 2, 2])
ck("LA BATTUTA: «in ogni caso» compare tre volte — chiude la 1, apre la 2, citato nella 6",
   'in ogni caso' in by[1]['italian'] and by[1]['italian'].rstrip().endswith('è andato bene.')
   and by[2]['italian'].lstrip(TAB + QUOTE).startswith('Quindi, in ogni caso')
   and "'in ogni caso'" in by[6]['italian']
   and "at any rate" in by[1]['english'].lower().replace('.', '')
   and EN_ALL.count('at any rate') == 3 == IT_ALL.count('in ogni caso'),
   (EN_ALL.count('at any rate'), IT_ALL.count('in ogni caso')))
ck("apici: 14 inglesi (unita' 1-9) e 8 italiani (unita' 1, 2, 3, 6, 11, 12), cause diverse",
   EN_A == 14 and IT_A == 8
   and [v['idx'] for v in cov if APOS in v['english']] == [1, 2, 4, 5, 6, 8, 9, 10, 23, 24]
   and [v['idx'] for v in cov if APOS in v['italian']] == [1, 2, 3, 6, 11, 12], (EN_A, IT_A))
ck('registro unico «tu»: nessun «Lei», nessun «mi scusi»',
   not re.search(r'\bLei\b|mi scusi|Si accomodi', IT_ALL))
ck('coerenza: «Il pagamento è <payment>» e «Consegna … su <destination>» (resa di L198)',
   all(by[i]['italian'].endswith('Il pagamento è <payment>.') for i in DESCS if i != 22)
   and all(' su <destination>' in by[i]['italian'] for i in DESCS if i != 22))
ck('nessun caporale e nessun carattere tipografico',
   not [v['idx'] for v in cov if any(c in v['italian'] for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026')])
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' you ', ' to the ', ' will be ',
        ' is ', ' are ', ' from the ', ' its ', ' it is ', ' such as ', ' rather than ', ' for a ', ' that ')
IT_SCAN = IT_ALL.replace('Secure delivery to', '').replace('Deep Security delivery to', '') \
    .replace('Transport consultants to', '')
ck('nessun residuo inglese (i VALUE restano inglesi e sono esclusi)',
   not [w for w in ENGW if w in IT_SCAN.lower()], [w for w in ENGW if w in IT_SCAN.lower()])
rs = [v['ratio'] for v in cov]
ck('rapporto nel gate 0,55-1,90', 0.55 < min(rs) and max(rs) < 1.90, '%.2f - %.2f' % (min(rs), max(rs)))
ACC = re.compile(r"\b(e|piu|perche|cosi|gia|puo|cioe|percio|fa)'", re.I)
bad = [(v['idx'], ACC.search(v['italian']).group(0)) for v in cov if ACC.search(v['italian'])]
ck('tipografia (accenti veri, nessun apostrofo al posto dell\'accento)', not bad, bad)
nonlat = [v['idx'] for v in cov for c in v['italian'] if ord(c) > 127 and not 0x00C0 <= ord(c) <= 0x024F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio (tab iniziali ammessi)',
   not [v['idx'] for v in cov if v['italian'] != v['italian'].rstrip()
        or '  ' in v['italian'].strip(TAB) or v['english'] != v['english'].rstrip()])
c = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
st = dict(c.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('tutte le 25 unita sono PENDING (misurato)',
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
