r"""verify.py — L316 (`data/coalition/coalition ships.txt`, righe 59-969). **Primo lotto** del file.

Verifica da sola e **solo fatti locali al segmento**, piu' un **limite monotono** (dopo la 969 restano 17 unita'): il file **non e'
finito**, quindi la copertura **si stampa** e non si asserisce.

Poi il contenuto: la **relazione fra contesti** della riga 275 (`Spindle` che descrive il `Hulk`), il **Judicator doppio** (968 + 969)
tutto dentro, la **sola tab** alla 969, i **due apici inglesi**, `Coalition` -> «Coalizione», i nomi invariati.

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
PATH = 'data/coalition/coalition ships.txt'
NAVI = ['Arach Courier', 'Arach Freighter', 'Arach Hulk', 'Arach Spindle', 'Arach Transport',
        'Breacher', 'Hunter', 'Interdictor', 'Judicator']
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


ck('riga grezza identica al sorgente (10/10)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = [u['idx'] for u in su
       if db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
       != (u['english'], u['kind'], u['path'], u['context'])]
ck('english/kind/path/context identici al DB', not bad, bad)
ck('10 unita, tutte DESCRIPTION, 9 contesti',
   len(tu) == 10 and collections.Counter(u['kind'] for u in tu) == {'DESCRIPTION': 10}
   and len({u['context'] for u in tu}) == 9)
ck("SEGMENTO: zero unita' prima della 59 (il lotto apre il file)",
   db.execute('select count(*) from units where path=? and line<59', (PATH,)).fetchone()[0] == 0)
ck("SEGMENTO: 17 unita' dopo la 969, la prossima alla 1141",
   db.execute('select count(*) from units where path=? and line>969', (PATH,)).fetchone()[0] == 17
   and db.execute('select min(line) from units where path=? and line>969', (PATH,)).fetchone()[0] == 1141)
righe = {u['line'] for u in tu}
altrui = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    if os.path.basename(os.path.dirname(f)) == os.path.basename(HERE):
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH and 59 <= u['line'] <= 969:
            altrui.append((os.path.basename(os.path.dirname(f)), u['line']))
ck('SEGMENTO: 10 righe distinte 59-969, nessun ALTRO lotto sulle stesse righe',
   len(righe) == 10 and min(righe) == 59 and max(righe) == 969 and not altrui, (len(righe), altrui))
ck('il Judicator ha due unita (968 + 969) e sta tutto dentro il lotto',
   [u['line'] for u in tu if u['context'].endswith('Judicator')] == [968, 969])
ck('la sola tab e alla 969, in prima posizione',
   [u['line'] for u in tu if u['italian'].startswith(TAB)] == [969])
ck('la 275 (contesto Spindle) descrive il Hulk, e il test lo verifica fra CONTESTI',
   at[275]['context'].endswith('Arach Spindle') and 'Hulk' in at[275]['english']
   and at[200]['context'].endswith('Arach Hulk'))
ck('`Coalition` -> «Coalizione», `Quarg` e i mondi ad anello',
   'Coalizione' in at[383]['italian'] and 'Quarg' in at[383]['italian']
   and 'mondi ad anello' in at[383]['italian'] and 'Coalition' not in at[383]['italian'])
ck('nomi delle navi invariati dove compaiono',
   all(n in u['italian'] for u in tu for n in NAVI if n in u['english']))
ck('il Hulk: pod laterali staccabili in pochi minuti',
   'pod laterali' in at[200]['italian'] and 'staccabili' in at[200]['italian'])
ck('il Breacher: volo radente; il Judicator: sei baie di caccia e cuccette',
   'volo radente' in at[461]['italian'] and 'sei baie di caccia' in at[969]['italian']
   and 'cuccette' in at[969]['italian'])
ck('l Interdictor: raggi attrattori e repulsori, aggancio iperspaziale',
   all(k in at[779]['italian'] for k in ('attrattori', 'repulsori', 'aggancio iperspaziale')))
ck('VIRGOLETTE: zero · SEGNAPOSTO: nessuno · ALTERNATIVE: nessuna (asserzioni vuote)',
   sum(u['italian'].count(QUOTE) for u in tu) == 0
   and not TAG.findall(''.join(u['italian'] for u in tu))
   and sum(len(ALT.findall(u['italian'])) for u in tu) == 0)
ck('apici: 2 in inglese (461, 968), 9 in italiano',
   [u['line'] for u in tu if u['english'].count(APOS)] == [461, 968]
   and sum(u['italian'].count(APOS) for u in tu) == 9)
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in tu for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessun doppio spazio (la tab iniziale non conta)',
   not [u['idx'] for u in tu if '  ' in u['italian'].lstrip(TAB)])
ck('rapporto nel gate 0,55-1,90',
   all(0.55 < u['ratio'] < 1.90 for u in tu),
   [(u['idx'], u['ratio']) for u in tu if not 0.55 < u['ratio'] < 1.90])
ck('tutte e 10 le unita sono PENDING',
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
print('FAIL:', len(fail), '·', 'verify L316 superato' if not fail else 'verify L316 fallito')
raise SystemExit(0 if not fail else 1)
