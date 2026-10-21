r"""verify.py — L50 (data/avgi/avgi 0 first contact.txt, 119 unita', righe 22-402)

Segmento **interno**: il file prosegue dopo la riga 402 (287 unita' restano). La copertura del file
NON e' un invariante di questo lotto: si asserisce la copertura del **segmento** (per righe) e il
numero di unita' prima e dopo.

Controlli indipendenti da check.py, senza riusarne la logica:

  1. la riga grezza di ogni unita' coincide con quella del file sorgente
  2. english / kind / path / context coincidono con state.db, e lo stato e' PENDING
  3. nessuna unita' del lotto risulta APPROVED
  4. id univoci e ordine = ordine del sorgente
  5. collocazione: 119 unita', righe 22-402
  6. **0 unita' prima della 22, 287 dopo la 402** (il lotto apre il file; 406 unita', max line 1120)
  7. copertura del segmento: le unita' del lotto coprono l'intervallo [22, 402] senza buchi
  8. distribuzione dei kind misurata: 102/7/3/2/2/2/1
  9. `NT`: **3 `UI_LABEL`** e **nessun riferimento di dato**
 10. **`LOGBOOK` 7**, tutte di testo; forme: 1 diretta, 1 fra backtick, 5 a tre argomenti
 11. **`DIALOG` 2** (43, 44) e **`TEXT` 1** (3): il `TEXT` e' la copia del contesto `phrase:` della
     unita' 2, e la traduzione **deve** essere identica (il duplicato e' nel sorgente)
 12. **0 virgolette dispari, 0 quadre, 0 backtick**: assenze dichiarate
 13. tab 96 e virgolette 118: parita' sui totali e **per unita'**
 14. token: parita' esatta (14 occorrenze, 5 famiglie)
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
PATH = 'data/avgi/avgi 0 first contact.txt'
SRC = os.path.join(ROOT, 'endless-sky', *PATH.split('/'))

source = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
trans = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))
su, tu = source['units'], trans['units']
lines = open(SRC, encoding='utf-8').read().split('\n')

NT = set([12, 89, 113])
LOG = (1, 47, 48, 49, 50, 51, 52)
DIALOG = (43, 44)
TEXT = (3,)
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
   len(tu) == 119 and (first, last) == (22, 402), (len(tu), first, last))

tot = db.execute('select count(*) from units where path = ?', (PATH,)).fetchone()[0]
before = db.execute('select count(*) from units where path = ? and line < ?',
                    (PATH, first)).fetchone()[0]
after = db.execute('select count(*) from units where path = ? and line > ?',
                   (PATH, last)).fetchone()[0]
maxline = db.execute('select max(line) from units where path = ?', (PATH,)).fetchone()[0]
ck('apre il file: 0 prima della 22, 287 dopo la 402',
   before == 0 and after == 287 and tot == 406, (before, after, tot, maxline))

lrows = sorted(u['line'] for u in su)
buchi = [x for i, x in enumerate(lrows) if i and lrows[i - 1] >= x]
ck('righe del segmento crescenti e senza ripetizioni', not buchi, buchi[:5])
ck('copertura del segmento: righe 22-402 continue',
   lrows[0] == 22 and lrows[-1] == 402 and buchi == [], (lrows[0], lrows[-1]))
dupl_lines = db.execute('select count(*) from units where path = ? and line between ? and ?',
                        (PATH, first, last)).fetchone()[0]
ck('nessuna altra unita nel DB dentro 22-402 (%d)' % dupl_lines, dupl_lines == len(tu), dupl_lines)

kinds = collections.Counter(u['kind'] for u in su)
atteso = {'MISSION_TEXT': 102, 'LOGBOOK': 7, 'UI_LABEL': 3, 'VALUE': 2, 'DESCRIPTION': 2,
          'DIALOG': 2, 'TEXT': 1}
ck('distribuzione dei kind come misurata', dict(kinds) == atteso, dict(kinds))

by_idx = {u['idx']: u for u in tu}
bad_nt = [i for i in NT if by_idx[i]['italian'] != by_idx[i]['english']]
missing_nt = [i for i in NT if i not in by_idx]
ck('NT: %d label identiche al sorgente, 0 riferimenti di dato' % len(NT),
   len(NT) == 3 and not bad_nt and not missing_nt, (bad_nt, missing_nt))
ui = sorted(u['idx'] for u in tu if u['kind'] == 'UI_LABEL')
ck('il segmento ha esattamente 3 UI_LABEL, tutte in NT', ui == sorted(NT), ui)

log_it = tuple(u['idx'] for u in tu if u['kind'] == 'LOGBOOK')
ck('LOGBOOK: %d righe nel lotto, %d attese' % (len(log_it), len(LOG)), log_it == LOG, log_it)
ck('LOGBOOK: nessuna riga lasciata identica all\'inglese',
   not [i for i in LOG if by_idx[i]['italian'].strip() == by_idx[i]['english'].strip()],
   [i for i in LOG if by_idx[i]['italian'].strip() == by_idx[i]['english'].strip()])
ck('LOGBOOK: tab del sorgente conservati',
   not [i for i in LOG if by_idx[i]['italian'].count('\t') != by_idx[i]['english'].count('\t')])
raw_by_idx = {u['idx']: u['raw'] for u in su}
f_three = tuple(i for i in LOG if re.match(r'\t+log "[^"]+" "[^"]+" `', raw_by_idx[i]))
f_back = tuple(i for i in LOG if re.match(r'\t+log `', raw_by_idx[i]))
f_quote = tuple(i for i in LOG if re.match(r'\t+log "[^"]+"\s*$', raw_by_idx[i]))
ck('LOGBOOK: forme 5+1+1 come misurate',
   (f_three, f_back, f_quote) == ((48, 49, 50, 51, 52), (47,), (1,)),
   (f_three, f_back, f_quote))
ck('LOGBOOK: nessuna categoria estratta (a differenza di L45-L47)',
   not [i for i in LOG if re.match(r'\t+log "[^"]+" "[^"]+"\s*$', raw_by_idx[i])])

dlg = tuple(u['idx'] for u in tu if u['kind'] == 'DIALOG')
ck('DIALOG: %d nodi, controllo positivo' % len(DIALOG), dlg == DIALOG, dlg)
ck('DIALOG: tutti con testo fra backtick e tradotti',
   all(re.match(r'\t+dialog `.+`$', raw_by_idx[i]) for i in DIALOG)
   and not [i for i in DIALOG if by_idx[i]['italian'].strip() == by_idx[i]['english'].strip()])
txt = tuple(u['idx'] for u in tu if u['kind'] == 'TEXT')
ck('TEXT: 1 unita dal contesto phrase, controllo positivo', txt == TEXT, txt)
ck('TEXT: e la copia esatta della unita 2 in inglese',
   by_idx[3]['english'] == by_idx[2]['english'])
ck('TEXT: e identica alla unita 2 anche in italiano (duplicato del sorgente)',
   by_idx[3]['italian'] == by_idx[2]['italian'])
ck('TEXT: contesto phrase registrato nel sorgente',
   source['units'][2]['context'].startswith('phrase:'))

conv = [u['idx'] for u in tu if u['kind'] == 'CONVERSATION']
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
ck('token totali %d = %d (5 famiglie)' % (tot_it, tot_en), tot_en == tot_it and len(fam) == 5,
   (tot_it, tot_en, len(fam)))

for ch, nome in (('\t', 'tab'), ('"', 'virgolette')):
    a = sum(u['english'].count(ch) for u in su)
    b = sum(u['italian'].count(ch) for u in tu)
    ck('%s totali %d = %d' % (nome, b, a), a == b)

per_unit = [u['idx'] for u in tu if u['english'].count('\t') != u['italian'].count('\t')
            or u['english'].count('"') != u['italian'].count('"')]
ck('tab e virgolette: parita per unita (119 unita)', per_unit == [], per_unit[:10])
lead = [u['idx'] for u in tu if u['english'].startswith('\t') != u['italian'].startswith('\t')]
ntab = len([u for u in tu if u['italian'].startswith('\t')])
ck('tab iniziale presente dove il sorgente lo ha (96)', ntab == 96 and lead == [], (ntab, lead[:5]))

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
dup_ok = all(len(set(by_idx[u['idx']]['italian'] for u in su if u['english'] == e)) == 1
             for e in dup_en)
ck('duplicati inglesi (%d gruppi): resa italiana identica' % len(dup_en), dup_ok)
nondup = [u['idx'] for u in tu if u['english'] not in dup_en]
seen = collections.Counter(by_idx[i]['italian'] for i in nondup)
ck('nessuna resa italiana ripetuta fra unita con inglese diverso',
   not [k[:40] for k, n in seen.items() if n > 1],
   [k[:40] for k, n in seen.items() if n > 1])

h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
en_w = sum(len(u['english'].split()) for u in tu)
it_w = sum(len(u['italian'].split()) for u in tu)
print('parole EN %d -> IT %d · traduzione sha256[:16] %s' % (en_w, it_w, h[:16]))

print()
print('FAIL:', len(fail), '·', 'verify L50 superato' if not fail else 'verify L50 fallito')
raise SystemExit(0 if not fail else 1)
