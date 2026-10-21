r"""check.py — L325 (`data/kahet/kahet outfits.txt`, righe 54-573). **LOTTO TERMINALE, FILE INTERO**.

Venticinque unita' in **venti contesti** e **due tipi**: **22 `DESCRIPTION`** da tradurre e **3 `VALUE`** da **copiare**.

Il test difende:

1. **i tre `VALUE` copiati all'identico** — `Maeri Engine Nacelles` (444), `Ka'het Sustainer Nacelles` (468), `Telis Engine
   Nacelles` (492): confronto per **identita'**, non per disuguaglianza;
2. **le cinque coppie** di contesti con **due** unita' ciascuno (EMP Deployer, Grand Restorer, Maeri, Ka'het Sustainer, Telis);
3. **le 2 tab** (285, 400), entrambe su una **nota** che segue la scheda;
4. **la nota dei rifornimenti** (285), quinta occorrenza: confronto con la **resa di maggioranza** del corpus;
5. **i 17 apici inglesi in 15 unita'**, con **425** e **561** che ne hanno **due**;
6. **la genealogia dei Costruttori**: `Ka'mar` droni -> `Het` navi -> `Ka'het`; `Ka'mar`, `Mar`, `Het`, `Ka'het`, `Telis'het`
   restano **invariati**.

E l'invariante di **FILE**: 25 unita', prima 54, ultima 573, zero prima e dopo.
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
PATH = 'data/kahet/kahet outfits.txt'
NOTA_EN = TAB + 'Ammunition for this weapon can be restocked at any outfitter.'
NOTA_IT = TAB + "Le munizioni per quest'arma possono essere rifornite presso qualsiasi emporio."
TAB_RIGHE = [285, 400]
APICI_EN = {166: 1, 359: 1, 372: 1, 399: 1, 400: 1, 414: 1, 425: 2, 465: 1, 468: 1,
            489: 1, 513: 1, 536: 1, 561: 2, 573: 1, 323: 1}
VALUE = {444: 'Maeri Engine Nacelles', 468: "Ka'het Sustainer Nacelles", 492: 'Telis Engine Nacelles'}
COPPIE = ["Ka'het EMP Deployer", "Ka'het Grand Restorer", 'Maeri Engine Nacelles',
          "Ka'het Sustainer Nacelles", 'Telis Engine Nacelles']
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


ck('unita tradotte 25/25', len(cov) == 25 == len(units), '%d/%d' % (len(cov), len(units)))
ck('22 DESCRIPTION + 3 VALUE',
   collections.Counter(u['kind'] for u in cov) == {'DESCRIPTION': 22, 'VALUE': 3},
   dict(collections.Counter(u['kind'] for u in cov)))
ck('20 contesti: cinque con DUE unita, quindici con una',
   len({u['context'] for u in cov}) == 20
   and sorted(collections.Counter(u['context'] for u in cov).values(), reverse=True)
   == [2, 2, 2, 2, 2] + [1] * 15,
   sorted(collections.Counter(u['context'] for u in cov).values(), reverse=True))
ck('le cinque coppie sono esattamente quelle attese',
   [c for c, n in collections.Counter(u['context'] for u in cov).items() if n == 2]
   == ['outfit:' + c for c in COPPIE],
   [c for c, n in collections.Counter(u['context'] for u in cov).items() if n == 2])
ck('i tre VALUE sono COPIATI all identico',
   all(at[l]['italian'] == at[l]['english'] == v for l, v in VALUE.items())
   and all(at[l]['kind'] == 'VALUE' for l in VALUE),
   [(l, at[l]['italian'], at[l]['english']) for l in VALUE if at[l]['italian'] != at[l]['english']])
ck('i tre VALUE NON sono tradotti (nessuna gondola, nessun motore)',
   not [l for l in VALUE if 'ondol' in at[l]['italian'] or 'otore' in at[l]['italian']])
ck('le 2 tab sono alle righe 285 e 400, come PRIMO carattere',
   [u['line'] for u in cov if u['italian'].startswith(TAB)] == TAB_RIGHE
   and at[285]['context'] == "outfit:Ka'het EMP Deployer"
   and at[400]['context'] == "outfit:Ka'het Grand Restorer"
   and all(not u['italian'].startswith(' ') for u in cov if u['line'] in TAB_RIGHE))
ck('la nota dei rifornimenti (285) usa la resa di maggioranza del corpus',
   at[285]['english'] == NOTA_EN and at[285]['italian'] == NOTA_IT)
ck('la genealogia: Ka mar (droni) -> Het (navi) -> Ka het',
   "Ka'mar" in at[414]['italian'] and 'Het' in at[414]['italian']
   and "Ka'het" in at[561]['italian'] and "Ka'mar" in at[561]['italian']
   and 'molto prima che i Ka het esistessero' not in at[561]['italian']
   and "molto prima che i Ka'het esistessero" in at[561]['italian'])
ck('`Ka het`, `Ka mar`, `Het`, `Telis het` restano invariati',
   all("\u2019" not in u['italian'] and "\u2018" not in u['italian'] for u in cov)
   and sum(u['italian'].count("Ka'het") for u in cov) == 8
   and sum(u['italian'].count("Ka'mar") for u in cov) == 3
   and sum(u['italian'].count("Telis'het") for u in cov) == 1
   and sum(u['italian'].count('Costruttori') for u in cov) == 11
   and sum(u['italian'].count('Builders') for u in cov) == 0,
   (sum(u['italian'].count("Ka'het") for u in cov), sum(u['italian'].count("Ka'mar") for u in cov)))
ck('il Nullifier: nessun danno a scudi e scafo, ma DISATTIVA i reattori',
   'disattivare' in at[54]['italian'] and 'pochi secondi' in at[54]['italian'])
ck('il Ravager Beam: nato per l ESTRAZIONE, capito in guerra suo malgrado',
   'estrazione dagli asteroidi' in at[138]['italian'] and 'si rivoltò contro di loro' in at[138]['italian'])
ck("l'EMP Deployer: armi aliene che ignoravano lo scafo, effetti REPLICATI",
   'ignorare lo scafo' in at[284]['italian'] and 'replicarne gli effetti' in at[284]['italian'])
ck('il Grand Restorer: nato per NECESSITA, non perfezionato in secoli',
   'per necessità' in at[399]['italian'] and 'rigeneratori di base' in at[399]['italian'])
ck("l'Ion Trap: converte tempeste pericolose in energia UTILE",
   'tempeste pericolose in energia utile' in at[439]['italian'])
ck('il Compact Engine: nessuna energia per accendersi NON e vero, ne serve un po',
   'richiede un po' in at[561]['italian'] and 'consumo costante' in at[561]['italian'])
ck('lo Stunner e l unica unita con la seconda persona (la tua nave)',
   [u['line'] for u in cov if re.search(r'\b(tua|tuo|tu)\b', u['italian'])] == [573],
   [u['line'] for u in cov if re.search(r'\b(tua|tuo|tu)\b', u['italian'])])
ck('VIRGOLETTE: zero · SEGNAPOSTO: nessuno · ALTERNATIVE: nessuna (asserzioni vuote)',
   sum(u['italian'].count(QUOTE) for u in cov) == 0
   and not TAG.findall(''.join(u['italian'] for u in cov))
   and sum(len(ALT.findall(u['italian'])) for u in cov) == 0)
ck('APICI: 17 caratteri in inglese su 15 unita',
   {u['line']: u['english'].count(APOS) for u in cov if u['english'].count(APOS)} == APICI_EN
   and sum(u['english'].count(APOS) for u in cov) == 17,
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
ck("FILE: ZERO unita' prima della 54 — il lotto APRE il file",
   db.execute('select count(*) from units where path=? and line<54', (PATH,)).fetchone()[0] == 0)
ck("FILE: ZERO unita' dopo la 573 — il lotto CHIUDE il file",
   db.execute('select count(*) from units where path=? and line>573', (PATH,)).fetchone()[0] == 0)
ck('FILE: 25 unita, righe 54-573, 22 DESCRIPTION + 3 VALUE',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (25, 54, 573)
   and dict(db.execute('select kind,count(*) from units where path=? group by kind', (PATH,)).fetchall())
   == {'DESCRIPTION': 22, 'VALUE': 3})
ck('FILE: copertura 25/25 — il file e tutto qui',
   db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0] == 25)
ck('tutte le 25 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · 22 DESCRIPTION + 3 VALUE in 20 contesti · 2 tab · FILE 25/25' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
