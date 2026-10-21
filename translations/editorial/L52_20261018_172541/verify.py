r"""verify.py — L52 (data/avgi/avgi 0 first contact.txt, 135 unita', righe 873-1120)

**L52 chiude il file.** Per la prima volta nella serie Avgi l'invariante «di file» e' legittimo:
  406 unita' = L50 (119, righe 22-402) + L51 (152, righe 413-869) + L52 (135, righe 873-1120),
  `max(line) = 1120` e **0 unita' dopo**.
Attenzione: l'invariante vale **solo perche'** la 1120 e' l'ultima riga. Se il file crescesse, questo
controllo diventerebbe rosso e andrebbe riscritto per segmento (decisione 166).

Controlli indipendenti da check.py, senza riusarne la logica:

  1. la riga grezza di ogni unita' coincide con quella del file sorgente
  2. english / kind / path / context coincidono con state.db, e lo stato e' PENDING
  3. nessuna unita' del lotto risulta APPROVED
  4. id univoci e ordine = ordine del sorgente
  5. collocazione: 135 unita', righe 873-1120
  6. **chiude il file**: 271 unita' prima (L50+L51), **0 dopo**, 406 totali, `max(line) = 1120`
  7. copertura del **file** 406/406 su **tre lotti** (L50 119 + L51 152 + L52 135), nessuna sovrapposizione
  8. distribuzione dei kind misurata: 106/17/4/4/3/1
  9. `NT`: **1 `UI_LABEL`** (57, `unknown ember waste`) identica al sorgente, 0 riferimenti di dato
 10. **`LOGBOOK` 17**: 10 a tre argomenti, 7 fra backtick, 0 dirette; nessuna categoria estratta
 11. **`DIALOG` 3** (76, 91, 133): tipo presente, controllo positivo; **`TEXT` 0**, **`CONVERSATION` 0**
 12. **0 virgolette dispari, 0 quadre, 0 backtick**: assenze dichiarate
 13. tab 94 e virgolette 212: parita' sui totali e **per unita'**
 14. token: parita' esatta (28 occorrenze, 6 famiglie)
 15. nessuna unita' con italiano vuoto; tipografia (accenti, apostrofi, dash)
 16. rapporto lunghezze dentro il gate 0,55-1,90
 17. nessuna unita' duplicata in inglese: nessuna resa italiana ripetuta
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
PATH = 'data/avgi/avgi 0 first contact.txt'
SRC = os.path.join(ROOT, 'endless-sky', *PATH.split('/'))

source = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
trans = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))
su, tu = source['units'], trans['units']
lines = open(SRC, encoding='utf-8').read().split('\n')

NT = set([57])
LOG = (4, 5, 6, 7, 16, 20, 21, 22, 67, 68, 89, 90, 95, 107, 108, 109, 134)
DIALOG = (76, 91, 133)
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
    row = db.execute('select english, kind, path, context, state from units where id = ?',
                     (u['id'],)).fetchone()
    if row is None or row['english'] != u['english'] or row['kind'] != u['kind'] \
            or row['path'] != u['path'] or row['context'] != u['context']:
        bad_db.append(u['idx'])
    elif row['state'] == 'APPROVED':
        approved.append(u['idx'])
    elif row['state'] != 'PENDING':
        bad_state.append((u['idx'], row['state']))
ck('english/kind/path/context identici al DB', not bad_db, bad_db[:10])
ck('state = PENDING per tutte le unita', not bad_state, bad_state[:10])
ck('nessuna unita del lotto e APPROVED nel DB', not approved, approved[:10])

ids = [u['id'] for u in tu]
ck('id univoci in translation.json', len(ids) == len(set(ids)))
ck('ordine delle unita = ordine del sorgente', [u['idx'] for u in tu] == [u['idx'] for u in su])
ck('stesse unita in source.json e translation.json',
   len(tu) == len(su) and [u['idx'] for u in tu] == [u['idx'] for u in su])

first, last = tu[0]['line'], tu[-1]['line']
ck('unita: %d righe %d - %d' % (len(tu), first, last),
   len(tu) == 135 and (first, last) == (873, 1120), (len(tu), first, last))

tot = db.execute('select count(*) from units where path = ?', (PATH,)).fetchone()[0]
before = db.execute('select count(*) from units where path = ? and line < ?',
                    (PATH, first)).fetchone()[0]
after = db.execute('select count(*) from units where path = ? and line > ?',
                   (PATH, last)).fetchone()[0]
maxline = db.execute('select max(line) from units where path = ?', (PATH,)).fetchone()[0]
ck('chiude il file: 271 prima della 873, 0 dopo la 1120',
   before == 271 and after == 0 and tot == 406, (before, after, tot, maxline))
ck('max(line) del file = 1120', maxline == 1120, maxline)

lotti = []
for name in sorted(os.listdir(os.path.join(L10N, 'staging', 'editorial'))):
    f = os.path.join(L10N, 'staging', 'editorial', name, 'translation.json')
    if not os.path.exists(f):
        continue
    d = json.load(open(f, encoding='utf-8'))['units']
    if d and d[0]['path'] == PATH:
        lotti.append((name.split('_')[0], set(u['id'] for u in d)))
sovrapposti = sum(len(a & b) for i, (_, a) in enumerate(lotti) for _, b in lotti[i + 1:])
ck('copertura del file %d / %d (tre lotti)' % (sum(len(s) for _, s in lotti), tot),
   tot == 406 and sum(len(s) for _, s in lotti) == tot, (sum(len(s) for _, s in lotti), tot))
ck('tre lotti (119 + 152 + 135), nessuna unita duplicata',
   sorted((lab, len(s)) for lab, s in lotti) == [('L50', 119), ('L51', 152), ('L52', 135)]
   and sovrapposti == 0,
   ([(lab, len(s)) for lab, s in lotti], sovrapposti))

kinds = collections.Counter(u['kind'] for u in su)
atteso = {'MISSION_TEXT': 106, 'LOGBOOK': 17, 'VALUE': 4, 'DESCRIPTION': 4, 'DIALOG': 3,
          'UI_LABEL': 1}
ck('distribuzione dei kind come misurata', dict(kinds) == atteso, dict(kinds))

by_idx = {u['idx']: u for u in tu}
ui = sorted(u['idx'] for u in tu if u['kind'] == 'UI_LABEL')
ck('UI_LABEL: esattamente 1 unita, ed e la 57', ui == [57], ui)
ck('NT: la label e identica al sorgente e non e una categoria',
   by_idx[57]['italian'] == by_idx[57]['english'] == 'unknown ember waste',
   (by_idx[57]['italian'], by_idx[57]['english']))

log_it = tuple(u['idx'] for u in tu if u['kind'] == 'LOGBOOK')
ck('LOGBOOK: %d righe nel lotto, %d attese' % (len(log_it), len(LOG)), log_it == LOG, log_it)
ck('LOGBOOK: nessuna riga lasciata identica all\'inglese',
   not [i for i in LOG if by_idx[i]['italian'].strip() == by_idx[i]['english'].strip()])
ck('LOGBOOK: tab del sorgente conservati',
   not [i for i in LOG if by_idx[i]['italian'].count('\t') != by_idx[i]['english'].count('\t')])
raw_by_idx = {u['idx']: u['raw'] for u in su}
f_three = tuple(i for i in LOG if re.match(r'\t+log "[^"]+" "[^"]+" `', raw_by_idx[i]))
f_back = tuple(i for i in LOG if re.match(r'\t+log `', raw_by_idx[i]))
f_quote = tuple(i for i in LOG if re.match(r'\t+log "[^"]+"\s*$', raw_by_idx[i]))
ck('LOGBOOK: forme 10 tre argomenti + 7 backtick + 0 dirette',
   (f_three, f_back, f_quote) == ((4, 5, 6, 7, 21, 22, 68, 90, 95, 109),
                                 (16, 20, 67, 89, 107, 108, 134), ()),
   (f_three, f_back, f_quote))
ck('LOGBOOK: nessuna categoria estratta (a differenza di L45-L47)',
   not [i for i in LOG if re.match(r'\t+log "[^"]+" "[^"]+"\s*$', raw_by_idx[i])])

dlg = tuple(u['idx'] for u in tu if u['kind'] == 'DIALOG')
ck('DIALOG: %d nodi, controllo positivo' % len(DIALOG), dlg == DIALOG, dlg)
ck('DIALOG: tutti con testo fra backtick e tradotti',
   all(re.match(r'\t+dialog `.+`$', raw_by_idx[i]) for i in DIALOG)
   and not [i for i in DIALOG if by_idx[i]['italian'].strip() == by_idx[i]['english'].strip()])
txt = tuple(u['idx'] for u in tu if u['kind'] == 'TEXT')
ck('TEXT: 0 unita nel segmento (assenza dichiarata)', txt == (), txt)
conv = [u for u in tu if u['kind'] == 'CONVERSATION']
ck('CONVERSATION: nessuna nel segmento (assenza dichiarata)', conv == [], conv)
br = [u['idx'] for u in su if '[' in u['english'] or ']' in u['english']]
ck('quadre: nessuna unita con [ o ] nel sorgente (assenza dichiarata)', br == [], br[:5])
pair = [u['idx'] for u in tu if '[' in u['italian'] or ']' in u['italian']]
ck('quadre: nessuna quadra nell\'italiano', pair == [], pair)
bt = [u['idx'] for u in tu if '`' in u['italian']]
ck('backtick: nessuno nell\'italiano (assenza dichiarata)', bt == [], bt)

diff = [u['idx'] for u in tu
        if collections.Counter(TAGS.findall(u['english'])) != collections.Counter(TAGS.findall(u['italian']))]
ck('nessuna unita con token diversi (parita esatta)', not diff, sorted(set(diff))[:10])
tot_en = sum(len(TAGS.findall(u['english'])) for u in su)
tot_it = sum(len(TAGS.findall(u['italian'])) for u in tu)
fam = collections.Counter(t for u in su for t in TAGS.findall(u['english']))
ck('token totali %d = %d (6 famiglie)' % (tot_it, tot_en), tot_en == tot_it and len(fam) == 6,
   (tot_it, tot_en, len(fam)))

for ch, nome in (('\t', 'tab'), ('"', 'virgolette')):
    a = sum(u['english'].count(ch) for u in su)
    b = sum(u['italian'].count(ch) for u in tu)
    ck('%s totali %d = %d' % (nome, b, a), a == b)

per_unit = [u['idx'] for u in tu if u['english'].count('\t') != u['italian'].count('\t')
            or u['english'].count('"') != u['italian'].count('"')]
ck('tab e virgolette: parita per unita (135 unita)', per_unit == [], per_unit[:10])
lead = [u['idx'] for u in tu if u['english'].startswith('\t') != u['italian'].startswith('\t')]
ntab = len([u for u in tu if u['italian'].startswith('\t')])
ck('tab iniziale presente dove il sorgente lo ha (94)', ntab == 94 and lead == [], (ntab, lead[:5]))

odd_en = sorted(u['idx'] for u in su if u['english'].count('"') % 2)
odd_it = sorted(u['idx'] for u in tu if u['italian'].count('"') % 2)
ck('virgolette dispari: nessuna nel lotto (assenza dichiarata)', odd_en == [] and odd_it == [],
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
apos = [u['idx'] for u in tu if re.search(r"\b(e|piu|perche|cosi|gia|puo|citta|verita|entita)'", u['italian'])]
ck('nessun accento sostitutivo con apostrofo', not apos, apos[:10])

bad_ratio = [u['idx'] for u in tu if u['ratio'] is None]
ck('rapporto lunghezze definito per tutte le unita', not bad_ratio, bad_ratio[:10])
rs = [u['ratio'] for u in tu if u['ratio'] is not None]
ck('rapporto dentro il gate 0,55-1,90', 0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
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

dup_en = [e for e, n in collections.Counter(u['english'] for u in su).items() if n > 1]
ck('nessuna unita duplicata in inglese (0 gruppi attesi)', dup_en == [], dup_en[:5])
seen = collections.Counter(u['italian'] for u in tu)
ck('nessuna resa italiana ripetuta fra unita diverse',
   not [k[:40] for k, n in seen.items() if n > 1],
   [k[:40] for k, n in seen.items() if n > 1])

h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
en_w = sum(len(u['english'].split()) for u in tu)
it_w = sum(len(u['italian'].split()) for u in tu)
print('parole EN %d -> IT %d · traduzione sha256[:16] %s' % (en_w, it_w, h[:16]))

print()
print('FAIL:', len(fail), '·', 'verify L52 superato' if not fail else 'verify L52 fallito')
raise SystemExit(0 if not fail else 1)
