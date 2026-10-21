r"""verify.py — L81 (data/successors/predecessors.txt, 22 unita', righe 1-200)

Verifica **indipendente** da `check.py`. Invariante di **segmento**: il file prosegue (riga 208 apre
`ship:Hasur, Vowsworn` di nuovo), quindi **0 prima** (il lotto apre il file), **37 dopo**, `max(line) = 782`,
file di **59 unita'**.

Misure attese: 22 unita', righe 17-196; **15 `TEXT` + 5 `DESCRIPTION` + 2 `VALUE`**; **17 unita' di dato**
(nomi di nave e di equipaggiamento) identiche, **5 di prosa** (la poesia di Resja) tradotte e **rimate**;
**0 tab**, **12 virgolette**, 0 dispari, **0 token**; **5 gruppi** di duplicati (nomi ripetuti su due navi).
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

DATA = {1, 2, 3, 4, 5, 6, 7, 8, 9, 15, 16, 17, 18, 19, 20, 21, 22}
PROSE = {10, 11, 12, 13, 14}
DUPS = [frozenset([3, 17]), frozenset([4, 18]), frozenset([6, 20]), frozenset([7, 21]), frozenset([9, 22])]
TAGS = re.compile(r'<[^<>]+>')
fail = []


def ck(name, cond, detail=''):
    print('%-68s %s %s' % (name, 'OK' if cond else 'FAIL', '' if cond else detail))
    if not cond:
        fail.append(name)


ck('riga grezza identica al file sorgente (22 righe)',
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
ck('idx del segmento senza buchi (1..22)', [u['idx'] for u in tu] == list(range(1, 23)))

first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 22 righe 17 - 196', len(tu) == 22 and (first, last) == (17, 196), (len(tu), first, last))
tot = db.execute('select count(*) from units where path = ?', (PATH,)).fetchone()[0]
before = db.execute('select count(*) from units where path = ? and line < ?', (PATH, first)).fetchone()[0]
after = db.execute('select count(*) from units where path = ? and line > ?', (PATH, last)).fetchone()[0]
maxline = db.execute('select max(line) from units where path = ?', (PATH,)).fetchone()[0]
ck('apre il file: 0 unita prima della riga 17', before == 0, before)
ck('il file prosegue: 37 unita dopo la riga 196', after == 37, after)
ck('file: 59 unita totali, max(line) = 782', tot == 59 and maxline == 782, (tot, maxline))
nxt = db.execute('select line, context from units where path = ? and line > ? order by line limit 1',
                 (PATH, last)).fetchone()
ck('confine dopo: riga 208 apre ship:Hasur, Vowsworn',
   nxt is not None and nxt['line'] == 208 and nxt['context'] == 'ship:Hasur, Vowsworn',
   tuple(nxt) if nxt else None)
inrange = db.execute('select count(*) from units where path = ? and line between ? and ?',
                     (PATH, first, last)).fetchone()[0]
ck('nessun altra unita nel DB dentro 17-196', inrange == len(tu), inrange)
ctxs = []
for u in su:
    if u['context'] not in ctxs:
        ctxs.append(u['context'])
ck('2 contesti ship:, in ordine di riga',
   ctxs == ['ship:Resja, of the Nine Eyes', 'ship:Hasur, Vowsworn'], ctxs)

kinds = collections.Counter(u['kind'] for u in su)
ck('kind: 15 TEXT, 5 DESCRIPTION, 2 VALUE', dict(kinds) == {'TEXT': 15, 'DESCRIPTION': 5, 'VALUE': 2},
   dict(kinds))
ck('MISSION_TEXT / UI_LABEL / LOGBOOK / DIALOG / CONVERSATION: nessuna (5 assenze)',
   all(not [u for u in tu if u['kind'] == k]
       for k in ('MISSION_TEXT', 'UI_LABEL', 'LOGBOOK', 'DIALOG', 'CONVERSATION')))

by_idx = {u['idx']: u for u in tu}
ck('le 17 unita di dato (navi + equipaggiamento) restano identiche',
   all(by_idx[i]['italian'] == by_idx[i]['english'] for i in DATA),
   [i for i in sorted(DATA) if by_idx[i]['italian'] != by_idx[i]['english']])
ck('le 5 unita di prosa sono tradotte',
   all(by_idx[i]['italian'].strip() != by_idx[i]['english'].strip() for i in PROSE),
   [i for i in sorted(PROSE) if by_idx[i]['italian'].strip() == by_idx[i]['english'].strip()])
rim = [by_idx[i]['italian'].rstrip(' ,.').lower()[-3:] for i in sorted(PROSE) if i > 10]
ck('la poesia mantiene la rima (-ora) nelle quattro strofe', len(set(rim)) == 1, (rim,))
ck('la poesia e 1 introduzione + 4 versi', len(PROSE) == 5)

tok = sum(len(TAGS.findall(u['english'])) for u in su) + sum(len(TAGS.findall(u['italian'])) for u in tu)
ck('token <...>: 0 in inglese e 0 in italiano (assenza asserita)', tok == 0, tok)
a = sum(u['english'].count('"') for u in su)
b = sum(u['italian'].count('"') for u in tu)
ck('virgolette: %d = %d (attese 12)' % (b, a), a == b == 12, (a, b))
ck('virgolette: parita per unita',
   not [u['idx'] for u in tu if u['english'].count('"') != u['italian'].count('"')])
ck('virgolette dispari: nessuna (assenza dichiarata)',
   not [u['idx'] for u in su if u['english'].count('"') % 2]
   and not [u['idx'] for u in tu if u['italian'].count('"') % 2])
ck('tab: 0 nel sorgente e 0 nel tradotto',
   not [u['idx'] for u in su if '\t' in u['english']] and not [u['idx'] for u in tu if '\t' in u['italian']])
ck('quadre e backtick: nessuna nel tradotto',
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
dups = set(frozenset(v) for v in grp.values() if len(v) > 1)
ck('duplicati inglesi: 5 gruppi (nomi ripetuti su due navi)', len(dups), dups == set(DUPS))
ck('i cinque gruppi hanno resa identica', all(len(set(by_idx[i]['italian'] for i in g)) == 1 for g in DUPS))
seen = collections.Counter(by_idx[u['idx']]['italian'] for u in tu)
free = [k[:40] for k, n in seen.items() if n > 1 and not any(k == by_idx[i]['italian'] for g in DUPS for i in g)]
ck('nessun altra resa ripetuta fra inglesi diversi', not free, free)

merged = {}
for f in sorted(glob.glob(os.path.join(HERE, 'parts', 'part*.json'))):
    for k, v in json.load(open(f, encoding='utf-8')).items():
        merged[int(k)] = v
en_by_idx = {u['idx']: u['english'] for u in su}
ck('le parti ricostruiscono translation.json',
   {i: '\t' * (len(en_by_idx[i]) - len(en_by_idx[i].lstrip('\t'))) + v for i, v in merged.items()}
   == {u['idx']: u['italian'] for u in tu})
ck('le parti coprono 1..22', sorted(merged) == list(range(1, 23)), len(merged))

h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('parole EN %d -> IT %d · sha256[:16] %s'
      % (sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu), h[:16]))
print()
print('FAIL:', len(fail), '·', 'verify L81 superato' if not fail else 'verify L81 fallito')
raise SystemExit(0 if not fail else 1)
