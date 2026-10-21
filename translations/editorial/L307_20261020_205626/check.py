r"""check.py — L307 (`data/avgi/avgi weapons.txt`, righe 25-203). **PRIMO lotto del file**.

Dodici schede in **sei contesti**: **due terzine** (`Speckle Coilgun` 67/68/69, `Speckle Turret` 106/107/108), **due coppie**
(`Optical Lasing Generator` 173/174, `Green Optical Laser` 202/203) e **due singole** (`Speck Round` 25, `Speck Magazine` 38).

Il test verifica:

1. **le due terzine** con **due tab consecutive** (sulla seconda e sulla terza unita');
2. **la ripetizione 69 = 108**: la nota «Ammunition for this weapon can be restocked at any outfitter.» compare sotto **due armi
   diverse** e la resa deve essere **identica**;
3. **il refuso del sorgente NON si riproduce**: la riga 174 dice `can altered` (manca il verbo) — l'italiano è **corretto**
   («può essere modificata») e il test rifiuta di ricopiare l'errore;
4. **il collegamento torretta -> generatore**: la 203 dice che la torretta **richiede** un `Optical Lasing Generator`, e i nomi
   restano invariati.
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
PATH = 'data/avgi/avgi weapons.txt'
TERZINE = {'outfit:Speckle Coilgun': [67, 68, 69], 'outfit:Speckle Turret': [106, 107, 108]}
COPPIE = [(173, 174), (202, 203)]
SINGOLE = [25, 38]
TABBED = [68, 69, 107, 108, 174, 203]
NOTA = '\tLe munizioni di quest\'arma si possono rifornire in qualsiasi emporio.'
NAMES = ['Avgi', 'Speckle Coilgun', 'Speckle Turret', 'Optical Lasing Generator', 'Green Optical Laser',
         'Blue Optical Laser']
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


grp = collections.Counter(u['context'] for u in cov)
ck('unita tradotte 12/12', len(cov) == 12 == len(units), '%d/%d' % (len(cov), len(units)))
ck('tutte DESCRIPTION, sei contesti: 2 terzine + 2 coppie + 2 singole',
   {u['kind'] for u in cov} == {'DESCRIPTION'} and len(grp) == 6
   and sorted(grp.values()) == [1, 1, 2, 2, 3, 3], dict(grp))
ck('TERZINE `Speckle Coilgun` 67/68/69 e `Speckle Turret` 106/107/108, tab sulla 2a e 3a',
   all([u['line'] for u in cov if u['context'] == c] == ls for c, ls in TERZINE.items())
   and all(at[l]['english'].startswith(TAB) and at[l]['italian'].startswith(TAB)
           for ls in TERZINE.values() for l in ls[1:])
   and all(not at[ls[0]]['english'].startswith(TAB) for ls in TERZINE.values()))
ck('COPPIE `Optical Lasing Generator` 173/174 e `Green Optical Laser` 202/203, tab sulla seconda',
   all(at[b]['context'] == at[a]['context'] and at[b]['english'].startswith(TAB) for a, b in COPPIE))
ck('le due singole sono `Speck Round` 25 e `Speck Magazine` 38',
   [l for l, u in at.items() if grp[u['context']] == 1] == SINGOLE,
   [l for l, u in at.items() if grp[u['context']] == 1])
ck('TAB: esattamente sei unita la portano, alle righe dichiarate',
   sorted(u['line'] for u in cov if u['english'].startswith(TAB)) == TABBED
   and sum(u['italian'].count(TAB) for u in cov) == 6)
ck('RIPETIZIONE 69 = 108: la nota sulle munizioni identica in inglese E in italiano',
   by[5]['english'] == by[8]['english'] and by[5]['italian'] == by[8]['italian'] == NOTA)
ck('il refuso del sorgente NON si riproduce: la 174 ha il verbo («può essere modificata»)',
   'can altered' in by[10]['english']
   and 'può essere modificata' in by[10]['italian']
   and 'altered' not in by[10]['italian'])
ck('collegamento torretta -> generatore: la 203 nomina `Optical Lasing Generator`',
   'Optical Lasing Generator' in by[12]['italian'] and 'tre Green Laser' in by[12]['italian'])
ck('tutte e 12 le unita sono TRADOTTE, nessuna copiata',
   all(u['italian'] != u['english'] for u in cov), [u['idx'] for u in cov if u['italian'] == u['english']])
ck('VIRGOLETTE, SEGNAPOSTO, ALTERNATIVE: tutti zero (asserzioni vuote)',
   sum(u['english'].count(QUOTE) for u in cov) == 0 == sum(u['italian'].count(QUOTE) for u in cov)
   and sum(len(TAG.findall(u['italian'])) for u in cov) == 0
   and sum(len(ALT.findall(u['italian'])) for u in cov) == 0)
ck('APICI: uno in inglese (202), dieci in italiano',
   sum(u['english'].count(APOS) for u in cov) == 1 and sum(u['italian'].count(APOS) for u in cov) == 10,
   (sum(u['english'].count(APOS) for u in cov), sum(u['italian'].count(APOS) for u in cov)))
ck('nomi di arma e fazione INVARIATI',
   all(n in ''.join(u['italian'] for u in cov) for n in NAMES),
   [n for n in NAMES if n not in ''.join(u['italian'] for u in cov)])
ck('terminologia: emporio (outfitter), coilgun, antimissile, cannone a massa',
   'emporio' in by[5]['italian'] and 'coilgun' in by[3]['italian']
   and 'antimissile' in by[11]['italian'] and 'cannone a massa' in by[4]['italian'])
ck('REGISTRO: nessuna seconda persona',
   not [u['idx'] for u in cov if re.search(r'\b(tu|tuo|tua|tuoi|tue|ti|te)\b', u['italian'])],
   [u['idx'] for u in cov if re.search(r'\b(tu|tuo|tua|tuoi|tue|ti|te)\b', u['italian'])])
ck('nessun caporale, nessun carattere tipografico',
   not [u['idx'] for u in cov for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026' if c in u['italian']])
nonlat = [(u['idx'], c) for u in cov for c in u['italian'] if ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessun doppio spazio (la tab iniziale non conta)',
   not [u['idx'] for u in cov if '  ' in u['italian'].lstrip(TAB)])
ck('rapporto nel gate 0,55-1,90 (1,06-1,27)',
   all(0.55 < u['ratio'] < 1.90 for u in cov),
   [(u['idx'], u['ratio']) for u in cov if not 0.55 < u['ratio'] < 1.90])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("ZERO unita' prima della 25: il lotto APRE il file",
   db.execute('select count(*) from units where path=? and line<25', (PATH,)).fetchone()[0] == 0)
ck("34 unita' dopo la 203; la prima e `Blue Optical Laser` alla 264",
   db.execute('select count(*) from units where path=? and line>203', (PATH,)).fetchone()[0] == 34
   and db.execute('select line,context from units where path=? and line>203 order by line limit 1', (PATH,)).fetchone()
   == (264, 'outfit:Blue Optical Laser'))
ck('il file ha 46 unita (35 DESCRIPTION + 7 TEXT + 4 VALUE), righe 25-969',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (46, 25, 969)
   and dict(db.execute('select kind,count(*) from units where path=? group by kind', (PATH,)).fetchall())
   == {'DESCRIPTION': 35, 'TEXT': 7, 'VALUE': 4})
ck('tutte le 12 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · 6 contesti · 2 terzine + 2 coppie · 6 tab · file 12/46' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
