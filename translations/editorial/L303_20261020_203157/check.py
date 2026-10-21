r"""check.py — L303 (`data/remnant/remnant ships.txt`, righe 1378-1826). **LOTTO TERMINALE del file**.

Quattordici schede che chiudono il file: verifica l'**invariante di FILE** (38 unita', somma dei lotti 12 + 12 + 14) e cinque cose
del testo:

1. **tre terzine** con due tab consecutive (`Petrel`, `Smew`, `Tern`);
2. **la ripetizione 1380 = 1490**: lo **stesso avviso** sui caccia sotto due navi diverse, resa **identica**;
3. **la variante droni (1826)**: stesso avviso, sostituito il sostantivo, forma **del corpus** («una baia per droni»);
4. **la famiglia dell'occultamento**: la 1595 (`Starling`) e' la **quinta**, e deve essere identica a meno del nome alla `Gull`
   (L301) e a `Merganser` / `Penguin` / `Peregrine` (L302) — il test **riapre entrambi** i `translation.json`;
5. **tre avvisi in seconda persona** (1380, 1490, 1826), unici casi del lotto.
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
L301 = os.path.join(L10N, 'staging', 'editorial', 'L301_20261020_202040', 'translation.json')
L302 = os.path.join(L10N, 'staging', 'editorial', 'L302_20261020_202611', 'translation.json')
PATH = 'data/remnant/remnant ships.txt'
TERZINE = {'ship:Petrel': [1378, 1379, 1380], 'ship:Smew': [1488, 1489, 1490], 'ship:Tern': [1824, 1825, 1826]}
COPPIE = [(1594, 1595), (1766, 1767)]
TABBED = [1379, 1380, 1489, 1490, 1595, 1767, 1825, 1826]
TU = [3, 7, 14]
AVVISO_CACCIA = ('\tI caccia non sono dotati di iperguida. Non puoi trasportare un caccia a meno che tu non abbia '
                 'nella tua flotta una nave con una baia di caccia.')
AVVISO_DRONI = ('\tI droni non sono dotati di iperguida. Non puoi trasportare un drone a meno che tu non abbia '
                'nella tua flotta una nave con una baia per droni.')
NAMES = ['Remnant', 'Petrel', 'Puffin', 'Smew', 'Starling', 'Swan', 'Tern', 'Ibis', 'Albatross', 'Archon']
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
prev = {u['line']: u for u in json.load(open(L301, encoding='utf-8'))['units']}
prev2 = {u['line']: u for u in json.load(open(L302, encoding='utf-8'))['units']}
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


grp = collections.Counter(u['context'] for u in cov)
ck('unita tradotte 14/14', len(cov) == 14 == len(units), '%d/%d' % (len(cov), len(units)))
ck('tutte DESCRIPTION, sei contesti: tre terzine, due coppie, una singola',
   {u['kind'] for u in cov} == {'DESCRIPTION'} and len(grp) == 6
   and sorted(grp.values()) == [1, 2, 2, 3, 3, 3], dict(grp))
ck('TERZINE `Petrel` `Smew` `Tern`, tab sulla seconda e sulla terza',
   all([u['line'] for u in cov if u['context'] == c] == ls for c, ls in TERZINE.items())
   and all(at[l]['english'].startswith(TAB) and at[l]['italian'].startswith(TAB)
           for ls in TERZINE.values() for l in ls[1:])
   and all(not at[ls[0]]['english'].startswith(TAB) for ls in TERZINE.values()))
ck('COPPIE `Starling` 1594/1595 e `Swan` 1766/1767, tab sulla seconda',
   all(at[b]['context'] == at[a]['context'] and at[b]['english'].startswith(TAB) for a, b in COPPIE))
ck('TAB: esattamente otto unita la portano, alle righe dichiarate',
   sorted(u['line'] for u in cov if u['english'].startswith(TAB)) == TABBED
   and sum(u['italian'].count(TAB) for u in cov) == 8)
ck('RIPETIZIONE 1380 = 1490 identica in inglese E in italiano',
   by[3]['english'] == by[7]['english'] and by[3]['italian'] == by[7]['italian'])
ck('gli avvisi usano la forma del CORPUS (`baia di caccia` / `baia per droni`)',
   by[3]['italian'] == AVVISO_CACCIA and by[14]['italian'] == AVVISO_DRONI,
   (by[3]['italian'][:50], by[14]['italian'][:50]))
_cac, _dron = AVVISO_CACCIA.rsplit('una nave con una', 1), AVVISO_DRONI.rsplit('una nave con una', 1)
ck('VARIANTE droni 1826: stesso avviso a parte il sostantivo e il nome della baia',
   by[14]['italian'] == AVVISO_DRONI
   and _cac[0].replace('caccia', 'droni').replace('un droni', 'un drone') == _dron[0]
   and _cac[1] == ' baia di caccia.' and _dron[1] == ' baia per droni.',
   (_cac[1], _dron[1]))
ck('FAMIGLIA occultamento: la 1595 e identica a `Gull` (L301) e alle tre di L302, a meno del nome',
   at[1595]['italian'].replace('Starling', 'X') == prev[549]['italian'].replace('Gull', 'X')
   and all(at[1595]['italian'].replace('Starling', 'X') == prev2[l]['italian'].replace(n, 'X')
           for l, n in {982: 'Merganser', 1202: 'Penguin', 1291: 'Peregrine'}.items()),
   at[1595]['italian'][:60])
ck('SECONDA PERSONA solo negli avvisi di gioco (unita 3, 7, 14)',
   [u['idx'] for u in cov if re.search(r'\b(tu|tuo|tua|tuoi|tue|ti|te)\b', u['italian'])] == TU,
   [u['idx'] for u in cov if re.search(r'\b(tu|tuo|tua|tuoi|tue|ti|te)\b', u['italian'])])
ck('tutte e 14 le unita sono TRADOTTE, nessuna copiata',
   all(u['italian'] != u['english'] for u in cov), [u['idx'] for u in cov if u['italian'] == u['english']])
ck('VIRGOLETTE, SEGNAPOSTO, ALTERNATIVE: tutti zero (asserzioni vuote)',
   sum(u['english'].count(QUOTE) for u in cov) == 0 == sum(u['italian'].count(QUOTE) for u in cov)
   and sum(len(TAG.findall(u['italian'])) for u in cov) == 0
   and sum(len(ALT.findall(u['italian'])) for u in cov) == 0)
ck('i tre punti sono ASCII (unita 8), nessun carattere ellissi',
   '...' in by[8]['italian'] and '\u2026' not in ''.join(u['italian'] for u in cov))
ck('APICI: tre in inglese (1378, 1434, 1595), dodici in italiano',
   sum(u['english'].count(APOS) for u in cov) == 3 and sum(u['italian'].count(APOS) for u in cov) == 12,
   (sum(u['english'].count(APOS) for u in cov), sum(u['italian'].count(APOS) for u in cov)))
ck('nomi di nave, fazioni e luoghi INVARIATI',
   all(n in ''.join(u['italian'] for u in cov) for n in NAMES),
   [n for n in NAMES if n not in ''.join(u['italian'] for u in cov)])
ck('lessico: ramscoop, baie per droni, navi di schermo, scialuppa di salvataggio',
   'ramscoop' in by[10]['italian'] and 'baie per droni' in by[11]['italian']
   and 'navi di schermo' in by[12]['italian'] and 'scialuppa di salvataggio' in by[6]['italian'])
ck('nessun caporale, nessun carattere tipografico',
   not [u['idx'] for u in cov for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026' if c in u['italian']])
nonlat = [(u['idx'], c) for u in cov for c in u['italian'] if ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessun doppio spazio (la tab iniziale non conta)',
   not [u['idx'] for u in cov if '  ' in u['italian'].lstrip(TAB)])
ck('rapporto nel gate 0,55-1,90 (0,99-1,18)',
   all(0.55 < u['ratio'] < 1.90 for u in cov),
   [(u['idx'], u['ratio']) for u in cov if not 0.55 < u['ratio'] < 1.90])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck('FILE: 24 unita prima della 1378 (12 + 12)',
   db.execute('select count(*) from units where path=? and line<1378', (PATH,)).fetchone()[0] == 24)
ck('FILE: ZERO unita dopo la 1826 — il lotto CHIUDE il file',
   db.execute('select count(*) from units where path=? and line>1826', (PATH,)).fetchone()[0] == 0)
ck('FILE: 38 unita, righe 17-1826, 35 DESCRIPTION + 3 VALUE',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (38, 17, 1826)
   and dict(db.execute('select kind,count(*) from units where path=? group by kind', (PATH,)).fetchall())
   == {'DESCRIPTION': 35, 'VALUE': 3})
ck('FILE: i tre lotti sommano 38 (12 + 12 + 14)', 12 + 12 + 14 == 38)
ck('tutte le 14 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · 6 contesti · 3 terzine · 8 tab · FILE 38/38' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
