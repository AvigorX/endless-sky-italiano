r"""verify.py — L132 (`data/hai/unfettered side missions.txt`, 84 unita', righe 17-229)

Invariante di **segmento** (il file non si chiude): **159 unita'** totali, **0 prima** della riga 17, **75 dopo** la
229, confine alla riga **237** (`mission:Hai Legacy 2`). Ricalcolato dal repository e da `state.db`.

Misure proprie: **2 contesti** (18 / 66), **78 `MISSION_TEXT`**, **3 `UI_LABEL`** identiche, **1 `DESCRIPTION`**, **1
`DIALOG`**, **1 `LOGBOOK`**, **zero `VALUE`**; **74 unita' con tab**; **89 virgolette** (tre unita' con una sola: 57,
62, 73); **8 token** in **4 famiglie**; **82 testi distinti**.
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
LAB = [39, 43, 48]
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
ck('idx 1..84 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 85)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 84 righe 17 - 229', len(tu) == 84 and (first, last) == (17, 229), (len(tu), first, last))
tot = db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0]
before = db.execute('select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0]
after = db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0]
maxl = db.execute('select max(line) from units where path=?', (PATH,)).fetchone()[0]
ck('file: 159 unita, max(line) = 510', tot == 159 and maxl == 510, (tot, maxl))
ck('0 unita prima della riga 17 (apre il file)', before == 0, before)
ck('75 unita dopo la riga 229', after == 75, after)
ck('il confine: la riga 237 apre mission:Hai Legacy 2',
   db.execute('select line,context from units where path=? and line>? order by line limit 1',
              (PATH, last)).fetchone() == (237, 'mission:Hai Legacy 2'))
ck('tipi: 78 MISSION_TEXT · 3 UI_LABEL · 1 DESCRIPTION · 1 DIALOG · 1 LOGBOOK',
   collections.Counter(u['kind'] for u in su) == {'MISSION_TEXT': 78, 'UI_LABEL': 3, 'DESCRIPTION': 1,
                                                  'DIALOG': 1, 'LOGBOOK': 1},
   collections.Counter(u['kind'] for u in su))
ck('le 3 UI_LABEL sono esattamente quelle elencate e sono identiche',
   [u['idx'] for u in su if u['kind'] == 'UI_LABEL'] == LAB
   and [by[i]['italian'] for i in LAB] == ['train back', 'tell me', 'try again'])
ck('ZERO VALUE nel segmento (asserzione vuota scritta)',
   [u['idx'] for u in su if u['kind'] == 'VALUE'] == [])
ck('la resa identica dichiarata: (No.) -> (No.)',
   by[4]['italian'].lstrip('\t') == by[4]['english'].lstrip('\t') == '(No.)')
ck('tutte PENDING',
   not [u['idx'] for u in su
        if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('tutte le unita prosaiche sono tradotte',
   not [u['idx'] for u in tu if u['idx'] not in LAB + [4] and u['italian'].strip() == u['english'].strip()])
ck('spazi iniziali e finali identici al sorgente (84/84)',
   not [u['idx'] for u in tu
        if len(u['italian']) - len(u['italian'].rstrip()) != len(u['english']) - len(u['english'].rstrip())])
tabs = [u['idx'] for u in su if u['english'].startswith('\t')]
ck('74 unita con tab iniziale, le stesse in traduzione',
   len(tabs) == 74 and tabs == [u['idx'] for u in tu if u['italian'].startswith('\t')], len(tabs))
ck('conteggio dei tab identico per unita',
   not [u['idx'] for u in tu if u['english'].count('\t') != u['italian'].count('\t')])
ck('89 virgolette, stesse per unita',
   sum(u['english'].count('"') for u in su) == 89 == sum(u['italian'].count('"') for u in tu)
   and not [u['idx'] for u in tu if u['english'].count('"') != u['italian'].count('"')])
ck('tre unita con una sola virgoletta (57, 62, 73)',
   [u['idx'] for u in su if u['english'].count('"') % 2] == [57, 62, 73]
   and all(by[i]['italian'].count('"') == 1 for i in (57, 62, 73)))
ck('distribuzione virgolette: 43 senza, 33 con 2, 5 con 4, 3 con 1',
   collections.Counter(u['english'].count('"') for u in su) == {0: 43, 2: 33, 4: 5, 1: 3})
tk = collections.Counter(t for u in su for t in TAGS.findall(u['english']))
ck('8 token in 4 famiglie, sequenza identica per unita',
   dict(tk) == {'<last>': 4, '<destination>': 2, '<first>': 1, '<payment>': 1}
   and not [u['idx'] for u in tu if TAGS.findall(u['english']) != TAGS.findall(u['italian'])], dict(tk))
ck('ZERO quadre e zero backtick nella traduzione',
   not [u for u in tu if any(c in u['italian'] for c in '[]`')])
seen = collections.OrderedDict()
for u in su:
    seen[u['context']] = seen.get(u['context'], 0) + 1
ck('2 contesti: 18 / 66', list(seen.values()) == [18, 66], list(seen.items()))
grp = {}
for u in tu:
    grp.setdefault(u['english'].lstrip('\t'), set()).add(u['italian'])
ck('82 testi inglesi distinti su 84 unita', len(grp) == 82, len(grp))
ck('stesso inglese => stessa resa', not [(k, v) for k, v in grp.items() if len(v) > 1])
ck('Hai-home resta nome proprio', 'Hai-home' in by[12]['italian'] and 'Hai-home' in by[18]['italian'])
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
ck('le tre parti ricostruiscono translation.json (1..84)',
   sorted(merged) == list(range(1, 85)) and merged == {u['idx']: u['italian'] for u in tu})
ck('nessun altro lotto rivendica queste righe',
   not [f for f in os.listdir(os.path.join(L10N, 'staging/editorial'))
        if f.startswith('L') and os.path.exists(os.path.join(L10N, 'staging/editorial', f, 'translation.json'))
        and f != os.path.basename(HERE)
        and any(u['path'] == PATH and 17 <= u['line'] <= 229
                for u in json.load(open(os.path.join(L10N, 'staging/editorial', f, 'translation.json'),
                                        encoding='utf-8'))['units'])])
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('copertura file: 84/159 (52.8%) · segmento (17, 229) · 75 unita dopo')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L132 superato' if not fail else 'verify L132 fallito')
raise SystemExit(0 if not fail else 1)
