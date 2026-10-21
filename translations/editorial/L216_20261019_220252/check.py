r"""check.py — L216 (`data/human/deep jobs.txt`, 30 unita', righe 866-929). Quinto lotto del file.

**Tre tipi insieme**: 14 `MISSION_TEXT` (dialogo di Julie, 12 con tab), 1 `LOGBOOK` (narrativa in terza persona), 15
`TEXT` in **due blocchi di frammenti** `phrase:` (pickup 10 unita', dropoff 5).

**Composizione pickup**: «In base alla richiesta di alloggio, tu» + «incontri i `<passengers>` nel loro alloggio in
albergo» + «in una zona tranquilla dello spazioporto» + «e li accompagni a bordo.» Quattro gruppi di alternative
(2 aperture, 4 modi di prelevare, 3 luoghi, 1 chiusura).

**Segnaposto**: 7 su 3 simboli, con **`<last>`** (un cognome) e **`<passengers>`** (un numero) per la prima volta in
questo lotto. L'articolo davanti a `<passengers>` segue l'inglese (*the <passengers>*): è una scelta dichiarata.
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
PHRASE = [u['idx'] for u in units if u['context'].startswith('phrase:')]
TAB_UNITS = list(range(1, 13)) + [15]
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 30/30", len(cov) == 30 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 15 TEXT, 14 MISSION_TEXT, 1 LOGBOOK (asserzione scritta)',
   KINDS == {'TEXT': 15, 'MISSION_TEXT': 14, 'LOGBOOK': 1}, dict(KINDS))
ck('ZERO VALUE, DIALOG, UI_LABEL (asserzioni vuote scritte)',
   [u['idx'] for u in units if u['kind'] not in ('TEXT', 'MISSION_TEXT', 'LOGBOOK')] == [])
ck('3 contesti, dal primo Deep Consultants a stranded consultant dropoff payment',
   len(CTX) == 3 and list(CTX)[0] == 'mission:Deep Consultants'
   and list(CTX)[-1] == 'phrase:stranded consultant dropoff payment',
   '%d · %s' % (len(CTX), list(CTX)[-1]))
ck('righe 866 e 929 (prima e ultima del lotto)',
   (cov[0]['line'], cov[-1]['line']) == (866, 929), (cov[0]['line'], cov[-1]['line']))
ck("TAB: 13 in entrambe le lingue, uno per unita' nelle 1-12 e nella 15",
   EN_TAB == 13 == IT_TAB
   and [v['idx'] for v in cov if TAB in v['english']] == TAB_UNITS
   and [v['idx'] for v in cov if TAB in v['italian']] == TAB_UNITS
   and all(v['english'].startswith(TAB) == v['italian'].startswith(TAB) for v in cov))
ck('26 virgolette, 2 per unita\' nelle 12 unita\' di dialogo e nella 15, zero altrove',
   EN_Q == 26 == IT_Q
   and all(v['english'].count(QUOTE) == v['italian'].count(QUOTE) for v in cov)
   and [v['idx'] for v in cov if QUOTE in v['english']] == list(range(1, 13)) + [15],
   (EN_Q, IT_Q))
ck('7 segnaposto su 3 simboli, identici per unita\' e nello stesso ordine',
   EN_T == 7 == IT_T
   and not [v['idx'] for v in cov if TAG.findall(v['english']) != TAG.findall(v['italian'])]
   and collections.Counter(t for v in cov for t in TAG.findall(v['english']))
   == {'<passengers>': 4, '<payment>': 2, '<last>': 1},
   (EN_T, collections.Counter(t for v in cov for t in TAG.findall(v['english']))))
ck('<passengers> sta solo nelle quattro alternative di prelievo (18-21)',
   [v['idx'] for v in cov if '<passengers>' in v['english']] == [18, 19, 20, 21])
ck('<last> sta solo nell\'unita\' 15 (la battuta finale di Julie) e non si traduce',
   [v['idx'] for v in cov if '<last>' in v['english']] == [15]
   and 'capitano <last>' in by[15]['italian'])
ck('COMPOSIZIONE: le due aperture finiscono con «tu», le quattro prese sono minuscole e distinte',
   [by[i]['italian'] for i in (16, 17)] == ['In base alla richiesta di alloggio, tu',
                                            'Nonostante il preavviso breve, tu']
   and all(by[i]['italian'][0].islower() for i in (18, 19, 20, 21, 22, 23, 24))
   and len({by[i]['italian'] for i in (18, 19, 20, 21)}) == 4
   and len({by[i]['italian'] for i in (22, 23, 24)}) == 3
   and by[25]['italian'].startswith('e li accompagni'))
ck('le quattro varianti di dropoff restano distinte (26-29) e la 30 e\' il pagamento',
   len({by[i]['italian'] for i in (26, 27, 28, 29)}) == 4
   and '<payment>' in by[30]['italian'])
ck("apici: 15 inglesi (unita' 1, 5, 6, 7, 9, 10, 11, 15, 28, 29) e 9 italiani (8, 9, 13, 14, 15, 23, 29)",
   EN_A == 15 and IT_A == 9
   and [v['idx'] for v in cov if APOS in v['english']] == [1, 5, 6, 7, 9, 10, 11, 15, 28, 29]
   and [v['idx'] for v in cov if APOS in v['italian']] == [8, 9, 13, 14, 15, 23, 29], (EN_A, IT_A))
ck("LOGBOOK: apre in terza persona («Una consulente che…») e poi parla al giocatore, come il sorgente (from you)",
   by[13]['italian'].startswith('Una consulente che')
   and re.search(r'\bti\b', by[13]['italian']) is not None
   and 'from you' in by[13]['english'] and 'showed you' in by[13]['english'])
ck('registro unico «tu»: nessun «Lei», nessun «mi scusi», nessun «Si accomodi»',
   not re.search(r'\bLei\b|mi scusi|Si accomodi', IT_ALL))
ck('coerenza: «ti avvisa subito» (L212/L214) qui diventa «ti avvisa presto», perche\' il sorgente dice soon',
   'ti avvisa presto' in by[30]['italian'] and 'ti avvisa subito' not in by[30]['italian']
   and 'soon notifies' in by[30]['english'])
ck('nessun caporale e nessun carattere tipografico',
   not [v['idx'] for v in cov if any(c in v['italian'] for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026')])
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' you ', ' to the ', ' will be ',
        ' is ', ' are ', ' from the ', ' its ', ' it is ', ' such as ', ' rather than ', ' for a ', ' that ')
ck('nessun residuo inglese', not [w for w in ENGW if w in IT_ALL.lower()],
   [w for w in ENGW if w in IT_ALL.lower()])
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
ck('tutte le 30 unita sono PENDING (misurato)',
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
