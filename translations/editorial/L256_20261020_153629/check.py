r"""check.py — L256 (`data/human/post-war reactions.txt`, righe 40-74). Primo lotto del file: 22 MISSION_TEXT di dialogo.

Il lotto e' un **dialogo** con due gemelli capitani: per questo i controlli tipografici non sono un dettaglio ma il cuore del
lotto — **21 tab** di rientro, **34 virgolette** dritte e **19 apici** inglesi (9 in italiano) da conservare **per unita'**:
un totale uguale non prova che nessuna sia stata spostata.

`Admiral Danforts` (riga 73) e' un **errore voluto** del gemello, corretto alla riga 74: la resa lo conserva e lo fa
correggere, altrimenti la battuta perderebbe il suo senso.
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
PATH = 'data/human/post-war reactions.txt'
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
TOK_EN = collections.Counter(t for v in cov for t in TAG.findall(v['english']))
TOK_IT = collections.Counter(t for v in cov for t in TAG.findall(v['italian']))
QUOTES = {i: 2 for i in (2, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22)}
APOS_EN = {1: 1, 4: 3, 5: 2, 6: 4, 10: 1, 11: 1, 13: 3, 16: 1, 17: 1, 19: 2}
APOS_IT = {1: 1, 5: 2, 6: 2, 7: 1, 10: 1, 13: 2}
TABBED = list(range(2, 23))
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck('unita tradotte 22/22', len(cov) == 22 == len(units), '%d/%d' % (len(cov), len(units)))
ck('tipo: 22 MISSION_TEXT', collections.Counter(u['kind'] for u in units) == {'MISSION_TEXT': 22},
   dict(collections.Counter(u['kind'] for u in units)))
ck("contesto unico: mission:War Reactions: Asteroid Miners",
   {u['context'] for u in cov} == {'mission:War Reactions: Asteroid Miners'},
   sorted({u['context'] for u in cov}))
ck('righe 40-74, nessun buco interno',
   [u['line'] for u in cov] == sorted({u['line'] for u in cov}) and cov[0]['line'] == 40 and cov[-1]['line'] == 74)
ck('tutte TRADOTTE, nessuna copiata', not [u for u in cov if u['italian'] == u['english']],
   [u['idx'] for u in cov if u['italian'] == u['english']])
ck('ZERO segnaposto in inglese e in italiano (asserzione negativa)',
   not TOK_EN and not TOK_IT, (dict(TOK_EN), dict(TOK_IT)))
ck('TAB: 21 in inglese, 21 in italiano, e **le stesse unita** rientrate',
   sum(u['english'].count(TAB) for u in cov) == 21 == sum(u['italian'].count(TAB) for u in cov)
   and [u['idx'] for u in cov if TAB in u['english']] == TABBED
   and [u['idx'] for u in cov if TAB in u['italian']] == TABBED,
   ([u['idx'] for u in cov if TAB in u['english']], [u['idx'] for u in cov if TAB in u['italian']]))
ck('il tab e il PRIMO carattere, dove c\'e\' (rientro della battuta)',
   all(u['italian'].startswith(TAB) for u in cov if u['idx'] in TABBED)
   and not by[1]['italian'].startswith(TAB))
ck('VIRGOLETTE: 34 in inglese, 34 in italiano, per unita identiche',
   {u['idx']: u['english'].count(QUOTE) for u in cov if QUOTE in u['english']} == QUOTES
   == {u['idx']: u['italian'].count(QUOTE) for u in cov if QUOTE in u['italian']},
   ({u['idx']: u['english'].count(QUOTE) for u in cov if QUOTE in u['english']},
    {u['idx']: u['italian'].count(QUOTE) for u in cov if QUOTE in u['italian']}))
ck('APICI: 19 in inglese (10 unita), 9 in italiano (7 unita), elenco per unita',
   {i: u['english'].count(APOS) for i, u in by.items() if APOS in u['english']} == APOS_EN
   and {i: u['italian'].count(APOS) for i, u in by.items() if APOS in u['italian']} == APOS_IT,
   ({i: u['english'].count(APOS) for i, u in by.items() if APOS in u['english']},
    {i: u['italian'].count(APOS) for i, u in by.items() if APOS in u['italian']}))
ck('nessun caporale e nessun carattere tipografico',
   not [u['idx'] for u in cov for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026' if c in u['italian']])
nonlat = [(u['idx'], c) for u in cov for c in u['italian'] if ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']],
   [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90 (0,83-1,32)',
   all(0.55 < u['ratio'] < 1.90 for u in cov),
   [(u['idx'], u['ratio']) for u in cov if not 0.55 < u['ratio'] < 1.90])
ck('lessico: «Marina» per Navy, «Sindacato» per Syndicate',
   'Marina' in by[10]['italian'] and 'Sindacato' in by[6]['italian']
   and 'Navy' not in by[10]['italian'] and 'Syndicate' not in by[6]['italian'])
ck('nomi propri invariati: Pug, Danforth, Maduena Kabiru, Bounty',
   all(w in ' '.join(u['italian'] for u in cov) for w in ('Pug', 'Danforth', 'Maduena Kabiru', 'Bounty')))
ck('il refuso voluto `Danforts` (riga 73) resta e viene corretto alla 74',
   'Danforts' in by[21]['italian'] and 'Danforts' not in by[22]['italian'] and 'Danforth' in by[22]['italian'],
   (by[21]['italian'][:40], by[22]['italian'][:40]))
ck('nessun residuo inglese di struttura nelle battute',
   not [u['idx'] for u in cov for w in (' the ', ' and ', ' you ', ' of ') if w in u['italian'].lower()],
   [(u['idx'], w) for u in cov for w in (' the ', ' and ', ' you ', ' of ') if w in u['italian'].lower()])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("ZERO unita' prima della 40: il lotto APRE il file",
   db.execute('select count(*) from units where path=? and line<40', (PATH,)).fetchone()[0] == 0)
ck("65 unita' dopo la 74", db.execute('select count(*) from units where path=? and line>74', (PATH,)).fetchone()[0] == 65)
ck('il file ha 87 unita, righe 40-264',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (87, 40, 264))
st = dict(db.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('tutte le 22 unita sono PENDING',
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
