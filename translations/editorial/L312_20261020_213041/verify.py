r"""verify.py — L312 (`data/bunrodea/bunrodea outfits.txt`, righe 135-236). **Secondo lotto** del file.

Verifica da sola e **solo fatti locali al segmento** (piu' due **limiti monotoni**: 12 unita' prima, 9 dopo), perche' il file
**non e' finito**: 24 delle 33 unita'. La copertura del **file** viene **stampata**, non asserita.

Poi il contenuto: il `VALUE` copiato per identita', la **famiglia delle tre note dei reattori** (204 = 220 = 236, `though.` in tutte
e tre), le due virgolette nella sola riga 235, i nomi invariati, le asserzioni vuote.

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
NOMI = ['Solar Battery', 'Solar Cell', 'Reactor Overclocker', 'Reactor Limiter',
        'Quark Reactor', 'Electroweak Reactor', 'Dark Reactor']
src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
su = sorted(src['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
raw_lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
by = {u['idx']: u for u in tu}
at = {u['line']: u for u in tu}
fail = []


def ck(n, c, d=''):
    print('%-98s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
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
ck('12 unita: 1 VALUE + 11 DESCRIPTION in 7 contesti',
   len(tu) == 12 and collections.Counter(u['kind'] for u in tu) == {'VALUE': 1, 'DESCRIPTION': 11}
   and len({u['context'] for u in tu}) == 7)
ck("SEGMENTO: 12 unita' prima (L311)",
   db.execute('select count(*) from units where path=? and line<135', (PATH,)).fetchone()[0] == 12)
ck("SEGMENTO: 9 unita' dopo la 236, la prossima alla 250",
   db.execute('select count(*) from units where path=? and line>236', (PATH,)).fetchone()[0] == 9
   and db.execute('select min(line) from units where path=? and line>236', (PATH,)).fetchone()[0] == 250)
righe = {u['line'] for u in tu}
altrui = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    if os.path.basename(os.path.dirname(f)) == os.path.basename(HERE):
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH and 135 <= u['line'] <= 236:
            altrui.append((os.path.basename(os.path.dirname(f)), u['line']))
ck('SEGMENTO: 12 righe distinte 135-236, nessun ALTRO lotto sulle stesse righe',
   len(righe) == 12 and min(righe) == 135 and max(righe) == 236 and not altrui,
   (len(righe), min(righe), max(righe), altrui))
ck('il VALUE `Solar Batteries` e copiato per identita',
   by[1]['italian'] == by[1]['english'] == 'Solar Batteries')
ck('la famiglia delle tre note: 204 == 220 == 236 in italiano, come in inglese',
   by[8]['italian'] == by[10]['italian'] == by[12]['italian']
   and by[8]['english'] == by[10]['english'] == by[12]['english'])
ck('tutte e tre chiudono con `though.` -> «però.»',
   all(by[i]['english'].rstrip().endswith('though.') for i in (8, 10, 12))
   and all(by[i]['italian'].rstrip().endswith('però.') for i in (8, 10, 12)))
ck('tab nelle quattro unita: 160, 204, 220, 236',
   [u['line'] for u in tu if u['italian'].startswith(TAB)] == [160, 204, 220, 236])
ck('2 virgolette: una coppia nella sola riga 235',
   by[11]['italian'].count(QUOTE) == 2
   and sum(u['italian'].count(QUOTE) for u in tu) == 2)
ck('nomi degli oggetti invariati dove compaiono',
   all(n in u['italian'] for u in tu for n in NOMI if n in u['english']))
ck('SEGNAPOSTO: nessuno · ALTERNATIVE: nessuna (asserzioni vuote)',
   not TAG.findall(''.join(u['italian'] for u in tu))
   and sum(len(ALT.findall(u['italian'])) for u in tu) == 0)
ck('apici: 1 in inglese, 12 in italiano',
   sum(u['english'].count(APOS) for u in tu) == 1 and sum(u['italian'].count(APOS) for u in tu) == 12,
   (sum(u['english'].count(APOS) for u in tu), sum(u['italian'].count(APOS) for u in tu)))
ck('overclocker e limiter: prima frase identica, seconda frase OPPOSTA',
   by[5]['italian'].split('è un componente', 1)[1].split('.')[0]
   == by[6]['italian'].split('è un componente', 1)[1].split('.')[0]
   and by[5]['italian'].split('.')[1] != by[6]['italian'].split('.')[1])
ck('le celle solari: calore di scarto che cresce con l energia',
   'calore di scarto' in by[3]['italian'] and 'cresce con' in by[3]['italian'])
ck('Polaris, XXVIII secolo, materia di quark',
   all(k in by[7]['italian'] for k in ('Polaris', 'XXVIII secolo', 'materia di quark')))
ck('stella elettrodebole, quark -> leptoni',
   'elettrodebole' in by[9]['italian'] and 'leptoni' in by[9]['italian'])
ck('stella oscura, materia oscura, siti di nucleazione',
   all(k in by[11]['italian'] for k in ('stella oscura', 'materia oscura', 'nucleazione')))
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
print('copertura del file: %d/%d (%.1f%%) — stampata, NON asserita: il file non e\' finito' % (
    len(righe), tot, 100.0 * len(righe) / tot))
print('parole EN %d -> IT %d · ratio %.2f - %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(u['ratio'] for u in tu), max(u['ratio'] for u in tu)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L312 superato' if not fail else 'verify L312 fallito')
raise SystemExit(0 if not fail else 1)
