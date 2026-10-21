r"""verify.py — L179 (`data/avgi/avgi ships.txt`, 5 unita', righe 2716-2770). **CHIUDE IL FILE.**

Invariante di **FILE**: le **6 finestre** (L174…L179) devono sommare **102 unita'** su **102 righe distinte**, con
`min(line) = 120` e `max(line) = 2770`; nessuna unita' oltre la 2770 (ultima del file), nessuna riga rivendicata due
volte, copertura esatta dell'insieme delle righe del file.
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
PATH = 'data/avgi/avgi ships.txt'
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


ck('riga grezza identica al sorgente (5/5)', not [u for u in su if lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck('idx 1..5 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 6)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 5 righe 2716 - 2770', len(tu) == 5 and (first, last) == (2716, 2770), (len(tu), first, last))
ck('97 unita prima della riga 2716 (L174…L178)', db.execute(
    'select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0] == 97)
ck('102 unita nel file, ZERO dopo la riga 2770 (fine file)', db.execute(
    'select count(*) from units where path=?', (PATH,)).fetchone()[0] == 102
   and db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0] == 0)
ck('max(line) del file = 2770, min(line) = 120', db.execute(
    'select min(line),max(line) from units where path=?', (PATH,)).fetchone() == (120, 2770))
lots, claimed = [], []
for f in sorted(os.listdir(os.path.join(L10N, 'staging/editorial'))):
    p = os.path.join(L10N, 'staging/editorial', f, 'translation.json')
    if not os.path.isdir(os.path.join(L10N, 'staging/editorial', f)) or not os.path.exists(p):
        continue
    us = [u for u in json.load(open(p, encoding='utf-8'))['units'] if u['path'] == PATH]
    if us:
        lots.append((f, len(us)))
        claimed.extend(u['line'] for u in us)
ck('6 lotti su questo file (L174…L179)', len(lots) == 6
   and [f[:4] for f, _ in lots] == ['L174', 'L175', 'L176', 'L177', 'L178', 'L179'], lots)
ck('somma delle finestre = 102 unita del file', sum(n for _, n in lots) == 102, [n for _, n in lots])
ck('zero sovrapposizioni: 102 righe rivendicate, 102 distinte',
   len(claimed) == 102 == len(set(claimed)), (len(claimed), len(set(claimed))))
ck('copertura esatta: min 120, max 2770, nessun buco',
   (min(claimed), max(claimed)) == (120, 2770)
   and sorted(set(claimed)) == sorted(r[0] for r in db.execute(
       'select line from units where path=?', (PATH,)).fetchall()))
ck('tipi: 4 DESCRIPTION + 1 VALUE', collections.Counter(u['kind'] for u in su)
   == {'DESCRIPTION': 4, 'VALUE': 1})
ck('ZERO UI_LABEL, ZERO virgolette, ZERO token, 2 tab',
   [u['idx'] for u in su if u['kind'] == 'UI_LABEL'] == []
   and sum(u['english'].count('"') for u in su) == 0 == sum(u['italian'].count('"') for u in tu)
   and {t for u in su for t in TAGS.findall(u['english'])} == set()
   and [u['idx'] for u in su if u['english'].startswith('\t')] == [2, 5]
   == [u['idx'] for u in tu if u['italian'].startswith('\t')])
ck('il boilerplate dei droni e identico in idx 2 e 5',
   by[2]['english'] == by[5]['english'] and by[2]['italian'] == by[5]['italian'])
ck('l VALUE e identico al sorgente',
   [u['idx'] for u in tu if u['kind'] == 'VALUE' and u['italian'] != u['english']] == [])
ck('4 testi distinti, 2 contesti', len({u['english'] for u in tu}) == 4
   and len({u['context'] for u in tu}) == 2)
ck('nessun possessivo inglese in italiano',
   not [u['idx'] for u in tu if re.search(r"[A-Za-z]+'s\b", u['italian'])])
ck('tutte PENDING', not [u['idx'] for u in su
                         if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('nessuno spazio finale, tab iniziale ammesso',
   not [u['idx'] for u in tu
        if u['english'].rstrip('\t') != u['english'].rstrip('\t').rstrip()
        or u['italian'].rstrip('\t') != u['italian'].rstrip('\t').rstrip()])
ck('nessun carattere tipografico e nessun non latino',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')
        or any(ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F for c in u['italian'])])
rs = [u['ratio'] for u in tu if u['kind'] == 'DESCRIPTION']
ck('rapporto nel gate (solo DESCRIPTION)', 0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
merged = {}
for f in sorted(os.listdir(os.path.join(HERE, 'parts'))):
    if f.endswith('.json'):
        for k, v in json.load(open(os.path.join(HERE, 'parts', f), encoding='utf-8')).items():
            merged[int(k)] = v
ck('le parti ricostruiscono translation.json (1..5)',
   sorted(merged) == list(range(1, 6)) and merged == {u['idx']: u['italian'] for u in tu})
ck('nessun altro lotto rivendica le righe 2716-2770',
   not [f for f in os.listdir(os.path.join(L10N, 'staging/editorial'))
        if f.startswith('L') and os.path.exists(os.path.join(L10N, 'staging/editorial', f, 'translation.json'))
        and os.path.abspath(os.path.join(L10N, 'staging/editorial', f)) != HERE
        and any(u['path'] == PATH and first <= u['line'] <= last for u in json.load(open(os.path.join(
            L10N, 'staging/editorial', f, 'translation.json'), encoding='utf-8'))['units'])])
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('file CHIUSO: 102/102 unita (100%) · 6 finestre (L174…L179) · 97 prima / 5 nel lotto / 0 dopo · max(line) 2770')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L179 superato' if not fail else 'verify L179 fallito')
raise SystemExit(0 if not fail else 1)
