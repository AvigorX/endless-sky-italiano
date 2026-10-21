r"""verify.py — L319 (`data/korath/korath weapons.txt`, righe 615-1222). **LOTTO TERMINALE**.

Verifica da sola e verifica il **FILE INTERO** (che questo lotto chiude): **39 unita'**, **prima riga 53**, **ultima 1222**, **zero
unita' dopo**, **somma dei lotti 17 + 22 = 39**, **righe distinte**, **37 `DESCRIPTION` + 2 `VALUE`**.

Poi il lotto: riga grezza, campi del DB, i **due `VALUE` copiati**, la **nota dei rifornimenti tripla** verificata cercando la
**stringa italiana** nel resto del corpus (meccanismo diverso da `check.py`), le **5 tab** con **due nello stesso contesto**, le due
famiglie `Firelight`/`Firestorm` distinte e citantisi, gli **apici per unita'**.

Indipendente da `check.py`.
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
ALT = re.compile(r'\[[^\]]*\]')
HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
ROOT = os.path.abspath(os.path.join(L10N, '..'))
PATH = 'data/korath/korath weapons.txt'
NOTE = (659, 1051, 1222)
TAB_RIGHE = [659, 930, 1050, 1051, 1222]
VALUE = {17: 'Firestorm Torpedoes', 20: 'Firestorm Batteries'}
NOMI = ['Cluster Mine Rack', 'Cluster Mine Layer', 'Shield Disruptor', 'Husk-Slice', 'Digger Mining',
        'Langrage Hyper-Heaver', 'Firelight', 'Microbot Grinder', 'Firestorm Torpedo', 'Firestorm Battery',
        'Korath Plasma Core', 'Banisher']
src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
su = sorted(src['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
raw_lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
by = {u['idx']: u for u in tu}
at = {u['line']: u for u in tu}
fail = []


def ck(n, c, d=''):
    print('%-96s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente (22/22)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = [u['idx'] for u in su
       if db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
       != (u['english'], u['kind'], u['path'], u['context'])]
ck('english/kind/path/context identici al DB', not bad, bad)
ck('22 unita: 20 DESCRIPTION + 2 VALUE in 15 contesti',
   len(tu) == 22 and collections.Counter(u['kind'] for u in tu) == {'DESCRIPTION': 20, 'VALUE': 2}
   and len({u['context'] for u in tu}) == 15)
ck("ZERO unita' dopo la 1222: il lotto chiude il file",
   db.execute('select count(*) from units where path=? and line>1222', (PATH,)).fetchone()[0] == 0)
ck("17 unita' prima della 615 (L318)",
   db.execute('select count(*) from units where path=? and line<615', (PATH,)).fetchone()[0] == 17)
righe = set()
somma = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    us = [u for u in json.load(open(f, encoding='utf-8'))['units'] if u['path'] == PATH]
    if us:
        somma.append(len(us))
        righe |= {u['line'] for u in us}
ck('FILE: somma dei lotti 17 + 22 = 39', somma == [17, 22] and sum(somma) == 39, somma)
ck('FILE: 39 unita, 39 righe distinte, prima 53, ultima 1222',
   len(righe) == 39 and min(righe) == 53 and max(righe) == 1222)
ck('FILE: copertura 39/39 (100%)',
   len(righe) == db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0], '%d/39' % len(righe))
ck('i due VALUE copiati per identita',
   all(by[i]['italian'] == v == by[i]['english'] for i, v in VALUE.items()))
ck('la nota dei rifornimenti e tripla e identica, e usa una resa GIA presente nel corpus',
   by[3]['italian'] == by[15]['italian'] == by[22]['italian']
   and [u['line'] for u in tu if u['english'] == by[3]['english']] == list(NOTE))
nota = by[3]['italian']
_occ = 0
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    if os.path.basename(os.path.dirname(f)) == os.path.basename(HERE):
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['italian'] == nota:
            _occ += 1
ck('la resa della nota compare in almeno due altri lotti (non e inventata qui)', _occ >= 2, _occ)
ck('5 tab, e due nello stesso contesto (Firelight Missile Bank)',
   [u['line'] for u in tu if u['italian'].startswith(TAB)] == TAB_RIGHE
   and at[1050]['context'] == at[1051]['context'])
ck('Firelight e Firestorm sono famiglie distinte e si citano',
   'Firestorm Torpedo' in at[1049]['italian'] and 'Firelight' in at[1221]['italian']
   and 'Firestorm Battery' in at[1159]['italian'])
ck('nomi invariati dove compaiono',
   all(n in u['italian'] for u in tu for n in NOMI if n in u['english']))
ck('il Microbot Grinder: sciame omicida e artigli',
   'omicida' in at[1145]['italian'] and 'artigli' in at[1145]['italian'])
ck('il Firestorm Battery: Plasma Core senza protezioni, fonde gli scafi',
   'Korath Plasma Core' in at[1221]['italian'] and 'fonderne lo scafo' in at[1221]['italian'])
ck('VIRGOLETTE: zero · SEGNAPOSTO: nessuno · ALTERNATIVE: nessuna (asserzioni vuote)',
   sum(u['italian'].count(QUOTE) for u in tu) == 0
   and not TAG.findall(''.join(u['italian'] for u in tu))
   and sum(len(ALT.findall(u['italian'])) for u in tu) == 0)
ck('apici inglesi: 2 + 1 + 1 nelle righe 743, 781, 1159',
   [(u['line'], u['english'].count(APOS)) for u in tu if u['english'].count(APOS)]
   == [(743, 2), (781, 1), (1159, 1)])
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in tu for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessun doppio spazio (la tab iniziale non conta)',
   not [u['idx'] for u in tu if '  ' in u['italian'].lstrip(TAB)])
ck('rapporto nel gate 0,55-1,90',
   all(0.55 < u['ratio'] < 1.90 for u in tu),
   [(u['idx'], u['ratio']) for u in tu if not 0.55 < u['ratio'] < 1.90])
ck('tutte e 22 le unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in tu))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('FILE: 39/39 (100%) · prima riga 53 · ultima 1222 · zero dopo · somma lotti 17+22 · 37 DESCRIPTION + 2 VALUE')
print('parole EN %d -> IT %d · ratio %.2f - %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(u['ratio'] for u in tu), max(u['ratio'] for u in tu)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L319 superato' if not fail else 'verify L319 fallito')
raise SystemExit(0 if not fail else 1)
