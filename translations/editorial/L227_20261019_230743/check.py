r"""check.py — L227 (`data/remnant/remnant outfits.txt`, 10 unita', righe 884-979). **Lotto terminale del file.**

Porta il file a **57/57**: `12 + 13 + 11 + 11 + 10 = 57`.

**Torna un'unita' da copiare.** Dopo due lotti con **0 identiche** (L224, L225, L226), qui il `VALUE` della riga 948
(`Void Sprite Parts`) riporta il confronto a **1 identica / 9 tradotte**. Non e' un'incoerenza: e' la composizione del file
(55 `DESCRIPTION` + 2 `VALUE`), e il controllo lo asserisce in modo esplicito in entrambe le direzioni.

**Zero virgolette**, come in L226: asserzione su un numero zero, in inglese e in italiano.

**L'ultima unita' non e' un equipaggiamento**: `Remnant Capital License` e' una licenza, e la sua scheda descrive un
dispositivo di richiesta soccorso — registro diverso dagli altri nove testi.
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
PATH = 'data/remnant/remnant outfits.txt'
WINDOWS = [('L223_20261019_224448', 12), ('L224_20261019_224956', 13),
           ('L225_20261019_225556', 11), ('L226_20261019_230148', 11),
           ('L227_20261019_230743', 10)]
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
VALS = [u['idx'] for u in units if u['kind'] == 'VALUE']
DESCS = [u['idx'] for u in units if u['kind'] == 'DESCRIPTION']
EN_A = [(v['idx'], v['english'].count(APOS)) for v in cov if APOS in v['english']]
IT_A = [(v['idx'], v['italian'].count(APOS)) for v in cov if APOS in v['italian']]
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 10/10", len(cov) == 10 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 9 DESCRIPTION, 1 VALUE (asserzione scritta)', KINDS == {'DESCRIPTION': 9, 'VALUE': 1}, dict(KINDS))
ck('ZERO TEXT, DIALOG, MISSION_TEXT, LOGBOOK, NEWS, UI_LABEL (asserzioni vuote scritte)',
   [u['idx'] for u in units if u['kind'] not in ('DESCRIPTION', 'VALUE')] == [])
ck('7 contesti: Void Sprite Parts 3 (con il VALUE), Void Rifle 2, gli altri 1',
   len(CTX) == 7 and CTX == {'outfit:Forge-Class Steering': 1, 'outfit:Smelter-Class Steering': 1,
                             'outfit:Tuning Rifle': 1, 'outfit:Void Rifle': 2,
                             'outfit:Void Sprite Parts': 3, 'outfit:Remnant License': 1,
                             'outfit:Remnant Capital License': 1}, dict(CTX))
ck('righe 884 e 979 (prima e ultima del lotto e del file)',
   (cov[0]['line'], cov[-1]['line']) == (884, 979), (cov[0]['line'], cov[-1]['line']))
ck('2 tab, nelle unita\' 5 e 8, identici nelle due lingue',
   [v['idx'] for v in cov if TAB in v['english']] == [5, 8]
   == [v['idx'] for v in cov if TAB in v['italian']])
ck('ZERO virgolette in inglese e in italiano: asserzione su un numero zero',
   sum(v['english'].count(QUOTE) for v in cov) == 0 == sum(v['italian'].count(QUOTE) for v in cov))
ck('NESSUN segnaposto (asserzione negativa scritta)',
   sum(len(TAG.findall(v['english'])) for v in cov) == 0 == sum(len(TAG.findall(v['italian'])) for v in cov))
ck('1 unita\' IDENTICA all\'inglese (il VALUE) e 9 tradotte: torna il confronto 1 / 9',
   sum(1 for v in cov if v['italian'] == v['english']) == 1
   and VALS == [6] and by[6]['italian'] == by[6]['english'] == 'Void Sprite Parts'
   and all(by[i]['italian'] != by[i]['english'] for i in DESCS),
   (sum(1 for v in cov if v['italian'] == v['english']), VALS))
ck('terminologia: «void sprite», «Archon», «Void Rifle», «IFF» invariati; «rifiuti»/«rifugi» non confusi',
   'void sprite' in IT_ALL and "l'Archon" in IT_ALL and 'Void Rifle' in IT_ALL
   and 'IFF' in IT_ALL and 'rifugi' in IT_ALL)
ck('nessun residuo inglese di struttura (the, of the, and, with, their)',
   not [w for w in (' the ', ' of the ', ' and ', ' with ', ' their ', ' while ', ' that they ')
        if w in IT_ALL.lower()],
   [w for w in (' the ', ' of the ', ' and ', ' with ', ' their ', ' while ', ' that they ') if w in IT_ALL.lower()])
ck("apici: 3 in inglese (2 It's+Remnant's, 10 Remnant's) e 7 in italiano in 5 unita'",
   sum(n for _, n in EN_A) == 3 and sum(n for _, n in IT_A) == 7
   and EN_A == [(2, 2), (10, 1)]
   and IT_A == [(1, 1), (4, 1), (5, 2), (7, 1), (10, 2)], (EN_A, IT_A))
ck('registro: nessun «Lei» e nessun «mi scusi»', not re.search(r'\bLei\b|mi scusi', IT_ALL))
ck('nessun caporale e nessun carattere tipografico',
   not [v['idx'] for v in cov if any(c in v['italian'] for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026')])
rs = [v['ratio'] for v in cov]
ck('rapporto nel gate 0,55-1,90 (0,84 - 1,11: qui l\'italiano e\' piu\' corto, 376 parole contro 382)',
   0.55 < min(rs) and max(rs) < 1.90, '%.2f - %.2f' % (min(rs), max(rs)))
ACC = re.compile(r"\b(e|piu|perche|cosi|gia|puo|cioe|percio|fa)'", re.I)
bad = [(v['idx'], ACC.search(v['italian']).group(0)) for v in cov if ACC.search(v['italian'])]
ck('tipografia (accenti veri, nessun apostrofo al posto dell\'accento)', not bad, bad)
nonlat = [v['idx'] for v in cov for c in v['italian'] if ord(c) > 127 and not 0x00C0 <= ord(c) <= 0x024F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio (tab iniziali delle 5 e 8 ammessi)',
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
ck('cinque finestre reali: 12, 13, 11, 11, 10',
   list(per_win.values()) == [12, 13, 11, 11, 10] and not wrong, (per_win, wrong))
dbl = [r[0] for r in db.execute('select line from units where path=? order by line', (PATH,))]
ck('FILE CHIUSO: 57 righe tradotte distinte coprono i 57 del DB (nessun UI_LABEL nel file)',
   len(lines) == 57 == len(set(lines)) and sorted(set(lines)) == dbl,
   (len(lines), len(set(lines)), len(dbl)))
ck('la riga 979 e\' l\'ultima del file e dopo non c\'e\' nulla',
   db.execute('select count(*) from units where path=? and line>979', (PATH,)).fetchone()[0] == 0)
st = dict(db.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('le 10 unita sono PENDING (misurato)',
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
