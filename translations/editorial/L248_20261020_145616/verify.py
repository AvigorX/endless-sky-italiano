r"""verify.py — L248 (`data/human/syndicate jobs.txt`, 20 unita', righe 157-275). Secondo lotto del file.

**Invariante di SEGMENTO** (il file NON e' chiuso: 94 unita'): **16** prima della 157 (L247), **20** qui, **58** dopo la
275, confine misurato alla **291**, che e' di nuovo `mission:Syndicate target practice [2]` — **lo stesso contesto
dell'ultima unita', con le parentesi quadre nel nome**: il controllo le cita grezze.

Verifica da sola: i **5 `VALUE`** copiati (3 distinti), le **15 unita' di prosa tradotte**, i **7 gruppi di inglese
identico** con una resa ciascuno, i **32 segnaposto** per famiglia **e per ordine**, **zero tab**, **zero virgolette**,
i **2 apici inglesi** (`You'll`) contro **1 italiano**, e che dopo `<commodity>` non segua mai un aggettivo concordato.

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
    print('%-92s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente (20/20)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck("unita: 20, righe 157 - 275", len(tu) == 20 and (tu[0]['line'], tu[-1]['line']) == (157, 275))
ck('5 VALUE + 10 DIALOG + 5 DESCRIPTION',
   collections.Counter(u['kind'] for u in su) == {'VALUE': 5, 'DIALOG': 10, 'DESCRIPTION': 5})
ck('5 contesti distinti, con le parentesi quadre in tre di essi',
   len(set(u['context'] for u in su)) == 5
   and sum(1 for c in set(u['context'] for u in su) if '[0]' in c or '[1]' in c or '[2]' in c) == 3,
   sorted(set(u['context'] for u in su)))
ck("16 unita' prima della 157: e' L247",
   db.execute('select count(*) from units where path=? and line<157', (PATH,)).fetchone()[0] == 16)
ck("58 unita' dopo la 275: il lotto NON chiude il file",
   db.execute('select count(*) from units where path=? and line>275', (PATH,)).fetchone()[0] == 58)
nxt = db.execute('select line,context from units where path=? and line>275 order by line limit 1', (PATH,)).fetchone()
ck("confine misurato: riga 291, mission:Syndicate target practice [2] — stesso contesto, parentesi grezze",
   nxt == (291, 'mission:Syndicate target practice [2]')
   and tu[-1]['context'] == 'mission:Syndicate target practice [2]', nxt)
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
ck("nessun ALTRO lotto rivendica le righe di questo segmento (20 righe distinte)",
   not overlap and len(mine) == 20, (overlap[:3], len(mine)))
VAL = [u for u in tu if u['kind'] == 'VALUE']
PROSA = [u for u in tu if u['kind'] in ('DESCRIPTION', 'DIALOG')]
ck("i 5 VALUE sono copiati carattere per carattere, e sono 3 distinti",
   len(VAL) == 5 and all(u['italian'] == u['english'] for u in VAL)
   and len({u['english'] for u in VAL}) == 3,
   [u['idx'] for u in VAL if u['italian'] != u['english']])
ck("le 15 unita' di prosa sono tradotte", all(u['italian'] != u['english'] for u in PROSA)
   and len(PROSA) == 15)
gruppi = [e for e, n in collections.Counter(u['english'] for u in tu).items() if n > 1]
ck('i 7 gruppi di inglese identico hanno una sola resa ciascuno',
   len(gruppi) == 7 and all(len({u['italian'] for u in tu if u['english'] == e}) == 1 for e in gruppi),
   (len(gruppi), [len([1 for u in tu if u['english'] == e]) for e in gruppi]))
mult = collections.Counter(u['english'] for u in tu)
ck("il gruppo con tre copie ('Syndicate target practice' e la sua scheda) ha una sola resa",
   max(mult.values()) == 3 and mult['Syndicate target practice'] == 3
   and len({u['italian'] for u in tu if u['english'] == 'Syndicate target practice'}) == 1,
   mult.most_common(2))
tok_en = collections.Counter(t for u in tu for t in TAG.findall(u['english']))
tok_it = collections.Counter(t for u in tu for t in TAG.findall(u['italian']))
ck('32 segnaposto in 8 famiglie, multiset identico',
   tok_en == tok_it and sum(tok_en.values()) == 32 and len(tok_en) == 8,
   (dict(tok_en), sum(tok_en.values())))
seq_bad = [u['idx'] for u in tu if TAG.findall(u['english']) != TAG.findall(u['italian'])]
ck("l'ordine dei segnaposto e' identico dentro ogni unita'", not seq_bad, seq_bad)
ck('ZERO tab (asserzione negativa scritta)',
   sum(u['english'].count(TAB) for u in tu) == 0 == sum(u['italian'].count(TAB) for u in tu))
ck('ZERO virgolette (asserzione negativa scritta)',
   sum(u['english'].count(QUOTE) for u in tu) == 0 == sum(u['italian'].count(QUOTE) for u in tu))
a_en = [(u['idx'], u['english'].count(APOS)) for u in tu if APOS in u['english']]
a_it = [(u['idx'], u['italian'].count(APOS)) for u in tu if APOS in u['italian']]
ck("2 apici inglesi (10, 16: `You'll`) e 1 italiano (2: `d'emergenza`)",
   a_en == [(10, 1), (16, 1)] and a_it == [(2, 1)], (a_en, a_it))
prosa = ' '.join(u['italian'] for u in PROSA)
ck("nessuna forma possessiva inglese e nessun `You'll` sopravvissuto",
   "'s " not in prosa and 'You' not in prosa and 'll ' not in prosa)
ck('cinque «Il pagamento è <payment>.» e quattro «incassi il pagamento di <payment>.»',
   sum(1 for u in PROSA if 'Il pagamento è <payment>.' in u['italian']) == 5
   and sum(1 for u in PROSA if 'incassi il pagamento di <payment>.' in u['italian']) == 4)
ck("dopo `<commodity>` non segue mai un aggettivo concordato",
   re.findall(r'<commodity>\s+(\w+)', prosa) == ['alla', 'per', 'alla'],
   re.findall(r'<commodity>\s+\w+', prosa))
ck('`<tons>` senza articolo e seguito da «di»',
   not re.search(r'\b(il|lo|la|i|gli|le|un|uno|una)\s+<tons>', prosa)
   and set(re.findall(r'<tons>\s+(\w+)', prosa)) == {'di'})
ck('lessico: «Sindacato», «nave-bersaglio», «dati di collaudo», «baia di carico», `Syndicate` assente',
   all(t in prosa for t in ('Sindacato', 'nave-bersaglio', 'dati di collaudo', 'baia di carico'))
   and not re.search(r'\bSyndicate\b', prosa))
ck("PENDING su tutte e 20", not [u['idx'] for u in su
                                 if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0]
                                 != 'PENDING'])
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in tu if u['italian'].rstrip() != u['italian'] or '  ' in u['italian']])
ck('nessun carattere tipografico e nessun non latino',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')
        or any(ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F for c in u['italian'])])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate 0,55-1,90 (0,93 - 1,32; 430 -> 422 parole)',
   0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print("SEGMENTO: %d/94 unita' del file (%.1f%%) · 16 prima · 20 qui · 58 dopo · confine riga 291"
      % (len(mine), 100.0 * len(mine) / 94))
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L248 superato' if not fail else 'verify L248 fallito')
raise SystemExit(0 if not fail else 1)
