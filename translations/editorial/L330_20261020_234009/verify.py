r"""verify.py — L330 (`data/wanderer/wanderers.txt`, 778–1042). **TERMINALE, FILE INTERO.** Indipendente da `check.py`."""
import collections
import glob
import hashlib
import json
import os
import sqlite3

TAB = chr(9)
HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
ROOT = os.path.abspath(os.path.join(L10N, '..'))
PATH = 'data/wanderer/wanderers.txt'
src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
su = sorted(src['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
raw = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
at = {u['line']: u for u in tu}
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
fail = []


def ck(n, c, d=''):
    print('%-92s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente (15/15)', not [u for u in su if raw[u['line'] - 1] != u['raw']])
ck('english/kind/path/context identici al DB',
   not [u['idx'] for u in su if db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
        != (u['english'], u['kind'], u['path'], u['context'])])
ck('15 unità PENDING, nessuna approvata, nessuna identica all inglese',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in tu)
   and not [u for u in tu if u['italian'] == u['english']])
righe = {u['line'] for u in tu}
ck('FILE: 15 righe distinte, prima 778, ultima 1042, nessuna fuori',
   len(righe) == 15 and min(righe) == 778 and max(righe) == 1042
   and db.execute('select count(*) from units where path=? and (line<778 or line>1042)', (PATH,)).fetchone()[0] == 0)
ck('FILE: copertura 15/15 (100%)',
   len(righe) == db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0] == 15)
ck('FILE: un solo lotto su questo file',
   sum(1 for f in glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))
       if any(u['path'] == PATH for u in json.load(open(f, encoding='utf-8'))['units'])) == 1)
ck('le 4 tab stanno nelle righe attese',
   sorted(u['line'] for u in tu if u['italian'].startswith(TAB)) == [884, 999, 1001, 1041])
ck('rapporto nel gate e conteggi coerenti (0 virgolette, 0 segnaposto)',
   all(0.55 < u['ratio'] < 1.90 for u in tu)
   and sum(u['italian'].count('"') for u in tu) == 0
   and '<' not in ''.join(u['italian'] for u in tu))
ck('nessun carattere tipografico o doppio spazio spurio',
   not [c for u in tu for c in u['italian'] if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026']
   and not [u['idx'] for u in tu if '  ' in u['italian'].lstrip(TAB)])
ck('state.db non riscritto (mtime anteriore a translation.json)',
   os.path.getmtime(os.path.join(L10N, 'state.db')) < os.path.getmtime(os.path.join(HERE, 'translation.json')))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('FILE: 15/15 · parole EN %d -> IT %d · 4 contesti' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L330 superato' if not fail else 'verify L330 fallito')
raise SystemExit(0 if not fail else 1)
