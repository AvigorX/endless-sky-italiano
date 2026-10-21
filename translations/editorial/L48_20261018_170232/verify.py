r"""verify.py — L48 (data/avgi/avgi side missions.txt, 180 unita', righe 26-499)

**Segmento interno**: il file conta 436 unita' e prosegue fino alla riga 1117; dopo la 499 restano **256**
unita' (lotto L49). La copertura TOTALE del file non e' un invariante di questo lotto; lo sono la
copertura del **segmento** (180/180, per righe) e il residuo misurato a valle.

Controlli indipendenti da check.py, senza riusare la sua logica:

  1. la riga grezza di ogni unita' coincide con quella del file sorgente
  2. english / kind / path coincidono con state.db, e lo stato e' PENDING
  3. nessuna unita' del lotto risulta APPROVED
  4. id univoci e ordine = ordine del sorgente
  5. collocazione: 180 unita', righe 26-499
  6. 0 unita' prima della 26, **256 dopo la 499** (max(line) = 1117, file di 436)
  7. copertura del segmento 180/180; nessun altro lotto che ne copra unita'
  8. distribuzione dei kind misurata: 152 MISSION_TEXT, 14 UI_LABEL, 14 LOGBOOK — e **nient'altro**:
     nessun `CONVERSATION`, `DIALOG`, `VALUE`, `DESCRIPTION`, `TEXT`
  9. `NT`: **14 `UI_LABEL`** e **nessun riferimento di dato**, elencate una per una
 10. **`LOGBOOK` 14 = 14 testi, 0 categorie**: in questo lotto la lacuna dell'estrattore NON si presenta.
     Forme identificate sul `raw`: `log "Categoria" "Nome" \`testo\`` (11) e `log \`testo\`` (3).
 11. **0 virgolette dispari, 0 quadre, 0 backtick**: assenze dichiarate
 12. tab 145 e virgolette 252: parita' sui totali e **per unita'**; 145 unita' che iniziano con tab
 13. token: parita' esatta (10 occorrenze, 4 famiglie)
 14. nessuna unita' con italiano vuoto; nessun carattere non latino sospetto
 15. nessun trattino lungo (U+2014) ne' en-dash, nessuna virgoletta curva
 16. rapporto lunghezze definito; estremi stampati
 17. le parti su disco ricostruiscono translation.json (tab del costruttore compresi)
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
PATH = 'data/avgi/avgi side missions.txt'
SRC = os.path.join(ROOT, 'endless-sky', *PATH.split('/'))

source = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
trans = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))
su, tu = source['units'], trans['units']
lines = open(SRC, encoding='utf-8').read().split('\n')

# le 14 label di salto: nessun riferimento di dato in questo lotto
NT = set([28, 30, 37, 39, 46, 61, 63, 65, 67, 76, 94, 116, 118, 121])
LOG = (84, 90, 99, 100, 101, 102, 103, 104, 105, 152, 153, 158, 176, 179)
FORM_THREE = (84, 90, 99, 100, 101, 102, 103, 104, 105, 153, 158)
FORM_ONE = (152, 176, 179)
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
   len(tu) == 180 and (first, last) == (26, 499), (len(tu), first, last))

maxline = db.execute('select max(line) from units where path = ?', (PATH,)).fetchone()[0]
before = db.execute('select count(*) from units where path = ? and line < ?',
                    (PATH, first)).fetchone()[0]
after = db.execute('select count(*) from units where path = ? and line > ?',
                   (PATH, last)).fetchone()[0]
tot = db.execute('select count(*) from units where path = ?', (PATH,)).fetchone()[0]
ck('segmento interno: 0 unita prima della 26, 256 dopo la 499',
   before == 0 and after == 256 and tot == 436 and maxline == 1117,
   (before, after, tot, maxline))

lotti = []
for name in sorted(os.listdir(os.path.join(L10N, 'staging', 'editorial'))):
    f = os.path.join(L10N, 'staging', 'editorial', name, 'translation.json')
    if not os.path.exists(f):
        continue
    d = json.load(open(f, encoding='utf-8'))['units']
    if d and d[0]['path'] == PATH:
        lotti.append((name.split('_')[0], set(u['id'] for u in d)))
print('lotti su questo file:', [(lab, len(s)) for lab, s in lotti])
seg_ids = set(r[0] for r in db.execute(
    'select id from units where path = ? and line between ? and ?', (PATH, first, last)).fetchall())
ck('copertura del segmento %d / %d (righe %d-%d)' % (len(seg_ids), len(tu), first, last),
   len(seg_ids) == 180 and set(u['id'] for u in tu) == seg_ids, (len(seg_ids), len(tu)))
altri = [(lab, len(s & seg_ids)) for lab, s in lotti if lab != 'L48' and (s & seg_ids)]
ck('nessun altro lotto copre unita del segmento', not altri, altri)

kinds = collections.Counter(u['kind'] for u in su)
atteso = {'MISSION_TEXT': 152, 'UI_LABEL': 14, 'LOGBOOK': 14}
ck('distribuzione dei kind: 152/14/14 e nient\'altro', dict(kinds) == atteso, dict(kinds))
for kind in ('CONVERSATION', 'DIALOG', 'VALUE', 'DESCRIPTION', 'TEXT'):
    ck('nessuna unita %s (assenza dichiarata)' % kind,
       not [u['idx'] for u in tu if u['kind'] == kind])

by_idx = {u['idx']: u for u in tu}
bad_nt = [i for i in NT if by_idx[i]['italian'] != by_idx[i]['english']]
missing_nt = [i for i in NT if i not in by_idx]
ck('NT: %d label identiche al sorgente, 0 riferimenti di dato' % len(NT),
   len(NT) == 14 and not bad_nt and not missing_nt, (bad_nt, missing_nt))
ui = sorted(u['idx'] for u in tu if u['kind'] == 'UI_LABEL')
ck('il segmento ha esattamente 14 UI_LABEL, tutte in NT', ui == sorted(NT), ui)

# --- LOGBOOK: 14 righe, tutte di testo (la lacuna dell'estrattore qui non c'e') ---
log_it = tuple(u['idx'] for u in tu if u['kind'] == 'LOGBOOK')
ck('LOGBOOK: %d righe nel lotto, %d attese' % (len(log_it), len(LOG)), log_it == LOG, log_it)
ck('LOGBOOK: nessuna riga lasciata identica all\'inglese',
   not [i for i in LOG if by_idx[i]['italian'].strip() == by_idx[i]['english'].strip()],
   [i for i in LOG if by_idx[i]['italian'].strip() == by_idx[i]['english'].strip()])
ck('LOGBOOK: tab del sorgente conservati',
   not [i for i in LOG if by_idx[i]['italian'].count('\t') != by_idx[i]['english'].count('\t')])
ck('LOGBOOK: nessuna categoria estratta (14 testi, 0 categorie)',
   len(log_it) == 14 and all(by_idx[i]['english'].strip() != 'People'
                             and by_idx[i]['english'].strip() != 'Factions'
                             and by_idx[i]['english'].strip() != 'Minor People' for i in LOG))
raw_by_idx = {u['idx']: u['raw'] for u in su}
f_three = tuple(i for i in LOG if re.match(r'\t+log "[^"]+" "[^"]+" `', raw_by_idx[i]))
f_one = tuple(i for i in LOG if re.match(r'\t+log `', raw_by_idx[i]))
ck('LOGBOOK due forme: %d a tre argomenti, %d diretta' % (len(f_three), len(f_one)),
   f_three == FORM_THREE and f_one == FORM_ONE, (f_three, f_one))

# assenze dichiarate: quadre, virgolette dispari, backtick
br = [u['idx'] for u in su if '[' in u['english'] or ']' in u['english']]
ck('quadre: nessuna unita con [ o ] nel sorgente (assenza dichiarata)', br == [], br[:5])
pair = [u['idx'] for u in tu if '[' in u['italian'] or ']' in u['italian']]
ck('quadre: nessuna quadra nell\'italiano', pair == [], pair)
odd_en = sorted(u['idx'] for u in su if u['english'].count('"') % 2)
odd_it = sorted(u['idx'] for u in tu if u['italian'].count('"') % 2)
ck('virgolette dispari: 0 nel segmento (assenza dichiarata)', odd_en == [] and odd_it == [],
   (odd_en, odd_it))

diff = [u['idx'] for u in tu
        if collections.Counter(TAGS.findall(u['english'])) != collections.Counter(TAGS.findall(u['italian']))]
ck('nessuna unita con token diversi (parita esatta)', not diff, sorted(set(diff))[:10])
tot_en = sum(len(TAGS.findall(u['english'])) for u in su)
tot_it = sum(len(TAGS.findall(u['italian'])) for u in tu)
ck('token totali %d = %d (4 famiglie)' % (tot_it, tot_en), tot_en == tot_it, (tot_it, tot_en))

for ch, nome in (('\t', 'tab'), ('"', 'virgolette'), ('`', 'backtick')):
    a = sum(u['english'].count(ch) for u in su)
    b = sum(u['italian'].count(ch) for u in tu)
    ck('%s totali %d = %d' % (nome, b, a), a == b)

per_unit = [u['idx'] for u in tu if u['english'].count('\t') != u['italian'].count('\t')
            or u['english'].count('"') != u['italian'].count('"')]
ck('tab e virgolette: parita per unita (180 unita)', per_unit == [], per_unit[:10])
lead = [u['idx'] for u in tu if u['english'].startswith('\t') != u['italian'].startswith('\t')]
ntab = len([u for u in tu if u['italian'].startswith('\t')])
ck('tab iniziale presente dove il sorgente lo ha (145)', ntab == 145 and lead == [], (ntab, lead[:5]))

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
print('FAIL:', len(fail), '·', 'verify L48 superato' if not fail else 'verify L48 fallito')
raise SystemExit(0 if not fail else 1)
