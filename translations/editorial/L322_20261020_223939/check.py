r"""check.py — L322 (`data/human/frontier jobs.txt`, righe 16-318). **LOTTO TERMINALE, FILE INTERO**.

**Il primo lotto a CINQUE TIPI**, e il test e' scritto **per gruppo**, mai su una somma unica:

| gruppo | tipi | unita' | trattamento |
|---|---|---|---|
| **A — copiati** | `VALUE` (7) + `UI_LABEL` (6) | **13** | **identici all'inglese** |
| **B — tradotti** | `DESCRIPTION` (8) + `DIALOG` (4) + `MISSION_TEXT` (20) | **32** | **diversi dall'inglese** |

Le 6 `UI_LABEL` sono **etichette di salto** della conversazione (`good luck`, `shoot and die`…): il testo le sembra prosa, il codice le
usa come **`goto`** — quindi **non sono visibili** e si copiano.

Poi: **19 tab**, **4 virgolette** in **due** unita' (277 e 281, due coppie ciascuna), **18 apici** in **12** unita' con i picchi
(263: 3, 281: 4, 302: 2), i **10 tipi di segnaposto** con i loro conteggi, la **seconda persona** nei `MISSION_TEXT`, e l'invariante di
**FILE** (45 unita', prima 16, ultima 318, zero dopo).
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
PATH = 'data/human/frontier jobs.txt'
COPIATI = {'VALUE': 7, 'UI_LABEL': 6}
TRADOTTI = {'DESCRIPTION': 8, 'DIALOG': 4, 'MISSION_TEXT': 20}
TAB_RIGHE = [250, 252, 256, 263, 267, 269, 271, 277, 281, 282, 284, 286, 288, 296, 302, 303, 311, 317, 318]
VIRG = {277: 2, 281: 2}
APICI_EN = {208: 1, 210: 1, 213: 1, 248: 1, 256: 1, 263: 3, 267: 1, 281: 4, 296: 1, 302: 2, 303: 1, 318: 1}
TOKEN = {'<planet>': 9, '<cargo>': 4, '<destination>': 7, '<payment>': 10, '<bunks>': 3,
         '<date>': 1, '<commodity>': 1, '<stopovers>': 2, '<origin>': 2, '<npc>': 1}
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


kinds = collections.Counter(u['kind'] for u in cov)
ck('unita tradotte 45/45', len(cov) == 45 == len(units), '%d/%d' % (len(cov), len(units)))
ck('cinque tipi: 7 VALUE + 6 UI_LABEL + 8 DESCRIPTION + 4 DIALOG + 20 MISSION_TEXT',
   kinds == {'VALUE': 7, 'UI_LABEL': 6, 'DESCRIPTION': 8, 'DIALOG': 4, 'MISSION_TEXT': 20}, dict(kinds))
ck('GRUPPO A — i 13 copiati (VALUE e UI_LABEL) sono IDENTICI all inglese',
   all(u['italian'] == u['english'] for u in cov if u['kind'] in COPIATI)
   and sum(1 for u in cov if u['kind'] in COPIATI) == 13,
   [(u['line'], u['kind']) for u in cov if u['kind'] in COPIATI and u['italian'] != u['english']])
ck('GRUPPO B — i 32 tradotti sono DIVERSI dall inglese',
   all(u['italian'] != u['english'] for u in cov if u['kind'] in TRADOTTI)
   and sum(1 for u in cov if u['kind'] in TRADOTTI) == 32,
   [(u['line'], u['kind']) for u in cov if u['kind'] in TRADOTTI and u['italian'] == u['english']])
ck('le sei UI_LABEL sono etichette di salto, non prosa: elencate',
   [u['italian'] for u in cov if u['kind'] == 'UI_LABEL'] ==
   ['good luck', 'bad luck', 'shoot and die', 'shoot and run', 'grab and die', 'grab and run'],
   [u['italian'] for u in cov if u['kind'] == 'UI_LABEL'])
ck('i sette VALUE sono titoli con segnaposto, elencati',
   collections.Counter(u['italian'] for u in cov if u['kind'] == 'VALUE') ==
   {'Frontier delivery to <planet>': 3, 'Emigration to <planet>': 3, 'Disaster relief to <planet>': 1},
   collections.Counter(u['italian'] for u in cov if u['kind'] == 'VALUE'))
ck('19 tab, alle righe attese e come PRIMO carattere',
   [u['line'] for u in cov if u['italian'].startswith(TAB)] == TAB_RIGHE,
   [u['line'] for u in cov if u['italian'].startswith(TAB)])
ck('4 virgolette in DUE unita (277 e 281, due coppie ciascuna)',
   {u['line']: u['italian'].count(QUOTE) for u in cov if u['italian'].count(QUOTE)} == VIRG,
   {u['line']: u['italian'].count(QUOTE) for u in cov if u['italian'].count(QUOTE)})
ck('18 apici inglesi in 12 unita, con i picchi 263 (3), 281 (4), 302 (2)',
   {u['line']: u['english'].count(APOS) for u in cov if u['english'].count(APOS)} == APICI_EN
   and sum(u['english'].count(APOS) for u in cov) == 18,
   {u['line']: u['english'].count(APOS) for u in cov if u['english'].count(APOS)})
ck('i 10 tipi di SEGNAPOSTO sono identici per tipo, non solo in totale',
   collections.Counter(TAG.findall(''.join(u['italian'] for u in cov))) == TOKEN
   == collections.Counter(TAG.findall(''.join(u['english'] for u in cov))),
   dict(collections.Counter(TAG.findall(''.join(u['italian'] for u in cov)))))
ck('la seconda persona e il registro dei MISSION_TEXT: presente in molte unita',
   sum(1 for u in cov if u['kind'] == 'MISSION_TEXT'
       and re.search(r'\b(ti|tu|tuo|tua|te|sei|stai|corri|spari|arraffi)\b', u['italian'], re.I)) >= 10,
   sum(1 for u in cov if u['kind'] == 'MISSION_TEXT'
       and re.search(r'\b(ti|tu|tuo|tua|te|sei|stai|corri|spari|arraffi)\b', u['italian'], re.I)))
ck('le tre consegne sono IDENTICHE fra loro, e cosi le tre emigrazioni',
   by[2]['italian'] == by[4]['italian'] == by[6]['italian']
   and by[8]['italian'] == by[10]['italian'] == by[12]['italian'])
ck('la Disastro: catastrofe, colonia, entro <date>',
   'catastrofe' in at[173]['italian'] and 'colonia' in at[173]['italian']
   and 'entro <date>' in at[173]['italian'])
ck('l istruttore: la <npc> e femminile e va scortata',
   'la <npc>' in at[210]['italian'] and '<stopovers>' in at[210]['italian'])
ck('il gioco d azzardo: quattro scelte e quattro finali',
   all(at[l]['italian'].lstrip(TAB).startswith('(') for l in (250, 252, 269, 271, 284, 286, 288))
   and '25.000 crediti' in at[263]['italian'] and '15.000 crediti' in at[277]['italian'])
ck('ALTERNATIVE: nessuna (asserzione vuota)', sum(len(ALT.findall(u['italian'])) for u in cov) == 0)
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in cov for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessun doppio spazio (la tab iniziale non conta)',
   not [u['idx'] for u in cov if '  ' in u['italian'].lstrip(TAB)])
ck('rapporto nel gate 0,55-1,90',
   all(0.55 < u['ratio'] < 1.90 for u in cov),
   [(u['idx'], u['ratio']) for u in cov if not 0.55 < u['ratio'] < 1.90])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("FILE: ZERO unita' prima della 16 — il lotto APRE il file",
   db.execute('select count(*) from units where path=? and line<16', (PATH,)).fetchone()[0] == 0)
ck("FILE: ZERO unita' dopo la 318 — il lotto CHIUDE il file",
   db.execute('select count(*) from units where path=? and line>318', (PATH,)).fetchone()[0] == 0)
ck('FILE: 45 unita, righe 16-318, cinque tipi',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (45, 16, 318)
   and dict(db.execute('select kind,count(*) from units where path=? group by kind', (PATH,)).fetchall())
   == {'VALUE': 7, 'UI_LABEL': 6, 'DESCRIPTION': 8, 'DIALOG': 4, 'MISSION_TEXT': 20})
ck('FILE: copertura 45/45 — il file e tutto qui',
   db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0] == 45)
ck('tutte le 45 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · 5 tipi (13 copiati / 32 tradotti) in 9 contesti · 19 tab · 4 virgolette · FILE 45/45' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
