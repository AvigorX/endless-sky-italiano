r"""verify.py — L260 (`data/human/post-war reactions.txt`, righe 253-264). **LOTTO TERMINALE**.

**Invariante di FILE**: dopo questo lotto `post-war reactions.txt` deve avere **87 unita' distinte su 87**
(`22 + 23 + 20 + 15 + 7`), la riga **264** come ultima e **0** unita' dopo; le righe dei cinque lotti devono coincidere
**esattamente** con quelle del database.

Verifica da sola: riga grezza, campi del DB, contesto unico, **7 tab**, **16 virgolette** (con le due unita' di narrazione a
zero), gli **apici**, **zero segnaposto**, e che **nessun altro lotto** rivendichi queste righe.

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
PATH = 'data/human/post-war reactions.txt'
CTX = 'mission:War Reactions: Syndicate Orphan'
src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
su = sorted(src['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
raw_lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
fail = []


def ck(n, c, d=''):
    print('%-96s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente (7/7)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = [u['idx'] for u in su
       if db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
       != (u['english'], u['kind'], u['path'], u['context'])]
ck('english/kind/path/context identici al DB', not bad, bad)
ck('7 unita, righe 253-264, tutte MISSION_TEXT in un solo contesto',
   len(tu) == 7 and [u['line'] for u in tu] == sorted({u['line'] for u in tu})
   and {u['kind'] for u in tu} == {'MISSION_TEXT'} and {u['context'] for u in tu} == {CTX},
   (len(tu), {u['kind'] for u in tu}, {u['context'] for u in tu}))
ck("80 unita' prima, e la precedente e nello stesso contesto",
   db.execute('select count(*) from units where path=? and line<253', (PATH,)).fetchone()[0] == 80
   and db.execute('select context from units where path=? and line<253 order by line desc limit 1', (PATH,)).fetchone()
   == (CTX,))
ck("ZERO unita' dopo la 264: il lotto CHIUDE il file",
   db.execute('select count(*) from units where path=? and line>264', (PATH,)).fetchone()[0] == 0)
ck("la 264 e' l'ultima riga del file (87 unita', righe 40 - 264)",
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (87, 40, 264))
lotti, righe = [], set()
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    us = [u for u in json.load(open(f, encoding='utf-8'))['units'] if u['path'] == PATH]
    if us:
        lotti.append((os.path.basename(os.path.dirname(f)), len(us)))
        righe |= {u['line'] for u in us}
ck('INVARIANTE DI FILE: 5 lotti (22 + 23 + 20 + 15 + 7) coprono 87 righe distinte su 87',
   [n for _, n in lotti] == [22, 23, 20, 15, 7] and len(righe) == 87, (lotti, len(righe)))
ck('nessun buco: le 87 righe dei lotti sono esattamente quelle del database',
   righe == {l for l, in db.execute('select line from units where path=?', (PATH,))})
overlap = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    if os.path.basename(os.path.dirname(f)) == os.path.basename(HERE):
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH and 253 <= u['line'] <= 264:
            overlap.append((os.path.basename(os.path.dirname(f)), u['line']))
ck('nessun altro lotto rivendica le righe 253-264', not overlap, overlap)
ck('copertura: 87/87 (100%)', len(righe) == 87 == 87, '%d/87' % len(righe))
ck('tutte tradotte, nessuna copiata',
   not [u['idx'] for u in tu if u['italian'] == u['english']],
   [u['idx'] for u in tu if u['italian'] == u['english']])
ck('TAB: 7 in inglese e 7 in italiano, su TUTTE le unita, come primo carattere',
   sum(u['english'].count(TAB) for u in tu) == 7 == sum(u['italian'].count(TAB) for u in tu)
   and all(u['italian'].startswith(TAB) for u in tu))
ck('VIRGOLETTE: 16 in inglese e 16 in italiano, mappa per unita identica',
   sum(u['english'].count(QUOTE) for u in tu) == 16 == sum(u['italian'].count(QUOTE) for u in tu)
   and {u['idx']: u['english'].count(QUOTE) for u in tu}
   == {u['idx']: u['italian'].count(QUOTE) for u in tu})
by = {u['idx']: u for u in tu}
ck('le due unita di narrazione (4 e 7) restano senza virgolette',
   by[4]['italian'].count(QUOTE) == 0 == by[7]['italian'].count(QUOTE)
   and by[4]['english'].count(QUOTE) == 0 == by[7]['english'].count(QUOTE))
ck('APICI: 11 in inglese, 6 in italiano (elencati)',
   sum(u['english'].count(APOS) for u in tu) == 11 and sum(u['italian'].count(APOS) for u in tu) == 6
   and sorted(i for i, u in by.items() if APOS in u['italian']) == [1, 4, 5, 6],
   (sum(u['english'].count(APOS) for u in tu), sum(u['italian'].count(APOS) for u in tu),
    sorted(i for i, u in by.items() if APOS in u['italian'])))
ck('ZERO segnaposto in inglese e in italiano',
   not [t for u in tu for t in TAG.findall(u['english']) + TAG.findall(u['italian'])])
ck('nomi e lessico: Calvin, Gus, Sindacato, Marina, presa al collo, distretto dell\'infanzia',
   'Calvin' in by[6]['italian'] and 'Gus' in by[4]['italian']
   and 'Sindacato' in by[2]['italian'] and 'Marina' in by[3]['italian']
   and 'presa al collo' in by[5]['italian'] and "distretto dell'infanzia" in by[5]['italian']
   and 'Syndicate' not in ' '.join(u['italian'] for u in tu))
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in tu for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90 per ogni unita',
   all(0.55 < u['ratio'] < 1.90 for u in tu),
   [(u['idx'], u['ratio']) for u in tu if not 0.55 < u['ratio'] < 1.90])
ck('tutte le 7 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in tu))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print("FILE: 87/87 unita' · 5 lotti (22 + 23 + 20 + 15 + 7) · 87 righe distinte · ultima riga 264 · 0 dopo")
print('parole EN %d -> IT %d · ratio %.2f - %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(u['ratio'] for u in tu), max(u['ratio'] for u in tu)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L260 superato' if not fail else 'verify L260 fallito')
raise SystemExit(0 if not fail else 1)
