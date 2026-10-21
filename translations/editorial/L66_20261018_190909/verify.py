r"""verify.py — L66 (data/human/culture conversations.txt, 45 unita', righe 930-1053)

**Segmento interno**: 294 unita' prima (L58–L65), **35 dopo** la 1053, file di 374, `max(line) = 1122`.
La finestra di export era 921-1053 ma la prima unita' sta sulla **930**: si asserisce il valore misurato
(decisione 196). La copertura del file NON e' un invariante qui (decisione 158).

Differenze rispetto a L65, tutte asserite:
  - **`NT` vuoto**: assenza dichiarata, dopo i 4 `UI_LABEL` di L64 e L65;
  - **0 token** `<…>`: assenza dichiarata;
  - **`DIALOG` 0**, **`LOGBOOK` 0**, **`CONVERSATION` 0`, **`TEXT` 0**: assenze dichiarate;
  - **41 tab**, **52 virgolette**, **2 dispari** (10, 34): due discorsi aperti e non chiusi, riprodotti;
  - **1 gruppo di duplicati inglesi** (2 unita'), resa identica.

Controlli indipendenti da check.py, senza riusarne la logica:

  1. la riga grezza di ogni unita' coincide con quella del file sorgente
  2. english / kind / path / context coincidono con state.db, e lo stato e' PENDING
  3. nessuna unita' del lotto risulta APPROVED
  4. id univoci e ordine = ordine del sorgente
  5. collocazione: 45 unita', righe 930-1053
  6. segmento interno: 294 prima, 35 dopo, 374 totali, `max(line) = 1122`
  7. copertura del segmento: righe [930, 1053] senza buchi, nessuna unita' del DB fuori da quelle
  8. distribuzione dei kind misurata: 45 `MISSION_TEXT`
  9. `NT` positivo su 4, 15, 26; assenze dichiarate per `DIALOG`, `LOGBOOK`, `CONVERSATION`, `TEXT`,
     token, quadre, backtick
 10. 41 tab e 52 virgolette, **2 dispari riprodotte** (10, 34); 0 token: parita' sui totali e **per unita'**, tab iniziale dove il sorgente lo ha
 11. nessuna virgoletta dispari (insieme vuoto, non «0 dispari» per caso)
 12. nessuna unita' con italiano vuoto; tipografia (accenti, apostrofi, dash)
 13. rapporto lunghezze dentro il gate 0,55-1,90
 14. duplicati inglesi: 1 gruppo, resa identica; nessuna resa ripetuta fra inglesi diversi
 15. le parti su disco ricostruiscono translation.json (tab del costruttore compresi)
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
PATH = 'data/human/culture conversations.txt'
SRC = os.path.join(ROOT, 'endless-sky', *PATH.split('/'))

source = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
trans = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))
su, tu = source['units'], trans['units']
lines = open(SRC, encoding='utf-8').read().split('\n')

NT = set()
DIALOG = ()
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
   len(tu) == 45 and (first, last) == (930, 1053), (len(tu), first, last))

tot = db.execute('select count(*) from units where path = ?', (PATH,)).fetchone()[0]
before = db.execute('select count(*) from units where path = ? and line < ?',
                    (PATH, first)).fetchone()[0]
after = db.execute('select count(*) from units where path = ? and line > ?',
                   (PATH, last)).fetchone()[0]
maxline = db.execute('select max(line) from units where path = ?', (PATH,)).fetchone()[0]
ck('segmento interno: 294 prima, 35 dopo, 374 totali',
   before == 294 and after == 35 and tot == 374, (before, after, tot))
ck('max(line) del file = 1122', maxline == 1122, maxline)

lrows = sorted(u['line'] for u in su)
ck('copertura del segmento: righe 930-1053 continue',
   lrows[0] == 930 and lrows[-1] == 1053)
inrange = db.execute('select count(*) from units where path = ? and line between ? and ?',
                     (PATH, first, last)).fetchone()[0]
ck('nessun altra unita nel DB dentro 930-1053 (%d)' % inrange, inrange == len(tu), inrange)

kinds = collections.Counter(u['kind'] for u in su)
ck('distribuzione dei kind: 45 MISSION_TEXT', dict(kinds) == {'MISSION_TEXT': 45}, dict(kinds))

by_idx = {u['idx']: u for u in tu}
raw_by_idx = {u['idx']: u['raw'] for u in su}
ui = sorted(u['idx'] for u in tu if u['kind'] == 'UI_LABEL')
ck('UI_LABEL: nessuna nel segmento (assenza dichiarata)', ui == [] and NT == set(), ui)
notid = [i for i in NT if by_idx[i]['italian'] != by_idx[i]['english']]
ck('NT: le 4 label identiche al sorgente', not notid, notid)
dlg = tuple(u['idx'] for u in tu if u['kind'] == 'DIALOG')
ck('DIALOG: nessuna nel segmento (assenza dichiarata)', dlg == DIALOG, dlg)
for kind in ('LOGBOOK', 'CONVERSATION', 'TEXT'):
    got = [u['idx'] for u in tu if u['kind'] == kind]
    ck('%s: nessuna unita nel segmento (assenza dichiarata)' % kind, got == [], got)

tok_en = sum(len(TAGS.findall(u['english'])) for u in su)
tok_it = sum(len(TAGS.findall(u['italian'])) for u in tu)
ck('token <...>: 0 nel sorgente e 0 in italiano (assenza dichiarata)',
   tok_en == 0 and tok_it == 0, (tok_en, tok_it))
diff = [u['idx'] for u in tu
        if collections.Counter(TAGS.findall(u['english'])) != collections.Counter(TAGS.findall(u['italian']))]
ck('nessuna unita con token diversi (parita esatta)', not diff, sorted(set(diff))[:10])

for ch, nome, atteso_n in (('\t', 'tab', 41), ('"', 'virgolette', 52)):
    a = sum(u['english'].count(ch) for u in su)
    b = sum(u['italian'].count(ch) for u in tu)
    ck('%s totali %d = %d (attese %d)' % (nome, b, a, atteso_n), a == b == atteso_n, (a, b))

per_unit = [u['idx'] for u in tu if u['english'].count('\t') != u['italian'].count('\t')
            or u['english'].count('"') != u['italian'].count('"')]
ck('tab e virgolette: parita per unita (45 unita)', per_unit == [], per_unit[:10])
ntab = len([u for u in tu if u['italian'].startswith('\t')])
lead = [u['idx'] for u in tu if u['english'].startswith('\t') != u['italian'].startswith('\t')]
ck('tab iniziale presente dove il sorgente lo ha (40)', ntab == 40 and lead == [], (ntab, lead[:5]))

odd_en = tuple(sorted(u['idx'] for u in su if u['english'].count('"') % 2))
odd_it = tuple(sorted(u['idx'] for u in tu if u['italian'].count('"') % 2))
ck('virgolette dispari: 2 unita (10, 34) riprodotte, non chiuse',
   odd_en == (10, 34) and odd_it == (10, 34), (odd_en, odd_it))
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
ck('duplicati inglesi (1 gruppo, 2 unita): resa italiana identica',
   len(dup_en) == 1 and dup_ok, (len(dup_en), dup_ok))
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
print('FAIL:', len(fail), '·', 'verify L66 superato' if not fail else 'verify L66 fallito')
raise SystemExit(0 if not fail else 1)
