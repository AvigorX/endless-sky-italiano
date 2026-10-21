r"""verify.py — L264 (`data/remnant/remnant jobs.txt`, righe 703-741). **LOTTO TERMINALE**.

**Invariante di FILE**: dopo questo lotto `remnant jobs.txt` deve avere **87 unita' distinte su 87**
(`25 + 29 + 24 + 9`), la riga **741** come ultima e **0** unita' dopo; le righe dei quattro lotti devono coincidere
**esattamente** con quelle del database.

Verifica da sola: riga grezza, campi del DB, i due contesti in sequenza, i **8 segnaposto**, la distinzione
**disabilitare/distruggere**, gli apici e che **nessun altro lotto** rivendichi queste righe.

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
HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
ROOT = os.path.abspath(os.path.join(L10N, '..'))
PATH = 'data/remnant/remnant jobs.txt'
CTX_A, CTX_B = 'mission:Remnant: Rescue 5', 'mission:Remnant: Disable 1'
src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
su = sorted(src['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
raw_lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
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
ck('9 unita, righe 703-741, tipi 5/2/1/1',
   len(tu) == 9 and [u['line'] for u in tu] == sorted({u['line'] for u in tu})
   and collections.Counter(u['kind'] for u in tu)
   == {'DIALOG': 5, 'MISSION_TEXT': 2, 'VALUE': 1, 'DESCRIPTION': 1},
   (len(tu), collections.Counter(u['kind'] for u in tu)))
ck('i due contesti compaiono in quest ordine, senza altri',
   [c for c in dict.fromkeys(u['context'] for u in tu)] == [CTX_A, CTX_B],
   [c for c in dict.fromkeys(u['context'] for u in tu)])
ck("78 unita' prima, e la precedente e in `Rescue 5`",
   db.execute('select count(*) from units where path=? and line<703', (PATH,)).fetchone()[0] == 78
   and db.execute('select context from units where path=? and line<703 order by line desc limit 1', (PATH,)).fetchone()
   == (CTX_A,))
ck("ZERO unita' dopo la 741: il lotto CHIUDE il file",
   db.execute('select count(*) from units where path=? and line>741', (PATH,)).fetchone()[0] == 0)
ck("la 741 e l'ultima riga del file (87 unita', righe 19 - 741)",
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (87, 19, 741))
lotti, righe = [], set()
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    us = [u for u in json.load(open(f, encoding='utf-8'))['units'] if u['path'] == PATH]
    if us:
        lotti.append((os.path.basename(os.path.dirname(f)), len(us)))
        righe |= {u['line'] for u in us}
ck('INVARIANTE DI FILE: 4 lotti (25 + 29 + 24 + 9) coprono 87 righe distinte su 87',
   [n for _, n in lotti] == [25, 29, 24, 9] and len(righe) == 87, (lotti, len(righe)))
ck('nessun buco: le 87 righe dei lotti sono esattamente quelle del database',
   righe == {l for l, in db.execute('select line from units where path=?', (PATH,))})
overlap = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    if os.path.basename(os.path.dirname(f)) == os.path.basename(HERE):
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH and 703 <= u['line'] <= 741:
            overlap.append((os.path.basename(os.path.dirname(f)), u['line']))
ck('nessun altro lotto rivendica le righe 703-741', not overlap, overlap)
ck('copertura: 87/87 (100%)', len(righe) == 87, '%d/87' % len(righe))
ck('il VALUE e copiato; le altre 8 unita sono tradotte',
   all(u['italian'] == u['english'] for u in tu if u['kind'] == 'VALUE')
   and all(u['italian'] != u['english'] for u in tu if u['kind'] != 'VALUE'))
ck('ZERO tab e ZERO virgolette in entrambe le lingue',
   sum(u['english'].count(TAB) + u['italian'].count(TAB) for u in tu) == 0
   and sum(u['english'].count(QUOTE) + u['italian'].count(QUOTE) for u in tu) == 0)
ck('APICI: 7 in inglese (6 da A\'awoj, 1 da You\'ve), 8 in italiano su 8 unita',
   sum(u['english'].count(APOS) for u in tu) == 7 and sum(u['italian'].count(APOS) for u in tu) == 8
   and sorted(u['idx'] for u in tu if APOS in u['italian']) == [1, 2, 3, 4, 5, 6, 8, 9],
   (sum(u['english'].count(APOS) for u in tu), sum(u['italian'].count(APOS) for u in tu)))
ck('SEGNAPOSTI: 8 in 3 famiglie, con ordine identico per unita',
   collections.Counter(t for u in tu for t in TAG.findall(u['english'])) ==
   collections.Counter(t for u in tu for t in TAG.findall(u['italian'])) ==
   collections.Counter({'<payment>': 3, '<planet>': 3, '<npc>': 2})
   and not [u['idx'] for u in tu if TAG.findall(u['english']) != TAG.findall(u['italian'])])
by = {u['idx']: u for u in tu}
ck('disabilitare e distruggere restano distinti: «distrugger» compare solo nel fallimento (unita 8)',
   [u['idx'] for u in tu if 'distrugger' in u['italian']] == [8]
   and 'disabilitarla' in by[4]['italian'] and 'disabilitato' in by[9]['italian'])
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in tu for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90 per ogni unita',
   all(0.55 < u['ratio'] < 1.90 for u in tu),
   [(u['idx'], u['ratio']) for u in tu if not 0.55 < u['ratio'] < 1.90])
ck('tutte le 9 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in tu))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print("FILE: 87/87 unita' · 4 lotti (25 + 29 + 24 + 9) · 87 righe distinte · ultima riga 741 · 0 dopo")
print('parole EN %d -> IT %d · ratio %.2f - %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(u['ratio'] for u in tu), max(u['ratio'] for u in tu)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L264 superato' if not fail else 'verify L264 fallito')
raise SystemExit(0 if not fail else 1)
