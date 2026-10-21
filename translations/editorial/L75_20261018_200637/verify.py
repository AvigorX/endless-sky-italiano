r"""verify.py — L75 (data/successors/successor 2 ghosts aqrabe.txt, 61 unita', righe 256-400)

Verifica **indipendente** da `check.py`.

Invariante di **segmento**: il file prosegue (riga 404 apre `Aqrabe 7`), quindi si asseriscono segmento
(259-400), **89 unita' prima** (L73 + L74), **30 dopo**, `max(line)` (478) e il confine.

Misure attese, lette dal workspace il 2026-10-18:
  - 61 unita', righe 259-400, **2 contesti interi** (`Ghosts Aqrabe 5` 53 unita', `Ghosts Aqrabe 6` 8);
  - tipi: 55 `MISSION_TEXT`, 2 `VALUE`, 2 `DESCRIPTION`, 1 `DIALOG`, 1 `LOGBOOK`;
  - **virgolette dispari: insieme (5, 6, 7, 8)** — due battute spezzate a meta'; si confronta l'**insieme**,
    e si verifica anche **dove** la virgoletta chiude (unita' 6 e 8, non 5 e 7);
  - **`LOGBOOK` 1** = categoria `People` (unita' 27), identica in `NT`; il testo della stessa riga **non e'
    nel lotto** (ottavo caso della lacuna dell'estrattore);
  - **`DIALOG` 1** (15): testo, tradotto; **0** `UI_LABEL` / `CONVERSATION` / `TEXT`;
  - **8 token** in 7 famiglie: `<destination>` 2, `<origin>`/`<first>`/`<last>`/`<planet>`/`<system>`/
    `<capacity>` 1;
  - **51 tab** su **51 unita'**, **130 virgolette**, 0 quadre, 0 backtick;
  - **1 gruppo** di duplicati inglesi: 6 e 8, resa identica **voluta**.
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
PATH = 'data/successors/successor 2 ghosts aqrabe.txt'
SRC = os.path.join(ROOT, 'endless-sky', *PATH.split('/'))

source = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
trans = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))
su, tu = source['units'], trans['units']
lines = open(SRC, encoding='utf-8').read().split('\n')

NT = {27}
LOG = {27}
ODD = {5, 6, 7, 8}
CLOSERS = {6, 8}
DLG = {15}
DUP = {6, 8}
TAGS = re.compile(r'<[^<>]+>')

fail = []


def ck(name, cond, detail=''):
    print('%-68s %s %s' % (name, 'OK' if cond else 'FAIL', '' if cond else detail))
    if not cond:
        fail.append(name)


bad_raw = [u['idx'] for u in su if lines[u['line'] - 1] != u['raw']]
ck('riga grezza identica al file sorgente (61 righe)', not bad_raw, bad_raw[:10])

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
ck('idx del segmento senza buchi (1..61)', [u['idx'] for u in tu] == list(range(1, 62)))

first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 61 righe 259 - 400', len(tu) == 61 and (first, last) == (259, 400), (len(tu), first, last))

tot = db.execute('select count(*) from units where path = ?', (PATH,)).fetchone()[0]
before = db.execute('select count(*) from units where path = ? and line < ?', (PATH, first)).fetchone()[0]
after = db.execute('select count(*) from units where path = ? and line > ?', (PATH, last)).fetchone()[0]
maxline = db.execute('select max(line) from units where path = ?', (PATH,)).fetchone()[0]
ck('continua il file: 89 unita prima della riga 259 (L73 + L74)', before == 89, before)
ck('il file prosegue: 30 unita dopo la riga 400', after == 30, after)
ck('file: 180 unita totali, max(line) = 478', tot == 180 and maxline == 478, (tot, maxline))
nxt = db.execute('select line, context from units where path = ? and line > ? order by line limit 1',
                 (PATH, last)).fetchone()
ck('confine dopo: riga 404 apre Successors: Ghosts Aqrabe 7',
   nxt is not None and nxt['line'] == 404 and nxt['context'] == 'mission:Successors: Ghosts Aqrabe 7',
   tuple(nxt) if nxt else None)

lrows = sorted(u['line'] for u in su)
ck('segmento 259-400: prima/ultima riga coerenti', lrows[0] == 259 and lrows[-1] == 400, (lrows[0], lrows[-1]))
ck('nessuna riga del segmento con due unita (61 righe distinte)', len(set(lrows)) == 61 == len(lrows))
inrange = db.execute('select count(*) from units where path = ? and line between ? and ?',
                     (PATH, first, last)).fetchone()[0]
ck('nessun altra unita nel DB dentro 259-400 (%d)' % inrange, inrange == len(tu), inrange)
ctxs = []
for u in su:
    if u['context'] not in ctxs:
        ctxs.append(u['context'])
ck('2 contesti interi, in ordine di riga',
   ctxs == ['mission:Successors: Ghosts Aqrabe 5', 'mission:Successors: Ghosts Aqrabe 6'], ctxs)
c5 = db.execute("select count(*) from units where path = ? and context = 'mission:Successors: Ghosts Aqrabe 5'",
                (PATH,)).fetchone()[0]
c6 = db.execute("select count(*) from units where path = ? and context = 'mission:Successors: Ghosts Aqrabe 6'",
                (PATH,)).fetchone()[0]
ck('i due contesti sono interi: 53 + 8 unita', (c5, c6) == (53, 8), (c5, c6))

kinds = collections.Counter(u['kind'] for u in su)
ck('kind: 55 MISSION_TEXT, 2 VALUE, 2 DESCRIPTION, 1 DIALOG, 1 LOGBOOK',
   dict(kinds) == {'MISSION_TEXT': 55, 'VALUE': 2, 'DESCRIPTION': 2, 'DIALOG': 1, 'LOGBOOK': 1},
   dict(kinds))

by_idx = {u['idx']: u for u in tu}
ui = [u['idx'] for u in su if u['kind'] == 'UI_LABEL']
ck('UI_LABEL: nessuna nel segmento (assenza dichiarata)', ui == [], ui)
ck('categoria di diario 27 (`People`) lasciata identica',
   by_idx[27]['italian'] == by_idx[27]['english'] == 'People')
raw_by_idx = {u['idx']: u['raw'] for u in su}
ck('la riga `log` e a tre argomenti (categoria + nome + testo)',
   re.match(r'\t+log "People" "Tiliia" "', raw_by_idx[27]) is not None, raw_by_idx[27][:70])
ck('il testo della riga log NON e nel lotto (lacuna dichiarata)',
   'Tiliia sees their role' not in source['units'][26]['english'])
dlg = sorted(u['idx'] for u in tu if u['kind'] == 'DIALOG')
ck('DIALOG: 1 unita (15), testo tradotto', dlg == sorted(DLG)
   and by_idx[15]['italian'].strip() != by_idx[15]['english'].strip(), dlg)
conv = [u['idx'] for u in tu if u['kind'] == 'CONVERSATION']
txt = [u['idx'] for u in tu if u['kind'] == 'TEXT']
ck('CONVERSATION e TEXT: nessuna unita (assenze dichiarate)', conv == [] and txt == [], (conv, txt))
vd = sorted(u['idx'] for u in su if u['kind'] in ('VALUE', 'DESCRIPTION'))
ck('VALUE e DESCRIPTION: 2 + 2 presenti e tradotti (1, 2, 54, 55)', vd == [1, 2, 54, 55], vd)
ck('i quattro VALUE/DESCRIPTION hanno testo diverso dall inglese',
   all(by_idx[i]['italian'].strip() != by_idx[i]['english'].strip() for i in vd))

tok_en = sum(len(TAGS.findall(u['english'])) for u in su)
tok_it = sum(len(TAGS.findall(u['italian'])) for u in tu)
fam_en = collections.Counter(t for u in su for t in TAGS.findall(u['english']))
fam_it = collections.Counter(t for u in tu for t in TAGS.findall(u['italian']))
ck('token <...>: 8 in inglese e 8 in italiano, 7 famiglie',
   tok_en == 8 and tok_it == 8 and fam_en == fam_it
   and fam_en == collections.Counter({'<destination>': 2, '<origin>': 1, '<first>': 1, '<last>': 1,
                                      '<planet>': 1, '<system>': 1, '<capacity>': 1}),
   (tok_en, tok_it, dict(fam_en), dict(fam_it)))
diff = [u['idx'] for u in tu
        if collections.Counter(TAGS.findall(u['english'])) != collections.Counter(TAGS.findall(u['italian']))]
ck('nessuna unita con token diversi (parita per simbolo e per unita)', not diff, sorted(set(diff))[:10])

for ch, nome, atteso_n in (('\t', 'tab', 51), ('"', 'virgolette', 130)):
    a = sum(u['english'].count(ch) for u in su)
    b = sum(u['italian'].count(ch) for u in tu)
    ck('%s totali %d = %d (attese %d)' % (nome, b, a, atteso_n), a == b == atteso_n, (a, b))

per_unit = [u['idx'] for u in tu if u['english'].count('\t') != u['italian'].count('\t')
            or u['english'].count('"') != u['italian'].count('"')]
ck('tab e virgolette: parita per unita (61 unita)', per_unit == [], per_unit[:10])
ntab = len([u for u in tu if u['italian'].startswith('\t')])
lead = [u['idx'] for u in tu if u['english'].startswith('\t') != u['italian'].startswith('\t')]
ck('tab iniziale su 51 unita su 61', ntab == 51 and lead == [], (ntab, lead[:5]))

odd_en = tuple(sorted(u['idx'] for u in su if u['english'].count('"') % 2))
odd_it = tuple(sorted(u['idx'] for u in tu if u['italian'].count('"') % 2))
ck('virgolette dispari: insieme (5, 6, 7, 8) in inglese e in italiano',
   odd_en == tuple(sorted(ODD)) and odd_it == tuple(sorted(ODD)), (odd_en, odd_it))
closed_en = tuple(sorted(u['idx'] for u in su if u['idx'] in ODD and u['english'].rstrip().endswith('"')))
closed_it = tuple(sorted(u['idx'] for u in tu if u['idx'] in ODD and u['italian'].rstrip().endswith('"')))
ck('fra le quattro dispari, la virgoletta chiude nelle unita 6 e 8 (non 5 e 7)',
   closed_en == tuple(sorted(CLOSERS)) and closed_it == tuple(sorted(CLOSERS)), (closed_en, closed_it))
brk = [u['idx'] for u in tu if u['italian'].count('[') != u['english'].count('[')
       or u['italian'].count(']') != u['english'].count(']')]
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
apos = [u['idx'] for u in tu if re.search(r"\b(e|piu|perche|cosi|gia|puo|citta|verita|entita|percio)'", u['italian'])]
ck('nessun accento sostitutivo con apostrofo', not apos, apos[:10])

rs = [u['ratio'] for u in tu if u['ratio'] is not None]
ck('rapporto definito per tutte le unita', len(rs) == len(tu), (len(rs), len(tu)))
ck('rapporto dentro il gate 0,55-1,90', 0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
print('rapporto IT/EN: min %.2f max %.2f' % (min(rs), max(rs)))

grp = {}
for u in su:
    grp.setdefault(u['english'], []).append(u['idx'])
dups = {k: v for k, v in grp.items() if len(v) > 1}
ck('duplicati inglesi: 1 gruppo di 2 unita (6, 8: firma di Saajret)',
   len(dups) == 1 and list(dups.values())[0] == [6, 8], {k[:20]: v for k, v in dups.items()})
ck('il gruppo duplicato ha resa identica', by_idx[6]['italian'] == by_idx[8]['italian'],
   (by_idx[6]['italian'], by_idx[8]['italian']))
seen = collections.Counter(by_idx[u['idx']]['italian'] for u in tu)
other = [k[:40] for k, n in seen.items() if n > 1 and k != by_idx[6]['italian']]
ck('nessun altra resa ripetuta fra inglesi diversi', not other, other)

merged = {}
for f in sorted(glob.glob(os.path.join(HERE, 'parts', 'part*.json'))):
    for k, v in json.load(open(f, encoding='utf-8')).items():
        merged[int(k)] = v
en_by_idx = {u['idx']: u['english'] for u in su}
rebuilt = {i: '\t' * (len(en_by_idx[i]) - len(en_by_idx[i].lstrip('\t'))) + v
           for i, v in merged.items()}
ck('le parti su disco ricostruiscono translation.json (tab compresi)',
   rebuilt == {u['idx']: u['italian'] for u in tu})
ck('le parti coprono tutti gli idx, senza chiavi fuori lotto',
   sorted(merged) == list(range(1, 62)), (len(merged), sorted(merged)[:5]))

h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
en_w = sum(len(u['english'].split()) for u in tu)
it_w = sum(len(u['italian'].split()) for u in tu)
print('parole EN %d -> IT %d · traduzione sha256[:16] %s' % (en_w, it_w, h[:16]))

print()
print('FAIL:', len(fail), '·', 'verify L75 superato' if not fail else 'verify L75 fallito')
raise SystemExit(0 if not fail else 1)
