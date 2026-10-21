r"""verify.py — L249 (`data/human/syndicate jobs.txt`, 19 unita', righe 291-431). Terzo lotto del file.

**Invariante di SEGMENTO** (il file NON e' chiuso: 94 unita'): **36** prima della 291 (L247 16 + L248 20), **19** qui,
**39** dopo la 431, confine misurato alla **435** (`mission:Syndicate Prisoner Transport [3]`, con le parentesi quadre).

**Il controllo centrale e' cross-lot**: 10 unita' ripetono una stringa inglese gia' tradotta in L248, e la resa deve essere
**identica carattere per carattere** — il file di L248 si rilegge da qui, non si assume.

Verifica da sola anche: i **4 `VALUE`** copiati, le **15 unita' di prosa tradotte**, i **4 gruppi interni** con una resa,
i **22 segnaposto** per famiglia **e per ordine**, **zero tab**, le **2 virgolette** di «"arresti domiciliari"», **2 apici
inglesi** contro **zero** italiani, e l'accordo al femminile plurale di `<bunks>` («spie … condannate … tenute»).
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
PREV = os.path.join(L10N, 'staging', 'editorial', 'L248_20261020_145616', 'translation.json')
PATH = 'data/human/syndicate jobs.txt'
src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
su = sorted(src['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
raw_lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
fail = []


def ck(n, c, d=''):
    print('%-94s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente (19/19)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck("unita: 19, righe 291 - 431", len(tu) == 19 and (tu[0]['line'], tu[-1]['line']) == (291, 431))
ck('4 VALUE + 11 DIALOG + 4 DESCRIPTION',
   collections.Counter(u['kind'] for u in su) == {'VALUE': 4, 'DIALOG': 11, 'DESCRIPTION': 4})
ck('5 contesti distinti, tre con parentesi quadre',
   len(set(u['context'] for u in su)) == 5
   and sum(1 for c in set(u['context'] for u in su) if '[' in c) == 5,
   sorted(set(u['context'] for u in su)))
ck("36 unita' prima della 291: L247 (16) + L248 (20)",
   db.execute('select count(*) from units where path=? and line<291', (PATH,)).fetchone()[0] == 36)
ck("39 unita' dopo la 431: il lotto NON chiude il file",
   db.execute('select count(*) from units where path=? and line>431', (PATH,)).fetchone()[0] == 39)
nxt = db.execute('select line,context from units where path=? and line>431 order by line limit 1', (PATH,)).fetchone()
ck("confine misurato: riga 435, mission:Syndicate Prisoner Transport [3] (parentesi grezze)",
   nxt == (435, 'mission:Syndicate Prisoner Transport [3]'), nxt)
ck('il file intero: 94 unita, righe 19 - 814',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (94, 19, 814))
mine = set(u['line'] for u in tu)
overlap = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    lot = os.path.basename(os.path.dirname(f))
    if lot == os.path.basename(HERE):
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH and u['line'] in mine:
            overlap.append((lot, u['line']))
ck("nessun ALTRO lotto rivendica le righe di questo segmento (19 righe distinte)",
   not overlap and len(mine) == 19, (overlap[:3], len(mine)))
# --- coerenza cross-lot, riletta dal file di L248 ---
prev = {u['english']: u['italian'] for u in json.load(open(PREV, encoding='utf-8'))['units']}
riuso = [u for u in tu if u['english'] in prev]
diversi = [(u['idx'], u['italian'][:60], prev[u['english']][:60]) for u in riuso if u['italian'] != prev[u['english']]]
ck("COERENZA CROSS-LOT: le 10 unita' ripetute da L248 hanno la resa IDENTICA",
   len(riuso) == 10 and not diversi, (len(riuso), diversi[:1]))
distinte = {u['english'] for u in tu}
in_prev = {e for e in distinte if e in prev}
ck("delle 15 stringhe distinte, 6 vengono da L248 e 9 sono nuove",
   len(distinte) == 15 and len(in_prev) == 6 and len(distinte) - len(in_prev) == 9,
   (len(distinte), len(in_prev)))
VAL = [u for u in tu if u['kind'] == 'VALUE']
PROSA = [u for u in tu if u['kind'] in ('DESCRIPTION', 'DIALOG')]
ck("i 4 VALUE sono copiati carattere per carattere",
   len(VAL) == 4 and all(u['italian'] == u['english'] for u in VAL),
   [u['idx'] for u in VAL if u['italian'] != u['english']])
ck("le 15 unita' di prosa sono tradotte", all(u['italian'] != u['english'] for u in PROSA)
   and len(PROSA) == 15)
mult = collections.Counter(u['english'] for u in tu)
gruppi = [e for e, n in mult.items() if n > 1]
ck('4 gruppi interni di inglese identico, una resa ciascuno, molteplicita\' massima 2',
   len(gruppi) == 4 and max(mult.values()) == 2
   and all(len({u['italian'] for u in tu if u['english'] == e}) == 1 for e in gruppi),
   (len(gruppi), mult.most_common(2)))
tok_en = collections.Counter(t for u in tu for t in TAG.findall(u['english']))
tok_it = collections.Counter(t for u in tu for t in TAG.findall(u['italian']))
ck('22 segnaposto in 5 famiglie, multiset identico',
   tok_en == tok_it and sum(tok_en.values()) == 22 and len(tok_en) == 5,
   (dict(tok_en), sum(tok_en.values())))
seq_bad = [u['idx'] for u in tu if TAG.findall(u['english']) != TAG.findall(u['italian'])]
ck("l'ordine dei segnaposto e' identico dentro ogni unita'", not seq_bad, seq_bad)
ck('ZERO tab (asserzione negativa scritta)',
   sum(u['english'].count(TAB) for u in tu) == 0 == sum(u['italian'].count(TAB) for u in tu))
q_it = [(u['idx'], u['italian'].count(QUOTE)) for u in tu if QUOTE in u['italian']]
ck('2 virgolette nella sola unita\' 12: «"arresti domiciliari"»',
   q_it == [(12, 2)] and '"arresti domiciliari"' in tu[11]['italian'], q_it)
a_en = [(u['idx'], u['english'].count(APOS)) for u in tu if APOS in u['english']]
a_it = [(u['idx'], u['italian'].count(APOS)) for u in tu if APOS in u['italian']]
ck("2 apici inglesi (2, 8: `You'll`) e ZERO italiani",
   a_en == [(2, 1), (8, 1)] and a_it == [], (a_en, a_it))
prosa = ' '.join(u['italian'] for u in PROSA)
ck("`You'll` reso con «Dovrai», senza apostrofo",
   'Dovrai tornare là' in prosa and 'll ' not in prosa)
ck("«Ricevi il pagamento di <payment>.» nelle 2 unita' attese (16, 19)",
   [u['idx'] for u in PROSA if 'Ricevi il pagamento di <payment>.' in u['italian']] == [16, 19])
ck('accordo al femminile plurale: «spie … condannate … tenute»',
   'spie aziendali condannate' in prosa and 'tenute in strutture' in prosa)
ck('lessico: «arresti domiciliari», «colletti bianchi», «sabotatore», «incatenati», `Syndicate` assente',
   all(t in prosa for t in ('arresti domiciliari', 'colletti bianchi', 'sabotatore', 'incatenati'))
   and not re.search(r'\bSyndicate\b', prosa))
ck("PENDING su tutte e 19", not [u['idx'] for u in su
                                 if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0]
                                 != 'PENDING'])
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in tu if u['italian'].rstrip() != u['italian'] or '  ' in u['italian']])
ck('nessun carattere tipografico e nessun non latino',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')
        or any(ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F for c in u['italian'])])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate 0,55-1,90 (0,93 - 1,18; 438 -> 419 parole)',
   0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print("SEGMENTO: %d/94 unita' del file (%.1f%%) · 36 prima · 19 qui · 39 dopo · confine riga 435"
      % (len(mine), 100.0 * len(mine) / 94))
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L249 superato' if not fail else 'verify L249 fallito')
raise SystemExit(0 if not fail else 1)
