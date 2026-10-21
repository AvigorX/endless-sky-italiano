r"""verify.py — L130 (`data/human/boarding missions.txt`, 75 unita', righe 417-686)

Invariante di **segmento** (il file non si chiude): **240 unita'** totali, **89 prima** della riga 417, **76 dopo** la
686, confine alla riga **695** (`mission:Turn in Tarquin`). Ricalcolato dal repository e da `state.db`.

Misure proprie: **4 contesti** (1 / 1 / 6 / 67), **50 `MISSION_TEXT`**, **22 `UI_LABEL`** identiche, **1
`CONVERSATION`**, **1 `DESCRIPTION`**, **1 `DIALOG`**, **zero `VALUE`**; **45 unita' con tab**; **31 virgolette** (una
unita' con tre); **19 token** in **5 famiglie**; **74 testi distinti** su 75 unita'.
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
LAB = [9, 10, 12, 14, 16, 22, 24, 36, 40, 41, 42, 44, 45, 54, 57, 60, 62, 63, 65, 67, 69, 72]
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
ck('idx 1..75 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 76)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 75 righe 417 - 686', len(tu) == 75 and (first, last) == (417, 686), (len(tu), first, last))
tot = db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0]
before = db.execute('select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0]
after = db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0]
ck('file: 240 unita', tot == 240, tot)
ck('89 unita prima della riga 417 (il lotto L129)', before == 89, before)
ck('76 unita dopo la riga 686', after == 76, after)
ck('il confine: la riga 695 apre mission:Turn in Tarquin',
   db.execute('select line,context from units where path=? and line>? order by line limit 1',
              (PATH, last)).fetchone() == (695, 'mission:Turn in Tarquin'))
ck('tipi: 50 MISSION_TEXT · 22 UI_LABEL · 1 CONVERSATION · 1 DESCRIPTION · 1 DIALOG',
   collections.Counter(u['kind'] for u in su) == {'MISSION_TEXT': 50, 'UI_LABEL': 22, 'CONVERSATION': 1,
                                                  'DESCRIPTION': 1, 'DIALOG': 1},
   collections.Counter(u['kind'] for u in su))
ck('le 22 UI_LABEL sono esattamente quelle elencate e sono identiche',
   [u['idx'] for u in su if u['kind'] == 'UI_LABEL'] == LAB
   and all(by[i]['italian'] == by[i]['english'] for i in LAB))
ck('ZERO VALUE nel segmento (asserzione vuota scritta)',
   [u['idx'] for u in su if u['kind'] == 'VALUE'] == [])
ck('tutte PENDING',
   not [u['idx'] for u in su
        if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('tutte le unita prosaiche sono tradotte',
   not [u['idx'] for u in tu if u['idx'] not in LAB and u['italian'].strip() == u['english'].strip()])
ck('spazi iniziali e finali identici al sorgente (75/75)',
   not [u['idx'] for u in tu
        if len(u['italian']) - len(u['italian'].rstrip()) != len(u['english']) - len(u['english'].rstrip())])
tabs = [u['idx'] for u in su if u['english'].startswith('\t')]
ck('45 unita con tab iniziale, le stesse in traduzione',
   len(tabs) == 45 and tabs == [u['idx'] for u in tu if u['italian'].startswith('\t')], len(tabs))
ck('conteggio dei tab identico per unita',
   not [u['idx'] for u in tu if u['english'].count('\t') != u['italian'].count('\t')])
ck('31 virgolette, stesse per unita',
   sum(u['english'].count('"') for u in su) == 31 == sum(u['italian'].count('"') for u in tu)
   and not [u['idx'] for u in tu if u['english'].count('"') != u['italian'].count('"')])
ck('una sola unita con virgolette dispari (21, tre virgolette)',
   [u['idx'] for u in su if u['english'].count('"') % 2] == [21] and by[21]['italian'].count('"') == 3)
tk = collections.Counter(t for u in su for t in TAGS.findall(u['english']))
ck('19 token in 5 famiglie, sequenza identica per unita',
   dict(tk) == {'<origin>': 12, '<payment>': 2, '<bunks>': 2, '<destination>': 2, '<planet>': 1}
   and not [u['idx'] for u in tu if TAGS.findall(u['english']) != TAGS.findall(u['italian'])], dict(tk))
ck('ZERO quadre e zero backtick nella traduzione',
   not [u for u in tu if any(c in u['italian'] for c in '[]`')])
seen = collections.OrderedDict()
for u in su:
    seen[u['context']] = seen.get(u['context'], 0) + 1
ck('4 contesti: 1 / 1 / 6 / 67', list(seen.values()) == [1, 1, 6, 67], list(seen.items()))
grp = {}
for u in tu:
    grp.setdefault(u['english'].lstrip('\t'), set()).add(u['italian'])
ck('74 testi inglesi distinti su 75 unita', len(grp) == 74, len(grp))
ck('stesso inglese => stessa resa', not [(k, v) for k, v in grp.items() if len(v) > 1])
ck('la fine del contesto e coerente: unita 75 chiude la missione con il database criminale',
   by[75]['english'].lstrip('	').startswith('A quick check of the public data')
   and 'database galattico della giustizia penale' in by[75]['italian'])
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
ck('le tre parti ricostruiscono translation.json (1..75)',
   sorted(merged) == list(range(1, 76)) and merged == {u['idx']: u['italian'] for u in tu})
ck('nessun altro lotto rivendica queste righe',
   not [f for f in os.listdir(os.path.join(L10N, 'staging/editorial'))
        if f.startswith('L') and os.path.exists(os.path.join(L10N, 'staging/editorial', f, 'translation.json'))
        and f != os.path.basename(HERE)
        and any(u['path'] == PATH and 417 <= u['line'] <= 686
                for u in json.load(open(os.path.join(L10N, 'staging/editorial', f, 'translation.json'),
                                        encoding='utf-8'))['units'])])
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('copertura file: 164/240 (68.3%) · segmento (417, 686) · 76 unita dopo')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L130 superato' if not fail else 'verify L130 fallito')
raise SystemExit(0 if not fail else 1)
