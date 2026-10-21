r"""verify.py — L247 (`data/human/syndicate jobs.txt`, 16 unita', righe 19-153). **Primo lotto del file.**

**Invariante di SEGMENTO** (il file NON e' chiuso: 94 unita'): **0** prima della 19 — il lotto **apre** il file —, **16** qui,
**78** dopo la 153, confine misurato alla **157** (`mission:Rush fuel Delivery`). La copertura si **stampa** (16/94, 17,0%) e
non si asserisce come elenco di lotti: si pretende che **nessun altro** `translation.json` rivendichi queste righe.

Verifica da sola: il `VALUE` copiato e le **15 unita' di prosa tradotte**, le **3 coppie di inglese identico** con una resa
ciascuna, i **39 segnaposto** per famiglia **e per ordine dentro ogni unita'** (`<planet stopovers>` intero), `<tons>` senza
articolo, i **0 tab**, le **2 virgolette** della citazione e i **6 apici inglesi** contro i **5 italiani**.

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
PATH = 'data/human/syndicate jobs.txt'
src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
su = sorted(src['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
raw_lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
fail = []


def ck(n, c, d=''):
    print('%-90s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente (16/16)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck("unita: 16, righe 19 - 153", len(tu) == 16 and (tu[0]['line'], tu[-1]['line']) == (19, 153))
ck('1 VALUE + 9 DIALOG + 6 DESCRIPTION',
   collections.Counter(u['kind'] for u in su) == {'VALUE': 1, 'DIALOG': 9, 'DESCRIPTION': 6})
ck('6 contesti distinti', len(set(u['context'] for u in su)) == 6,
   sorted(set(u['context'] for u in su)))
ck("ZERO unita' prima della 19: e' la prima riga del file",
   db.execute('select count(*) from units where path=? and line<19', (PATH,)).fetchone()[0] == 0)
ck("78 unita' dopo la 153: il lotto NON chiude il file",
   db.execute('select count(*) from units where path=? and line>153', (PATH,)).fetchone()[0] == 78)
nxt = db.execute('select line,context from units where path=? and line>153 order by line limit 1', (PATH,)).fetchone()
ck('confine misurato: riga 157, mission:Rush fuel Delivery', nxt == (157, 'mission:Rush fuel Delivery'), nxt)
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
ck("nessun ALTRO lotto rivendica le righe di questo segmento (16 righe distinte)",
   not overlap and len(mine) == 16, (overlap[:3], len(mine)))
VAL = [u for u in tu if u['kind'] == 'VALUE']
PROSA = [u for u in tu if u['kind'] in ('DESCRIPTION', 'DIALOG')]
ck("il VALUE e' copiato carattere per carattere (nome del lavoro)",
   len(VAL) == 1 and VAL[0]['italian'] == VAL[0]['english'])
ck("le 15 unita' di prosa (DIALOG + DESCRIPTION) sono tutte tradotte",
   all(u['italian'] != u['english'] for u in PROSA) and len(PROSA) == 15)
gruppi = [e for e, n in collections.Counter(u['english'] for u in tu).items() if n > 1]
posseduti = all(len({u['italian'] for u in tu if u['english'] == e}) == 1 for e in gruppi)
ck('le 3 coppie di inglese identico hanno una sola resa ciascuna',
   len(gruppi) == 3 and posseduti, (len(gruppi), posseduti))
tok_en = collections.Counter(t for u in tu for t in TAG.findall(u['english']))
tok_it = collections.Counter(t for u in tu for t in TAG.findall(u['italian']))
ck('39 segnaposto in 11 famiglie, multiset identico',
   tok_en == tok_it and sum(tok_en.values()) == 39 and len(tok_en) == 11,
   (dict(tok_en), sum(tok_en.values())))
seq_bad = [u['idx'] for u in tu if TAG.findall(u['english']) != TAG.findall(u['italian'])]
ck("l'ordine dei segnaposto e' identico dentro ogni unita'", not seq_bad, seq_bad)
ck('`<planet stopovers>` resta un simbolo intero (uno spazio dentro)',
   tok_it.get('<planet stopovers>') == 1 and tok_it.get('<stopovers>') == 2)
prosa = ' '.join(u['italian'] for u in PROSA)
ck('`<tons>` senza articolo e seguito da «di»',
   not re.search(r'\b(il|lo|la|i|gli|le|un|uno|una)\s+<tons>', prosa)
   and set(re.findall(r'<tons>\s+(\w+)', prosa)) == {'di'},
   re.findall(r'.{10}<tons>\s+\w+', prosa))
ck('ZERO tab in tutto il lotto', sum(u['english'].count(TAB) for u in tu) == 0 == sum(u['italian'].count(TAB) for u in tu))
q_it = [(u['idx'], u['italian'].count(QUOTE)) for u in tu if QUOTE in u['italian']]
ck("2 virgolette, nella sola unita' 12: la citazione «Ci farà risparmiare mesi!»",
   q_it == [(12, 2)] and '"Ci farà risparmiare mesi!"' in tu[11]['italian'], q_it)
a_en = [(u['idx'], u['english'].count(APOS)) for u in tu if APOS in u['english']]
a_it = [(u['idx'], u['italian'].count(APOS)) for u in tu if APOS in u['italian']]
ck("6 apici inglesi su 6 unita' (4, 5, 8, 9, 11, 14) e 5 italiani su 4 (4, 8, 15, 16)",
   a_en == [(4, 1), (5, 1), (8, 1), (9, 1), (11, 1), (14, 1)] and a_it == [(4, 1), (8, 1), (15, 1), (16, 2)],
   (a_en, a_it))
ck("nessun possessivo inglese sopravvissuto in nessuna delle 16 unita'",
   "'s " not in prosa and "s' " not in prosa)
ck('lessico: «Sindacato», «ritiro aziendale», «Iniziativa Verde», `Syndicated Systems` invariato',
   all(t in prosa for t in ('Sindacato', 'ritiro aziendale', 'Iniziativa Verde', 'Syndicated Systems'))
   and not re.search(r'\bSyndicate\b', prosa))
ck('le due rese fisse del corpus sono rispettate (5 «Il pagamento è», 2 «Incassi il pagamento di»)',
   sum(1 for u in PROSA if 'Il pagamento è <payment>.' in u['italian']) == 5
   and sum(1 for u in PROSA if 'Incassi il pagamento di <payment>.' in u['italian']) == 2)
ck("PENDING su tutte e 16", not [u['idx'] for u in su
                                 if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0]
                                 != 'PENDING'])
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in tu if u['italian'].rstrip() != u['italian'] or '  ' in u['italian']])
ck('nessun carattere tipografico e nessun non latino',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')
        or any(ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F for c in u['italian'])])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate 0,55-1,90 (0,97 - 1,23; 488 -> 510 parole)',
   0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print("SEGMENTO: %d/94 unita' del file (%.1f%%) · 0 prima · 16 qui · 78 dopo · confine riga 157"
      % (len(mine), 100.0 * len(mine) / 94))
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L247 superato' if not fail else 'verify L247 fallito')
raise SystemExit(0 if not fail else 1)
