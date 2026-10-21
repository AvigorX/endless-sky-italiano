r"""verify.py — L288 (`data/gegno/gegno ships.txt`, righe 725-1192). **Terzo lotto del file**.

Verifica da sola: riga grezza, campi del DB, il **segmento** (16 prima, 9 qui, **12** dopo la 1192), i **sette contesti**, il
**`VALUE` copiato** e distinto dalle `DESCRIPTION` dello stesso contesto, la **coppia consecutiva** 1061-1062, le **asserzioni
vuote**, `Halite` che **prosegue oltre il confine**, e che **nessun altro lotto** rivendichi le righe 725-1192.

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
PATH = 'data/gegno/gegno ships.txt'
NAMES = ['Rhyolite', 'Eclogite', 'Diorite', 'Hornfel', 'Gneiss', 'Granulite', 'Halite', 'Gegno', 'Vi', 'Scin',
         'Ballistic Cannons']
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
ck('9 unita, righe distinte, 8 DESCRIPTION + 1 VALUE',
   len(tu) == 9 and len({u['line'] for u in tu}) == 9
   and collections.Counter(u['kind'] for u in tu) == {'DESCRIPTION': 8, 'VALUE': 1},
   collections.Counter(u['kind'] for u in tu))
ck('sette contesti con le righe dichiarate',
   [(u['context'], u['line']) for u in tu]
   == [('ship:Rhyolite', 725), ('ship:Eclogite', 776), ('ship:Diorite', 832), ('ship:Hornfel', 917),
       ('ship:Gneiss', 983), ('ship:Gneiss', 1061), ('ship:Gneiss', 1062), ('ship:Granulite', 1149),
       ('ship:Halite', 1192)])
ck("16 unita' prima della 725 e 12 dopo la 1192",
   db.execute('select count(*) from units where path=? and line<725', (PATH,)).fetchone()[0] == 16
   and db.execute('select count(*) from units where path=? and line>1192', (PATH,)).fetchone()[0] == 12)
ck('`Halite` continua oltre il confine: la prima unita dopo la 1192 e ancora `ship:Halite`',
   db.execute('select context from units where path=? and line>1192 order by line limit 1', (PATH,)).fetchone()
   == ('ship:Halite',))
ck('il file ha 37 unita, righe 53-1616',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (37, 53, 1616))
righe = set()
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH:
            righe.add(u['line'])
seg = {l for l in righe if 725 <= l <= 1192}
ck('SEGMENTO: le 9 righe del lotto sono esattamente quelle 725-1192',
   seg == {u['line'] for u in tu} and len(seg) == 9, (sorted(seg - {u['line'] for u in tu}), len(seg)))
overlap = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    if os.path.basename(os.path.dirname(f)) == os.path.basename(HERE):
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH and 725 <= u['line'] <= 1192:
            overlap.append((os.path.basename(os.path.dirname(f)), u['line']))
ck('nessun altro lotto rivendica le righe 725-1192', not overlap, overlap)
ck('copertura: 9 righe nel segmento, il totale del file e stampato e non supera 37',
   len(seg) == 9 and len(righe) <= 37, '%d/37 al momento' % len(righe))
ck('il VALUE e copiato; le 8 DESCRIPTION tradotte; il contesto `ship:Gneiss` ha tutti e tre i tipi',
   at[983]['kind'] == 'VALUE' and at[983]['italian'] == at[983]['english'] == 'Gneiss'
   and at[1061]['kind'] == at[1062]['kind'] == 'DESCRIPTION'
   and at[1061]['italian'] != at[1061]['english'] and at[1062]['italian'] != at[1062]['english']
   and {at[l]['context'] for l in (983, 1061, 1062)} == {'ship:Gneiss'})
ck('coppia consecutiva 1061-1062, la seconda continua con «Purtroppo»',
   at[1062]['line'] == at[1061]['line'] + 1
   and at[1062]['italian'].lstrip(TAB).startswith('Purtroppo'))
ck('tab: uno solo, riga 1062, primo carattere',
   sum(u['english'].count(TAB) for u in tu) == 1 == sum(u['italian'].count(TAB) for u in tu)
   and at[1062]['italian'].startswith(TAB))
ck('asserzioni vuote: 0 virgolette, 0 segnaposto, 0 alternative',
   sum(u['english'].count(QUOTE) for u in tu) == 0 == sum(u['italian'].count(QUOTE) for u in tu)
   and sum(len(TAG.findall(u['english'])) for u in tu) == 0 == sum(len(TAG.findall(u['italian'])) for u in tu)
   and sum(len(ALT.findall(u['english'])) for u in tu) == 0 == sum(len(ALT.findall(u['italian'])) for u in tu))
ck('apici: 9 in inglese, 9 in italiano',
   sum(u['english'].count(APOS) for u in tu) == 9 == sum(u['italian'].count(APOS) for u in tu),
   (sum(u['english'].count(APOS) for u in tu), sum(u['italian'].count(APOS) for u in tu)))
ck('nomi di modello e di fazione invariati', all(n in ''.join(u['italian'] for u in tu) for n in NAMES),
   [n for n in NAMES if n not in ''.join(u['italian'] for u in tu)])
ck('`Hornfel` non diventa `Hornfels` in italiano, e `Gneiss` resta invariabile',
   'Hornfels' not in ''.join(u['italian'] for u in tu) and 'Gneisss' not in ''.join(u['italian'] for u in tu))
ck('registro in terza persona: nessun «tu»/«tuo»',
   not [u['idx'] for u in tu if re.search(r'\b(tu|tuo|tua|tuoi|tue|ti|te)\b', u['italian'])])
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
print('SEGMENTO: 16 prima · 9 qui · 12 dopo la 1192 · 7 contesti')
print('parole EN %d -> IT %d · ratio %.2f - %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(u['ratio'] for u in tu), max(u['ratio'] for u in tu)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L288 superato' if not fail else 'verify L288 fallito')
raise SystemExit(0 if not fail else 1)
