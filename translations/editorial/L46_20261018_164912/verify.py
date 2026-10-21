r"""verify.py — L46 (data/successors/successor 1 prologue.txt, 221 unita', righe 24-664)

**Non e' fine file**: il file conta 345 unita' e prosegue dopo la riga 664 fino alla 1024. La copertura
TOTALE del file **non** e' un invariante di questo lotto; lo e' invece la copertura del segmento dichiarato
(221/221) e il residuo misurato a valle (124 unita' dopo la riga 664).

Controlli indipendenti da check.py, senza riusare la sua logica:

  1. la riga grezza di ogni unita' coincide con quella del file sorgente
  2. english / kind / path coincidono con state.db, e lo stato e' PENDING
  3. nessuna unita' del lotto risulta APPROVED
  4. id univoci e ordine = ordine del sorgente
  5. collocazione: 221 unita', righe 24-664
  6. **0 unita' prima della 24, 124 dopo la 664** (segmento interno al file, non chiusura)
  7. copertura del **segmento** 221/221 (righe 24-664), e nessun altro lotto che ne copra unita':
     il file prosegue e altri lotti lo tradurranno, quindi il controllo e' sulle righe, non sul file
  8. distribuzione dei kind misurata: 187 MISSION_TEXT, 17 UI_LABEL, 9 LOGBOOK, 3 VALUE,
     3 DESCRIPTION, 2 DIALOG
  9. `NT`: le **17** `UI_LABEL` (label di salto, bersagli di `goto`) **piu' 1 riferimento di dato**
     (62 = categoria di `log`), identici al sorgente ed elencati uno per uno
 10. **`LOGBOOK` 9**: controllo POSITIVO. Le **8** righe `log` di testo sono presenti, tradotte, con i
     tab del sorgente, e le **tre forme** presenti nel segmento sono identificate sul `raw`:
     `log "testo"` (6: 19, 21, 98, 100, 197, 204), `log \`testo\`` (1: 25),
     `log "Categoria" "Nome" \`testo\`` (1: 26). La nona (62) e' la categoria estratta come unita'.
 11. **`CONVERSATION` 0**: assenza dichiarata (il file ne ha altrove, il segmento no)
 12. **tab 175 e virgolette 278**: parita' sui totali e **per unita'**; 175 unita' che iniziano con tab
 13. **0 virgolette dispari**: assenza dichiarata, non un elenco ereditato
 14. token: parita' esatta su tutte le unita' (36 occorrenze, 8 famiglie)
 15. **0 unita' con quadre**: assenza dichiarata (nessun frammento redatto in questo segmento)
 16. 0 backtick nell'italiano, 0 nell'inglese
 17. nessuna unita' con italiano vuoto; nessun carattere non latino sospetto
 18. nessun trattino lungo (U+2014) ne' en-dash, nessuna virgoletta curva
 19. rapporto lunghezze definito; estremi stampati
 20. le parti su disco ricostruiscono translation.json (tab del costruttore compresi)
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
PATH = 'data/successors/successor 1 prologue.txt'
SRC = os.path.join(ROOT, 'endless-sky', *PATH.split('/'))

source = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
trans = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))
su, tu = source['units'], trans['units']
lines = open(SRC, encoding='utf-8').read().split('\n')

# le 17 label di salto: bersagli di `goto`, restano identiche
NT_LABEL = set([44, 54, 81, 123, 126, 128, 134, 152, 154, 156, 163, 172, 175, 183, 185, 191, 193])
# il riferimento di dato: categoria di diario (log "People" "Sieasej" "testo")
NT_DATA = set([62])
NT = NT_LABEL | NT_DATA
# le 8 righe di diario di testo, attese e tradotte (controllo positivo)
LOG = (19, 21, 25, 26, 98, 100, 197, 204)
# le tre forme di `log` presenti nel segmento
FORM_DIRECT = (19, 21, 98, 100, 197, 204)
FORM_BACKTICK = (25,)
FORM_THREE = (26,)
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
   len(tu) == 221 and (first, last) == (24, 664), (len(tu), first, last))

maxline = db.execute('select max(line) from units where path = ?', (PATH,)).fetchone()[0]
before = db.execute('select count(*) from units where path = ? and line < ?',
                    (PATH, first)).fetchone()[0]
after = db.execute('select count(*) from units where path = ? and line > ?',
                   (PATH, last)).fetchone()[0]
tot = db.execute('select count(*) from units where path = ?', (PATH,)).fetchone()[0]
ck('segmento interno: 0 unita prima della 24, 124 dopo la 664',
   before == 0 and after == 124 and tot == 345 and maxline == 1024,
   (before, after, tot, maxline))

# Copertura del SEGMENTO, non del file: il file prosegue dopo la riga 664 e altri lotti (a partire da
# L47) lo tradurranno. Il controllo deve restare valido quando il workspace cresce, senza diventare falso.
lotti = []
for name in sorted(os.listdir(os.path.join(L10N, 'staging', 'editorial'))):
    f = os.path.join(L10N, 'staging', 'editorial', name, 'translation.json')
    if not os.path.exists(f):
        continue
    d = json.load(open(f, encoding='utf-8'))['units']
    if d and d[0]['path'] == PATH:
        lotti.append((name.split('_')[0], set(u['id'] for u in d)))
print('lotti su questo file:', [(lab, len(ids)) for lab, ids in lotti])
seg_ids = set(r[0] for r in db.execute(
    'select id from units where path = ? and line between ? and ?', (PATH, first, last)).fetchall())
ck('copertura del segmento %d / %d (righe %d-%d)' % (len(seg_ids), len(tu), first, last),
   len(seg_ids) == 221 and set(u['id'] for u in tu) == seg_ids, (len(seg_ids), len(tu)))
altri = [(lab, len(ids & seg_ids)) for lab, ids in lotti if lab != 'L46' and (ids & seg_ids)]
ck('nessun altro lotto copre unita del segmento', not altri, altri)

kinds = collections.Counter(u['kind'] for u in su)
atteso = {'MISSION_TEXT': 187, 'UI_LABEL': 17, 'LOGBOOK': 9, 'VALUE': 3,
          'DESCRIPTION': 3, 'DIALOG': 2}
ck('distribuzione dei kind come misurata', dict(kinds) == atteso, dict(kinds))

by_idx = {u['idx']: u for u in tu}
bad_nt = [i for i in NT if by_idx[i]['italian'] != by_idx[i]['english']]
missing_nt = [i for i in NT if i not in by_idx]
ck('NT: %d riferimenti identici al sorgente (17 label + 1 dato)' % len(NT),
   len(NT) == 18 and not bad_nt and not missing_nt, (bad_nt, missing_nt))
ui = sorted(u['idx'] for u in tu if u['kind'] == 'UI_LABEL')
ck('il file ha esattamente 17 UI_LABEL nel segmento, tutte in NT',
   ui == sorted(NT_LABEL), ui)
ck('il riferimento di dato e una categoria di diario, non prosa',
   by_idx[62]['kind'] == 'LOGBOOK' and by_idx[62]['english'] == 'People')

# --- CONVERSATION: asserzione di assenza dichiarata ---
conv = [u['idx'] for u in tu if u['kind'] == 'CONVERSATION']
ck('CONVERSATION: nessuna nel segmento (assenza dichiarata)', conv == [], conv)

# --- LOGBOOK: controllo positivo, non assenza ---
log_it = tuple(u['idx'] for u in tu if u['kind'] == 'LOGBOOK' and u['idx'] != 62)
ck('LOGBOOK: %d righe di testo nel lotto, %d attese' % (len(log_it), len(LOG)),
   log_it == LOG, log_it)
ck('LOGBOOK: nessuna riga di testo lasciata identica all\'inglese',
   not [i for i in LOG if by_idx[i]['italian'].strip() == by_idx[i]['english'].strip()],
   [i for i in LOG if by_idx[i]['italian'].strip() == by_idx[i]['english'].strip()])
ck('LOGBOOK: tab del sorgente conservati',
   not [i for i in LOG if by_idx[i]['italian'].count('\t') != by_idx[i]['english'].count('\t')])
raw_by_idx = {u['idx']: u['raw'] for u in su}
f_direct = tuple(i for i in LOG if re.match(r'\t+log "[^"]+"\s*$', raw_by_idx[i]))
f_back = tuple(i for i in LOG if re.match(r'\t+log `', raw_by_idx[i]))
f_three = tuple(i for i in LOG if re.match(r'\t+log "[^"]+" "[^"]+" `', raw_by_idx[i]))
ck('LOGBOOK tre forme: %d diretta, %d backtick, %d a tre argomenti'
   % (len(f_direct), len(f_back), len(f_three)),
   f_direct == FORM_DIRECT and f_back == FORM_BACKTICK and f_three == FORM_THREE,
   (f_direct, f_back, f_three))
ck('LOGBOOK a tre argomenti: categoria e nome NON dentro l\'unita',
   all('log "' not in by_idx[i]['english'] and '`' not in by_idx[i]['english'] for i in FORM_THREE))

# quadre: nessun frammento redatto in questo segmento
br = [u['idx'] for u in su if '[' in u['english'] or ']' in u['english']]
ck('quadre: nessuna unita con [ o ] nel sorgente (assenza dichiarata)', br == [], br[:5])
pair = [u['idx'] for u in tu if '[' in u['italian'] or ']' in u['italian']]
ck('quadre: nessuna quadra nell\'italiano', pair == [], pair)

diff = [u['idx'] for u in tu
        if collections.Counter(TAGS.findall(u['english'])) != collections.Counter(TAGS.findall(u['italian']))]
ck('nessuna unita con token diversi (parita esatta)', not diff, sorted(set(diff))[:10])
tot_en = sum(len(TAGS.findall(u['english'])) for u in su)
tot_it = sum(len(TAGS.findall(u['italian'])) for u in tu)
ck('token totali %d = %d (8 famiglie)' % (tot_it, tot_en), tot_en == tot_it, (tot_it, tot_en))

for ch, nome in (('\t', 'tab'), ('"', 'virgolette'), ('`', 'backtick')):
    a = sum(u['english'].count(ch) for u in su)
    b = sum(u['italian'].count(ch) for u in tu)
    ck('%s totali %d = %d' % (nome, b, a), a == b)

per_unit = [u['idx'] for u in tu if u['english'].count('\t') != u['italian'].count('\t')
            or u['english'].count('"') != u['italian'].count('"')]
ck('tab e virgolette: parita per unita (221 unita)', per_unit == [], per_unit[:10])
lead = [u['idx'] for u in tu if u['english'].startswith('\t') != u['italian'].startswith('\t')]
ntab = len([u for u in tu if u['italian'].startswith('\t')])
ck('tab iniziale presente dove il sorgente lo ha (175)', ntab == 175 and lead == [], (ntab, lead[:5]))

odd_en = sorted(u['idx'] for u in su if u['english'].count('"') % 2)
odd_it = sorted(u['idx'] for u in tu if u['italian'].count('"') % 2)
ck('virgolette dispari: 0 nel segmento (assenza dichiarata)', odd_en == [] and odd_it == [],
   (odd_en, odd_it))

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
print('FAIL:', len(fail), '·', 'verify L46 superato' if not fail else 'verify L46 fallito')
raise SystemExit(0 if not fail else 1)
