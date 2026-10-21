r"""verify.py — L250 (`data/human/syndicate jobs.txt`, 27 unita', righe 435-678). Quarto lotto del file.

**Invariante di SEGMENTO** (il file NON e' chiuso: 94 unita'): **55** prima della 435 (L247 16 + L248 20 + L249 19), **27**
qui, **12** dopo la 678, confine misurato alla **701** (`mission:Megaparsec Shipment [0]`). Dopo questo lotto restano 12
unita': il successivo e' il lotto **terminale** del file.

Verifica da sola: gli **11 `VALUE`** copiati (uno solo, `Shipment to <planet>`, ripetuto **6 volte**), le **16 unita' di
prosa tradotte**, i **3 gruppi** di inglese identico con molteplicita' **6 / 3 / 2**, i **46 segnaposto** per famiglia **e
per ordine dentro ogni unita'** (riordinare i segnaposto e' un errore, non una scelta di stile), **zero tab**, le **4
virgolette** delle unita' 5 e 6, **zero apici inglesi** contro **2 italiani**.
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
    print('%-94s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente (27/27)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck("unita: 27, righe 435 - 678", len(tu) == 27 and (tu[0]['line'], tu[-1]['line']) == (435, 678))
ck('11 VALUE + 11 DESCRIPTION + 5 DIALOG',
   collections.Counter(u['kind'] for u in su) == {'VALUE': 11, 'DESCRIPTION': 11, 'DIALOG': 5})
ck('11 contesti distinti', len(set(u['context'] for u in su)) == 11,
   sorted(set(u['context'] for u in su)))
ck("55 unita' prima della 435: L247 (16) + L248 (20) + L249 (19)",
   db.execute('select count(*) from units where path=? and line<435', (PATH,)).fetchone()[0] == 55)
ck("12 unita' dopo la 678: il lotto NON chiude il file",
   db.execute('select count(*) from units where path=? and line>678', (PATH,)).fetchone()[0] == 12)
nxt = db.execute('select line,context from units where path=? and line>678 order by line limit 1', (PATH,)).fetchone()
ck('confine misurato: riga 701, mission:Megaparsec Shipment [0]',
   nxt == (701, 'mission:Megaparsec Shipment [0]'), nxt)
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
ck("nessun ALTRO lotto rivendica le righe di questo segmento (27 righe distinte)",
   not overlap and len(mine) == 27, (overlap[:3], len(mine)))
VAL = [u for u in tu if u['kind'] == 'VALUE']
PROSA = [u for u in tu if u['kind'] in ('DESCRIPTION', 'DIALOG')]
ck("gli 11 VALUE sono copiati carattere per carattere, e sono 6 distinti",
   len(VAL) == 11 and all(u['italian'] == u['english'] for u in VAL)
   and len({u['english'] for u in VAL}) == 6,
   [u['idx'] for u in VAL if u['italian'] != u['english']])
ck("il VALUE `Shipment to <planet>` compare 6 volte, sempre identico",
   collections.Counter(u['english'] for u in tu)['Shipment to <planet>'] == 6
   and len({u['italian'] for u in tu if u['english'] == 'Shipment to <planet>'}) == 1)
ck("le 16 unita' di prosa sono tradotte", all(u['italian'] != u['english'] for u in PROSA)
   and len(PROSA) == 16)
mult = collections.Counter(u['english'] for u in tu)
gruppi = [e for e, n in mult.items() if n > 1]
ck('3 gruppi di inglese identico con molteplicita\' 6, 3 e 2, una resa ciascuno',
   len(gruppi) == 3 and sorted(mult[e] for e in gruppi) == [2, 3, 6]
   and all(len({u['italian'] for u in tu if u['english'] == e}) == 1 for e in gruppi),
   sorted(mult[e] for e in gruppi))
tok_en = collections.Counter(t for u in tu for t in TAG.findall(u['english']))
tok_it = collections.Counter(t for u in tu for t in TAG.findall(u['italian']))
ck('46 segnaposto in 6 famiglie, multiset identico',
   tok_en == tok_it and sum(tok_en.values()) == 46 and len(tok_en) == 6,
   (dict(tok_en), sum(tok_en.values())))
seq_bad = [u['idx'] for u in tu if TAG.findall(u['english']) != TAG.findall(u['italian'])]
ck("l'ORDINE dei segnaposto e' identico dentro ogni unita' (nessuno spostato)", not seq_bad, seq_bad)
ck('ZERO tab (asserzione negativa scritta)',
   sum(u['english'].count(TAB) for u in tu) == 0 == sum(u['italian'].count(TAB) for u in tu))
q_it = [(u['idx'], u['italian'].count(QUOTE)) for u in tu if QUOTE in u['italian']]
ck('4 virgolette nelle unita\' 5 e 6: «"trattamento"» e «"traditori di classe"»',
   q_it == [(5, 2), (6, 2)] and '"trattamento"' in tu[4]['italian']
   and '"traditori di classe"' in tu[5]['italian'], q_it)
a_en = [(u['idx'], u['english'].count(APOS)) for u in tu if APOS in u['english']]
a_it = [(u['idx'], u['italian'].count(APOS)) for u in tu if APOS in u['italian']]
ck("ZERO apici inglesi e 2 italiani (3 e 9: `dell'arresto`, `l'ingresso`)",
   a_en == [] and a_it == [(3, 1), (9, 1)], (a_en, a_it))
prosa = ' '.join(u['italian'] for u in PROSA)
ck('lessico: «manifestanti», «sindacalisti», «colletti bianchi», «prosciolto», «sprezzanti»',
   all(t in prosa for t in ('manifestanti', 'sindacalisti', 'colletti bianchi', 'prosciolto', 'sprezzanti')))
ck('la coda fissa delle due schede di detenzione e\' la stessa (2 e 5)',
   [u['idx'] for u in PROSA if 'strutture adatte al trasferimento dei criminali' in u['italian']] == [2, 5])
ck('nomi propri invariati: `Syndicated Shipyards` 4 volte e `Syndicated Systems` 2',
   prosa.count('Syndicated Shipyards') == 4 and prosa.count('Syndicated Systems') == 2)
ck("nessun `Syndicate` sciolto come fazione (le forme sono nomi propri composti)",
   not re.search(r'\bSyndicate\b', prosa), re.findall(r'\bSyndicate\w*', prosa))
ck("PENDING su tutte e 27", not [u['idx'] for u in su
                                 if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0]
                                 != 'PENDING'])
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in tu if u['italian'].rstrip() != u['italian'] or '  ' in u['italian']])
ck('nessun carattere tipografico e nessun non latino',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')
        or any(ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F for c in u['italian'])])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate 0,55-1,90 (0,90 - 1,26; 432 -> 454 parole)',
   0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print("SEGMENTO: %d/94 unita' del file (%.1f%%) · 55 prima · 27 qui · 12 dopo · confine riga 701"
      % (len(mine), 100.0 * len(mine) / 94))
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L250 superato' if not fail else 'verify L250 fallito')
raise SystemExit(0 if not fail else 1)
