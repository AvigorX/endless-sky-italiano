"""verify.py — L42 (data/remnant/remnant 2 cognizance.txt, 572 unita', righe 16-1747, fine file)

L42 chiude il file `remnant 2 cognizance.txt`: copre dalla prima unita' all'ultima, quindi la
copertura TOTALE del file e' un invariante legittimo (come in L28-L41).

Controlli indipendenti da check.py, senza riusare la sua logica:

  1. la riga grezza di ogni unita' coincide con quella del file sorgente
  2. english / kind / path coincidono con state.db, e lo stato e' PENDING
  3. nessuna unita' del lotto risulta APPROVED
  4. id univoci e ordine = ordine del sorgente
  5. collocazione: 572 unita', righe 16-1747
  6. nessuna unita' del file prima della 16 o dopo la 1747
  7. copertura totale del file 572/572, da un solo lotto
  8. distribuzione dei kind misurata: 438 MISSION_TEXT, 39 VALUE, 39 DESCRIPTION, 19 DIALOG,
     35 UI_LABEL, 2 LOGBOOK
  9. `NT`: le **35** `UI_LABEL` (label di salto, bersagli di `goto`) identiche al sorgente,
     elencate una per una; nessuna altra unita' non traducibile
 10. `LOGBOOK`: 2 unita', entrambe tradotte e non vuote
 11. tab 342 e virgolette 909: parita' sui totali, e parita' **per unita'** su ogni unita'
 12. **11 virgolette dispari**: l'insieme degli idx coincide con quello del sorgente
     (32, 48, 50, 201, 240, 241, 245, 246, 342, 485, 558) - confronto di insiemi, non di totali
 13. token: parita' esatta su tutte le unita' (16 famiglie, 174 occorrenze)
 14. nessun backtick nell'italiano (il backtick e' nel `raw`, non nell'`english`)
 15. nessuna unita' con italiano vuoto; nessun carattere non latino sospetto
 16. nessun trattino lungo (U+2014) ne' en-dash
 17. rapporto lunghezze definito; estremi stampati
 18. le parti su disco ricostruiscono translation.json

Nota di inventario (dichiarata): il file ha 2 righe `log`. La prima (log a tre argomenti su Gavriil)
produce **una sola** unita', che e' il testo del diario: categoria e nome non sono inventariati
(lacuna di `tools/l10n.py`, protetto: si documenta e basta, non si ripara). La seconda e' un `log`
a due argomenti, il cui testo e' inventariato regolarmente.
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
PATH = 'data/remnant/remnant 2 cognizance.txt'
SRC = os.path.join(ROOT, 'endless-sky', *PATH.split('/'))

source = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
trans = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))
su, tu = source['units'], trans['units']
lines = open(SRC, encoding='utf-8').read().split('\n')

# le 35 label di salto: bersagli di `goto`, restano identiche
NT = set([49, 62, 110, 173, 175, 202, 204, 214, 218, 220, 232, 236, 255, 257, 266, 296, 320,
          331, 333, 343, 352, 369, 374, 394, 396, 398, 428, 445, 447, 465, 468, 479, 530, 565, 569])
ODD = (32, 48, 50, 201, 240, 241, 245, 246, 342, 485, 558)
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
ck('ordine delle unita = ordine del sorgente',
   [u['idx'] for u in tu] == [u['idx'] for u in su])
ck('stesse unita in source.json e translation.json',
   len(tu) == len(su) and [u['idx'] for u in tu] == [u['idx'] for u in su])

first, last = tu[0]['line'], tu[-1]['line']
ck('unita: %d righe %d - %d' % (len(tu), first, last),
   len(tu) == 572 and (first, last) == (16, 1747), (len(tu), first, last))

maxline = db.execute('select max(line) from units where path = ?', (PATH,)).fetchone()[0]
before = db.execute('select count(*) from units where path = ? and line < ?',
                    (PATH, first)).fetchone()[0]
after = db.execute('select count(*) from units where path = ? and line > ?',
                   (PATH, last)).fetchone()[0]
ck('lotto inizia alla riga 16: 0 unita prima, 0 dopo (fine file)',
   before == 0 and after == 0 and maxline == 1747, (before, after, maxline))

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
   tot == 572 and tot_staging == tot, (tot_staging, tot))
ck('un solo lotto, nessuna unita duplicata', len(lotti) == 1 and sovrapposti == 0,
   (lotti, sovrapposti))

kinds = collections.Counter(u['kind'] for u in su)
atteso = {'MISSION_TEXT': 438, 'VALUE': 39, 'DESCRIPTION': 39, 'DIALOG': 19,
          'UI_LABEL': 35, 'LOGBOOK': 2}
ck('distribuzione dei kind come misurata', dict(kinds) == atteso, dict(kinds))

by_idx = {u['idx']: u for u in tu}
bad_nt = [i for i in NT if by_idx[i]['italian'] != by_idx[i]['english']]
missing_nt = [i for i in NT if i not in by_idx]
ck('NT: %d label di salto identiche al sorgente' % len(NT),
   len(NT) == 35 and not bad_nt and not missing_nt, (bad_nt, missing_nt))
ui = sorted(u['idx'] for u in tu if u['kind'] == 'UI_LABEL')
ck('il file ha esattamente 35 UI_LABEL, tutte in NT', ui == sorted(NT), ui)
conv = [u['idx'] for u in tu if u['kind'] == 'CONVERSATION']
ck('CONVERSATION: nessuna nel file', conv == [], conv)
log = [u['idx'] for u in tu if u['kind'] == 'LOGBOOK']
ck('LOGBOOK: 2 unita, tutte tradotte',
   len(log) == 2 and all(u['italian'].strip() for u in tu if u['kind'] == 'LOGBOOK'), log)

# quadre: 0 unita' con parentesi quadre nel sorgente (asserzione di assenza, non controllo omesso)
br = [u['idx'] for u in su if '[' in u['english'] or ']' in u['english']]
ck('quadre: nessuna unita con [ o ] nel sorgente', br == [], br[:5])
pair = [u['idx'] for u in tu if '[' in u['italian'] or ']' in u['italian']]
ck("quadre: nessuna quadre nell'italiano", pair == [], pair)

diff = [u['idx'] for u in tu
        if collections.Counter(TAGS.findall(u['english'])) != collections.Counter(TAGS.findall(u['italian']))]
ck('nessuna unita con token diversi (parita esatta)', not diff, sorted(set(diff))[:10])
tot_en = sum(len(TAGS.findall(u['english'])) for u in su)
tot_it = sum(len(TAGS.findall(u['italian'])) for u in tu)
ck('token totali %d = %d' % (tot_it, tot_en), tot_en == tot_it, (tot_it, tot_en))

for ch, nome in (('\t', 'tab'), ('"', 'virgolette'), ('`', 'backtick')):
    a = sum(u['english'].count(ch) for u in su)
    b = sum(u['italian'].count(ch) for u in tu)
    ck('%s totali %d = %d' % (nome, b, a), a == b)

per_unit = [u['idx'] for u in tu if u['english'].count('\t') != u['italian'].count('\t')
            or u['english'].count('"') != u['italian'].count('"')]
ck('tab e virgolette: parita per unita (572 unita)', per_unit == [], per_unit[:10])
lead = [u['idx'] for u in tu if u['english'].startswith('\t') != u['italian'].startswith('\t')]
ck('tab iniziale presente dove il sorgente lo ha (342)', len([u for u in tu if u['italian'].startswith('\t')]) == 342 and lead == [],
   (len([u for u in tu if u['italian'].startswith('\t')]), lead[:5]))

odd_en = sorted(u['idx'] for u in su if u['english'].count('"') % 2)
odd_it = sorted(u['idx'] for u in tu if u['italian'].count('"') % 2)
print('unita con virgolette dispari:', len(odd_en), odd_en)
ck('virgolette dispari: insieme degli idx = %d attesi' % len(ODD), tuple(odd_en) == ODD, odd_en)
ck('virgolette dispari: stessi idx in italiano', odd_en == odd_it, (odd_en, odd_it))

ck('nessuna unita con italiano vuoto', all(u['italian'].strip() for u in tu))
NONLAT = re.compile(r'[^\x00-\x7F\u00C0-\u024F\u2018\u2019\u201C\u201D\u2013\u2014\u2026]')
sus = [(u['idx'], NONLAT.findall(u['italian'])[:3]) for u in tu if NONLAT.search(u['italian'])]
ck('nessun carattere non latino sospetto', not sus, sus[:10])

dash = [u['idx'] for u in tu if '\u2014' in u['italian'] or '\u2013' in u['italian']]
ck('nessun trattino lungo/en-dash (vietati)', not dash, dash[:10])
curly = [u['idx'] for u in tu if '\u2018' in u['italian'] or '\u2019' in u['italian']
         or '\u201C' in u['italian'] or '\u201D' in u['italian']]
ck('nessuna virgoletta curva (apostrofo dritto)', not curly, curly[:10])

bad_ratio = [u['idx'] for u in tu if u['ratio'] is None]
ck('rapporto lunghezze definito per tutte le unita', not bad_ratio, bad_ratio[:10])
rs = [u['ratio'] for u in tu if u['ratio'] is not None]
print('rapporto IT/EN: min %.2f max %.2f' % (min(rs), max(rs)))

merged = {}
for f in sorted(glob.glob(os.path.join(HERE, 'parts', 'part*.json'))):
    for k, v in json.load(open(f, encoding='utf-8')).items():
        merged[int(k)] = v
# il costruttore antepone i tab iniziali del sorgente: il confronto li rimette
en_by_idx = {u['idx']: u['english'] for u in su}
rebuilt = {i: '\t' * (len(en_by_idx[i]) - len(en_by_idx[i].lstrip('\t'))) + v
           for i, v in merged.items()}
ck('le parti su disco ricostruiscono translation.json (tab compresi)',
   rebuilt == {u['idx']: u['italian'] for u in tu})

h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
en_w = sum(len(u['english'].split()) for u in tu)
it_w = sum(len(u['italian'].split()) for u in tu)
print('parole EN %d -> IT %d · traduzione sha256[:16] %s' % (en_w, it_w, h[:16]))

print()
print('FAIL:', len(fail), '·', 'verify L42 superato' if not fail else 'verify L42 fallito')
raise SystemExit(0 if not fail else 1)
