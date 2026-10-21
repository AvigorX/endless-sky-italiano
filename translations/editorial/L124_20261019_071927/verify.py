r"""verify.py — L124 (`data/human/ships.txt`, 29 unita', righe 2102-3422)

Invariante di **segmento** (il file non si chiude): **103 unità**, **54 prima** della riga 2102 (L123), **20 dopo**
la 3422, confine alla riga **3491** (`ship:Roost`). Ricalcolato dal repository e da `state.db`.

Misure proprie: **28 `DESCRIPTION`**, **1 `VALUE`**, **24 contesti**, **29 testi distinti**, **3 unità con tab**,
**14 virgolette**, **zero token**.
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
PATH = 'data/human/ships.txt'
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
ck('idx 1..29 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 30)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 29 righe 2102 - 3422', len(tu) == 29 and (first, last) == (2102, 3422), (len(tu), first, last))
tot = db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0]
before = db.execute('select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0]
after = db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0]
ck('file: 103 unita', tot == 103, tot)
ck('54 unita prima della riga 2102 (L123)', before == 54, before)
ck('20 unita dopo la riga 3422', after == 20, after)
ck('il confine: la riga 3491 apre ship:Roost',
   db.execute('select line,context from units where path=? and line>? order by line limit 1',
              (PATH, last)).fetchone() == (3491, 'ship:Roost'))
ck('tipi: 28 DESCRIPTION · 1 VALUE',
   collections.Counter(u['kind'] for u in su) == {'DESCRIPTION': 28, 'VALUE': 1},
   collections.Counter(u['kind'] for u in su))
VAL = [u['idx'] for u in su if u['kind'] == 'VALUE']
ck('l\'unico VALUE (unita 18) e identico al sorgente',
   VAL == [18] and by[18]['italian'] == by[18]['english'] == 'Modified Argosies')
ck('tutte PENDING',
   not [u['idx'] for u in su
        if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('tutte le unita non-VALUE sono tradotte',
   not [u['idx'] for u in tu if u['kind'] != 'VALUE' and u['italian'].strip() == u['english'].strip()])
tabs = [u['idx'] for u in su if u['english'].startswith('\t')]
ck('3 unita con tab iniziale (9, 12, 17), le stesse in traduzione',
   tabs == [9, 12, 17] == [u['idx'] for u in tu if u['italian'].startswith('\t')], tabs)
ck('conteggio dei tab identico per unita',
   not [u['idx'] for u in tu if u['english'].count('\t') != u['italian'].count('\t')])
ck('14 virgolette, nelle unita 8, 9, 10, 20, 23 e 26',
   sum(u['english'].count('"') for u in su) == 14 == sum(u['italian'].count('"') for u in tu)
   and [u['idx'] for u in su if '"' in u['english']] == [8, 9, 10, 20, 23, 26])
ck('ZERO token (asserito)', collections.Counter(t for u in su for t in TAGS.findall(u['english'])) == {}
   == collections.Counter(t for u in tu for t in TAGS.findall(u['italian'])))
ck('nessun backtick e nessuna quadra nella traduzione',
   not [u for u in tu if '`' in u['italian'] or '[' in u['italian'] or ']' in u['italian']])
seen = collections.Counter(u['context'] for u in su)
ck('24 contesti: 19x1, 5x2',
   len(seen) == 24 and collections.Counter(seen.values()) == {1: 19, 2: 5}, collections.Counter(seen.values()))
grp = collections.Counter(u['english'] for u in su)
ck('29 testi inglesi distinti per 29 unita', len(grp) == 29, len(grp))
it_grp = {}
for u in tu:
    it_grp.setdefault(u['italian'], []).append(u)
ck('nessun duplicato italiano non spiegato dal sorgente',
   not [g for g in it_grp.values() if len(g) > 1 and len({v['english'] for v in g}) > 1])
NONLAT = re.compile(r'[^\x00-\x7F\u00C0-\u024F]')
ck('nessun carattere non latino', not [u for u in tu if NONLAT.search(u['italian'])])
ck('nessun trattino lungo, virgoletta curva o ellissi tipografica',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate', 0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
ck('registro approvato: nessun «voi»',
   not [u['idx'] for u in tu if re.search(r'\b(avete|potete|potrete|siete|vostro|vostra|vostri|vostre)\b',
                                          u['italian'])])
merged = {}
for f in sorted(os.listdir(os.path.join(HERE, 'parts'))):
    if f.endswith('.json'):
        for k, v in json.load(open(os.path.join(HERE, 'parts', f), encoding='utf-8')).items():
            merged[int(k)] = v
ck('le due parti ricostruiscono translation.json (1..29)',
   sorted(merged) == list(range(1, 30)) and merged == {u['idx']: u['italian'] for u in tu})
ck('nessun altro lotto rivendica queste righe',
   not [f for f in os.listdir(os.path.join(L10N, 'staging/editorial'))
        if f.startswith('L') and os.path.exists(os.path.join(L10N, 'staging/editorial', f, 'translation.json'))
        and f != os.path.basename(HERE)
        and any(u['path'] == PATH and 2102 <= u['line'] <= 3422
                for u in json.load(open(os.path.join(L10N, 'staging/editorial', f, 'translation.json'),
                                        encoding='utf-8'))['units'])])
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('copertura file: 83/103 (80.6%) · segmento (2102, 3422) · 20 unita dopo')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L124 superato' if not fail else 'verify L124 fallito')
raise SystemExit(0 if not fail else 1)
