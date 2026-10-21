r"""verify.py — L129 (`data/human/boarding missions.txt`, 89 unita', righe 15-386)

Invariante di **segmento** (il file non si chiude): **240 unita'** totali, **0 prima** della riga 15, **151 dopo** la
386, confine alla riga **417** (`conversation:boarding pirate`). Ricalcolato dal repository e da `state.db`.

Misure proprie: **48 `TEXT`** (frammenti), **21 `MISSION_TEXT`**, **6 `CONVERSATION`**, **6 `VALUE`**, **6
`DESCRIPTION`**, **2 `DIALOG`**; **4 unita' identiche** perche' non sono testo; **22 unita' con tab**; **10
virgolette**; **43 token** in **7 famiglie**; **80 testi distinti** su 89 unita'; **spazi iniziali e finali identici**
al sorgente.
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
PATH = 'data/human/boarding missions.txt'
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
ck('idx 1..89 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 90)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 89 righe 15 - 386', len(tu) == 89 and (first, last) == (15, 386), (len(tu), first, last))
tot = db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0]
before = db.execute('select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0]
after = db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0]
maxl = db.execute('select max(line) from units where path=?', (PATH,)).fetchone()[0]
ck('file: 240 unita, max(line) = 959', tot == 240 and maxl == 959, (tot, maxl))
ck('0 unita prima della riga 15 (apre il file)', before == 0, before)
ck('151 unita dopo la riga 386', after == 151, after)
ck('il confine: la riga 417 apre conversation:boarding pirate',
   db.execute('select line,context from units where path=? and line>? order by line limit 1',
              (PATH, last)).fetchone() == (417, 'conversation:boarding pirate'))
ck('tipi: 48 TEXT · 21 MISSION_TEXT · 6 CONVERSATION · 6 VALUE · 6 DESCRIPTION · 2 DIALOG',
   collections.Counter(u['kind'] for u in su) == {'TEXT': 48, 'MISSION_TEXT': 21, 'CONVERSATION': 6, 'VALUE': 6,
                                                  'DESCRIPTION': 6, 'DIALOG': 2},
   collections.Counter(u['kind'] for u in su))
IDENT = [1, 2, 27, 28]
ck('le 4 unita che non sono testo restano identiche',
   [by[i]['italian'] for i in IDENT] == [by[i]['english'] for i in IDENT])
VAL = [u['idx'] for u in su if u['kind'] == 'VALUE']
ck('i 6 VALUE sono identici al sorgente',
   VAL == [51, 71, 82, 84, 86, 88] and all(by[i]['italian'] == by[i]['english'] for i in VAL))
ck('i 2 frammenti di sola punteggiatura restano identici', by[29]['italian'] == ', ' and by[44]['italian'] == '.')
ck('tutte PENDING',
   not [u['idx'] for u in su
        if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('tutte le unita prosaiche sono tradotte',
   not [u['idx'] for u in tu if u['idx'] not in IDENT + VAL and u['idx'] not in (29, 44)
        and u['italian'].strip() == u['english'].strip()])
ck('spazi iniziali e finali identici al sorgente (89/89)',
   not [u['idx'] for u in tu
        if len(u['italian']) - len(u['italian'].rstrip()) != len(u['english']) - len(u['english'].rstrip())
        or len(u['italian'].lstrip('\t')) - len(u['italian'].lstrip('\t').lstrip(' '))
        != len(u['english'].lstrip('\t')) - len(u['english'].lstrip('\t').lstrip(' '))])
tabs = [u['idx'] for u in su if u['english'].startswith('\t')]
ck('22 unita con tab iniziale, le stesse in traduzione',
   len(tabs) == 22 and tabs == [u['idx'] for u in tu if u['italian'].startswith('\t')], len(tabs))
ck('conteggio dei tab identico per unita',
   not [u['idx'] for u in tu if u['english'].count('\t') != u['italian'].count('\t')])
ck('10 virgolette, stesse per unita',
   sum(u['english'].count('"') for u in su) == 10 == sum(u['italian'].count('"') for u in tu)
   and not [u['idx'] for u in tu if u['english'].count('"') != u['italian'].count('"')])
tk = collections.Counter(t for u in su for t in TAGS.findall(u['english']))
ck('43 token in 7 famiglie, sequenza identica per unita',
   dict(tk) == {'<origin>': 17, '<destination>': 9, '<planet>': 7, '<payment>': 6, '<cargo>': 2, '<bunks>': 1,
                '<commodity>': 1}
   and not [u['idx'] for u in tu if TAGS.findall(u['english']) != TAGS.findall(u['italian'])], dict(tk))
ck('ZERO quadre e zero backtick nella traduzione',
   not [u for u in tu if any(c in u['italian'] for c in '[]`')])
seen = collections.OrderedDict()
for u in su:
    seen[u['context']] = seen.get(u['context'], 0) + 1
ck('18 contesti: distribuzione 1/1/6/3/5/10/2/1/5/9/7/20/7/4/2/2/2/2',
   len(seen) == 18 and list(seen.values()) == [1, 1, 6, 3, 5, 10, 2, 1, 5, 9, 7, 20, 7, 4, 2, 2, 2, 2],
   list(seen.values()))
grp = {}
for u in tu:
    grp.setdefault(u['english'].lstrip('\t'), set()).add(u['italian'])
ck('80 testi inglesi distinti su 89 unita', len(grp) == 80, len(grp))
ck('stesso inglese => stessa resa', not [(k, v) for k, v in grp.items() if len(v) > 1])
ck('frammenti di frase presenti con i loro spazi',
   by[3]['italian'] == 'Sapendo che ' and by[26]['italian'] == 'il' and by[45]['italian'].startswith(' in ')
   and by[36]['italian'] == 'il ')
CORT = re.findall(r'\bLei\b|(?<![.!?] )\b(?:Suo|Sua|Suoi|Sue)\b', ' '.join(u['italian'] for u in tu))
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
ck('le tre parti ricostruiscono translation.json (1..89)',
   sorted(merged) == list(range(1, 90)) and merged == {u['idx']: u['italian'] for u in tu})
ck('nessun altro lotto rivendica queste righe',
   not [f for f in os.listdir(os.path.join(L10N, 'staging/editorial'))
        if f.startswith('L') and os.path.exists(os.path.join(L10N, 'staging/editorial', f, 'translation.json'))
        and f != os.path.basename(HERE)
        and any(u['path'] == PATH and 15 <= u['line'] <= 386
                for u in json.load(open(os.path.join(L10N, 'staging/editorial', f, 'translation.json'),
                                        encoding='utf-8'))['units'])])
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('copertura file: 89/240 (37.1%) · segmento (15, 386) · 151 unita dopo')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L129 superato' if not fail else 'verify L129 fallito')
raise SystemExit(0 if not fail else 1)
