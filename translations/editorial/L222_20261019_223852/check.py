r"""check.py — L222 (`data/successors/successor ships.txt`, 26 unita', righe 1141-1338). **Lotto terminale del file.**

Porta il file a **146/146**: `45 + 25 + 26 + 24 + 26 = 146`, **senza `UI_LABEL`** (questo file non ne ha).

**20 unita' su 26 identiche all'inglese** (18 `TEXT` + 2 `VALUE`), **6 `DESCRIPTION`** tradotte. I nomi sono generati dal
sorgente, non trascritti.

**Due coerenze**:
- le unita' **12 e 14** sono la stessa scheda della Vujlet, la seconda **senza** l'apertura participiale; il testo condiviso
  deve restare identico **e la differenza di punteggiatura va conservata** (la 12 dice «a corto raggio e relativamente
  vulnerabili, e le navi», la 14 «a corto raggio, relativamente vulnerabili, e le navi»);
- l'unita' **1** (Veusade) riprende la formula gia' resa in **L221 unita' 24**: «un progetto così specializzato rende queste
  navi inadatte all'uso polivalente, ma vengono spesso impiegate come unità ausiliarie o di polizia».
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
PATH = 'data/successors/successor ships.txt'
WINDOWS = [('L218_20261019_221520', 45), ('L219_20261019_222027', 25),
           ('L220_20261019_222539', 26), ('L221_20261019_223227', 24),
           ('L222_20261019_223852', 26)]
SHARED = ('una nave da guerra prodotta in serie dalle Alte Case, abbastanza flessibile da ricoprire una varietà di '
          'ruoli leggeri. Essendo abbastanza grande da operare come unità autosufficiente, questi vascelli costituiscono '
          'un ponte utile tra gli intercettori a corto raggio')
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
ck('tipi: 18 TEXT, 6 DESCRIPTION, 2 VALUE (asserzione scritta)',
   KINDS == {'TEXT': 18, 'DESCRIPTION': 6, 'VALUE': 2}, dict(KINDS))
ck('ZERO DIALOG, MISSION_TEXT, LOGBOOK, NEWS, UI_LABEL (asserzioni vuote scritte)',
   [u['idx'] for u in units if u['kind'] not in ('TEXT', 'DESCRIPTION', 'VALUE')] == [])
ck('3 contesti con le dimensioni misurate: Vujlet 13, Vujlet-Usaqri 12, Veusade 1',
   CTX == {'ship:Veusade': 1, 'ship:Vujlet': 13, 'ship:Vujlet-Usaqri': 12}, dict(CTX))
ck('righe 1141 e 1338 (prima e ultima del lotto e del file)',
   (cov[0]['line'], cov[-1]['line']) == (1141, 1338), (cov[0]['line'], cov[-1]['line']))
ck('2 tab, unita\' 13 e 26 (entrambe DESCRIPTION), identici nelle due lingue',
   [v['idx'] for v in cov if TAB in v['english']] == [13, 26]
   == [v['idx'] for v in cov if TAB in v['italian']]
   and all(by[i]['italian'].startswith(TAB) and not by[i]['italian'].startswith(TAB + TAB) for i in (13, 26)))
ck('36 virgolette: 2 per ognuna delle 18 TEXT e NESSUNA in prosa (misurato)',
   sum(EN_Q.values()) == 36 == sum(IT_Q.values()) and EN_Q == IT_Q
   and EN_Q == {i: 2 for i in TEXTS} and len(EN_Q) == 18, (EN_Q, IT_Q))
ck('NESSUN segnaposto (asserzione negativa scritta)',
   sum(len(TAG.findall(v['english'])) for v in cov) == 0
   == sum(len(TAG.findall(v['italian'])) for v in cov))
ck('20 unita\' IDENTICHE all\'inglese (18 TEXT + 2 VALUE) e 6 tradotte: sono esattamente le DESCRIPTION',
   sum(1 for v in cov if v['italian'] == v['english']) == 20
   and sorted(v['idx'] for v in cov if v['italian'] != v['english']) == DESCS,
   (sum(1 for v in cov if v['italian'] == v['english']),
    sorted(v['idx'] for v in cov if v['italian'] != v['english'])))
ck('i nomi sono COPIATI dal sorgente: 18 TEXT e 2 VALUE identici carattere per carattere',
   all(by[i]['italian'] == by[i]['english'] for i in TEXTS + VALS))
ck('COERENZA 12/14: il testo condiviso della Vujlet e\' identico nelle due schede',
   SHARED in by[12]['italian'] and SHARED in by[14]['italian'])
ck('COERENZA 12/14: la differenza di punteggiatura del sorgente e\' conservata',
   'a corto raggio e relativamente vulnerabili, e le navi' in by[12]['italian']
   and 'a corto raggio, relativamente vulnerabili, e le navi' in by[14]['italian']
   and by[12]['italian'].startswith('Con la grazia') and by[14]['italian'].startswith('La compatta Vujlet'))
ck("COERENZA con L221/24: la formula della Veusade usa la resa gia' fissata",
   "inadatte all'uso polivalente" in by[1]['italian']
   and 'unità ausiliarie o di polizia' in by[1]['italian'])
ck('terminologia: «Alte Case», «Nuove Case», «Casa Kaatrij», «Predecessori»; «High Houses» assente',
   'Alte Case' in IT_ALL and 'Nuove Case' in IT_ALL and 'Casa Kaatrij' in IT_ALL
   and 'Predecessori' in IT_ALL and 'High Houses' not in IT_ALL and 'New Houses' not in IT_ALL)
ck('le 6 DESCRIPTION sono tutte tradotte e tutte distinte',
   len(DESCS) == 6 and all(by[i]['italian'] != by[i]['english'] for i in DESCS)
   and len({by[i]['italian'] for i in DESCS}) == 6)
ck("apici: 5 in inglese (13 Predecessors', 25 x3 House's/ship's/cloak's, 26 Usaqri's) e 8 in italiano "
   "(1 x2, 13 x2, 25 x3, 26)",
   sum(n for _, n in EN_A) == 5 and sum(n for _, n in IT_A) == 8
   and EN_A == [(13, 1), (25, 3), (26, 1)] and IT_A == [(1, 2), (13, 2), (25, 3), (26, 1)], (EN_A, IT_A))
ck('registro: nessun «Lei» e nessun «mi scusi»',
   not re.search(r'\bLei\b|mi scusi', IT_ALL))
ck('nessun caporale e nessun carattere tipografico',
   not [v['idx'] for v in cov if any(c in v['italian'] for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026')])
DESC_TXT = ' '.join(by[i]['italian'] for i in DESCS)
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' you ', ' to the ', ' will be ',
        ' is ', ' are ', ' from the ', ' its ', ' it is ', ' such as ', ' rather than ', ' for a ', ' that ',
        ' have ', ' they ', ' their ', ' while ')
ck('nessun residuo inglese nelle DESCRIPTION',
   not [w for w in ENGW if w in DESC_TXT.lower()], [w for w in ENGW if w in DESC_TXT.lower()])
rs = [v['ratio'] for v in cov]
ck('rapporto nel gate 0,55-1,90 (nomi 1,00; DESCRIPTION 1,06-1,21)',
   0.55 < min(rs) and max(rs) < 1.90, '%.2f - %.2f' % (min(rs), max(rs)))
ACC = re.compile(r"\b(e|piu|perche|cosi|gia|puo|cioe|percio|fa)'", re.I)
bad = [(v['idx'], ACC.search(v['italian']).group(0)) for v in cov if ACC.search(v['italian'])]
ck('tipografia (accenti veri, nessun apostrofo al posto dell\'accento)', not bad, bad)
nonlat = [v['idx'] for v in cov for c in v['italian'] if ord(c) > 127 and not 0x00C0 <= ord(c) <= 0x024F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio (tab iniziali delle 13 e 26 ammessi)',
   not [v['idx'] for v in cov if v['italian'] != v['italian'].rstrip()
        or '  ' in v['italian'].strip(TAB) or v['english'] != v['english'].rstrip()])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
lines, per_win, wrong = [], {}, []
for w, n in WINDOWS:
    d = json.load(open(os.path.join(ED, w, 'translation.json'), encoding='utf-8'))['units']
    got = [u['line'] for u in d if u['path'] == PATH]
    per_win[w] = len(got)
    if len(got) != n:
        wrong.append((w, n, len(got)))
    lines += got
ck('cinque finestre reali: 45, 25, 26, 24, 26',
   list(per_win.values()) == [45, 25, 26, 24, 26] and not wrong, (per_win, wrong))
dbl = [r[0] for r in db.execute('select line from units where path=? order by line', (PATH,))]
ck('FILE CHIUSO: 146 righe tradotte distinte coprono i 146 del DB (nessun UI_LABEL nel file)',
   len(lines) == 146 == len(set(lines)) and sorted(set(lines)) == dbl,
   (len(lines), len(set(lines)), len(dbl)))
ck('la riga 1338 e\' l\'ultima del file e dopo non c\'e\' nulla',
   db.execute('select count(*) from units where path=? and line>1338', (PATH,)).fetchone()[0] == 0)
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
