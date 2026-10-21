r"""verify.py — L138 (`data/starts.txt`, 47 unita', righe 215-358). Quarto inizio: gli Hai.

Invariante di **segmento**: 113 unita' nel file, **64 prima** della riga 215, **2 dopo** la 358, confine riga **365**
(`ship:Grasshopper`). Il file **non** si chiude: mancano le due `TEXT` di `ship:Grasshopper`, che chiuderanno in L139.

Misure proprie: **due `VALUE` identici**, **32 tab**, **56 virgolette** con **quattro unita' dispari** (26, 36, 37, 38)
riprodotte, **cinque unita' rilette da L135** identiche, **45 testi distinti**.
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
PATH = 'data/starts.txt'
PREV = os.path.join(L10N, 'staging/editorial/L135_20261019_131024/translation.json')
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
ck('idx 1..47 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 48)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 47 righe 215 - 358', len(tu) == 47 and (first, last) == (215, 358), (len(tu), first, last))
ck('64 unita prima della riga 215 (L135 + L136 + L137)', db.execute(
    'select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0] == 64)
ck('113 unita nel file, 2 dopo la riga 358', db.execute(
    'select count(*) from units where path=?', (PATH,)).fetchone()[0] == 113
   and db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0] == 2)
ck('confine alla riga 365: ship:Grasshopper', db.execute(
    'select line,context from units where path=? and line>? order by line limit 1',
    (PATH, last)).fetchone() == (365, 'ship:Grasshopper'))
ck('tipi: 32 CONVERSATION, 7 LOGBOOK, 6 DESCRIPTION, 2 VALUE',
   collections.Counter(u['kind'] for u in su)
   == {'CONVERSATION': 32, 'LOGBOOK': 7, 'DESCRIPTION': 6, 'VALUE': 2},
   collections.Counter(u['kind'] for u in su))
ck('ZERO UI_LABEL nel segmento (asserzione vuota)',
   [u['idx'] for u in su if u['kind'] == 'UI_LABEL'] == [])
ck('ZERO token nel segmento (asserzione vuota)',
   collections.Counter(t for u in su for t in TAGS.findall(u['english'])) == {})
ck('due VALUE identici: Hai Origins (unita 1 e 5)',
   [(u['idx'], u['italian']) for u in tu if u['kind'] == 'VALUE'] == [(1, 'Hai Origins'), (5, 'Hai Origins')])
ck('i due inizi non dicono la stessa cosa sulle condizioni di sblocco',
   by[4]['italian'] == 'Questo inizio è bloccato.'
   and by[8]['italian'].lstrip('\t').startswith('Per sbloccare questo inizio'))
ck('tutte le unita di testo sono tradotte',
   not [u['idx'] for u in tu if u['kind'] != 'VALUE' and u['italian'].strip() == u['english'].strip()])
ck('tutte PENDING', not [u['idx'] for u in su
                         if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('spazi iniziali e finali identici al sorgente (47/47)',
   not [u['idx'] for u in tu
        if len(u['italian']) - len(u['italian'].rstrip()) != len(u['english']) - len(u['english'].rstrip())])
tabs = [u['idx'] for u in su if u['english'].startswith('\t')]
ck('32 unita con tab iniziale, le stesse in traduzione',
   len(tabs) == 32 and tabs == [u['idx'] for u in tu if u['italian'].startswith('\t')], len(tabs))
ck('56 virgolette, stesse per unita',
   sum(u['english'].count('"') for u in su) == 56 == sum(u['italian'].count('"') for u in tu)
   and not [u['idx'] for u in tu if u['english'].count('"') != u['italian'].count('"')])
ck('quattro unita dispari con una virgoletta: 26, 36, 37, 38',
   [(u['idx'], u['italian'].count('"')) for u in tu if u['italian'].count('"') % 2]
   == [(26, 1), (36, 1), (37, 1), (38, 1)])
ck('le quattro dispari restano aperte (nessuna riparazione)',
   all(u['italian'].count('"') == 1 and not u['italian'].rstrip().endswith('"')
       for u in tu if u['idx'] in (26, 36, 37, 38)))
ck('2 contesti completi: start:hai space 8, conversation:hai intro 39',
   [(v, len([u for u in su if u['context'] == v])) for v in ('start:hai space', 'conversation:hai intro')]
   == [('start:hai space', 8), ('conversation:hai intro', 39)])
prev = {u['english']: u['italian'] for u in json.load(open(PREV, encoding='utf-8'))['units']}
ck('5 unita rilette da L135 identiche (testo e inglese)',
   all(by[i]['english'].lstrip('\t') in prev and prev[by[i]['english'].lstrip('\t')] == by[i]['italian']
       for i in (10, 11, 12, 13, 14)))
ck('45 testi inglesi distinti su 47 unita', len({u['english'] for u in tu}) == 45,
   len({u['english'] for u in tu}))
NUM = ' '.join(u['italian'] for u in tu)
ck('quattro cifre in convenzione italiana',
   all(t in NUM for t in ('1,431 milioni', '0,3%', '4.836', '1,132 milioni')))
ck('nessuna cifra in forma inglese',
   not any(t in NUM for t in ('1.431 million', '0.3%', '4,836', '1.132 million')))
ck('i nomi restano: Greenwater, Pristine Jewel, Grasshopper, Aphid, Sheragi, Drak',
   all(t in NUM for t in ('Greenwater', 'Pristine Jewel', 'Grasshopper', 'Aphid', 'Sheragi', 'Drak')))
CORT = re.findall(r'\bLei\b|(?<![.!?] )\b(?:Suo|Sua|Suoi|Sue)\b', NUM)
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
ck('le cinque parti ricostruiscono translation.json (1..47)',
   sorted(merged) == list(range(1, 48)) and merged == {u['idx']: u['italian'] for u in tu})
ck('nessun altro lotto rivendica le righe 215-358 di starts.txt',
   not [f for f in os.listdir(os.path.join(L10N, 'staging/editorial'))
        if f.startswith('L') and os.path.exists(os.path.join(L10N, 'staging/editorial', f, 'translation.json'))
        and os.path.abspath(os.path.join(L10N, 'staging/editorial', f)) != HERE
        and any(u['path'] == PATH and first <= u['line'] <= last for u in json.load(open(os.path.join(
            L10N, 'staging/editorial', f, 'translation.json'), encoding='utf-8'))['units'])])
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('segmento: 111/113 unita del file (98,2%) · 2 contesti completi · 64 prima / 2 dopo')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L138 superato' if not fail else 'verify L138 fallito')
raise SystemExit(0 if not fail else 1)
