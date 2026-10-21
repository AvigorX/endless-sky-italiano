r"""check.py — L220 (`data/successors/successor ships.txt`, 26 unita', righe 634-873). Terzo lotto del file.

**20 unita' su 26 identiche all'inglese** (16 `TEXT` + 4 `VALUE`), **6 `DESCRIPTION`** tradotte.

**La trappola del lotto**: le unita' **23 e 25** sono lo stesso testo, lungo 374 e 372 caratteri: l'unica differenza sono
le **due virgolette** attorno al nome nella 23 (`l'"Ojde"`). La traduzione deve conservare esattamente quella differenza:
`t[23].replace('"','') == t[25]`. Se una delle due venisse riformulata, la stessa nave avrebbe due schede discordanti.

**Le 34 virgolette** non sono 2 x 17: sono 2 x 16 `TEXT` = 32, piu' le **2 dell'unita' 23 dentro una `DESCRIPTION`**.
Il controllo confronta le mappe per unita', non il totale.
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
PATH = 'data/successors/successor ships.txt'
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
KINDS = collections.Counter(u['kind'] for u in units)
CTX = collections.Counter(u['context'] for u in units)
TEXTS = [u['idx'] for u in units if u['kind'] == 'TEXT']
VALS = [u['idx'] for u in units if u['kind'] == 'VALUE']
DESCS = [u['idx'] for u in units if u['kind'] == 'DESCRIPTION']
EN_Q = {v['idx']: v['english'].count(QUOTE) for v in cov if QUOTE in v['english']}
IT_Q = {v['idx']: v['italian'].count(QUOTE) for v in cov if QUOTE in v['italian']}
EN_A = [(v['idx'], v['english'].count(APOS)) for v in cov if APOS in v['english']]
IT_A = [(v['idx'], v['italian'].count(APOS)) for v in cov if APOS in v['italian']]
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 26/26", len(cov) == 26 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 16 TEXT, 6 DESCRIPTION, 4 VALUE (asserzione scritta)',
   KINDS == {'TEXT': 16, 'DESCRIPTION': 6, 'VALUE': 4}, dict(KINDS))
ck('ZERO DIALOG, MISSION_TEXT, LOGBOOK, NEWS, UI_LABEL (asserzioni vuote scritte)',
   [u['idx'] for u in units if u['kind'] not in ('TEXT', 'DESCRIPTION', 'VALUE')] == [])
ck('4 contesti con le dimensioni misurate: Nnesaarau 9, Ojde 9, Nnaatej 7, Seiitej 1',
   CTX == {'ship:Nnaatej': 7, 'ship:Nnesaarau': 9, 'ship:Ojde': 9, 'ship:Seiitej': 1}, dict(CTX))
ck('righe 634 e 873 (prima e ultima del lotto)',
   (cov[0]['line'], cov[-1]['line']) == (634, 873), (cov[0]['line'], cov[-1]['line']))
ck('1 tab, solo nell\'unita\' 24, identico nelle due lingue',
   [v['idx'] for v in cov if TAB in v['english']] == [24] == [v['idx'] for v in cov if TAB in v['italian']]
   and by[24]['italian'].startswith(TAB) and not by[24]['italian'].startswith(TAB + TAB))
ck('34 virgolette, stesse per unita\' nelle due lingue: 2 x 16 TEXT piu\' 2 nell\'unita\' 23 (DESCRIPTION)',
   sum(EN_Q.values()) == 34 == sum(IT_Q.values()) and EN_Q == IT_Q
   and {i: n for i, n in EN_Q.items() if i in TEXTS} == {i: 2 for i in TEXTS}
   and EN_Q.get(23) == 2 and len(TEXTS) == 16, (EN_Q, IT_Q))
ck('NESSUN segnaposto (asserzione negativa scritta)',
   sum(len(TAG.findall(v['english'])) for v in cov) == 0
   == sum(len(TAG.findall(v['italian'])) for v in cov))
ck('20 unita\' IDENTICHE all\'inglese (16 TEXT + 4 VALUE) e 6 tradotte: sono esattamente le DESCRIPTION',
   sum(1 for v in cov if v['italian'] == v['english']) == 20
   and sorted(v['idx'] for v in cov if v['italian'] != v['english']) == DESCS,
   (sum(1 for v in cov if v['italian'] == v['english']),
    sorted(v['idx'] for v in cov if v['italian'] != v['english'])))
ck('i nomi sono stati COPIATI dal sorgente: 16 TEXT e 4 VALUE identici carattere per carattere',
   all(by[i]['italian'] == by[i]['english'] for i in TEXTS + VALS))
ck('LA COPPIA 23/25: stesso testo, l\'unica differenza sono le 2 virgolette della 23',
   by[23]['italian'].replace(QUOTE, '') == by[25]['italian']
   and by[23]['english'].replace(QUOTE, '') == by[25]['english']
   and len(by[23]['english']) - len(by[25]['english']) == 2
   and len(by[23]['italian']) - len(by[25]['italian']) == 2)
ck('la 25 NON ha virgolette e la 23 si\', e il nome resta nella forma elisa in entrambe',
   QUOTE not in by[25]['italian'] and "l'" + QUOTE + 'Ojde' + QUOTE in by[23]['italian']
   and "l'Ojde" in by[25]['italian'])
ck('coerenza: «Bulk Freighter» e «Behemoth» restano invariati in entrambe le schede',
   IT_ALL.count('Bulk Freighter') == 2 and IT_ALL.count('Behemoth') == 2)
ck('terminologia: «Casa Chydiyi», «Myaede», «Successori»; «House Chydiyi» assente',
   'Casa Chydiyi' in IT_ALL and 'Myaede' in IT_ALL and 'Successori' in IT_ALL
   and 'House Chydiyi' not in IT_ALL)
ck('le 6 DESCRIPTION sono tutte tradotte e tutte distinte',
   len(DESCS) == 6 and all(by[i]['italian'] != by[i]['english'] for i in DESCS)
   and len({by[i]['italian'] for i in DESCS}) == 6)
ck("apici: 2 in inglese (15 House Chydiyi's, 16 don't) e 12 in italiano in 6 unita' "
   "(7 x3, 15, 16, 23 x2, 24 x3, 25 x2)",
   sum(n for _, n in EN_A) == 2 and sum(n for _, n in IT_A) == 12
   and EN_A == [(15, 1), (16, 1)] and IT_A == [(7, 3), (15, 1), (16, 1), (23, 2), (24, 3), (25, 2)],
   (EN_A, IT_A))
ck('registro: nessun «Lei» e nessun «mi scusi»',
   not re.search(r'\bLei\b|mi scusi', IT_ALL))
ck('nessun caporale e nessun carattere tipografico (le virgolette dritte sono legittime)',
   not [v['idx'] for v in cov if any(c in v['italian'] for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026')])
DESC_TXT = ' '.join(by[i]['italian'] for i in DESCS)
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' you ', ' to the ', ' will be ',
        ' is ', ' are ', ' from the ', ' its ', ' it is ', ' such as ', ' rather than ', ' for a ', ' that ',
        ' have ', ' they ', ' their ')
ck('nessun residuo inglese nelle DESCRIPTION (i nomi sono esclusi perche\' identici)',
   not [w for w in ENGW if w in DESC_TXT.lower()], [w for w in ENGW if w in DESC_TXT.lower()])
rs = [v['ratio'] for v in cov]
ck('rapporto nel gate 0,55-1,90 (nomi 1,00; DESCRIPTION 1,05-1,16)',
   0.55 < min(rs) and max(rs) < 1.90, '%.2f - %.2f' % (min(rs), max(rs)))
ACC = re.compile(r"\b(e|piu|perche|cosi|gia|puo|cioe|percio|fa)'", re.I)
bad = [(v['idx'], ACC.search(v['italian']).group(0)) for v in cov if ACC.search(v['italian'])]
ck('tipografia (accenti veri, nessun apostrofo al posto dell\'accento)', not bad, bad)
nonlat = [v['idx'] for v in cov for c in v['italian'] if ord(c) > 127 and not 0x00C0 <= ord(c) <= 0x024F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio (il tab iniziale dell\'unita\' 24 e\' ammesso)',
   not [v['idx'] for v in cov if v['italian'] != v['italian'].rstrip()
        or '  ' in v['italian'].strip(TAB) or v['english'] != v['english'].rstrip()])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck('70 unita tradotte prima della 634 (L218 45 + L219 25)',
   db.execute('select count(*) from units where path=? and line<634', (PATH,)).fetchone()[0] == 70)
ck('lotto + residuo = file: 70 + 26 + 50 = 146',
   70 + 26 + db.execute('select count(*) from units where path=? and line>873', (PATH,)).fetchone()[0] == 146)
st = dict(db.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('le 26 unita sono PENDING (misurato)',
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
