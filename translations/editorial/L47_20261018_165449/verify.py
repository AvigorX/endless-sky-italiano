r"""verify.py — L47 (data/successors/successor 1 prologue.txt, 124 unita', righe 680-1024, fine file)

L47 chiude il file: 221 unita' di L46 (righe 24-664) piu' 124 di L47 (righe 680-1024) = 345/345.
La copertura TOTALE del file e' quindi un invariante legittimo, ma va verificata **sui due lotti**, non
sul solo L47.

Controlli indipendenti da check.py, senza riusare la sua logica:

  1. la riga grezza di ogni unita' coincide con quella del file sorgente
  2. english / kind / path coincidono con state.db, e lo stato e' PENDING
  3. nessuna unita' del lotto risulta APPROVED
  4. id univoci e ordine = ordine del sorgente
  5. collocazione: 124 unita', righe 680-1024
  6. 221 unita' prima della 680 (L46), **0 dopo la 1024** (fine file)
  7. copertura totale 345/345 su **due lotti** (L46 221 + L47 124), nessuna sovrapposizione
  8. distribuzione dei kind misurata: 108 MISSION_TEXT, 8 UI_LABEL, 4 LOGBOOK, 2 VALUE, 2 DESCRIPTION
  9. `NT`: **8 `UI_LABEL`** (label di salto) **piu' 1 riferimento di dato** (54 = categoria di `log`)
 10. **`LOGBOOK` 4**: controllo POSITIVO. **3** righe di testo (59, 67, 68) presenti e tradotte, con i
     tab del sorgente; forme identificate sul `raw`: `log "testo"` (59, 67) e
     `log "Categoria" "Nome" \`testo\`` (68). La quarta (54) e' la categoria `People`.
 11. **`CONVERSATION` 0**: assenza dichiarata
 12. **tab 102 caratteri su 100 unita'** e virgolette 124: parita' sui totali e **per unita'**
 13. **2 virgolette dispari** (46, 63): stesso insieme di idx in italiano
 14. token: parita' esatta (24 occorrenze, 9 famiglie)
 15. **1 unita' con quadre** (21, annuncio in maiuscolo): conteggio di `[` e `]` invariato per unita'
 16. 0 backtick nell'italiano
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

# le 8 label di salto
NT_LABEL = set([6, 12, 18, 20, 79, 81, 85, 112])
# il riferimento di dato: categoria di diario (`log "People" "Saajret..." "testo"`)
NT_DATA = set([54])
NT = NT_LABEL | NT_DATA
LOG = (59, 67, 68)
FORM_DIRECT = (59, 67)
FORM_THREE = (68,)
ODD = (46, 63)
BRACKETS = (21,)
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
   len(tu) == 124 and (first, last) == (680, 1024), (len(tu), first, last))

maxline = db.execute('select max(line) from units where path = ?', (PATH,)).fetchone()[0]
before = db.execute('select count(*) from units where path = ? and line < ?',
                    (PATH, first)).fetchone()[0]
after = db.execute('select count(*) from units where path = ? and line > ?',
                   (PATH, last)).fetchone()[0]
tot = db.execute('select count(*) from units where path = ?', (PATH,)).fetchone()[0]
ck('fine file: 221 prima della 680, 0 dopo la 1024',
   before == 221 and after == 0 and tot == 345 and maxline == 1024,
   (before, after, tot, maxline))

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
ck('copertura del file %d / %d (L46 + L47)' % (tot_staging, tot),
   tot == 345 and tot_staging == tot, (tot_staging, tot))
ck('due lotti (221 + 124), nessuna unita duplicata',
   sorted(lotti) == [('L46', 221), ('L47', 124)] and sovrapposti == 0, (lotti, sovrapposti))

kinds = collections.Counter(u['kind'] for u in su)
atteso = {'MISSION_TEXT': 108, 'UI_LABEL': 8, 'LOGBOOK': 4, 'VALUE': 2, 'DESCRIPTION': 2}
ck('distribuzione dei kind come misurata', dict(kinds) == atteso, dict(kinds))

by_idx = {u['idx']: u for u in tu}
bad_nt = [i for i in NT if by_idx[i]['italian'] != by_idx[i]['english']]
missing_nt = [i for i in NT if i not in by_idx]
ck('NT: %d riferimenti identici al sorgente (8 label + 1 dato)' % len(NT),
   len(NT) == 9 and not bad_nt and not missing_nt, (bad_nt, missing_nt))
ui = sorted(u['idx'] for u in tu if u['kind'] == 'UI_LABEL')
ck('il segmento ha esattamente 8 UI_LABEL, tutte in NT', ui == sorted(NT_LABEL), ui)
ck('il riferimento di dato e una categoria di diario, non prosa',
   by_idx[54]['kind'] == 'LOGBOOK' and by_idx[54]['english'] == 'People')

conv = [u['idx'] for u in tu if u['kind'] == 'CONVERSATION']
ck('CONVERSATION: nessuna nel segmento (assenza dichiarata)', conv == [], conv)

# --- LOGBOOK: controllo positivo ---
log_it = tuple(u['idx'] for u in tu if u['kind'] == 'LOGBOOK' and u['idx'] != 54)
ck('LOGBOOK: %d righe di testo nel lotto, %d attese' % (len(log_it), len(LOG)),
   log_it == LOG, log_it)
ck('LOGBOOK: nessuna riga di testo lasciata identica all\'inglese',
   not [i for i in LOG if by_idx[i]['italian'].strip() == by_idx[i]['english'].strip()],
   [i for i in LOG if by_idx[i]['italian'].strip() == by_idx[i]['english'].strip()])
ck('LOGBOOK: tab del sorgente conservati',
   not [i for i in LOG if by_idx[i]['italian'].count('\t') != by_idx[i]['english'].count('\t')])
raw_by_idx = {u['idx']: u['raw'] for u in su}
f_direct = tuple(i for i in LOG if re.match(r'\t+log "[^"]+"\s*$', raw_by_idx[i]))
f_three = tuple(i for i in LOG if re.match(r'\t+log "[^"]+" "[^"]+" `', raw_by_idx[i]))
ck('LOGBOOK due forme: %d diretta, %d a tre argomenti' % (len(f_direct), len(f_three)),
   f_direct == FORM_DIRECT and f_three == FORM_THREE, (f_direct, f_three))
ck('LOGBOOK a tre argomenti: categoria e nome NON dentro l\'unita',
   all('log "' not in by_idx[i]['english'] and '`' not in by_idx[i]['english'] for i in FORM_THREE))

# quadre: una sola unita', annuncio in maiuscolo
br = tuple(u['idx'] for u in su if '[' in u['english'] or ']' in u['english'])
ck('quadre: %d unita con [ o ] nel sorgente, %d attesa' % (len(br), len(BRACKETS)),
   br == BRACKETS, br)
bad_br = [u['idx'] for u in tu
          if u['english'].count('[') != u['italian'].count('[')
          or u['english'].count(']') != u['italian'].count(']')]
ck('quadre: conteggio di [ e ] invariato per unita', not bad_br, bad_br)

diff = [u['idx'] for u in tu
        if collections.Counter(TAGS.findall(u['english'])) != collections.Counter(TAGS.findall(u['italian']))]
ck('nessuna unita con token diversi (parita esatta)', not diff, sorted(set(diff))[:10])
tot_en = sum(len(TAGS.findall(u['english'])) for u in su)
tot_it = sum(len(TAGS.findall(u['italian'])) for u in tu)
ck('token totali %d = %d (9 famiglie)' % (tot_it, tot_en), tot_en == tot_it, (tot_it, tot_en))

for ch, nome in (('\t', 'tab'), ('"', 'virgolette'), ('`', 'backtick')):
    a = sum(u['english'].count(ch) for u in su)
    b = sum(u['italian'].count(ch) for u in tu)
    ck('%s totali %d = %d' % (nome, b, a), a == b)

per_unit = [u['idx'] for u in tu if u['english'].count('\t') != u['italian'].count('\t')
            or u['english'].count('"') != u['italian'].count('"')]
ck('tab e virgolette: parita per unita (124 unita)', per_unit == [], per_unit[:10])
lead = [u['idx'] for u in tu if u['english'].startswith('\t') != u['italian'].startswith('\t')]
ntab = len([u for u in tu if u['italian'].startswith('\t')])
ck('tab iniziale presente dove il sorgente lo ha (100 unita)', ntab == 100 and lead == [], (ntab, lead[:5]))

odd_en = sorted(u['idx'] for u in su if u['english'].count('"') % 2)
odd_it = sorted(u['idx'] for u in tu if u['italian'].count('"') % 2)
ck('virgolette dispari: insieme degli idx = %d attese' % len(ODD), tuple(odd_en) == ODD, odd_en)
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
print('FAIL:', len(fail), '·', 'verify L47 superato' if not fail else 'verify L47 fallito')
raise SystemExit(0 if not fail else 1)
