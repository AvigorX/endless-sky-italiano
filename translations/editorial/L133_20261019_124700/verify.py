r"""verify.py — L133 (`data/hai/unfettered side missions.txt`, 67 unita', righe 237-477)

Invariante di **segmento** (il file non si chiude): **159 unita'** totali, **84 prima** della riga 237, **8 dopo** la
477, confine alla riga **494** (`mission:Undeserved Anomalocaris`). Ricalcolato dal repository e da `state.db`.

Misure proprie: **2 contesti** (10 / 57), **50 `MISSION_TEXT`**, **9 `DIALOG`**, **2 `VALUE`** identici, **2
`DESCRIPTION`**, **2 `LOGBOOK`**, **2 `UI_LABEL`** identiche; **34 unita' con tab**; **98 virgolette** (quattro unita'
dispari); **8 token** in **6 famiglie**; **64 testi distinti**.
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
PATH = 'data/hai/unfettered side missions.txt'
TAGS = re.compile(r'<[^<>]+>')
VAL = [1, 11]
LAB = [40, 44]
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
ck('idx 1..67 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 68)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 67 righe 237 - 477', len(tu) == 67 and (first, last) == (237, 477), (len(tu), first, last))
tot = db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0]
before = db.execute('select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0]
after = db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0]
ck('file: 159 unita', tot == 159, tot)
ck('84 unita prima della riga 237 (L132)', before == 84, before)
ck('8 unita dopo la riga 477 (l ultimo segmento)', after == 8, after)
ck('il confine: la riga 494 apre mission:Undeserved Anomalocaris',
   db.execute('select line,context from units where path=? and line>? order by line limit 1',
              (PATH, last)).fetchone() == (494, 'mission:Undeserved Anomalocaris'))
ck('tipi: 50 MISSION_TEXT · 9 DIALOG · 2 VALUE · 2 DESCRIPTION · 2 LOGBOOK · 2 UI_LABEL',
   collections.Counter(u['kind'] for u in su) == {'MISSION_TEXT': 50, 'DIALOG': 9, 'VALUE': 2, 'DESCRIPTION': 2,
                                                  'LOGBOOK': 2, 'UI_LABEL': 2},
   collections.Counter(u['kind'] for u in su))
ck('i 2 VALUE sono identici al sorgente',
   [u['idx'] for u in su if u['kind'] == 'VALUE'] == VAL
   and [by[i]['italian'] for i in VAL] == ['Heritage Reclaimed', 'Ancient Claim'])
ck('le 2 UI_LABEL sono identiche',
   [u['idx'] for u in su if u['kind'] == 'UI_LABEL'] == LAB
   and [by[i]['italian'] for i in LAB] == ['too many ships', 'too many ships'])
ck('tutte PENDING',
   not [u['idx'] for u in su
        if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('tutte le unita prosaiche sono tradotte',
   not [u['idx'] for u in tu if u['idx'] not in VAL + LAB and u['italian'].strip() == u['english'].strip()])
ck('spazi iniziali e finali identici al sorgente (67/67)',
   not [u['idx'] for u in tu
        if len(u['italian']) - len(u['italian'].rstrip()) != len(u['english']) - len(u['english'].rstrip())])
tabs = [u['idx'] for u in su if u['english'].startswith('\t')]
ck('34 unita con tab iniziale, le stesse in traduzione',
   len(tabs) == 34 and tabs == [u['idx'] for u in tu if u['italian'].startswith('\t')], len(tabs))
ck('conteggio dei tab identico per unita',
   not [u['idx'] for u in tu if u['english'].count('\t') != u['italian'].count('\t')])
ck('98 virgolette, stesse per unita',
   sum(u['english'].count('"') for u in su) == 98 == sum(u['italian'].count('"') for u in tu)
   and not [u['idx'] for u in tu if u['english'].count('"') != u['italian'].count('"')])
ck('quattro unita dispari (47, 48, 64, 65) con 1, 1, 3, 1 virgolette',
   [u['idx'] for u in su if u['english'].count('"') % 2] == [47, 48, 64, 65]
   and [by[i]['italian'].count('"') for i in (47, 48, 64, 65)] == [1, 1, 3, 1])
ck('distribuzione virgolette: 18 / 44 / 1 / 3 / 1',
   collections.Counter(u['english'].count('"') for u in su) == {0: 18, 2: 44, 4: 1, 1: 3, 3: 1})
tk = collections.Counter(t for u in su for t in TAGS.findall(u['english']))
ck('8 token in 6 famiglie, sequenza identica per unita',
   dict(tk) == {'<planet>': 2, '<date>': 2, '<destination>': 1, '<last>': 1, '<payment>': 1, '<system>': 1}
   and not [u['idx'] for u in tu if TAGS.findall(u['english']) != TAGS.findall(u['italian'])], dict(tk))
ck('ZERO quadre e zero backtick nella traduzione',
   not [u for u in tu if any(c in u['italian'] for c in '[]`')])
seen = collections.OrderedDict()
for u in su:
    seen[u['context']] = seen.get(u['context'], 0) + 1
ck('2 contesti: 10 / 57', list(seen.values()) == [10, 57], list(seen.items()))
grp = {}
for u in tu:
    grp.setdefault(u['english'].lstrip('\t'), set()).add(u['italian'])
ck('64 testi inglesi distinti su 67 unita', len(grp) == 64, len(grp))
ck('stesso inglese => stessa resa', not [(k, v) for k, v in grp.items() if len(v) > 1])
ck('nomi propri intatti: Ehma Ti, Firelode, Lightning Bug, Mera',
   all(t in ' '.join(u['italian'] for u in tu) for t in ('Ehma Ti', 'Firelode', 'Lightning Bug', 'Mera')))
ck('incoerenza del sorgente riprodotta (diario: cibo; testo: forniture mediche)',
   'carico urgente di cibo' in by[10]['italian'] and 'forniture mediche' in by[9]['italian'])
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
ck('le tre parti ricostruiscono translation.json (1..67)',
   sorted(merged) == list(range(1, 68)) and merged == {u['idx']: u['italian'] for u in tu})
ck('nessun altro lotto rivendica queste righe',
   not [f for f in os.listdir(os.path.join(L10N, 'staging/editorial'))
        if f.startswith('L') and os.path.exists(os.path.join(L10N, 'staging/editorial', f, 'translation.json'))
        and f != os.path.basename(HERE)
        and any(u['path'] == PATH and 237 <= u['line'] <= 477
                for u in json.load(open(os.path.join(L10N, 'staging/editorial', f, 'translation.json'),
                                        encoding='utf-8'))['units'])])
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('copertura file: 151/159 (95.0%) · segmento (237, 477) · 8 unita dopo')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L133 superato' if not fail else 'verify L133 fallito')
raise SystemExit(0 if not fail else 1)
