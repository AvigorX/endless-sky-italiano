r"""verify.py — L314 (`data/drak/drak culture conversations.txt`, righe 26-79). **Primo lotto** del file.

Verifica da sola e **solo fatti locali al segmento**, piu' un **limite monotono** (dopo la 79 restano 16 unita'): il file **non e'
finito**, quindi la copertura **si stampa** e non si asserisce.

Poi il contenuto: i **tre blocchi** (la prima unita' di ognuno senza tab, le altre tredici con), i **4 segnaposto** per tipo, la
**coppia di virgolette** nella sola riga 44, gli **apici inglesi** per unita', la **seconda persona** distribuita nei tre blocchi, e i
tre **svelamenti** finali.

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
SECONDA = re.compile(r'\b(ti|tu|tuo|tua|tuoi|tue|te|riesci|vedi|scendi|batti|riapri|noti|guardi|'
                     r'ritrovi|assopisco|sorprendi)\b')
HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
ROOT = os.path.abspath(os.path.join(L10N, '..'))
PATH = 'data/drak/drak culture conversations.txt'
PRIME = (26, 43, 74)
APICI_EN = {1: 1, 2: 1, 5: 1, 6: 1, 12: 1, 14: 1}
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


ck('riga grezza identica al sorgente (16/16)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = [u['idx'] for u in su
       if db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
       != (u['english'], u['kind'], u['path'], u['context'])]
ck('english/kind/path/context identici al DB', not bad, bad)
ck('16 unita, tutte MISSION_TEXT, 3 contesti',
   len(tu) == 16 and collections.Counter(u['kind'] for u in tu) == {'MISSION_TEXT': 16}
   and len({u['context'] for u in tu}) == 3)
ck("SEGMENTO: zero unita' prima della 26 (il lotto apre il file)",
   db.execute('select count(*) from units where path=? and line<26', (PATH,)).fetchone()[0] == 0)
ck("SEGMENTO: 16 unita' dopo la 79, la prossima alla 93",
   db.execute('select count(*) from units where path=? and line>79', (PATH,)).fetchone()[0] == 16
   and db.execute('select min(line) from units where path=? and line>79', (PATH,)).fetchone()[0] == 93)
righe = {u['line'] for u in tu}
altrui = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    if os.path.basename(os.path.dirname(f)) == os.path.basename(HERE):
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH and 26 <= u['line'] <= 79:
            altrui.append((os.path.basename(os.path.dirname(f)), u['line']))
ck('SEGMENTO: 16 righe distinte 26-79, nessun ALTRO lotto sulle stesse righe',
   len(righe) == 16 and min(righe) == 26 and max(righe) == 79 and not altrui,
   (len(righe), altrui))
ck('le prime unita dei tre blocchi NON hanno la tab, le altre tredici si',
   not [l for l in PRIME if at[l]['italian'].startswith(TAB)]
   and [u['line'] for u in tu if u['italian'].startswith(TAB)] ==
   [27, 28, 29, 30, 44, 45, 46, 47, 75, 76, 77, 78, 79])
ck('4 segnaposto identici per tipo: <ship> x3, <origin> x1',
   collections.Counter(TAG.findall(''.join(u['italian'] for u in tu)))
   == collections.Counter(TAG.findall(''.join(u['english'] for u in tu)))
   == {'<ship>': 3, '<origin>': 1})
ck('2 virgolette: una coppia nella sola riga 44',
   by[7]['italian'].count(QUOTE) == 2 and sum(u['italian'].count(QUOTE) for u in tu) == 2)
ck('apici inglesi: 6, uno per unita nelle righe attese',
   {i: by[i]['english'].count(APOS) for i in APICI_EN} == APICI_EN
   and sum(u['english'].count(APOS) for u in tu) == 6)
_per = collections.Counter(u['context'] for u in tu if SECONDA.search(u['italian']))
ck('seconda persona: almeno tre unita per blocco',
   all(_per[c] >= 3 for c in {u['context'] for u in tu}) and sum(_per.values()) >= 12, dict(_per))
ck('i tre svelamenti: sottoterra, pozzanghera normale, il letto',
   'sottoterra' in at[26]['italian'] and 'normale' in at[47]['italian']
   and 'letto' in at[79]['italian'])
ck('la visione Humanity: culla, masso, fiamme, entita senza forma',
   all(k in ''.join(u['italian'] for u in tu if u['context'].endswith('Humanity'))
       for k in ('culla', 'masso', 'fiamme', 'entità senza forma')))
ck('la visione Hai: arcipelago, onde che inghiottono navi e isole',
   'arcipelago' in at[45]['italian'] and 'inghiottono' in at[45]['italian'])
ck('la visione Arachi: nuvole, tunnel, marcia sopra la testa',
   'nuvole' in at[26]['italian'] and 'tunnel' in at[28]['italian']
   and 'marcia continua' in at[28]['italian'])
ck('ALTERNATIVE: nessuna (asserzione vuota)',
   sum(len(ALT.findall(u['italian'])) for u in tu) == 0)
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in tu for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessun doppio spazio (la tab iniziale non conta)',
   not [u['idx'] for u in tu if '  ' in u['italian'].lstrip(TAB)])
ck('rapporto nel gate 0,55-1,90',
   all(0.55 < u['ratio'] < 1.90 for u in tu),
   [(u['idx'], u['ratio']) for u in tu if not 0.55 < u['ratio'] < 1.90])
ck('tutte e 16 le unita sono PENDING',
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
print('FAIL:', len(fail), '·', 'verify L314 superato' if not fail else 'verify L314 fallito')
raise SystemExit(0 if not fail else 1)
