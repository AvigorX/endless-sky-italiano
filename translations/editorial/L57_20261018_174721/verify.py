r"""verify.py — L57 (data/gegno/gegno I corroboration.txt, 127 unita', righe 943-1287)

**Chiude il file**: L56 (171 unita', righe 29-904) + L57 (127 unita', righe 943-1287) = **298/298**.
La finestra di export era 905-1287: le righe 905-942 non contengono unita' (nessun `mission`, `phrase`,
`label` o `log`), quindi la prima unita' del lotto sta sulla 943.
Qui l'invariante "di file" torna legittimo (decisione 181): 0 unita' dopo la 1287, `max(line) = 1287`,
copertura 298/298 sui due lotti.

Differenze rispetto a L56, tutte asserite:
  - `NT` = **17** `UI_LABEL` (16, 18, 20, 38, 44, 60, 79, 81, 86, 91, 93, 97, 101, 112, 116, 119, 121);
  - **`DIALOG` 3** (22, 23, 125): 22 e 23 sono **identiche** (stessa scena, due esiti della missione);
  - **13 token in 6 famiglie**: `<destination>` 4, `<ship>` 3, `<first>` 2, `<last>` 2, `<origin>` 1,
    `<payment>` 1 — `<payment>` compare per la prima volta nella linea Gegno;
  - **`LOGBOOK` 0**, **`CONVERSATION` 0**, **`TEXT` 0**: assenze dichiarate;
  - **94 tab**, **60 virgolette**, **0 dispari**, **0 quadre**, **0 backtick**.
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
PATH = 'data/gegno/gegno I corroboration.txt'
SRC = os.path.join(ROOT, 'endless-sky', *PATH.split('/'))

source = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
trans = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))
su, tu = source['units'], trans['units']
lines = open(SRC, encoding='utf-8').read().split('\n')

NT = set([16, 18, 20, 38, 44, 60, 79, 81, 86, 91, 93, 97, 101, 112, 116, 119, 121])
DIALOG = (22, 23, 125)
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

first, last = tu[0]['line'], tu[-1]['line']
ck('unita: %d righe %d - %d' % (len(tu), first, last),
   len(tu) == 127 and (first, last) == (943, 1287), (len(tu), first, last))

tot = db.execute('select count(*) from units where path = ?', (PATH,)).fetchone()[0]
before = db.execute('select count(*) from units where path = ? and line < ?',
                    (PATH, first)).fetchone()[0]
after = db.execute('select count(*) from units where path = ? and line > ?',
                   (PATH, last)).fetchone()[0]
maxline = db.execute('select max(line) from units where path = ?', (PATH,)).fetchone()[0]
ck('chiude il file: 171 prima, 0 dopo, 298 totali',
   before == 171 and after == 0 and tot == 298, (before, after, tot))
ck('max(line) del file = 1287', maxline == 1287, maxline)

lrows = sorted(u['line'] for u in su)
ck('copertura del segmento: righe 943-1287 continue',
   lrows[0] == 943 and lrows[-1] == 1287)
inrange = db.execute('select count(*) from units where path = ? and line between ? and ?',
                     (PATH, 29, 1287)).fetchone()[0]
ck('copertura del file 298/298 su L56+L57 (%d)' % inrange, inrange == 298, inrange)

kinds = collections.Counter(u['kind'] for u in su)
atteso = {'MISSION_TEXT': 101, 'UI_LABEL': 17, 'DIALOG': 3, 'VALUE': 3, 'DESCRIPTION': 3}
ck('distribuzione dei kind come misurata', dict(kinds) == atteso, dict(kinds))

by_idx = {u['idx']: u for u in tu}
raw_by_idx = {u['idx']: u['raw'] for u in su}
ui = sorted(u['idx'] for u in tu if u['kind'] == 'UI_LABEL')
ck('UI_LABEL: 17 attese, tutte elencate', ui == sorted(NT), ui)
notid = [i for i in NT if by_idx[i]['italian'] != by_idx[i]['english']]
ck('NT: tutte le 17 label identiche al sorgente', not notid, notid)
ck('NT: tutte sono label di salto, nessun riferimento di dato',
   all(re.match(r'\t+label "', raw_by_idx[i]) for i in NT))

dlg = tuple(u['idx'] for u in tu if u['kind'] == 'DIALOG')
ck('DIALOG: 3 unita (22, 23, 125)', dlg == DIALOG, dlg)
ck('DIALOG: 22 e 23 sono identiche nel sorgente',
   by_idx[22]['english'] == by_idx[23]['english'])
ck('DIALOG: 22 e 23 sono identiche anche in italiano',
   by_idx[22]['italian'] == by_idx[23]['italian'])
ck('DIALOG: tutti tradotti e non lasciati in inglese',
   not [i for i in DIALOG if by_idx[i]['italian'].strip() == by_idx[i]['english'].strip()])
ck('DIALOG 22/23 = DIALOG 170/171 di L56 (stessa resa)',
   by_idx[22]['italian'] == ("Dopo aver deciso di aprire il fuoco sulla flotta Gegno che sorvegliava la tua "
                             "visita al loro mondo natale, ti trovi davanti a un'opposizione aggressiva e a "
                             "quelle che suonano come innumerevoli chiamate furiose. Qualsiasi possibilità ti "
                             "restasse di avere a che fare con i Gegno è ora svanita."))

for kind in ('LOGBOOK', 'CONVERSATION', 'TEXT'):
    got = [u['idx'] for u in tu if u['kind'] == kind]
    ck('%s: nessuna unita nel segmento (assenza dichiarata)' % kind, got == [], got)

diff = [u['idx'] for u in tu
        if collections.Counter(TAGS.findall(u['english'])) != collections.Counter(TAGS.findall(u['italian']))]
ck('nessuna unita con token diversi (parita esatta)', not diff, sorted(set(diff))[:10])
tot_en = sum(len(TAGS.findall(u['english'])) for u in su)
tot_it = sum(len(TAGS.findall(u['italian'])) for u in tu)
fam = collections.Counter(t for u in su for t in TAGS.findall(u['english']))
ck('token totali %d = %d (6 famiglie)' % (tot_it, tot_en),
   tot_en == tot_it == 13 and len(fam) == 6, (tot_it, tot_en, len(fam), dict(fam)))

for ch, nome, atteso_n in (('\t', 'tab', 94), ('"', 'virgolette', 60)):
    a = sum(u['english'].count(ch) for u in su)
    b = sum(u['italian'].count(ch) for u in tu)
    ck('%s totali %d = %d (attese %d)' % (nome, b, a, atteso_n), a == b == atteso_n, (a, b))

per_unit = [u['idx'] for u in tu if u['english'].count('\t') != u['italian'].count('\t')
            or u['english'].count('"') != u['italian'].count('"')]
ck('tab e virgolette: parita per unita (127 unita)', per_unit == [], per_unit[:10])
ntab = len([u for u in tu if u['italian'].startswith('\t')])
lead = [u['idx'] for u in tu if u['english'].startswith('\t') != u['italian'].startswith('\t')]
ck('tab iniziale presente dove il sorgente lo ha (94)', ntab == 94 and lead == [], (ntab, lead[:5]))

odd_en = tuple(sorted(u['idx'] for u in su if u['english'].count('"') % 2))
odd_it = tuple(sorted(u['idx'] for u in tu if u['italian'].count('"') % 2))
ck('virgolette dispari: nessuna nel lotto (assenza dichiarata)', odd_en == () and odd_it == (),
   (odd_en, odd_it))
brk = [u['idx'] for u in tu if '[' in u['italian'] or ']' in u['italian']]
bt = [u['idx'] for u in tu if '`' in u['italian']]
ck('quadre e backtick: nessuna nel lotto (assenza dichiarata)', brk == [] and bt == [], (brk, bt))

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

rs = [u['ratio'] for u in tu if u['ratio'] is not None]
ck('rapporto definito per tutte le unita', len(rs) == len(tu), (len(rs), len(tu)))
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
ck('duplicati inglesi (%d gruppi): resa italiana identica' % len(dup_en), len(dup_en) == 4 and dup_ok)
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
print('FAIL:', len(fail), '·', 'verify L57 superato' if not fail else 'verify L57 fallito')
raise SystemExit(0 if not fail else 1)
