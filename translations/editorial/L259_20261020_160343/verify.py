r"""verify.py — L259 (`data/human/post-war reactions.txt`, righe 222-250). **Quarto lotto del file**.

Verifica da sola: riga grezza, campi del DB, il **segmento** (65 prima, 15 qui, **7** dopo la 250), il contesto unico, i
**15 tab**, le **45 virgolette** (con la **2** a **cinque**), i **quattro segnaposti**, la differenza fra le **unita' 7 e 8**,
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


ck('riga grezza identica al sorgente (15/15)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = [u['idx'] for u in su
       if db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
       != (u['english'], u['kind'], u['path'], u['context'])]
ck('english/kind/path/context identici al DB', not bad, bad)
ck('15 unita, righe 222-250, tutte MISSION_TEXT in un solo contesto',
   len(tu) == 15 and [u['line'] for u in tu] == sorted({u['line'] for u in tu})
   and {u['kind'] for u in tu} == {'MISSION_TEXT'} and {u['context'] for u in tu} == {CTX},
   (len(tu), {u['kind'] for u in tu}, {u['context'] for u in tu}))
ck("65 unita' prima: la 222 prosegue il contesto di L258",
   db.execute('select count(*) from units where path=? and line<222', (PATH,)).fetchone()[0] == 65
   and db.execute('select context from units where path=? and line<222 order by line desc limit 1', (PATH,)).fetchone()
   == (CTX,))
ck("7 unita' dopo la 250",
   db.execute('select count(*) from units where path=? and line>250', (PATH,)).fetchone()[0] == 7)
ck('confine: la 253 resta nel contesto del lotto (nessun cambio di missione)',
   db.execute('select context from units where path=? and line>250 order by line limit 1', (PATH,)).fetchone()
   == (CTX,))
ck('il file ha 87 unita, righe 40-264',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (87, 40, 264))
per_lotto, righe = [], set()
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    us = [u for u in json.load(open(f, encoding='utf-8'))['units'] if u['path'] == PATH]
    if us:
        per_lotto.append((os.path.basename(os.path.dirname(f)), len(us)))
        righe |= {u['line'] for u in us}
seg = {l for l in righe if 222 <= l <= 250}
ck('SEGMENTO: le 15 righe del lotto sono esattamente quelle 222-250',
   seg == {u['line'] for u in tu} and len(seg) == 15, (sorted(seg - {u['line'] for u in tu}), len(seg)))
overlap = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    if os.path.basename(os.path.dirname(f)) == os.path.basename(HERE):
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH and 222 <= u['line'] <= 250:
            overlap.append((os.path.basename(os.path.dirname(f)), u['line']))
ck('nessun altro lotto rivendica le righe 222-250', not overlap, overlap)
ck('copertura del SEGMENTO: 15/15; nel file restano 7 unita fuori (stampato, non asserito)',
   len(seg) == 15 and 87 - len(seg) == 72, '%d/87 (file)' % len(righe))
ck('tutte tradotte, nessuna copiata',
   not [u['idx'] for u in tu if u['italian'] == u['english']],
   [u['idx'] for u in tu if u['italian'] == u['english']])
ck('TAB: 15 in inglese e 15 in italiano, su TUTTE le unita, come primo carattere',
   sum(u['english'].count(TAB) for u in tu) == 15 == sum(u['italian'].count(TAB) for u in tu)
   and all(u['italian'].startswith(TAB) for u in tu))
ck('VIRGOLETTE: 45 in inglese e 45 in italiano, mappa per unita identica',
   sum(u['english'].count(QUOTE) for u in tu) == 45 == sum(u['italian'].count(QUOTE) for u in tu)
   and {u['idx']: u['english'].count(QUOTE) for u in tu if QUOTE in u['english']}
   == {u['idx']: u['italian'].count(QUOTE) for u in tu if QUOTE in u['italian']})
by = {u['idx']: u for u in tu}
ck('la 2 ha CINQUE virgolette in entrambe le lingue (citazione aperta e non chiusa)',
   by[2]['english'].count(QUOTE) == 5 == by[2]['italian'].count(QUOTE))
ck('APICI: 19 in inglese, 17 in italiano (elencati)',
   sum(u['english'].count(APOS) for u in tu) == 19 and sum(u['italian'].count(APOS) for u in tu) == 17
   and sorted(i for i, u in by.items() if APOS in u['italian']) == [1, 2, 3, 7, 8, 9, 10, 12],
   (sum(u['english'].count(APOS) for u in tu), sum(u['italian'].count(APOS) for u in tu),
    sorted(i for i, u in by.items() if APOS in u['italian'])))
ck('SEGNAPOSTI: <first> 2, <last> 2, ordine identico per unita, solo nelle unita 4 e 7',
   collections.Counter(t for u in tu for t in TAG.findall(u['english']))
   == collections.Counter(t for u in tu for t in TAG.findall(u['italian']))
   == collections.Counter({'<first>': 2, '<last>': 2})
   and [u['idx'] for u in tu if TAG.search(u['english'])] == [4, 7]
   and not [u['idx'] for u in tu if TAG.findall(u['english']) != TAG.findall(u['italian'])])
ck('7 e 8 differiscono per una battuta e coincidono nel resto',
   'Sei il capitano' in by[7]['italian'] and 'Sei il capitano' not in by[8]['italian']
   and "l'attacco" in by[8]['italian'] and "l'attacco" not in by[7]['italian']
   and by[7]['italian'][:60] == by[8]['italian'][:60]
   and by[7]['italian'].endswith('Ti tende la mano e tu la stringi.')
   and by[8]['italian'].endswith('Ti tende la mano e tu la stringi.'))
ck('lessico: Servizio di Sicurezza Ausiliario, Dispositivo per l\'Infanzia, tablet, navi da guerra',
   'Servizio di Sicurezza Ausiliario' in by[1]['italian']
   and "Dispositivo per l'Infanzia del Sindacato" in by[8]['italian']
   and 'tablet' in by[7]['italian'] and 'navi da guerra' in by[9]['italian'])
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in tu for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90 per ogni unita',
   all(0.55 < u['ratio'] < 1.90 for u in tu),
   [(u['idx'], u['ratio']) for u in tu if not 0.55 < u['ratio'] < 1.90])
ck('nomi propri invariati: Pug, Maker; Syndicate reso «Sindacato»',
   'Pug' in by[3]['italian'] and 'Maker' in by[3]['italian']
   and 'Sindacato' in by[1]['italian'] and 'Syndicate' not in ' '.join(u['italian'] for u in tu))
ck('tutte le 15 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in tu))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('SEGMENTO: 65 prima · 15 qui · 7 dopo · contesto unico · nessun cambio di missione')
print('parole EN %d -> IT %d · ratio %.2f - %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(u['ratio'] for u in tu), max(u['ratio'] for u in tu)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L259 superato' if not fail else 'verify L259 fallito')
raise SystemExit(0 if not fail else 1)
