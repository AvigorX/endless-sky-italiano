r"""verify.py — L245 (`data/hai/hai ships.txt`, 46 unita', righe 901-1516). Terzo lotto del file.

**Invariante di SEGMENTO** (il file NON e' chiuso: 157 unita'): **74** prima della 901 (L243 29 + L244 45), **46** qui,
**37** dopo la 1516, confine misurato alla **1517**, che e' di nuovo `ship:Emperor Beetle` — **lo stesso contesto
dell'ultima unita'**: il controllo lo registra esplicitamente invece di pretendere un contesto diverso.

Verifica da sola: i **41 nomi** copiati e **nessun `VALUE`** nel lotto, le **5 descrizioni** tradotte, **il tab unico
all'inizio della unita' 46** (secondo paragrafo della scheda dell'Emperor Beetle), le **82 virgolette per unita'**, i
**2 apici italiani** e la regola dei **plurali inglesi** (`Shield Beetles` → «Shield Beetle», `Trackers` → «i Tracker»).

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
src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
su = sorted(src['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
raw_lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
fail = []


def ck(n, c, d=''):
    print('%-88s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente (46/46)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck("unita: 46, righe 901 - 1516", len(tu) == 46 and (tu[0]['line'], tu[-1]['line']) == (901, 1516))
ck('41 TEXT + 5 DESCRIPTION, nessun VALUE',
   collections.Counter(u['kind'] for u in su) == {'TEXT': 41, 'DESCRIPTION': 5})
ck('5 contesti distinti', len(set(u['context'] for u in su)) == 5,
   sorted(set(u['context'] for u in su)))
ck("74 unita' prima della 901: L243 (29) + L244 (45)",
   db.execute('select count(*) from units where path=? and line<901', (PATH,)).fetchone()[0] == 74)
ck("37 unita' dopo la 1516: il lotto NON chiude il file",
   db.execute('select count(*) from units where path=? and line>1516', (PATH,)).fetchone()[0] == 37)
nxt = db.execute('select line,context from units where path=? and line>1516 order by line limit 1', (PATH,)).fetchone()
ck("confine misurato: riga 1517, ship:Emperor Beetle — lo STESSO contesto dell'ultima unita'",
   nxt == (1517, 'ship:Emperor Beetle') and tu[-1]['context'] == 'ship:Emperor Beetle', nxt)
ck('il file intero: 157 unita, righe 15 - 1860',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (157, 15, 1860))
mine = set(u['line'] for u in tu)
overlap = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    lot = os.path.basename(os.path.dirname(f))
    if lot == os.path.basename(HERE):
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH and u['line'] in mine:
            overlap.append((lot, u['line']))
ck("nessun ALTRO lotto rivendica le righe di questo segmento (46 righe distinte)",
   not overlap and len(mine) == 46, (overlap[:3], len(mine)))
DATA = [u for u in tu if u['kind'] in ('VALUE', 'TEXT')]
DES = [u for u in tu if u['kind'] == 'DESCRIPTION']
ck("i 41 TEXT sono copiati carattere per carattere (virgolette comprese)",
   all(u['italian'] == u['english'] for u in DATA) and len(DATA) == 41,
   [u['idx'] for u in DATA if u['italian'] != u['english']])
ck("le 5 descrizioni sono tradotte", all(u['italian'] != u['english'] for u in DES) and len(DES) == 5)
tabs = [(u['idx'], u['english'].count(TAB), u['italian'].count(TAB)) for u in tu
        if TAB in u['english'] or TAB in u['italian']]
ck("il tab e' uno solo, all'inizio della unita' 46, conservato in entrambe le lingue",
   tabs == [(46, 1, 1)] and tu[-1]['italian'][0] == TAB and tu[-1]['english'][0] == TAB, tabs)
ck('il paragrafo col tab e\' tradotto: contiene «baie di carico» e finisce con punto',
   'baie di carico' in tu[-1]['italian'] and tu[-1]['italian'].endswith('.'))
q_en = [(u['idx'], u['english'].count(QUOTE)) for u in tu if QUOTE in u['english']]
q_it = [(u['idx'], u['italian'].count(QUOTE)) for u in tu if QUOTE in u['italian']]
ck('82 virgolette, 2 per unita\', su 41 unita\' (tutti e soli i nomi)',
   q_en == q_it and len(q_it) == 41 and set(n for _, n in q_it) == {2}, (len(q_en), len(q_it)))
a_it = [(u['idx'], u['italian'].count(APOS)) for u in tu if APOS in u['italian']]
ck("0 apici in inglese, 2 in italiano (27, 45): elisioni",
   sum(u['english'].count(APOS) for u in tu) == 0 and a_it == [(27, 1), (45, 1)], a_it)
ck("nessun 's in nessuna delle 46 unita'", "'s " not in ' '.join(u['italian'] for u in tu))
# Conteggio **per nome**, non un totale: un nome aggiunto al sorgente sposta il numero e il controllo diventa rosso.
# Misurato sulle 5 schede: Sea Scorpion 1, Scarab 1, Shield Beetle 3, Emperor Beetle 1, Lightning Bug 1,
# Grasshopper 1, Titan Beetle 1, Titan 1, Tracker 1 = **11 unita'-nome** (una scheda puo' nominarne piu' d'uno).
ATTESI = {'Sea Scorpion': 1, 'Scarab': 1, 'Shield Beetle': 3, 'Emperor Beetle': 1, 'Lightning Bug': 1,
          'Grasshopper': 1, 'Titan Beetle': 1, 'Titan': 1, 'Tracker': 1}
misurati = {n: sum(1 for u in DES if n in u['english']) for n in ATTESI}
persi = [(u['idx'], n) for u in DES for n in ATTESI if n in u['english'] and n not in u['italian']]
ck("ogni nome proprio che l'inglese nomina resta in italiano (11 unita'-nome, 0 perse)",
   misurati == ATTESI and not persi, (misurati, persi))
prosa = ' '.join(u['italian'] for u in DES)
ck('plurali inglesi non copiati: «Shield Beetle» e «i Tracker» (=0 «Shield Beetles», =0 «Trackers»)',
   'Shield Beetle' in prosa and 'i Tracker' in prosa
   and 'Shield Beetles' not in prosa and 'Trackers' not in prosa
   and 'Shield Beetles' in ' '.join(u['english'] for u in DES)
   and 'Trackers' in ' '.join(u['english'] for u in DES))
ck('lessico: «Slegati», «convogli mercantili», «baie di carico», «ammiraglie», «navi trofeo»',
   all(t in prosa for t in ('Slegati', 'convogli mercantili', 'baie di carico', 'ammiraglie', 'navi trofeo'))
   and 'Unfettered' not in ' '.join(u['italian'] for u in tu))
ck('«cugina» e «cugino» coerenti col genere della nave a cui si riferisce (Scarab: femminile)',
   'Cugina laboriosa' in prosa)
ck("nessun segnaposto e nessun tab fuori dalla unita' 46",
   sum(len(TAG.findall(u['english'])) for u in tu) == 0 == sum(len(TAG.findall(u['italian'])) for u in tu)
   and sum(u['italian'].count(TAB) for u in tu) == 1)
ck("PENDING su tutte e 46", not [u['idx'] for u in su
                                 if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0]
                                 != 'PENDING'])
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in tu if u['italian'].rstrip() != u['italian'] or '  ' in u['italian']])
ck('nessun carattere tipografico e nessun non latino',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')
        or any(ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F for c in u['italian'])])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate 0,55-1,90 (0,98 - 1,10; 442 -> 441 parole)',
   0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print("SEGMENTO: %d/157 unita' del file (%.1f%%) · 74 prima · 46 qui · 37 dopo · confine riga 1517"
      % (len(mine), 100.0 * len(mine) / 157))
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L245 superato' if not fail else 'verify L245 fallito')
raise SystemExit(0 if not fail else 1)
