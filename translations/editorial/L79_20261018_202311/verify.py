r"""verify.py — L79 (data/successors/successor side missions.txt, 29 unita', righe 326-400)

Verifica **indipendente** da `check.py`. Invariante di **segmento**: il file prosegue (riga 416 apre
`Unified Defense`), quindi **116 prima**, **19 dopo**, `max(line) = 453`, file di 164.

Misure attese, lette dal workspace il 2026-10-18: 29 unita', righe 336-381, **1 contesto intero**
(`People's Houses: First Contact`); **tutte `MISSION_TEXT`**; **3 virgolette dispari (10, 22, 27)** che
aprono e non chiudono; **0 token**; **3 gruppi di duplicati** (22/27, 23/28, 18/24/29); **28 tab** su 28
unita'; **33 virgolette**.
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
PATH = 'data/successors/successor side missions.txt'
SRC = os.path.join(ROOT, 'endless-sky', *PATH.split('/'))

source = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
trans = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))
su, tu = source['units'], trans['units']
lines = open(SRC, encoding='utf-8').read().split('\n')

ODD = (10, 22, 27)
DUPS = [frozenset([22, 27]), frozenset([23, 28]), frozenset([18, 24, 29])]
TAGS = re.compile(r'<[^<>]+>')

fail = []


def ck(name, cond, detail=''):
    print('%-66s %s %s' % (name, 'OK' if cond else 'FAIL', '' if cond else detail))
    if not cond:
        fail.append(name)


ck('riga grezza identica al file sorgente (29 righe)',
   not [u['idx'] for u in su if lines[u['line'] - 1] != u['raw']])

db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
db.row_factory = sqlite3.Row
bad_db, bad_state, appr = [], [], []
for u in su:
    row = db.execute('select english, kind, path, context, state from units where id = ?', (u['id'],)).fetchone()
    if row is None or row['english'] != u['english'] or row['kind'] != u['kind'] \
            or row['path'] != u['path'] or row['context'] != u['context']:
        bad_db.append(u['idx'])
    elif row['state'] == 'APPROVED':
        appr.append(u['idx'])
    elif row['state'] != 'PENDING':
        bad_state.append((u['idx'], row['state']))
ck('english/kind/path/context identici al DB', not bad_db, bad_db[:8])
ck('state = PENDING per tutte le unita', not bad_state, bad_state[:5])
ck('nessuna unita del lotto e APPROVED nel DB', not appr, appr[:5])
ck('id univoci e ordine = sorgente',
   len(set(u['id'] for u in tu)) == len(tu) and [u['idx'] for u in tu] == [u['idx'] for u in su])
ck('idx del segmento senza buchi (1..29)', [u['idx'] for u in tu] == list(range(1, 30)))

first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 29 righe 336 - 381', len(tu) == 29 and (first, last) == (336, 381), (len(tu), first, last))
tot = db.execute('select count(*) from units where path = ?', (PATH,)).fetchone()[0]
before = db.execute('select count(*) from units where path = ? and line < ?', (PATH, first)).fetchone()[0]
after = db.execute('select count(*) from units where path = ? and line > ?', (PATH, last)).fetchone()[0]
maxline = db.execute('select max(line) from units where path = ?', (PATH,)).fetchone()[0]
ck('continua il file: 116 unita prima della riga 336 (L77 + L78)', before == 116, before)
ck('il file prosegue: 19 unita dopo la riga 381', after == 19, after)
ck('file: 164 unita totali, max(line) = 453', tot == 164 and maxline == 453, (tot, maxline))
nxt = db.execute('select line, context from units where path = ? and line > ? order by line limit 1',
                 (PATH, last)).fetchone()
ck('confine dopo: riga 416 apre Successors: Unified Defense',
   nxt is not None and nxt['line'] == 416 and nxt['context'] == 'mission:Successors: Unified Defense',
   tuple(nxt) if nxt else None)
lrows = sorted(u['line'] for u in su)
ck('segmento 336-381: 29 righe distinte',
   lrows[0] == 336 and lrows[-1] == 381 and len(set(lrows)) == 29, (lrows[0], lrows[-1]))
inrange = db.execute('select count(*) from units where path = ? and line between ? and ?',
                     (PATH, first, last)).fetchone()[0]
ck('nessun altra unita nel DB dentro 336-381', inrange == len(tu), inrange)
ctxs = []
for u in su:
    if u['context'] not in ctxs:
        ctxs.append(u['context'])
ck('1 contesto intero: People\'s Houses: First Contact',
   ctxs == ["mission:Successors: People's Houses: First Contact"], ctxs)
c1 = db.execute("select count(*) from units where path = ? and context = ?",
                (PATH, "mission:Successors: People's Houses: First Contact")).fetchone()[0]
ck('il contesto e intero: 29 unita', c1 == 29, c1)

kinds = collections.Counter(u['kind'] for u in su)
ck('kind: 29 MISSION_TEXT, nessun altro tipo',
   dict(kinds) == {'MISSION_TEXT': 29}, dict(kinds))
by_idx = {u['idx']: u for u in tu}
ck('VALUE / DESCRIPTION / UI_LABEL / LOGBOOK / DIALOG / CONVERSATION / TEXT: nessuna (7 assenze)',
   all(not [u for u in tu if u['kind'] == k]
       for k in ('VALUE', 'DESCRIPTION', 'UI_LABEL', 'LOGBOOK', 'DIALOG', 'CONVERSATION', 'TEXT')))

tok_en = sum(len(TAGS.findall(u['english'])) for u in su)
tok_it = sum(len(TAGS.findall(u['italian'])) for u in tu)
ck('token <...>: 0 in inglese e 0 in italiano (assenza asserita)', (tok_en, tok_it),
   tok_en == 0 and tok_it == 0)
for ch, nome, n in (('\t', 'tab', 28), ('"', 'virgolette', 33)):
    a = sum(u['english'].count(ch) for u in su)
    b = sum(u['italian'].count(ch) for u in tu)
    ck('%s: %d = %d (attese %d)' % (nome, b, a, n), a == b == n, (a, b))
ck('tab e virgolette: parita per unita',
   not [u['idx'] for u in tu if u['english'].count('\t') != u['italian'].count('\t')
        or u['english'].count('"') != u['italian'].count('"')])

odd_en = tuple(sorted(u['idx'] for u in su if u['english'].count('"') % 2))
odd_it = tuple(sorted(u['idx'] for u in tu if u['italian'].count('"') % 2))
ck('virgolette dispari: insieme (10, 22, 27) in inglese e in italiano',
   odd_en == ODD and odd_it == ODD, (odd_en, odd_it))
ck('le tre dispari aprono e NON chiudono',
   all(by_idx[i]['italian'].lstrip('\t').startswith('"')
       and not by_idx[i]['italian'].rstrip().endswith('"') for i in ODD))
ck('le altre unita con virgolette sono bilanciate',
   all(u['italian'].count('"') % 2 == 0 for u in tu if u['idx'] not in ODD))
ck('quadre e backtick: nessuna nel tradotto',
   not [u['idx'] for u in tu if '[' in u['italian'] or '`' in u['italian']])

ck('nessuna unita con italiano vuoto', all(u['italian'].strip() for u in tu))
NONLAT = re.compile(r'[^\x00-\x7F\u00C0-\u024F\u2018\u2019\u201C\u201D\u2013\u2014\u2026]')
ck('nessun carattere non latino sospetto', not [u for u in tu if NONLAT.search(u['italian'])])
ck('nessun trattino lungo/en-dash',
   not [u['idx'] for u in tu if '\u2014' in u['italian'] or '\u2013' in u['italian']])
ck('nessuna virgoletta curva',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2018\u2019\u201C\u201D')])
ck('nessun accento sostitutivo con apostrofo',
   not [u['idx'] for u in tu
        if re.search(r"\b(e|piu|perche|cosi|gia|puo|citta|verita|entita|percio)'", u['italian'])])

rs = [u['ratio'] for u in tu if u['ratio'] is not None]
ck('rapporto dentro il gate 0,55-1,90', len(rs) == len(tu) and 0.55 < min(rs) and max(rs) < 1.90,
   (min(rs), max(rs)))
print('rapporto IT/EN: min %.2f max %.2f' % (min(rs), max(rs)))

grp = {}
for u in su:
    grp.setdefault(u['english'], []).append(u['idx'])
dups = set(frozenset(v) for v in grp.values() if len(v) > 1)
ck('duplicati inglesi: 3 gruppi attesi', len(dups), dups == set(DUPS))
ck('i tre gruppi hanno resa identica', all(len(set(by_idx[i]['italian'] for i in g)) == 1 for g in DUPS))
seen = collections.Counter(by_idx[u['idx']]['italian'] for u in tu)
free = [k[:40] for k, n in seen.items() if n > 1 and not any(k == by_idx[i]['italian'] for g in DUPS for i in g)]
ck('nessun altra resa ripetuta fra inglesi diversi', not free, free)

merged = {}
for f in sorted(glob.glob(os.path.join(HERE, 'parts', 'part*.json'))):
    for k, v in json.load(open(f, encoding='utf-8')).items():
        merged[int(k)] = v
en_by_idx = {u['idx']: u['english'] for u in su}
ck('le parti ricostruiscono translation.json (tab compresi)',
   {i: '\t' * (len(en_by_idx[i]) - len(en_by_idx[i].lstrip('\t'))) + v for i, v in merged.items()}
   == {u['idx']: u['italian'] for u in tu})
ck('le parti coprono 1..29', sorted(merged) == list(range(1, 30)), len(merged))

h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('parole EN %d -> IT %d · sha256[:16] %s'
      % (sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu), h[:16]))
print()
print('FAIL:', len(fail), '·', 'verify L79 superato' if not fail else 'verify L79 fallito')
raise SystemExit(0 if not fail else 1)
