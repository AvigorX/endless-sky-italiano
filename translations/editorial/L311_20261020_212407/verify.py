r"""verify.py — L311 (`data/bunrodea/bunrodea outfits.txt`, righe 25-130). **Primo lotto** del file.

Verifica da sola e **solo fatti locali al segmento** (piu' un **limite monotono**: dopo la 130 restano unita'), perche' questo file
**non e' finito**: 12 delle 33 unita'. La copertura del **file** viene **stampata**, non asserita.

Poi il contenuto: la **famiglia della nota degli upgrade** (54 = 70 identiche; 114 e 130 diverse **solo nell'ultima parola**), le
**quattro coppie** con la tab sulla seconda, le **quattro schede singole**, i **nomi invariati**, le asserzioni vuote.

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
PATH = 'data/bunrodea/bunrodea outfits.txt'
NOMI = ['Shield Relay Booster', 'Shield Relay Limiter', 'Small Shield Relay', 'Large Shield Relay',
        'Nanite Enhancer', 'Nanite Limiter', 'Small Nanite Fabricator', 'Large Nanite Fabricator']
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


ck('riga grezza identica al sorgente (12/12)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = [u['idx'] for u in su
       if db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
       != (u['english'], u['kind'], u['path'], u['context'])]
ck('english/kind/path/context identici al DB', not bad, bad)
ck('12 unita, tutte DESCRIPTION in 8 contesti',
   len(tu) == 12 and collections.Counter(u['kind'] for u in tu) == {'DESCRIPTION': 12}
   and len({u['context'] for u in tu}) == 8)
ck("SEGMENTO: zero unita' prima della 25",
   db.execute('select count(*) from units where path=? and line<25', (PATH,)).fetchone()[0] == 0)
ck("SEGMENTO: 21 unita' dopo la 130 (limite monotono: il file non e' finito)",
   db.execute('select count(*) from units where path=? and line>130', (PATH,)).fetchone()[0] == 21)
righe = {u['line'] for u in tu}
altrui = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    if os.path.basename(os.path.dirname(f)) == os.path.basename(HERE):
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH and 25 <= u['line'] <= 130:
            altrui.append((os.path.basename(os.path.dirname(f)), u['line']))
ck('SEGMENTO: 12 righe distinte, dalla 25 alla 130, nessun ALTRO lotto sulle stesse righe',
   len(righe) == 12 and min(righe) == 25 and max(righe) == 130 and not altrui,
   (len(righe), min(righe), max(righe), altrui))
ck('le quattro coppie hanno la TAB sulla seconda unita',
   [u['line'] for u in tu if u['italian'].startswith(TAB)] == [54, 70, 114, 130])
ck('54 e 70 sono IDENTICHE in italiano (come in inglese)',
   by[4]['italian'] == by[6]['italian'] and by[4]['english'] == by[6]['english'])
ck('114 e 130 differiscono SOLO nell ultima parola',
   by[10]['italian'] != by[12]['italian']
   and by[10]['italian'].rsplit(' ', 1)[0] == by[12]['italian'].rsplit(' ', 1)[0])
ck('la differenza e quella del SORGENTE: `though.` / `however.`',
   by[10]['english'].rstrip().endswith('though.') and by[12]['english'].rstrip().endswith('however.')
   and by[10]['italian'].rstrip().endswith('però.') and by[12]['italian'].rstrip().endswith('tuttavia.'))
ck('le coppie condividono il contesto e la seconda porta la nota',
   all(at[l]['context'] == at[p]['context'] for l, p in ((53, 54), (69, 70), (113, 114), (129, 130)))
   and 'slot' in at[54]['italian'] and 'slot' in at[130]['italian'])
ck('nomi degli equipaggiamenti invariati dove compaiono',
   all(n in u['italian'] for u in tu for n in NOMI if n in u['english']))
ck('VIRGOLETTE: zero · SEGNAPOSTO: nessuno · ALTERNATIVE: nessuna (asserzioni vuote)',
   sum(u['italian'].count(QUOTE) for u in tu) == 0
   and not TAG.findall(''.join(u['italian'] for u in tu))
   and sum(len(ALT.findall(u['italian'])) for u in tu) == 0)
ck('apici: 1 in inglese, 9 in italiano',
   sum(u['english'].count(APOS) for u in tu) == 1 and sum(u['italian'].count(APOS) for u in tu) == 9,
   (sum(u['english'].count(APOS) for u in tu), sum(u['italian'].count(APOS) for u in tu)))
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in tu for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessun doppio spazio (la tab iniziale non conta)',
   not [u['idx'] for u in tu if '  ' in u['italian'].lstrip(TAB)])
ck('rapporto nel gate 0,55-1,90',
   all(0.55 < u['ratio'] < 1.90 for u in tu),
   [(u['idx'], u['ratio']) for u in tu if not 0.55 < u['ratio'] < 1.90])
ck('tutte e 12 le unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in tu))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
tot = db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0]
righe = {u['line'] for u in tu}
print('copertura del file: %d/%d (%.1f%%) — stampata, NON asserita: il file non e\' finito' % (
    len(righe), tot, 100.0 * len(righe) / tot))
print('parole EN %d -> IT %d · ratio %.2f - %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(u['ratio'] for u in tu), max(u['ratio'] for u in tu)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L311 superato' if not fail else 'verify L311 fallito')
raise SystemExit(0 if not fail else 1)
