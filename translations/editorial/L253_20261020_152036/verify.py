r"""verify.py — L253 (`data/wanderer/wanderer jobs.txt`, 24 unita', righe 264-442). Secondo lotto del file.

**Invariante di SEGMENTO** (il file NON e' chiuso: 92 unita'): **26** prima della 264 (L252), **24** qui, **42** dopo la
442, confine misurato alla **458**, di nuovo nel contesto `Wanderer Invasive Species [1]` (la finestra si chiude a meta'
missione). Copertura stampata (50/92, 54,3%).

Verifica da sola: gli **8 `VALUE`** copiati (4 distinti), le **16 unita' di prosa tradotte**, **14 stringhe distinte** con
**10 gruppi da due copie** e **4 singolari** (le due schede e le due battute degli invasivi, che differiscono per una
parola), i **56 segnaposto** per famiglia **e per ordine**, l'identita' di `<stopovers>` (2) e l'**assenza** di
`<planet stopovers>`, **zero tab e virgolette**, **zero apici inglesi** contro **1 italiano**.
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


ck('riga grezza identica al sorgente (24/24)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck("unita: 24, righe 264 - 442", len(tu) == 24 and (tu[0]['line'], tu[-1]['line']) == (264, 442))
ck('8 VALUE + 8 DESCRIPTION + 8 DIALOG',
   collections.Counter(u['kind'] for u in su) == {'VALUE': 8, 'DESCRIPTION': 8, 'DIALOG': 8})
ck('8 contesti distinti', len(set(u['context'] for u in su)) == 8,
   sorted(set(u['context'] for u in su)))
ck("26 unita' prima della 264: e' L252",
   db.execute('select count(*) from units where path=? and line<264', (PATH,)).fetchone()[0] == 26)
ck("42 unita' dopo la 442: il lotto NON chiude il file",
   db.execute('select count(*) from units where path=? and line>442', (PATH,)).fetchone()[0] == 42)
nxt = db.execute('select line,context from units where path=? and line>442 order by line limit 1', (PATH,)).fetchone()
ck("confine misurato: riga 458, mission:Wanderer Invasive Species [1] — stesso contesto dell'ultima unita'",
   nxt == (458, 'mission:Wanderer Invasive Species [1]')
   and tu[-1]['context'] == 'mission:Wanderer Invasive Species [1]', nxt)
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
ck("nessun ALTRO lotto rivendica le righe di questo segmento (24 righe distinte)",
   not overlap and len(mine) == 24, (overlap[:3], len(mine)))
VAL = [u for u in tu if u['kind'] == 'VALUE']
PROSA = [u for u in tu if u['kind'] in ('DESCRIPTION', 'DIALOG')]
ck("gli 8 VALUE sono copiati carattere per carattere (4 distinti)",
   len(VAL) == 8 and all(u['italian'] == u['english'] for u in VAL)
   and len({u['english'] for u in VAL}) == 4,
   [u['idx'] for u in VAL if u['italian'] != u['english']])
ck("le 16 unita' di prosa sono tradotte", all(u['italian'] != u['english'] for u in PROSA)
   and len(PROSA) == 16)
mult = collections.Counter(u['english'] for u in tu)
gruppi = [e for e, n in mult.items() if n > 1]
ck('14 stringhe distinte: 10 gruppi da 2 e 4 singolari',
   len(mult) == 14 and len(gruppi) == 10 and set(mult[e] for e in gruppi) == {2}
   and all(len({u['italian'] for u in tu if u['english'] == e}) == 1 for e in gruppi),
   (len(mult), len(gruppi)))
ck('i 4 singolari sono le due schede e le due battute degli invasivi (20, 21, 22, 24)',
   sorted(u['idx'] for u in PROSA if mult[u['english']] == 1) == [20, 21, 22, 24])
ck('le due schede degli invasivi differiscono per UNA parola (animale / pianta), non sono la stessa stringa',
   tu[19]['english'] != tu[23]['english']
   and 'animal' in tu[19]['english'] and 'plant' in tu[23]['english']
   and tu[19]['italian'] != tu[23]['italian'])
tok_en = collections.Counter(t for u in tu for t in TAG.findall(u['english']))
tok_it = collections.Counter(t for u in tu for t in TAG.findall(u['italian']))
ck('56 segnaposto in 8 famiglie, multiset identico',
   tok_en == tok_it and sum(tok_en.values()) == 56 and len(tok_en) == 8,
   (dict(tok_en), sum(tok_en.values())))
ck("`<stopovers>` (2) e' un simbolo intero e `<planet stopovers>` non compare",
   tok_it.get('<stopovers>') == 2 and tok_it.get('<planet stopovers>') is None)
seq_bad = [u['idx'] for u in tu if TAG.findall(u['english']) != TAG.findall(u['italian'])]
ck("l'ORDINE dei segnaposto e' identico dentro ogni unita'", not seq_bad, seq_bad)
ck('ZERO tab e ZERO virgolette (due asserzioni negative scritte)',
   sum(u['english'].count(TAB) for u in tu) == 0 == sum(u['italian'].count(TAB) for u in tu)
   and sum(u['english'].count(QUOTE) for u in tu) == 0 == sum(u['italian'].count(QUOTE) for u in tu))
a_en = [(u['idx'], u['english'].count(APOS)) for u in tu if APOS in u['english']]
a_it = [(u['idx'], u['italian'].count(APOS)) for u in tu if APOS in u['italian']]
ck("ZERO apici inglesi e 1 italiano (unita' 21: `un'ora`)",
   a_en == [] and a_it == [(21, 1)], (a_en, a_it))
prosa = ' '.join(u['italian'] for u in PROSA)
ck('«Il pagamento sarà» in 4 schede e «Il pagamento è» in 2: la forma segue il tempo inglese',
   sum(1 for u in PROSA if 'Il pagamento sarà <payment>.' in u['italian']) == 4
   and sum(1 for u in PROSA if 'Il pagamento è <payment>.' in u['italian']) == 2)
ck('«in cambio di un pagamento di <payment>» nelle 2 schede degli invasivi',
   [u['idx'] for u in PROSA if 'in cambio di un pagamento di <payment>' in u['italian']] == [20, 24])
ck('«Fai gli auguri ai …» in 6 battute (3, 6, 9, 12, 15, 18)',
   [u['idx'] for u in PROSA if 'Fai gli auguri ai' in u['italian']] == [3, 6, 9, 12, 15, 18])
ck('`Wanderer` invariato (`Wanderers` non compare)',
   prosa.count('Wanderer') >= 8 and 'Wanderers' not in prosa)
ck('lessico: «biologi», «botanici», «raccolta del cibo», «stiva», «gabbie»',
   all(t in prosa for t in ('biologi', 'botanici', 'raccolta del cibo', 'stiva', 'gabbie')))
ck("PENDING su tutte e 24", not [u['idx'] for u in su
                                 if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0]
                                 != 'PENDING'])
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in tu if u['italian'].rstrip() != u['italian'] or '  ' in u['italian']])
ck('nessun carattere tipografico e nessun non latino',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')
        or any(ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F for c in u['italian'])])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate 0,55-1,90 (0,84 - 1,12; 427 -> 406 parole)',
   0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print("SEGMENTO: %d/92 unita' del file (%.1f%%) · 26 prima · 24 qui · 42 dopo · confine riga 458"
      % (len(mine), 100.0 * len(mine) / 92))
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L253 superato' if not fail else 'verify L253 fallito')
raise SystemExit(0 if not fail else 1)
