r"""verify.py — L293 (`data/avgi/avgi culture conversations.txt`, righe 260-270). **LOTTO TERMINALE**.

Verifica da sola, e verifica il **FILE INTERO**: 46 unita', **somma dei lotti 8 + 12 + 17 + 9 = 46**, **righe distinte**,
**prima riga 24**, **ultima 270**, **zero unita' dopo**. Poi il lotto: riga grezza, campi del DB, **contesto unico**, **9 tab su
9**, **10 virgolette**, gli **atti dichiarati**, la **scommessa**, e che **nessun altro lotto** rivendichi le righe 260-270.

Indipendente da `check.py`: rilegge `source.json`, il `translation.json`, il database, il file del gioco e **tutti** i
`translation.json` dello staging.
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
PATH = 'data/avgi/avgi culture conversations.txt'
LINES = [260, 261, 262, 263, 264, 265, 266, 267, 270]
ATTI = ['Stupore.', 'Riposo.', 'Sconcerto.', 'Isteria.', 'Adorazione!']
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


ck('riga grezza identica al sorgente (9/9)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = [u['idx'] for u in su
       if db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
       != (u['english'], u['kind'], u['path'], u['context'])]
ck('english/kind/path/context identici al DB', not bad, bad)
ck('9 unita, righe tutte quelle dichiarate, tutte MISSION_TEXT, contesto unico',
   len(tu) == 9 and sorted(u['line'] for u in tu) == LINES and {u['kind'] for u in tu} == {'MISSION_TEXT'}
   and {u['context'] for u in tu} == {'mission:Avgi Culture: Fencing'},
   (sorted({u['line'] for u in tu}), {u['kind'] for u in tu}))
ck("37 unita' prima della 260 (8 + 12 + 17)",
   db.execute('select count(*) from units where path=? and line<260', (PATH,)).fetchone()[0] == 37)
ck("ZERO unita' dopo la 270: il lotto CHIUDE il file",
   db.execute('select count(*) from units where path=? and line>270', (PATH,)).fetchone()[0] == 0)
righe, lotti = set(), []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    us = [u for u in json.load(open(f, encoding='utf-8'))['units'] if u['path'] == PATH]
    if us:
        lotti.append((os.path.basename(os.path.dirname(f)), len(us)))
        righe |= {u['line'] for u in us}
ck('FILE: i quattro lotti sommano 46 unita (8 + 12 + 17 + 9)',
   [n for _, n in lotti] == [8, 12, 17, 9] and sum(n for _, n in lotti) == 46 == len(righe),
   (lotti, len(righe)))
ck('FILE: 46 unita, 46 righe distinte, prima 24, ultima 270',
   len(righe) == 46 and min(righe) == 24 and max(righe) == 270
   and db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (46, 24, 270))
ck('FILE: copertura 46/46 (100%)',
   len(righe) == db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0], '%d/46' % len(righe))
overlap = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    if os.path.basename(os.path.dirname(f)) == os.path.basename(HERE):
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH and 260 <= u['line'] <= 270:
            overlap.append((os.path.basename(os.path.dirname(f)), u['line']))
ck('nessun altro lotto rivendica le righe 260-270', not overlap, overlap)
ck('tutte e 9 le unita sono tradotte', all(u['italian'] != u['english'] for u in tu))
ck('tab: nove su nove, primo carattere',
   sum(u['english'].count(TAB) for u in tu) == 9 == sum(u['italian'].count(TAB) for u in tu)
   and all(at[l]['italian'].startswith(TAB) for l in LINES))
ck('atti dichiarati presenti, con «Adorazione!» esclamativo',
   all(a in ''.join(u['italian'] for u in tu) for a in ATTI)
   and '"Adorazione! Ti amo, Zomp!"' in at[265]['italian'])
ck('virgolette 10 in entrambe le lingue, per unita; zero segnaposto e alternative',
   sum(u['english'].count(QUOTE) for u in tu) == 10 == sum(u['italian'].count(QUOTE) for u in tu)
   and all(u['english'].count(QUOTE) == u['italian'].count(QUOTE) for u in tu)
   and sum(len(TAG.findall(u['english'])) for u in tu) == 0 == sum(len(TAG.findall(u['italian'])) for u in tu)
   and sum(len(ALT.findall(u['italian'])) for u in tu) == 0)
ck('apici: 5 in inglese, 14 in italiano',
   sum(u['english'].count(APOS) for u in tu) == 5 and sum(u['italian'].count(APOS) for u in tu) == 14,
   (sum(u['english'].count(APOS) for u in tu), sum(u['italian'].count(APOS) for u in tu)))
ck('la scommessa: «dieci a uno» per `10 to 1`',
   'dieci a uno' in at[264]['italian'] and '10 to 1' in at[264]['english'])
ck("coerenza con L292: «campione in carica» per `reigning champion`",
   'campione in carica' in at[263]['italian'])
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in tu for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90',
   all(0.55 < u['ratio'] < 1.90 for u in tu),
   [(u['idx'], u['ratio']) for u in tu if not 0.55 < u['ratio'] < 1.90])
ck('tutte le 9 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in tu))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('FILE: 46/46 (100%) · somma lotti 8+12+17+9 · prima riga 24 · ultima 270 · zero dopo')
print('parole EN %d -> IT %d · ratio %.2f - %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(u['ratio'] for u in tu), max(u['ratio'] for u in tu)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L293 superato' if not fail else 'verify L293 fallito')
raise SystemExit(0 if not fail else 1)
