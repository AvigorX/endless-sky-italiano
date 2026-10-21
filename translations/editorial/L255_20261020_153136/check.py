r"""check.py — L255 (`data/wanderer/wanderer jobs.txt`, 1 unita', riga 891). **LOTTO TERMINALE**: chiude il file.

**Una unita' sola non e' un lotto senza controlli**: tipo, traduzione, segnaposto, tab/virgolette/apici a zero, rapporto, e
l'**invariante di FILE** (`26 + 24 + 41 + 1 = 92`).

Il testo e' la chiusura della missione `Wanderers to Kor Efreti` iniziata in L254:
`When you return, the Wanderers thank you for taking them to the Kor Efreti and hand you <payment> before disembarking.`
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
PATH = 'data/wanderer/wanderer jobs.txt'
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
U = cov[0]
TOK_EN = collections.Counter(t for v in cov for t in TAG.findall(v['english']))
TOK_IT = collections.Counter(t for v in cov for t in TAG.findall(v['italian']))
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotta 1/1", len(cov) == 1 == len(units), '%d/%d' % (len(cov), len(units)))
ck('tipo: 1 DIALOG', collections.Counter(u['kind'] for u in units) == {'DIALOG': 1},
   dict(collections.Counter(u['kind'] for u in units)))
ck('contesto: mission:Wanderers to Kor Efreti (lo stesso di L254)',
   U['context'] == 'mission:Wanderers to Kor Efreti', U['context'])
ck('riga 891 (unica del lotto)', U['line'] == 891, U['line'])
ck("e' TRADOTTA, non copiata", U['italian'] != U['english'] and U['italian'].startswith('Al ritorno'))
ck('il segnaposto `<payment>` c\'e\' ed e\' al suo posto',
   TOK_EN == TOK_IT == collections.Counter({'<payment>': 1}), (dict(TOK_EN), dict(TOK_IT)))
ck('ZERO tab, ZERO virgolette, ZERO apici in entrambe le lingue',
   sum(v['english'].count(TAB) for v in cov) == 0 == sum(v['italian'].count(TAB) for v in cov)
   and sum(v['english'].count(QUOTE) for v in cov) == 0 == sum(v['italian'].count(QUOTE) for v in cov)
   and sum(v['english'].count(APOS) for v in cov) == 0 == sum(v['italian'].count(APOS) for v in cov))
ck('lessico: «Wanderer» invariato, «Kor Efreti» invariato, nessun `Unfettered`',
   'Wanderer' in U['italian'] and 'Kor Efreti' in U['italian']
   and 'Unfettered' not in U['italian'] and 'Wanderers' not in U['italian'])
ck('nessun residuo inglese di struttura (the, and, you, them, when)',
   not [w for w in (' the ', ' and ', ' you ', ' them ', ' when ' or ' When ') if w in U['italian'].lower()],
   [w for w in (' the ', ' and ', ' you ', ' them ') if w in U['italian'].lower()])
ck('nessun caporale e nessun carattere tipografico',
   not any(c in U['italian'] for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026'))
ck('rapporto nel gate 0,55-1,90 (0,98; 20 -> 19 parole)',
   0.55 < U['ratio'] < 1.90, U['ratio'])
nonlat = [c for c in U['italian'] if ord(c) > 127 and not 0x00C0 <= ord(c) <= 0x024F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio',
   U['italian'] == U['italian'].rstrip() and '  ' not in U['italian'])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("91 unita' prima della 891: L252 (26) + L253 (24) + L254 (41)",
   db.execute('select count(*) from units where path=? and line<891', (PATH,)).fetchone()[0] == 91)
ck("ZERO unita' dopo la 891: il lotto CHIUDE il file",
   db.execute('select count(*) from units where path=? and line>891', (PATH,)).fetchone()[0] == 0)
ck("la 891 e' l'ultima riga del file (92 unita', righe 15 - 891)",
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (92, 15, 891))
ck("INVARIANTE DI FILE: 26 + 24 + 41 + 1 = 92", 26 + 24 + 41 + 1 == 92 == len(units) + 91)
st = dict(db.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck("l'unita e' PENDING (misurato)",
   db.execute('select state from units where id=?', (U['id'],)).fetchone()[0] == 'PENDING')
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d' % (sum(len(v['english'].split()) for v in cov),
                                sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
