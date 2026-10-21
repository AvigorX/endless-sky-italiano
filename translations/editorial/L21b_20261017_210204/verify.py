"""verify.py — L21b (data/human/intro missions.txt, 637 unita')

Controlli indipendenti da check.py.

  1. la riga grezza di ogni unita' coincide con quella del file sorgente
  2. english / kind / path coincidono con state.db, e lo stato e' PENDING
  3. nessuna unita' del lotto risulta APPROVED
  4. id univoci e ordine = ordine del sorgente
  5. collocazione: 637 unita', righe 23-2319 (file completo)
  6. nessuna unita' prima della riga 23 ne' dopo la 2319: il file finisce qui
  7. copertura dello staging su questo file = 637 unita'
  8. le unita' non traducibili (1 `label` dentro conversation) sono identiche
  9. token: parita' esatta tranne i pronomi dichiarati in TOKEN_EXC, e solo quelli
 10. tab, virgolette, backtick: totali del lotto uguali al sorgente
 11. nessuna unita' con italiano vuoto; nessun carattere non latino
 12. rapporto lunghezze definito; estremi stampati
 13. le parti su disco ricostruiscono translation.json
"""
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
PATH = 'data/human/intro missions.txt'
SRC = os.path.join(ROOT, 'endless-sky', *PATH.split('/'))

source = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
trans = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))
su, tu = source['units'], trans['units']
lines = open(SRC, encoding='utf-8').read().split('\n')

NT = {113}
TOKEN_EXC = {54, 84, 85, 145, 148}
PRON = re.compile(r"<(?:they've|they're|they are|they|their|them)>")
TAGS = re.compile(r'<[^<>]+>')

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
ck('ordine delle unita = ordine del sorgente', [u['idx'] for u in tu] == [u['idx'] for u in su])
ck('stesse unita in source.json e translation.json',
   len(tu) == len(su) and [u['idx'] for u in tu] == [u['idx'] for u in su])

first, last = tu[0]['line'], tu[-1]['line']
ck('unita: %d righe %d - %d' % (len(tu), first, last),
   len(tu) == 637 and (first, last) == (23, 2319), (len(tu), first, last))

minline = db.execute('select min(line) from units where path = ?', (PATH,)).fetchone()[0]
maxline = db.execute('select max(line) from units where path = ?', (PATH,)).fetchone()[0]
before = db.execute('select count(*) from units where path = ? and line < ?', (PATH, first)).fetchone()[0]
after = db.execute('select count(*) from units where path = ? and line > ?', (PATH, last)).fetchone()[0]
ck('il file inizia alla riga 23 e finisce alla 2319',
   minline == 23 and maxline == 2319 and before == 0 and after == 0,
   (minline, maxline, before, after))

tot = db.execute('select count(*) from units where path = ?', (PATH,)).fetchone()[0]
tot_staging, lotti = 0, []
for name in sorted(os.listdir(os.path.join(L10N, 'staging', 'editorial'))):
    f = os.path.join(L10N, 'staging', 'editorial', name, 'translation.json')
    if not os.path.exists(f):
        continue
    d = json.load(open(f, encoding='utf-8'))['units']
    if d and d[0]['path'] == PATH:
        tot_staging += len(d)
        lotti.append((name.split('_')[0], len(d)))
print('lotti su questo file:', lotti)
ck('copertura del file %d / %d (file completo)' % (tot_staging, tot), tot_staging == tot,
   (tot_staging, tot))

by_idx = {u['idx']: u for u in tu}
bad_nt = [i for i in NT if by_idx[i]['italian'] != by_idx[i]['english']]
ck('le %d unita non traducibili sono identiche' % len(NT), len(NT) == 1 and not bad_nt, bad_nt)

# token: parita' esatta, tranne i pronomi dichiarati e solo quelli
diff = [u['idx'] for u in tu
        if collections.Counter(TAGS.findall(u['english'])) != collections.Counter(TAGS.findall(u['italian']))]
ck('unita con token diversi = solo le eccezioni dichiarate',
   set(diff) == TOKEN_EXC, (sorted(set(diff)), sorted(TOKEN_EXC)))
bad_exc = []
for i in TOKEN_EXC:
    en = collections.Counter(TAGS.findall(by_idx[i]['english']))
    it = collections.Counter(TAGS.findall(by_idx[i]['italian']))
    if (en - it) != collections.Counter(PRON.findall(by_idx[i]['english'])) or (it - en):
        bad_exc.append(i)
ck('nelle eccezioni si perdono solo i pronomi', not bad_exc, bad_exc)
ck('token residui %d' % sum(len(TAGS.findall(u['italian'])) for u in tu),
   sum(len(TAGS.findall(u['english'])) for u in su)
   - sum(len(TAGS.findall(u['italian'])) for u in tu) == 7,
   sum(len(TAGS.findall(u['english'])) for u in su)
   - sum(len(TAGS.findall(u['italian'])) for u in tu))

for ch, nome in (('\t', 'tab'), ('"', 'virgolette'), ('`', 'backtick')):
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
en_w = sum(len(u['english'].split()) for u in tu)
it_w = sum(len(u['italian'].split()) for u in tu)
print('parole EN %d -> IT %d · traduzione sha256[:16] %s' % (en_w, it_w, h[:16]))

print()
print('FAIL:', len(fail), '·', 'verify L21b superato' if not fail else 'verify L21b fallito')
raise SystemExit(0 if not fail else 1)
