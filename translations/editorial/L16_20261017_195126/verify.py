"""verify.py — L16 (primo lotto di data/human/human missions.txt)

Controlli indipendenti da check.py:
  1. la riga grezza di ogni unità coincide con la riga del file sorgente
  2. english / kind / path / state coincidono con il database
  3. gli id sono univoci in translation.json
  4. collocazione del lotto nel file, tratto successivo, copertura del file
  5. la riga `log` tripla (categoria, nome, testo) resta un tripletto coerente
"""
import json
import os
import sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
ROOT = os.path.abspath(os.path.join(L10N, '..'))
PATH = 'data/human/human missions.txt'
SRC = os.path.join(ROOT, 'endless-sky', *PATH.split('/'))

source = json.load(open(os.path.join(HERE, 'source.json')))
trans = json.load(open(os.path.join(HERE, 'translation.json')))
su, tu = source['units'], trans['units']

lines = open(SRC, encoding='utf-8').read().split('\n')

bad_raw = [u['idx'] for u in su if lines[u['line'] - 1] != u['raw']]
print('riga grezza identica al file: ', 'OK' if not bad_raw else 'FAIL %s' % bad_raw)

db = sqlite3.connect(os.path.join(L10N, 'state.db'))
db.row_factory = sqlite3.Row
bad_db, bad_state = [], []
for u in su:
    row = db.execute('select english, kind, path, state from units where id = ?', (u['id'],)).fetchone()
    if row is None or row['english'] != u['english'] or row['kind'] != u['kind'] \
            or row['path'] != u['path']:
        bad_db.append(u['idx'])
    elif row['state'] != 'PENDING':
        bad_state.append((u['idx'], row['state']))
print('english/kind/path identici al DB:', 'OK' if not bad_db else 'FAIL %s' % bad_db)
print('state = PENDING per tutte le unita:', 'OK' if not bad_state else 'FAIL %s' % bad_state)

ids = [u['id'] for u in tu]
print('id univoci in translation.json:', len(ids) == len(set(ids)))

first, last = tu[0]['line'], tu[-1]['line']
print('unita: %d righe %d - %d' % (len(tu), first, last))

nxt = db.execute('select line, context from units where path = ? and line > ? '
                 'order by line limit 1', (PATH, last)).fetchone()
print('unita successiva nel file:', (nxt['line'], nxt['context']) if nxt else 'nessuna')

lastline = db.execute('select max(line) from units where path = ?', (PATH,)).fetchone()[0]
tot = db.execute('select count(*) from units where path = ?', (PATH,)).fetchone()[0]
resto = db.execute('select count(*), sum(length(english)-length(replace(english," ",""))+1) '
                   'from units where path = ? and line > ?', (PATH, last)).fetchone()
print('%s: %d unita totali, ultima riga %d' % (PATH, tot, lastline))
print('unita del file dopo la riga %d: %d (%s parole)' % (last, resto[0], resto[1]))

# copertura del solo file in corso: somma le unita dei lotti che hanno questo path
tot_staging, lotti = 0, []
for name in sorted(os.listdir(os.path.join(L10N, 'staging', 'editorial'))):
    f = os.path.join(L10N, 'staging', 'editorial', name, 'translation.json')
    if not os.path.exists(f):
        continue
    d = json.load(open(f))['units']
    if d and d[0]['path'] == PATH:
        tot_staging += len(d)
        lotti.append((name, len(d)))
print('lotti su questo file:', lotti)
print('copertura di %s: %d / %d' % (PATH, tot_staging, tot))
print('stato:', 'IN CORSO' if tot_staging < tot else 'COMPLETA', '(lotto %d di %d)' % (tot_staging, tot))

# riga `log` tripla: categoria, nome, testo sulla stessa riga di sorgente
multi = {}
for u in tu:
    multi.setdefault(u['line'], []).append(u['idx'])
tri = [(l, ids_) for l, ids_ in multi.items() if len(ids_) > 1]
print('righe con piu unita:', tri or 'nessuna')
if tri:
    l, idxs = tri[0]
    txt = [u['english'] for u in su if u['idx'] in idxs]
    ok = len(idxs) == 3 and txt[1] == 'Puny' and txt[0] == 'Minor People'
    print('tripletto log (categoria, nome, testo) alla riga %d:' % l, 'OK' if ok else 'FAIL %s' % txt)
