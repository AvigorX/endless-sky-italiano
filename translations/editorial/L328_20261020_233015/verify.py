r"""verify.py — L328 (`data/_ui/help.txt`, righe 72–116). **SECONDO DI TRE LOTTI — NON TERMINALE.**

Verifica da sola, con meccanismi **diversi** da `check.py`:

- rilegge il **testo approvato dal database** e lo confronta con `translation.json` **unità per unità**;
- verifica che `state.db` **non sia stato riscritto** (`mtime` del database **anteriore** a `translation.json`);
- verifica l'**invariante di SEGMENTO** — 25 unità proprie in 72–116, righe distinte, **nessun altro lotto** sulle stesse righe, confine
  alla **119** — **senza** contare i lotti del file;
- verifica **per riga** che le virgolette dell'italiano siano nelle stesse righe dell'inglese, e che il segnaposto sia **uno solo**;
- misura la **divergenza terminologica** dichiarata: il testo approvato usa «fornitore», non «emporio».

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
RIGHE = (72, 116)
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


ck('riga grezza identica al sorgente (25/25)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
bad = [u['idx'] for u in su
       if db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
       != (u['english'], u['kind'], u['path'], u['context'])]
ck('english/kind/path/context identici al DB', not bad, bad)
ck('25 unita HELP, 11 contesti',
   len(tu) == 25 and collections.Counter(u['kind'] for u in tu) == {'HELP': 25}
   and len({u['context'] for u in tu}) == 11)
approvato = {r[0]: r[1] for r in db.execute(
    'select id, italian from units where path=? and line between ? and ?', (PATH, RIGHE[0], RIGHE[1]))}
ck('25/25: il testo in staging E il testo approvato del database',
   len(approvato) == 25 and all(approvato[u['id']] == u['italian'] for u in tu),
   [u['line'] for u in tu if approvato.get(u['id']) != u['italian']])
ck('le 25 unita sono APPROVED, e nessuna e stata cambiata di stato',
   collections.Counter(db.execute('select state from units where path=? and line between ? and ?',
                                  (PATH, RIGHE[0], RIGHE[1])).fetchall()) == {('APPROVED',): 25})
ck('NESSUN BACKUP SCRITTO: state.db piu vecchio di translation.json',
   os.path.getmtime(os.path.join(L10N, 'state.db')) < os.path.getmtime(os.path.join(HERE, 'translation.json')))
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
ck('SEGMENTO: 25 righe distinte, prima 72, ultima 116, nessuna fuori finestra',
   len(righe) == 25 and min(righe) == 72 and max(righe) == 116
   and all(RIGHE[0] <= l <= RIGHE[1] for l in righe))
ck('SEGMENTO: nessun ALTRO lotto tocca queste righe', not altri, altri)
ck('SEGMENTO: dopo la 116 c e la 119 (help:fleet asteroid mining), che NON e nel lotto',
   db.execute('select line, context from units where path=? and line>? order by line limit 1',
              (PATH, RIGHE[1])).fetchone() == (119, 'help:fleet asteroid mining')
   and 119 not in at)
ck('SEGMENTO: L327 resta separato (finisce alla 69) e il file ha 113 unita',
   db.execute('select count(*) from units where path=? and line between 15 and 69', (PATH,)).fetchone()[0] == 28
   and db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0] == 113)
ck('il segnaposto: 1 sola occorrenza, identica all inglese',
   collections.Counter(t for u in tu for t in TAG.findall(u['italian'])) == {'<View player info>': 1}
   and all(TAG.findall(u['english']) == TAG.findall(u['italian']) for u in tu))
ck('le virgolette dell italiano cadono nelle STESSE righe dell inglese (93, 105, 106)',
   {u['line'] for u in tu if u['italian'].count(QUOTE)} == {u['line'] for u in tu if u['english'].count(QUOTE)}
   == {93, 105, 106}
   and sum(u['italian'].count(QUOTE) for u in tu) == 10)
ck('DIVERGENZA DICHIARATA: 5 unita usano «fornitore» e NESSUNA usa «emporio»',
   sum(1 for u in tu if 'fornitor' in u['italian'].lower()) == 5
   and not any('emporio' in u['italian'].lower() for u in tu))
ck('nessuna tab, nessun doppio spazio, nessun carattere tipografico',
   not [u['idx'] for u in tu if TAB in u['italian'] or '  ' in u['italian']]
   and not [c for u in tu for c in u['italian'] if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026'])
ck('rapporto nel gate 0,55-1,90',
   all(0.55 < u['ratio'] < 1.90 for u in tu),
   [(u['idx'], u['ratio']) for u in tu if not 0.55 < u['ratio'] < 1.90])
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('SEGMENTO: righe 72-116 · 25 unita proprie · 11 contesti · 113 unita nel file (copertura 53/113 con L327)')
print('parole EN %d -> IT %d · ratio %.2f - %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(u['ratio'] for u in tu), max(u['ratio'] for u in tu)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L328 superato' if not fail else 'verify L328 fallito')
raise SystemExit(0 if not fail else 1)
