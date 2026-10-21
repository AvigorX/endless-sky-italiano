r"""verify.py — L184 (`data/human/outfits.txt`, 13 unita', righe 520-606). **CHIUDE IL FILE: 63/63.**

Invariante di **FILE**: le **5 finestre** del file (L180, L181, L182, L183, L184) devono coprire **tutte e 63** le unita'
del database, su **63 righe distinte**, con `min(line) = 15` e `max(line) = 606`. Il lotto e' terminale: **non esiste**
un'unita' dopo la 606, e questa e' l'asserzione che sostituisce il confronto con il confine.
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
PATH = 'data/human/outfits.txt'
WINDOWS = ['L180_20261019_190943', 'L181_20261019_191337', 'L182_20261019_191839',
           'L183_20261019_192229', 'L184_20261019_192644']
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


ck('riga grezza identica al sorgente (13/13)', not [u for u in su if lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck('idx 1..13 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 14)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 13 righe 520 - 606', len(tu) == 13 and (first, last) == (520, 606), (len(tu), first, last))
ck('50 unita prima (chiuse da L180, L181, L182, L183)', db.execute(
    'select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0] == 50)

# --- invariante di FILE: somma delle 5 finestre ---
allu, per_win = [], {}
for w in WINDOWS:
    d = json.load(open(os.path.join(ED, w, 'translation.json'), encoding='utf-8'))['units']
    per_win[w] = len(d)
    allu += [(w, u['line']) for u in d if u['path'] == PATH]
ck('5 finestre presenti: L180 12, L181 9, L182 14, L183 15, L184 13',
   list(per_win.values()) == [12, 9, 14, 15, 13], per_win)
ck('somma delle finestre = 63 unita', len(allu) == 63, len(allu))
ck('63 righe DISTINTE (nessuna rivendicata due volte)', len({l for _, l in allu}) == 63,
   len({l for _, l in allu}))
dbl = {r[0] for r in db.execute('select line from units where path=?', (PATH,))}
ck('le 63 righe sono ESATTAMENTE quelle del database (nessun buco)',
   {l for _, l in allu} == dbl, sorted(dbl - {l for _, l in allu})[:5])
ck('min(line) = 15 e max(line) = 606 su tutto il file',
   db.execute('select min(line),max(line) from units where path=?', (PATH,)).fetchone() == (15, 606))
ck('lotto TERMINALE: nessuna unita dopo la riga 606',
   db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0] == 0)
ck('tipi del lotto: 12 DESCRIPTION + 1 VALUE', collections.Counter(u['kind'] for u in su)
   == {'DESCRIPTION': 12, 'VALUE': 1})
ck('il VALUE e\' `"Puny"` con le virgolette dentro il nome',
   by[1]['italian'] == by[1]['english'] == '"Puny"')
ck('2 virgolette, tutte in idx 1; 1 tab (idx 3); 7 apici inglesi',
   sum(u['english'].count('"') for u in su) == 2 == sum(u['italian'].count('"') for u in tu)
   and [u['idx'] for u in su if u['english'].startswith('\t')] == [3]
   and {u['idx']: u['english'].count("'") for u in su if "'" in u['english']} == {3: 2, 7: 2, 10: 2, 13: 1})
ck('nessun possessivo inglese in italiano; 3 apici italiani di elisione',
   not [u['idx'] for u in tu if re.search(r"\b[A-Za-z]'s\b", u['italian']) or re.search(r"[A-Za-z]+'s\b", u['italian'])]
   and {u['idx']: u['italian'].count("'") for u in tu if "'" in u['italian']} == {9: 1, 13: 2})
ck('13 testi distinti, 11 contesti (Puny con 3)', len({u['english'] for u in tu}) == 13
   and len({u['context'] for u in tu}) == 11
   and sorted(collections.Counter(u['context'] for u in tu).values()) == [1] * 10 + [3])
ck('tutte PENDING', not [u['idx'] for u in su
                         if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('nessuno spazio finale (tab iniziale ammesso)',
   not [u['idx'] for u in tu if u['english'].rstrip('\t') != u['english'].rstrip('\t').rstrip()
        or u['italian'].rstrip('\t') != u['italian'].rstrip('\t').rstrip()])
ck('nessun carattere tipografico e nessun non latino',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')
        or any(ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F for c in u['italian'])])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate', 0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
merged = {}
for f in sorted(os.listdir(os.path.join(HERE, 'parts'))):
    if f.endswith('.json'):
        for k, v in json.load(open(os.path.join(HERE, 'parts', f), encoding='utf-8')).items():
            merged[int(k)] = v
ck('le parti ricostruiscono translation.json (1..13)',
   sorted(merged) == list(range(1, 14)) and merged == {u['idx']: u['italian'] for u in tu})
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('FILE CHIUSO: 63/63 unita (100%) in 5 finestre · 13 nel lotto · 0 dopo la riga 606')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L184 superato' if not fail else 'verify L184 fallito')
raise SystemExit(0 if not fail else 1)
