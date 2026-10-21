"""verify.py — L20 (quinto lotto di data/human/human missions.txt)

Controlli indipendenti da check.py: non importa nulla da check.py e non riusa
le sue funzioni. Ogni controllo legge la fonte primaria che gli compete
(file sorgente, state.db, source.json, translation.json, parti).

  1. la riga grezza di ogni unita' coincide con quella del file sorgente
  2. english / kind / path coincidono con state.db, e lo stato e' PENDING
  3. nessuna unita' del lotto risulta APPROVED nel database
  4. id univoci e ordine delle unita' = ordine del sorgente
  5. collocazione del lotto nel file, unita' successiva, copertura del file
  6. le 71 `label` sono identiche al sorgente e il loro kind e' UI_LABEL
  7. token <...>, tab, virgolette: totali del lotto uguali al sorgente
  8. nessuna unita' con italiano vuoto; nessun carattere non latino
  9. rapporto lunghezze: nessun valore nullo, estremi documentati
 10. le parti su disco ricostruiscono esattamente translation.json
"""
import glob
import hashlib
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
    print('%-58s %s %s' % (name, 'OK' if cond else 'FAIL', '' if cond else detail))
    if not cond:
        fail.append(name)


# 1 --------------------------------------------------------------- riga grezza
bad_raw = [u['idx'] for u in su if lines[u['line'] - 1] != u['raw']]
ck('riga grezza identica al file sorgente', not bad_raw, bad_raw[:10])

# 2-3 ----------------------------------------------------- confronto con il DB
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
db.row_factory = sqlite3.Row
bad_db, bad_state, approved = [], [], []
for u in su:
    row = db.execute('select english, kind, path, state from units where id = ?',
                     (u['id'],)).fetchone()
    if row is None or row['english'] != u['english'] or row['kind'] != u['kind'] \
            or row['path'] != u['path']:
        bad_db.append(u['idx'])
    elif row['state'] == 'APPROVED':
        approved.append(u['idx'])
    elif row['state'] != 'PENDING':
        bad_state.append((u['idx'], row['state']))
ck('english/kind/path identici al DB', not bad_db, bad_db[:10])
ck('state = PENDING per tutte le unita', not bad_state, bad_state[:10])
ck('nessuna unita del lotto e APPROVED nel DB', not approved, approved[:10])

# 4 --------------------------------------------------------- ordine e univocita
ids = [u['id'] for u in tu]
ck('id univoci in translation.json', len(ids) == len(set(ids)))
ck('ordine delle unita = ordine del sorgente',
   [u['idx'] for u in tu] == [u['idx'] for u in su])
ck('stesse unita in source.json e translation.json',
   [u['idx'] for u in tu] == [u['idx'] for u in su] and len(tu) == len(su))

# 5 ----------------------------------------------------------- collocazione
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: %d righe %d - %d' % (len(tu), first, last),
   len(tu) == 1676 and (first, last) == (6432, 10806), (len(tu), first, last))

nxt = db.execute('select line, context from units where path = ? and line > ? '
                 'order by line limit 1', (PATH, last)).fetchone()
ck('unita successiva nel file = riga 10812 Stone to Ice Queen',
   nxt is not None and nxt['line'] == 10812
   and nxt['context'] == 'mission:Stone to Ice Queen', dict(nxt) if nxt else None)

prev = db.execute('select line, context from units where path = ? and line < ? '
                  'order by line desc limit 1', (PATH, first)).fetchone()
ck('unita precedente = riga 6428 (confine L19)',
   prev is not None and prev['line'] == 6428, dict(prev) if prev else None)

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

# Nessun totale cablato: 501+1611+1676 invecchia al lotto successivo e faceva fallire il verify
# di un lotto chiuso appena se ne aggiungeva uno. L'invariante vero e' che i lotti sullo stesso
# file non si sovrappongano e restino dentro il file.
spans.sort()
overlap = [(a[2], b[2]) for a, b in zip(spans, spans[1:]) if b[0] <= a[1]]
ck('nessuna sovrapposizione fra lotti sullo stesso file', not overlap, overlap)
out_of_file = [x for x in spans if not (1 <= x[0] <= x[1] <= len(lines))]
ck('intervalli dei lotti dentro il file', not out_of_file, out_of_file)

# 6 ---------------------------------------------------------------- etichette
labels = [u for u in su if u['kind'] == 'UI_LABEL']
trans_by_idx = {u['idx']: u for u in tu}
bad_lab = [u['idx'] for u in labels if trans_by_idx[u['idx']]['italian'] != u['english']]
ck('le %d label sono identiche al sorgente' % len(labels), len(labels) == 71 and not bad_lab,
   bad_lab[:10])
kinds_lab = {trans_by_idx[u['idx']]['kind'] for u in labels}
ck('kind UI_LABEL coerente in translation.json', kinds_lab == {'UI_LABEL'}, kinds_lab)

# 7 ------------------------------------------------------------------- token
TAGS = re.compile(r'<[^<>]+>')
tok_en = sum(len(TAGS.findall(u['english'])) for u in su)
tok_it = sum(len(TAGS.findall(u['italian'])) for u in tu)
ck('token <...> totali %d = %d' % (tok_it, tok_en), tok_it == tok_en)
for ch, nome in (('\t', 'tab'), ('"', 'virgolette')):
    a = sum(u['english'].count(ch) for u in su)
    b = sum(u['italian'].count(ch) for u in tu)
    ck('%s totali %d = %d' % (nome, b, a), a == b)

# 8 --------------------------------------------------- vuoti e caratteri
ck('nessuna unita con italiano vuoto', all(u['italian'].strip() for u in tu))
NONLAT = re.compile(r'[^\x00-\x7F\u00C0-\u024F\u2018\u2019\u201C\u201D\u2013\u2014\u2026]')
sus = [(u['idx'], NONLAT.findall(u['italian'])[:3]) for u in tu
       if NONLAT.search(u['italian'])]
ck('nessun carattere non latino sospetto', not sus, sus[:10])

# 9 ------------------------------------------------------------- rapporti
bad_ratio = [u['idx'] for u in tu if u['ratio'] is None]
ck('rapporto lunghezze definito per tutte le unita', not bad_ratio, bad_ratio[:10])
rs = [u['ratio'] for u in tu if u['ratio'] is not None]
lt05 = sorted([(u['ratio'], u['idx']) for u in tu if u['ratio'] is not None and u['ratio'] < 0.5])
gt20 = sorted([(u['ratio'], u['idx']) for u in tu if u['ratio'] is not None and u['ratio'] > 2.0])
print('rapporto IT/EN: min %.2f max %.2f · sotto 0,50: %d · sopra 2,00: %d'
      % (min(rs), max(rs), len(lt05), len(gt20)))

# 10 ------------------------------------------------- parti = translation.json
merged = {}
for f in sorted(glob.glob(os.path.join(HERE, 'parts', 'part*.json'))):
    for k, v in json.load(open(f, encoding='utf-8')).items():
        merged[int(k)] = v
same = merged == {u['idx']: u['italian'] for u in tu}
ck('le parti su disco ricostruiscono translation.json', same)

h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
en = sum(len(u['english'].split()) for u in tu)
ita = sum(len(u['italian'].split()) for u in tu)
print('parole EN %d -> IT %d · traduzione sha256[:16] %s' % (en, ita, h[:16]))

print()
print('FAIL:', len(fail), '·', 'verify L20 superato' if not fail else 'verify L20 fallito')
raise SystemExit(0 if not fail else 1)
