r"""verify.py — L68 (data/successors/successor 2 ghosts myurej.txt, 49 unita', righe 16-113)

Verifica **indipendente** da `check.py`: rilegge la riga grezza dal file su disco, confronta
`english`/`kind`/`path`/`context` con `state.db` in sola lettura, ricostruisce `translation.json`
dalle parti. Nessuna funzione, nessuna costante di controllo e nessun conteggio e' importato da
`check.py`.

Invariante di **segmento**, non di file (decisione 166): il file prosegue oltre il lotto — riga 118
apre `mission:Successors: Ghosts Myurej 2` — quindi si asserisce il **segmento** (16-113), il numero
di unita' che restano **dopo** la 113 e la `max(line)` del file; **non** la copertura del file.

Misure attese, lette dal workspace il 2026-10-18 (rigenerate con `state.db` in sola lettura):
  - file: 211 unita' totali, 0 prima della riga 16, **162 dopo** la 113, `max(line) = 531`;
  - lotto: 49 unita', righe 16-113, un solo contesto `Successors: Ghosts Myurej 1`;
  - tipi: 44 `MISSION_TEXT`, 1 `VALUE`, 1 `DESCRIPTION`, 1 `UI_LABEL`, 2 `LOGBOOK`;
  - **non traducibili 2**: unita' 20 (`label "follow up"`, bersaglio di salto) e unita' 23
    (categoria di diario `People` emersa da un `log` a tre argomenti fra virgolette: resta identica
    perche' le altre categorie dello stesso file non sono inventariate);
  - **`LOGBOOK` 2** con forme diverse: 1 a tre argomenti fra virgolette (unita' 23, **categoria**;
    il testo di quella voce resta fuori inventario: lacuna dichiarata) + 1 diretta (unita' 24, testo);
  - **10 token** in 5 famiglie: `<first>` 3, `<last>` 3, `<ship>` 2, `<destination>` 1, `<planet>` 1;
  - **42 tab**, **90 virgolette**, **0 dispari**, **0 quadre**, **0 backtick**;
  - **2 gruppi di duplicati inglesi** (15/21, 16/22): stesse battute di scelta nei due rami.
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

NT = {20, 23}
NT_LABEL = {20}
LOG = {23, 24}
LOG_CAT = {23}
DIALOG = ()
TAGS = re.compile(r'<[^<>]+>')

fail = []


def ck(name, cond, detail=''):
    print('%-64s %s %s' % (name, 'OK' if cond else 'FAIL', '' if cond else detail))
    if not cond:
        fail.append(name)


# 1. la riga grezza dell'inventario esiste davvero nel file su disco
bad_raw = [u['idx'] for u in su if lines[u['line'] - 1] != u['raw']]
ck('riga grezza identica al file sorgente (49 righe)', not bad_raw, bad_raw[:10])

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

# 3. id univoci e ordine uguale al sorgente
ids = [u['id'] for u in tu]
ck('id univoci in translation.json', len(ids) == len(set(ids)))
ck('ordine delle unita = ordine del sorgente', [u['idx'] for u in tu] == [u['idx'] for u in su])
ck('idx del segmento senza buchi (1..49)',
   [u['idx'] for u in tu] == list(range(1, 50)), [u['idx'] for u in tu][:5])

# 4. collocazione misurata
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 49 righe 16 - 113', len(tu) == 49 and (first, last) == (16, 113), (len(tu), first, last))

# 5. apertura/chiusura: segmento, non file
tot = db.execute('select count(*) from units where path = ?', (PATH,)).fetchone()[0]
before = db.execute('select count(*) from units where path = ? and line < ?',
                    (PATH, first)).fetchone()[0]
after = db.execute('select count(*) from units where path = ? and line > ?',
                   (PATH, last)).fetchone()[0]
maxline = db.execute('select max(line) from units where path = ?', (PATH,)).fetchone()[0]
ck('apre il file: 0 unita prima della riga 16', before == 0, before)
ck('il file prosegue: 162 unita dopo la riga 113', after == 162, after)
ck('file: 211 unita totali, max(line) = 531', tot == 211 and maxline == 531, (tot, maxline))
nxt = db.execute('select line, context from units where path = ? and line > ? order by line limit 1',
                 (PATH, last)).fetchone()
ck('confine dopo: riga 118 apre Successors: Ghosts Myurej 2',
   nxt is not None and nxt['line'] == 118 and nxt['context'] == 'mission:Successors: Ghosts Myurej 2',
   tuple(nxt) if nxt else None)

# 6. copertura del segmento senza buchi
lrows = sorted(u['line'] for u in su)
ck('segmento 16-113: prima/ultima riga coerenti', lrows[0] == 16 and lrows[-1] == 113, (lrows[0], lrows[-1]))
ck('nessuna riga del segmento con due unita (49 righe distinte)',
   len(set(lrows)) == 49 == len(lrows), len(set(lrows)))
inrange = db.execute('select count(*) from units where path = ? and line between ? and ?',
                     (PATH, first, last)).fetchone()[0]
ck('nessun altra unita nel DB dentro 16-113 (%d)' % inrange, inrange == len(tu), inrange)

# 7. distribuzione dei kind
kinds = collections.Counter(u['kind'] for u in su)
ck('kind: 44 MISSION_TEXT, 1 VALUE, 1 DESCRIPTION, 1 UI_LABEL, 2 LOGBOOK',
   dict(kinds) == {'MISSION_TEXT': 44, 'VALUE': 1, 'DESCRIPTION': 1, 'UI_LABEL': 1, 'LOGBOOK': 2},
   dict(kinds))

# 8. non traducibili, LOGBOOK, DIALOG, TEXT, CONVERSATION
by_idx = {u['idx']: u for u in tu}
ui = sorted(u['idx'] for u in su if u['kind'] == 'UI_LABEL')
ck('UI_LABEL: una sola, unita 20', ui == [20], ui)
notid = [i for i in NT if by_idx[i]['italian'] != by_idx[i]['english']]
ck('NT (20 label, 23 categoria): identiche al sorgente', notid == [], notid)
ck('la label 20 e un bersaglio di salto: resta `follow up`',
   by_idx[20]['italian'] == 'follow up' == by_idx[20]['english'])
cat = sorted(i for i in LOG_CAT)
ck('categoria di diario: unita 23 = `People`, identica', cat == [23] and by_idx[23]['italian'] == 'People',
   (cat, by_idx[23]['italian']))
dlg = tuple(u['idx'] for u in tu if u['kind'] == 'DIALOG')
ck('DIALOG: nessuna nel segmento (assenza dichiarata)', dlg == DIALOG, dlg)
log_units = sorted(u['idx'] for u in tu if u['kind'] == 'LOGBOOK')
ck('LOGBOOK: 2 unita (23 categoria, 24 testo)', log_units == sorted(LOG) == [23, 24], log_units)
ck('LOGBOOK testo (24) tradotto, non lasciato in inglese',
   by_idx[24]['italian'].strip() != by_idx[24]['english'].strip()
   and len(by_idx[24]['italian'].split()) >= 15, by_idx[24]['italian'][:60])
for kind in ('CONVERSATION', 'TEXT'):
    got = [u['idx'] for u in tu if u['kind'] == kind]
    ck('%s: nessuna unita nel segmento (assenza dichiarata)' % kind, got == [], got)
vd = sorted(u['idx'] for u in su if u['kind'] in ('VALUE', 'DESCRIPTION'))
ck('VALUE (1) e DESCRIPTION (2) presenti e tradotti', vd == [1, 2], vd)

# 9. tab / virgolette / token / dispari
tok_en = sum(len(TAGS.findall(u['english'])) for u in su)
tok_it = sum(len(TAGS.findall(u['italian'])) for u in tu)
fam_en = collections.Counter(t for u in su for t in TAGS.findall(u['english']))
fam_it = collections.Counter(t for u in tu for t in TAGS.findall(u['italian']))
ck('token <...>: 10 in inglese e 10 in italiano, 5 famiglie (%s)' % dict(fam_en),
   tok_en == 10 and tok_it == 10 and fam_en == fam_it
   and fam_en == collections.Counter({'<first>': 3, '<last>': 3, '<ship>': 2,
                                      '<destination>': 1, '<planet>': 1}),
   (tok_en, tok_it, dict(fam_en), dict(fam_it)))
diff = [u['idx'] for u in tu
        if collections.Counter(TAGS.findall(u['english'])) != collections.Counter(TAGS.findall(u['italian']))]
ck('nessuna unita con token diversi (parita per simbolo e per unita)', not diff, sorted(set(diff))[:10])

for ch, nome, atteso_n in (('\t', 'tab', 42), ('"', 'virgolette', 90)):
    a = sum(u['english'].count(ch) for u in su)
    b = sum(u['italian'].count(ch) for u in tu)
    ck('%s totali %d = %d (attese %d)' % (nome, b, a, atteso_n), a == b == atteso_n, (a, b))

per_unit = [u['idx'] for u in tu if u['english'].count('\t') != u['italian'].count('\t')
            or u['english'].count('"') != u['italian'].count('"')]
ck('tab e virgolette: parita per unita (49 unita)', per_unit == [], per_unit[:10])
ntab = len([u for u in tu if u['italian'].startswith('\t')])
lead = [u['idx'] for u in tu if u['english'].startswith('\t') != u['italian'].startswith('\t')]
ck('tab iniziale presente dove il sorgente lo ha (42)', ntab == 42 and lead == [], (ntab, lead[:5]))
ck('7 unita senza tab iniziale (nome, descrizione, label e 3 testi non indentati)',
   len([u for u in tu if not u['italian'].startswith('\t')]) == 7,
   len([u for u in tu if not u['italian'].startswith('\t')]))

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
ck('duplicati inglesi: 2 gruppi, resa identica dentro il gruppo',
   len(dup_en) == 2 and dup_ok, (len(dup_en), dup_ok))
nondup = [u['idx'] for u in tu if u['english'] not in dup_en]
seen = collections.Counter(by_idx[i]['italian'] for i in nondup)
ck('nessuna resa italiana ripetuta fra unita con inglese diverso',
   not [k[:40] for k, n in seen.items() if n > 1], [k[:40] for k, n in seen.items() if n > 1])

# 13. ricostruzione di translation.json dalle parti (tab del costruttore compresi)
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
   sorted(merged) == list(range(1, 50)), (len(merged), sorted(merged)[:5]))

h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
en_w = sum(len(u['english'].split()) for u in tu)
it_w = sum(len(u['italian'].split()) for u in tu)
print('parole EN %d -> IT %d · traduzione sha256[:16] %s' % (en_w, it_w, h[:16]))

print()
print('FAIL:', len(fail), '·', 'verify L68 superato' if not fail else 'verify L68 fallito')
raise SystemExit(0 if not fail else 1)
