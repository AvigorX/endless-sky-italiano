r"""verify.py — L135 (`data/starts.txt`, 32 unita', righe 18-134). File **nuovo**: nessuna invariante di file.

Invariante di **segmento**: 113 unita' nel file, **0 prima** della riga 18, **81 dopo** la 134, confine alla riga
**135** (`start:paradise`). Ricalcolato dal repository e da `state.db`.

Misure proprie: **4 contesti completi**, **2 `VALUE`** identici, **zero token**, **14 tab**, **14 virgolette** senza
unita' dispari, **27 testi distinti**, **5 frasi ripetute** con resa identica.
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
ck('idx 1..32 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 33)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 32 righe 18 - 130', len(tu) == 32 and (first, last) == (18, 130), (len(tu), first, last))
ck('ZERO unita prima della riga 18', db.execute(
    'select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0] == 0)
ck('113 unita nel file, 81 dopo la riga 130', db.execute(
    'select count(*) from units where path=?', (PATH,)).fetchone()[0] == 113
   and db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0] == 81)
ck('confine alla riga 135: start:paradise', db.execute(
    'select line,context from units where path=? and line>? order by line limit 1',
    (PATH, last)).fetchone() == (135, 'start:paradise'))
ck('tipi: 18 CONVERSATION, 8 LOGBOOK, 4 DESCRIPTION, 2 VALUE',
   collections.Counter(u['kind'] for u in su)
   == {'CONVERSATION': 18, 'LOGBOOK': 8, 'DESCRIPTION': 4, 'VALUE': 2},
   collections.Counter(u['kind'] for u in su))
ck('ZERO UI_LABEL nel segmento (asserzione vuota)',
   [u['idx'] for u in su if u['kind'] == 'UI_LABEL'] == [])
ck('ZERO token nel segmento (asserzione vuota)',
   collections.Counter(t for u in su for t in TAGS.findall(u['english'])) == {})
ck('2 VALUE identici: Endless Sky, Deep Desire',
   [(u['idx'], u['italian']) for u in tu if u['kind'] == 'VALUE']
   == [(1, 'Endless Sky'), (17, 'Deep Desire')])
ck('tutte le unita di testo sono tradotte',
   not [u['idx'] for u in tu if u['kind'] != 'VALUE' and u['italian'].strip() == u['english'].strip()])
ck('tutte PENDING', not [u['idx'] for u in su
                         if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('spazi iniziali e finali identici al sorgente (32/32)',
   not [u['idx'] for u in tu
        if len(u['italian']) - len(u['italian'].rstrip()) != len(u['english']) - len(u['english'].rstrip())])
tabs = [u['idx'] for u in su if u['english'].startswith('\t')]
ck('14 unita con tab iniziale, le stesse in traduzione',
   len(tabs) == 14 and tabs == [u['idx'] for u in tu if u['italian'].startswith('\t')], len(tabs))
ck('conteggio dei tab identico per unita',
   not [u['idx'] for u in tu if u['english'].count('\t') != u['italian'].count('\t')])
ck('14 virgolette, stesse per unita, nessuna dispari',
   sum(u['english'].count('"') for u in su) == 14 == sum(u['italian'].count('"') for u in tu)
   and not [u['idx'] for u in tu if u['english'].count('"') != u['italian'].count('"')]
   and [u['idx'] for u in su if u['english'].count('"') % 2] == [])
ck('4 contesti completi: start:default, conversation:default intro, start:deep, conversation:deep intro',
   [(v, len([u for u in su if u['context'] == v])) for v in ('start:default', 'conversation:default intro',
    'start:deep', 'conversation:deep intro')] == [('start:default', 3), ('conversation:default intro', 13),
                                                  ('start:deep', 3), ('conversation:deep intro', 13)])
ck('27 testi inglesi distinti su 32 unita', len({u['english'] for u in tu}) == 27,
   len({u['english'] for u in tu}))
ck('5 frasi ripetute con resa identica (21-25 = 5-9)',
   all(by[a]['english'] == by[b]['english'] and by[a]['italian'] == by[b]['italian']
       for a, b in ((21, 5), (22, 6), (23, 7), (24, 8), (25, 9))))
ck('numeri in convenzione italiana, otto cifre chiave',
   all(t in ' '.join(u['italian'] for u in tu)
       for t in ('480.000', '2.503', '433.567', '680.000', '2.627', '278.760', '0,4%', '0,2%')))
ck('nessun numero inglese rimasto',
   not any(t in ' '.join(u['italian'] for u in tu)
           for t in ('480,000', '2,503', '433,567', '680,000', '2,627', '278,760', '0.4%', '0.2%')))
ck('i nomi di regione restano inglesi: Deep, Dirt Belt, nessun «Profondo»',
   'Deep' in ' '.join(u['italian'] for u in tu) and 'Profondo' not in ' '.join(u['italian'] for u in tu))
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
ck('le quattro parti ricostruiscono translation.json (1..32)',
   sorted(merged) == list(range(1, 33)) and merged == {u['idx']: u['italian'] for u in tu})
ck('nessun altro lotto rivendica le righe 18-130 di starts.txt',
   not [f for f in os.listdir(os.path.join(L10N, 'staging/editorial'))
        if f.startswith('L') and os.path.exists(os.path.join(L10N, 'staging/editorial', f, 'translation.json'))
        and os.path.abspath(os.path.join(L10N, 'staging/editorial', f)) != HERE
        and any(u['path'] == PATH and first <= u['line'] <= last for u in json.load(open(os.path.join(
            L10N, 'staging/editorial', f, 'translation.json'), encoding='utf-8'))['units'])])
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('segmento: 32/113 unita del file (28,3%) · 4 contesti completi · 0 prima / 81 dopo')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L135 superato' if not fail else 'verify L135 fallito')
raise SystemExit(0 if not fail else 1)
