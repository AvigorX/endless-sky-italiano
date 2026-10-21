"""verify.py — L21a (coda di data/human/human missions.txt, 465 unita')

Controlli indipendenti da check.py: non importa nulla da check.py e non riusa le sue funzioni.

  1. la riga grezza di ogni unita' coincide con quella del file sorgente
  2. english / kind / path coincidono con state.db, e lo stato e' PENDING
  3. nessuna unita' del lotto risulta APPROVED nel database
  4. id univoci e ordine = ordine del sorgente
  5. collocazione: 465 unita', righe 10812-11777 (fine file)
  6. dopo la riga 11777 non c'e' nessuna unita': il file finisce qui
  7. l'unita' precedente e' la 10806 (ultimo confine di L20)
  8. copertura dello staging su questo file = 4.253 unita' (file completo)
  9. le 19 unita' non traducibili (12 `label` + 7 `label` dentro conversation) sono identiche
 10. token <...>, tab, virgolette: totali del lotto uguali al sorgente
 11. nessuna unita' con italiano vuoto; nessun carattere non latino
 12. rapporto lunghezze definito; estremi stampati
 13. le parti su disco ricostruiscono translation.json
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


bad_raw = [u['idx'] for u in su if lines[u['line'] - 1] != u['raw']]
ck('riga grezza identica al file sorgente', not bad_raw, bad_raw[:10])

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

ids = [u['id'] for u in tu]
ck('id univoci in translation.json', len(ids) == len(set(ids)))
ck('ordine delle unita = ordine del sorgente',
   [u['idx'] for u in tu] == [u['idx'] for u in su])
ck('stesse unita in source.json e translation.json',
   len(tu) == len(su) and [u['idx'] for u in tu] == [u['idx'] for u in su])

first, last = tu[0]['line'], tu[-1]['line']
ck('unita: %d righe %d - %d' % (len(tu), first, last),
   len(tu) == 465 and (first, last) == (10812, 11777), (len(tu), first, last))

maxline = db.execute('select max(line) from units where path = ?', (PATH,)).fetchone()[0]
after = db.execute('select count(*) from units where path = ? and line > ?', (PATH, last)).fetchone()[0]
ck('il file finisce alla riga 11777 (nessuna unita dopo)',
   maxline == 11777 and after == 0, (maxline, after))

prev = db.execute('select line, context from units where path = ? and line < ? '
                  'order by line desc limit 1', (PATH, first)).fetchone()
ck('unita precedente = riga 10806 (confine L20)',
   prev is not None and prev['line'] == 10806
   and prev['context'] == 'mission:Stone to Hope', dict(prev) if prev else None)

tot = db.execute('select count(*) from units where path = ?', (PATH,)).fetchone()[0]
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
ck('copertura del file %d / %d (file completo)' % (tot_staging, tot),
   tot_staging == tot, (tot_staging, tot))
spans.sort()
overlap = [(a[2], b[2]) for a, b in zip(spans, spans[1:]) if b[0] <= a[1]]
ck('nessuna sovrapposizione fra lotti sullo stesso file', not overlap, overlap)
out_of_file = [x for x in spans if not (1 <= x[0] <= x[1] <= len(lines))]
ck('intervalli dei lotti dentro il file', not out_of_file, out_of_file)

# non traducibili: 12 `label` di missione + 7 `label` dentro blocchi conversation
NT = sorted([u['idx'] for u in su if u['kind'] == 'UI_LABEL'] +
            [u['idx'] for u in su if u['kind'] == 'CONVERSATION' and u['delimiter'] == 'quote'])
trans_by_idx = {u['idx']: u for u in tu}
bad_nt = [i for i in NT if trans_by_idx[i]['italian'] != trans_by_idx[i]['english']]
ck('le %d unita non traducibili sono identiche' % len(NT),
   len(NT) == 19 and not bad_nt, (len(NT), bad_nt[:10]))

TAGS = re.compile(r'<[^<>]+>')
tok_en = sum(len(TAGS.findall(u['english'])) for u in su)
tok_it = sum(len(TAGS.findall(u['italian'])) for u in tu)
ck('token <...> totali %d = %d' % (tok_it, tok_en), tok_it == tok_en)
for ch, nome in (('\t', 'tab'), ('"', 'virgolette')):
    a = sum(u['english'].count(ch) for u in su)
    b = sum(u['italian'].count(ch) for u in tu)
    ck('%s totali %d = %d' % (nome, b, a), a == b)

ck('nessuna unita con italiano vuoto', all(u['italian'].strip() for u in tu))
NONLAT = re.compile(r'[^\x00-\x7F\u00C0-\u024F\u2018\u2019\u201C\u201D\u2013\u2014\u2026]')
sus = [(u['idx'], NONLAT.findall(u['italian'])[:3]) for u in tu if NONLAT.search(u['italian'])]
ck('nessun carattere non latino sospetto', not sus, sus[:10])

bad_ratio = [u['idx'] for u in tu if u['ratio'] is None]
ck('rapporto lunghezze definito per tutte le unita', not bad_ratio, bad_ratio[:10])
rs = [u['ratio'] for u in tu if u['ratio'] is not None]
print('rapporto IT/EN: min %.2f max %.2f' % (min(rs), max(rs)))

merged = {}
for f in sorted(glob.glob(os.path.join(HERE, 'parts', 'part*.json'))):
    for k, v in json.load(open(f, encoding='utf-8')).items():
        merged[int(k)] = v
ck('le parti su disco ricostruiscono translation.json',
   merged == {u['idx']: u['italian'] for u in tu})

h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
en = sum(len(u['english'].split()) for u in tu)
ita = sum(len(u['italian'].split()) for u in tu)
print('parole EN %d -> IT %d · traduzione sha256[:16] %s' % (en, ita, h[:16]))

print()
print('FAIL:', len(fail), '·', 'verify L21a superato' if not fail else 'verify L21a fallito')
raise SystemExit(0 if not fail else 1)
