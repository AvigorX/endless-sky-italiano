r"""verify.py — L320 (`data/wanderer/wanderer outfits.txt`, righe 40-450). **Primo lotto** del file.

Verifica da sola e **solo fatti locali al segmento**, piu' un **limite monotono** (dopo la 450 restano 13 unita'): il file **non e'
finito**, quindi la copertura **si stampa** e non si asserisce.

La nota dei rifornimenti (271) e' verificata con un meccanismo **diverso** da `check.py`: si cerca la **stringa italiana** in tutti gli
altri lotti e si pretende che compaia **almeno due volte** — se fosse una resa nuova, il conteggio sarebbe zero.

Poi: la **sola tab**, i **due apici** per unita', i **nomi invariati**, la **scala dei reattori**, lo **scambio identico nei due
scudi**, le **asserzioni vuote**.

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
PATH = 'data/wanderer/wanderer outfits.txt'
NOMI = ['Sunbeam', 'Moonbeam', 'Thunderhead', 'Biochemical Cell', 'Red Sun', 'Yellow Sun', 'White Sun',
        'Blue Sun', 'Bright Cloud Shielding', 'Dark Storm Shielding', 'Wanderer', 'Hai Slegati', 'Strong Wind']
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


ck('riga grezza identica al sorgente (18/18)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = [u['idx'] for u in su
       if db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
       != (u['english'], u['kind'], u['path'], u['context'])]
ck('english/kind/path/context identici al DB', not bad, bad)
ck('18 unita, tutte DESCRIPTION, 17 contesti',
   len(tu) == 18 and collections.Counter(u['kind'] for u in tu) == {'DESCRIPTION': 18}
   and len({u['context'] for u in tu}) == 17)
ck("SEGMENTO: zero unita' prima della 40 (il lotto apre il file)",
   db.execute('select count(*) from units where path=? and line<40', (PATH,)).fetchone()[0] == 0)
ck("SEGMENTO: 13 unita' dopo la 450, la prossima alla 463",
   db.execute('select count(*) from units where path=? and line>450', (PATH,)).fetchone()[0] == 13
   and db.execute('select min(line) from units where path=? and line>450', (PATH,)).fetchone()[0] == 463)
righe = {u['line'] for u in tu}
altrui = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    if os.path.basename(os.path.dirname(f)) == os.path.basename(HERE):
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH and 40 <= u['line'] <= 450:
            altrui.append((os.path.basename(os.path.dirname(f)), u['line']))
ck('SEGMENTO: 18 righe distinte 40-450, nessun ALTRO lotto sulle stesse righe',
   len(righe) == 18 and min(righe) == 40 and max(righe) == 450 and not altrui, (len(righe), altrui))
ck('una sola tab (271) e nessun altra',
   [u['line'] for u in tu if u['italian'].startswith(TAB)] == [271])
nota = at[271]['italian']
_occ = 0
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    if os.path.basename(os.path.dirname(f)) == os.path.basename(HERE):
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['italian'] == nota:
            _occ += 1
ck('la nota dei rifornimenti usa una resa GIA presente nel corpus (>=2 altri lotti)', _occ >= 2, _occ)
ck('nomi invariati dove compaiono, e «Hai Slegati» invece di Unfettered',
   all(n in u['italian'] for u in tu for n in NOMI if n in u['english'])
   and 'Unfettered' not in ''.join(u['italian'] for u in tu))
ck('i due apici inglesi: righe 436 e 450',
   [u['line'] for u in tu if u['english'].count(APOS)] == [436, 450])
ck('la scala dei reattori cresce: piccolo, compatto, grande, nuclei sempre più grandi',
   'piccolo reattore' in at[376]['italian'] and 'compatto' in at[391]['italian']
   and 'grande reattore' in at[406]['italian'] and 'sempre più grandi' in at[421]['italian'])
ck('entrambi gli scudi dichiarano lo scambio ricarica/consumo',
   'più energia' in at[436]['italian'] and 'più energia' in at[450]['italian'])
ck('i raggi: uno per torretta, due nel Dual, 50% in più per il Moonbeam in torretta',
   'uno solo' in at[82]['italian'] and 'coppia' in at[114]['italian'] and '50%' in at[195]['italian'])
ck('il Thunderhead: cinque submunizioni, quaranta per lanciatore, stivaggio dedicato',
   'cinque submunizioni' in at[270]['italian'] and '40' in at[283]['italian']
   and 'Storage Array' in at[320]['italian'])
ck('VIRGOLETTE: zero · SEGNAPOSTO: nessuno · ALTERNATIVE: nessuna (asserzioni vuote)',
   sum(u['italian'].count(QUOTE) for u in tu) == 0
   and not TAG.findall(''.join(u['italian'] for u in tu))
   and sum(len(ALT.findall(u['italian'])) for u in tu) == 0)
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in tu for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessun doppio spazio (la tab iniziale non conta)',
   not [u['idx'] for u in tu if '  ' in u['italian'].lstrip(TAB)])
ck('rapporto nel gate 0,55-1,90',
   all(0.55 < u['ratio'] < 1.90 for u in tu),
   [(u['idx'], u['ratio']) for u in tu if not 0.55 < u['ratio'] < 1.90])
ck('tutte e 18 le unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in tu))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
tot = db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0]
print('copertura del file: %d/%d (%.1f%%) — stampata, NON asserita: il file non e\' finito' % (
    len(righe), tot, 100.0 * len(righe) / tot))
print('parole EN %d -> IT %d · ratio %.2f - %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(u['ratio'] for u in tu), max(u['ratio'] for u in tu)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L320 superato' if not fail else 'verify L320 fallito')
raise SystemExit(0 if not fail else 1)
