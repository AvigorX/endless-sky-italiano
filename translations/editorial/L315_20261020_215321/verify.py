r"""verify.py — L315 (`data/drak/drak culture conversations.txt`, righe 93-138). **LOTTO TERMINALE**.

Verifica da sola e verifica il **FILE INTERO** (che questo lotto chiude): **32 unita'**, **prima riga 26**, **ultima 138**, **zero
unita' dopo**, **somma dei lotti 16 + 16 = 32**, **righe distinte**. Poi il lotto: riga grezza, campi del DB, la **struttura dei tre
blocchi** (prima unita' senza tab), i **4 segnaposto con conteggio invertito**, le **zero virgolette**, i **3 apici inglesi**, la
seconda persona **distribuita per blocco**.

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
SECONDA = re.compile(r'\b(ti|tu|tuo|tua|tuoi|tue|te|hai|vedi|riesci|riapri|apri|trovi|alzi|ritrovi|'
                     r'batti|senti|guardi)\b', re.I)
HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
ROOT = os.path.abspath(os.path.join(L10N, '..'))
PATH = 'data/drak/drak culture conversations.txt'
PRIME = (93, 116, 134)
TAB_RIGHE = [94, 95, 96, 97, 98, 117, 118, 119, 120, 135, 136, 137, 138]
APICI_EN = {11: 1, 12: 1, 16: 1}
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


ck('riga grezza identica al sorgente (16/16)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = [u['idx'] for u in su
       if db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
       != (u['english'], u['kind'], u['path'], u['context'])]
ck('english/kind/path/context identici al DB', not bad, bad)
ck('16 unita, tutte MISSION_TEXT, 3 contesti (6 + 5 + 5)',
   len(tu) == 16 and collections.Counter(u['kind'] for u in tu) == {'MISSION_TEXT': 16}
   and collections.Counter(u['context'] for u in tu) == {
       'mission:Drak Revelations: Korath': 6, 'mission:Drak Revelations: Quarg': 5,
       'mission:Drak Revelations: Saryds': 5})
ck("ZERO unita' dopo la 138: il lotto chiude il file",
   db.execute('select count(*) from units where path=? and line>138', (PATH,)).fetchone()[0] == 0)
ck("16 unita' prima della 93 (L314)",
   db.execute('select count(*) from units where path=? and line<93', (PATH,)).fetchone()[0] == 16)
righe = set()
somma = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    us = [u for u in json.load(open(f, encoding='utf-8'))['units'] if u['path'] == PATH]
    if us:
        somma.append(len(us))
        righe |= {u['line'] for u in us}
ck('FILE: somma dei lotti 16 + 16 = 32', somma == [16, 16] and sum(somma) == 32, somma)
ck('FILE: 32 unita, 32 righe distinte, prima 26, ultima 138',
   len(righe) == 32 and min(righe) == 26 and max(righe) == 138
   and db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (32, 26, 138))
ck('FILE: copertura 32/32 (100%)',
   len(righe) == db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0], '%d/32' % len(righe))
ck('struttura: prime unita senza tab, le altre 13 con la tab in prima posizione',
   not [l for l in PRIME if at[l]['italian'].startswith(TAB)]
   and [u['line'] for u in tu if u['italian'].startswith(TAB)] == TAB_RIGHE)
ck('4 segnaposto identici, conteggio invertito rispetto a L314: <origin> x2, <ship> x2',
   collections.Counter(TAG.findall(''.join(u['italian'] for u in tu)))
   == collections.Counter(TAG.findall(''.join(u['english'] for u in tu)))
   == {'<origin>': 2, '<ship>': 2})
ck('VIRGOLETTE: zero (asserzione vuota)',
   sum(u['italian'].count(QUOTE) for u in tu) == 0)
ck('apici inglesi: 3, uno per unita nelle righe 120, 134, 138',
   {i: by[i]['english'].count(APOS) for i in APICI_EN} == APICI_EN
   and sum(u['english'].count(APOS) for u in tu) == 3)
_per = collections.Counter(u['context'] for u in tu if SECONDA.search(u['italian']))
ck('seconda persona: almeno tre unita per blocco, nove in tutto',
   all(_per[c] >= 3 for c in {u['context'] for u in tu}) and sum(_per.values()) >= 9, dict(_per))
ck('i tre svelamenti chiudono i tre blocchi',
   'abitacolo della <ship>' in at[98]['italian']
   and 'luci della nave' in at[120]['italian'] and 'porta del tuo abitacolo' in at[138]['italian'])
ck('Korath: creature di terra e ruggine, torri a cupola, bronzo, il crollo',
   all(k in ''.join(u['italian'] for u in tu if u['context'].endswith('Korath'))
       for k in ('terra e ruggine', 'torre a cupola', 'bronzo', 'crolla')))
ck('Quarg: il gigante scarno e le TOMBE',
   all(k in ''.join(u['italian'] for u in tu if u['context'].endswith('Quarg'))
       for k in ('scarno', 'tombe', 'nebbia')))
ck('Saryds: cervi d acciaio, argento, gabbie, fulmini, cadaveri',
   all(k in ''.join(u['italian'] for u in tu if u['context'].endswith('Saryds'))
       for k in ("cervi d'acciaio", 'argento', 'gabbie', 'fulmini', 'cadaveri')))
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
ck('tutte e 16 le unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in tu))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('FILE: 32/32 (100%) · prima riga 26 · ultima 138 · zero dopo · somma lotti 16+16')
print('parole EN %d -> IT %d · ratio %.2f - %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(u['ratio'] for u in tu), max(u['ratio'] for u in tu)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L315 superato' if not fail else 'verify L315 fallito')
raise SystemExit(0 if not fail else 1)
