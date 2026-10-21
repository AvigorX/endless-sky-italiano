r"""verify.py — L310 (`data/korath/korath culture conversations.txt`, righe 26-75). **LOTTO TERMINALE, FILE INTERO**.

Verifica da sola, e verifica il **FILE INTERO** (che e' tutto qui): **27 unita'**, **prima riga 26**, **ultima 75**, **zero unita'
prima e dopo**. Poi il lotto: riga grezza, campi del DB, **UI_LABEL copiati**, le **14 virgolette per unita'**, i **3 segnaposto
identici**, le **23 tab**, la **seconda persona narrante**, le **quattro offerte** e i **nomi invariati**.

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
PATH = 'data/korath/korath culture conversations.txt'
CONTEXT = "mission:Korath Far'en Lai Prayer"
UI = {21: 'small credits', 23: 'medium credits', 25: 'large credits'}
QUOTED = {8: 2, 9: 2, 11: 2, 12: 2, 13: 4, 19: 2}
OFFERTE = {15: '100 crediti', 16: '10.000 crediti', 17: '10.000.000 crediti', 18: 'una fotografia'}
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


ck('riga grezza identica al sorgente (27/27)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = [u['idx'] for u in su
       if db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
       != (u['english'], u['kind'], u['path'], u['context'])]
ck('english/kind/path/context identici al DB', not bad, bad)
kinds = collections.Counter(u['kind'] for u in tu)
ck('27 unita: 24 MISSION_TEXT + 3 UI_LABEL',
   len(tu) == 27 and kinds == {'MISSION_TEXT': 24, 'UI_LABEL': 3}, dict(kinds))
ck('UN SOLO contesto', {u['context'] for u in tu} == {CONTEXT})
ck("ZERO unita' prima della 26 e ZERO dopo la 75: il file e' tutto qui",
   db.execute('select count(*) from units where path=? and line<26', (PATH,)).fetchone()[0] == 0
   and db.execute('select count(*) from units where path=? and line>75', (PATH,)).fetchone()[0] == 0)
righe, lotti = set(), []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    us = [u for u in json.load(open(f, encoding='utf-8'))['units'] if u['path'] == PATH]
    if us:
        lotti.append((os.path.basename(os.path.dirname(f)), len(us)))
        righe |= {u['line'] for u in us}
ck('FILE: un solo lotto da 27 unita', [n for _, n in lotti] == [27], lotti)
ck('FILE: 27 unita, 27 righe distinte, prima 26, ultima 75',
   len(righe) == 27 and min(righe) == 26 and max(righe) == 75
   and db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (27, 26, 75))
ck('FILE: copertura 27/27 (100%)',
   len(righe) == db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0], '%d/27' % len(righe))
overlap = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    if os.path.basename(os.path.dirname(f)) == os.path.basename(HERE):
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH:
            overlap.append((os.path.basename(os.path.dirname(f)), u['line']))
ck('nessun altro lotto tocca questo file', not overlap, overlap)
ck('tutte e 27 le unita sono in staging e coerenti col tipo',
   all((u['italian'] != u['english']) if u['kind'] == 'MISSION_TEXT' else (u['italian'] == u['english'])
       for u in tu))
ck('UI_LABEL copiati', all(by[i]['italian'] == v == by[i]['english'] for i, v in UI.items()))
ck('14 virgolette, per unita', sum(u['italian'].count(QUOTE) for u in tu) == 14
   and {i: by[i]['italian'].count(QUOTE) for i in QUOTED} == QUOTED)
ck('3 segnaposto identici',
   collections.Counter(TAG.findall(''.join(u['italian'] for u in tu)))
   == collections.Counter(TAG.findall(''.join(u['english'] for u in tu))) == {'<origin>': 2, '<home planet>': 1})
ck('23 tab: tutte le MISSION_TEXT tranne la 26',
   sum(u['italian'].count(TAB) for u in tu) == 23
   and not at[26]['italian'].startswith(TAB)
   and all(at[u['line']]['italian'].startswith(TAB) for u in tu
           if u['kind'] == 'MISSION_TEXT' and u['line'] != 26))
ck('seconda persona narrante presente (pronome e verbo)',
   'ti serve' in at[26]['italian'] and 'noti' in at[27]['italian'] and 'Ti ricordi' in at[58]['italian'])
ck('le quattro offerte conservano parentesi e valori italiani',
   all(v in by[i]['italian'] and by[i]['italian'].lstrip(TAB).startswith('(') for i, v in OFFERTE.items()))
ck('nomi invariati: Korath, Far\'en Lai, "humani efreti"',
   "Far'en Lai" in ''.join(u['italian'] for u in tu)
   and 'humani efreti' in at[33]['italian'])
ck('ASSERZIONI VUOTE: 0 alternative', sum(len(ALT.findall(u['italian'])) for u in tu) == 0)
ck('apici: 10 in inglese, 12 in italiano',
   sum(u['english'].count(APOS) for u in tu) == 10 and sum(u['italian'].count(APOS) for u in tu) == 12,
   (sum(u['english'].count(APOS) for u in tu), sum(u['italian'].count(APOS) for u in tu)))
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in tu for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessun doppio spazio (la tab iniziale non conta)',
   not [u['idx'] for u in tu if '  ' in u['italian'].lstrip(TAB)])
ck('rapporto nel gate 0,55-1,90',
   all(0.55 < u['ratio'] < 1.90 for u in tu),
   [(u['idx'], u['ratio']) for u in tu if not 0.55 < u['ratio'] < 1.90])
ck('tutte le 27 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in tu))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('FILE: 27/27 (100%) · prima riga 26 · ultima 75 · zero prima e dopo · un solo contesto')
print('parole EN %d -> IT %d · ratio %.2f - %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(u['ratio'] for u in tu), max(u['ratio'] for u in tu)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L310 superato' if not fail else 'verify L310 fallito')
raise SystemExit(0 if not fail else 1)
