r"""verify.py — L258 (`data/human/post-war reactions.txt`, righe 152-215). **Terzo lotto del file**.

Verifica da sola: riga grezza, campi del DB, il **segmento** (45 prima, 20 qui, **22** dopo la 215), i **due contesti**
(11 poi 9, cambio alla riga 196/196 = unita' 12), i **19 tab**, le **45 virgolette** (con la **5** a **tre**), gli **apici**
e che **nessun altro lotto** rivendichi queste righe.

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
CTX_A = 'mission:War Reactions: Navy and Free Worlds Captains'
CTX_B = 'mission:War Reactions: Syndicate Orphan'
src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
su = sorted(src['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
raw_lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
fail = []


def ck(n, c, d=''):
    print('%-96s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente (20/20)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = [u['idx'] for u in su
       if db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
       != (u['english'], u['kind'], u['path'], u['context'])]
ck('english/kind/path/context identici al DB', not bad, bad)
ck('20 unita, righe 152-215, tutte MISSION_TEXT',
   len(tu) == 20 and [u['line'] for u in tu] == sorted({u['line'] for u in tu})
   and {u['kind'] for u in tu} == {'MISSION_TEXT'}, (len(tu), {u['kind'] for u in tu}))
ck('DUE contesti: 11 della prima missione, 9 di Syndicate Orphan, cambio alla unita 12',
   collections.Counter(u['context'] for u in tu) == {CTX_A: 11, CTX_B: 9}
   and [u['context'] for u in tu if u['idx'] in (11, 12)] == [CTX_A, CTX_B],
   dict(collections.Counter(u['context'] for u in tu)))
ck("45 unita' prima: la 152 prosegue il contesto aperto alla 110",
   db.execute('select count(*) from units where path=? and line<152', (PATH,)).fetchone()[0] == 45
   and db.execute('select context from units where path=? and line<152 order by line desc limit 1', (PATH,)).fetchone()
   == (CTX_A,))
ck("22 unita' dopo la 215",
   db.execute('select count(*) from units where path=? and line>215', (PATH,)).fetchone()[0] == 22)
ck('confine: la 222 resta nel contesto aperto dalla 196',
   db.execute('select context from units where path=? and line>215 order by line limit 1', (PATH,)).fetchone()
   == (CTX_B,))
ck('il file ha 87 unita, righe 40-264',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (87, 40, 264))
per_lotto, righe = [], set()
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    us = [u for u in json.load(open(f, encoding='utf-8'))['units'] if u['path'] == PATH]
    if us:
        per_lotto.append((os.path.basename(os.path.dirname(f)), len(us)))
        righe |= {u['line'] for u in us}
seg = {l for l in righe if 152 <= l <= 215}
ck('SEGMENTO: le 20 righe del lotto sono esattamente quelle 152-215',
   seg == {u['line'] for u in tu} and len(seg) == 20, (sorted(seg - {u['line'] for u in tu}), len(seg)))
overlap = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    if os.path.basename(os.path.dirname(f)) == os.path.basename(HERE):
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH and 152 <= u['line'] <= 215:
            overlap.append((os.path.basename(os.path.dirname(f)), u['line']))
ck('nessun altro lotto rivendica le righe 152-215', not overlap, overlap)
ck('copertura del SEGMENTO: 20/20 righe; 67 restano fuori nel file (stampato, non asserito)',
   len(seg) == 20 and 87 - len(seg) == 67, '%d/87 (file)' % len(righe))
ck('tutte tradotte, nessuna copiata',
   not [u['idx'] for u in tu if u['italian'] == u['english']],
   [u['idx'] for u in tu if u['italian'] == u['english']])
ck('TAB: 19 in inglese e 19 in italiano, stesse unita, la 12 senza',
   sum(u['english'].count(TAB) for u in tu) == 19 == sum(u['italian'].count(TAB) for u in tu)
   and [u['idx'] for u in tu if TAB in u['english']] == [u['idx'] for u in tu if TAB in u['italian']]
   and not any(TAB in u['italian'] for u in tu if u['idx'] == 12)
   and all(u['italian'].startswith(TAB) for u in tu if TAB in u['italian']))
ck('VIRGOLETTE: 45 in inglese e 45 in italiano, mappa per unita identica',
   sum(u['english'].count(QUOTE) for u in tu) == 45 == sum(u['italian'].count(QUOTE) for u in tu)
   and {u['idx']: u['english'].count(QUOTE) for u in tu if QUOTE in u['english']}
   == {u['idx']: u['italian'].count(QUOTE) for u in tu if QUOTE in u['italian']})
by = {u['idx']: u for u in tu}
ck('la 5 ha TRE virgolette anche in italiano (citazione aperta e non chiusa)',
   by[5]['english'].count(QUOTE) == 3 == by[5]['italian'].count(QUOTE))
ck('APICI: 18 in inglese, 12 in italiano (elencati)',
   sum(u['english'].count(APOS) for u in tu) == 18 and sum(u['italian'].count(APOS) for u in tu) == 12
   and sorted(i for i, u in by.items() if APOS in u['italian']) == [1, 3, 10, 12, 15, 16, 18],
   (sum(u['english'].count(APOS) for u in tu), sum(u['italian'].count(APOS) for u in tu),
    sorted(i for i, u in by.items() if APOS in u['italian'])))
ck('ZERO segnaposto in inglese e in italiano',
   not [t for u in tu for t in TAG.findall(u['english']) + TAG.findall(u['italian'])])
ck('navi e istituzioni: corazzata, ausiliaria, incrociatore, Senato, Parlamento',
   'corazzata' in by[1]['italian'] and 'ausiliaria' in by[1]['italian']
   and 'incrociatore' in by[7]['italian']
   and 'Senato dei Free Worlds' in by[5]['italian'] and 'Parlamento della Repubblica' in by[5]['italian'])
ck('lessico del soccorso: officina, fondina, capsula — nessun «Dreadnought» o «Auxiliary»',
   'officina' in by[16]['italian'] and 'fondina' in by[15]['italian']
   and 'Dreadnought' not in ' '.join(u['italian'] for u in tu)
   and 'Auxiliary' not in ' '.join(u['italian'] for u in tu))
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in tu for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90 per ogni unita',
   all(0.55 < u['ratio'] < 1.90 for u in tu),
   [(u['idx'], u['ratio']) for u in tu if not 0.55 < u['ratio'] < 1.90])
ck('nomi propri invariati: Rain, Fiona, Longjump, Gus',
   all(w in ' '.join(u['italian'] for u in tu) for w in ('Rain', 'Fiona', 'Longjump', 'Gus')))
ck('tutte le 20 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in tu))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('SEGMENTO: 45 prima · 20 qui · 22 dopo · contesti 11 + 9 · cambio missione alla riga 196')
print('parole EN %d -> IT %d · ratio %.2f - %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(u['ratio'] for u in tu), max(u['ratio'] for u in tu)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L258 superato' if not fail else 'verify L258 fallito')
raise SystemExit(0 if not fail else 1)
