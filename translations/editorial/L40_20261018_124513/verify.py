"""verify.py — L40 (data/human/free worlds side plots.txt, 211 unita', righe 18-888, fine file)

L40 chiude il file `free worlds side plots.txt`: copre dalla prima unita' all'ultima, quindi la
copertura TOTALE del file e' un invariante legittimo (come in L28-L39).

Il file **inizia alla riga 18**, non 16. La coppia attesa e' (18, 888), misurata all'export.

Controlli indipendenti da check.py, senza riusare la sua logica:

  1. la riga grezza di ogni unita' coincide con quella del file sorgente
  2. english / kind / path coincidono con state.db, e lo stato e' PENDING
  3. nessuna unita' del lotto risulta APPROVED
  4. id univoci e ordine = ordine del sorgente
  5. collocazione: 211 unita', righe 18-888
  6. nessuna unita' del file prima della 18 o dopo la 888
  7. copertura totale del file 211/211, da un solo lotto
  8. distribuzione dei kind misurata: 154 MISSION_TEXT, 19 DIALOG, 15 VALUE, 15 DESCRIPTION,
     7 LOGBOOK, 1 UI_LABEL, 0 CONVERSATION
  9. `NT` = {80}: la `label` di salto `brower death` identica; le UI_LABEL del file sono esattamente
     quella, e il controllo lo verifica
 10. **CONVERSATION 0**: asserzione di assenza (in L39 erano 34), cosi' un cambio di inventario non
     passa inosservato
 11. **quadre**: 0 unita' con `[` o `]` nel sorgente e 0 nell'italiano
 12. token: parita' esatta su tutte le unita'
 13. tab, virgolette, backtick: totali uguali al sorgente
 14. unita' con numero dispari di virgolette: stesso insieme di idx del sorgente (56, 202)
 15. nessuna unita' con italiano vuoto; nessun carattere non latino sospetto
 16. nessun trattino lungo (U+2014) ne' en-dash
 17. rapporto lunghezze definito; estremi stampati
 18. le parti su disco ricostruiscono translation.json

Nota di inventario (dichiarata): 7 righe `log` producono 7 unita' `LOGBOOK` (1:1).
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
PATH = 'data/human/free worlds side plots.txt'
SRC = os.path.join(ROOT, 'endless-sky', *PATH.split('/'))

source = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
trans = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))
su, tu = source['units'], trans['units']
lines = open(SRC, encoding='utf-8').read().split('\n')

# 80 `brower death` (label di salto)
NT = {80}
PRON = re.compile(r"<(?:they've|they're|they are|they|their|them)>")
TAGS = re.compile(r'<[^<>]+>')
BR = re.compile(r'\[[^\]]*\]')

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
   len(tu) == 211 and (first, last) == (18, 888), (len(tu), first, last))

maxline = db.execute('select max(line) from units where path = ?', (PATH,)).fetchone()[0]
before = db.execute('select count(*) from units where path = ? and line < ?',
                    (PATH, first)).fetchone()[0]
after = db.execute('select count(*) from units where path = ? and line > ?',
                   (PATH, last)).fetchone()[0]
ck('lotto inizia alla riga 16: 0 unita prima, 0 dopo (fine file)',
   before == 0 and after == 0 and maxline == 888, (before, after, maxline))

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
   tot == 211 and tot_staging == tot, (tot_staging, tot))
ck('un solo lotto, nessuna unita duplicata', len(lotti) == 1 and sovrapposti == 0,
   (lotti, sovrapposti))

kinds = collections.Counter(u['kind'] for u in su)
atteso = {'MISSION_TEXT': 154, 'DIALOG': 19, 'VALUE': 15, 'DESCRIPTION': 15, 'LOGBOOK': 7,
          'UI_LABEL': 1}
ck('distribuzione dei kind come misurata', dict(kinds) == {k: v for k, v in atteso.items() if v}, dict(kinds))

by_idx = {u['idx']: u for u in tu}
bad_nt = [i for i in NT if by_idx[i]['italian'] != by_idx[i]['english']]
missing_nt = [i for i in NT if i not in by_idx]
ck('NT (%d unita) identiche al sorgente' % len(NT), not bad_nt and not missing_nt,
   (bad_nt, missing_nt))
ui = sorted(u['idx'] for u in tu if u['kind'] == 'UI_LABEL')
ck('UI_LABEL: la sola label di salto 80', ui == [80], ui)
conv = [u['idx'] for u in tu if u['kind'] == 'CONVERSATION']
ck('CONVERSATION: nessuna nel file', conv == [], conv)

# 10. quadre: struttura delle parentesi del motore, non alternative. Una sola unita' (143) ne ha una coppia.
br = [u['idx'] for u in su if '[' in u['english'] or ']' in u['english']]
ck('quadre: nessuna unita con [ o ] nel sorgente', br == [], br[:5])
pair = [(u['idx'], u['english'].count('['), u['english'].count(']'),
         u['italian'].count('['), u['italian'].count(']')) for u in tu if '[' in u['italian'] or ']' in u['italian']]
ck("quadre: nessuna quadre nell'italiano", pair == [], pair)

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

odd_en = sorted(u['idx'] for u in su if u['english'].count('"') % 2)
odd_it = sorted(u['idx'] for u in tu if u['italian'].count('"') % 2)
print('unita con virgolette dispari:', len(odd_en))
ck('virgolette dispari: stessi idx del sorgente', odd_en == odd_it, (odd_en, odd_it))

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
print('FAIL:', len(fail), '·', 'verify L40 superato' if not fail else 'verify L40 fallito')
raise SystemExit(0 if not fail else 1)
