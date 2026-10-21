r"""verify.py — L252 (`data/wanderer/wanderer jobs.txt`, 26 unita', righe 15-261). **Primo lotto del file.**

**Invariante di SEGMENTO** (il file NON e' chiuso: 92 unita'): **0** prima della 15 — il lotto **apre** il file —, **26**
qui, **66** dopo la 261, confine misurato alla **264** (`mission:Wanderer Biologists [0]`). Copertura stampata (26/92, 28,3%).

Verifica da sola: i **10 `VALUE`** copiati (5 distinti), le **16 unita' di prosa tradotte**, i **12 gruppi** di inglese
identico (11 con 2 copie, **1 con 4**) con una resa ciascuno, i **58 segnaposto** per famiglia **e per ordine**
(`<bunks>` e `<destination>` sono 10 e 10: il multiset da solo sarebbe cieco), **zero tab e zero virgolette**, **zero apici
inglesi** contro **4 italiani**, e `Wanderer` invariato al singolare e al plurale.
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
    print('%-94s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente (26/26)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck("unita: 26, righe 15 - 261", len(tu) == 26 and (tu[0]['line'], tu[-1]['line']) == (15, 261))
ck('10 VALUE + 10 DESCRIPTION + 6 DIALOG',
   collections.Counter(u['kind'] for u in su) == {'VALUE': 10, 'DESCRIPTION': 10, 'DIALOG': 6})
ck('10 contesti distinti', len(set(u['context'] for u in su)) == 10,
   sorted(set(u['context'] for u in su)))
ck("ZERO unita' prima della 15: e' la prima riga del file",
   db.execute('select count(*) from units where path=? and line<15', (PATH,)).fetchone()[0] == 0)
ck("66 unita' dopo la 261: il lotto NON chiude il file",
   db.execute('select count(*) from units where path=? and line>261', (PATH,)).fetchone()[0] == 66)
nxt = db.execute('select line,context from units where path=? and line>261 order by line limit 1', (PATH,)).fetchone()
ck('confine misurato: riga 264, mission:Wanderer Biologists [0]',
   nxt == (264, 'mission:Wanderer Biologists [0]'), nxt)
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
ck("nessun ALTRO lotto rivendica le righe di questo segmento (26 righe distinte)",
   not overlap and len(mine) == 26, (overlap[:3], len(mine)))
VAL = [u for u in tu if u['kind'] == 'VALUE']
PROSA = [u for u in tu if u['kind'] in ('DESCRIPTION', 'DIALOG')]
ck("i 10 VALUE sono copiati carattere per carattere (5 distinti)",
   len(VAL) == 10 and all(u['italian'] == u['english'] for u in VAL)
   and len({u['english'] for u in VAL}) == 5,
   [u['idx'] for u in VAL if u['italian'] != u['english']])
ck("le 16 unita' di prosa sono tradotte", all(u['italian'] != u['english'] for u in PROSA)
   and len(PROSA) == 16)
mult = collections.Counter(u['english'] for u in tu)
gruppi = [e for e, n in mult.items() if n > 1]
ck('12 gruppi identici con molteplicita\' 2 (×11) e 4 (×1), una resa ciascuno',
   len(gruppi) == 12 and sorted(mult[e] for e in gruppi) == [2] * 11 + [4]
   and all(len({u['italian'] for u in tu if u['english'] == e}) == 1 for e in gruppi),
   sorted(mult[e] for e in gruppi))
ck("il gruppo da 4 e' la battuta degli scienziati",
   mult['You wish the scientists the best of luck on <planet> as they carry their scientific equipment off of your ship and hand you your payment of <payment>.'] == 4)
tok_en = collections.Counter(t for u in tu for t in TAG.findall(u['english']))
tok_it = collections.Counter(t for u in tu for t in TAG.findall(u['italian']))
ck('58 segnaposto in 6 famiglie, multiset identico',
   tok_en == tok_it and sum(tok_en.values()) == 58 and len(tok_en) == 6,
   (dict(tok_en), sum(tok_en.values())))
ck('`<bunks>` e `<destination>` sono 10 e 10: il confronto per ordine e\' necessario',
   tok_en['<bunks>'] == tok_en['<destination>'] == 10)
seq_bad = [u['idx'] for u in tu if TAG.findall(u['english']) != TAG.findall(u['italian'])]
ck("l'ORDINE dei segnaposto e' identico dentro ogni unita'", not seq_bad, seq_bad)
ck('ZERO tab e ZERO virgolette (due asserzioni negative scritte)',
   sum(u['english'].count(TAB) for u in tu) == 0 == sum(u['italian'].count(TAB) for u in tu)
   and sum(u['english'].count(QUOTE) for u in tu) == 0 == sum(u['italian'].count(QUOTE) for u in tu))
a_en = [(u['idx'], u['english'].count(APOS)) for u in tu if APOS in u['english']]
a_it = [(u['idx'], u['italian'].count(APOS)) for u in tu if APOS in u['italian']]
ck("ZERO apici inglesi e 4 italiani (10, 11, 13, 14)",
   a_en == [] and a_it == [(10, 1), (11, 2), (13, 1), (14, 2)], (a_en, a_it))
prosa = ' '.join(u['italian'] for u in PROSA)
ck('`Wanderer` invariato al singolare e al plurale (`Wanderers` non compare)',
   prosa.count('Wanderer') >= 8 and 'Wanderers' not in prosa)
ck('«Il pagamento sarà <payment>.» nelle 4 schede degli scienziati (16, 19, 22, 25)',
   [u['idx'] for u in PROSA if 'Il pagamento sarà <payment>.' in u['italian']] == [16, 19, 22, 25])
ck('«per portarli fin là» nelle 4 schede di trasporto (2, 4, 6, 8)',
   [u['idx'] for u in PROSA if 'per portarli fin là' in u['italian']] == [2, 4, 6, 8])
ck('lessico: «lavoratori», «agricoltori», «piccoli», «scienziati», «inquinanti atmosferici»',
   all(t in prosa for t in ('lavoratori', 'agricoltori', 'piccoli', 'scienziati', 'inquinanti atmosferici')))
ck("PENDING su tutte e 26", not [u['idx'] for u in su
                                 if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0]
                                 != 'PENDING'])
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in tu if u['italian'].rstrip() != u['italian'] or '  ' in u['italian']])
ck('nessun carattere tipografico e nessun non latino',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')
        or any(ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F for c in u['italian'])])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate 0,55-1,90 (0,93 - 1,12; 430 -> 426 parole)',
   0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print("SEGMENTO: %d/92 unita' del file (%.1f%%) · 0 prima · 26 qui · 66 dopo · confine riga 264"
      % (len(mine), 100.0 * len(mine) / 92))
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L252 superato' if not fail else 'verify L252 fallito')
raise SystemExit(0 if not fail else 1)
