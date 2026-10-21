r"""verify.py — L261 (`data/remnant/remnant jobs.txt`, righe 19-209). **Primo lotto del file.**

Verifica da sola: riga grezza, campi del DB, il **segmento** (0 prima della 19, **62** dopo la 209 — il lotto apre il file),
i **7 contesti** in sequenza, i **29 segnaposto** per famiglia e per ordine, i **7 `VALUE` copiati**, lo zero di tab e
virgolette, e che **nessun altro lotto** rivendichi queste righe.

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
CTXS = ['mission:Remnant: Bounty', 'mission:Remnant: Bounty 2', 'mission:Remnant: Broken Jump Drive job',
        'mission:Remnant: Expanded Horizons Astral job', 'mission:Remnant: Expanded Horizons Astral job late',
        'mission:Remnant: Bounty 3', 'mission:Remnant: Bounty 4']
src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
su = sorted(src['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
raw_lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
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
ck('25 unita, righe 19-209, tipi 11/7/7',
   len(tu) == 25 and [u['line'] for u in tu] == sorted({u['line'] for u in tu})
   and collections.Counter(u['kind'] for u in tu) == {'DIALOG': 11, 'DESCRIPTION': 7, 'VALUE': 7},
   (len(tu), collections.Counter(u['kind'] for u in tu)))
ck('i 7 contesti compaiono nell ordine atteso e senza altri',
   [c for c in dict.fromkeys(u['context'] for u in tu)] == CTXS,
   [c for c in dict.fromkeys(u['context'] for u in tu)])
ck("ZERO unita' prima della 19: il lotto APRE il file",
   db.execute('select count(*) from units where path=? and line<19', (PATH,)).fetchone()[0] == 0)
ck("62 unita' dopo la 209", db.execute('select count(*) from units where path=? and line>209', (PATH,)).fetchone()[0] == 62)
ck('confine: la 226 apre `Remnant: Bounty 4` (il contesto dell ultima unita del lotto)',
   db.execute('select line,context from units where path=? and line>209 order by line limit 1', (PATH,)).fetchone()
   == (226, CTXS[6]))
ck('il file ha 87 unita, righe 19-741',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (87, 19, 741))
per_lotto, righe = [], set()
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    us = [u for u in json.load(open(f, encoding='utf-8'))['units'] if u['path'] == PATH]
    if us:
        per_lotto.append((os.path.basename(os.path.dirname(f)), len(us)))
        righe |= {u['line'] for u in us}
seg = {l for l in righe if 19 <= l <= 209}
ck('SEGMENTO: le 25 righe del lotto sono esattamente quelle 19-209',
   seg == {u['line'] for u in tu} and len(seg) == 25, (sorted(seg - {u['line'] for u in tu}), len(seg)))
overlap = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    if os.path.basename(os.path.dirname(f)) == os.path.basename(HERE):
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH and 19 <= u['line'] <= 209:
            overlap.append((os.path.basename(os.path.dirname(f)), u['line']))
ck('nessun altro lotto rivendica le righe 19-209', not overlap, overlap)
ck('copertura del SEGMENTO: 25/25 righe del lotto; il totale del file e stampato, non asserito',
   len(seg) == 25 and 87 - len(seg) == 62, '%d/87 (file)' % len(righe))
ck('i VALUE sono copiati identici; tutto il resto e tradotto',
   all(u['italian'] == u['english'] for u in tu if u['kind'] == 'VALUE')
   and all(u['italian'] != u['english'] for u in tu if u['kind'] != 'VALUE'))
ck('ZERO tab e ZERO virgolette in entrambe le lingue',
   sum(u['english'].count(TAB) + u['italian'].count(TAB) for u in tu) == 0
   and sum(u['english'].count(QUOTE) + u['italian'].count(QUOTE) for u in tu) == 0)
ck('APICI: 2 in inglese (nome Rano\'erek), 4 in italiano (le due indennità)',
   sum(u['english'].count(APOS) for u in tu) == 2 and sum(u['italian'].count(APOS) for u in tu) == 4
   and sorted(u['idx'] for u in tu if APOS in u['italian']) == [15, 19, 20, 24],
   (sum(u['english'].count(APOS) for u in tu), sum(u['italian'].count(APOS) for u in tu)))
ck('SEGNAPOSTI: 29 in 6 famiglie, con ordine identico per unita',
   collections.Counter(t for u in tu for t in TAG.findall(u['english'])) ==
   collections.Counter(t for u in tu for t in TAG.findall(u['italian'])) ==
   collections.Counter({'<payment>': 10, '<planet>': 8, '<waypoints>': 4, '<npc>': 3,
                        '<npc model>': 2, '<destination>': 2})
   and not [u['idx'] for u in tu if TAG.findall(u['english']) != TAG.findall(u['italian'])])
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in tu for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90 per ogni unita',
   all(0.55 < u['ratio'] < 1.90 for u in tu),
   [(u['idx'], u['ratio']) for u in tu if not 0.55 < u['ratio'] < 1.90])
ck('fazioni invariante: Remnant e Korath presenti, nessun «Remnants»',
   'Remnant' in tu[1]['italian'] and 'Korath' in tu[1]['italian']
   and 'Remnants' not in ' '.join(u['italian'] for u in tu))
ck('tutte le 25 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in tu))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('SEGMENTO: 0 prima · 25 qui · 62 dopo · 7 contesti · 29 segnaposto in 6 famiglie')
print('parole EN %d -> IT %d · ratio %.2f - %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(u['ratio'] for u in tu), max(u['ratio'] for u in tu)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L261 superato' if not fail else 'verify L261 fallito')
raise SystemExit(0 if not fail else 1)
