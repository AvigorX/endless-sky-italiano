r"""check.py — L319 (`data/korath/korath weapons.txt`, righe 615-1222). **LOTTO TERMINALE**.

Ventidue unita' in **15 contesti**: **20 `DESCRIPTION`** da tradurre e **2 `VALUE`** da **copiare** (`Firestorm Torpedoes` 1149,
`Firestorm Batteries` 1174).

Il test difende quattro cose:

1. **i due `VALUE` copiati per identita'** (sono i nomi d'emporio);
2. **la nota dei rifornimenti TRIPLA** (659, 1051, 1222), **identica** alle altre del corpus — la resa e' quella di **L318**, che a sua
   volta e' la **di maggioranza** (16 su 26);
3. **le 5 tab**, con **due nello stesso contesto** (`Firelight Missile Bank`, 1050 e 1051): configurazione nuova rispetto a L311/L312,
   dove ogni contesto aveva **una** sola nota;
4. **le due famiglie distinte**: `Firelight` (missili) e `Firestorm` (torpedini), con il `Firestorm Torpedo` che **cita** il
   `Firelight` e il `Firestorm Battery` che **contiene** il torpedine.

E l'invariante di **FILE**: 39 unita', somma lotti **17 + 22**, prima riga **53**, ultima **1222**, **zero dopo**.
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
PATH = 'data/korath/korath weapons.txt'
NOTA_EN = TAB + 'Ammunition for this weapon can be restocked at any outfitter.'
NOTE = (659, 1051, 1222)
TAB_RIGHE = [659, 930, 1050, 1051, 1222]
VALUE = {17: 'Firestorm Torpedoes', 20: 'Firestorm Batteries'}
NOMI = ['Cluster Mine Rack', 'Cluster Mine Layer', 'Shield Disruptor', 'Husk-Slice', 'Digger Mining',
        'Langrage Hyper-Heaver', 'Firelight', 'Microbot Grinder', 'Firestorm Torpedo', 'Firestorm Battery',
        'Korath Plasma Core', 'Banisher']
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


ck('unita tradotte 22/22', len(cov) == 22 == len(units), '%d/%d' % (len(cov), len(units)))
ck('20 DESCRIPTION + 2 VALUE',
   collections.Counter(u['kind'] for u in cov) == {'DESCRIPTION': 20, 'VALUE': 2},
   dict(collections.Counter(u['kind'] for u in cov)))
ck('15 contesti: Missile Bank x3, quattro doppi, dieci singoli',
   collections.Counter(u['context'] for u in cov) == {
       'outfit:Cluster Mine Rack': 1, 'outfit:Cluster Mine Layer': 2, 'outfit:Shield Disruptor Turret': 1,
       'outfit:Husk-Slice': 1, 'outfit:Husk-Slice Turret': 1, 'outfit:Digger Mining Turret': 1,
       'outfit:Digger Mining Beam': 1, 'outfit:Langrage Hyper-Heaver': 2,
       'outfit:Firelight Storage Rack': 1, 'outfit:Firelight Missile': 1,
       'outfit:Firelight Missile Bank': 3, 'outfit:Microbot Grinder': 1,
       'outfit:Firestorm Torpedo': 2, 'outfit:Firestorm Torpedo Rack': 1,
       'outfit:Firestorm Battery': 3},
   collections.Counter(u['context'] for u in cov).most_common(3))
ck('i due VALUE sono COPIATI per identita',
   all(by[i]['italian'] == v == by[i]['english'] for i, v in VALUE.items()),
   {i: by[i]['italian'] for i in VALUE})
ck('la nota dei rifornimenti e TRIPLA e identica (659, 1051, 1222)',
   by[3]['italian'] == by[15]['italian'] == by[22]['italian']
   and by[3]['english'] == by[15]['english'] == by[22]['english']
   and [u['line'] for u in cov if u['english'] == NOTA_EN] == list(NOTE),
   [u['line'] for u in cov if u['english'] == NOTA_EN])
ck('la nota usa la resa di maggioranza del corpus (quella di L318)',
   by[3]['italian'] == NOTA_EN.replace(
       'Ammunition for this weapon can be restocked at any outfitter.',
       "Le munizioni per quest'arma possono essere rifornite presso qualsiasi emporio."))
ck('le 5 tab sono alle righe attese, e DUE sono nello stesso contesto',
   [u['line'] for u in cov if u['italian'].startswith(TAB)] == TAB_RIGHE
   and at[1050]['context'] == at[1051]['context'] == 'outfit:Firelight Missile Bank')
ck('la famiglia Firelight e distinta dalla Firestorm, e si citano a vicenda',
   'Firelight' in at[1049]['italian'] and 'Firestorm Torpedo' in at[1049]['italian']
   and 'Firelight' in at[1221]['italian'] and 'Firestorm Battery' in at[1159]['italian'])
ck('i nomi restano INVARIATI dove compaiono',
   all(n in u['italian'] for u in cov for n in NOMI if n in u['english']),
   [(u['line'], n) for u in cov for n in NOMI if n in u['english'] and n not in u['italian']])
ck('il Cluster Mine Layer: la mina che non si e ancora dispiegata fa meno danni',
   'mina prima che abbia il tempo di dispiegarsi' in at[658]['italian'])
ck('lo Shield Disruptor: scudi attivi ma scafo danneggiabile',
   'anche quando gli scudi sono attivi' in at[743]['italian'])
ck('Langrage: il campo di lancio collassa e la nube si espande',
   'campo di lancio collassa' in at[930]['italian'] and 'rapida espansione' in at[930]['italian'])
ck('il Microbot Grinder: bocche, artigli, sciame omicida',
   'bocche di aspirazione' in at[1145]['italian'] and 'artigli demolitore' in at[1145]['italian']
   and 'omicida' in at[1145]['italian'])
ck('il Firestorm Battery: Plasma Core senza involucro ne sicurezze',
   'Korath Plasma Core' in at[1221]['italian'] and 'involucro protettivo' in at[1221]['italian']
   and 'dispositivi di sicurezza' in at[1221]['italian'])
ck('VIRGOLETTE: zero · SEGNAPOSTO: nessuno · ALTERNATIVE: nessuna (asserzioni vuote)',
   sum(u['italian'].count(QUOTE) for u in cov) == 0
   and not TAG.findall(''.join(u['italian'] for u in cov))
   and sum(len(ALT.findall(u['italian'])) for u in cov) == 0)
ck('APICI: 4 caratteri in inglese su 3 unita (743 x2, 781, 1159)',
   [(u['line'], u['english'].count(APOS)) for u in cov if u['english'].count(APOS)]
   == [(743, 2), (781, 1), (1159, 1)],
   [(u['line'], u['english'].count(APOS)) for u in cov if u['english'].count(APOS)])
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in cov for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessun doppio spazio (la tab iniziale non conta)',
   not [u['idx'] for u in cov if '  ' in u['italian'].lstrip(TAB)])
ck('rapporto nel gate 0,55-1,90',
   all(0.55 < u['ratio'] < 1.90 for u in cov),
   [(u['idx'], u['ratio']) for u in cov if not 0.55 < u['ratio'] < 1.90])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck('FILE: 17 unita prima (L318, righe 53-603)',
   db.execute('select count(*) from units where path=? and line<615', (PATH,)).fetchone()[0] == 17)
ck('FILE: ZERO unita dopo la 1222 — il lotto CHIUDE il file',
   db.execute('select count(*) from units where path=? and line>1222', (PATH,)).fetchone()[0] == 0)
ck('FILE: 39 unita (17 + 22), righe 53-1222, 37 DESCRIPTION + 2 VALUE',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (39, 53, 1222)
   and dict(db.execute('select kind,count(*) from units where path=? group by kind', (PATH,)).fetchall())
   == {'DESCRIPTION': 37, 'VALUE': 2})
ck('FILE: copertura 39/39 — il file e tutto qui',
   db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0] == 39)
ck('tutte le 22 unita di questo lotto sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · 20 DESCRIPTION + 2 VALUE in 15 contesti · 5 tab · FILE 39/39' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
