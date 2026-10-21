r"""check.py — L264 (`data/remnant/remnant jobs.txt`, righe 703-741). **LOTTO TERMINALE**: chiude il file a 87/87.

Chiude la sottotrama del soccorso (`Rescue 5`) e apre un lavoro nuovo, `Disable 1`: la **Dathnak A'awoj** va **disabilitata
senza distruggerla**, perche' ha a bordo una popolazione civile. Il `check.py` verifica che i due verbi restino distinti:
«disabilitare» e' il compito, «distruggere» e' il **fallimento** (unita' 8).

**Invariante di FILE**: `25 + 29 + 24 + 9 = 87` unita', 87 righe distinte, **741** ultima riga, **0** dopo.
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
TAG = re.compile(r'<[^<>]+>')
HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
PATH = 'data/remnant/remnant jobs.txt'
src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
units = sorted(src['units'], key=lambda x: x['line'])
tr = {}
for p in sorted(f for f in os.listdir(os.path.join(HERE, 'parts')) if f.endswith('.json')):
    for k, v in json.load(open(os.path.join(HERE, 'parts', p), encoding='utf-8')).items():
        tr[int(k)] = v
out = {'block': src['block'], 'note': src['note'], 'units': []}
for u in units:
    if u['idx'] in tr:
        it = tr[u['idx']]
        out['units'].append({"idx": u['idx'], "id": u['id'], "path": u['path'], "line": u['line'],
                             "kind": u['kind'], "context": u['context'], "english": u['english'],
                             "italian": it, "ratio": round(len(it) / max(1, len(u['english'])), 3)})
open(os.path.join(HERE, 'translation.json'), 'w', encoding='utf-8').write(
    json.dumps(out, ensure_ascii=False, indent=1))
cov = out['units']
by = {u['idx']: u for u in cov}
CTX_A, CTX_B = 'mission:Remnant: Rescue 5', 'mission:Remnant: Disable 1'
TOK = {'<payment>': 3, '<planet>': 3, '<npc>': 2}
APOS_EN = {3: 1, 4: 1, 5: 1, 6: 2, 8: 1, 9: 1}
APOS_IT = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 8: 1, 9: 1}
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck('unita tradotte 9/9', len(cov) == 9 == len(units), '%d/%d' % (len(cov), len(units)))
ck('tipi: 5 DIALOG + 2 MISSION_TEXT + 1 VALUE + 1 DESCRIPTION',
   collections.Counter(u['kind'] for u in units)
   == {'DIALOG': 5, 'MISSION_TEXT': 2, 'VALUE': 1, 'DESCRIPTION': 1},
   dict(collections.Counter(u['kind'] for u in units)))
ck('due contesti, in sequenza: Rescue 5 (1-2) poi Disable 1 (3-9)',
   [by[1]['context'], by[2]['context'], by[3]['context']] == [CTX_A, CTX_A, CTX_B]
   and collections.Counter(u['context'] for u in cov) == {CTX_A: 2, CTX_B: 7},
   dict(collections.Counter(u['context'] for u in cov)))
ck('righe 703-741, la 741 e l ultima del lotto',
   [u['line'] for u in cov] == sorted({u['line'] for u in cov})
   and cov[0]['line'] == 703 and cov[-1]['line'] == 741)
ck('il VALUE e COPIATO (nome del lavoro, con l apice di A\'awoj)',
   by[3]['kind'] == 'VALUE' and by[3]['italian'] == by[3]['english'] == "Disable Damaged Dathnak A'awoj")
ck('le altre 8 unita sono TRADOTTE, nessuna copiata',
   all(u['italian'] != u['english'] for u in cov if u['kind'] != 'VALUE'),
   [u['idx'] for u in cov if u['kind'] != 'VALUE' and u['italian'] == u['english']])
ck('ZERO tab e ZERO virgolette in entrambe le lingue (asserzioni negative)',
   sum(u['english'].count(TAB) + u['italian'].count(TAB) for u in cov) == 0
   and sum(u['english'].count(QUOTE) + u['italian'].count(QUOTE) for u in cov) == 0)
ck('APICI: 7 in inglese (6 dal nome A\'awoj, 1 da `You\'ve`), 8 in italiano, mappe dichiarate',
   {u['idx']: u['english'].count(APOS) for u in cov if APOS in u['english']} == APOS_EN
   and {u['idx']: u['italian'].count(APOS) for u in cov if APOS in u['italian']} == APOS_IT,
   ({u['idx']: u['english'].count(APOS) for u in cov if APOS in u['english']},
    {u['idx']: u['italian'].count(APOS) for u in cov if APOS in u['italian']}))
ck('SEGNAPOSTO: 8 in 3 famiglie, e ORDINE identico per unita',
   collections.Counter(t for u in cov for t in TAG.findall(u['english'])) == TOK
   == collections.Counter(t for u in cov for t in TAG.findall(u['italian']))
   and not [u['idx'] for u in cov if TAG.findall(u['english']) != TAG.findall(u['italian'])],
   [u['idx'] for u in cov if TAG.findall(u['english']) != TAG.findall(u['italian'])])
ck('il compito e DISABILITARE, non distruggere: «distruggere» compare solo nel ramo del fallimento (8)',
   'disabilitarla' in by[4]['italian'] and 'disabilitato' in by[5]['italian']
   and 'disabilitala' in by[6]['italian'] and 'disabilitato' in by[9]['italian']
   and [u['idx'] for u in cov if 'distrugger' in u['italian']] == [8],
   [u['idx'] for u in cov if 'distrugger' in u['italian']])
ck('il motivo e la popolazione civile: «popolazione civile» e «massacro» nella scheda',
   'popolazione civile' in by[4]['italian'] and 'massacro' in by[4]['italian'])
ck('luoghi e nomi: Postverta, Dathnak A\'awoj, le Braci',
   'Postverta' in by[4]['italian'] and by[4]['italian'].count("A'awoj") == 1
   and 'Braci' in by[1]['italian'])
ck('grado: `prefect` -> «prefetto», e «compenso logistico» come nei lotti precedenti',
   'prefetto militare' in by[9]['italian'] and 'compenso logistico' in by[9]['italian']
   and 'compenso logistico' in by[4]['italian'])
ck('nessun caporale, nessun carattere tipografico',
   not [u['idx'] for u in cov for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026' if c in u['italian']])
nonlat = [(u['idx'], c) for u in cov for c in u['italian'] if ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']],
   [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90',
   all(0.55 < u['ratio'] < 1.90 for u in cov),
   [(u['idx'], u['ratio']) for u in cov if not 0.55 < u['ratio'] < 1.90])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("78 unita' prima (L261-L263), e l'ultima prima della 703 e in `Rescue 5`",
   db.execute('select count(*) from units where path=? and line<703', (PATH,)).fetchone()[0] == 78
   and db.execute('select context from units where path=? and line<703 order by line desc limit 1', (PATH,)).fetchone()
   == (CTX_A,))
ck("ZERO unita' dopo la 741: il lotto CHIUDE il file",
   db.execute('select count(*) from units where path=? and line>741', (PATH,)).fetchone()[0] == 0)
ck("la 741 e la riga massima del file, che ha 87 unita' fra la 19 e la 741",
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (87, 19, 741))
righe, lotti = set(), []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    us = [u for u in json.load(open(f, encoding='utf-8'))['units'] if u['path'] == PATH]
    if us:
        lotti.append((os.path.basename(os.path.dirname(f)), len(us)))
        righe |= {u['line'] for u in us}
ck('INVARIANTE DI FILE: 25 + 29 + 24 + 9 = 87 unita in 4 lotti',
   [n for _, n in lotti] == [25, 29, 24, 9] and sum(n for _, n in lotti) == 87 == len(righe),
   (lotti, len(righe)))
ck('le 87 righe dei lotti sono esattamente quelle del database (nessun buco)',
   righe == {l for l, in db.execute('select line from units where path=?', (PATH,))})
st = dict(db.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('tutte le 9 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d' % (sum(len(v['english'].split()) for v in cov),
                                sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
