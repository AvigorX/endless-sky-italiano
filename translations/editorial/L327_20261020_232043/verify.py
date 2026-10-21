r"""verify.py — L327 (`data/_ui/help.txt`, righe 15-69). **PRIMO DI TRE LOTTI — NON TERMINALE.**

Verifica da sola, con meccanismi **diversi** da `check.py`:

- rilegge il **testo approvato dal database** e lo confronta con `translation.json` **unita' per unita'** (e' il fatto centrale del
  lotto: qui **non si traduce**, si **trascrive** un testo gia' approvato);
- verifica che `state.db` **non sia stato riscritto**: il suo **mtime** deve essere **anteriore** a `translation.json`;
- verifica l'**invariante di SEGMENTO**: 28 unita' proprie dentro 15–69, righe distinte, **nessun altro lotto** sulle stesse righe, e il
  confine dopo alla riga **72** (`help:map advanced`) — **senza** contare i lotti del file;
- verifica i **segnaposto** (14 in 5 forme) contando **le occorrenze**, e le **virgolette** (12) riga per riga.

Indipendente da `check.py`.
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
TAG = re.compile(r'<[^<>]+>')
HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
ROOT = os.path.abspath(os.path.join(L10N, '..'))
PATH = 'data/_ui/help.txt'
RIGHE = (15, 69)
TAG_ATTESI = {'<Initiate hyperspace jump>': 5, '<Show main menu>': 4, '<View star map>': 3,
              '<Select next ship>': 1, '<Talk to selected ship>': 1}
src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
su = sorted(src['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
raw_lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
by = {u['idx']: u for u in tu}
at = {u['line']: u for u in tu}
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
fail = []


def ck(n, c, d=''):
    print('%-96s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente (28/28)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
bad = [u['idx'] for u in su
       if db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
       != (u['english'], u['kind'], u['path'], u['context'])]
ck('english/kind/path/context identici al DB', not bad, bad)
ck('28 unita HELP, 14 contesti', len(tu) == 28
   and collections.Counter(u['kind'] for u in tu) == {'HELP': 28}
   and len({u['context'] for u in tu}) == 14)
approvato = {r[0]: r[1] for r in db.execute(
    'select id, italian from units where path=? and line between ? and ?', (PATH, RIGHE[0], RIGHE[1]))}
ck('28/28: il testo in staging E il testo approvato del database',
   len(approvato) == 28 and all(approvato[u['id']] == u['italian'] for u in tu),
   [u['line'] for u in tu if approvato.get(u['id']) != u['italian']])
ck('le 28 unita sono APPROVED, e nessuna e stata cambiata di stato',
   collections.Counter(db.execute('select state from units where path=? and line between ? and ?',
                                  (PATH, RIGHE[0], RIGHE[1])).fetchall()) == {('APPROVED',): 28})
mt_db = os.path.getmtime(os.path.join(L10N, 'state.db'))
mt_tr = os.path.getmtime(os.path.join(HERE, 'translation.json'))
ck('NESSUN BACKUP SCRITTO: state.db piu vecchio di translation.json',
   mt_db < mt_tr, (mt_db, mt_tr))
righe, altri = set(), []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    if os.path.basename(os.path.dirname(f)) == os.path.basename(HERE):
        continue
    us = [u for u in json.load(open(f, encoding='utf-8'))['units']
          if u['path'] == PATH and RIGHE[0] <= u['line'] <= RIGHE[1]]
    if us:
        altri.append((os.path.basename(os.path.dirname(f)), len(us)))
for u in tu:
    righe.add(u['line'])
ck('SEGMENTO: 28 righe distinte, prima 15, ultima 69, nessuna fuori finestra',
   len(righe) == 28 and min(righe) == 15 and max(righe) == 69
   and all(RIGHE[0] <= l <= RIGHE[1] for l in righe))
ck('SEGMENTO: nessun ALTRO lotto tocca queste righe', not altri, altri)
ck('SEGMENTO: dopo la 69 c e la 72 (help:map advanced), che NON e nel lotto',
   db.execute('select line, context from units where path=? and line>? order by line limit 1',
              (PATH, RIGHE[1])).fetchone() == (72, 'help:map advanced')
   and 72 not in at)
ck('le unita del file sono 113: il lotto ne copre 28 (copertura parziale DICHIARATA)',
   db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0] == 113)
ck('i segnaposto: 14 occorrenze in 5 forme, e ogni unita ha gli stessi del suo inglese',
   collections.Counter(t for u in tu for t in TAG.findall(u['italian'])) == TAG_ATTESI
   and all(TAG.findall(u['english']) == TAG.findall(u['italian']) for u in tu))
ck('le virgolette: 12 in tutto, su quattro righe',
   sum(u['italian'].count(QUOTE) for u in tu) == 12
   and sum(1 for u in tu if u['italian'].count(QUOTE)) == 4)
ck('nessuna tab, nessun doppio spazio, nessun carattere tipografico',
   not [u['idx'] for u in tu if TAB in u['italian'] or '  ' in u['italian']]
   and not [c for u in tu for c in u['italian'] if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026'])
ck('rapporto nel gate 0,55-1,90',
   all(0.55 < u['ratio'] < 1.90 for u in tu),
   [(u['idx'], u['ratio']) for u in tu if not 0.55 < u['ratio'] < 1.90])
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('SEGMENTO: righe 15-69 · 28 unita proprie · 14 contesti · 113 unita nel file (copertura 28/113)')
print('parole EN %d -> IT %d · ratio %.2f - %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(u['ratio'] for u in tu), max(u['ratio'] for u in tu)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L327 superato' if not fail else 'verify L327 fallito')
raise SystemExit(0 if not fail else 1)
