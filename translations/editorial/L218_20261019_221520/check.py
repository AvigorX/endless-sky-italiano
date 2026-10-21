r"""check.py — L218 (`data/successors/successor ships.txt`, 45 unita', righe 17-381). **Primo lotto del file.**

**Il tratto del file**: su 45 unita', **35 sono `TEXT` che sono NOMI DI EQUIPAGGIAMENTO** (`"Ojet" Bimodal Coilgun`,
`"Nnesa" Fusion Core`, `6-"Ruuv" Betavoltaic Cell`) e **4 sono `VALUE`** (nomi di specie: `Aaulqran`, `Ejniisden`). Tutti e
39 vanno **copiati alla lettera, virgolette comprese**: sono nomi mostrati nella schermata della nave. Si traducono solo le
**6 `DESCRIPTION`**.

La regola si decide dal **contenuto**, non dall'etichetta del tipo: in `coalition news.txt` i `TEXT` erano citazioni di
giornale e si traducevano; qui sono nomi di prodotto.

**Nessun segnaposto** nel file: l'asserzione e' negativa e scritta comunque.
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
EN_ALL = ' '.join(v['english'] for v in cov)
KINDS = collections.Counter(u['kind'] for u in units)
CTX = collections.Counter(u['context'] for u in units)
TEXTS = [u['idx'] for u in units if u['kind'] == 'TEXT']
VALS = [u['idx'] for u in units if u['kind'] == 'VALUE']
DESCS = [u['idx'] for u in units if u['kind'] == 'DESCRIPTION']
EN_Q = sum(v['english'].count(QUOTE) for v in cov)
IT_Q = sum(v['italian'].count(QUOTE) for v in cov)
EN_A = sum(v['english'].count(APOS) for v in cov)
IT_A = sum(v['italian'].count(APOS) for v in cov)
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 45/45", len(cov) == 45 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 35 TEXT, 6 DESCRIPTION, 4 VALUE (asserzione scritta)',
   KINDS == {'TEXT': 35, 'DESCRIPTION': 6, 'VALUE': 4}, dict(KINDS))
ck('ZERO DIALOG, MISSION_TEXT, LOGBOOK, NEWS, UI_LABEL (asserzioni vuote scritte)',
   [u['idx'] for u in units if u['kind'] not in ('TEXT', 'DESCRIPTION', 'VALUE')] == [])
ck('4 contesti con le dimensioni misurate: Aaulqra 16, Kaskhorade 13, Ejniisde-Khora 9, Ejniisde 7',
   CTX == {'ship:Aaulqra': 16, 'ship:Ejniisde': 7, 'ship:Ejniisde-Khora': 9, 'ship:Kaskhorade': 13}, dict(CTX))
ck('righe 17 e 381 (prima e ultima del lotto)',
   (cov[0]['line'], cov[-1]['line']) == (17, 381), (cov[0]['line'], cov[-1]['line']))
ck('PRIMO LOTTO DEL FILE: 0 unita prima della 17',
   not [u for u in units if u['line'] < 17])
ck('1 tab, solo nell\'unita\' 32 (la nota sulle Case del Popolo), identico nelle due lingue',
   [v['idx'] for v in cov if TAB in v['english']] == [32]
   and [v['idx'] for v in cov if TAB in v['italian']] == [32]
   and by[32]['italian'].startswith(TAB) and not by[32]['italian'].startswith(TAB + TAB))
ck('70 virgolette: esattamente 2 per ognuna delle 35 TEXT, zero altrove',
   EN_Q == 70 == IT_Q
   and [v['idx'] for v in cov if QUOTE in v['english']] == TEXTS
   and all(v['english'].count(QUOTE) == 2 == v['italian'].count(QUOTE) for v in cov if v['kind'] == 'TEXT'))
ck('NESSUN segnaposto (asserzione negativa scritta)',
   sum(len(TAG.findall(v['english'])) for v in cov) == 0
   == sum(len(TAG.findall(v['italian'])) for v in cov))
ck('i 35 TEXT sono IDENTICI all\'inglese, virgolette comprese',
   len(TEXTS) == 35 and all(by[i]['italian'] == by[i]['english'] for i in TEXTS))
ck('i 4 VALUE sono IDENTICI all\'inglese',
   VALS == [1, 17, 24, 33] and all(by[i]['italian'] == by[i]['english'] for i in VALS))
ck('i nomi si ripetono come nel sorgente: 17 testi distinti, dimensioni [1x9, 2x5, 3x2, 10x1]',
   sorted(collections.Counter(by[i]['english'] for i in TEXTS).values())
   == [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 10]
   and collections.Counter(by[i]['english'] for i in TEXTS)
   == collections.Counter(by[i]['italian'] for i in TEXTS))
ck('«"Ojet" Bimodal Coilgun» compare 10 volte, come nel sorgente',
   sum(1 for i in TEXTS if by[i]['english'] == QUOTE + 'Ojet' + QUOTE + ' Bimodal Coilgun') == 10)
ck('le 6 DESCRIPTION sono TUTTE tradotte (diverse dall\'inglese) e tutte distinte',
   len(DESCS) == 6 and all(by[i]['italian'] != by[i]['english'] for i in DESCS)
   and len({by[i]['italian'] for i in DESCS}) == 6, DESCS)
ck('terminologia: «Alte Case», «Case del Popolo», «Successori» presenti, «High Houses» assente',
   'Alte Case' in IT_ALL and 'Case del Popolo' in IT_ALL and 'Successori' in IT_ALL
   and 'High Houses' not in IT_ALL)
ck("apici: 4 in inglese (15 ship's, 31 People's + liner's, 32 People's) e 4 in italiano "
   "(15 L'Aaulqra, 31 all'interno + dell'Ejniisde, 45 un'ampia): le unita' NON coincidono, e va bene",
   EN_A == 4 and IT_A == 4
   and [(v['idx'], v['english'].count(APOS)) for v in cov if APOS in v['english']] == [(15, 1), (31, 2), (32, 1)]
   and [(v['idx'], v['italian'].count(APOS)) for v in cov if APOS in v['italian']] == [(15, 1), (31, 2), (45, 1)],
   ([(v['idx'], v['english'].count(APOS)) for v in cov if APOS in v['english']],
    [(v['idx'], v['italian'].count(APOS)) for v in cov if APOS in v['italian']]))
ck('registro: nessun «Lei» e nessun «mi scusi»',
   not re.search(r'\bLei\b|mi scusi', IT_ALL))
ck('nessun caporale e nessun carattere tipografico (le virgolette dritte dei nomi sono ammesse)',
   not [v['idx'] for v in cov if any(c in v['italian'] for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026')])
DESC_TXT = ' '.join(by[i]['italian'] for i in DESCS)
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' you ', ' to the ', ' will be ',
        ' is ', ' are ', ' from the ', ' its ', ' it is ', ' such as ', ' rather than ', ' for a ', ' that ',
        ' have ', ' they ', ' their ')
ck('nessun residuo inglese nelle DESCRIPTION (i nomi sono esclusi perche\' identici)',
   not [w for w in ENGW if w in DESC_TXT.lower()], [w for w in ENGW if w in DESC_TXT.lower()])
rs = [v['ratio'] for v in cov]
ck('rapporto nel gate 0,55-1,90 (i nomi valgono 1,00; le DESCRIPTION 1,09-1,15)',
   0.55 < min(rs) and max(rs) < 1.90, '%.2f - %.2f' % (min(rs), max(rs)))
ACC = re.compile(r"\b(e|piu|perche|cosi|gia|puo|cioe|percio|fa)'", re.I)
bad = [(v['idx'], ACC.search(v['italian']).group(0)) for v in cov if ACC.search(v['italian'])]
ck('tipografia (accenti veri, nessun apostrofo al posto dell\'accento)', not bad, bad)
nonlat = [v['idx'] for v in cov for c in v['italian'] if ord(c) > 127 and not 0x00C0 <= ord(c) <= 0x024F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio (il tab iniziale dell\'unita\' 32 e\' ammesso)',
   not [v['idx'] for v in cov if v['italian'] != v['italian'].rstrip()
        or '  ' in v['italian'].strip(TAB) or v['english'] != v['english'].rstrip()])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck('il file ha 146 unita', db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0] == 146)
ck('lotto + residuo = file: 45 + 101 = 146',
   45 + db.execute('select count(*) from units where path=? and line>381', (PATH,)).fetchone()[0] == 146)
st = dict(db.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('le 45 unita sono PENDING (misurato)',
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
