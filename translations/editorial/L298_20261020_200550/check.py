r"""check.py — L298 (`data/coalition/coalition outfits.txt`, righe 202-337). **Secondo lotto del file**.

Quindici schede in **dieci contesti**: **cinque coppie** (la seconda unita' inizia con `\t`) e **cinque schede singole**.

Il test verifica:

1. **le cinque coppie con tab** (247, 260, 274, 290, 337) e che ogni unita' con tab sia la **seconda** del suo contesto;
2. **la coppia a cavallo del confine**: `Outskirts Gauger` occupa le righe **336-337** e deve essere **interamente** dentro il
   lotto — l'unita' successiva del file e' alla **356** e appartiene a un **altro** contesto;
3. **le cinque schede singole** (202, 218, 232, 306, 323), elencate per riga;
4. i **nomi delle fazioni**: `Lunarium` invariato, `House Idriss` -> «Casa Idriss», `Saryds` -> «Saryd», `Saros` invariato.
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
ALT = re.compile(r'\[[^\]]*\]')
HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
PATH = 'data/coalition/coalition outfits.txt'
PAIRS = {(246, 247), (259, 260), (273, 274), (289, 290), (336, 337)}
TABBED = [247, 260, 274, 290, 337]
SINGOLE = [202, 218, 232, 306, 323]
NAMES = ['Lunarium', 'Saryd', 'Saros', 'Casa Idriss', 'Heliarch', 'Coalizione']
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
at = {u['line']: u for u in cov}
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck('unita tradotte 15/15', len(cov) == 15 == len(units), '%d/%d' % (len(cov), len(units)))
ck('tutte DESCRIPTION, dieci contesti: cinque doppi e cinque singoli',
   {u['kind'] for u in cov} == {'DESCRIPTION'}
   and len({u['context'] for u in cov}) == 10
   and sum(1 for n in collections.Counter(u['context'] for u in cov).values() if n == 2) == 5
   and sum(1 for n in collections.Counter(u['context'] for u in cov).values() if n == 1) == 5,
   collections.Counter(u['context'] for u in cov))
ck('le cinque coppie sono quelle dichiarate, con lo stesso contesto',
   {(at[a]['line'], at[b]['line']) for a, b in PAIRS} == PAIRS
   and all(at[a]['context'] == at[b]['context'] for a, b in PAIRS)
   and all(b - a == 1 for a, b in PAIRS))
ck('le cinque schede singole sono quelle dichiarate, per riga',
   [l for l, u in at.items() if collections.Counter(x['context'] for x in cov)[u['context']] == 1] == SINGOLE,
   [l for l, u in at.items() if collections.Counter(x['context'] for x in cov)[u['context']] == 1])
ck('TAB: esattamente cinque unita la portano, alle righe dichiarate, come primo carattere',
   sorted(u['line'] for u in cov if u['english'].startswith(TAB)) == TABBED
   and all(at[l]['italian'].startswith(TAB) for l in TABBED)
   and sum(u['italian'].count(TAB) for u in cov) == 5,
   [u['line'] for u in cov if u['english'].startswith(TAB)])
ck('ogni unita con tab e la SECONDA del suo contesto (compagno alla riga precedente)',
   all(at[l]['context'] == at[l - 1]['context'] for l in TABBED))
ck('la coppia a cavallo del confine (336-337) e interamente nel lotto',
   336 in at and 337 in at and at[336]['context'] == at[337]['context'] == 'outfit:Outskirts Gauger')
ck('tutte e 15 le unita sono TRADOTTE, nessuna copiata',
   all(u['italian'] != u['english'] for u in cov), [u['idx'] for u in cov if u['italian'] == u['english']])
ck('VIRGOLETTE, SEGNAPOSTO, ALTERNATIVE: tutti zero (asserzioni vuote)',
   sum(u['english'].count(QUOTE) for u in cov) == 0 == sum(u['italian'].count(QUOTE) for u in cov)
   and sum(len(TAG.findall(u['italian'])) for u in cov) == 0
   and sum(len(ALT.findall(u['italian'])) for u in cov) == 0)
ck('APICI: sette in inglese (unita 1, 2, 6 x2, 9, 11, 12), sei in italiano',
   sum(u['english'].count(APOS) for u in cov) == 7 and sum(u['italian'].count(APOS) for u in cov) == 6,
   (sum(u['english'].count(APOS) for u in cov), sum(u['italian'].count(APOS) for u in cov)))
ck('nomi: `Lunarium` e `Saros` invariati, `House Idriss` -> «Casa Idriss», `Saryds` -> «Saryd»',
   'Lunarium' in ''.join(u['italian'] for u in cov) and 'Saros' in at[246]['italian']
   and 'Casa Idriss' in at[336]['italian'] and 'i Saryd' in at[246]['italian']
   and 'House Idriss' not in ''.join(u['italian'] for u in cov)
   and 'Saryds' not in ''.join(u['italian'] for u in cov))
ck('terminologia: rivestimento, siluri Heliarch, generatori di scudi, disturbo radar, corazzatura',
   'rivestimento' in at[259]['italian'] and 'siluri Heliarch' in at[260]['italian']
   and 'generatori di scudi' in at[289]['italian'] and 'disturbo radar' in at[260]['italian']
   and 'corazzatura' in at[290]['italian'])
ck('REGISTRO: nessuna seconda persona',
   not [u['idx'] for u in cov if re.search(r'\b(tu|tuo|tua|tuoi|tue|ti|te)\b', u['italian'])],
   [u['idx'] for u in cov if re.search(r'\b(tu|tuo|tua|tuoi|tue|ti|te)\b', u['italian'])])
ck('nessun caporale, nessun carattere tipografico',
   not [u['idx'] for u in cov for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026' if c in u['italian']])
nonlat = [(u['idx'], c) for u in cov for c in u['italian'] if ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessun doppio spazio', not [u['idx'] for u in cov if '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90 (0,94-1,30)',
   all(0.55 < u['ratio'] < 1.90 for u in cov),
   [(u['idx'], u['ratio']) for u in cov if not 0.55 < u['ratio'] < 1.90])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("15 unita' prima della 202 (L297)",
   db.execute('select count(*) from units where path=? and line<202', (PATH,)).fetchone()[0] == 15)
ck("19 unita' dopo la 337 e la prima e `outfit:Small Thrust Module` alla 356",
   db.execute('select count(*) from units where path=? and line>337', (PATH,)).fetchone()[0] == 19
   and db.execute('select line,context from units where path=? and line>337 order by line limit 1', (PATH,)).fetchone()
   == (356, 'outfit:Small Thrust Module'))
ck("l'unita successiva al confine NON e Outskirts Gauger: la coppia non e spezzata",
   db.execute('select context from units where path=? and line>337 order by line limit 1', (PATH,)).fetchone()[0]
   != 'outfit:Outskirts Gauger')
ck('il file ha 49 unita, righe 26-533',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (49, 26, 533))
ck('tutte le 15 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · 10 contesti (5 coppie + 5 singole) · 5 tab · file 30/49' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
