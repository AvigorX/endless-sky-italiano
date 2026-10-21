import json, sqlite3, hashlib

D = 'staging/editorial/L10_20261017_192600'
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

# prossima sezione: da 5122 accumulando ~4.500 parole
nxt = c.execute("select id,line,context,english from units where path='data/map planets.txt' and line>2163 order by line").fetchall()
acc, w, out = [], 0, []
for uid, line, ctx, eng in nxt:
    if w >= 4500:
        break
    acc.append((uid, line, ctx, len(eng.split())))
    w += len(eng.split())
print('PROSSIMA SEZIONE: unita %d, righe %d-%d, parole %d, pianeti %d (da %s a %s)' % (
    len(acc), acc[0][1], acc[-1][1], w, len(set(a[2].split('|')[0] for a in acc)),
    acc[0][2].split('|')[0], acc[-1][2].split('|')[0]))
last = acc[-1]
nxtu = c.execute("select line,context from units where path='data/map planets.txt' and line>? order by line limit 1", (last[1],)).fetchone()
print('unita successiva non inclusa: riga %d %s' % (nxtu[0], nxtu[1].split('|')[0]))
# totale lotto L3 fino a 6370
lot = c.execute("select count(*), sum(length(english)-length(replace(english,' ',''))+1) from units where path='data/map planets.txt' and line between 2171 and 3845").fetchone()
print('resto del lotto L3 (2171-3845): %d unita, ~%d parole' % (lot[0], lot[1]))
