r"""verify.py — L263 (`data/remnant/remnant jobs.txt`, righe 491-682). **Terzo lotto del file**.

Verifica da sola: riga grezza, campi del DB, il **segmento** (54 prima, 24 qui, **9** dopo la 682), i **6 contesti** in
sequenza, i **28 segnaposto** per famiglia e per ordine, il **femminile di `<npc>`**, il **tab** e le **virgolette**, e che
**nessun altro lotto** rivendichi queste righe.

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
CTXS = ['mission:Remnant: Rescue 2', 'mission:Remnant: Rescue 2B', 'mission:Remnant: Rescue 3',
        'mission:Remnant: Rescue 3B', 'mission:Remnant: Rescue 4', 'mission:Remnant: Rescue 5']
src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
su = sorted(src['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
raw_lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
fail = []


def ck(n, c, d=''):
    print('%-96s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente (24/24)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = [u['idx'] for u in su
       if db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
       != (u['english'], u['kind'], u['path'], u['context'])]
ck('english/kind/path/context identici al DB', not bad, bad)
ck('24 unita, righe 491-682, tipi 13/6/5',
   len(tu) == 24 and [u['line'] for u in tu] == sorted({u['line'] for u in tu})
   and collections.Counter(u['kind'] for u in tu) == {'MISSION_TEXT': 13, 'DESCRIPTION': 6, 'VALUE': 5},
   (len(tu), collections.Counter(u['kind'] for u in tu)))
ck('i sei contesti compaiono in quest ordine, senza altri',
   [c for c in dict.fromkeys(u['context'] for u in tu)] == CTXS,
   [c for c in dict.fromkeys(u['context'] for u in tu)])
ck("54 unita' prima, e la precedente apre `Rescue 2`",
   db.execute('select count(*) from units where path=? and line<491', (PATH,)).fetchone()[0] == 54
   and db.execute('select context from units where path=? and line<491 order by line desc limit 1', (PATH,)).fetchone()
   == (CTXS[0],))
ck("9 unita' dopo la 682", db.execute('select count(*) from units where path=? and line>682', (PATH,)).fetchone()[0] == 9)
ck('confine: la 703 resta in `Rescue 5`, il contesto dell ultima unita del lotto',
   db.execute('select line,context from units where path=? and line>682 order by line limit 1', (PATH,)).fetchone()
   == (703, CTXS[5]))
ck('il file ha 87 unita, righe 19-741',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (87, 19, 741))
per_lotto, righe = [], set()
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    us = [u for u in json.load(open(f, encoding='utf-8'))['units'] if u['path'] == PATH]
    if us:
        per_lotto.append((os.path.basename(os.path.dirname(f)), len(us)))
        righe |= {u['line'] for u in us}
seg = {l for l in righe if 491 <= l <= 682}
ck('SEGMENTO: le 24 righe del lotto sono esattamente quelle 491-682',
   seg == {u['line'] for u in tu} and len(seg) == 24, (sorted(seg - {u['line'] for u in tu}), len(seg)))
overlap = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    if os.path.basename(os.path.dirname(f)) == os.path.basename(HERE):
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH and 491 <= u['line'] <= 682:
            overlap.append((os.path.basename(os.path.dirname(f)), u['line']))
ck('nessun altro lotto rivendica le righe 491-682', not overlap, overlap)
ck('copertura del SEGMENTO: 24/24 righe; il totale del file e stampato, non asserito',
   len(seg) == 24 and 87 - len(seg) == 63, '%d/87 (file)' % len(righe))
ck('i 5 VALUE sono copiati identici; le altre 19 sono tradotte',
   all(u['italian'] == u['english'] for u in tu if u['kind'] == 'VALUE')
   and all(u['italian'] != u['english'] for u in tu if u['kind'] != 'VALUE'))
ck('TAB: uno solo, unita 21, primo carattere; VIRGOLETTE: due, unita 20',
   sum(u['italian'].count(TAB) for u in tu) == 1
   and [u['idx'] for u in tu if TAB in u['italian']] == [21]
   and sum(u['italian'].count(QUOTE) for u in tu) == 2
   and [u['idx'] for u in tu if QUOTE in u['italian']] == [20])
ck('APICI: zero in inglese, 13 in italiano (elencati per unita)',
   sum(u['english'].count(APOS) for u in tu) == 0 and sum(u['italian'].count(APOS) for u in tu) == 13,
   (sum(u['english'].count(APOS) for u in tu), sum(u['italian'].count(APOS) for u in tu)))
ck('SEGNAPOSTI: 28 in 3 famiglie, con ordine identico per unita',
   collections.Counter(t for u in tu for t in TAG.findall(u['english'])) ==
   collections.Counter(t for u in tu for t in TAG.findall(u['italian'])) ==
   collections.Counter({'<npc>': 17, '<destination>': 6, '<payment>': 5})
   and not [u['idx'] for u in tu if TAG.findall(u['english']) != TAG.findall(u['italian'])])
ck('`<npc>` al femminile in tutte le 17 occorrenze, mai con articolo maschile',
   sum(u['italian'].count('<npc>') for u in tu) == 17
   and not re.search(r'\b(?:il|lo|un|uno|del|dello)\s+<npc>', ' '.join(u['italian'] for u in tu))
   and 'la <npc>' in ' '.join(u['italian'] for u in tu))
ck('nessun participio maschile riferito alla nave',
   not re.search(r'\b(?:scomparso|distrutto|disperso|perduto)\b', ' '.join(u['italian'] for u in tu)))
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in tu for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90 per ogni unita',
   all(0.55 < u['ratio'] < 1.90 for u in tu),
   [(u['idx'], u['ratio']) for u in tu if not 0.55 < u['ratio'] < 1.90])
ck('tutte le 24 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in tu))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('SEGMENTO: 54 prima · 24 qui · 9 dopo · 6 contesti · 28 segnaposto in 3 famiglie')
print('parole EN %d -> IT %d · ratio %.2f - %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(u['ratio'] for u in tu), max(u['ratio'] for u in tu)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L263 superato' if not fail else 'verify L263 fallito')
raise SystemExit(0 if not fail else 1)
