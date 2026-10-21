r"""verify.py — L202 (`data/hai/hai outfits.txt`, 16 unita', righe 205-484). Secondo lotto; il file resta aperto.

Il file ha ora **due finestre reali** (L201 8 unita', L202 16) e **41 unita' residue**. Si verificano percio':

1. **8 unita' prima della 205** coperte da L201 (letto dal suo `translation.json`);
2. **41 unita' dopo la 484** (57 - 16);
3. **file intero**: 65 unita', `min(line) = 27`, `max(line) = 984`;
4. **L201 + L202 + residuo = 65 righe distinte**, nessuna rivendicata due volte.

Il **confine** e' misurato: la prima unita' dopo la 484 e' la riga **508**, una `DESCRIPTION` del contesto
`outfit:Chameleon Anti-Missile`.
"""
import collections
import hashlib
import json
import os
import sqlite3

TAB = chr(9)
HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
ROOT = os.path.abspath(os.path.join(L10N, '..'))
ED = os.path.join(L10N, 'staging/editorial')
PATH = 'data/hai/hai outfits.txt'
PREV = 'L201_20261019_204959'
su = sorted(json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
fail = []


def ck(n, c, d=''):
    print('%-72s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente (16/16)', not [u for u in su if lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck('unita: 16 righe 205 - 484', len(tu) == 16 and (tu[0]['line'], tu[-1]['line']) == (205, 484))
ck('8 unita prima della 205, coperte da L201', db.execute(
    'select count(*) from units where path=? and line<205', (PATH,)).fetchone()[0] == 8)
ck('41 unita dopo la 484 (57 - 16)', db.execute(
    'select count(*) from units where path=? and line>484', (PATH,)).fetchone()[0] == 41)
nxt = db.execute('select line,kind,context from units where path=? and line>484 order by line limit 1',
                 (PATH,)).fetchone()
ck('confine misurato: riga 508, DESCRIPTION di "Chameleon Anti-Missile"',
   nxt == (508, 'DESCRIPTION', 'outfit:Chameleon Anti-Missile'), nxt)
ck('il file intero: 65 unita, min(line) 27, max(line) 984',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (65, 27, 984),
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone())
prev = [u for u in json.load(open(os.path.join(ED, PREV, 'translation.json'), encoding='utf-8'))['units']
        if u['path'] == PATH]
ck('finestra L201 letta dal suo translation.json: 8 unita', len(prev) == 8, len(prev))
lot = {u['line'] for u in tu}
prv = {u['line'] for u in prev}
rest = {r[0] for r in db.execute('select line from units where path=? and line>484', (PATH,))}
ck('L201, L202 e residuo sono DISGIUNTI a due a due',
   not (lot & prv) and not (lot & rest) and not (prv & rest),
   (sorted(lot & prv)[:3], sorted(lot & rest)[:3], sorted(prv & rest)[:3]))
ck('8 + 16 + 41 = 65 righe = tutto il file (nessun buco)',
   len(prv | lot | rest) == 65 and len(prv) + len(lot) + len(rest) == 65,
   (len(prv), len(lot), len(rest), len(prv | lot | rest)))
ck('tipi del lotto: 13 DESCRIPTION, 3 VALUE',
   collections.Counter(u['kind'] for u in su) == {'DESCRIPTION': 13, 'VALUE': 3})
ck('0 segnaposto, 4 tab, 0 virgolette, 2 apici EN / 10 IT',
   sum(u['english'].count('<') for u in su) == 0 == sum(u['italian'].count('<') for u in tu)
   and [u['idx'] for u in su if u['english'].startswith(TAB)] == [3, 10, 11, 15]
   and sum(u['english'].count('"') for u in su) == 0 == sum(u['italian'].count('"') for u in tu)
   and sum(u['english'].count(chr(39)) for u in su) == 2
   and sum(u['italian'].count(chr(39)) for u in tu) == 10)
ck('3 VALUE restano inglesi alla lettera',
   all(u['italian'] == u['english'] for u in tu if u['kind'] == 'VALUE'))
ck('PENDING su tutte e 16', not [u['idx'] for u in su
                                 if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('nessuno spazio finale e nessun doppio spazio (tab iniziali ammessi)',
   not [u['idx'] for u in tu if u['italian'].rstrip(TAB) != u['italian'].rstrip(TAB).rstrip()
        or '  ' in u['italian']])
ck('nessun carattere tipografico e nessun non latino',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')
        or any(ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F for c in u['italian'])])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate 0,55-1,90', 0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('APERTO: 24/65 unita del file (36.9%) · 41 dopo la riga 484 · confine riga 508')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L202 superato' if not fail else 'verify L202 fallito')
raise SystemExit(0 if not fail else 1)
