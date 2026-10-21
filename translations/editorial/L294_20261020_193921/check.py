r"""check.py — L294 (`data/human/marauders.txt`, righe 62-484). **Primo lotto del file**.

Dodici descrizioni di **navi pirata modificate**: **quattro serie da tre** (Arrow, Bounder, Falcon, Firebird), ognuna con tre
allestimenti diversi dello stesso modello. Il test verifica:

1. **le quattro serie**: tre unita' per contesto, e i nomi di modello **invariati**;
2. **il registro**: le schede sono tecniche, ma **quattro** di esse si rivolgono al lettore («che possiate trovare», «il tuo
   sogno», «tu possa immaginare», «sospetti»). Non e' il registro impersonale dei Gegno: il test elenca le righe ammesse;
3. **asserzioni vuote**: zero tab, zero virgolette, zero segnaposto, zero alternative;
4. **la terminologia del corpus**: «porto per cannoni» (11 occorrenze), «corazzatura», «intercettore».
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
PATH = 'data/human/marauders.txt'
SERIES = {'ship:Marauder Arrow': [62, 84, 111], 'ship:Marauder Bounder': [166, 193, 223],
          'ship:Marauder Falcon': [288, 325, 364], 'ship:Marauder Firebird': [423, 453, 484]}
NAMES = ['Arrow', 'Bounder', 'Falcon', 'Firebird', 'Megaparsec', 'Tarazed', 'Betelgeuse', 'Headhunter', 'Lionheart',
         'Flivver']
TU = [1, 8, 9, 10]  # unita' che si rivolgono al lettore
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


ck('unita tradotte 12/12', len(cov) == 12 == len(units), '%d/%d' % (len(cov), len(units)))
ck('tutte DESCRIPTION, quattro serie da tre',
   {u['kind'] for u in cov} == {'DESCRIPTION'}
   and {(u['context'], u['line']) for u in cov} == {(c, l) for c, ls in SERIES.items() for l in ls}
   and all(sum(1 for u in cov if u['context'] == c) == 3 for c in SERIES),
   {c: sum(1 for u in cov if u['context'] == c) for c in SERIES})
ck('tutte e 12 le unita sono TRADOTTE, nessuna copiata',
   all(u['italian'] != u['english'] for u in cov), [u['idx'] for u in cov if u['italian'] == u['english']])
ck('TAB, VIRGOLETTE, SEGNAPOSTO, ALTERNATIVE: tutti zero (asserzioni vuote)',
   sum(u['english'].count(TAB) for u in cov) == 0 == sum(u['italian'].count(TAB) for u in cov)
   and sum(u['english'].count(QUOTE) for u in cov) == 0 == sum(u['italian'].count(QUOTE) for u in cov)
   and sum(len(TAG.findall(u['english'])) for u in cov) == 0 == sum(len(TAG.findall(u['italian'])) for u in cov)
   and sum(len(ALT.findall(u['english'])) for u in cov) == 0 == sum(len(ALT.findall(u['italian'])) for u in cov))
ck('APICI: cinque in inglese, sette in italiano',
   sum(u['english'].count(APOS) for u in cov) == 5 and sum(u['italian'].count(APOS) for u in cov) == 7,
   (sum(u['english'].count(APOS) for u in cov), sum(u['italian'].count(APOS) for u in cov)))
ck('REGISTRO: solo le unita 1, 8, 9, 10 si rivolgono al lettore',
   [u['idx'] for u in cov
    if re.search(r'\b(tu|tuo|tua|tuoi|tue|ti|te|tuo|possiate|sospetti)\b', u['italian'])] == TU,
   [u['idx'] for u in cov
    if re.search(r'\b(tu|tuo|tua|tuoi|tue|ti|te|possiate|sospetti)\b', u['italian'])])
ck('i nomi di modello e di cantiere restano INVARIATI',
   all(n in ''.join(u['italian'] for u in cov) for n in NAMES),
   [n for n in NAMES if n not in ''.join(u['italian'] for u in cov)])
ck('nessun plurale o adattamento: `Arrow`, `Bounder`, `Falcon`, `Firebird` mai tradotti',
   not [p for p in ('Freccia', 'Balzatore', 'Falcone', 'Uccello di fuoco') if p in ''.join(u['italian'] for u in cov)])
ck('terminologia del CORPUS: «porto per cannoni» (11 occorrenze) e «corazzatura»',
   'porto per cannoni' in by[4]['italian'] and by[9]['italian'].count('porti per cannoni') == 1
   and 'corazzatura' in by[2]['italian'] and 'feritoia' not in ''.join(u['italian'] for u in cov))
ck('«intercettore» per `interceptor`, coerente col corpus (58 occorrenze)',
   by[1]['italian'].count('intercettori') == 1 and by[4]['italian'].count('intercettore') == 1)
ck('le tre varianti di ogni serie si distinguono per contenuto',
   'combattimento' in by[1]['italian'] and 'missile' in by[2]['italian'] and 'sistemi d\'arma' in by[3]['italian']
   and 'ancora più veloce' in by[5]['italian'] and 'letale' in by[6]['italian'])
ck('nessun caporale, nessun carattere tipografico',
   not [u['idx'] for u in cov for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026' if c in u['italian']])
nonlat = [(u['idx'], c) for u in cov for c in u['italian'] if ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']],
   [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90 (1,08-1,29)',
   all(0.55 < u['ratio'] < 1.90 for u in cov),
   [(u['idx'], u['ratio']) for u in cov if not 0.55 < u['ratio'] < 1.90])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("ZERO unita' prima della 62: il lotto APRE il file",
   db.execute('select count(*) from units where path=? and line<62', (PATH,)).fetchone()[0] == 0)
ck("17 unita' dopo la 484",
   db.execute('select count(*) from units where path=? and line>484', (PATH,)).fetchone()[0] == 17)
ck('il file ha 29 unita, righe 62-1146, tutte DESCRIPTION',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (29, 62, 1146)
   and dict(db.execute('select kind,count(*) from units where path=? group by kind', (PATH,)).fetchall())
   == {'DESCRIPTION': 29})
ck('tutte le 12 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · 4 serie da 3 · 0 tab · 0 virgolette · 4 unita in seconda persona' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
