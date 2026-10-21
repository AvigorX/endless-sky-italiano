r"""check.py — L324 (`data/incipias/incipias outfits.txt`, righe 40-388). **LOTTO TERMINALE, FILE INTERO**.

Ventitre `DESCRIPTION` in **17 contesti**: scaricatore al plasma, raggi di stagnazione, `Star Tail`, scudi `Gas`/`Liquid-Class`,
idrogeno metallico, la **scala dei colori** e la licenza `Hicemus`.

Il test difende:

1. **la nota dei rifornimenti** (135) con la resa **di maggioranza** del corpus — quarta occorrenza in quattro lotti;
2. **la scala dei colori**: `Blue` **il più debole**, `Green` **l'equilibrio**, `Red` **il forte**, con i nomi **invariati**;
3. **le 6 tab**: `Stagnation Beam` ne ha **due** (86, 87) e `Star Tail` **due** (134, 135), una delle quali e' la nota;
4. **i 9 apici inglesi in 5 unita'** (40, 85 x2, 86 x3, 225 x2, 351);
5. **zero virgolette, zero segnaposto, zero alternative**: asserzioni vuote, dichiarate.

E l'invariante di **FILE**: 23 unita', prima 40, ultima 388, zero prima e dopo.
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
PATH = 'data/incipias/incipias outfits.txt'
NOTA_EN = TAB + 'Ammunition for this weapon can be restocked at any outfitter.'
TAB_RIGHE = [41, 86, 87, 134, 135, 190]
APICI_EN = {40: 1, 85: 2, 86: 3, 225: 2, 351: 1}
NOMI = ['Plasma Discharger', 'Stagnation Beam', 'Star Tail', 'Horizon Grappler', 'Gas-Class Shield',
        'Liquid-Class Shield', 'Metallic Hydrogen Cell', 'MH Blue-Class', 'MH Green-Class', 'MH Red-Class',
        'Cloud Piercer', 'Hicemus']
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
    rows.append((n, d if d else ('OK' if c else 'FAIL'), c))


ck('unita tradotte 23/23', len(cov) == 23 == len(units), '%d/%d' % (len(cov), len(units)))
ck('tutte e 23 sono DESCRIPTION',
   collections.Counter(u['kind'] for u in cov) == {'DESCRIPTION': 23})
ck('17 contesti: Plasma 2, Stagnation 3, Star Tail 3, Storage 2, TREDICI singoli',
   len({u['context'] for u in cov}) == 17
   and sorted(collections.Counter(u['context'] for u in cov).values(), reverse=True)
   == [3, 3, 2, 2] + [1] * 13,
   sorted(collections.Counter(u['context'] for u in cov).values(), reverse=True))
ck('le 6 tab sono alle righe attese, e Stagnation e Star Tail ne hanno DUE',
   [u['line'] for u in cov if u['italian'].startswith(TAB)] == TAB_RIGHE
   and at[86]['context'] == at[87]['context'] == 'outfit:Stagnation Beam'
   and at[134]['context'] == at[135]['context'] == 'outfit:Star Tail')
ck('la nota dei rifornimenti usa la resa di maggioranza del corpus',
   at[135]['english'] == NOTA_EN
   and at[135]['italian'] == NOTA_EN.replace(
       'Ammunition for this weapon can be restocked at any outfitter.',
       "Le munizioni per quest'arma possono essere rifornite presso qualsiasi emporio."))
ck('la SCALA dei colori: blu il più debole, verde equilibrio, rosso il forte',
   'colore più debole' in at[289]['italian']
   and 'colore di equilibrio' in at[320]['italian']
   and 'fonte di energia potente' in at[351]['italian']
   and 'combattimento' in at[365]['italian'])
ck('i nomi MH restano INVARIATI nelle tre classi',
   all(c in u['italian'] for u in cov for c in ('Blue-Class', 'Green-Class', 'Red-Class')
       if c in u['english']))
ck('nomi degli equipaggiamenti INVARIATI dove compaiono',
   all(n in u['italian'] for u in cov for n in NOMI if n in u['english']),
   [(u['line'], n) for u in cov for n in NOMI if n in u['english'] and n not in u['italian']])
ck('il Plasma Discharger: estratti PRIMA del volo intrasistemico, e non all altezza delle armi umane',
   'viaggi intrasistemici' in at[40]['italian'] and 'armi umane' in at[40]['italian'])
ck('lo Stagnation Beam: prototipi PRIMA del sogno del volo spaziale',
   'prima che gli Incipias sognassero il viaggio spaziale' in at[85]['italian'])
ck('lo Star Tail: una cella per UN colpo esatto',
   'esattamente per un colpo' in at[177]['italian'])
ck('gli scudi: idrogeno bruciato nel nucleo, fonte di energia di tutte le navi',
   'bruciato idrogeno' in at[246]['italian'] and 'fonte di energia principale' in at[246]['italian'])
ck('la licenza Hicemus: fiducia e vantaggio sulle altre fazioni',
   'si sono fidati di te' in at[388]['italian'] and 'vantaggio sulle altre fazioni' in at[388]['italian'])
ck('VIRGOLETTE: zero · SEGNAPOSTO: nessuno · ALTERNATIVE: nessuna (asserzioni vuote)',
   sum(u['italian'].count(QUOTE) for u in cov) == 0
   and not TAG.findall(''.join(u['italian'] for u in cov))
   and sum(len(ALT.findall(u['italian'])) for u in cov) == 0)
ck('APICI: 9 caratteri in inglese su 5 unita (40, 85 x2, 86 x3, 225 x2, 351)',
   {u['line']: u['english'].count(APOS) for u in cov if u['english'].count(APOS)} == APICI_EN
   and sum(u['english'].count(APOS) for u in cov) == 9,
   {u['line']: u['english'].count(APOS) for u in cov if u['english'].count(APOS)})
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in cov for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessun doppio spazio (la tab iniziale non conta)',
   not [u['idx'] for u in cov if '  ' in u['italian'].lstrip(TAB)])
ck('rapporto nel gate 0,55-1,90',
   all(0.55 < u['ratio'] < 1.90 for u in cov),
   [(u['idx'], u['ratio']) for u in cov if not 0.55 < u['ratio'] < 1.90])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("FILE: ZERO unita' prima della 40 — il lotto APRE il file",
   db.execute('select count(*) from units where path=? and line<40', (PATH,)).fetchone()[0] == 0)
ck("FILE: ZERO unita' dopo la 388 — il lotto CHIUDE il file",
   db.execute('select count(*) from units where path=? and line>388', (PATH,)).fetchone()[0] == 0)
ck('FILE: 23 unita, righe 40-388, tutte DESCRIPTION',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (23, 40, 388)
   and dict(db.execute('select kind,count(*) from units where path=? group by kind', (PATH,)).fetchall())
   == {'DESCRIPTION': 23})
ck('FILE: copertura 23/23 — il file e tutto qui',
   db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0] == 23)
ck('tutte le 23 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · 23 DESCRIPTION in 17 contesti · 6 tab · 0 virgolette · FILE 23/23' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
