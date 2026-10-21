r"""check.py — L299 (`data/coalition/coalition outfits.txt`, righe 356-509). **Terzo lotto del file**.

Quattordici schede in **dieci contesti**: **due coppie**, **una terzina** e **sette singole**.

Il test verifica:

1. **la terzina `Guardian Turret`** (495, 496, 497): tre unita' dello **stesso contesto** su righe consecutive, con la tab
   sulla **seconda e sulla terza** (due tab consecutive);
2. **le due coppie** (394/395 `Small Reverse`, 414/415 `Large Reverse`), tab sulla seconda;
3. **la ripetizione del sorgente**: le unita' **4 e 6** hanno lo **stesso testo inglese** («Because a reverse thruster must be
   facing forwards…») e devono avere la **stessa resa**;
4. **la seconda persona in due sole unita'** (4 e 6: «della **tua** nave»), che sono **istruzioni di gioco** sull'installazione.
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
PAIRS = [(394, 395), (414, 415)]
TRIPLE = [495, 496, 497]
SINGOLE = [356, 375, 434, 453, 467, 481, 509]
TABBED = [395, 415, 496, 497]
TU = [4, 6]
NAMES = ['Heliarch', 'Quarg', 'Coalizione']
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


ck('unita tradotte 14/14', len(cov) == 14 == len(units), '%d/%d' % (len(cov), len(units)))
grp = collections.Counter(u['context'] for u in cov)
ck('tutte DESCRIPTION, dieci contesti: due doppi, un triplo, sette singoli',
   {u['kind'] for u in cov} == {'DESCRIPTION'} and len(grp) == 10
   and sorted(grp.values()) == [1] * 7 + [2, 2, 3], dict(grp))
ck('TERZINA `Guardian Turret` 495/496/497, stesso contesto, righe consecutive',
   [u['line'] for u in cov if u['context'] == 'outfit:Guardian Turret'] == TRIPLE
   and all(at[l]['context'] == 'outfit:Guardian Turret' for l in TRIPLE))
ck('TERZINA: la tab e sulla SECONDA e sulla TERZA (due tab consecutive)',
   at[496]['english'].startswith(TAB) and at[497]['english'].startswith(TAB)
   and not at[495]['english'].startswith(TAB)
   and at[496]['italian'].startswith(TAB) and at[497]['italian'].startswith(TAB))
ck('COPPIE: 394/395 e 414/415, stesso contesto, tab sulla seconda',
   all(at[b]['context'] == at[a]['context'] and at[b]['english'].startswith(TAB) for a, b in PAIRS))
ck('le sette singole sono quelle dichiarate, per riga',
   [l for l, u in at.items() if grp[u['context']] == 1] == SINGOLE,
   [l for l, u in at.items() if grp[u['context']] == 1])
ck('TAB: esattamente quattro unita la portano, alle righe dichiarate',
   sorted(u['line'] for u in cov if u['english'].startswith(TAB)) == TABBED
   and sum(u['italian'].count(TAB) for u in cov) == 4)
ck('RIPETIZIONE del sorgente: le unita 4 e 6 (395 e 415) identiche in inglese E in italiano',
   by[4]['english'] == by[6]['english'] and by[4]['italian'] == by[6]['italian'])
ck('tutte e 14 le unita sono TRADOTTE, nessuna copiata',
   all(u['italian'] != u['english'] for u in cov), [u['idx'] for u in cov if u['italian'] == u['english']])
ck('VIRGOLETTE, SEGNAPOSTO, ALTERNATIVE: tutti zero (asserzioni vuote)',
   sum(u['english'].count(QUOTE) for u in cov) == 0 == sum(u['italian'].count(QUOTE) for u in cov)
   and sum(len(TAG.findall(u['italian'])) for u in cov) == 0
   and sum(len(ALT.findall(u['italian'])) for u in cov) == 0)
ck('i tre punti sono ASCII: unita 1 con `...`, nessun carattere ellissi',
   '...' in by[1]['italian'] and '\u2026' not in ''.join(u['italian'] for u in cov))
ck('APICI: quattro in inglese (11, 12, 13, 14), tredici in italiano',
   sum(u['english'].count(APOS) for u in cov) == 4 and sum(u['italian'].count(APOS) for u in cov) == 13,
   (sum(u['english'].count(APOS) for u in cov), sum(u['italian'].count(APOS) for u in cov)))
ck('REGISTRO: la seconda persona compare solo nelle unita 4 e 6 (istruzioni di installazione)',
   [u['idx'] for u in cov if re.search(r'\b(tu|tuo|tua|tuoi|tue|ti|te)\b', u['italian'])] == TU,
   [u['idx'] for u in cov if re.search(r'\b(tu|tuo|tua|tuoi|tue|ti|te)\b', u['italian'])])
ck('terminologia del corpus: «propulsore di spinta inversa», non «invertitore»',
   'propulsore di spinta inversa' in by[4]['italian']
   and 'invertitore' not in ''.join(u['italian'] for u in cov))
ck('lessico: torretta, antiabbordaggio, cecchinaggio, dissidenti, navi capitali',
   'torretta' in by[11]['italian'] and 'antiabbordaggio' in by[11]['italian']
   and 'cecchinaggio' in by[12]['italian'] and 'dissidenti' in by[10]['italian']
   and 'navi capitali' in by[8]['italian'])
ck('nessun caporale, nessun carattere tipografico',
   not [u['idx'] for u in cov for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026' if c in u['italian']])
nonlat = [(u['idx'], c) for u in cov for c in u['italian'] if ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessun doppio spazio (la tab iniziale non conta)',
   not [u['idx'] for u in cov if '  ' in u['italian'].lstrip(TAB)])
ck('rapporto nel gate 0,55-1,90 (0,90-1,22)',
   all(0.55 < u['ratio'] < 1.90 for u in cov),
   [(u['idx'], u['ratio']) for u in cov if not 0.55 < u['ratio'] < 1.90])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("30 unita' prima della 356 (L297 + L298)",
   db.execute('select count(*) from units where path=? and line<356', (PATH,)).fetchone()[0] == 30)
ck("5 unita' dopo la 509: il lotto successivo e il TERMINALE del file",
   db.execute('select count(*) from units where path=? and line>509', (PATH,)).fetchone()[0] == 5)
ck('la prima unita dopo la 509 e `Coalition License` alla 516 (coppia lasciata intera)',
   db.execute('select line,context from units where path=? and line>509 order by line limit 1', (PATH,)).fetchone()
   == (516, 'outfit:Coalition License'))
ck('il file ha 49 unita, righe 26-533, ultima riga 533',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (49, 26, 533))
ck('tutte le 14 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · 2 coppie + 1 terzina + 7 singole · 4 tab · file 44/49' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
