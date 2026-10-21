r"""verify.py — L251 (`data/human/syndicate jobs.txt`, 12 unita', righe 701-814). **LOTTO TERMINALE**.

**Invariante di FILE** (il file si chiude qui): **82** unita' prima (L247 16 + L248 20 + L249 19 + L250 27), **12** qui,
**0** dopo la 814; i cinque lotti coprono **94 righe distinte su 94** e queste righe sono **esattamente** quelle del
database (nessun buco interno, non solo la coda).

Verifica da sola: i **5 `VALUE`** copiati (3 distinti), le **7 unita' di prosa tradotte**, i **2 gruppi** con tre copie,
i **24 segnaposto** per famiglia **e per ordine**, **zero tab / virgolette / apici** in entrambe le lingue, il lessico
(`Megaparsec Inc.` e `hovercraft` invariati) e le due formule fisse.
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


ck('riga grezza identica al sorgente (12/12)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck("unita: 12, righe 701 - 814", len(tu) == 12 and (tu[0]['line'], tu[-1]['line']) == (701, 814))
ck('5 VALUE + 5 DESCRIPTION + 2 DIALOG',
   collections.Counter(u['kind'] for u in su) == {'VALUE': 5, 'DESCRIPTION': 5, 'DIALOG': 2})
ck('5 contesti distinti', len(set(u['context'] for u in su)) == 5,
   sorted(set(u['context'] for u in su)))
ck("82 unita' prima della 701: 16 + 20 + 19 + 27",
   db.execute('select count(*) from units where path=? and line<701', (PATH,)).fetchone()[0] == 82)
ck("ZERO unita' dopo la 814: il lotto CHIUDE il file",
   db.execute('select count(*) from units where path=? and line>814', (PATH,)).fetchone()[0] == 0)
ck("la 814 e' l'ultima riga del file (94 unita', righe 19 - 814)",
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (94, 19, 814))
per_lotto, righe = [], set()
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    us = [u for u in json.load(open(f, encoding='utf-8'))['units'] if u['path'] == PATH]
    if us:
        per_lotto.append((os.path.basename(os.path.dirname(f)), len(us)))
        righe |= {u['line'] for u in us}
ck('INVARIANTE DI FILE: 5 lotti, 16 + 20 + 19 + 27 + 12 = 94 = righe distinte',
   [n for _, n in per_lotto] == [16, 20, 19, 27, 12] and len(righe) == 94,
   (per_lotto, len(righe)))
ck('nessun buco: le 94 righe sono esattamente quelle del database',
   righe == {l for l, in db.execute('select line from units where path=?', (PATH,))})
mine = set(u['line'] for u in tu)
overlap = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    lot = os.path.basename(os.path.dirname(f))
    if lot == os.path.basename(HERE):
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH and u['line'] in mine:
            overlap.append((lot, u['line']))
ck("nessun altro lotto rivendica le 12 righe di questo segmento",
   not overlap and len(mine) == 12, (overlap[:3], len(mine)))
VAL = [u for u in tu if u['kind'] == 'VALUE']
PROSA = [u for u in tu if u['kind'] in ('DESCRIPTION', 'DIALOG')]
ck("i 5 VALUE sono copiati carattere per carattere (3 distinti)",
   len(VAL) == 5 and all(u['italian'] == u['english'] for u in VAL)
   and len({u['english'] for u in VAL}) == 3,
   [u['idx'] for u in VAL if u['italian'] != u['english']])
ck("le 7 unita' di prosa sono tradotte", all(u['italian'] != u['english'] for u in PROSA) and len(PROSA) == 7)
mult = collections.Counter(u['english'] for u in tu)
gruppi = [e for e, n in mult.items() if n > 1]
ck('2 gruppi con tre copie, una resa ciascuno',
   len(gruppi) == 2 and max(mult.values()) == 3
   and all(len({u['italian'] for u in tu if u['english'] == e}) == 1 for e in gruppi),
   [(e[:35], mult[e]) for e in gruppi])
tok_en = collections.Counter(t for u in tu for t in TAG.findall(u['english']))
tok_it = collections.Counter(t for u in tu for t in TAG.findall(u['italian']))
ck('24 segnaposto in 6 famiglie, multiset identico',
   tok_en == tok_it and sum(tok_en.values()) == 24 and len(tok_en) == 6,
   (dict(tok_en), sum(tok_en.values())))
seq_bad = [u['idx'] for u in tu if TAG.findall(u['english']) != TAG.findall(u['italian'])]
ck("l'ORDINE dei segnaposto e' identico dentro ogni unita'", not seq_bad, seq_bad)
ck('ZERO tab, ZERO virgolette, ZERO apici in entrambe le lingue',
   sum(u['english'].count(TAB) for u in tu) == 0 == sum(u['italian'].count(TAB) for u in tu)
   and sum(u['english'].count(QUOTE) for u in tu) == 0 == sum(u['italian'].count(QUOTE) for u in tu)
   and sum(u['english'].count(APOS) for u in tu) == 0 == sum(u['italian'].count(APOS) for u in tu))
prosa = ' '.join(u['italian'] for u in PROSA)
ck('«Il pagamento è <payment>.» nelle 3 schede Megaparsec (2, 4, 6)',
   [u['idx'] for u in PROSA if 'Il pagamento è <payment>.' in u['italian']] == [2, 4, 6])
ck('«entro il <date> in cambio di <payment>» nelle 2 schede dei trasporti (8, 11)',
   [u['idx'] for u in PROSA if 'entro il <date> in cambio di <payment>' in u['italian']] == [8, 11])
ck('`Megaparsec Inc.` e `hovercraft` restano invariati',
   prosa.count('Megaparsec Inc.') == 3 and prosa.count('hovercraft') == 3)
ck('lessico: «sede di», «progetti leggeri», «carico di», «squadra»',
   all(t in prosa for t in ('sede di', 'progetti leggeri', 'carico di', 'squadra')))
ck("PENDING su tutte e 12", not [u['idx'] for u in su
                                 if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0]
                                 != 'PENDING'])
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in tu if u['italian'].rstrip() != u['italian'] or '  ' in u['italian']])
ck('nessun carattere tipografico e nessun non latino',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')
        or any(ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F for c in u['italian'])])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate 0,55-1,90 (0,88 - 1,28; 139 -> 150 parole)',
   0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print("FILE: 94/94 unita' · 5 lotti (16 + 20 + 19 + 27 + 12) · 94 righe distinte · ultima riga 814 · 0 dopo")
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L251 superato' if not fail else 'verify L251 fallito')
raise SystemExit(0 if not fail else 1)
