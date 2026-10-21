r"""verify.py — L329 (`data/_ui/help.txt`, 119–212). **TERMINALE, chiude il file 113/113.** Indipendente da `check.py`."""
import collections
import glob
import hashlib
import json
import os
import re
import sqlite3

TAB = chr(9)
TAG = re.compile(r'<[^<>]+>')
HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
ROOT = os.path.abspath(os.path.join(L10N, '..'))
PATH = 'data/_ui/help.txt'
APPROVATE = [119, 120, 123, 124, 125, 126, 128, 129, 130, 133, 135, 137, 145, 147, 150]
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


ck('riga grezza identica al sorgente (60/60)', not [u for u in su if raw[u['line'] - 1] != u['raw']])
ck('english/kind/path/context identici al DB',
   not [u['idx'] for u in su if db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
        != (u['english'], u['kind'], u['path'], u['context'])])
ck('GRUPPO APPROVED: 15/15 identiche al testo del database',
   all(db.execute('select italian,state from units where id=?', (at[l]['id'],)).fetchone()
       == (at[l]['italian'], 'APPROVED') for l in APPROVATE))
ck('GRUPPO PENDING: 45/45 ancora PENDING e senza testo nel database',
   all(db.execute('select state,italian from units where id=?', (u['id'],)).fetchone() == ('PENDING', None)
       for u in tu if u['line'] not in APPROVATE))
ck('GRUPPO PENDING: 45 traduzioni, nessuna identica all inglese, gate rispettato',
   len([u for u in tu if u['line'] not in APPROVATE]) == 45
   and not [u for u in tu if u['line'] not in APPROVATE and (u['italian'] == u['english'] or not 0.55 < u['ratio'] < 1.90)])
ck('state.db non riscritto (mtime anteriore a translation.json)',
   os.path.getmtime(os.path.join(L10N, 'state.db')) < os.path.getmtime(os.path.join(HERE, 'translation.json')))
blocchi, righe = {}, set()
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    us = [u for u in json.load(open(f, encoding='utf-8'))['units'] if u['path'] == PATH]
    if us:
        blocchi[os.path.basename(os.path.dirname(f))] = len(us)
        righe |= {u['line'] for u in us}
ck('FILE: tre lotti (28 + 25 + 60) e 113 righe distinte su 113 unità',
   sorted(blocchi.values()) == [25, 28, 60] and len(righe) == 113,
   (blocchi, len(righe)))
ck('FILE: prima 15, ultima 212, nessuna unità fuori',
   min(righe) == 15 and max(righe) == 212
   and db.execute('select count(*) from units where path=? and (line<15 or line>212)', (PATH,)).fetchone()[0] == 0)
ck('FILE: copertura 113/113 asserita',
   len(righe) == db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0] == 113)
ck('i 6 tab cadono nelle righe attese e non altrove',
   sorted(u['line'] for u in tu if u['italian'].startswith(TAB)) == [124, 125, 126, 129, 130, 147])
ck('segnaposto 14, virgolette 38, per unità identici al sorgente',
   sum(len(TAG.findall(u['italian'])) for u in tu) == 14
   and sum(u['italian'].count(chr(34)) for u in tu) == 38
   and all(TAG.findall(u['english']) == TAG.findall(u['italian']) for u in tu))
ck('nessuna tab, caporale o doppio spazio spurio',
   not [c for u in tu for c in u['italian'] if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026']
   and not [u['idx'] for u in tu if '  ' in u['italian'].lstrip(TAB)])
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('FILE: 113/113 · 15 APPROVED trascritte + 45 PENDING tradotte · parole EN %d -> IT %d' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L329 superato' if not fail else 'verify L329 fallito')
raise SystemExit(0 if not fail else 1)
