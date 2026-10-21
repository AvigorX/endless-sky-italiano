r"""check.py — L214 (`data/human/deep jobs.txt`, 35 unita', righe 457-682). Terzo lotto del file.

**15 tab** dentro 16 `MISSION_TEXT` e 1 `LOGBOOK`: sono i separatori dei paragrafi dei testi di missione lunghi. Il
controllo li verifica **per unita'** (`1` in ognuna delle unita' 21-35, `0` nelle altre), non a totale.

**Blocco di frammenti** `phrase:secure package dropoff payment` (1-8): «Come da istruzioni, consegni il pacco» + «alla
reception di un'azienda tecnologica.» La preposizione articolata sta **dentro l'alternativa**, perche' cambia con la
destinazione; il frammento d'apertura resta senza.

**10 unita' ripetute**: 5 `VALUE` «Secure delivery to <planet>» (invariati) e 5 `DESCRIPTION` identiche.

**Dialogo con Wayde**: 22 virgolette in 11 unita', registro unico «tu» (nessuna cortesia «Lei»), anche dove l'inglese e'
piu' formale (*allow me to take a moment of your time*).
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
VALS = [u['idx'] for u in units if u['kind'] == 'VALUE']
DESCS = [u['idx'] for u in units if u['kind'] == 'DESCRIPTION']
TAB_UNITS = list(range(21, 36))
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 35/35", len(cov) == 35 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 16 MISSION_TEXT, 8 TEXT, 5 VALUE, 5 DESCRIPTION, 1 LOGBOOK',
   KINDS == {'MISSION_TEXT': 16, 'TEXT': 8, 'VALUE': 5, 'DESCRIPTION': 5, 'LOGBOOK': 1}, dict(KINDS))
ck('ZERO DIALOG e ZERO UI_LABEL (asserzioni vuote scritte)',
   [u['idx'] for u in units if u['kind'] in ('DIALOG', 'UI_LABEL')] == [])
ck('7 contesti, dal primo secure package dropoff payment a Deep Security Package Reveal',
   len(CTX) == 7 and list(CTX)[0] == 'phrase:secure package dropoff payment'
   and list(CTX)[-1] == 'mission:Deep Security Package Reveal', '%d · %s' % (len(CTX), list(CTX)[-1]))
ck('righe 457 e 682 (prima e ultima del lotto)',
   (cov[0]['line'], cov[-1]['line']) == (457, 682), (cov[0]['line'], cov[-1]['line']))
ck("TAB: 15 in inglese e 15 in italiano, UNO in ognuna delle unita' 21-35 e zero altrove",
   EN_TAB == 15 == IT_TAB
   and [v['idx'] for v in cov if TAB in v['english']] == TAB_UNITS
   and [v['idx'] for v in cov if TAB in v['italian']] == TAB_UNITS
   and not [v['idx'] for v in cov if v['english'].count(TAB) != v['italian'].count(TAB)], (EN_TAB, IT_TAB))
ck('il tab e\' iniziale, non interno (separatore di paragrafo)',
   all(v['english'].startswith(TAB) == v['italian'].startswith(TAB) for v in cov))
ck('22 virgolette, 2 per unita\' nelle 11 unita\' di dialogo, in entrambe le lingue',
   EN_Q == 22 == IT_Q and all(v['english'].count(QUOTE) == v['italian'].count(QUOTE) for v in cov)
   and [v['idx'] for v in cov if QUOTE in v['english']] == [24, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35],
   (EN_Q, IT_Q))
ck('16 segnaposto su 3 simboli, identici per unita\'',
   EN_T == 16 == IT_T
   and collections.Counter(t for v in cov for t in TAG.findall(v['english']))
   == {'<payment>': 6, '<planet>': 5, '<destination>': 5}
   and not [v['idx'] for v in cov
            if collections.Counter(TAG.findall(v['english'])) != collections.Counter(TAG.findall(v['italian']))],
   (EN_T, IT_T))
ck('5 VALUE identici all\'inglese (nomi di missione)',
   VALS == [9, 11, 13, 15, 17] and all(by[i]['italian'] == by[i]['english'] for i in VALS))
ck('FAMIGLIE: 5 VALUE identici e 5 DESCRIPTION identiche, in entrambe le lingue',
   len({by[i]['english'] for i in VALS}) == 1 and len({by[i]['italian'] for i in VALS}) == 1
   and len({by[i]['english'] for i in DESCS}) == 1 and len({by[i]['italian'] for i in DESCS}) == 1
   and DESCS == [10, 12, 14, 16, 18])
ck("COMPOSIZIONE: il frammento d'apertura non porta la preposizione, che sta nelle alternative",
   by[1]['italian'] == 'Come da istruzioni, consegni il pacco'
   and all(by[i]['italian'].startswith(('a ', 'al ', 'alla ')) for i in range(2, 8))
   and not [v['idx'] for v in cov if v['idx'] in PHRASE
            and v['english'][0].isupper() != v['italian'][0].isupper()])
ck('le sei alternative di consegna restano distinte',
   len({by[i]['italian'] for i in range(2, 8)}) == 6)
ck("apici: 6 inglesi (unita' 23, 27, 28, 31, 35) e 6 italiani (unita' 2, 3, 31), cause diverse",
   EN_A == 6 and IT_A == 6
   and [v['idx'] for v in cov if APOS in v['english']] == [23, 27, 28, 31, 35]
   and [v['idx'] for v in cov if APOS in v['italian']] == [2, 3, 31], (EN_A, IT_A))
ck('registro unico «tu» anche nel dialogo formale: «Accomodati», non «Si accomodi»',
   'Accomodati' in by[24]['italian'] and 'Si accomodi' not in IT_ALL
   and not re.search(r'\bLei\b', IT_ALL))
ck('coerenza con L212: la notifica bancaria usa la stessa resa',
   by[8]['italian'] == 'Il tuo conto in banca ti avvisa subito che il pagamento concordato di <payment> è stato depositato.'
   and by[8]['italian'].startswith('Il tuo conto in banca ti avvisa subito'))
ck('nessun caporale e nessun carattere tipografico',
   not [v['idx'] for v in cov if any(c in v['italian'] for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026')])
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' you ', ' to the ', ' will be ',
        ' is ', ' are ', ' from the ', ' its ', ' it is ', ' such as ', ' rather than ', ' for a ', ' that ')
IT_SCAN = IT_ALL.replace('Secure delivery to', '')
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
ck('tutte le 35 unita sono PENDING (misurato)',
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
