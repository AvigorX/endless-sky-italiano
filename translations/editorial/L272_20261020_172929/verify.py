r"""verify.py — L272 (`data/dialog phrases.txt`, righe 102-172). **LOTTO TERMINALE: chiude il file.**

Verifica da sola: riga grezza, campi del DB, il **segmento** (29 prima, 25 qui, **0 dopo** la 172) e l'**invariante di FILE**
(54 unità, righe distinte, ultima riga 172, somma dei due lotti), i **diciotto contesti** con le righe, i **30 segnaposto** in
**sei famiglie**, e che **nessun altro lotto** rivendichi queste righe.

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
PATH = 'data/dialog phrases.txt'
CTX = ['generic hunted bounty eliminated dialog', 'generic bounty hunting payment dialog',
       'generic bounty hunting on visit', 'generic bounty hunting boarding on visit',
       'generic hunted bounty fleet eliminated and payment dialog', 'generic hunted bounty fleet eliminated dialog',
       'generic fleet bounty hunting payment dialog', 'generic fleet bounty hunting on visit',
       'generic pirate fleet battle on visit', 'generic completed pirate cargo mission',
       'generic completed highly illegal pirate cargo mission', 'generic aborted pirate passenger mission',
       'generic aborted pirate cargo mission', 'generic completed pirate slave mission',
       'generic aborted pirate slave mission', 'free worlds failed', 'free worlds declined',
       'tribute pacifist undefined']
TOK = {'<npc>': 8, '<destination>': 4, '<planet>': 8, '<payment>': 6, '<commodity>': 3, '<bunks>': 1}
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


ck('riga grezza identica al sorgente (25/25)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = [u['idx'] for u in su
       if db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
       != (u['english'], u['kind'], u['path'], u['context'])]
ck('english/kind/path/context identici al DB', not bad, bad)
ck('25 unita, righe 102-172, tutte TEXT',
   len(tu) == 25 and [u['line'] for u in tu] == sorted({u['line'] for u in tu})
   and {u['kind'] for u in tu} == {'TEXT'}, (len(tu), {u['kind'] for u in tu}))
ck('i diciotto contesti compaiono in quest ordine, senza altri',
   [c.replace('phrase:', '', 1) for c in dict.fromkeys(u['context'] for u in tu)] == CTX,
   [c for c in dict.fromkeys(u['context'] for u in tu)])
ck("29 unita' prima (L271)",
   db.execute('select count(*) from units where path=? and line<102', (PATH,)).fetchone()[0] == 29)
ck("ZERO unita' dopo la 172: il lotto CHIUDE il file",
   db.execute('select count(*) from units where path=? and line>172', (PATH,)).fetchone()[0] == 0)
ck('INVARIANTE DI FILE: il database ha 54 unita, righe 16-172, ultima alla 172',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (54, 16, 172))
per_lotto, righe = [], set()
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    us = [u for u in json.load(open(f, encoding='utf-8'))['units'] if u['path'] == PATH]
    if us:
        per_lotto.append((os.path.basename(os.path.dirname(f)), len(us)))
        righe |= {u['line'] for u in us}
seg = {l for l in righe if 102 <= l <= 172}
ck('SEGMENTO: le 25 righe del lotto sono esattamente quelle 102-172',
   seg == {u['line'] for u in tu} and len(seg) == 25, (sorted(seg - {u['line'] for u in tu}), len(seg)))
ck('INVARIANTE DI FILE: due lotti, somma 54, righe distinte 54, nessuna riga fuori',
   sum(n for _, n in per_lotto) == 54 and len(righe) == 54 and min(righe) == 16 and max(righe) == 172,
   (sum(n for _, n in per_lotto), len(righe)))
ck('COPERTURA: 54/54 righe del file (100%)', len(righe) == 54, '%d/54' % len(righe))
overlap = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    if os.path.basename(os.path.dirname(f)) == os.path.basename(HERE):
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH and 102 <= u['line'] <= 172:
            overlap.append((os.path.basename(os.path.dirname(f)), u['line']))
ck('nessun altro lotto rivendica le righe 102-172', not overlap, overlap)
ck('tutte tradotte, nessuna copiata',
   not [u['idx'] for u in tu if u['italian'] == u['english']],
   [u['idx'] for u in tu if u['italian'] == u['english']])
ck('segnaposto per famiglia: 30 token, sei famiglie, identici in inglese e italiano',
   {t: sum(collections.Counter(TAG.findall(u['english']))[t] for u in tu) for t in TOK} == TOK
   == {t: sum(collections.Counter(TAG.findall(u['italian']))[t] for u in tu) for t in TOK})
ck('zero tab e zero virgolette',
   sum(u['english'].count(TAB) + u['italian'].count(TAB) for u in tu) == 0
   and sum(u['english'].count(QUOTE) + u['italian'].count(QUOTE) for u in tu) == 0)
ck('apici: 7 in inglese, 4 in italiano',
   sum(u['english'].count(APOS) for u in tu) == 7 and sum(u['italian'].count(APOS) for u in tu) == 4,
   (sum(u['english'].count(APOS) for u in tu), sum(u['italian'].count(APOS) for u in tu)))
ck('`<npc>` al femminile e `<bunks>` come numero di cuccette',
   'è stata eliminata' in by[1]['italian'] and 'sono state eliminate' in by[5]['italian']
   and '<bunks> schiavi' in by[14]['italian'])
ck('il tributo pacifista: otto frasi distinte, una sola nomina il tributo',
   len({by[i]['italian'] for i in range(18, 26)}) == 8
   and sum(1 for i in range(18, 26) if 'tributo' in by[i]['italian']) == 1)
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in tu for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90 per ogni unita',
   all(0.55 < u['ratio'] < 1.90 for u in tu),
   [(u['idx'], u['ratio']) for u in tu if not 0.55 < u['ratio'] < 1.90])
ck('tutte le 25 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in tu))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('SEGMENTO: 29 prima · 25 qui · 0 dopo (FINE FILE) · 18 contesti · 30 segnaposto')
print('parole EN %d -> IT %d · ratio %.2f - %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(u['ratio'] for u in tu), max(u['ratio'] for u in tu)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L272 superato' if not fail else 'verify L272 fallito')
raise SystemExit(0 if not fail else 1)
