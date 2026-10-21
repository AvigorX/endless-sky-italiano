r"""verify.py — L246 (`data/hai/hai ships.txt`, 37 unita', righe 1517-1860). **LOTTO TERMINALE**.

**Invariante di FILE** (il file si chiude qui): 120 unita' prima (L243 29 + L244 45 + L245 46), **37** qui, **0** dopo la
1860; i quattro lotti coprono **157 righe distinte su 157**, la 1860 e' l'ultima riga del file.

Verifica da sola: i **32 nomi** copiati e **nessun `VALUE`**, le **5 descrizioni** tradotte, i **due tab** (unita' 1 e 24)
come primo carattere in entrambe le lingue, le **66 virgolette per unita'** (32 nomi + il `"Giftbringer"`), i **2 apici
inglesi** contro i **5 italiani**, e la **coerenza cross-lot della nota sui caccia**: la resa deve essere quella
**dominante** nei 8 lotti che gia' contengono la stessa stringa inglese.

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
PATH = 'data/hai/hai ships.txt'
FNOTE_EN = TAB + 'Fighters do not come equipped with a hyperdrive. You cannot carry a fighter unless you have a ship in your fleet with a fighter bay.'
src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
su = sorted(src['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
raw_lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
fail = []


def ck(n, c, d=''):
    print('%-92s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente (37/37)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck("unita: 37, righe 1517 - 1860", len(tu) == 37 and (tu[0]['line'], tu[-1]['line']) == (1517, 1860))
ck('32 TEXT + 5 DESCRIPTION, nessun VALUE',
   collections.Counter(u['kind'] for u in su) == {'TEXT': 32, 'DESCRIPTION': 5})
ck('4 contesti distinti', len(set(u['context'] for u in su)) == 4,
   sorted(set(u['context'] for u in su)))
ck("120 unita' prima della 1517: L243 (29) + L244 (45) + L245 (46)",
   db.execute('select count(*) from units where path=? and line<1517', (PATH,)).fetchone()[0] == 120)
ck("ZERO unita' dopo la 1860: il lotto CHIUDE il file",
   db.execute('select count(*) from units where path=? and line>1860', (PATH,)).fetchone()[0] == 0)
ck("la 1860 e' l'ultima riga del file (157 unita', righe 15 - 1860)",
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (157, 15, 1860))
# --- invariante di FILE: quattro lotti, 157 righe distinte, nessun buco ---
per_lotto, righe = [], set()
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    us = [u for u in json.load(open(f, encoding='utf-8'))['units'] if u['path'] == PATH]
    if us:
        per_lotto.append((os.path.basename(os.path.dirname(f)), len(us)))
        righe |= {u['line'] for u in us}
ck('INVARIANTE DI FILE: 4 lotti, 29 + 45 + 46 + 37 = 157 = righe distinte',
   [n for _, n in per_lotto] == [29, 45, 46, 37] and len(righe) == 157,
   (per_lotto, len(righe)))
ck('nessun buco: le 157 righe sono esattamente quelle del database',
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
ck("nessun altro lotto rivendica le 37 righe di questo segmento",
   not overlap and len(mine) == 37, (overlap[:3], len(mine)))
DATA = [u for u in tu if u['kind'] in ('VALUE', 'TEXT')]
DES = [u for u in tu if u['kind'] == 'DESCRIPTION']
ck("i 32 TEXT sono copiati carattere per carattere (virgolette comprese)",
   all(u['italian'] == u['english'] for u in DATA) and len(DATA) == 32,
   [u['idx'] for u in DATA if u['italian'] != u['english']])
ck("le 5 descrizioni sono tradotte", all(u['italian'] != u['english'] for u in DES) and len(DES) == 5)
tabs = [(u['idx'], u['english'].count(TAB), u['italian'].count(TAB)) for u in tu
        if TAB in u['english'] or TAB in u['italian']]
ck("i DUE tab stanno all'inizio delle unita' 1 e 24, conservati in entrambe le lingue",
   tabs == [(1, 1, 1), (24, 1, 1)] and tu[0]['italian'][0] == TAB and tu[23]['italian'][0] == TAB, tabs)
ck("i due paragrafi col tab sono tradotti (contengono «capi militari» e «baia di caccia»)",
   'capi militari' in tu[0]['italian'] and 'baia di caccia' in tu[23]['italian'])
q_en = [(u['idx'], u['english'].count(QUOTE)) for u in tu if QUOTE in u['english']]
q_it = [(u['idx'], u['italian'].count(QUOTE)) for u in tu if QUOTE in u['italian']]
ck("66 virgolette, 2 per unita', su 33 unita' (32 nomi + il Giftbringer)",
   q_en == q_it and len(q_it) == 33 and set(n for _, n in q_it) == {2}, (len(q_en), len(q_it)))
a_en = [(u['idx'], u['english'].count(APOS)) for u in tu if APOS in u['english']]
a_it = [(u['idx'], u['italian'].count(APOS)) for u in tu if APOS in u['italian']]
ck("2 apici inglesi (1, 5) e 5 italiani (1 e 30): possessivi contro elisioni",
   a_en == [(1, 1), (5, 1)] and a_it == [(1, 2), (30, 3)], (a_en, a_it))
ck("nessun 's sopravvissuto in nessuna delle 37 unita'",
   "'s " not in ' '.join(u['italian'] for u in tu) and "s' " not in ' '.join(u['italian'] for u in tu))
# --- coerenza cross-lot: la nota si copia, non si reinventa ---
forma = collections.Counter()
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    if os.path.basename(os.path.dirname(f)) == os.path.basename(HERE):
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['english'] == FNOTE_EN:
            forma[u['italian']] += 1
ck('la nota sui caccia riproduce la resa DOMINANTE del corpus (%d occorrenze, %d forme)'
   % (sum(forma.values()), len(forma)),
   sum(forma.values()) >= 6 and forma.most_common(1)[0][0] == tu[23]['italian'],
   (forma.most_common(2), tu[23]['italian']))
ck('la variante «baia per caccia» e\' la minoritaria (2) e non e\' quella scelta',
   any(n == 2 for _, n in forma.most_common()) and 'baia per caccia' not in tu[23]['italian'])
ATTESI = {'Emperor Beetle': 1, 'Shield Beetle': 1, 'Solifuge': 0, 'Violin Spider': 0, 'Water Bug': 1,
          'Aphid': 1, 'Alphas': 1, 'Giftbringer': 1}
misurati = {n: sum(1 for u in DES if n in u['english']) for n in ATTESI}
persi = [(u['idx'], n) for u in DES for n in ATTESI if n in u['english'] and n not in u['italian']]
ck('ogni nome proprio che l\'inglese nomina resta in italiano (6 unita\'-nome, 0 perse; Solifuge e Violin Spider a 0)',
   misurati == ATTESI and not persi, (misurati, persi))
prosa = ' '.join(u['italian'] for u in DES)
ck('lessico: «Slegati», «porta-caccia», «motori di salto», «baia di caccia», «mercante»',
   all(t in prosa for t in ('Slegati', 'porta-caccia', 'motori di salto', 'baia di caccia', 'mercantile'))
   and 'Unfettered' not in ' '.join(u['italian'] for u in tu))
ck("nessun segnaposto e nessun tab fuori dalle unita' 1 e 24",
   sum(len(TAG.findall(u['english'])) for u in tu) == 0 == sum(len(TAG.findall(u['italian'])) for u in tu)
   and sum(u['italian'].count(TAB) for u in tu) == 2)
ck("PENDING su tutte e 37", not [u['idx'] for u in su
                                 if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0]
                                 != 'PENDING'])
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in tu if u['italian'].rstrip() != u['italian'] or '  ' in u['italian']])
ck('nessun carattere tipografico e nessun non latino',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')
        or any(ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F for c in u['italian'])])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate 0,55-1,90 (0,99 - 1,23; 327 -> 324 parole)',
   0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('FILE: 157/157 unita\' · 4 lotti (29 + 45 + 46 + 37) · 157 righe distinte · ultima riga 1860 · 0 dopo')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L246 superato' if not fail else 'verify L246 fallito')
raise SystemExit(0 if not fail else 1)
