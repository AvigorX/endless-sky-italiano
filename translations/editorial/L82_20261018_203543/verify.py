r"""verify.py — L82 (data/successors/predecessors.txt, 15 unita', righe 201-400)

Verifica **indipendente** da `check.py`. Invariante di **segmento**: **22 prima** (L81), **22 dopo**,
`max(line) = 782`, file di **59 unita'**, confine alla riga 446 (`outfit:"Torji," Lethal Sight`).

Misure attese: 15 unita', righe 208-381; **8 `TEXT` + 5 `DESCRIPTION` + 2 `VALUE`**; **10 unita' di dato**
identiche, **5 di prosa** tradotte; **1 tab** (unita' 2); **8 virgolette**, 0 dispari; **0 token**;
**0 duplicati**.
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
PATH = 'data/successors/predecessors.txt'
SRC = os.path.join(ROOT, 'endless-sky', *PATH.split('/'))
source = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
trans = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))
su, tu = source['units'], trans['units']
lines = open(SRC, encoding='utf-8').read().split('\n')

DATA = {3, 4, 5, 6, 7, 8, 9, 10, 11, 14}
PROSE = {1, 2, 12, 13, 15}
TAGS = re.compile(r'<[^<>]+>')
fail = []


def ck(name, cond, detail=''):
    print('%-68s %s %s' % (name, 'OK' if cond else 'FAIL', '' if cond else detail))
    if not cond:
        fail.append(name)


ck('riga grezza identica al file sorgente (15 righe)',
   not [u['idx'] for u in su if lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
db.row_factory = sqlite3.Row
bad_db, appr, bad_state = [], [], []
for u in su:
    row = db.execute('select english,kind,path,context,state from units where id=?', (u['id'],)).fetchone()
    if row is None or row['english'] != u['english'] or row['kind'] != u['kind'] \
            or row['path'] != u['path'] or row['context'] != u['context']:
        bad_db.append(u['idx'])
    elif row['state'] == 'APPROVED':
        appr.append(u['idx'])
    elif row['state'] != 'PENDING':
        bad_state.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad_db, bad_db[:6])
ck('state = PENDING per tutte le unita', not bad_state, bad_state[:5])
ck('nessuna unita del lotto e APPROVED', not appr, appr[:5])
ck('id univoci e ordine = sorgente',
   len(set(u['id'] for u in tu)) == len(tu) and [u['idx'] for u in tu] == [u['idx'] for u in su])
ck('idx senza buchi (1..15)', [u['idx'] for u in tu] == list(range(1, 16)))

first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 15 righe 208 - 381', len(tu) == 15 and (first, last) == (208, 381), (len(tu), first, last))
tot = db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0]
before = db.execute('select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0]
after = db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0]
maxline = db.execute('select max(line) from units where path=?', (PATH,)).fetchone()[0]
ck('continua il file: 22 unita prima della riga 208 (L81)', before == 22, before)
ck('il file prosegue: 22 unita dopo la riga 381', after == 22, after)
ck('file: 59 unita totali, max(line) = 782', tot == 59 and maxline == 782, (tot, maxline))
nxt = db.execute('select line,context from units where path=? and line>? order by line limit 1',
                 (PATH, last)).fetchone()
ck('confine dopo: riga 446 apre outfit:"Torji," Lethal Sight',
   nxt is not None and nxt['line'] == 446 and nxt['context'] == 'outfit:"Torji," Lethal Sight',
   tuple(nxt) if nxt else None)
inrange = db.execute('select count(*) from units where path=? and line between ? and ?',
                     (PATH, first, last)).fetchone()[0]
ck('nessun altra unita nel DB dentro 208-381', inrange == len(tu), inrange)
ctxs = []
for u in su:
    if u['context'] not in ctxs:
        ctxs.append(u['context'])
ck('4 contesti, in ordine di riga',
   ctxs == ['ship:Hasur, Vowsworn', 'ship:Queru, Luminous Gaze',
            'outfit:"Iasa," Lethal Word', 'outfit:"Kis," Lethal Wish'], ctxs)

kinds = collections.Counter(u['kind'] for u in su)
ck('kind: 8 TEXT, 5 DESCRIPTION, 2 VALUE',
   dict(kinds) == {'TEXT': 8, 'DESCRIPTION': 5, 'VALUE': 2}, dict(kinds))
ck('MISSION_TEXT/UI_LABEL/LOGBOOK/DIALOG/CONVERSATION: nessuna (5 assenze)',
   all(not [u for u in tu if u['kind'] == k]
       for k in ('MISSION_TEXT', 'UI_LABEL', 'LOGBOOK', 'DIALOG', 'CONVERSATION')))
by_idx = {u['idx']: u for u in tu}
ck('le 10 unita di dato restano identiche',
   all(by_idx[i]['italian'] == by_idx[i]['english'] for i in DATA),
   [i for i in sorted(DATA) if by_idx[i]['italian'] != by_idx[i]['english']])
ck('le 5 unita di prosa sono tradotte',
   all(by_idx[i]['italian'].strip() != by_idx[i]['english'].strip() for i in PROSE),
   [i for i in sorted(PROSE) if by_idx[i]['italian'].strip() == by_idx[i]['english'].strip()])

tok = sum(len(TAGS.findall(u['english'])) for u in su) + sum(len(TAGS.findall(u['italian'])) for u in tu)
ck('token <...>: 0 = 0 (assenza asserita)', tok == 0, tok)
a = sum(u['english'].count('"') for u in su)
b = sum(u['italian'].count('"') for u in tu)
ck('virgolette: %d = %d (attese 8)' % (b, a), a == b == 8, (a, b))
ck('virgolette: parita per unita',
   not [u['idx'] for u in tu if u['english'].count('"') != u['italian'].count('"')])
ck('virgolette dispari: nessuna',
   not [u['idx'] for u in tu if u['italian'].count('"') % 2])
ck('tab: parita per unita e presente solo in unita 2',
   not [u['idx'] for u in tu if u['english'].count('\t') != u['italian'].count('\t')]
   and [u['idx'] for u in tu if u['italian'].startswith('\t')] == [2])
ck('quadre e backtick: nessuna',
   not [u['idx'] for u in tu if '[' in u['italian'] or '`' in u['italian']])
ck('nessuna unita con italiano vuoto', all(u['italian'].strip() for u in tu))
NONLAT = re.compile(r'[^\x00-\x7F\u00C0-\u024F\u2018\u2019\u201C\u201D\u2013\u2014\u2026]')
ck('nessun carattere non latino sospetto', not [u for u in tu if NONLAT.search(u['italian'])])
ck('nessun trattino lungo/en-dash e nessuna virgoletta curva',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D')])
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
ck('duplicati inglesi: nessuno', not [v for v in grp.values() if len(v) > 1])
seen = collections.Counter(by_idx[u['idx']]['italian'] for u in tu)
ck('nessuna resa ripetuta fra inglesi diversi', not [k[:40] for k, n in seen.items() if n > 1])
merged = {}
for f in sorted(glob.glob(os.path.join(HERE, 'parts', 'part*.json'))):
    for k, v in json.load(open(f, encoding='utf-8')).items():
        merged[int(k)] = v
en_by_idx = {u['idx']: u['english'] for u in su}
ck('le parti ricostruiscono translation.json',
   {i: '\t' * (len(en_by_idx[i]) - len(en_by_idx[i].lstrip('\t'))) + v for i, v in merged.items()}
   == {u['idx']: u['italian'] for u in tu})
ck('le parti coprono 1..15', sorted(merged) == list(range(1, 16)), len(merged))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('parole EN %d -> IT %d · sha256[:16] %s'
      % (sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu), h[:16]))
print()
print('FAIL:', len(fail), '·', 'verify L82 superato' if not fail else 'verify L82 fallito')
raise SystemExit(0 if not fail else 1)
