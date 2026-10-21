r"""verify.py — L262 (`data/remnant/remnant jobs.txt`, righe 226-490). **Secondo lotto del file**.

Verifica da sola: riga grezza, campi del DB, il **segmento** (25 prima, 29 qui, **33** dopo la 490), i **nove contesti** in
sequenza, i **43 segnaposto** per famiglia e per ordine, gli **8 `VALUE` copiati**, `Ember Waste` **invariato**, e che
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
CTXS = ['mission:Remnant: Bounty 4', 'mission:Remnant: Bounty 5',
        'mission:Remnant: Logistics Civil Engineering', 'mission:Remnant: Logistics Industrial Delivery',
        'mission:Remnant: Logistics Outfitter Delivery', 'mission:Remnant: Logistics Salvage Delivery',
        'mission:Remnant: Rescue', 'mission:Remnant: Rescue 1B', 'mission:Remnant: Rescue 2']
src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
su = sorted(src['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
raw_lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
fail = []


def ck(n, c, d=''):
    print('%-96s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente (29/29)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = [u['idx'] for u in su
       if db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
       != (u['english'], u['kind'], u['path'], u['context'])]
ck('english/kind/path/context identici al DB', not bad, bad)
ck('29 unita, righe 226-490, tipi 9/8/7/5',
   len(tu) == 29 and [u['line'] for u in tu] == sorted({u['line'] for u in tu})
   and collections.Counter(u['kind'] for u in tu)
   == {'DIALOG': 9, 'VALUE': 8, 'DESCRIPTION': 7, 'MISSION_TEXT': 5},
   (len(tu), collections.Counter(u['kind'] for u in tu)))
ck('i nove contesti compaiono in quest ordine, senza altri',
   [c for c in dict.fromkeys(u['context'] for u in tu)] == CTXS,
   [c for c in dict.fromkeys(u['context'] for u in tu)])
ck("25 unita' prima, e la precedente e in `Bounty 4`",
   db.execute('select count(*) from units where path=? and line<226', (PATH,)).fetchone()[0] == 25
   and db.execute('select context from units where path=? and line<226 order by line desc limit 1', (PATH,)).fetchone()
   == (CTXS[0],))
ck("33 unita' dopo la 490", db.execute('select count(*) from units where path=? and line>490', (PATH,)).fetchone()[0] == 33)
ck('confine: la 491 resta in `Rescue 2`, il contesto dell ultima unita del lotto',
   db.execute('select line,context from units where path=? and line>490 order by line limit 1', (PATH,)).fetchone()
   == (491, CTXS[8]))
ck('il file ha 87 unita, righe 19-741',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (87, 19, 741))
per_lotto, righe = [], set()
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    us = [u for u in json.load(open(f, encoding='utf-8'))['units'] if u['path'] == PATH]
    if us:
        per_lotto.append((os.path.basename(os.path.dirname(f)), len(us)))
        righe |= {u['line'] for u in us}
seg = {l for l in righe if 226 <= l <= 490}
ck('SEGMENTO: le 29 righe del lotto sono esattamente quelle 226-490',
   seg == {u['line'] for u in tu} and len(seg) == 29, (sorted(seg - {u['line'] for u in tu}), len(seg)))
overlap = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    if os.path.basename(os.path.dirname(f)) == os.path.basename(HERE):
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH and 226 <= u['line'] <= 490:
            overlap.append((os.path.basename(os.path.dirname(f)), u['line']))
ck('nessun altro lotto rivendica le righe 226-490', not overlap, overlap)
ck('copertura del SEGMENTO: 29/29 righe del lotto; il totale del file e stampato, non asserito',
   len(seg) == 29 and 87 - len(seg) == 58, '%d/87 (file)' % len(righe))
ck('gli 8 VALUE sono copiati identici; le altre 21 sono tradotte',
   all(u['italian'] == u['english'] for u in tu if u['kind'] == 'VALUE')
   and all(u['italian'] != u['english'] for u in tu if u['kind'] != 'VALUE'))
ck('ZERO tab e ZERO virgolette in entrambe le lingue',
   sum(u['english'].count(TAB) + u['italian'].count(TAB) for u in tu) == 0
   and sum(u['english'].count(QUOTE) + u['italian'].count(QUOTE) for u in tu) == 0)
ck('APICI: 1 in inglese (unita 6), 8 in italiano su 7 unita',
   sum(u['english'].count(APOS) for u in tu) == 1 and sum(u['italian'].count(APOS) for u in tu) == 8
   and sorted(u['idx'] for u in tu if APOS in u['italian']) == [4, 15, 21, 22, 25, 26, 27],
   (sum(u['english'].count(APOS) for u in tu), sum(u['italian'].count(APOS) for u in tu)))
ck('SEGNAPOSTI: 43 in 5 famiglie, con ordine identico per unita',
   collections.Counter(t for u in tu for t in TAG.findall(u['english'])) ==
   collections.Counter(t for u in tu for t in TAG.findall(u['italian'])) ==
   collections.Counter({'<payment>': 13, '<planet>': 12, '<npc>': 8, '<cargo>': 8, '<destination>': 2})
   and not [u['idx'] for u in tu if TAG.findall(u['english']) != TAG.findall(u['italian'])])
by = {u['idx']: u for u in tu}
ck('`Ember Waste` invariato: 3 in inglese, 3 in italiano, nessuna resa',
   sum(u['english'].count('Ember Waste') for u in tu) == 3
   and sum(u['italian'].count('Ember Waste') for u in tu) == 3
   and not [u['idx'] for u in tu if re.search(r'[Bb]race|[Bb]raci', u['italian'])])
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in tu for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90 per ogni unita',
   all(0.55 < u['ratio'] < 1.90 for u in tu),
   [(u['idx'], u['ratio']) for u in tu if not 0.55 < u['ratio'] < 1.90])
ck('lessico: emporio/empori per outfitter, compenso logistico, assegnazione di risorse',
   "dell'emporio" in by[15]['italian'] and 'empori' in by[18]['italian']
   and 'compenso logistico' in by[9]['italian'] and 'assegnazione di risorse' in by[22]['italian'])
ck('tutte le 29 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in tu))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('SEGMENTO: 25 prima · 29 qui · 33 dopo · 9 contesti · 43 segnaposto in 5 famiglie')
print('parole EN %d -> IT %d · ratio %.2f - %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(u['ratio'] for u in tu), max(u['ratio'] for u in tu)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L262 superato' if not fail else 'verify L262 fallito')
raise SystemExit(0 if not fail else 1)
