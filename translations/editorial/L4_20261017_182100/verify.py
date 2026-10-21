import json, sqlite3, hashlib

D = 'staging/editorial/L4_20261017_182100'
src = json.load(open(f'{D}/source.json'))
lines = [l.rstrip('\n') for l in open('../endless-sky/data/map planets.txt', encoding='utf-8')]
c = sqlite3.connect('file:state.db?mode=ro', uri=True)

raw_bad = [u['idx'] for u in src['units'] if u['raw'] != lines[u['line'] - 1]]
db_bad = []
for u in src['units']:
    row = c.execute('select english, kind, context, path, state from units where id=?', (u['id'],)).fetchone()
    if row is None or row[0] != u['english'] or row[3] != u['path'] or row[4] != 'PENDING':
        db_bad.append(u['idx'])
tr = json.load(open(f'{D}/translation.json'))['units']
ids = [v['id'] for v in tr]
print('riga grezza identica al file: ', 'OK' if not raw_bad else raw_bad)
print('english/kind/path/state identici al DB:', 'OK' if not db_bad else db_bad)
print('id univoci in translation.json:', len(ids) == len(set(ids)))
print('unita:', len(tr), 'righe', tr[0]['line'], '-', tr[-1]['line'])

# L4 chiude il file: nessuna sezione successiva
nxt = c.execute("select count(*) from units where path='data/map planets.txt' and line>6802").fetchone()[0]
print('unità dopo la riga 6802 nel file:', nxt)
print('map planets.txt: file esaurito' if nxt == 0 else 'ATTENZIONE: restano unità non tradotte')
print('ultima unità del file:', c.execute("select line,context from units where path='data/map planets.txt' order by line desc limit 1").fetchone())
