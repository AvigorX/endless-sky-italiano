"""verify.py — L44 (data/sheragi/archaeology missions.txt, 625 unita', righe 16-1718, fine file)

L44 chiude il file: copre dalla prima unita' all'ultima, quindi la copertura TOTALE del file e' un
invariante legittimo (come in L28-L43).

Controlli indipendenti da check.py, senza riusare la sua logica:

  1. la riga grezza di ogni unita' coincide con quella del file sorgente
  2. english / kind / path coincidono con state.db, e lo stato e' PENDING
  3. nessuna unita' del lotto risulta APPROVED
  4. id univoci e ordine = ordine del sorgente
  5. collocazione: 625 unita', righe 16-1718
  6. nessuna unita' del file prima della 16 o dopo la 1718
  7. copertura totale del file 625/625, da un solo lotto
  8. distribuzione dei kind misurata: 535 MISSION_TEXT, 30 DESCRIPTION, 28 VALUE, 12 LOGBOOK,
     10 DIALOG, 10 UI_LABEL
  9. `NT`: le **10** `UI_LABEL` (label di salto, bersagli di `goto`) identiche al sorgente, elencate
     una per una; il file ha esattamente 10 `UI_LABEL`
 10. **`LOGBOOK` 12**: controllo POSITIVO. Le 12 righe `log` sono presenti, tradotte (nessuna identica
     all'inglese), con i tab del sorgente; le 5 a tre argomenti (`log "Categoria" "Nome" `testo``) sono
     identificate: l'unita' e' solo il testo, quindi categoria e nome restano in inglese (lacuna di
     inventario di `tools/l10n.py`, protetta, documentata nel `review.md`).
 11. tab 483 e virgolette 921: parita' sui totali e **per unita'**; 483 unita' che iniziano con tab
 12. **17 virgolette dispari**: l'insieme degli idx coincide con quello del sorgente
     (209, 249, 260, 262, 269, 302, 322, 367, 369, 379, 383, 388, 477, 478, 502, 522, 542)
 13. token: parita' esatta su tutte le unita' (73 occorrenze, 8 famiglie)
 14. nessun backtick nell'italiano
 15. nessuna unita' con italiano vuoto; nessun carattere non latino sospetto
 16. nessun trattino lungo (U+2014) ne' en-dash, nessuna virgoletta curva
 17. rapporto lunghezze definito; estremi stampati
 18. le parti su disco ricostruiscono translation.json (tab del costruttore compresi)
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
PATH = 'data/sheragi/archaeology missions.txt'
SRC = os.path.join(ROOT, 'endless-sky', *PATH.split('/'))

source = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
trans = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))
su, tu = source['units'], trans['units']
lines = open(SRC, encoding='utf-8').read().split('\n')

# le 10 label di salto: bersagli di `goto`, restano identiche
NT = set([204, 216, 244, 286, 290, 453, 459, 510, 569, 576])
# le 12 righe di diario, attese e tradotte (controllo positivo)
LOG = (37, 49, 69, 96, 122, 176, 180, 221, 409, 410, 411, 605)
ODD = (209, 249, 260, 262, 269, 302, 322, 367, 369, 379, 383, 388, 477, 478, 502, 522, 542)
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
   len(tu) == 625 and (first, last) == (16, 1718), (len(tu), first, last))

maxline = db.execute('select max(line) from units where path = ?', (PATH,)).fetchone()[0]
before = db.execute('select count(*) from units where path = ? and line < ?',
                    (PATH, first)).fetchone()[0]
after = db.execute('select count(*) from units where path = ? and line > ?',
                   (PATH, last)).fetchone()[0]
ck('lotto inizia alla riga 16: 0 unita prima, 0 dopo (fine file)',
   before == 0 and after == 0 and maxline == 1718, (before, after, maxline))

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
   tot == 625 and tot_staging == tot, (tot_staging, tot))
ck('un solo lotto, nessuna unita duplicata', len(lotti) == 1 and sovrapposti == 0,
   (lotti, sovrapposti))

kinds = collections.Counter(u['kind'] for u in su)
atteso = {'MISSION_TEXT': 535, 'DESCRIPTION': 30, 'VALUE': 28, 'LOGBOOK': 12,
          'DIALOG': 10, 'UI_LABEL': 10}
ck('distribuzione dei kind come misurata', dict(kinds) == atteso, dict(kinds))

by_idx = {u['idx']: u for u in tu}
bad_nt = [i for i in NT if by_idx[i]['italian'] != by_idx[i]['english']]
missing_nt = [i for i in NT if i not in by_idx]
ck('NT: %d label di salto identiche al sorgente' % len(NT),
   len(NT) == 10 and not bad_nt and not missing_nt, (bad_nt, missing_nt))
ui = sorted(u['idx'] for u in tu if u['kind'] == 'UI_LABEL')
ck('il file ha esattamente 10 UI_LABEL, tutte in NT', ui == sorted(NT), ui)
conv = [u['idx'] for u in tu if u['kind'] == 'CONVERSATION']
ck('CONVERSATION: nessuna nel file (asserzione di assenza)', conv == [], conv)

# --- LOGBOOK: controllo positivo, non assenza ---
log_it = [u['idx'] for u in tu if u['kind'] == 'LOGBOOK']
ck('LOGBOOK: %d righe nel lotto, %d attese' % (len(log_it), len(LOG)),
   tuple(log_it) == LOG, log_it)
ck('LOGBOOK: nessuna lasciata identica all\'inglese',
   not [i for i in LOG if by_idx[i]['italian'].strip() == by_idx[i]['english'].strip()],
   [i for i in LOG if by_idx[i]['italian'].strip() == by_idx[i]['english'].strip()])
ck('LOGBOOK: tab del sorgente conservati',
   not [i for i in LOG if by_idx[i]['italian'].count('\t') != by_idx[i]['english'].count('\t')])
raw_by_idx = {u['idx']: u['raw'] for u in su}
log3 = [i for i in LOG if re.match(r'\t\tlog "[^"]+" "[^"]+" `', raw_by_idx[i])]
ck('LOGBOOK a tre argomenti identificati: %d (categoria e nome in inglese)' % len(log3),
   sorted(log3) == [49, 180, 409, 410, 411], log3)
ck('LOGBOOK a tre argomenti: categoria e nome NON dentro l\'unita',
   all('log "' not in by_idx[i]['english'] and '" ' not in by_idx[i]['english'] for i in log3))

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
ck('tab e virgolette: parita per unita (625 unita)', per_unit == [], per_unit[:10])
lead = [u['idx'] for u in tu if u['english'].startswith('\t') != u['italian'].startswith('\t')]
ntab = len([u for u in tu if u['italian'].startswith('\t')])
ck('tab iniziale presente dove il sorgente lo ha (483)', ntab == 483 and lead == [], (ntab, lead[:5]))

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
print('FAIL:', len(fail), '·', 'verify L44 superato' if not fail else 'verify L44 fallito')
raise SystemExit(0 if not fail else 1)
