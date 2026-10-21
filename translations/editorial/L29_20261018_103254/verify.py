"""verify.py — L29 (data/hai/hai missions.txt, righe 23-2696, 823 unita')

L29 e' l'unico lotto di questo file: copre l'intero `hai missions.txt` dalla prima unita'
all'ultima. La copertura TOTALE del file e' quindi un invariante legittimo, come in L26 e L28.

Controlli indipendenti da check.py, senza riusare la sua logica:

  1. la riga grezza di ogni unita' coincide con quella del file sorgente
  2. english / kind / path coincidono con state.db, e lo stato e' PENDING
  3. nessuna unita' del lotto risulta APPROVED
  4. id univoci e ordine = ordine del sorgente
  5. collocazione: 823 unita', righe 23-2696 (prima e ultima unita' del file)
  6. nessuna unita' del file prima della 23 o dopo la 2696: il lotto e' tutto il file
  7. copertura totale del file 823/823, da un solo lotto
  8. distribuzione dei kind misurata (non dedotta): 685 MISSION_TEXT, 41 DESCRIPTION,
     35 VALUE, 34 DIALOG, 15 UI_LABEL, 13 LOGBOOK
  9. NT: le 15 `UI_LABEL` + 2 riferimenti di dato (455, 599) sono identici al sorgente
 10. nessuna `CONVERSATION` in questo file
 11. token: parita' esatta su tutte le unita' (nessun pronome-token nel sorgente)
 12. tab, virgolette, backtick: totali del lotto uguali al sorgente
 13. nessuna unita' con italiano vuoto; nessun carattere non latino sospetto
 14. nessun trattino lungo (U+2014) ne' en-dash
 15. rapporto lunghezze definito; estremi stampati
 16. le parti su disco ricostruiscono translation.json
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
PATH = 'data/hai/hai missions.txt'
SRC = os.path.join(ROOT, 'endless-sky', *PATH.split('/'))

source = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
trans = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))
su, tu = source['units'], trans['units']
lines = open(SRC, encoding='utf-8').read().split('\n')

# 15 `UI_LABEL` (bersagli di `goto`) + 2 riferimenti di dato, non prosa:
#   455 `outfit/crystal pendant` (comando `scene`)
#   599 `thumbnail/hai pond strider`
NT = {77, 84, 86, 365, 455, 465, 469, 473, 478, 481, 483, 599, 659, 741, 796, 800, 808}
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
   len(tu) == 823 and (first, last) == (23, 2696), (len(tu), first, last))

maxline = db.execute('select max(line) from units where path = ?', (PATH,)).fetchone()[0]
before = db.execute('select count(*) from units where path = ? and line < ?',
                    (PATH, first)).fetchone()[0]
after = db.execute('select count(*) from units where path = ? and line > ?',
                   (PATH, last)).fetchone()[0]
ck('lotto inizia alla riga 23: 0 unita prima, 0 dopo (fine file)',
   before == 0 and after == 0 and maxline == 2696, (before, after, maxline))

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
sovrapposti = sum(len(a & b) for i, a in enumerate(ids_lotti) for b in ids_lotti[i + 1:])
ck('copertura del file %d / %d (file completo)' % (tot_staging, tot),
   tot == 823 and tot_staging == tot, (tot_staging, tot))
ck('un solo lotto, nessuna unita duplicata', len(lotti) == 1 and sovrapposti == 0,
   (lotti, sovrapposti))

kinds = collections.Counter(u['kind'] for u in su)
atteso = {'MISSION_TEXT': 685, 'DESCRIPTION': 41, 'VALUE': 35,
          'DIALOG': 34, 'UI_LABEL': 15, 'LOGBOOK': 13}
ck('distribuzione dei kind come misurata', dict(kinds) == atteso, dict(kinds))

by_idx = {u['idx']: u for u in tu}
bad_nt = [i for i in NT if by_idx[i]['italian'] != by_idx[i]['english']]
missing_nt = [i for i in NT if i not in by_idx]
ck('NT (%d unita) identiche al sorgente' % len(NT), not bad_nt and not missing_nt,
   (bad_nt, missing_nt))

conv = [u for u in tu if u['kind'] == 'CONVERSATION']
ck('nessuna CONVERSATION in questo file', len(conv) == 0, len(conv))

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
print('FAIL:', len(fail), '·', 'verify L29 superato' if not fail else 'verify L29 fallito')
raise SystemExit(0 if not fail else 1)
