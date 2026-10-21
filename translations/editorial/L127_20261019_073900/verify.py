r"""verify.py — L127 (`data/incipias/incipias first contact.txt`, 63 unita', righe 224-331)

Invariante di **segmento** (il file non si chiude): **161 unità** totali, **0 prima** della riga 224, **43 dopo** la
331, confine alla riga **343** (`mission:Incipias: Fix Saves Missing Language`). Ricalcolato dal repository e da
`state.db`.

Misure proprie: **58 `MISSION_TEXT`**, **3 `LOGBOOK`**, **1 `VALUE`** identico, **1 `DESCRIPTION`**, **1 contesto**,
**55 unità con tab**, **98 virgolette**, **2 token** nella sola unità 38, **63 testi distinti**.
"""
import collections
import hashlib
import json
import os
import re
import sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
ROOT = os.path.abspath(os.path.join(L10N, '..'))
PATH = 'data/incipias/incipias first contact.txt'
TAGS = re.compile(r'<[^<>]+>')
su = sorted(json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
by = {u['idx']: u for u in tu}
lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
fail = []


def ck(n, c, d=''):
    print('%-70s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente', not [u for u in su if lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck('idx 1..63 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 64)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 63 righe 224 - 331', len(tu) == 63 and (first, last) == (224, 331), (len(tu), first, last))
tot = db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0]
before = db.execute('select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0]
after = db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0]
maxl = db.execute('select max(line) from units where path=?', (PATH,)).fetchone()[0]
ck('file: 161 unita, max(line) = 439', tot == 161 and maxl == 439, (tot, maxl))
ck('55 unita prima della riga 224 (L126)', before == 55, before)
ck('43 unita dopo la riga 331 (161 - 55 di L126 - 63 di L127)', after == 43, after)
ck('il confine: la riga 343 apre mission:Incipias: Fix Saves Missing Language',
   db.execute('select line,context from units where path=? and line>? order by line limit 1',
              (PATH, last)).fetchone() == (343, 'mission:Incipias: Fix Saves Missing Language'))
ck('tipi: 58 MISSION_TEXT · 3 LOGBOOK · 1 VALUE · 1 DESCRIPTION',
   collections.Counter(u['kind'] for u in su) == {'MISSION_TEXT': 58, 'LOGBOOK': 3, 'VALUE': 1,
                                                  'DESCRIPTION': 1},
   collections.Counter(u['kind'] for u in su))
ck('il VALUE (unita 1) e identico al sorgente',
   [u['idx'] for u in su if u['kind'] == 'VALUE'] == [1]
   and by[1]['italian'] == by[1]['english'] == 'Seek help from the Incipias')
ck('tutte PENDING',
   not [u['idx'] for u in su
        if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('tutte le unita prosaiche sono tradotte',
   not [u['idx'] for u in tu if u['kind'] != 'VALUE' and u['italian'].strip() == u['english'].strip()])
tabs = [u['idx'] for u in su if u['english'].startswith('\t')]
ck('55 unita con tab iniziale, le stesse in traduzione',
   len(tabs) == 55 and tabs == [u['idx'] for u in tu if u['italian'].startswith('\t')], len(tabs))
ck('conteggio dei tab identico per unita',
   not [u['idx'] for u in tu if u['english'].count('\t') != u['italian'].count('\t')])
ck('98 virgolette, stesse per unita',
   sum(u['english'].count('"') for u in su) == 98 == sum(u['italian'].count('"') for u in tu)
   and not [u['idx'] for u in tu if u['english'].count('"') != u['italian'].count('"')])
tk = collections.Counter(t for u in su for t in TAGS.findall(u['english']))
ck('2 token, nella sola unita 38, uguali in traduzione',
   dict(tk) == {'<first>': 1, '<last>': 1}
   and [u['idx'] for u in su if TAGS.findall(u['english'])] == [38]
   and TAGS.findall(by[38]['italian']) == ['<first>', '<last>'], (dict(tk), TAGS.findall(by[38]['italian'])))
ck('ZERO quadre e zero backtick nella traduzione',
   not [u for u in tu if any(c in u['italian'] for c in '[]`')])
seen = collections.Counter(u['context'] for u in su)
ck('un solo contesto, 63 unita', list(seen.items()) == [('mission:Incipias: Help The Stranded 1', 63)],
   list(seen.items()))
ck('63 testi inglesi distinti per 63 unita', len({u['english'] for u in su}) == 63)
it_grp = {}
for u in tu:
    it_grp.setdefault(u['italian'], []).append(u)
ck('nessun duplicato italiano',
   not [g for g in it_grp.values() if len(g) > 1], [[v['idx'] for v in g] for g in it_grp.values() if len(g) > 1])
ck('stile Incipias: sei composti con trattino',
   all(c in ' '.join(u['italian'] for u in tu).lower() for c in
       ('intenzione-scopo', 'stazione-capitale', 'essere-esterno', 'viaggiatore-di-mondi', 'pianeta-d\'aria',
        'luoghi-sistema')))
ck('il Quarg parla di se in terza persona: «questo uno» almeno 6 volte',
   ' '.join(u['italian'] for u in tu).lower().count('questo uno') >= 6)
CORT = re.findall(r'\b(?:Lei|lei)\b|(?<![.!?] )\b(?:Suo|Sua|Suoi|Sue)\b', ' '.join(u['italian'] for u in tu))
ck('nessuna forma di cortesia «Lei»', not CORT, CORT)
NONLAT = re.compile(r'[^\x00-\x7F\u00C0-\u024F]')
ck('nessun carattere non latino', not [u for u in tu if NONLAT.search(u['italian'])])
ck('nessun trattino lungo, virgoletta curva o ellissi tipografica',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate', 0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
merged = {}
for f in sorted(os.listdir(os.path.join(HERE, 'parts'))):
    if f.endswith('.json'):
        for k, v in json.load(open(os.path.join(HERE, 'parts', f), encoding='utf-8')).items():
            merged[int(k)] = v
ck('le tre parti ricostruiscono translation.json (1..63)',
   sorted(merged) == list(range(1, 64)) and merged == {u['idx']: u['italian'] for u in tu})
ck('nessun altro lotto rivendica queste righe',
   not [f for f in os.listdir(os.path.join(L10N, 'staging/editorial'))
        if f.startswith('L') and os.path.exists(os.path.join(L10N, 'staging/editorial', f, 'translation.json'))
        and f != os.path.basename(HERE)
        and any(u['path'] == PATH and 224 <= u['line'] <= 331
                for u in json.load(open(os.path.join(L10N, 'staging/editorial', f, 'translation.json'),
                                        encoding='utf-8'))['units'])])
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('copertura file: 118/161 (73.3%) · segmento (224, 331) · 43 unita dopo')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L127 superato' if not fail else 'verify L127 fallito')
raise SystemExit(0 if not fail else 1)
