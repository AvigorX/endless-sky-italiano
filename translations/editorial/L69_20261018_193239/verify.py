r"""verify.py — L69 (data/successors/successor 2 ghosts myurej.txt, 31 unita', righe 114-197)

Verifica **indipendente** da `check.py`: rilegge la riga grezza dal file su disco, confronta
`english`/`kind`/`path`/`context` con `state.db` in sola lettura, ricostruisce `translation.json` dalle
parti. Nessuna funzione, costante o conteggio importato da `check.py`.

Invariante di **segmento** (decisione 166): il file prosegue — riga 215 apre
`mission:Successors: Ghosts Myurej 4` — quindi si asseriscono segmento (118-197), unita' **prima** (49,
cioe' L68) e **dopo** (131), `max(line)` del file (531) e il confine; **non** la copertura del file.

Misure attese, lette dal workspace il 2026-10-18:
  - file: 211 unita', 49 prima, **131 dopo**, `max(line) = 531`; prossima unita' riga 215 (`Myurej 4`);
  - lotto: 31 unita', righe 118-197, 4 contesti (`Myurej 2`, `3`, `3 Direct`, `3 Checking`);
  - tipi: 23 `MISSION_TEXT`, 4 `VALUE`, 4 `DESCRIPTION`; **nessun** `UI_LABEL`/`LOGBOOK`/`DIALOG`/
    `CONVERSATION`/`TEXT` (assenze dichiarate);
  - **10 token** in 4 famiglie: `<destination>` 3, `<origin>` 3, `<planet>` 2, `<ship>` 2;
  - **27 tab** su **21 unita'** con tab iniziale, **4 virgolette**, 0 dispari, 0 quadre, 0 backtick;
  - **1 gruppo** di duplicati inglesi (`Track down Riiria`, unita' 28 e 30).
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
PATH = 'data/successors/successor 2 ghosts myurej.txt'
SRC = os.path.join(ROOT, 'endless-sky', *PATH.split('/'))

source = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
trans = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))
su, tu = source['units'], trans['units']
lines = open(SRC, encoding='utf-8').read().split('\n')

NT = set()
LOG = set()
DIALOG = ()
TAGS = re.compile(r'<[^<>]+>')

fail = []


def ck(name, cond, detail=''):
    print('%-64s %s %s' % (name, 'OK' if cond else 'FAIL', '' if cond else detail))
    if not cond:
        fail.append(name)


# 1. riga grezza contro il file su disco
bad_raw = [u['idx'] for u in su if lines[u['line'] - 1] != u['raw']]
ck('riga grezza identica al file sorgente (31 righe)', not bad_raw, bad_raw[:10])

# 2. english / kind / path / context contro il database, stato PENDING
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

# 3. id univoci, ordine, segmento senza buchi
ids = [u['id'] for u in tu]
ck('id univoci in translation.json', len(ids) == len(set(ids)))
ck('ordine delle unita = ordine del sorgente', [u['idx'] for u in tu] == [u['idx'] for u in su])
ck('idx del segmento senza buchi (1..31)',
   [u['idx'] for u in tu] == list(range(1, 32)), [u['idx'] for u in tu][:5])

# 4. collocazione misurata
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 31 righe 118 - 197', len(tu) == 31 and (first, last) == (118, 197), (len(tu), first, last))

# 5. apertura/chiusura: segmento, non file
tot = db.execute('select count(*) from units where path = ?', (PATH,)).fetchone()[0]
before = db.execute('select count(*) from units where path = ? and line < ?', (PATH, first)).fetchone()[0]
after = db.execute('select count(*) from units where path = ? and line > ?', (PATH, last)).fetchone()[0]
maxline = db.execute('select max(line) from units where path = ?', (PATH,)).fetchone()[0]
ck('eredita L68: 49 unita prima della riga 118', before == 49, before)
ck('il file prosegue: 131 unita dopo la riga 197', after == 131, after)
ck('file: 211 unita totali, max(line) = 531', tot == 211 and maxline == 531, (tot, maxline))
nxt = db.execute('select line, context from units where path = ? and line > ? order by line limit 1',
                 (PATH, last)).fetchone()
ck('confine dopo: riga 215 apre Successors: Ghosts Myurej 4',
   nxt is not None and nxt['line'] == 215 and nxt['context'] == 'mission:Successors: Ghosts Myurej 4',
   tuple(nxt) if nxt else None)

# 6. copertura del segmento senza buchi
lrows = sorted(u['line'] for u in su)
ck('segmento 118-197: prima/ultima riga coerenti', lrows[0] == 118 and lrows[-1] == 197, (lrows[0], lrows[-1]))
ck('nessuna riga del segmento con due unita (31 righe distinte)',
   len(set(lrows)) == 31 == len(lrows), len(set(lrows)))
inrange = db.execute('select count(*) from units where path = ? and line between ? and ?',
                     (PATH, first, last)).fetchone()[0]
ck('nessun altra unita nel DB dentro 118-197 (%d)' % inrange, inrange == len(tu), inrange)
ctxs = []
for u in su:
    if u['context'] not in ctxs:
        ctxs.append(u['context'])
ck('4 contesti, in ordine di riga',
   ctxs == ['mission:Successors: Ghosts Myurej 2', 'mission:Successors: Ghosts Myurej 3',
            'mission:Successors: Ghosts Myurej 3 Direct', 'mission:Successors: Ghosts Myurej 3 Checking'],
   ctxs)

# 7. distribuzione dei kind
kinds = collections.Counter(u['kind'] for u in su)
ck('kind: 23 MISSION_TEXT, 4 VALUE, 4 DESCRIPTION',
   dict(kinds) == {'MISSION_TEXT': 23, 'VALUE': 4, 'DESCRIPTION': 4}, dict(kinds))

# 8. assenze dichiarate e controlli positivi
by_idx = {u['idx']: u for u in tu}
ui = sorted(u['idx'] for u in su if u['kind'] == 'UI_LABEL')
ck('UI_LABEL: nessuna nel segmento (assenza dichiarata)', ui == [] and NT == set(), ui)
dlg = tuple(u['idx'] for u in tu if u['kind'] == 'DIALOG')
ck('DIALOG: nessuna nel segmento (assenza dichiarata)', dlg == DIALOG, dlg)
log_units = sorted(u['idx'] for u in tu if u['kind'] == 'LOGBOOK')
ck('LOGBOOK: nessuna nel segmento (assenza dichiarata)', log_units == [] and LOG == set(), log_units)
for kind in ('CONVERSATION', 'TEXT'):
    got = [u['idx'] for u in tu if u['kind'] == kind]
    ck('%s: nessuna unita nel segmento (assenza dichiarata)' % kind, got == [], got)
vd = sorted(u['idx'] for u in su if u['kind'] in ('VALUE', 'DESCRIPTION'))
ck('VALUE e DESCRIPTION: 8 unita presenti e tradotte', vd == [1, 2, 10, 11, 28, 29, 30, 31], vd)
ck('nessuna unita VALUE rimasta identica all inglese',
   all(by_idx[i]['italian'] != by_idx[i]['english'] for i in vd
       if by_idx[i]['kind'] == 'VALUE'), [i for i in vd if by_idx[i]['kind'] == 'VALUE'
                                          and by_idx[i]['italian'] == by_idx[i]['english']])

# 9. tab / virgolette / token / dispari
tok_en = sum(len(TAGS.findall(u['english'])) for u in su)
tok_it = sum(len(TAGS.findall(u['italian'])) for u in tu)
fam_en = collections.Counter(t for u in su for t in TAGS.findall(u['english']))
fam_it = collections.Counter(t for u in tu for t in TAGS.findall(u['italian']))
ck('token <...>: 10 in inglese e 10 in italiano, 4 famiglie (%s)' % dict(fam_en),
   tok_en == 10 and tok_it == 10 and fam_en == fam_it
   and fam_en == collections.Counter({'<destination>': 3, '<origin>': 3, '<planet>': 2, '<ship>': 2}),
   (tok_en, tok_it, dict(fam_en), dict(fam_it)))
diff = [u['idx'] for u in tu
        if collections.Counter(TAGS.findall(u['english'])) != collections.Counter(TAGS.findall(u['italian']))]
ck('nessuna unita con token diversi (parita per simbolo e per unita)', not diff, sorted(set(diff))[:10])

for ch, nome, atteso_n in (('\t', 'tab', 27), ('"', 'virgolette', 4)):
    a = sum(u['english'].count(ch) for u in su)
    b = sum(u['italian'].count(ch) for u in tu)
    ck('%s totali %d = %d (attese %d)' % (nome, b, a, atteso_n), a == b == atteso_n, (a, b))

per_unit = [u['idx'] for u in tu if u['english'].count('\t') != u['italian'].count('\t')
            or u['english'].count('"') != u['italian'].count('"')]
ck('tab e virgolette: parita per unita (31 unita)', per_unit == [], per_unit[:10])
ntab = len([u for u in tu if u['italian'].startswith('\t')])
lead = [u['idx'] for u in tu if u['english'].startswith('\t') != u['italian'].startswith('\t')]
ck('tab iniziale presente dove il sorgente lo ha (21 unita)', ntab == 21 and lead == [], (ntab, lead[:5]))
ck('10 unita senza tab iniziale (4 nomi, 4 descrizioni, 2 testi)', 
   len([u for u in tu if not u['italian'].startswith('\t')]) == 10,
   len([u for u in tu if not u['italian'].startswith('\t')]))
ck('6 unita con due tab (le scelte di dialogo indentate)',
   len([u for u in tu if u['italian'].startswith('\t\t')]) == 6,
   len([u for u in tu if u['italian'].startswith('\t\t')]))

odd_en = tuple(sorted(u['idx'] for u in su if u['english'].count('"') % 2))
odd_it = tuple(sorted(u['idx'] for u in tu if u['italian'].count('"') % 2))
ck('virgolette dispari: nessuna nel lotto (assenza dichiarata)', odd_en == () and odd_it == (),
   (odd_en, odd_it))
brk = [u['idx'] for u in tu if u['italian'].count('[') != u['english'].count('[')
       or u['italian'].count(']') != u['english'].count(']')]
bt = [u['idx'] for u in tu if '`' in u['italian']]
ck('quadre e backtick: nessuna nel lotto (assenza dichiarata)', brk == [] and bt == [], (brk, bt))

# 10. tipografia e caratteri non latini
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

# 11. rapporto
rs = [u['ratio'] for u in tu if u['ratio'] is not None]
ck('rapporto definito per tutte le unita', len(rs) == len(tu), (len(rs), len(tu)))
ck('rapporto dentro il gate 0,55-1,90', 0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
print('rapporto IT/EN: min %.2f max %.2f' % (min(rs), max(rs)))

# 12. duplicati
dup_en = [e for e, n in collections.Counter(u['english'] for u in su).items() if n > 1]
dup_ok = all(len(set(by_idx[u['idx']]['italian'] for u in su if u['english'] == e)) == 1
             for e in dup_en)
ck('duplicati inglesi: 1 gruppo (Track down Riiria), resa identica',
   len(dup_en) == 1 and dup_en[0] == 'Track down Riiria' and dup_ok, (len(dup_en), dup_ok))
nondup = [u['idx'] for u in tu if u['english'] not in dup_en]
seen = collections.Counter(by_idx[i]['italian'] for i in nondup)
ck('nessuna resa italiana ripetuta fra unita con inglese diverso',
   not [k[:40] for k, n in seen.items() if n > 1], [k[:40] for k, n in seen.items() if n > 1])

# 13. ricostruzione dalle parti
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
   sorted(merged) == list(range(1, 32)), (len(merged), sorted(merged)[:5]))

h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
en_w = sum(len(u['english'].split()) for u in tu)
it_w = sum(len(u['italian'].split()) for u in tu)
print('parole EN %d -> IT %d · traduzione sha256[:16] %s' % (en_w, it_w, h[:16]))

print()
print('FAIL:', len(fail), '·', 'verify L69 superato' if not fail else 'verify L69 fallito')
raise SystemExit(0 if not fail else 1)
