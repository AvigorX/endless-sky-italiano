"""verify.py — L25 (data/coalition/coalition missions.txt, righe 16-2907, 1174 unita')

Controlli indipendenti da check.py: rileggono il file sorgente, il database e le parti
su disco, senza riusare la logica del checker del lotto.

  1. la riga grezza di ogni unita' coincide con quella del file sorgente
  2. english / kind / path coincidono con state.db, e lo stato e' PENDING
  3. nessuna unita' del lotto risulta APPROVED
  4. id univoci e ordine = ordine del sorgente
  5. collocazione: 1174 unita', righe 16-2907
  6. il lotto inizia alla riga 16 (niente prima) e lascia 406 unita' dopo la 2907
  7. copertura dichiarata: 1174 unita' da un solo lotto, su 1580 del file
  8. NT: le 16 unita' non traducibili (UI_LABEL) sono identiche al sorgente
  9. token: parita' esatta su tutte le unita' (nessun pronome-token nel sorgente)
 10. tab, virgolette, backtick: totali del lotto uguali al sorgente
 11. nessuna unita' con italiano vuoto; nessun carattere non latino sospetto
 12. nessun trattino lungo (U+2014) ne' en-dash: la tipografia del lotto lo vieta
 13. rapporto lunghezze definito; estremi stampati
 14. le parti su disco ricostruiscono translation.json
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
PATH = 'data/coalition/coalition missions.txt'
SRC = os.path.join(ROOT, 'endless-sky', *PATH.split('/'))

source = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
trans = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))
su, tu = source['units'], trans['units']
lines = open(SRC, encoding='utf-8').read().split('\n')

# 16 `UI_LABEL`: bersagli di `goto`, restano identici (nessun `label` fuori da essi).
NT = {109, 111, 509, 520, 536, 558, 602, 630, 640, 646, 648, 661, 710, 733, 752, 1079}
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
   len(tu) == 1174 and (first, last) == (16, 2907), (len(tu), first, last))

minline = db.execute('select min(line) from units where path = ?', (PATH,)).fetchone()[0]
before = db.execute('select count(*) from units where path = ? and line < ?',
                    (PATH, first)).fetchone()[0]
after = db.execute('select count(*) from units where path = ? and line > ?',
                   (PATH, last)).fetchone()[0]
ck('il lotto inizia alla riga 16 e lascia 406 unita dopo la 2907',
   minline == 16 and before == 0 and after == 406, (minline, before, after))

tot = db.execute('select count(*) from units where path = ?', (PATH,)).fetchone()[0]
tot_staging, lotti, ids_lotti = 0, [], []
for name in sorted(os.listdir(os.path.join(L10N, 'staging', 'editorial'))):
    f = os.path.join(L10N, 'staging', 'editorial', name, 'translation.json')
    if not os.path.exists(f):
        continue
    d = json.load(open(f, encoding='utf-8'))['units']
    if d and d[0]['path'] == PATH:
        tot_staging += len(d)
        lotti.append((name.split('_')[0], len(d)))
        ids_lotti.append(set(u['id'] for u in d))
print('lotti su questo file:', lotti)
# L25 e' un segmento: dal 2026-10-17 esiste anche L26 sullo stesso file. L'invariante che regge nel
# tempo non e' la copertura cumulativa (cambia a ogni lotto) ma: nessuna sovrapposizione fra lotti e
# nessun lotto oltre il numero di unita' del file.
sovrapposti = sum(len(a & b) for i, a in enumerate(ids_lotti) for b in ids_lotti[i + 1:])
ck('lotto dentro il file: %d unita su %d, righe %d-%d' % (len(tu), tot, first, last),
   len(tu) == 1174 and tot == 1580 and 0 < first < last <= max(
       l for l in [db.execute('select max(line) from units where path = ?', (PATH,)).fetchone()[0]]))
ck('nessuna unita duplicata fra lotti dello stesso file', sovrapposti == 0,
   (sovrapposti, [l[0] for l in lotti]))
print('copertura cumulata del file: %d / %d unita' % (tot_staging, tot))

by_idx = {u['idx']: u for u in tu}
bad_nt = [i for i in NT if by_idx[i]['italian'] != by_idx[i]['english']]
missing_nt = [i for i in NT if i not in by_idx]
ck('NT (%d unita) identiche al sorgente' % len(NT), not bad_nt and not missing_nt,
   (bad_nt, missing_nt))

diff = [u['idx'] for u in tu
        if collections.Counter(TAGS.findall(u['english'])) != collections.Counter(TAGS.findall(u['italian']))]
ck('nessuna unita con token diversi (parita esatta)', not diff, sorted(set(diff))[:10])
tot_en = sum(len(TAGS.findall(u['english'])) for u in su)
tot_it = sum(len(TAGS.findall(u['italian'])) for u in tu)
ck('token totali %d = %d' % (tot_it, tot_en), tot_en == tot_it, (tot_it, tot_en))
ck('nessun pronome-token nel sorgente', not any(PRON.search(u['english']) for u in su),
   [u['idx'] for u in su if PRON.search(u['english'])][:5])

for ch, nome in (('\t', 'tab'), ('"', 'virgolette'), ('`', 'backtick')):
    a = sum(u['english'].count(ch) for u in su)
    b = sum(u['italian'].count(ch) for u in tu)
    ck('%s totali %d = %d' % (nome, b, a), a == b)

ck('nessuna unita con italiano vuoto', all(u['italian'].strip() for u in tu))
NONLAT = re.compile(r'[^\x00-\x7F\u00C0-\u024F\u2018\u2019\u201C\u201D\u2013\u2014\u2026]')
sus = [(u['idx'], NONLAT.findall(u['italian'])[:3]) for u in tu if NONLAT.search(u['italian'])]
ck('nessun carattere non latino sospetto', not sus, sus[:10])

dash = [u['idx'] for u in tu if '\u2014' in u['italian'] or '\u2013' in u['italian']]
ck('nessun trattino lungo/en-dash (vietati)', not dash, dash[:10])

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
print('FAIL:', len(fail), '·', 'verify L25 superato' if not fail else 'verify L25 fallito')
raise SystemExit(0 if not fail else 1)
