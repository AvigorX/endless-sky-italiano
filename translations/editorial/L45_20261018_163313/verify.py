"""verify.py — L45 (data/successors/successor 2 ghosts.txt, 680 unita', righe 37-2167, fine file)

L45 chiude il file: copre dalla prima unita' all'ultima, quindi la copertura TOTALE del file e' un
invariante legittimo (come in L28-L44).

Controlli indipendenti da check.py, senza riusare la sua logica:

  1. la riga grezza di ogni unita' coincide con quella del file sorgente
  2. english / kind / path coincidono con state.db, e lo stato e' PENDING
  3. nessuna unita' del lotto risulta APPROVED
  4. id univoci e ordine = ordine del sorgente
  5. collocazione: 680 unita', righe 37-2167
  6. nessuna unita' del file prima della 37 o dopo la 2167
  7. copertura totale del file 680/680, da un solo lotto
  8. distribuzione dei kind misurata: 559 MISSION_TEXT, 26 UI_LABEL, 23 LOGBOOK, 21 DESCRIPTION,
     20 VALUE, 16 CONVERSATION, 15 DIALOG
  9. `NT`: le **26** `UI_LABEL` (label di salto, bersagli di `goto`) **piu' 8 riferimenti di dato**
     (195, 305, 357, 418 = categoria di `log`; 355, 467, 513, 552 = nome di `government`), identici
     al sorgente ed elencati uno per uno; il file ha esattamente 26 `UI_LABEL`
 10. **`LOGBOOK` 23**: controllo POSITIVO. Le **19** righe `log` di testo sono presenti, tradotte
     (nessuna identica all'inglese), con i tab del sorgente. Le altre **4** sono categorie di diario
     (`log "Categoria" "Nome" "testo"` con il testo fra virgolette): l'unita' e' la sola categoria,
     quindi resta in inglese — lacuna di inventario di `tools/l10n.py` (protetto), documentata nel
     `review.md`. Controllo dedicato: categoria identica e testo NON dentro l'unita'.
 11. **`CONVERSATION` 16** (135-138, 256-267): nodi di conversazione (prima volta nella serie).
     Presenti, tradotti, nessuno identico all'inglese tranne 137 `(No.)` -> `(No.)`.
 12. tab 526 e virgolette 1107: parita' sui totali e **per unita'**; 526 unita' che iniziano con tab
 13. **15 virgolette dispari**: l'insieme degli idx coincide con quello del sorgente
     (15, 95, 159, 163, 479, 524, 525, 611, 612, 651, 652, 657, 666, 667, 669)
 14. token: parita' esatta su tutte le unita' (102 occorrenze, 14 famiglie)
 15. **11 unita' con quadre** (651, 652, 653, 655, 657, 664, 666, 667, 668, 669, 670): marcatori
     `[...]` dei frammenti redatti; conteggio di `[` e `]` invariato per unita'
 16. nessun backtick (ne' nell'inglese ne' nell'italiano)
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
PATH = 'data/successors/successor 2 ghosts.txt'
SRC = os.path.join(ROOT, 'endless-sky', *PATH.split('/'))

source = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
trans = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))
su, tu = source['units'], trans['units']
lines = open(SRC, encoding='utf-8').read().split('\n')

# le 26 label di salto: bersagli di `goto`, restano identiche
NT_LABEL = set([12, 51, 56, 99, 186, 206, 208, 218, 221, 349, 434, 473, 533, 536, 574, 578, 616, 627,
                632, 636, 639, 641, 643, 654, 656, 658])
# gli 8 riferimenti di dato: categoria di diario (195, 305, 357, 418) e nome di governo (355, 467,
# 513, 552). Non sono prosa: restano identici.
NT_DATA = set([195, 305, 357, 418, 355, 467, 513, 552])
NT = NT_LABEL | NT_DATA
# le 19 righe di diario di testo, attese e tradotte (controllo positivo)
LOG = (1, 7, 25, 59, 125, 151, 231, 252, 255, 282, 304, 356, 554, 586, 651, 652, 653, 655, 657)
# le 4 categorie di diario estratte come unita' (il testo del diario resta fuori)
LOG_CAT = (195, 305, 357, 418)
CONV = (135, 136, 137, 138, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267)
CONV_SAME = (137,)
ODD = (15, 95, 159, 163, 479, 524, 525, 611, 612, 651, 652, 657, 666, 667, 669)
BRACKETS = (651, 652, 653, 655, 657, 664, 666, 667, 668, 669, 670)
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
   len(tu) == 680 and (first, last) == (37, 2167), (len(tu), first, last))

maxline = db.execute('select max(line) from units where path = ?', (PATH,)).fetchone()[0]
before = db.execute('select count(*) from units where path = ? and line < ?',
                    (PATH, first)).fetchone()[0]
after = db.execute('select count(*) from units where path = ? and line > ?',
                   (PATH, last)).fetchone()[0]
ck('lotto inizia alla riga 37: 0 unita prima, 0 dopo (fine file)',
   before == 0 and after == 0 and maxline == 2167, (before, after, maxline))

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
   tot == 680 and tot_staging == tot, (tot_staging, tot))
ck('un solo lotto, nessuna unita duplicata', len(lotti) == 1 and sovrapposti == 0,
   (lotti, sovrapposti))

kinds = collections.Counter(u['kind'] for u in su)
atteso = {'MISSION_TEXT': 559, 'UI_LABEL': 26, 'LOGBOOK': 23, 'DESCRIPTION': 21,
          'VALUE': 20, 'CONVERSATION': 16, 'DIALOG': 15}
ck('distribuzione dei kind come misurata', dict(kinds) == atteso, dict(kinds))

by_idx = {u['idx']: u for u in tu}
bad_nt = [i for i in NT if by_idx[i]['italian'] != by_idx[i]['english']]
missing_nt = [i for i in NT if i not in by_idx]
ck('NT: %d riferimenti identici al sorgente (26 label + 8 dati)' % len(NT),
   len(NT) == 34 and not bad_nt and not missing_nt, (bad_nt, missing_nt))
ui = sorted(u['idx'] for u in tu if u['kind'] == 'UI_LABEL')
ck('il file ha esattamente 26 UI_LABEL, tutte in NT', ui == sorted(NT_LABEL), ui)

# --- CONVERSATION: controllo dedicato (16 attese) ---
conv_it = tuple(u['idx'] for u in tu if u['kind'] == 'CONVERSATION')
ck('CONVERSATION: %d nodi nel lotto, %d attesi' % (len(conv_it), len(CONV)),
   conv_it == CONV, conv_it)
conv_same = [i for i in CONV if by_idx[i]['italian'].strip() == by_idx[i]['english'].strip()
             and i not in CONV_SAME]
ck('CONVERSATION: nessuno lasciato in inglese (%d identico per necessita)' % len(CONV_SAME),
   not conv_same, conv_same)
ck('CONVERSATION: tab interni al nodo conservati',
   not [i for i in CONV if by_idx[i]['italian'].count('\t') != by_idx[i]['english'].count('\t')])

# --- LOGBOOK: controllo positivo, non assenza ---
log_it = tuple(u['idx'] for u in tu if u['kind'] == 'LOGBOOK' and u['idx'] not in LOG_CAT)
ck('LOGBOOK: %d righe di testo nel lotto, %d attese' % (len(log_it), len(LOG)),
   log_it == LOG, log_it)
ck('LOGBOOK: nessuna riga di testo lasciata identica all\'inglese',
   not [i for i in LOG if by_idx[i]['italian'].strip() == by_idx[i]['english'].strip()],
   [i for i in LOG if by_idx[i]['italian'].strip() == by_idx[i]['english'].strip()])
ck('LOGBOOK: tab del sorgente conservati',
   not [i for i in LOG if by_idx[i]['italian'].count('\t') != by_idx[i]['english'].count('\t')])
raw_by_idx = {u['idx']: u['raw'] for u in su}
log_cat = tuple(i for i in LOG_CAT if re.match(r'\t+log "[^"]+" "[^"]+" "', raw_by_idx[i]))
ck('LOGBOOK con testo fra virgolette: %d categorie estratte come unita' % len(log_cat),
   log_cat == LOG_CAT, log_cat)
ck('LOGBOOK categorie: identiche al sorgente, testo del diario fuori dall\'unita',
   all(by_idx[i]['italian'] == by_idx[i]['english']
       and by_idx[i]['english'] in ('People', 'Factions') for i in LOG_CAT))

# quadre: 11 unita' con i marcatori [...] dei frammenti redatti
br = tuple(u['idx'] for u in su if '[' in u['english'] or ']' in u['english'])
ck('quadre: %d unita con [ o ] nel sorgente, %d attese' % (len(br), len(BRACKETS)),
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
ck('token totali %d = %d (14 famiglie)' % (tot_it, tot_en), tot_en == tot_it, (tot_it, tot_en))

for ch, nome in (('\t', 'tab'), ('"', 'virgolette'), ('`', 'backtick')):
    a = sum(u['english'].count(ch) for u in su)
    b = sum(u['italian'].count(ch) for u in tu)
    ck('%s totali %d = %d' % (nome, b, a), a == b)

per_unit = [u['idx'] for u in tu if u['english'].count('\t') != u['italian'].count('\t')
            or u['english'].count('"') != u['italian'].count('"')]
ck('tab e virgolette: parita per unita (680 unita)', per_unit == [], per_unit[:10])
lead = [u['idx'] for u in tu if u['english'].startswith('\t') != u['italian'].startswith('\t')]
ntab = len([u for u in tu if u['italian'].startswith('\t')])
ck('tab iniziale presente dove il sorgente lo ha (526)', ntab == 526 and lead == [], (ntab, lead[:5]))

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
print('FAIL:', len(fail), '·', 'verify L45 superato' if not fail else 'verify L45 fallito')
raise SystemExit(0 if not fail else 1)
