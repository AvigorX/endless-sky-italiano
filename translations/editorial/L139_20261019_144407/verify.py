r"""verify.py — L139 (`data/starts.txt`, 2 unita', righe 365-366). **CHIUDE IL FILE**.

Invariante di **file**: legge i **cinque** `translation.json` del percorso e dimostra che `data/starts.txt` e'
**113/113**, con **sovrapposti = 0** e `max(line) = 366`. Il totale viene dalla somma dei lotti, non da un numero
scritto a mano.
"""
import collections
import hashlib
import json
import os
import re
import sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
ROOT = os.path.abspath(os.path.join(L10N, '..'))
PATH = 'data/starts.txt'
LOTS = [os.path.abspath(os.path.join(L10N, 'staging', 'editorial', d)) for d in
        ('L135_20261019_131024', 'L136_20261019_133830', 'L137_20261019_140902', 'L138_20261019_142846',
         'L139_20261019_144407')]
TAGS = re.compile(r'<[^<>]+>')
su = sorted(json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
by = {u['idx']: u for u in tu}
lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
fail = []


def ck(n, c, d=''):
    print('%-70s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente', not [u for u in su if lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck('idx 1..2 e ordine = sorgente', [u['idx'] for u in tu] == [1, 2] == [u['idx'] for u in su])
ck('unita: 2 righe 365 - 366', len(tu) == 2 and (tu[0]['line'], tu[-1]['line']) == (365, 366))
ck('111 unita prima della riga 365 (L135 + L136 + L137 + L138)', db.execute(
    'select count(*) from units where path=? and line<?', (PATH, 365)).fetchone()[0] == 111)
ck('ZERO unita dopo: il lotto chiude il file',
   db.execute('select count(*) from units where path=? and line>?', (PATH, 366)).fetchone()[0] == 0)
ck('max(line) del file = 366', db.execute('select max(line) from units where path=?', (PATH,)).fetchone()[0] == 366)
ck('tipi: 2 TEXT', collections.Counter(u['kind'] for u in su) == {'TEXT': 2})
ck('ZERO VALUE, ZERO UI_LABEL, ZERO token (tre asserzioni vuote)',
   [u['idx'] for u in su if u['kind'] in ('VALUE', 'UI_LABEL')] == []
   and collections.Counter(t for u in su for t in TAGS.findall(u['english'])) == {})
ck('i due nomi sono identici al sorgente (ID_OK)',
   [u['italian'] for u in tu] == ['"Benga" Atomic Thruster', '"Biroo" Atomic Steering'])
ck('tutte PENDING',
   not [u['idx'] for u in su
        if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('zero tab, 4 virgolette (due per nome)',
   [u['idx'] for u in tu if '\t' in u['italian']] == []
   and sum(u['italian'].count('"') for u in tu) == 4)
ck('1 contesto: 2 unita', list(collections.Counter(u['context'] for u in su).values()) == [2])
rs = [u['ratio'] for u in tu]
ck('rapporto 1.00 (testi identici)', all(r == 1.0 for r in rs), rs)
ck('nessun carattere non latino, nessun carattere tipografico',
   not [u['idx'] for u in tu if any(ord(c) > 126 for c in u['italian'])])
merged = {}
for f in sorted(os.listdir(os.path.join(HERE, 'parts'))):
    if f.endswith('.json'):
        for k, v in json.load(open(os.path.join(HERE, 'parts', f), encoding='utf-8')).items():
            merged[int(k)] = v
ck('la parte ricostruisce translation.json (1..2)',
   sorted(merged) == [1, 2] and merged == {u['idx']: u['italian'] for u in tu})

# --- invariante di FILE: i cinque lotti insieme devono coprire 113/113 righe, senza sovrapposizioni ---
seen = collections.Counter()
per_lot = []
for lot in LOTS:
    d = json.load(open(os.path.join(lot, 'translation.json'), encoding='utf-8'))['units']
    per_lot.append(len(d))
    for u in d:
        assert u['path'] == PATH, (lot, u['path'])
        seen[u['line']] += 1
ck('i cinque lotti hanno 32 + 15 + 17 + 47 + 2 = 113 unita', per_lot == [32, 15, 17, 47, 2] and sum(per_lot) == 113,
   per_lot)
ck('file coperto 113/113 righe', len(seen) == 113
   and len(seen) == db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0],
   (len(seen), db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0]))
ck('sovrapposti = 0', [l for l, n in seen.items() if n > 1] == [], [l for l, n in seen.items() if n > 1])
ck('max(line) coperta = 366', max(seen) == 366, max(seen))
ck('nessuna unita del file resta fuori', not [l for l, _ in db.execute(
    'select line,id from units where path=?', (PATH,)).fetchall() if l not in seen])
ck('nessun altro lotto rivendica righe di starts.txt',
   not [f for f in os.listdir(os.path.join(L10N, 'staging/editorial'))
        if f.startswith('L') and os.path.exists(os.path.join(L10N, 'staging/editorial', f, 'translation.json'))
        and os.path.abspath(os.path.join(L10N, 'staging/editorial', f)) not in LOTS
        and any(u['path'] == PATH for u in json.load(open(os.path.join(L10N, 'staging/editorial', f,
                'translation.json'), encoding='utf-8'))['units'])])
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('file CHIUSO: 113/113 (100.0%) · cinque lotti 32 + 15 + 17 + 47 + 2 · sovrapposti 0 · max(line) 366')
print('parole EN %d -> IT %d · rapporto %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu), rs[0]))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L139 superato' if not fail else 'verify L139 fallito')
raise SystemExit(0 if not fail else 1)
