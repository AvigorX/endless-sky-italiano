r"""verify.py — L190 (`data/gegno/gegno outfits.txt`, 1 unita', riga 1137). **CHIUDE IL FILE: 60/60.**

Invariante di **FILE**: le **6 finestre** del file (L185…L190) devono coprire **tutte e 60** le unita' del database, su
**60 righe distinte**, con `min(line) = 17` e `max(line) = 1137`. Il lotto e' terminale: **non esiste** un'unita' dopo
la 1137, e questa e' l'asserzione che sostituisce il confronto con il confine.
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
ED = os.path.join(L10N, 'staging/editorial')
PATH = 'data/gegno/gegno outfits.txt'
WINDOWS = ['L185_20261019_193201', 'L186_20261019_193316', 'L187_20261019_193503',
           'L188_20261019_193540', 'L189_20261019_193709', 'L190_20261019_193747']
su = sorted(json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
by = {u['idx']: u for u in tu}
lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
fail = []


def ck(n, c, d=''):
    print('%-70s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente (1/1)', not [u for u in su if lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck('unita: riga 1137, contesto `outfit:Scin Adjutant License`',
   len(tu) == 1 and tu[0]['line'] == 1137 and tu[0]['context'] == 'outfit:Scin Adjutant License')
ck('le 59 unita precedenti sono coperte da L185…L189', db.execute(
    'select count(*) from units where path=? and line<1137', (PATH,)).fetchone()[0] == 59)

# --- invariante di FILE: somma delle 6 finestre ---
allu, per_win = [], {}
for w in WINDOWS:
    d = json.load(open(os.path.join(ED, w, 'translation.json'), encoding='utf-8'))['units']
    per_win[w] = len(d)
    allu += [(w, u['line']) for u in d if u['path'] == PATH]
ck('6 finestre: L185 13, L186 14, L187 7, L188 13, L189 12, L190 1',
   list(per_win.values()) == [13, 14, 7, 13, 12, 1], per_win)
ck('somma delle finestre = 60 unita', len(allu) == 60, len(allu))
ck('60 righe DISTINTE (nessuna rivendicata due volte)', len({l for _, l in allu}) == 60,
   len({l for _, l in allu}))
dbl = {r[0] for r in db.execute('select line from units where path=?', (PATH,))}
ck('le 60 righe sono ESATTAMENTE quelle del database (nessun buco)',
   {l for _, l in allu} == dbl, sorted(dbl - {l for _, l in allu})[:5])
ck('min(line) = 17 e max(line) = 1137 su tutto il file',
   db.execute('select min(line),max(line) from units where path=?', (PATH,)).fetchone() == (17, 1137))
ck("lotto TERMINALE: nessuna unita' dopo la riga 1137",
   db.execute('select count(*) from units where path=? and line>1137', (PATH,)).fetchone()[0] == 0)
ck('tipi del lotto: 1 DESCRIPTION, zero VALUE',
   collections.Counter(u['kind'] for u in su) == {'DESCRIPTION': 1})
ck('zero tab e zero virgolette; 0 apici inglesi, 1 italiano (elisione)',
   [u['idx'] for u in su if chr(9) in u['english']] == []
   and [u['idx'] for u in tu if chr(9) in u['italian']] == []
   and sum(v['english'].count(chr(39)) for v in su) == 0
   and sum(v['italian'].count(chr(39)) for v in tu) == 1)
ck('«Gegno Scin» invariato nella resa',
   'Gegno Scin' in by[1]['italian'])
ck('PENDING', db.execute('select state from units where id=?', (su[0]['id'],)).fetchone()[0] == 'PENDING')
ck('nessuno spazio finale', tu[0]['english'] == tu[0]['english'].rstrip()
   and tu[0]['italian'] == tu[0]['italian'].rstrip())
ck('nessun carattere tipografico e nessun non latino',
   not any(c in tu[0]['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')
   and not any(ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F for c in tu[0]['italian']))
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate', 0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
merged = {}
for f in sorted(os.listdir(os.path.join(HERE, 'parts'))):
    if f.endswith('.json'):
        for k, v in json.load(open(os.path.join(HERE, 'parts', f), encoding='utf-8')).items():
            merged[int(k)] = v
ck('le parti ricostruiscono translation.json',
   merged == {u['idx']: u['italian'] for u in tu})
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('FILE CHIUSO: 60/60 unita (100%) in 6 finestre · 1 nel lotto · 0 dopo la riga 1137')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L190 superato' if not fail else 'verify L190 fallito')
raise SystemExit(0 if not fail else 1)
