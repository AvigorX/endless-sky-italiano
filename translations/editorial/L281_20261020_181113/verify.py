r"""verify.py — L281 (`data/quarg/quarg news.txt`, righe 23-490). **LOTTO TERMINALE: chiude il file.**

Verifica da sola: riga grezza, campi del DB, il **segmento** (0 prima — apre il file — 50 qui, **0 dopo** la 490) e
l'**invariante di FILE** (50 unità, righe distinte, ultima riga 490, copertura 50/50), i **dieci contesti** con le righe, i
**28 delimitatori** copiati, le **44 virgolette** per unità.

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
PATH = 'data/quarg/quarg news.txt'
CTX = ['anonymous quarg', 'linguist on quarg planets in human and hai space',
       'tourist on quarg planets in human and hai space', 'engineer on quarg planets in human space',
       'merchant on quarg planets in human and hai space', 'merchant on quarg planets in human space',
       'reporter on quarg planets in human space', 'student on quarg planets', 'quarg anywhere',
       'ringworld quarg phrases']
src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
su = sorted(src['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
raw_lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
by = {u['idx']: u for u in tu}
fail = []


def ck(n, c, d=''):
    print('%-96s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente (50/50)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']][:5])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = [u['idx'] for u in su
       if db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
       != (u['english'], u['kind'], u['path'], u['context'])]
ck('english/kind/path/context identici al DB', not bad, bad[:5])
ck('50 unita, righe 23-490, 40 NEWS + 10 TEXT',
   len(tu) == 50 and [u['line'] for u in tu] == sorted({u['line'] for u in tu})
   and collections.Counter(u['kind'] for u in tu) == {'NEWS': 40, 'TEXT': 10},
   (len(tu), collections.Counter(u['kind'] for u in tu)))
ck('i dieci contesti compaiono in quest ordine',
   [c.replace('news:', '', 1).replace('phrase:', '', 1) for c in dict.fromkeys(u['context'] for u in tu)] == CTX,
   [c for c in dict.fromkeys(u['context'] for u in tu)])
ck("ZERO unita' prima della 23: il lotto APRE il file",
   db.execute('select count(*) from units where path=? and line<23', (PATH,)).fetchone()[0] == 0)
ck("ZERO unita' dopo la 490: il lotto CHIUDE il file",
   db.execute('select count(*) from units where path=? and line>490', (PATH,)).fetchone()[0] == 0)
ck('INVARIANTE DI FILE: il database ha 50 unita, righe 23-490, ultima alla 490',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (50, 23, 490))
per_lotto, righe = [], set()
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    us = [u for u in json.load(open(f, encoding='utf-8'))['units'] if u['path'] == PATH]
    if us:
        per_lotto.append((os.path.basename(os.path.dirname(f)), len(us)))
        righe |= {u['line'] for u in us}
ck('INVARIANTE DI FILE: un solo lotto, somma 50, righe distinte 50',
   sum(n for _, n in per_lotto) == 50 and len(righe) == 50 and min(righe) == 23 and max(righe) == 490,
   (sum(n for _, n in per_lotto), len(righe)))
ck('COPERTURA: 50/50 righe del file (100%)', len(righe) == 50, '%d/50' % len(righe))
overlap = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    if os.path.basename(os.path.dirname(f)) == os.path.basename(HERE):
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH and 23 <= u['line'] <= 490:
            overlap.append((os.path.basename(os.path.dirname(f)), u['line']))
ck('nessun altro lotto rivendica le righe 23-490', not overlap, overlap)
ck('28 delimitatori copiati e 22 unita di prosa tradotte',
   len([u for u in tu if u['english'] == '"']) == 28
   and all(u['italian'] == '"' for u in tu if u['english'] == '"')
   and not [u for u in tu if u['english'] != '"'] == [] and
   all(u['italian'] != u['english'] for u in tu if u['english'] != '"'),
   (len([u for u in tu if u['english'] == '"']),
    len([u for u in tu if u['english'] != '"' and u['italian'] == u['english']])))
ck('virgolette: 44 in tutto e lo stesso numero per ogni unita',
   sum(u['english'].count(QUOTE) for u in tu) == 44 == sum(u['italian'].count(QUOTE) for u in tu)
   and all(u['english'].count(QUOTE) == u['italian'].count(QUOTE) for u in tu))
ck('zero tab e zero segnaposto',
   sum(u['english'].count(TAB) + u['italian'].count(TAB) for u in tu) == 0
   and not [t for u in tu for t in TAG.findall(u['english']) + TAG.findall(u['italian'])])
ck('apici: 14 in inglese, 20 in italiano',
   sum(u['english'].count(APOS) for u in tu) == 14 and sum(u['italian'].count(APOS) for u in tu) == 20,
   (sum(u['english'].count(APOS) for u in tu), sum(u['italian'].count(APOS) for u in tu)))
ck('il registro Quarg e il rifiuto della tecnologia',
   'Hai qualche domanda' in by[30]['italian']
   and 'non ti forniremo la nostra tecnologia' in by[32]['italian']
   and 'mondo ad anello' in by[41]['italian'])
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in tu for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90 sulle unita di prosa',
   all(0.55 < u['ratio'] < 1.90 for u in tu if u['english'] != '"'),
   [(u['idx'], u['ratio']) for u in tu if u['english'] != '"' and not 0.55 < u['ratio'] < 1.90])
ck('tutte le 50 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in tu))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('SEGMENTO: 0 prima (apre il file) · 50 qui · 0 dopo (FINE FILE) · 10 contesti')
print('parole EN %d -> IT %d · ratio prosa %.2f - %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(u['ratio'] for u in tu if u['english'] != '"'),
    max(u['ratio'] for u in tu if u['english'] != '"')))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L281 superato' if not fail else 'verify L281 fallito')
raise SystemExit(0 if not fail else 1)
