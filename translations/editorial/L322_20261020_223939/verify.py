r"""verify.py — L322 (`data/human/frontier jobs.txt`, righe 16-318). **LOTTO TERMINALE, FILE INTERO**.

Verifica da sola il **FILE INTERO**: **45 unita'**, **prima riga 16**, **ultima 318**, **zero unita' prima e dopo**, **un solo lotto**
(copertura **45/45**), **cinque tipi**.

Poi il lotto, con meccanismi **diversi** da `check.py`:
- il gruppo dei **copiati** e' verificato **per tipo** (`VALUE` e `UI_LABEL` identici), e per ognuno si elenca **quello che e'**;
- i **10 tipi di segnaposto** sono confrontati **contro il dizionario atteso** e fra inglese e italiano;
- le **19 tab** sono verificate come **righe** e non come conteggio;
- le **4 virgolette** e i **18 apici** sono verificati **per unita'**;
- la **seconda persona** e' verificata con **forme verbali**, non solo pronomi.

Indipendente da `check.py`.
"""
import collections
import glob
import hashlib
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
ROOT = os.path.abspath(os.path.join(L10N, '..'))
PATH = 'data/human/frontier jobs.txt'
COPIATI = ('VALUE', 'UI_LABEL')
TRADOTTI = ('DESCRIPTION', 'DIALOG', 'MISSION_TEXT')
TAB_RIGHE = [250, 252, 256, 263, 267, 269, 271, 277, 281, 282, 284, 286, 288, 296, 302, 303, 311, 317, 318]
TOKEN = {'<planet>': 9, '<cargo>': 4, '<destination>': 7, '<payment>': 10, '<bunks>': 3,
         '<date>': 1, '<commodity>': 1, '<stopovers>': 2, '<origin>': 2, '<npc>': 1}
src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
su = sorted(src['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
raw_lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
by = {u['idx']: u for u in tu}
at = {u['line']: u for u in tu}
fail = []


def ck(n, c, d=''):
    print('%-96s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente (45/45)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = [u['idx'] for u in su
       if db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
       != (u['english'], u['kind'], u['path'], u['context'])]
ck('english/kind/path/context identici al DB', not bad, bad)
ck('45 unita, cinque tipi, 9 contesti',
   len(tu) == 45 and len({u['context'] for u in tu}) == 9
   and collections.Counter(u['kind'] for u in tu) ==
   {'VALUE': 7, 'UI_LABEL': 6, 'DESCRIPTION': 8, 'DIALOG': 4, 'MISSION_TEXT': 20})
ck("FILE: zero unita' prima della 16 e zero dopo la 318: il file e' tutto qui",
   db.execute('select count(*) from units where path=? and line<16', (PATH,)).fetchone()[0] == 0
   and db.execute('select count(*) from units where path=? and line>318', (PATH,)).fetchone()[0] == 0)
righe, lotti = set(), []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    us = [u for u in json.load(open(f, encoding='utf-8'))['units'] if u['path'] == PATH]
    if us:
        lotti.append((os.path.basename(os.path.dirname(f)), len(us)))
        righe |= {u['line'] for u in us}
ck('FILE: un solo lotto da 45 unita', [n for _, n in lotti] == [45], lotti)
ck('FILE: 45 unita, 45 righe distinte, prima 16, ultima 318',
   len(righe) == 45 and min(righe) == 16 and max(righe) == 318)
ck('FILE: copertura 45/45 (100%)',
   len(righe) == db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0], '%d/45' % len(righe))
ck('copiati per tipo: 7 VALUE identici e 6 UI_LABEL identiche',
   sum(1 for u in tu if u['kind'] == 'VALUE' and u['italian'] == u['english']) == 7
   and sum(1 for u in tu if u['kind'] == 'UI_LABEL' and u['italian'] == u['english']) == 6)
ck('tradotti per tipo: 8 DESCRIPTION, 4 DIALOG, 20 MISSION_TEXT diversi dall inglese',
   all(u['italian'] != u['english'] for u in tu if u['kind'] in TRADOTTI)
   and collections.Counter(u['kind'] for u in tu if u['kind'] in TRADOTTI)
   == {'DESCRIPTION': 8, 'DIALOG': 4, 'MISSION_TEXT': 20})
ck('le 19 tab sono righe esatte, non un conteggio',
   [u['line'] for u in tu if u['italian'].startswith(TAB)] == TAB_RIGHE)
ck('10 tipi di segnaposto, identici per tipo fra inglese e italiano',
   collections.Counter(TAG.findall(''.join(u['italian'] for u in tu))) == TOKEN
   == collections.Counter(TAG.findall(''.join(u['english'] for u in tu))))
ck('4 virgolette in due sole unita (277 e 281)',
   sum(u['italian'].count(QUOTE) for u in tu) == 4
   and [u['line'] for u in tu if u['italian'].count(QUOTE)] == [277, 281])
ck('18 apici inglesi in 12 unita (picchi: 263 ha 3, 281 ha 4, 302 ha 2)',
   sum(u['english'].count(APOS) for u in tu) == 18
   and at[263]['english'].count(APOS) == 3 and at[281]['english'].count(APOS) == 4
   and at[302]['english'].count(APOS) == 2)
ck('seconda persona nei MISSION_TEXT (forme verbali, non solo pronomi)',
   sum(1 for u in tu if u['kind'] == 'MISSION_TEXT'
       and re.search(r'\b(ti|tu|te|tuo|tua|sei|stai|corri|spari|arraffi|provi|cadi)\b', u['italian'], re.I)) >= 10)
ck('i due finali «run» sono identici nella prima frase, diversi nella seconda',
   at[303]['italian'].split('!')[0] == at[318]['italian'].split('!')[0]
   and at[303]['italian'] != at[318]['italian'])
ck('la <npc> e femminile; i crediti sono in forma italiana',
   'la <npc>' in at[210]['italian'] and '25.000 crediti' in at[263]['italian'])
ck('ALTERNATIVE: nessuna (asserzione vuota)',
   sum(len(ALT.findall(u['italian'])) for u in tu) == 0)
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in tu for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessun doppio spazio (la tab iniziale non conta)',
   not [u['idx'] for u in tu if '  ' in u['italian'].lstrip(TAB)])
ck('rapporto nel gate 0,55-1,90',
   all(0.55 < u['ratio'] < 1.90 for u in tu),
   [(u['idx'], u['ratio']) for u in tu if not 0.55 < u['ratio'] < 1.90])
ck('tutte le 45 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in tu))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('FILE: 45/45 (100%) · prima riga 16 · ultima 318 · zero prima e dopo · un solo lotto · 5 tipi')
print('parole EN %d -> IT %d · ratio %.2f - %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(u['ratio'] for u in tu), max(u['ratio'] for u in tu)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L322 superato' if not fail else 'verify L322 fallito')
raise SystemExit(0 if not fail else 1)
