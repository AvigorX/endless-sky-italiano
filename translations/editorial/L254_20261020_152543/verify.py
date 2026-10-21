r"""verify.py — L254 (`data/wanderer/wanderer jobs.txt`, 41 unita', righe 458-888). Terzo lotto del file.

**Invariante di SEGMENTO** (il file NON e' chiuso, ma quasi: 92 unita'): **50** prima della 458 (L252 26 + L253 24), **41**
qui, **1** dopo la 888, confine misurato alla **891** (`mission:Wanderers to Kor Efreti`). Copertura stampata (91/92, 98,9%):
**dopo questo lotto resta una sola unita'**, quindi il successivo e' il lotto **terminale**.

Verifica da sola: i **18 `VALUE`** copiati (6 distinti), le **22 unita' di prosa** tradotte, il **`TEXT`** del blocco
`phrase` tradotto, **17 stringhe distinte** con **6 gruppi** di molteplicita' 8/8/4/4/3/3, i **83 segnaposto** per famiglia
**e per ordine**, **zero tab e virgolette**, **3 apici inglesi** contro **1 italiano**, e le **due schede generiche**
confrontate con la **forma dominante del corpus** calcolata a runtime (39 e 17 occorrenze).
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
G1 = 'Deliver <cargo> to <destination>. Payment is <payment>.'
G2 = 'Deliver <cargo> to <destination> by <date>. Payment is <payment>.'
src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
su = sorted(src['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
raw_lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
fail = []


def ck(n, c, d=''):
    print('%-96s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


def corpus(english):
    c = collections.Counter()
    for f in glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json')):
        if os.path.basename(os.path.dirname(f)) == os.path.basename(HERE):
            continue
        for u in json.load(open(f, encoding='utf-8'))['units']:
            if u['english'] == english:
                c[u['italian']] += 1
    return c


ck('riga grezza identica al sorgente (41/41)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck("unita: 41, righe 458 - 888", len(tu) == 41 and (tu[0]['line'], tu[-1]['line']) == (458, 888))
ck('18 VALUE + 18 DESCRIPTION + 4 DIALOG + 1 TEXT',
   collections.Counter(u['kind'] for u in su) == {'VALUE': 18, 'DESCRIPTION': 18, 'DIALOG': 4, 'TEXT': 1})
ck('20 contesti distinti (19 missioni + il blocco `phrase`)', len(set(u['context'] for u in su)) == 20
   and sum(1 for c in set(u['context'] for u in su) if c.startswith('phrase:')) == 1,
   len(set(u['context'] for u in su)))
ck("50 unita' prima della 458: L252 (26) + L253 (24)",
   db.execute('select count(*) from units where path=? and line<458', (PATH,)).fetchone()[0] == 50)
ck("1 unita' dopo la 888: ne resta solo una al file",
   db.execute('select count(*) from units where path=? and line>888', (PATH,)).fetchone()[0] == 1)
nxt = db.execute('select line,context from units where path=? and line>888 order by line limit 1', (PATH,)).fetchone()
ck('confine misurato: riga 891, mission:Wanderers to Kor Efreti',
   nxt == (891, 'mission:Wanderers to Kor Efreti'), nxt)
ck('il file intero: 92 unita, righe 15 - 891',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (92, 15, 891))
mine = set(u['line'] for u in tu)
overlap = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    lot = os.path.basename(os.path.dirname(f))
    if lot == os.path.basename(HERE):
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH and u['line'] in mine:
            overlap.append((lot, u['line']))
ck("nessun ALTRO lotto rivendica le righe di questo segmento (41 righe distinte)",
   not overlap and len(mine) == 41, (overlap[:3], len(mine)))
VAL = [u for u in tu if u['kind'] == 'VALUE']
PROSA = [u for u in tu if u['kind'] in ('DESCRIPTION', 'DIALOG')]
TXT = [u for u in tu if u['kind'] == 'TEXT']
ck("i 18 VALUE sono copiati carattere per carattere (6 distinti)",
   len(VAL) == 18 and all(u['italian'] == u['english'] for u in VAL)
   and len({u['english'] for u in VAL}) == 6,
   [u['idx'] for u in VAL if u['italian'] != u['english']])
ck("le 22 unita' di prosa sono tradotte", all(u['italian'] != u['english'] for u in PROSA)
   and len(PROSA) == 22)
ck("il TEXT del blocco `phrase` e' tradotto e resta una frase intera (inizia e finisce con punto)",
   len(TXT) == 1 and TXT[0]['italian'] != TXT[0]['english']
   and TXT[0]['italian'].endswith('.') and TXT[0]['italian'].startswith('Scarichi'))
mult = collections.Counter(u['english'] for u in tu)
gruppi = [e for e, n in mult.items() if n > 1]
ck('17 stringhe distinte, 6 gruppi con molteplicita\' 8/8/4/4/3/3, una resa ciascuno',
   len(mult) == 17 and sorted(mult[e] for e in gruppi) == [3, 3, 4, 4, 8, 8]
   and all(len({u['italian'] for u in tu if u['english'] == e}) == 1 for e in gruppi),
   (len(mult), sorted(mult[e] for e in gruppi)))
ck('COERENZA CROSS-LOT (calcolata a runtime): le 8 schede generiche usano la resa a 39 occorrenze',
   len({u['italian'] for u in tu if u['english'] == G1}) == 1
   and corpus(G1).most_common(1)[0][0] == [u['italian'] for u in tu if u['english'] == G1][0],
   corpus(G1).most_common(2))
ck('COERENZA CROSS-LOT: le 4 schede «rush» usano la resa a 17 occorrenze',
   corpus(G2).most_common(1)[0][0] == [u['italian'] for u in tu if u['english'] == G2][0],
   corpus(G2).most_common(2))
tok_en = collections.Counter(t for u in tu for t in TAG.findall(u['english']))
tok_it = collections.Counter(t for u in tu for t in TAG.findall(u['italian']))
ck('83 segnaposto in 9 famiglie, multiset identico',
   tok_en == tok_it and sum(tok_en.values()) == 83 and len(tok_en) == 9,
   (dict(tok_en), sum(tok_en.values())))
ck('`<cargo>` e `<destination>` sono 15 e 15: il confronto per ordine e\' indispensabile',
   tok_en['<cargo>'] == tok_en['<destination>'] == 15)
seq_bad = [u['idx'] for u in tu if TAG.findall(u['english']) != TAG.findall(u['italian'])]
ck("l'ORDINE dei segnaposto e' identico dentro ogni unita'", not seq_bad, seq_bad)
ck('ZERO tab e ZERO virgolette (due asserzioni negative scritte)',
   sum(u['english'].count(TAB) for u in tu) == 0 == sum(u['italian'].count(TAB) for u in tu)
   and sum(u['english'].count(QUOTE) for u in tu) == 0 == sum(u['italian'].count(QUOTE) for u in tu))
a_en = [(u['idx'], u['english'].count(APOS)) for u in tu if APOS in u['english']]
a_it = [(u['idx'], u['italian'].count(APOS)) for u in tu if APOS in u['italian']]
ck("3 apici inglesi (29: 1, 41: 2) e 1 italiano (unita' 1: `un'ora`)",
   a_en == [(29, 1), (41, 2)] and a_it == [(1, 1)], (a_en, a_it))
prosa = ' '.join(u['italian'] for u in PROSA)
ck("«Slegati» nella prosa, `Unfettered` solo nel VALUE copiato",
   'Slegati' in prosa and 'Unfettered' not in prosa
   and any('Unfettered' in u['italian'] for u in VAL))
ck('lessico: «governatore», «Kor Efreti», «Korath», «stiva», «capitale»',
   all(t in prosa for t in ('governatore', 'Kor Efreti', 'Korath', 'stiva', 'capitale')))
ck('`Wanderer` invariato (`Wanderers` non compare nella prosa)',
   prosa.count('Wanderer') >= 6 and 'Wanderers' not in prosa)
ck("PENDING su tutte e 41", not [u['idx'] for u in su
                                 if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0]
                                 != 'PENDING'])
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in tu if u['italian'].rstrip() != u['italian'] or '  ' in u['italian']])
ck('nessun carattere tipografico e nessun non latino',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')
        or any(ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F for c in u['italian'])])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate 0,55-1,90 (0,94 - 1,17; 426 -> 434 parole)',
   0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print("SEGMENTO: %d/92 unita' del file (%.1f%%) · 50 prima · 41 qui · 1 dopo · confine riga 891"
      % (len(mine), 100.0 * len(mine) / 92))
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L254 superato' if not fail else 'verify L254 fallito')
raise SystemExit(0 if not fail else 1)
