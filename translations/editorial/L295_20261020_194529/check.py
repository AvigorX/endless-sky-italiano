r"""check.py — L295 (`data/human/marauders.txt`, righe 548-858). **Secondo lotto del file**.

Nove descrizioni in **tre serie da tre** (`Leviathan`, `Manta`, `Quicksilver`). Il test verifica soprattutto **le ripetizioni del
sorgente**:

1. **le unita' 8 e 9 sono IDENTICHE nel testo inglese** (righe 831 e 858): la stessa descrizione compare due volte, e la resa
   deve essere **identica** in entrambe — altrimenti lo stesso modello appare descritto in due modi;
2. **`Manta` 5 e 6 chiudono con la stessa frase** («Se il suo tonnellaggio a vuoto fosse appena più alto…»), e la 4 ne ha una
   **variante**;
3. **`Quicksilver` 7 e 8 condividono la frase sul supporto per torrette** («forse in risposta alla Headhunter della Lionheart»).
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
SERIES = {'ship:Marauder Leviathan': [548, 580, 616], 'ship:Marauder Manta': [676, 710, 747],
          'ship:Marauder Quicksilver': [799, 831, 858]}
NAMES = ['Leviathan', 'Manta', 'Quicksilver', 'Betelgeuse', 'Megaparsec', 'Lionheart', 'Headhunter',
         'Vanguard Heavy Warship']
CHIUSA = 'Se il suo tonnellaggio a vuoto fosse appena più alto, sarebbe classificata come nave da guerra pesante.'
TORRETTA = 'in risposta alla Headhunter della Lionheart'
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


ck('unita tradotte 9/9', len(cov) == 9 == len(units), '%d/%d' % (len(cov), len(units)))
ck('tutte DESCRIPTION, tre serie da tre con le righe dichiarate',
   {u['kind'] for u in cov} == {'DESCRIPTION'}
   and {(u['context'], u['line']) for u in cov} == {(c, l) for c, ls in SERIES.items() for l in ls}
   and all(sum(1 for u in cov if u['context'] == c) == 3 for c in SERIES),
   {c: sum(1 for u in cov if u['context'] == c) for c in SERIES})
ck('tutte e 9 le unita sono TRADOTTE, nessuna copiata',
   all(u['italian'] != u['english'] for u in cov), [u['idx'] for u in cov if u['italian'] == u['english']])
ck('RIPETIZIONE del sorgente: le unita 8 e 9 sono identiche in inglese E in italiano',
   by[8]['english'] == by[9]['english'] and by[8]['italian'] == by[9]['italian'])
ck('`Manta`: la 5 e la 6 chiudono con la STESSA frase, la 4 con la variante',
   by[5]['italian'].endswith(CHIUSA) and by[6]['italian'].endswith(CHIUSA)
   and 'È solo il tonnellaggio a vuoto a impedirle' in by[4]['italian'])
ck('`Quicksilver`: 7 e 8 condividono la frase sul supporto per torrette',
   TORRETTA in by[7]['italian'] and TORRETTA in by[8]['italian'])
ck('TAB, VIRGOLETTE, SEGNAPOSTO, ALTERNATIVE: tutti zero (asserzioni vuote)',
   sum(u['english'].count(TAB) for u in cov) == 0 == sum(u['italian'].count(TAB) for u in cov)
   and sum(u['english'].count(QUOTE) for u in cov) == 0 == sum(u['italian'].count(QUOTE) for u in cov)
   and sum(len(TAG.findall(u['italian'])) for u in cov) == 0
   and sum(len(ALT.findall(u['italian'])) for u in cov) == 0)
ck('APICI: otto in inglese, quattordici in italiano',
   sum(u['english'].count(APOS) for u in cov) == 8 and sum(u['italian'].count(APOS) for u in cov) == 14,
   (sum(u['english'].count(APOS) for u in cov), sum(u['italian'].count(APOS) for u in cov)))
ck('REGISTRO impersonale: nessuna unita si rivolge al lettore (contrario di L294)',
   not [u['idx'] for u in cov if re.search(r'\b(tu|tuo|tua|tuoi|tue|ti|te|possiate|sospetti)\b', u['italian'])],
   [u['idx'] for u in cov if re.search(r'\b(tu|tuo|tua|tuoi|tue|ti|te|possiate|sospetti)\b', u['italian'])])
ck('nomi di modello, cantiere e nave restano INVARIATI',
   all(n in ''.join(u['italian'] for u in cov) for n in NAMES),
   [n for n in NAMES if n not in ''.join(u['italian'] for u in cov)])
ck('terminologia del corpus: «porto per cannoni», «supporto per torrette», «spazio per gli equipaggiamenti»',
   'porti per cannoni' in by[5]['italian'] and 'supporto per torrette' in by[6]['italian']
   and 'spazio per gli equipaggiamenti' in by[4]['italian'])
ck('`shield projectors` -> «proiettori di scudi», distinto da `shield emitters` -> «emettitori di scudi»',
   'proiettori di scudi' in by[1]['italian'] and 'emettitori di scudi' in by[4]['italian']
   and 'proiettori di scudi' not in by[4]['italian'])
ck('lessico: tonnellaggio a vuoto, coda forcuta, torrette antimissile, porto per propulsori, cuccetta',
   'tonnellaggio a vuoto' in by[4]['italian'] and 'coda forcuta' in by[5]['italian']
   and 'torrette antimissile' in by[4]['italian'] and 'porto per propulsori' in by[8]['italian']
   and 'cuccetta' in by[7]['italian'])
ck('nessun caporale, nessun carattere tipografico',
   not [u['idx'] for u in cov for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026' if c in u['italian']])
nonlat = [(u['idx'], c) for u in cov for c in u['italian'] if ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']],
   [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90 (1,08-1,21)',
   all(0.55 < u['ratio'] < 1.90 for u in cov),
   [(u['idx'], u['ratio']) for u in cov if not 0.55 < u['ratio'] < 1.90])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("12 unita' prima della 548 (L294)",
   db.execute('select count(*) from units where path=? and line<548', (PATH,)).fetchone()[0] == 12)
ck("8 unita' dopo la 858",
   db.execute('select count(*) from units where path=? and line>858', (PATH,)).fetchone()[0] == 8)
ck('QUICKSILVER continua oltre il confine: la prima unita dopo la 858 e ancora `Marauder Quicksilver`',
   db.execute('select context from units where path=? and line>858 order by line limit 1', (PATH,)).fetchone()
   == ('ship:Marauder Quicksilver',))
ck('il file ha 29 unita, righe 62-1146',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (29, 62, 1146))
ck('tutte le 9 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · 3 serie da 3 · unita 8 e 9 identiche · 0 tab · 0 virgolette' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
