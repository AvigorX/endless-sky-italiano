r"""check.py — L332 (`data/human/south jobs.txt`, 15–347). **TERMINALE, FILE INTERO.** 40 unità, quattro tipi."""
import collections
import glob
import json
import os
import re
import sqlite3

TAB = chr(9)
HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
PATH = 'data/human/south jobs.txt'
TOKEN = {'<system>': 6, '<planet>': 20, '<date>': 4, '<payment>': 18,
         '<destination>': 7, '<tons>': 2, '<fare>': 2, '<cargo>': 7}
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
kind = collections.Counter(u['kind'] for u in cov)
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else 'FAIL'), c))


ck('40/40 unità tradotte', len(cov) == 40 == len(units))
ck('quattro tipi: 14 VALUE + 14 DESCRIPTION + 8 DIALOG + 4 CONVERSATION',
   kind == {'VALUE': 14, 'DESCRIPTION': 14, 'DIALOG': 8, 'CONVERSATION': 4}, kind)
ck('15 contesti, 2 tab (133, 135) come primo carattere',
   len({u['context'] for u in cov}) == 15
   and [u['line'] for u in cov if u['italian'].startswith(TAB)] == [133, 135])
ck('segnaposto: 52 in 8 forme, identici per unità',
   all(re.findall(r'<[^<>]+>', u['english']) == re.findall(r'<[^<>]+>', u['italian']) for u in cov)
   and collections.Counter(t for u in cov for t in re.findall(r'<[^<>]+>', u['italian'])) == TOKEN,
   collections.Counter(t for u in cov for t in re.findall(r'<[^<>]+>', u['italian'])))
ck('VIRGOLETTE: 2 (solo la conversazione 131)',
   sum(u['italian'].count('"') for u in cov) == 2 and at[131]['italian'].count('"') == 2)
ck('VALUE: i titoli sono tradotti (Consegna, Spedizione, Trasporto passeggeri, Pirati)',
   all(u['italian'] != u['english'] for u in cov if u['kind'] == 'VALUE')
   and at[15]['italian'] == at[53]['italian'] == at[92]['italian'] == 'Pirati che occupano <system>'
   and at[142]['italian'] == at[163]['italian'] == 'Consegna a <planet>'
   and at[186]['italian'] == at[208]['italian'] == 'Trasporto passeggeri a <planet>'
   and {at[l]['italian'] for l in (230, 250, 270, 289, 308, 327, 346)} == {'Spedizione a <planet>'})
ck('DESCRIPTION: la scala dei pirati è piccola < banda < grande banda',
   'Una piccola banda' in at[18]['italian'] and 'Una banda di pirati' in at[56]['italian']
   and 'Una grande banda' in at[95]['italian'])
ck('DESCRIPTION: <tons>, <fare>, <cargo> non diventano parole italiane',
   '<tons>' in at[145]['italian'] and '<fare>' in at[189]['italian'] and '<cargo>' in at[231]['italian'])
ck('DIALOG: le due coppie sono identiche al loro interno',
   at[155]['italian'] == at[176]['italian'] and at[160]['italian'] == at[181]['italian']
   and at[200]['italian'] == at[222]['italian'] and at[205]['italian'] == at[227]['italian'])
ck('CONVERSATION: la battuta porta i tre segnaposto e la scelta è fra due opzioni',
   all(f'<{t}>' in at[131]['italian'] for t in ('destination', 'date', 'planet'))
   and at[133]['italian'].startswith(TAB) and at[135]['italian'].startswith(TAB)
   and at[133]['italian'].strip('(').strip(')') != at[135]['italian'].strip('(').strip(')'))
ck('nomi delle ditte invariati: Delta V Corporation, Tarazed Shipyards, Tarazed Systems',
   all(n in ''.join(u['italian'] for u in cov) for n in
       ('Delta V Corporation', 'Tarazed Shipyards', 'Tarazed Systems')))
ck('`Southern Rim` reso «Bordo Meridionale» (il corpus usa «Bordo»)',
   'Bordo Meridionale' in at[231]['italian'])
ck('nessuna unità identica all inglese, nessun caporale o doppio spazio',
   not [u for u in cov if u['italian'] == u['english']]
   and not [c for u in cov for c in u['italian'] if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026']
   and not [u['idx'] for u in cov if '  ' in u['italian'].lstrip(TAB)])
ck('rapporto nel gate 0,55-1,90', all(0.55 < u['ratio'] < 1.90 for u in cov),
   [(u['idx'], u['ratio']) for u in cov if not 0.55 < u['ratio'] < 1.90])
ck('FILE: 40 unità, righe 15–347, zero prima e dopo',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (40, 15, 347)
   and db.execute('select count(*) from units where path=? and (line<15 or line>347)', (PATH,)).fetchone()[0] == 0)
ck('FILE: copertura 40/40, un solo lotto',
   db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0] == 40
   and sum(1 for f in glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))
           if any(u['path'] == PATH for u in json.load(open(f, encoding='utf-8'))['units'])) == 1)
ck('tutte le 40 unità restano PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · 14 VALUE + 14 DESCRIPTION + 8 DIALOG + 4 CONVERSATION · 66 segnaposto · FILE 40/40' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
