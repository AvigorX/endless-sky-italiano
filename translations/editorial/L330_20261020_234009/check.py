r"""check.py — L330 (`data/wanderer/wanderers.txt`, righe 778–1042). **TERMINALE, FILE INTERO.** 15 unità `PENDING`, tutte tradotte."""
import collections
import glob
import json
import os
import re
import sqlite3

TAB = chr(9)
HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
PATH = 'data/wanderer/wanderers.txt'
TAB_RIGHE = [884, 999, 1001, 1041]
APICI_EN = {778: 1, 885: 1, 897: 1, 1040: 1}
NOMI = ['Unfettered', 'Wanderer', 'Mereti', 'Hai', 'Korath', "Varu K'est"]
src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
units = sorted(src['units'], key=lambda x: x['line'])
hits = {}
for p in sorted(f for f in os.listdir(os.path.join(HERE, 'parts')) if f.endswith('.json')):
    for k, v in json.load(open(os.path.join(HERE, 'parts', p), encoding='utf-8')).items():
        hits[int(k)] = v
out = {'block': src['block'], 'note': src['note'], 'units': []}
for u in units:
    it = hits[u['idx']]
    out['units'].append({"idx": u['idx'], "id": u['id'], "path": u['path'], "line": u['line'],
                         "kind": u['kind'], "context": u['context'], "english": u['english'],
                         "italian": it, "ratio": round(len(it) / max(1, len(u['english'])), 3)})
open(os.path.join(HERE, 'translation.json'), 'w', encoding='utf-8').write(
    json.dumps(out, ensure_ascii=False, indent=1))
cov = out['units']
at = {u['line']: u for u in cov}
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else 'FAIL'), c))


ck('15/15 unità tradotte', len(cov) == 15 == len(units))
ck('14 DESCRIPTION + 1 MISSION_TEXT',
   collections.Counter(u['kind'] for u in cov) == {'DESCRIPTION': 14, 'MISSION_TEXT': 1})
ck('4 contesti: more systems lost 7, spera anatrusk 3, desi seledrak 3, invasion 2',
   collections.Counter(u['context'] for u in cov) == {
       'event:wanderers: more systems lost': 7, 'event:wanderers: spera anatrusk colony': 3,
       'event:wanderers: desi seledrak': 3, 'event:wanderers: unfettered invasion starts': 2},
   collections.Counter(u['context'] for u in cov))
ck('le 4 tab sono alle righe attese e come primo carattere',
   [u['line'] for u in cov if u['italian'].startswith(TAB)] == TAB_RIGHE)
ck('nessuna virgoletta, nessun segnaposto, nessuna alternativa (asserzioni vuote)',
   sum(u['italian'].count('"') for u in cov) == 0
   and not re.findall(r'<[^<>]+>', ''.join(u['italian'] for u in cov))
   and not re.findall(r'\[[^\]]*\]', ''.join(u['italian'] for u in cov)))
ck('4 apici inglesi su 4 unità, nomi propri compresi (Varu K est)',
   {u['line']: u['english'].count(chr(39)) for u in cov if u['english'].count(chr(39))} == APICI_EN
   and "Varu K'est" in at[778]['italian'])
ck('i nomi delle fazioni restano invariati',
   all(n in ''.join(u['italian'] for u in cov) for n in NOMI))
ck('nessuna unità identica all inglese', not [u for u in cov if u['italian'] == u['english']])
ck('nessun caporale, nessun carattere tipografico, nessun doppio spazio',
   not [c for u in cov for c in u['italian'] if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026']
   and not [u['idx'] for u in cov if '  ' in u['italian'].lstrip(TAB)])
ck('rapporto nel gate 0,55-1,90', all(0.55 < u['ratio'] < 1.90 for u in cov),
   [(u['idx'], u['ratio']) for u in cov if not 0.55 < u['ratio'] < 1.90])
ck('FILE: 15 unità, righe 778–1042, zero prima e dopo',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (15, 778, 1042)
   and db.execute('select count(*) from units where path=? and (line<778 or line>1042)', (PATH,)).fetchone()[0] == 0)
ck('FILE: copertura 15/15, un solo lotto',
   db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0] == 15
   and sum(1 for f in glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))
           if any(u['path'] == PATH for u in json.load(open(f, encoding='utf-8'))['units'])) == 1)
ck('tutte le 15 unità restano PENDING (nessuna approvazione)',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · 14 DESCRIPTION + 1 MISSION_TEXT · 4 contesti · 4 tab · FILE 15/15' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
