r"""check.py — L212 (`data/human/deep jobs.txt`, 45 unita', righe 16-322). **Primo lotto del file.**

Il file ha una forma nuova: **28 `TEXT`** che sono **frammenti di frase** composti dal gioco (`phrase:`), **8 `VALUE`** e
**9 `DESCRIPTION`** di missione. Il lotto e' quindi un test di due cose che i lotti precedenti non chiedevano:

1. **I frammenti devono comporre.** «Come da istruzioni, tu» + «apri una cassetta di sicurezza» + «in un magazzino
   anonimo e disabitato» + «e prelevi il pacco misterioso.» Il controllo verifica che **la maiuscola/minuscola iniziale
   di ogni frammento resti quella inglese**, che e' il marcatore di concatenazione.
2. **I segnaposto devono coincidere uno per uno.** 31 segnaposto su 6 simboli (`<payment>` 11, `<planet>` 8,
   `<destination>` 8, `<stopovers>` 2, `<planet stopovers>` 1, `<bunks>` 1): il controllo confronta il **multiset per
   unita'**, non il totale.

**Famiglie**: 6 `VALUE` identici («Mystery delivery to <planet>») e 6 `DESCRIPTION` identiche («Deliver a package to
<destination>...»). I `VALUE` restano inglesi; le `DESCRIPTION` usano la resa di L198 («su <destination>», «Il pagamento
e' <payment>»).
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
KINDS = collections.Counter(u['kind'] for u in units)
CTX = collections.Counter(u['context'] for u in units)
PHRASE = [u['idx'] for u in units if u['context'].startswith('phrase:')]
VALS = [u['idx'] for u in units if u['kind'] == 'VALUE']
DESCS = [u['idx'] for u in units if u['kind'] == 'DESCRIPTION']
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 45/45", len(cov) == 45 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 28 TEXT, 8 VALUE, 9 DESCRIPTION (asserzione scritta)',
   KINDS == {'TEXT': 28, 'VALUE': 8, 'DESCRIPTION': 9}, dict(KINDS))
ck('ZERO DIALOG, LOGBOOK, MISSION_TEXT, UI_LABEL (asserzioni vuote scritte)',
   [u['idx'] for u in units if u['kind'] not in ('TEXT', 'VALUE', 'DESCRIPTION')] == [])
ck('12 contesti, dal primo phrase:deep mystery cube pickup a mission:Transport scientists',
   len(CTX) == 12 and list(CTX)[0] == 'phrase:deep mystery cube pickup'
   and list(CTX)[-1] == 'mission:Transport scientists', '%d · %s' % (len(CTX), list(CTX)[-1]))
ck('righe 16 e 322 (prima e ultima del lotto)',
   (cov[0]['line'], cov[-1]['line']) == (16, 322), (cov[0]['line'], cov[-1]['line']))
ck('ZERO tab (asserzione negativa scritta)',
   [v['idx'] for v in cov if TAB in v['english'] or TAB in v['italian']] == [])
ck('31 segnaposto su 6 simboli, identici in totale e per unita\'',
   EN_T == 31 == IT_T
   and not [v['idx'] for v in cov
            if collections.Counter(TAG.findall(v['english'])) != collections.Counter(TAG.findall(v['italian']))],
   (EN_T, IT_T))
ck('la distribuzione dei simboli e\' quella misurata all\'export',
   collections.Counter(t for v in cov for t in TAG.findall(v['english']))
   == {'<payment>': 11, '<planet>': 8, '<destination>': 8, '<stopovers>': 2,
       '<planet stopovers>': 1, '<bunks>': 1},
   collections.Counter(t for v in cov for t in TAG.findall(v['english'])))
ck('i segnaposto rari (<bunks>, <planet stopovers>) stanno nelle unita\' giuste',
   TAG.findall(by[45]['italian']) == ['<bunks>', '<stopovers>', '<planet>', '<payment>']
   and TAG.findall(by[43]['italian']) == ['<planet stopovers>'])
ck('8 VALUE identici all\'inglese (nomi di missione mostrati nella bacheca)',
   VALS == [29, 31, 33, 35, 37, 39, 41, 43]
   and all(by[i]['italian'] == by[i]['english'] for i in VALS))
ck('FAMIGLIE: i VALUE sono 2 testi (7 + 1), le DESCRIPTION 3 testi (7 + 1 + 1), uguali nelle due lingue',
   sorted(collections.Counter(' '.join(by[i]['english'].split()) for i in VALS).values()) == [1, 7]
   and sorted(collections.Counter(' '.join(by[i]['italian'].split()) for i in VALS).values()) == [1, 7]
   and sorted(collections.Counter(' '.join(by[i]['english'].split()) for i in DESCS).values()) == [1, 1, 7]
   and sorted(collections.Counter(' '.join(by[i]['italian'].split()) for i in DESCS).values()) == [1, 1, 7])
ck('«Deliver a package to <destination>. Payment is <payment>.» usa la resa di L198: «su <destination>», «Il pagamento e\'»',
   by[30]['italian'] == 'Consegna un pacco su <destination>. Il pagamento è <payment>.')
ck('COMPOSIZIONE: ogni frammento `phrase:` conserva maiuscola o minuscola iniziale dell\'inglese',
   not [v['idx'] for v in cov if v['idx'] in PHRASE
        and v['english'][0].isupper() != v['italian'][0].isupper()],
   [v['idx'] for v in cov if v['idx'] in PHRASE
    and v['english'][0].isupper() != v['italian'][0].isupper()])
ck('COMPOSIZIONE: i primi frammenti «As instructed, you» / «You» sono resi «Come da istruzioni, tu» / «Tu»',
   [by[i]['italian'] for i in (1, 2, 13, 21)] == ['Come da istruzioni, tu', 'Tu', 'Come da istruzioni, tu',
                                                  'Come da istruzioni, tu'])
ck('4 virgolette, nelle unita\' 19 e 27 (citazione del promemoria)',
   EN_Q == 4 == IT_Q and [v['idx'] for v in cov if QUOTE in v['english']] == [19, 27]
   and [v['idx'] for v in cov if QUOTE in v['italian']] == [19, 27], (EN_Q, IT_Q))
ck("lo spazio iniziale delle unita' 19 e 27 e' conservato in entrambe le lingue",
   [v['idx'] for v in cov if v['english'].startswith(' ')] == [19, 27]
   and [v['idx'] for v in cov if v['italian'].startswith(' ')] == [19, 27])
ck("apici: 5 inglesi (unita' 11, 19, 27) e 2 italiani (unita' 12, 23)",
   EN_A == 5 and IT_A == 2
   and [v['idx'] for v in cov if APOS in v['english']] == [11, 19, 27]
   and [v['idx'] for v in cov if APOS in v['italian']] == [12, 23], (EN_A, IT_A))
ck('nessun caporale e nessun carattere tipografico',
   not [v['idx'] for v in cov if any(c in v['italian'] for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026')])
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' you ', ' to the ', ' will be ',
        ' is ', ' are ', ' from the ', ' its ', ' it is ', ' such as ', ' rather than ', ' for a ', ' that ')
IT_SCAN = IT_ALL.replace('Mystery delivery to', '').replace('Mystery retrieval from', '')
ck('nessun residuo inglese (i VALUE restano inglesi e sono esclusi dal controllo)',
   not [w for w in ENGW if w in IT_SCAN.lower()], [w for w in ENGW if w in IT_SCAN.lower()])
rs = [v['ratio'] for v in cov]
ck('rapporto nel gate 0,55-1,90 (i frammenti corti stanno agli estremi del gate)',
   0.55 < min(rs) and max(rs) < 1.90, '%.2f - %.2f' % (min(rs), max(rs)))
ACC = re.compile(r"\b(e|piu|perche|cosi|gia|puo|cioe|percio|fa)'", re.I)
bad = [(v['idx'], ACC.search(v['italian']).group(0)) for v in cov if ACC.search(v['italian'])]
ck('tipografia (accenti veri, nessun apostrofo al posto dell\'accento)', not bad, bad)
nonlat = [v['idx'] for v in cov for c in v['italian'] if ord(c) > 127 and not 0x00C0 <= ord(c) <= 0x024F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio',
   not [v['idx'] for v in cov if v['italian'] != v['italian'].rstrip()
        or '  ' in v['italian'] or v['english'] != v['english'].rstrip()])
ck('i termini di gioco restano coerenti: «bacheca delle missioni», «spazioporto»',
   'bacheca delle missioni' in IT_ALL and 'spazioporto' in IT_ALL)
c = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
st = dict(c.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('tutte le 45 unita sono PENDING (misurato)',
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
