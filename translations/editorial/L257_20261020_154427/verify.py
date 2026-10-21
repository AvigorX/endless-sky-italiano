r"""verify.py — L257 (`data/human/post-war reactions.txt`, righe 76-151). **Secondo lotto del file**.

Verifica da sola: riga grezza, campi del DB, il **segmento** (22 prima, 23 qui, **42** dopo la 151), i **due contesti**
(9 poi 14, con il cambio alla riga 110), i **tab** e le **virgolette** per unita', i **cinque segnaposti** nello stesso
ordine, e che **nessun altro lotto** rivendichi queste righe.

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
CTX_A = 'mission:War Reactions: Asteroid Miners'
CTX_B = 'mission:War Reactions: Navy and Free Worlds Captains'
src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
su = sorted(src['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
raw_lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
fail = []


def ck(n, c, d=''):
    print('%-96s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente (23/23)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = [u['idx'] for u in su
       if db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
       != (u['english'], u['kind'], u['path'], u['context'])]
ck('english/kind/path/context identici al DB', not bad, bad)
ck('23 unita, righe 76-151, tutte MISSION_TEXT',
   len(tu) == 23 and [u['line'] for u in tu] == sorted({u['line'] for u in tu})
   and {u['kind'] for u in tu} == {'MISSION_TEXT'}, (len(tu), {u['kind'] for u in tu}))
ck('DUE contesti: le 9 unita fino alla riga 92 e le 14 dalla 110',
   collections.Counter(u['context'] for u in tu) == {CTX_A: 9, CTX_B: 14}
   and [u['context'] for u in tu if u['idx'] == 10] == [CTX_B],
   dict(collections.Counter(u['context'] for u in tu)))
ck("22 unita' prima: la 76 prosegue il contesto di L256",
   db.execute('select count(*) from units where path=? and line<76', (PATH,)).fetchone()[0] == 22
   and db.execute('select context from units where path=? and line<76 order by line desc limit 1', (PATH,)).fetchone()
   == (CTX_A,))
ck("42 unita' dopo la 151",
   db.execute('select count(*) from units where path=? and line>151', (PATH,)).fetchone()[0] == 42)
ck('confine: la 152 resta nel contesto aperto dalla 110',
   db.execute('select context from units where path=? and line>151 order by line limit 1', (PATH,)).fetchone()
   == (CTX_B,))
ck('il file ha 87 unita, righe 40-264',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (87, 40, 264))
per_lotto, righe = [], set()
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    us = [u for u in json.load(open(f, encoding='utf-8'))['units'] if u['path'] == PATH]
    if us:
        per_lotto.append((os.path.basename(os.path.dirname(f)), len(us)))
        righe |= {u['line'] for u in us}
seg = {l for l in righe if 76 <= l <= 151}
ck('SEGMENTO: le 23 righe del lotto sono esattamente quelle 76-151',
   seg == {u['line'] for u in tu} and len(seg) == 23, (sorted(seg - {u['line'] for u in tu}), len(seg)))
overlap = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    if os.path.basename(os.path.dirname(f)) == os.path.basename(HERE):
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH and 76 <= u['line'] <= 151:
            overlap.append((os.path.basename(os.path.dirname(f)), u['line']))
ck('nessun altro lotto rivendica le righe 76-151', not overlap, overlap)
ck('copertura del SEGMENTO: 23/23 righe; del file ne restano 42 fuori (stampato, non asserito)',
   len(seg) == 23 and 87 - len(seg) == 64, '%d/87 (file)' % len(righe))
ck('tutte tradotte, nessuna copiata',
   not [u['idx'] for u in tu if u['italian'] == u['english']],
   [u['idx'] for u in tu if u['italian'] == u['english']])
ck('TAB: 22 in inglese e 22 in italiano, stesse unita, la 10 senza',
   sum(u['english'].count(TAB) for u in tu) == 22 == sum(u['italian'].count(TAB) for u in tu)
   and [u['idx'] for u in tu if TAB in u['english']] == [u['idx'] for u in tu if TAB in u['italian']]
   and not any(TAB in u['italian'] for u in tu if u['idx'] == 10)
   and all(u['italian'].startswith(TAB) for u in tu if TAB in u['italian']))
ck('VIRGOLETTE: 45 in inglese e 45 in italiano, mappa per unita identica',
   sum(u['english'].count(QUOTE) for u in tu) == 45 == sum(u['italian'].count(QUOTE) for u in tu)
   and {u['idx']: u['english'].count(QUOTE) for u in tu if QUOTE in u['english']}
   == {u['idx']: u['italian'].count(QUOTE) for u in tu if QUOTE in u['italian']})
by = {u['idx']: u for u in tu}
ck('la 12 ha TRE virgolette anche in italiano (citazione aperta e non chiusa nel sorgente)',
   by[12]['english'].count(QUOTE) == 3 == by[12]['italian'].count(QUOTE))
ck('APICI: 17 in inglese, 5 in italiano (elencati)',
   sum(u['english'].count(APOS) for u in tu) == 17 and sum(u['italian'].count(APOS) for u in tu) == 5
   and sorted(i for i, u in by.items() if APOS in u['italian']) == [10, 12, 22, 23],
   (sum(u['english'].count(APOS) for u in tu), sum(u['italian'].count(APOS) for u in tu),
    sorted(i for i, u in by.items() if APOS in u['italian'])))
ck('SEGNAPOSTI: <first> 1, <last> 3, <ship> 1, con ordine identico per unita',
   collections.Counter(t for u in tu for t in TAG.findall(u['english']))
   == collections.Counter(t for u in tu for t in TAG.findall(u['italian']))
   == collections.Counter({'<first>': 1, '<last>': 3, '<ship>': 1})
   and not [u['idx'] for u in tu if TAG.findall(u['english']) != TAG.findall(u['italian'])],
   [u['idx'] for u in tu if TAG.findall(u['english']) != TAG.findall(u['italian'])])
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in tu for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90 per ogni unita',
   all(0.55 < u['ratio'] < 1.90 for u in tu),
   [(u['idx'], u['ratio']) for u in tu if not 0.55 < u['ratio'] < 1.90])
ck('lessico: Marina e Free Worlds nella 10, Pug nella 12, nessun «Navy»',
   'Marina' in by[10]['italian'] and 'Free Worlds' in by[10]['italian']
   and 'Pug' in by[12]['italian'] and 'Navy' not in by[10]['italian'])
ck('nomi propri invariati: Rain, Fiona, Camuy, Baobab, Spider Funk',
   all(w in ' '.join(u['italian'] for u in tu)
       for w in ('Rain', 'Fiona', 'R.N.S. Camuy', 'F.S. Baobab', 'Spider Funk')))
ck('tutte le 23 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in tu))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('SEGMENTO: 22 prima · 23 qui · 42 dopo · contesti 9 + 14 · cambio missione alla riga 110')
print('parole EN %d -> IT %d · ratio %.2f - %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(u['ratio'] for u in tu), max(u['ratio'] for u in tu)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L257 superato' if not fail else 'verify L257 fallito')
raise SystemExit(0 if not fail else 1)
