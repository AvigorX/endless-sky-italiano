"""verify.py — L19 (quarto lotto di data/human/human missions.txt)

Controlli indipendenti da check.py, che non riusa nulla di check.py:
  1. la riga grezza di ogni unita' coincide con la riga del file sorgente
  2. english / kind / path coincidono con il database, e lo stato e' PENDING
  3. gli id sono univoci in translation.json e l'ordine e' quello del sorgente
  4. collocazione del lotto nel file, unita' successiva, copertura del file
  5. le 39 `label` sono identiche al sorgente e il loro kind nel DB e' UI_LABEL
  6. i token <...> e il numero di tab/virgolette tornano a livello di lotto
"""
import json
import os
import re
import sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
ROOT = os.path.abspath(os.path.join(L10N, '..'))
PATH = 'data/human/human missions.txt'
SRC = os.path.join(ROOT, 'endless-sky', *PATH.split('/'))

source = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
trans = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))
su, tu = source['units'], trans['units']
lines = open(SRC, encoding='utf-8').read().split('\n')

fail = []


def ck(name, cond, detail=''):
    print('%-52s %s %s' % (name, 'OK' if cond else 'FAIL', '' if cond else detail))
    if not cond:
        fail.append(name)


bad_raw = [u['idx'] for u in su if lines[u['line'] - 1] != u['raw']]
ck('riga grezza identica al file sorgente', not bad_raw, bad_raw)

db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
db.row_factory = sqlite3.Row
bad_db, bad_state = [], []
for u in su:
    row = db.execute('select english, kind, path, state from units where id = ?', (u['id'],)).fetchone()
    if row is None or row['english'] != u['english'] or row['kind'] != u['kind'] or row['path'] != u['path']:
        bad_db.append(u['idx'])
    elif row['state'] != 'PENDING':
        bad_state.append((u['idx'], row['state']))
ck('english/kind/path identici al DB', not bad_db, bad_db)
ck('state = PENDING per tutte le unita', not bad_state, bad_state)

ids = [u['id'] for u in tu]
ck('id univoci in translation.json', len(ids) == len(set(ids)))
ck('ordine delle unita = ordine del sorgente', [u['idx'] for u in tu] == [u['idx'] for u in su])

first, last = tu[0]['line'], tu[-1]['line']
ck('unita: %d righe %d - %d' % (len(tu), first, last), len(tu) == 1611 and (first, last) == (1811, 6428))

nxt = db.execute('select line, context from units where path = ? and line > ? order by line limit 1',
                 (PATH, last)).fetchone()
ck('unita successiva nel file', nxt is not None and nxt['line'] == 6432
   and nxt['context'] == 'mission:Care Package to South 1', dict(nxt) if nxt else None)

tot = db.execute('select count(*) from units where path = ?', (PATH,)).fetchone()[0]
resto = db.execute('select count(*), sum(length(english)-length(replace(english," ",""))+1) '
                   'from units where path = ? and line > ?', (PATH, last)).fetchone()
print('%s: %d unita totali · dopo la riga %d: %d (%s parole)'
      % (PATH, tot, last, resto[0], resto[1]))

tot_staging, lotti, spans = 0, [], []
for name in sorted(os.listdir(os.path.join(L10N, 'staging', 'editorial'))):
    f = os.path.join(L10N, 'staging', 'editorial', name, 'translation.json')
    if not os.path.exists(f):
        continue
    d = json.load(open(f, encoding='utf-8'))['units']
    if d and d[0]['path'] == PATH:
        tot_staging += len(d)
        lotti.append((name.split('_')[0], len(d)))
        spans.append((d[0]['line'], d[-1]['line'], name.split('_')[0]))
print('lotti su questo file:', lotti)
ck('copertura del file %d / %d' % (tot_staging, tot), tot_staging <= tot, tot_staging)

# Nessun totale cablato: 501+1611 (L19) o 501+1611+1676 (L20) invecchiano a ogni lotto nuovo e
# facevano fallire il verify di un lotto chiuso appena se ne aggiungeva uno. L'invariante vero e'
# che i lotti sullo stesso file non si sovrappongano e restino dentro il file.
spans.sort()
overlap = [(a[2], b[2]) for a, b in zip(spans, spans[1:]) if b[0] <= a[1]]
ck('nessuna sovrapposizione fra lotti sullo stesso file', not overlap, overlap)
out_of_file = [x for x in spans if not (1 <= x[0] <= x[1] <= len(lines))]
ck('intervalli dei lotti dentro il file', not out_of_file, out_of_file)

labels = [u for u in su if u['kind'] == 'UI_LABEL']
trans_by_idx = {u['idx']: u for u in tu}
bad_lab = [u['idx'] for u in labels if trans_by_idx[u['idx']]['italian'] != u['english']]
ck('le %d label sono identiche al sorgente' % len(labels), len(labels) == 39 and not bad_lab, bad_lab)
kinds_lab = [trans_by_idx[u['idx']]['kind'] for u in labels]
ck('kind UI_LABEL coerente in translation.json', set(kinds_lab) == {'UI_LABEL'}, set(kinds_lab))

multi = {}
for u in tu:
    multi.setdefault(u['line'], []).append(u['idx'])
ck('nessuna riga con piu\' unita (in L19 non ci sono `log` ne\' `phrase`)',
   all(len(v) == 1 for v in multi.values()), [k for k, v in multi.items() if len(v) > 1])

TAGS = re.compile(r'<[^<>]+>')
tok_en = sum(len(TAGS.findall(u['english'])) for u in su)
tok_it = sum(len(TAGS.findall(u['italian'])) for u in tu)
ck('token <...> totali %d = %d' % (tok_it, tok_en), tok_it == tok_en)
tab_en = sum(u['english'].count('\t') for u in su)
tab_it = sum(u['italian'].count('\t') for u in tu)
ck('tab totali %d = %d' % (tab_it, tab_en), tab_it == tab_en)
quo_en = sum(u['english'].count('"') for u in su)
quo_it = sum(u['italian'].count('"') for u in tu)
ck('virgolette totali %d = %d' % (quo_it, quo_en), quo_it == quo_en)

ck('parole: nessuna unita con italiano vuoto',
   all(u['italian'].strip() for u in tu))

print()
print('FAIL:', len(fail), '·', 'verify L19 superato' if not fail else 'verify L19 fallito')
raise SystemExit(0 if not fail else 1)
