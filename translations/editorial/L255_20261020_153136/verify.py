r"""verify.py — L255 (`data/wanderer/wanderer jobs.txt`, 1 unita', riga 891). **LOTTO TERMINALE**.

**Invariante di FILE**: dopo questo lotto `wanderer jobs.txt` deve avere **92 unita' distinte su 92**
(`26 + 24 + 41 + 1`), la riga **891** come ultima e **0** unita' dopo; le righe dei quattro lotti devono coincidere
**esattamente** con quelle del database (nessun buco interno).

Verifica da sola: la riga grezza, il tipo, il segnaposto unico, l'assenza di tab/virgolette/apici, il lessico
(`Wanderer` e `Kor Efreti` invariati, nessun `Wanderers`, nessun `Unfettered`) e il rapporto.

Indipendente da `check.py`: rilegge `source.json`, il `translation.json`, il database e il file del gioco.
"""
import collections
import glob
import hashlib
import json
import os
import re
import sqlite3

TAB = chr(9)
QUOTE = chr(34)
APOS = chr(39)
TAG = re.compile(r'<[^<>]+>')
HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
ROOT = os.path.abspath(os.path.join(L10N, '..'))
PATH = 'data/wanderer/wanderer jobs.txt'
src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
su = sorted(src['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
raw_lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
fail = []


def ck(n, c, d=''):
    print('%-96s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente (1/1)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck('unita: 1, riga 891', len(tu) == 1 and tu[0]['line'] == 891)
ck('tipo DIALOG, contesto della missione di L254',
   tu[0]['kind'] == 'DIALOG' and tu[0]['context'] == 'mission:Wanderers to Kor Efreti')
ck("91 unita' prima della 891: L252 (26) + L253 (24) + L254 (41)",
   db.execute('select count(*) from units where path=? and line<891', (PATH,)).fetchone()[0] == 91)
ck("ZERO unita' dopo la 891: il lotto CHIUDE il file",
   db.execute('select count(*) from units where path=? and line>891', (PATH,)).fetchone()[0] == 0)
ck("la 891 e' l'ultima riga (92 unita', righe 15 - 891)",
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (92, 15, 891))
per_lotto, righe = [], set()
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    us = [u for u in json.load(open(f, encoding='utf-8'))['units'] if u['path'] == PATH]
    if us:
        per_lotto.append((os.path.basename(os.path.dirname(f)), len(us)))
        righe |= {u['line'] for u in us}
ck('INVARIANTE DI FILE: 4 lotti (26 + 24 + 41 + 1) coprono 92 righe distinte su 92',
   [n for _, n in per_lotto] == [26, 24, 41, 1] and len(righe) == 92,
   (per_lotto, len(righe)))
ck('nessun buco: le 92 righe sono esattamente quelle del database',
   righe == {l for l, in db.execute('select line from units where path=?', (PATH,))})
overlap = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    lot = os.path.basename(os.path.dirname(f))
    if lot == os.path.basename(HERE):
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH and u['line'] == 891:
            overlap.append((lot, u['line']))
ck("nessun altro lotto rivendica la riga 891", not overlap, overlap)
ck("l'unita e' tradotta (non copiata)", tu[0]['italian'] != tu[0]['english'])
tok_en = collections.Counter(t for u in tu for t in TAG.findall(u['english']))
tok_it = collections.Counter(t for u in tu for t in TAG.findall(u['italian']))
ck("il segnaposto `<payment>` e' presente una volta, in entrambe le lingue",
   tok_en == tok_it == collections.Counter({'<payment>': 1}), (dict(tok_en), dict(tok_it)))
ck('ZERO tab, virgolette e apici in entrambe le lingue',
   sum(u['english'].count(TAB) for u in tu) == 0 == sum(u['italian'].count(TAB) for u in tu)
   and sum(u['english'].count(QUOTE) for u in tu) == 0 == sum(u['italian'].count(QUOTE) for u in tu)
   and sum(u['english'].count(APOS) for u in tu) == 0 == sum(u['italian'].count(APOS) for u in tu))
it = tu[0]['italian']
ck('lessico: «Wanderer» e «Kor Efreti» invariati, nessun `Wanderers`, nessun `Unfettered`',
   'Wanderer' in it and 'Kor Efreti' in it and 'Wanderers' not in it and 'Unfettered' not in it)
ck('nessun residuo inglese di struttura (the, and, you, them, when)',
   not [w for w in (' the ', ' and ', ' you ', ' them ', ' when ') if w in it.lower()],
   [w for w in (' the ', ' and ', ' you ', ' them ', ' when ') if w in it.lower()])
ck("nessun carattere tipografico e nessun non latino",
   not any(c in it for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')
   and not any(ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F for c in it))
ck('nessuno spazio finale e nessun doppio spazio', it == it.rstrip() and '  ' not in it)
ck('rapporto nel gate 0,55-1,90 (0,98; 20 -> 19 parole)', 0.55 < tu[0]['ratio'] < 1.90, tu[0]['ratio'])
ck("PENDING sull'unica unita'",
   db.execute('select state from units where id=?', (tu[0]['id'],)).fetchone()[0] == 'PENDING')
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print("FILE: 92/92 unita' · 4 lotti (26 + 24 + 41 + 1) · 92 righe distinte · ultima riga 891 · 0 dopo")
print('parole EN %d -> IT %d · rapporto %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu), tu[0]['ratio']))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L255 superato' if not fail else 'verify L255 fallito')
raise SystemExit(0 if not fail else 1)
