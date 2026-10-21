r"""check.py — L326 (`data/_deprecated/deprecated outfits.txt`, righe 25-792). **LOTTO TERMINALE, FILE INTERO**.

Quarantasette unita' in **trentanove contesti** e **tre tipi**: **42 `DESCRIPTION`** da tradurre, **3 `VALUE`** e **2 `TEXT`** da
**copiare**.

Il file e' sotto `_deprecated/`: materiale **ritirato dal gioco ma ancora nei dati**. Si traduce come gli altri, e questo test lo
tratta come un file normale.

Il test difende:

1. **i cinque copiati** (621, 641, 722, 736, 740): identita' all'inglese, **per tipo**, comprese le **virgolette dentro il nome**
   (`Z-3600 "Beam" Amat Torches`);
2. **le coppie gemelle**: 70/82 e 97/109 hanno **lo stesso inglese** e devono avere **la stessa resa**; e' la ripetizione del
   sorgente, non una svista;
3. **le 3 tab** (709, 776, 792) e le **4 righe con virgolette** (722, 736, 740, 776 = 8 caratteri): la 776 ha **entrambe**;
4. **i 12 apici inglesi in 8 unita'**, con **618 che ne ha tre**;
5. **le otto coppie di contesti** e i **trentuno singoli** (39 in tutto): misurati, non dedotti.

E l'invariante di **FILE**: 47 unita', prima 25, ultima 792, zero prima e dopo.
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
PATH = 'data/_deprecated/deprecated outfits.txt'
TAB_RIGHE = [709, 776, 792]
VIRG = {722: 2, 736: 2, 740: 2, 776: 2}
APICI_EN = {192: 2, 467: 1, 554: 2, 579: 1, 618: 3, 638: 1, 709: 1, 775: 1}
VALUE = {621: 'Nanotech Batteries', 641: 'Intrusion Countermeasures'}
TEXT = {722: '"Nettle" KKV', 736: '"Orchid" Nuclear Missile'}
VALUE_Q = {740: 'Z-3600 "Beam" Amat Torches'}
GEMELLE = [(70, 82), (97, 109)]
COPPIE = ['Nanotech Battery', 'Intrusion Countermeasures', 'Multimodal Armor: Resilient',
          'Nettle Magazine', 'Orchid Magazine', 'Z-3600 "Beam" Amat Torch', 'Teciimach Canister',
          'Teciimach Canister Rack']
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


ck('unita tradotte 47/47', len(cov) == 47 == len(units), '%d/%d' % (len(cov), len(units)))
ck('42 DESCRIPTION + 3 VALUE + 2 TEXT',
   collections.Counter(u['kind'] for u in cov) == {'DESCRIPTION': 42, 'VALUE': 3, 'TEXT': 2},
   dict(collections.Counter(u['kind'] for u in cov)))
ck('39 contesti: otto coppie e trentuno singoli',
   len({u['context'] for u in cov}) == 39
   and sorted(collections.Counter(u['context'] for u in cov).values(), reverse=True)
   == [2] * 8 + [1] * 31,
   (len({u['context'] for u in cov}),
    sorted(collections.Counter(u['context'] for u in cov).values(), reverse=True)))
ck('le otto coppie sono esattamente quelle attese',
   sorted(c for c, n in collections.Counter(u['context'] for u in cov).items() if n == 2)
   == sorted('outfit:' + c for c in COPPIE))
ck('i DUE VALUE senza virgolette sono copiati all identico',
   all(at[l]['italian'] == at[l]['english'] == v and at[l]['kind'] == 'VALUE' for l, v in VALUE.items()))
ck('i DUE TEXT sono copiati all identico (virgolette comprese)',
   all(at[l]['italian'] == at[l]['english'] == v and at[l]['kind'] == 'TEXT' for l, v in TEXT.items()),
   [(l, at[l]['italian']) for l in TEXT if at[l]['italian'] != at[l]['english']])
ck('il VALUE con le virgolette nel nome e copiato all identico',
   all(at[l]['italian'] == at[l]['english'] == v and at[l]['kind'] == 'VALUE' for l, v in VALUE_Q.items()),
   [(l, at[l]['italian'], at[l]['english']) for l in VALUE_Q])
ck('nessun DESCRIPTION e identico al suo inglese (i copiati sono solo i cinque)',
   not [u['line'] for u in cov if u['kind'] == 'DESCRIPTION' and u['italian'] == u['english']])
ck('le due coppie GEMELLE hanno la stessa resa (testo uguale, traduzione uguale)',
   all(at[a]['english'] == at[b]['english'] and at[a]['italian'] == at[b]['italian'] for a, b in GEMELLE),
   [(a, b, at[a]['italian'] == at[b]['italian']) for a, b in GEMELLE])
ck('le 3 tab sono alle righe 709, 776, 792 e come PRIMO carattere',
   [u['line'] for u in cov if u['italian'].startswith(TAB)] == TAB_RIGHE
   and all(not u['italian'].startswith(' ') for u in cov))
ck('le 8 virgolette sono su quattro righe, e la 776 ha tab E virgolette',
   {u['line']: u['italian'].count(QUOTE) for u in cov if u['italian'].count(QUOTE)} == VIRG
   and sum(u['italian'].count(QUOTE) for u in cov) == 8
   and at[776]['italian'].startswith(TAB),
   {u['line']: u['italian'].count(QUOTE) for u in cov if u['italian'].count(QUOTE)})
ck('i 12 apici inglesi sono in 8 unita, con 618 che ne ha TRE',
   {u['line']: u['english'].count(APOS) for u in cov if u['english'].count(APOS)} == APICI_EN
   and sum(u['english'].count(APOS) for u in cov) == 12,
   {u['line']: u['english'].count(APOS) for u in cov if u['english'].count(APOS)})
ck('i nomi delle fazioni restano invariati',
   all(n in ''.join(u['italian'] for u in cov)
       for n in ('Korath', 'Quarg', 'Successor', 'Avgi', 'Anax', 'Antivli', 'Teciimach')))
ck('il Piercer: due testate, la prima apre il varco negli scudi',
   'due testate' in at[467]['italian'] and 'aprire un varco negli scudi' in at[467]['italian'])
ck('la mina: UNDICI submunizioni',
   'undici submunizioni' in at[475]['italian'])
ck('lo Slicer: taglia l armatura come carta',
   'come se fosse di carta' in at[579]['italian'])
ck('le batterie Quarg: un terzo in piu di energia e oltre un terzo piu piccole',
   'un terzo di energia in più' in at[628]['italian'] and 'oltre un terzo più piccole' in at[628]['italian'])
ck('il motore a raggi Avgi: 0,2c in spinta, 0,4c con l antimateria',
   '0,2c' in at[765]['italian'] and '0,4c' in at[765]['italian']
   and 'motore iperspaziale' in at[765]['italian'])
ck("l'ESPANSIONE DI MASSA non aumenta lo spazio per armi o motori",
   'non aumenta lo spazio per armi o motori' in at[122]['italian'])
ck('VIRGOLETTE dritte, nessun caporale',
   not [c for u in cov for c in u['italian'] if c in '\u2018\u2019\u201C\u201D\u00AB\u00BB\u2014\u2013\u2026'])
ck('SEGNAPOSTO: nessuno · ALTERNATIVE: nessuna (asserzioni vuote)',
   not TAG.findall(''.join(u['italian'] for u in cov))
   and sum(len(ALT.findall(u['italian'])) for u in cov) == 0)
ck('nessun doppio spazio (la tab iniziale non conta)',
   not [u['idx'] for u in cov if '  ' in u['italian'].lstrip(TAB)])
ck('rapporto nel gate 0,55-1,90',
   all(0.55 < u['ratio'] < 1.90 for u in cov),
   [(u['idx'], u['ratio']) for u in cov if not 0.55 < u['ratio'] < 1.90])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("FILE: ZERO unita' prima della 25 — il lotto APRE il file",
   db.execute('select count(*) from units where path=? and line<25', (PATH,)).fetchone()[0] == 0)
ck("FILE: ZERO unita' dopo la 792 — il lotto CHIUDE il file",
   db.execute('select count(*) from units where path=? and line>792', (PATH,)).fetchone()[0] == 0)
ck('FILE: 47 unita, righe 25-792, 42 DESCRIPTION + 3 VALUE + 2 TEXT',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (47, 25, 792)
   and dict(db.execute('select kind,count(*) from units where path=? group by kind', (PATH,)).fetchall())
   == {'DESCRIPTION': 42, 'VALUE': 3, 'TEXT': 2})
ck('FILE: copertura 47/47 — il file e tutto qui',
   db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0] == 47)
ck('tutte le 47 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · 42 DESCRIPTION + 3 VALUE + 2 TEXT in 39 contesti · 3 tab · 8 virgolette · FILE 47/47' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
