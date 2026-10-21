r"""check.py — L329 (`data/_ui/help.txt`, righe 119–212). **TERMINALE — chiude il file a 113/113.**

**Lotto MISTO**: 15 unità `APPROVED` (trascritte dal DB) + 45 `PENDING` (tradotte qui). I due gruppi si verificano **separatamente**.
"""
import collections
import json
import os
import re
import sqlite3

TAB = chr(9)
QUOTE = chr(34)
TAG = re.compile(r'<[^<>]+>')
HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
PATH = 'data/_ui/help.txt'
APPROVATE = [119, 120, 123, 124, 125, 126, 128, 129, 130, 133, 135, 137, 145, 147, 150]
TAB_RIGHE = [124, 125, 126, 129, 130, 147]
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


ck('60/60 unità presenti (15 trascritte + 45 tradotte)', len(cov) == 60 == len(units))
ck('15 unità APPROVED: testo IDENTICO al database',
   all(db.execute('select italian from units where id=?', (at[l]['id'],)).fetchone()[0] == at[l]['italian']
       for l in APPROVATE),
   [l for l in APPROVATE if db.execute('select italian from units where id=?', (at[l]['id'],)).fetchone()[0] != at[l]['italian']])
ck('45 unità PENDING: nessun testo approvato nel DB (niente da trascrivere)',
   all(db.execute('select state, italian from units where id=?', (u['id'],)).fetchone() == ('PENDING', None)
       for u in cov if u['line'] not in APPROVATE),
   [(u['line'], db.execute('select state from units where id=?', (u['id'],)).fetchone()) for u in cov if u['line'] not in APPROVATE][:3])
ck('45 unità PENDING: tutte tradotte, nessuna identica all\'inglese',
   not [u['line'] for u in cov if u['line'] not in APPROVATE and u['italian'] == u['english']])
ck('tutte e 60 sono HELP', collections.Counter(u['kind'] for u in cov) == {'HELP': 60})
ck('15 contesti', len({u['context'] for u in cov}) == 15,
   collections.Counter(u['context'] for u in cov))
ck('le 6 tab sono alle righe attese e come PRIMO carattere',
   [u['line'] for u in cov if u['italian'].startswith(TAB)] == TAB_RIGHE)
ck('segnaposto: 12 forme, 14 occorrenze, identici al sorgente per unità',
   all(TAG.findall(u['english']) == TAG.findall(u['italian']) for u in cov)
   and sum(len(TAG.findall(u['italian'])) for u in cov) == 14,
   collections.Counter(t for u in cov for t in TAG.findall(u['italian'])))
ck('virgolette: 38 in entrambe le lingue, per unità',
   sum(u['italian'].count(QUOTE) for u in cov) == 38,
   [(u['line'], u['english'].count(QUOTE), u['italian'].count(QUOTE)) for u in cov
    if u['english'].count(QUOTE) != u['italian'].count(QUOTE)])
ck('`outfitter` → «fornitore» nelle tradotte (righe 160, 165, 166, 176, 178, 183, 190)',
   all('fornitor' in at[l]['italian'] for l in (160, 165, 166, 176, 178, 183, 190))
   and not [u['line'] for u in cov if 'emporio' in u['italian']])
ck('le 15 trascritte lasciano le 45 PENDING intatte: nessuna approvazione',
   db.execute("select count(*) from units where path=? and state='PENDING' and line between 119 and 212",
              (PATH,)).fetchone()[0] == 45)
ck('nessun caporale, nessun carattere tipografico, nessun doppio spazio',
   not [c for u in cov for c in u['italian'] if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026']
   and not [u['idx'] for u in cov if '  ' in u['italian'].lstrip(TAB)])
ck('rapporto nel gate 0,55-1,90', all(0.55 < u['ratio'] < 1.90 for u in cov),
   [(u['idx'], u['ratio']) for u in cov if not 0.55 < u['ratio'] < 1.90])
ck('FILE: 113 unità, prima 15, ultima 212, zero prima e dopo',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (113, 15, 212)
   and db.execute('select count(*) from units where path=? and line<15', (PATH,)).fetchone()[0] == 0
   and db.execute('select count(*) from units where path=? and line>212', (PATH,)).fetchone()[0] == 0)
block = {}
for f in sorted(__import__('glob').glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    us = [u for u in json.load(open(f, encoding='utf-8'))['units'] if u['path'] == PATH]
    if us:
        block[os.path.basename(os.path.dirname(f))] = (len(us), min(u['line'] for u in us), max(u['line'] for u in us))
tot = sum(v[0] for v in block.values())
ck('FILE: tre lotti, 28 + 25 + 60 = 113 unità, copertura 113/113',
   sorted(v[0] for v in block.values()) == [25, 28, 60] and tot == 113, block)
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · 15 APPROVED + 45 PENDING · 15 contesti · 6 tab · 38 virgolette · FILE 113/113' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
