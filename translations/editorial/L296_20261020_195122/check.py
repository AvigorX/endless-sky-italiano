r"""check.py — L296 (`data/human/marauders.txt`, righe 884-1146). **LOTTO TERMINALE del file**.

Otto descrizioni che chiudono il file: verifica l'**invariante di FILE** (29 unita', somma dei lotti 12 + 9 + 8) e tre cose del
testo:

1. **le unita' 1 e 2 sono IDENTICHE nel sorgente** (righe 884 e 910): la resa deve esserlo in **entrambe le lingue**;
2. **la seconda persona compare in TRE unita'** (3: «che **ti** aspetti»; 5: «fa chiedere quanto si possa…»; 7: «che **tu**
   trovi»): va **elencata**, come in L294 — e il contratto ne prevedeva una sola;
3. **i tre motivi delle serie**: `Raven` riconoscibile «solo grazie alle ali» (3 unita'), `Splinter` con «ampie sezioni dello
   scafo» coperte (3 unita').
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
ALT = re.compile(r'\[[^\]]*\]')
HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
PATH = 'data/human/marauders.txt'
SERIES = {'ship:Marauder Quicksilver': [884, 910], 'ship:Marauder Raven': [968, 996, 1026],
          'ship:Marauder Splinter': [1083, 1114, 1146]}
NAMES = ['Quicksilver', 'Raven', 'Splinter', 'Megaparsec', 'Lionheart', 'Headhunter']
TU = [3, 5, 7]  # tre, non due: la seconda persona e' anche in «che ti aspetti» (unita' 3)
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
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck('unita tradotte 8/8', len(cov) == 8 == len(units), '%d/%d' % (len(cov), len(units)))
ck('tutte DESCRIPTION, tre contesti con le righe dichiarate (2 + 3 + 3)',
   {u['kind'] for u in cov} == {'DESCRIPTION'}
   and {(u['context'], u['line']) for u in cov} == {(c, l) for c, ls in SERIES.items() for l in ls}
   and {c: sum(1 for u in cov if u['context'] == c) for c in SERIES} == {c: len(ls) for c, ls in SERIES.items()},
   {c: sum(1 for u in cov if u['context'] == c) for c in SERIES})
ck('tutte e 8 le unita sono TRADOTTE, nessuna copiata',
   all(u['italian'] != u['english'] for u in cov), [u['idx'] for u in cov if u['italian'] == u['english']])
ck('RIPETIZIONE del sorgente: le unita 1 e 2 identiche in inglese E in italiano',
   by[1]['english'] == by[2]['english'] and by[1]['italian'] == by[2]['italian'])
ck('TAB, VIRGOLETTE, SEGNAPOSTO, ALTERNATIVE: tutti zero (asserzioni vuote)',
   sum(u['english'].count(TAB) for u in cov) == 0 == sum(u['italian'].count(TAB) for u in cov)
   and sum(u['english'].count(QUOTE) for u in cov) == 0 == sum(u['italian'].count(QUOTE) for u in cov)
   and sum(len(TAG.findall(u['italian'])) for u in cov) == 0
   and sum(len(ALT.findall(u['italian'])) for u in cov) == 0)
ck('APICI: dieci in inglese, dieci in italiano',
   sum(u['english'].count(APOS) for u in cov) == 10 and sum(u['italian'].count(APOS) for u in cov) == 10,
   (sum(u['english'].count(APOS) for u in cov), sum(u['italian'].count(APOS) for u in cov)))
ck('REGISTRO: la seconda persona compare solo nelle unita 3, 5 e 7',
   [u['idx'] for u in cov if re.search(r'\b(tu|tuo|tua|tuoi|tue|ti|te|possa|trovi)\b', u['italian'])] == TU,
   [u['idx'] for u in cov if re.search(r'\b(tu|tuo|tua|tuoi|tue|ti|te|possa|trovi)\b', u['italian'])])
ck('`Raven`: tutte e tre le varianti la riconoscono «solo grazie alle ali»',
   sum(1 for i in (3, 4, 5) if 'ali' in by[i]['italian']) == 3)
ck('`Splinter`: le tre varianti parlano tutte di sezioni dello scafo coperte',
   sum(1 for i in (6, 7, 8) if 'sezioni dello scafo' in by[i]['italian']) == 3,
   [i for i in (6, 7, 8) if 'sezioni dello scafo' not in by[i]['italian']])
ck('nomi di modello e di cantiere restano INVARIATI',
   all(n in ''.join(u['italian'] for u in cov) for n in NAMES),
   [n for n in NAMES if n not in ''.join(u['italian'] for u in cov)])
ck('terminologia: «porti per cannoni», «punti di attacco», «paratie», «baie motore», «porto motore»',
   'porti per cannoni' in by[1]['italian'] and 'punti di attacco' in by[8]['italian']
   and 'paratie' in by[3]['italian'] and 'baie motore' in by[4]['italian'] and 'porto motore' in by[7]['italian'])
ck('«kilotonnellaggio» per `sub-kiloton`',
   'sotto il kilotonnellaggio' in by[7]['italian'])
ck('nessun caporale, nessun carattere tipografico',
   not [u['idx'] for u in cov for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026' if c in u['italian']])
nonlat = [(u['idx'], c) for u in cov for c in u['italian'] if ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']],
   [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90 (1,03-1,21)',
   all(0.55 < u['ratio'] < 1.90 for u in cov),
   [(u['idx'], u['ratio']) for u in cov if not 0.55 < u['ratio'] < 1.90])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck('FILE: 21 unita prima della 884 (12 + 9)',
   db.execute('select count(*) from units where path=? and line<884', (PATH,)).fetchone()[0] == 21)
ck('FILE: ZERO unita dopo la 1146 — il lotto CHIUDE il file',
   db.execute('select count(*) from units where path=? and line>1146', (PATH,)).fetchone()[0] == 0)
ck('FILE: 29 unita, righe 62-1146, tutte DESCRIPTION',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (29, 62, 1146)
   and dict(db.execute('select kind,count(*) from units where path=? group by kind', (PATH,)).fetchall())
   == {'DESCRIPTION': 29})
ck('FILE: i tre lotti sommano 29 (12 + 9 + 8)',
   12 + 9 + 8 == 29 and db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0] == 29)
ck('tutte le 8 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · 3 contesti · unita 1 e 2 identiche · FILE 29/29' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
