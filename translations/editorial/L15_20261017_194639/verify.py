"""verify.py — L15 (lotto finale di map planets.txt)

Controlli indipendenti da check.py:
  1. la riga grezza di ogni unità coincide con la riga del file sorgente
  2. english / kind / path / state coincidono con il database
  3. gli id sono univoci in translation.json
  4. collocazione del lotto nel file e stato del tratto successivo
"""
import json
import os
import sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
ROOT = os.path.abspath(os.path.join(L10N, '..'))
SRC = os.path.join(ROOT, 'endless-sky', 'data', 'map planets.txt')

source = json.load(open(os.path.join(HERE, 'source.json')))
trans = json.load(open(os.path.join(HERE, 'translation.json')))
su = source['units']
tu = trans['units']

lines = open(SRC, encoding='utf-8').read().split('\n')

# 1. riga grezza
bad_raw = [u['idx'] for u in su if lines[u['line'] - 1] != u['raw']]
print('riga grezza identica al file: ', 'OK' if not bad_raw else 'FAIL %s' % bad_raw)

# 2. campi dal database
db = sqlite3.connect(os.path.join(L10N, 'state.db'))
db.row_factory = sqlite3.Row
bad_db = []
bad_state = []
for u in su:
    row = db.execute('select english, kind, path, state from units where id = ?', (u['id'],)).fetchone()
    if row is None or row['english'] != u['english'] or row['kind'] != u['kind'] \
            or row['path'] != u['path']:
        bad_db.append(u['idx'])
    elif row['state'] != 'PENDING':
        bad_state.append((u['idx'], row['state']))
print('english/kind/path identici al DB:', 'OK' if not bad_db else 'FAIL %s' % bad_db)
print('state = PENDING per tutte le unita:', 'OK' if not bad_state else 'FAIL %s' % bad_state)

# 3. id univoci
ids = [u['id'] for u in tu]
print('id univoci in translation.json:', len(ids) == len(set(ids)))

# 4. collocazione
first, last = tu[0]['line'], tu[-1]['line']
print('unita: %d righe %d - %d' % (len(tu), first, last))

nxt = db.execute("select line, context from units where path = 'data/map planets.txt' "
                 "and line > ? order by line limit 1", (last,)).fetchone()
print('unita successiva nel file:', (nxt['line'], nxt['context']) if nxt else 'nessuna')

tot = db.execute("select count(*) from units where path = 'data/map planets.txt'").fetchone()[0]
print('map planets.txt: %d unita totali nel DB' % tot)

resto = db.execute("select count(*), sum(length(english)-length(replace(english,' ',''))+1) "
                   "from units where path = 'data/map planets.txt' and line > ?", (last,)).fetchone()
print('unita del file dopo la riga %d: %d (%s parole), gia tradotte da L1-L4' % (last, resto[0], resto[1]))

# copertura complessiva: somma delle unita di tutti i lotti in staging
tot_staging = 0
for name in sorted(os.listdir(os.path.join(L10N, 'staging', 'editorial'))):
    f = os.path.join(L10N, 'staging', 'editorial', name, 'translation.json')
    if os.path.exists(f):
        tot_staging += len(json.load(open(f))['units'])
print('unita in staging (tutti i lotti):', tot_staging)
print('copertura di map planets.txt:', '%d / %d' % (tot_staging, tot))
print('stato:', 'COMPLETA' if tot_staging == tot else 'INCOMPLETA')
