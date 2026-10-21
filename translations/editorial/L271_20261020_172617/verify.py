r"""verify.py — L271 (`data/dialog phrases.txt`, righe 16-98). **Primo lotto del file**.

Verifica da sola: riga grezza, campi del DB, il **segmento** (0 prima — apre il file — 29 qui, **25** dopo la 98), i **venti
contesti** con le righe, i **45 segnaposto** in **dieci famiglie**, e che **nessun altro lotto** rivendichi queste righe.
Verifica **anche la composizione** del phrase dei pirati, ricostruita dai soli frammenti italiani.

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
CTX = ['generic arrived-without-npc dialog', 'generic safe escort completion dialog',
       'generic pirate attack payment dialog', 'generic cargo delivery payment', 'generic cargo on visit',
       'generic passenger dropoff payment', 'generic passenger on visit', 'generic cargo and passenger on visit',
       'generic mineral delivery payment', 'generic mineral on visit',
       'generic missing stopover or cargo and passengers', 'generic missing stopover or passengers',
       'generic missing stopover or cargo', 'generic missing stopover or escort',
       'generic missing waypoint or cargo and passengers', 'generic missing waypoint or passengers',
       'generic missing waypoint or cargo', 'generic stopover on visit', 'generic waypoint on visit',
       'generic hunted bounty eliminated and payment dialog']
TOK = {'<planet>': 17, '<npc>': 4, '<payment>': 7, '<commodity>': 1, '<passengers>': 2,
       '<amount>': 2, '<mineral>': 2, '<origin>': 1, '<stopovers>': 5, '<waypoints>': 4}
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


ck('riga grezza identica al sorgente (29/29)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = [u['idx'] for u in su
       if db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
       != (u['english'], u['kind'], u['path'], u['context'])]
ck('english/kind/path/context identici al DB', not bad, bad)
ck('29 unita, righe 16-98, tutte TEXT',
   len(tu) == 29 and [u['line'] for u in tu] == sorted({u['line'] for u in tu})
   and {u['kind'] for u in tu} == {'TEXT'}, (len(tu), {u['kind'] for u in tu}))
ck('i venti contesti `phrase:` compaiono in quest ordine, senza altri',
   [c.replace('phrase:', '', 1) for c in dict.fromkeys(u['context'] for u in tu)] == CTX,
   [c for c in dict.fromkeys(u['context'] for u in tu)])
ck("ZERO unita' prima della 16: il lotto APRE il file",
   db.execute('select count(*) from units where path=? and line<16', (PATH,)).fetchone()[0] == 0)
ck("25 unita' dopo la 98", db.execute('select count(*) from units where path=? and line>98', (PATH,)).fetchone()[0] == 25)
ck('confine: la 102 apre un contesto nuovo (`hunted bounty eliminated`)',
   db.execute('select line,context from units where path=? and line>98 order by line limit 1', (PATH,)).fetchone()
   == (102, 'phrase:generic hunted bounty eliminated dialog'))
ck('il file ha 54 unita, righe 16-172',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (54, 16, 172))
per_lotto, righe = [], set()
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    us = [u for u in json.load(open(f, encoding='utf-8'))['units'] if u['path'] == PATH]
    if us:
        per_lotto.append((os.path.basename(os.path.dirname(f)), len(us)))
        righe |= {u['line'] for u in us}
seg = {l for l in righe if 16 <= l <= 98}
ck('SEGMENTO: le 29 righe del lotto sono esattamente quelle 16-98',
   seg == {u['line'] for u in tu} and len(seg) == 29, (sorted(seg - {u['line'] for u in tu}), len(seg)))
overlap = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    if os.path.basename(os.path.dirname(f)) == os.path.basename(HERE):
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH and 16 <= u['line'] <= 98:
            overlap.append((os.path.basename(os.path.dirname(f)), u['line']))
ck('nessun altro lotto rivendica le righe 16-98', not overlap, overlap)
ck('copertura del SEGMENTO: 29/29 righe; il totale del file e stampato, non asserito',
   len(seg) == 29 and 54 - len(seg) == 25, '%d/54 (file)' % len(righe))
ck('tutte tradotte, nessuna copiata',
   not [u['idx'] for u in tu if u['italian'] == u['english']],
   [u['idx'] for u in tu if u['italian'] == u['english']])
ck('segnaposto per famiglia: 45 token, dieci famiglie, identici in inglese e italiano',
   {t: sum(collections.Counter(TAG.findall(u['english']))[t] for u in tu) for t in TOK} == TOK
   == {t: sum(collections.Counter(TAG.findall(u['italian']))[t] for u in tu) for t in TOK})
ck('composizione del phrase dei pirati: 12 combinazioni ben formate, ricostruite dai frammenti',
   len([1 for a in [' ', by[4]['italian']] for b in [by[6]['italian'], by[7]['italian']]
        for c in [by[9]['italian'], by[10]['italian'], by[11]['italian']]]) == 12
   and not [s for a in [' ', by[4]['italian']] for b in [by[6]['italian'], by[7]['italian']]
            for c in [by[9]['italian'], by[10]['italian'], by[11]['italian']]
            for s in [by[3]['italian'] + a + by[5]['italian'] + b + by[8]['italian'] + c]
            if '  ' in s or not s.endswith('.') or s.count('<payment>') != 1])
ck('zero tab e zero virgolette',
   sum(u['english'].count(TAB) + u['italian'].count(TAB) for u in tu) == 0
   and sum(u['english'].count(QUOTE) + u['italian'].count(QUOTE) for u in tu) == 0)
ck('apici: 17 in inglese, zero in italiano',
   sum(u['english'].count(APOS) for u in tu) == 17 and sum(u['italian'].count(APOS) for u in tu) == 0,
   (sum(u['english'].count(APOS) for u in tu), sum(u['italian'].count(APOS) for u in tu)))
ck('spazi finali solo nei frammenti 4, 6, 7, 8 (strutturali), nessun doppio spazio',
   sorted(u['idx'] for u in tu if u['italian'] != u['italian'].rstrip()) == [4, 6, 7, 8]
   and not [u['idx'] for u in tu if '  ' in u['italian']])
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in tu for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('rapporto nel gate 0,55-1,90 per le 20 FRASI; i frammenti 4 e 8 sono fuori gate per costruzione',
   all(0.55 < u['ratio'] < 1.90 for u in tu if u['idx'] not in range(3, 12))
   and sorted(u['idx'] for u in tu if u['idx'] in range(3, 12) and not 0.55 < u['ratio'] < 1.90) == [4, 8],
   [(u['idx'], u['ratio']) for u in tu if not 0.55 < u['ratio'] < 1.90])
ck('tutte le 29 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in tu))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('SEGMENTO: 0 prima (apre il file) · 29 qui · 25 dopo · 20 contesti · 45 segnaposto')
print('parole EN %d -> IT %d · ratio %.2f - %.2f (frasi) ' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(u['ratio'] for u in tu if u['idx'] not in range(3, 12)),
    max(u['ratio'] for u in tu if u['idx'] not in range(3, 12))))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L271 superato' if not fail else 'verify L271 fallito')
raise SystemExit(0 if not fail else 1)
