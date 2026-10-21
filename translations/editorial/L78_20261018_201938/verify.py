r"""verify.py — L78 (data/successors/successor side missions.txt, 53 unita', righe 221-325)

Verifica **indipendente** da `check.py`. Invariante di **segmento**: il file prosegue (riga 336 apre
`People's Houses: First Contact`), quindi **63 prima**, **48 dopo**, `max(line) = 453`, file di 164.

Misure attese, lette dal workspace il 2026-10-18: 53 unita', righe 224-325, **1 contesto intero**
(`Stargazing 1`); tipi 49 `MISSION_TEXT` + 1 `VALUE` + 1 `DESCRIPTION` + **2 `UI_LABEL`**; **0** `LOGBOOK` /
`DIALOG` / `CONVERSATION` / `TEXT`; **0 virgolette dispari** (86); **5 gruppi di duplicati** (13/20, 15/22,
16/23, 39/41, 45/49) con resa identica; **13 token** in 7 famiglie; **46 tab** su 46 unita'.
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

NT = {47, 50}
DUPS = [frozenset([13, 20]), frozenset([15, 22]), frozenset([16, 23]), frozenset([39, 41]), frozenset([45, 49])]
TAGS = re.compile(r'<[^<>]+>')

fail = []


def ck(name, cond, detail=''):
    print('%-68s %s %s' % (name, 'OK' if cond else 'FAIL', '' if cond else detail))
    if not cond:
        fail.append(name)


ck('riga grezza identica al file sorgente (53 righe)',
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
ck('idx del segmento senza buchi (1..53)', [u['idx'] for u in tu] == list(range(1, 54)))

first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 53 righe 224 - 325', len(tu) == 53 and (first, last) == (224, 325), (len(tu), first, last))
tot = db.execute('select count(*) from units where path = ?', (PATH,)).fetchone()[0]
before = db.execute('select count(*) from units where path = ? and line < ?', (PATH, first)).fetchone()[0]
after = db.execute('select count(*) from units where path = ? and line > ?', (PATH, last)).fetchone()[0]
maxline = db.execute('select max(line) from units where path = ?', (PATH,)).fetchone()[0]
ck('continua il file: 63 unita prima della riga 224 (L77)', before == 63, before)
ck('il file prosegue: 48 unita dopo la riga 325', after == 48, after)
ck('file: 164 unita totali, max(line) = 453', tot == 164 and maxline == 453, (tot, maxline))
nxt = db.execute('select line, context from units where path = ? and line > ? order by line limit 1',
                 (PATH, last)).fetchone()
ck('confine dopo: riga 336 apre People\'s Houses: First Contact',
   nxt is not None and nxt['line'] == 336
   and nxt['context'] == "mission:Successors: People's Houses: First Contact", tuple(nxt) if nxt else None)
lrows = sorted(u['line'] for u in su)
ck('segmento 224-325: 53 righe distinte', lrows[0] == 224 and lrows[-1] == 325 and len(set(lrows)) == 53)
inrange = db.execute('select count(*) from units where path = ? and line between ? and ?',
                     (PATH, first, last)).fetchone()[0]
ck('nessun altra unita nel DB dentro 224-325', inrange == len(tu), inrange)
ctxs = []
for u in su:
    if u['context'] not in ctxs:
        ctxs.append(u['context'])
ck('1 contesto intero: Successors: Stargazing 1', ctxs == ['mission:Successors: Stargazing 1'], ctxs)
c1 = db.execute("select count(*) from units where path = ? and context = 'mission:Successors: Stargazing 1'",
                (PATH,)).fetchone()[0]
ck('il contesto e intero: 53 unita', c1 == 53, c1)

kinds = collections.Counter(u['kind'] for u in su)
ck('kind: 49 MISSION_TEXT, 1 VALUE, 1 DESCRIPTION, 2 UI_LABEL',
   dict(kinds) == {'MISSION_TEXT': 49, 'VALUE': 1, 'DESCRIPTION': 1, 'UI_LABEL': 2}, dict(kinds))
by_idx = {u['idx']: u for u in tu}
ui = sorted(u['idx'] for u in su if u['kind'] == 'UI_LABEL')
ck('UI_LABEL: 2 unita (47, 50)', ui == [47, 50], ui)
ck('le due label restano identiche',
   all(by_idx[i]['italian'] == by_idx[i]['english'] for i in NT),
   {i: by_idx[i]['italian'] for i in NT})
ck('LOGBOOK / DIALOG / CONVERSATION / TEXT: nessuna (assenze dichiarate)',
   all(not [u for u in tu if u['kind'] == k] for k in ('LOGBOOK', 'DIALOG', 'CONVERSATION', 'TEXT')))
vd = sorted(u['idx'] for u in su if u['kind'] in ('VALUE', 'DESCRIPTION'))
ck('VALUE e DESCRIPTION: 1 + 1 (1, 2), tradotti',
   vd == [1, 2] and all(by_idx[i]['italian'].strip() != by_idx[i]['english'].strip() for i in vd), vd)

tok_en = sum(len(TAGS.findall(u['english'])) for u in su)
tok_it = sum(len(TAGS.findall(u['italian'])) for u in tu)
fam_en = collections.Counter(t for u in su for t in TAGS.findall(u['english']))
fam_it = collections.Counter(t for u in tu for t in TAGS.findall(u['italian']))
want = collections.Counter({'<ship>': 4, '<home system>': 4, '<planet stopovers>': 1,
                            '<destination>': 1, '<date>': 1, '<origin>': 1, '<payment>': 1})
ck('token: 13 = 13 in 7 famiglie (`<home system>` nuovo)',
   tok_en == 13 and tok_it == 13 and fam_en == fam_it == want, (tok_en, tok_it, dict(fam_en)))
ck('nessuna unita con token diversi',
   not [u['idx'] for u in tu
        if collections.Counter(TAGS.findall(u['english'])) != collections.Counter(TAGS.findall(u['italian']))])

for ch, nome, n in (('\t', 'tab', 46), ('"', 'virgolette', 86)):
    a = sum(u['english'].count(ch) for u in su)
    b = sum(u['italian'].count(ch) for u in tu)
    ck('%s: %d = %d (attese %d)' % (nome, b, a, n), a == b == n, (a, b))
ck('tab e virgolette: parita per unita',
   not [u['idx'] for u in tu if u['english'].count('\t') != u['italian'].count('\t')
        or u['english'].count('"') != u['italian'].count('"')])
ck('tab iniziale su 46 unita su 53',
   len([u for u in tu if u['italian'].startswith('\t')]) == 46
   and not [u['idx'] for u in tu if u['english'].startswith('\t') != u['italian'].startswith('\t')])
ck('virgolette dispari: nessuna (assenza dichiarata)',
   not [u['idx'] for u in su if u['english'].count('"') % 2]
   and not [u['idx'] for u in tu if u['italian'].count('"') % 2])
ck('quadre e backtick: nessuna nel tradotto',
   not [u['idx'] for u in tu if '[' in u['italian'] or '`' in u['italian']
        or u['italian'].count('[') != u['english'].count('[')])

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
ck('duplicati inglesi: 5 gruppi attesi', len(dups), dups == set(DUPS))
ck('i cinque gruppi hanno resa identica', all(len(set(by_idx[i]['italian'] for i in g)) == 1 for g in DUPS))
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
ck('le parti coprono 1..53', sorted(merged) == list(range(1, 54)), len(merged))

h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('parole EN %d -> IT %d · sha256[:16] %s'
      % (sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu), h[:16]))
print()
print('FAIL:', len(fail), '·', 'verify L78 superato' if not fail else 'verify L78 fallito')
raise SystemExit(0 if not fail else 1)
