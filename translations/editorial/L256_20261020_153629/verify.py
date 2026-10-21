r"""verify.py — L256 (`data/human/post-war reactions.txt`, righe 40-74). **Primo lotto del file.**

Verifica da sola: riga grezza, campi del DB, il **segmento** (0 prima della 40, 65 dopo la 74, confine alla riga 76 nello
stesso contesto), i segni tipografici del dialogo **per unita'** (21 tab, 34 virgolette, 19 apici inglesi / 9 italiani),
zero segnaposto, e che **nessun altro lotto** rivendichi queste righe.

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
CTX = 'mission:War Reactions: Asteroid Miners'
src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
su = sorted(src['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
raw_lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
fail = []


def ck(n, c, d=''):
    print('%-96s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente (22/22)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = [u['idx'] for u in su
       if db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
       != (u['english'], u['kind'], u['path'], u['context'])]
ck('english/kind/path/context identici al DB', not bad, bad)
ck('22 unita, righe 40-74, tutte MISSION_TEXT nello stesso contesto',
   len(tu) == 22 and [u['line'] for u in tu] == sorted({u['line'] for u in tu})
   and {u['kind'] for u in tu} == {'MISSION_TEXT'} and {u['context'] for u in tu} == {CTX},
   ({u['kind'] for u in tu}, {u['context'] for u in tu}, len(tu)))
ck("ZERO unita' prima della 40: il lotto APRE il file",
   db.execute('select count(*) from units where path=? and line<40', (PATH,)).fetchone()[0] == 0)
ck("65 unita' dopo la 74",
   db.execute('select count(*) from units where path=? and line>74', (PATH,)).fetchone()[0] == 65)
ck("confine: la riga 76 apre lo stesso contesto (nessun cambio di missione)",
   db.execute('select context from units where path=? and line>74 order by line limit 1', (PATH,)).fetchone()
   == (CTX,))
ck('il file ha 87 unita, righe 40-264',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (87, 40, 264))
per_lotto, righe = [], set()
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    us = [u for u in json.load(open(f, encoding='utf-8'))['units'] if u['path'] == PATH]
    if us:
        per_lotto.append((os.path.basename(os.path.dirname(f)), len(us)))
        righe |= {u['line'] for u in us}
seg = {l for l in righe if 40 <= l <= 74}
ck('SEGMENTO: le 22 righe del lotto sono esattamente quelle 40-74 (nessuna in piu, nessuna in meno)',
   seg == {u['line'] for u in tu} and len(seg) == 22, (sorted(seg - {u['line'] for u in tu}), len(seg)))
overlap = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    if os.path.basename(os.path.dirname(f)) == os.path.basename(HERE):
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH and 40 <= u['line'] <= 74:
            overlap.append((os.path.basename(os.path.dirname(f)), u['line']))
ck('nessun altro lotto rivendica le righe 40-74', not overlap, overlap)
ck('copertura del SEGMENTO: 22/22 righe; del file 65 restano fuori (stampato, non asserito)',
   len(seg) == 22 and 87 - len(seg) == 65, '%d/87' % len(seg))
ck('tutte tradotte, nessuna copiata',
   not [u['idx'] for u in tu if u['italian'] == u['english']],
   [u['idx'] for u in tu if u['italian'] == u['english']])
tok = [t for u in tu for t in TAG.findall(u['english']) + TAG.findall(u['italian'])]
ck('ZERO segnaposto in inglese e in italiano', not tok, tok)
ck('TAB: 21 in inglese e 21 in italiano, sulle stesse unita (2-22), come PRIMO carattere',
   sum(u['english'].count(TAB) for u in tu) == 21 == sum(u['italian'].count(TAB) for u in tu)
   and [u['idx'] for u in tu if TAB in u['english']] == [u['idx'] for u in tu if TAB in u['italian']]
   == list(range(2, 23))
   and all(u['italian'].startswith(TAB) for u in tu if u['idx'] in range(2, 23)))
ck('VIRGOLETTE: 34 in inglese e 34 in italiano, per unita identiche',
   sum(u['english'].count(QUOTE) for u in tu) == 34 == sum(u['italian'].count(QUOTE) for u in tu)
   and {u['idx']: u['english'].count(QUOTE) for u in tu if QUOTE in u['english']}
   == {u['idx']: u['italian'].count(QUOTE) for u in tu if QUOTE in u['italian']})
ck('APICI: 19 in inglese, 9 in italiano (differenza elencata per unita)',
   sum(u['english'].count(APOS) for u in tu) == 19 and sum(u['italian'].count(APOS) for u in tu) == 9,
   (sum(u['english'].count(APOS) for u in tu), sum(u['italian'].count(APOS) for u in tu)))
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in tu for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90 per ogni unita',
   all(0.55 < u['ratio'] < 1.90 for u in tu),
   [(u['idx'], u['ratio']) for u in tu if not 0.55 < u['ratio'] < 1.90])
by = {u['idx']: u['italian'] for u in tu}
ck('il refuso voluto `Danforts` resta nella 21 e sparisce nella correzione della 22',
   'Danforts' in by[21] and 'Danforts' not in by[22] and 'Danforth' in by[22])
ck('lessico: Marina / Sindacato, nomi propri invariati',
   'Marina' in by[10] and 'Sindacato' in by[6] and 'Pug' in by[8] and 'Maduena Kabiru' in by[11])
ck('tutte le 22 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in tu))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print("SEGMENTO: 0 prima · 22 qui · 65 dopo · confine riga 76 (%s)" % CTX)
print('parole EN %d -> IT %d · ratio %.2f - %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(u['ratio'] for u in tu), max(u['ratio'] for u in tu)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L256 superato' if not fail else 'verify L256 fallito')
raise SystemExit(0 if not fail else 1)
