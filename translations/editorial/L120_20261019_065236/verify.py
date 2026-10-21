r"""verify.py — L120 (`data/human/campaign events.txt`, 52 unita', righe 28-242)

Il lotto **apre** il file, quindi l'invariante è di **segmento** (il file non si chiude): 150 unità totali,
`max(line) = 3468`, **0 unità prima** della riga 28, **98 dopo** la 242, confine alla riga **282**
(`event:initial deployment 1`). Tutto ricalcolato dal repository originale e da `state.db`, senza fidarsi di
`check.py`.

Misure proprie del lotto: **41 unità con tab** (e conteggio per unità), **58 virgolette** di dialogo, **5 token**,
**3 contesti** con distribuzione 6 / 9 / 37, **45 testi distinti** e **zero `VALUE`**.
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
PATH = 'data/human/campaign events.txt'
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
ck('idx 1..52 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 53)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 52 righe 28 - 242', len(tu) == 52 and (first, last) == (28, 242), (len(tu), first, last))
tot = db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0]
before = db.execute('select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0]
after = db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0]
maxl = db.execute('select max(line) from units where path=?', (PATH,)).fetchone()[0]
ck('file: 150 unita, max(line) = 3468', tot == 150 and maxl == 3468, (tot, maxl))
ck('0 unita prima della riga 28 (apre il file)', before == 0, before)
ck('98 unita dopo la riga 242', after == 98, after)
ck('il confine: la riga 282 apre event:initial deployment 1',
   db.execute('select line,context from units where path=? and line>? order by line limit 1',
              (PATH, last)).fetchone() == (282, 'event:initial deployment 1'))
ck('tipi: 41 MISSION_TEXT · 9 DESCRIPTION · 2 LOGBOOK',
   collections.Counter(u['kind'] for u in su) == {'MISSION_TEXT': 41, 'DESCRIPTION': 9, 'LOGBOOK': 2},
   collections.Counter(u['kind'] for u in su))
ck('ZERO VALUE nel file (asserzione vuota, dichiarata)',
   not [u['idx'] for u in su if u['kind'] == 'VALUE'])
ck('tutte PENDING',
   not [u['idx'] for u in su
        if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('tutte le unita sono tradotte',
   not [u['idx'] for u in tu if u['italian'].strip() == u['english'].strip()])
tabs = [u['idx'] for u in su if u['english'].startswith('\t')]
ck('41 unita con tab iniziale, le stesse in traduzione',
   len(tabs) == 41 and tabs == [u['idx'] for u in tu if u['italian'].startswith('\t')], len(tabs))
ck('conteggio dei tab identico per unita',
   not [u['idx'] for u in tu if u['english'].count('\t') != u['italian'].count('\t')])
ck('58 virgolette in inglese e in italiano',
   sum(u['english'].count('"') for u in su) == 58 == sum(u['italian'].count('"') for u in tu))
ck('virgolette per unita: stesso numero',
   not [u['idx'] for u in tu if u['english'].count('"') != u['italian'].count('"')])
TOK = {'<ship>': 4, '<planet>': 1}
ck('5 token nelle due famiglie attese',
   collections.Counter(t for u in su for t in TAGS.findall(u['english'])) == TOK
   == collections.Counter(t for u in tu for t in TAGS.findall(u['italian'])))
ck('token per unita: stessi simboli e stesso ordine',
   not [u['idx'] for u in tu if TAGS.findall(u['italian']) != TAGS.findall(u['english'])])
seen = collections.Counter(u['context'] for u in su)
ck('3 contesti: 6 / 9 / 37 unita',
   len(seen) == 3 and sorted(seen.values()) == [6, 9, 37]
   and seen['mission:event: war begins'] == 37, dict(seen))
grp = collections.Counter(u['english'] for u in su)
ck('45 testi inglesi distinti per 52 unita', len(grp) == 45, len(grp))
ck('7 coppie ripetute, nessuna con due rese',
   collections.Counter(grp.values()) == {1: 38, 2: 7}
   and not [k for k in grp if len({by[u['idx']]['italian'] for u in su if u['english'] == k}) > 1],
   collections.Counter(grp.values()))
it_grp = {}
for u in tu:
    it_grp.setdefault(u['italian'], []).append(u)
ck('nessun duplicato italiano non spiegato dal sorgente',
   not [g for g in it_grp.values() if len(g) > 1 and len({v['english'] for v in g}) > 1])
ck('nessun backtick e nessuna quadra nella traduzione',
   not [u for u in tu if '`' in u['italian'] or '[' in u['italian'] or ']' in u['italian']])
NONLAT = re.compile(r'[^\x00-\x7F\u00C0-\u024F]')
ck('nessun carattere non latino', not [u for u in tu if NONLAT.search(u['italian'])])
ck('nessun trattino lungo, virgoletta curva o ellissi tipografica',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate', 0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
ck('registro approvato: nessun «voi» e nessuna cortesia «lei»',
   not [u['idx'] for u in tu if re.search(r'\b(avete|potete|potrete|siete|vostro|vostra|vostri|vostre|Pensi quello|la sua nave|la farò)\b',
                                          u['italian'])])
merged = {}
for f in sorted(os.listdir(os.path.join(HERE, 'parts'))):
    if f.endswith('.json'):
        for k, v in json.load(open(os.path.join(HERE, 'parts', f), encoding='utf-8')).items():
            merged[int(k)] = v
ck('le tre parti ricostruiscono translation.json (1..52)',
   sorted(merged) == list(range(1, 53)) and merged == {u['idx']: u['italian'] for u in tu})
ck('nessun altro lotto rivendica queste righe',
   not [f for f in os.listdir(os.path.join(L10N, 'staging/editorial'))
        if f.startswith('L') and os.path.exists(os.path.join(L10N, 'staging/editorial', f, 'translation.json'))
        and f != os.path.basename(HERE)
        and any(u['path'] == PATH and 28 <= u['line'] <= 242
                for u in json.load(open(os.path.join(L10N, 'staging/editorial', f, 'translation.json'),
                                        encoding='utf-8'))['units'])])
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('copertura file: 52/150 (34.7%) · segmento (28, 242) · 98 unita dopo')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L120 superato' if not fail else 'verify L120 fallito')
raise SystemExit(0 if not fail else 1)
