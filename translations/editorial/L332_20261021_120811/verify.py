r"""verify.py — L332 (`data/human/south jobs.txt`, 15–347). **TERMINALE, FILE INTERO.** Indipendente da `check.py`."""
import collections
import glob
import hashlib
import json
import os
import re
import sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
ROOT = os.path.abspath(os.path.join(L10N, '..'))
PATH = 'data/human/south jobs.txt'
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


ck('riga grezza identica al sorgente (40/40)', not [u for u in su if raw[u['line'] - 1] != u['raw']])
ck('english/kind/path/context identici al DB',
   not [u['idx'] for u in su if db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
        != (u['english'], u['kind'], u['path'], u['context'])])
ck('quattro tipi e 40 unità, tutte PENDING e nessuna identica all inglese',
   collections.Counter(u['kind'] for u in tu) == {'VALUE': 14, 'DESCRIPTION': 14, 'DIALOG': 8, 'CONVERSATION': 4}
   and all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in tu)
   and not [u for u in tu if u['italian'] == u['english']])
righe = {u['line'] for u in tu}
ck('FILE: 40 righe distinte, prima 15, ultima 347', len(righe) == 40 and min(righe) == 15 and max(righe) == 347)
ck('FILE: copertura 40/40 e un solo lotto',
   len(righe) == db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0] == 40
   and sum(1 for f in glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))
           if any(u['path'] == PATH for u in json.load(open(f, encoding='utf-8'))['units'])) == 1)
ck('segnaposto per unità identici, e 66 in totale',
   all(re.findall(r'<[^<>]+>', u['english']) == re.findall(r'<[^<>]+>', u['italian']) for u in tu)
   and sum(len(re.findall(r'<[^<>]+>', u['italian'])) for u in tu) == 66)
ck('le due tab sono sulle righe delle scelte (133, 135)',
   sorted(u['line'] for u in tu if u['italian'].startswith('\t')) == [133, 135])
ck('nessuna resa VALUE in inglese e nessuna catena IT/EN',
   all(u['english'] != u['italian'] for u in tu if u['kind'] == 'VALUE')
   and at[15]['italian'] == 'Pirati che occupano <system>')
ck('rapporto nel gate 0,55-1,90', all(0.55 < u['ratio'] < 1.90 for u in tu),
   [(u['idx'], u['ratio']) for u in tu if not 0.55 < u['ratio'] < 1.90])
ck('state.db non riscritto (mtime)', os.path.getmtime(os.path.join(L10N, 'state.db'))
   < os.path.getmtime(os.path.join(HERE, 'translation.json')))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('FILE: 40/40 · parole EN %d -> IT %d · 15 contesti' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L332 superato' if not fail else 'verify L332 fallito')
raise SystemExit(0 if not fail else 1)
