r"""verify.py — L137 (`data/starts.txt`, 17 unita', righe 172-214). Terzo inizio: `Escaping Squalor`.

Invariante di **segmento**: 113 unita' nel file, **47 prima** della riga 172, **49 dopo** la 214, confine riga **215**
(`start:hai space`). Il file **non** si chiude.

Misure proprie: **2 contesti completi**, **1 `VALUE`**, **zero token**, **12 virgolette** (6:2, 11:2, 13:2, 14:4,
17:2), **8 tab**, **17 testi distinti**, **5 unita' rilette da L135** identiche, numeri italiani su cinque cifre.
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
ck('idx 1..17 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 18)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 17 righe 172 - 210', len(tu) == 17 and (first, last) == (172, 210), (len(tu), first, last))
ck('47 unita prima della riga 172 (L135 + L136)', db.execute(
    'select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0] == 47)
ck('113 unita nel file, 49 dopo la riga 210', db.execute(
    'select count(*) from units where path=?', (PATH,)).fetchone()[0] == 113
   and db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0] == 49)
ck('confine alla riga 215: start:hai space', db.execute(
    'select line,context from units where path=? and line>? order by line limit 1',
    (PATH, last)).fetchone() == (215, 'start:hai space'))
ck('tipi: 10 CONVERSATION, 4 LOGBOOK, 2 DESCRIPTION, 1 VALUE',
   collections.Counter(u['kind'] for u in su)
   == {'CONVERSATION': 10, 'LOGBOOK': 4, 'DESCRIPTION': 2, 'VALUE': 1},
   collections.Counter(u['kind'] for u in su))
ck('ZERO UI_LABEL nel segmento (asserzione vuota)',
   [u['idx'] for u in su if u['kind'] == 'UI_LABEL'] == [])
ck('ZERO token nel segmento (asserzione vuota)',
   collections.Counter(t for u in su for t in TAGS.findall(u['english'])) == {})
ck('1 VALUE identico: Escaping Squalor',
   [(u['idx'], u['italian']) for u in tu if u['kind'] == 'VALUE'] == [(1, 'Escaping Squalor')])
ck('tutte le unita di testo sono tradotte',
   not [u['idx'] for u in tu if u['kind'] != 'VALUE' and u['italian'].strip() == u['english'].strip()])
ck('tutte PENDING', not [u['idx'] for u in su
                         if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('spazi iniziali e finali identici al sorgente (17/17)',
   not [u['idx'] for u in tu
        if len(u['italian']) - len(u['italian'].rstrip()) != len(u['english']) - len(u['english'].rstrip())])
tabs = [u['idx'] for u in su if u['english'].startswith('\t')]
ck('8 unita con tab iniziale, le stesse in traduzione',
   len(tabs) == 8 and tabs == [u['idx'] for u in tu if u['italian'].startswith('\t')], len(tabs))
ck('12 virgolette, stesse per unita, distribuzione 6:2 11:2 13:2 14:4 17:2',
   sum(u['english'].count('"') for u in su) == 12 == sum(u['italian'].count('"') for u in tu)
   and [(u['idx'], u['italian'].count('"')) for u in tu if u['italian'].count('"')]
   == [(6, 2), (11, 2), (13, 2), (14, 4), (17, 2)]
   and [u['idx'] for u in su if u['english'].count('"') % 2] == [])
ck('2 contesti completi: start:syndicate 3, conversation:syndicate intro 14',
   [(v, len([u for u in su if u['context'] == v])) for v in ('start:syndicate', 'conversation:syndicate intro')]
   == [('start:syndicate', 3), ('conversation:syndicate intro', 14)])
prev = {u['english']: u['italian'] for u in json.load(open(PREV, encoding='utf-8'))['units']}
ck('5 unita rilette da L135 identiche (testo e inglese)',
   all(by[i]['english'].lstrip('\t') in prev and prev[by[i]['english'].lstrip('\t')] == by[i]['italian']
       for i in (5, 6, 7, 8, 9)))
ck('17 testi inglesi distinti su 17 unita', len({u['english'] for u in tu}) == 17,
   len({u['english'] for u in tu}))
NUM = ' '.join(u['italian'] for u in tu)
ck('cinque cifre in convenzione italiana',
   all(t in NUM for t in ('600.000', '0,5%', '3.580', '706.571', '480.000')))
ck('nessuna cifra in forma inglese',
   not any(t in NUM for t in ('600,000', '0.5%', '3,580', '706,571', '480,000')))
ck('i nomi restano: Delve, Antipode, Terra, Syndicated Systems',
   all(t in NUM for t in ('Delve', 'Antipode', 'Terra', 'Syndicated Systems')))
CORT = re.findall(r'\bLei\b|(?<![.!?] )\b(?:Suo|Sua|Suoi|Sue)\b', NUM)
ck('cortesia non propagata alla narrazione (al massimo una forma, dentro la battuta)',
   len(CORT) <= 1, CORT)
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
ck('le tre parti ricostruiscono translation.json (1..17)',
   sorted(merged) == list(range(1, 18)) and merged == {u['idx']: u['italian'] for u in tu})
ck('nessun altro lotto rivendica le righe 172-210 di starts.txt',
   not [f for f in os.listdir(os.path.join(L10N, 'staging/editorial'))
        if f.startswith('L') and os.path.exists(os.path.join(L10N, 'staging/editorial', f, 'translation.json'))
        and os.path.abspath(os.path.join(L10N, 'staging/editorial', f)) != HERE
        and any(u['path'] == PATH and first <= u['line'] <= last for u in json.load(open(os.path.join(
            L10N, 'staging/editorial', f, 'translation.json'), encoding='utf-8'))['units'])])
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('segmento: 64/113 unita del file (56,6%) · 2 contesti completi · 47 prima / 49 dopo')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L137 superato' if not fail else 'verify L137 fallito')
raise SystemExit(0 if not fail else 1)
