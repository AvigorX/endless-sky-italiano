r"""verify.py — L146 (`data/hai/unfettered 0 prologue.txt`, 19 unita', righe 460-530). **CHIUDE IL FILE.**

Invariante di **file** (non di segmento): dopo la riga 530 non c'e' nulla, e i **sette** lotti che coprono il file
devono sommare esattamente le 147 unita' del database:

    L140 25 + L141 20 + L142 20 + L143 30 + L144 20 + L145 13 + L146 19 = 147

La somma si **calcola dai `translation.json`**, non si scrive a mano; `max(line)` e `count(*)` si interrogano.
"""
import collections
import glob
import hashlib
import json
import os
import re
import sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
ROOT = os.path.abspath(os.path.join(L10N, '..'))
PATH = 'data/hai/unfettered 0 prologue.txt'
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
ck('idx 1..19 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 20)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 19 righe 460 - 530', len(tu) == 19 and (first, last) == (460, 530), (len(tu), first, last))
ck('128 unita prima della riga 460 (L140…L145)', db.execute(
    'select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0] == 128)

# ---- invariante di FILE ----
tot = db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0]
maxl = db.execute('select max(line) from units where path=?', (PATH,)).fetchone()[0]
ck('147 unita nel file e max(line) = 530 (l ultima unita chiude il file)',
   tot == 147 and maxl == 530 and db.execute(
       'select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0] == 0, (tot, maxl))
lots = {}
for d in sorted(glob.glob(os.path.join(L10N, 'staging/editorial', 'L*'))):
    f = os.path.join(d, 'translation.json')
    if not os.path.exists(f):
        continue
    us = [u for u in json.load(open(f, encoding='utf-8'))['units'] if u['path'] == PATH]
    if us:
        lots[os.path.basename(d)] = sorted(u['line'] for u in us)
somma = sum(len(v) for v in lots.values())
ck('i 7 lotti del file sommano 147 (calcolato dai translation.json)', somma == 147 == len(set(
    l for v in lots.values() for l in v)), (somma, {k: len(v) for k, v in lots.items()}))
ck('7 lotti, ognuno con il suo intervallo, zero sovrapposizioni',
   len(lots) == 7 and not [1 for a in lots.values() for b in lots.values() if a is not b and set(a) & set(b)],
   {k: (v[0], v[-1], len(v)) for k, v in lots.items()})
ck('confine: dopo la riga 530 non c e nessuna unita (fine file)',
   db.execute('select line,context from units where path=? and line>? order by line limit 1',
              (PATH, last)).fetchone() is None)
ck('tipi: 17 MISSION_TEXT + 2 UI_LABEL',
   collections.Counter(u['kind'] for u in su) == {'MISSION_TEXT': 17, 'UI_LABEL': 2})
ck('le 2 UI_LABEL sono identiche al sorgente',
   [(u['idx'], u['italian'].lstrip('\t')) for u in tu if u['kind'] == 'UI_LABEL']
   == [(1, 'back to choose'), (8, 'buy tripulse')])
ck('ZERO VALUE (asserzione vuota scritta)', [u['idx'] for u in su if u['kind'] == 'VALUE'] == [])
ck('4 token, parita 1 = 1 per simbolo, nelle stesse unita (9, 11, 13, 17)',
   dict(collections.Counter(t for u in su for t in TAGS.findall(u['english'])))
   == {'<origin>': 1, '<as before (run)>': 1, '<as before (flee)>': 1, '<leave>': 1}
   == dict(collections.Counter(t for u in tu for t in TAGS.findall(u['italian'])))
   and [u['idx'] for u in tu if TAGS.findall(u['italian'])] == [9, 11, 13, 17])
ck('token con parentesi interi e a inizio frase',
   by[11]['italian'].lstrip('\t').startswith('<as before (run)> riesci')
   and by[13]['italian'].lstrip('\t').startswith('<as before (flee)> fuggi')
   and by[17]['italian'].lstrip('\t').startswith("<leave> L'ingegnere") and 'qui su <origin>' in by[9]['italian'])
ck('28 virgolette e ZERO dispari in inglese e in italiano',
   sum(u['english'].count('"') for u in su) == 28 == sum(u['italian'].count('"') for u in tu)
   and [u['idx'] for u in su if u['english'].count('"') % 2] == []
   and [u['idx'] for u in tu if u['italian'].count('"') % 2] == [])
ck('tutte le unita di testo sono tradotte (le 2 UI_LABEL a parte)',
   not [u['idx'] for u in tu if u['kind'] != 'UI_LABEL' and u['italian'].strip() == u['english'].strip()])
ck('tutte PENDING', not [u['idx'] for u in su
                         if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('spazi iniziali e finali identici al sorgente (19/19)',
   not [u['idx'] for u in tu
        if len(u['italian']) - len(u['italian'].rstrip()) != len(u['english']) - len(u['english'].rstrip())])
tabs = [u['idx'] for u in su if u['english'].startswith('\t')]
ck('17 unita con tab (le 2 UI_LABEL no)',
   len(tabs) == 17 and tabs == [u['idx'] for u in tu if u['italian'].startswith('\t')]
   and [u['idx'] for u in su if not u['english'].startswith('\t')] == [1, 8], len(tabs))
ck('1 contesto: 19 unita', list(collections.Counter(u['context'] for u in su).values()) == [19])
ck('19 testi inglesi distinti', len({u['english'] for u in tu}) == 19)
ck('i nomi restano inglesi: 3 nomi',
   all(n in ' '.join(u['italian'] for u in tu)
       for n in ('Tripulse Shredder', 'Sea Scorpion', 'Shield Beetle')))
ck('nessun carattere tipografico e nessun non latino fuori dai token',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')
        or any(ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F for c in TAGS.sub('', u['italian']))])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate', 0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
merged = {}
for f in sorted(os.listdir(os.path.join(HERE, 'parts'))):
    if f.endswith('.json'):
        for k, v in json.load(open(os.path.join(HERE, 'parts', f), encoding='utf-8')).items():
            merged[int(k)] = v
ck('le tre parti ricostruiscono translation.json (1..19)',
   sorted(merged) == list(range(1, 20)) and merged == {u['idx']: u['italian'] for u in tu})
ck('nessun altro lotto rivendica le righe 460-530',
   not [f for f in os.listdir(os.path.join(L10N, 'staging/editorial'))
        if f.startswith('L') and os.path.exists(os.path.join(L10N, 'staging/editorial', f, 'translation.json'))
        and os.path.abspath(os.path.join(L10N, 'staging', 'editorial', f)) != HERE
        and any(u['path'] == PATH and first <= u['line'] <= last for u in json.load(open(os.path.join(
            L10N, 'staging', 'editorial', f, 'translation.json'), encoding='utf-8'))['units'])])
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('FILE CHIUSO: 147/147 unita (100%) · 7 lotti · max(line) 530 · zero sovrapposizioni')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L146 superato — file chiuso' if not fail else 'verify L146 fallito')
raise SystemExit(0 if not fail else 1)
