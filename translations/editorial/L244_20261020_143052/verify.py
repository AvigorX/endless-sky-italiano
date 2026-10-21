r"""verify.py — L244 (`data/hai/hai ships.txt`, 45 unita', righe 362-885). Secondo lotto del file.

**Invariante di SEGMENTO** (il file NON e' chiuso: 157 unita'): **29** prima della 362 (L243), **45** qui, **83** dopo la
885, confine misurato alla **901**, che e' di nuovo `ship:Pond Strider` — **lo stesso contesto dell'ultima unita'**: il
controllo lo registra esplicitamente invece di pretendere un contesto diverso.

Verifica da sola: i **37 dati** copiati (1 `VALUE` + 36 `TEXT` con le virgolette), le **8 descrizioni** tradotte, **il tab
unico all'inizio della unita' 3**, le **72 virgolette per unita'**, i **3 apici italiani** che in inglese non ci sono, e i
nomi propri che restano inglesi **dove l'inglese li nomina** (la scheda della Ladybug non pronuncia mai il nome: non e' una
dimenticanza, e' il testo).

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
by = {u['idx']: u for u in tu}
raw_lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
fail = []


def ck(n, c, d=''):
    print('%-86s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente (45/45)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck("unita: 45, righe 362 - 885", len(tu) == 45 and (tu[0]['line'], tu[-1]['line']) == (362, 885))
ck('1 VALUE + 36 TEXT + 8 DESCRIPTION',
   collections.Counter(u['kind'] for u in su) == {'VALUE': 1, 'TEXT': 36, 'DESCRIPTION': 8})
ck('6 contesti distinti', len(set(u['context'] for u in su)) == 6,
   sorted(set(u['context'] for u in su)))
ck("29 unita' prima della 362: e' L243",
   db.execute('select count(*) from units where path=? and line<362', (PATH,)).fetchone()[0] == 29)
ck("83 unita' dopo la 885: il lotto NON chiude il file",
   db.execute('select count(*) from units where path=? and line>885', (PATH,)).fetchone()[0] == 83)
nxt = db.execute('select line,context from units where path=? and line>885 order by line limit 1', (PATH,)).fetchone()
ck("confine misurato: riga 901, ship:Pond Strider — lo STESSO contesto dell'ultima unita'",
   nxt == (901, 'ship:Pond Strider') and tu[-1]['context'] == 'ship:Pond Strider', nxt)
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
ck("nessun ALTRO lotto rivendica le righe di questo segmento (45 righe distinte)",
   not overlap and len(mine) == 45, (overlap[:3], len(mine)))
DATA = [u for u in tu if u['kind'] in ('VALUE', 'TEXT')]
DES = [u for u in tu if u['kind'] == 'DESCRIPTION']
ck("i 37 dati sono copiati carattere per carattere (virgolette comprese)",
   all(u['italian'] == u['english'] for u in DATA) and len(DATA) == 37,
   [u['idx'] for u in DATA if u['italian'] != u['english']])
ck("le 8 descrizioni sono tradotte", all(u['italian'] != u['english'] for u in DES) and len(DES) == 8)
tabs = [(u['idx'], u['english'].count(TAB), u['italian'].count(TAB)) for u in tu
        if TAB in u['english'] or TAB in u['italian']]
ck("il tab e' uno solo, all'inizio della unita' 3, conservato in entrambe le lingue",
   tabs == [(3, 1, 1)] and tu[2]['italian'][0] == TAB and tu[2]['english'][0] == TAB, tabs)
q_en = [(u['idx'], u['english'].count(QUOTE)) for u in tu if QUOTE in u['english']]
q_it = [(u['idx'], u['italian'].count(QUOTE)) for u in tu if QUOTE in u['italian']]
ck('72 virgolette, 2 per unita\', su 36 unita\' (tutti e soli i nomi)',
   q_en == q_it and len(q_it) == 36 and set(n for _, n in q_it) == {2}, (len(q_en), len(q_it)))
a_it = [(u['idx'], u['italian'].count(APOS)) for u in tu if APOS in u['italian']]
ck("0 apici in inglese, 3 in italiano (9, 34, 35): elisioni, non possessivi",
   sum(u['english'].count(APOS) for u in tu) == 0 and a_it == [(9, 1), (34, 1), (35, 1)], a_it)
ck("nessun 's in nessuna delle 45 unita'", "'s " not in ' '.join(u['italian'] for u in tu))
NAMES = ('Flea', 'Geocoris', 'Grasshopper', 'Lightning Bug', 'Ladybug', 'Pond Strider', 'Skipper Railgun')
lost = [(u['idx'], n) for u in DES for n in NAMES if n in u['english'] and n not in u['italian']]
# Misurate: Flea 1, Geocoris 1, Grasshopper 1, Lightning Bug 2, Pond Strider 1, Skipper Railgun 2 = **8**.
# **Ladybug 0**: la sua scheda non pronuncia mai il nome («these vessels», «this ship»), quindi non c'e' nulla da
# conservare. Il conteggio e' asserito perche' un nome aggiunto al sorgente deve far fallire il controllo.
ck('ogni nome proprio che l\'inglese nomina resta in italiano (8 occorrenze, 0 perse; Ladybug 0 per testo)',
   not lost and sum(1 for u in DES for n in NAMES if n in u['english']) == 8
   and 'Ladybug' not in ' '.join(u['english'] for u in DES),
   (lost, sum(1 for u in DES for n in NAMES if n in u['english'])))
prosa = ' '.join(u['italian'] for u in DES)
ck('lessico: «baia per droni», «danni ionici», «scorta ai convogli», «riparazione dello scafo», «Slegati»',
   all(t in prosa for t in ('baia per droni', 'danni ionici', 'scorta ai convogli',
                            'riparazione dello scafo', 'Slegati')))
ck('`ramscoop` e `Skipper Railgun` restano invariati, `Unfettered` e `Fleas` non compaiono in italiano',
   prosa.count('ramscoop') == 2 and 'Skipper Railgun' in prosa
   and 'Unfettered' not in prosa and 'Fleas' not in prosa)
ck('la nota col tab e\' una frase italiana compiuta (contiene «baia per droni» e finisce con punto)',
   'baia per droni' in tu[2]['italian'] and tu[2]['italian'].endswith('.'))
ck("nessun segnaposto e nessun tab fuori dalla unita' 3",
   sum(len(TAG.findall(u['english'])) for u in tu) == 0 == sum(len(TAG.findall(u['italian'])) for u in tu)
   and sum(u['italian'].count(TAB) for u in tu) == 1)
ck("PENDING su tutte e 45", not [u['idx'] for u in su
                                 if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0]
                                 != 'PENDING'])
ck('nessuno spazio finale e nessun doppio spazio (il tab iniziale non conta)',
   not [u['idx'] for u in tu if u['italian'].rstrip() != u['italian'] or '  ' in u['italian']])
ck('nessun carattere tipografico e nessun non latino',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')
        or any(ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F for c in u['italian'])])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate 0,55-1,90 (1,00 - 1,21; 466 -> 498 parole)',
   0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print("SEGMENTO: %d/157 unita' del file (%.1f%%) · 29 prima · 45 qui · 83 dopo · confine riga 901"
      % (len(mine), 100.0 * len(mine) / 157))
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L244 superato' if not fail else 'verify L244 fallito')
raise SystemExit(0 if not fail else 1)
