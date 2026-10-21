r"""verify.py — L331 (`data/human/power.txt`, 23–272). **TERMINALE, FILE INTERO.** Indipendente da `check.py`."""
import glob
import hashlib
import json
import os
import sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
ROOT = os.path.abspath(os.path.join(L10N, '..'))
PATH = 'data/human/power.txt'
src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
su = sorted(src['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
raw = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
fail = []


def ck(n, c, d=''):
    print('%-92s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente (22/22)', not [u for u in su if raw[u['line'] - 1] != u['raw']])
ck('english/kind/path/context identici al DB',
   not [u['idx'] for u in su if db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
        != (u['english'], u['kind'], u['path'], u['context'])])
ck('22 unità PENDING, nessuna identica all inglese, nessuna approvata',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in tu)
   and not [u for u in tu if u['italian'] == u['english']])
righe = {u['line'] for u in tu}
ck('FILE: 22 righe distinte, prima 23, ultima 272',
   len(righe) == 22 and min(righe) == 23 and max(righe) == 272)
ck('FILE: copertura 22/22 (100%) e un solo lotto',
   len(righe) == db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0] == 22
   and sum(1 for f in glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))
           if any(u['path'] == PATH for u in json.load(open(f, encoding='utf-8'))['units'])) == 1)
ck('zero tab, zero virgolette, zero segnaposto (asserzioni vuote)',
   not [u for u in tu if '\t' in u['italian'] or '"' in u['italian'] or '<' in u['italian']])
ck('rapporto nel gate 0,55-1,90', all(0.55 < u['ratio'] < 1.90 for u in tu),
   [(u['idx'], u['ratio']) for u in tu if not 0.55 < u['ratio'] < 1.90])
ck('nessun carattere tipografico o doppio spazio spurio',
   not [c for u in tu for c in u['italian'] if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026']
   and not [u['idx'] for u in tu if '  ' in u['italian']])
ck('state.db non riscritto (mtime anteriore a translation.json)',
   os.path.getmtime(os.path.join(L10N, 'state.db')) < os.path.getmtime(os.path.join(HERE, 'translation.json')))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('FILE: 22/22 · parole EN %d -> IT %d · 22 contesti' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L331 superato' if not fail else 'verify L331 fallito')
raise SystemExit(0 if not fail else 1)
