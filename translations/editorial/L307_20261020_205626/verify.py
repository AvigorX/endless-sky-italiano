r"""verify.py — L307 (`data/avgi/avgi weapons.txt`, righe 25-203). **PRIMO lotto del file**.

Verifica da sola: riga grezza, campi del DB, il **segmento** (**0** prima, **12** qui, **34** dopo la 203), le **due terzine** con
due tab consecutive, le **due coppie**, la **ripetizione 69/108**, il **refuso non riprodotto** (174) e il **collegamento
torretta -> generatore** (203), e che **nessun altro lotto** rivendichi le righe 25-203.

Indipendente da `check.py`. La copertura del **FILE** e' **stampata, non asserita**.
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
PATH = 'data/avgi/avgi weapons.txt'
TERZINE = {'outfit:Speckle Coilgun': [67, 68, 69], 'outfit:Speckle Turret': [106, 107, 108]}
COPPIE = [(173, 174), (202, 203)]
TABBED = [68, 69, 107, 108, 174, 203]
NOTA = '\tLe munizioni di quest\'arma si possono rifornire in qualsiasi emporio.'
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
grp = collections.Counter(u['context'] for u in tu)
ck('12 unita DESCRIPTION, sei contesti (2 terzine + 2 coppie + 2 singole)',
   len(tu) == 12 and {u['kind'] for u in tu} == {'DESCRIPTION'}
   and sorted(grp.values()) == [1, 1, 2, 2, 3, 3], dict(grp))
ck("ZERO unita' prima della 25 (il lotto apre il file) e 34 dopo la 203",
   db.execute('select count(*) from units where path=? and line<25', (PATH,)).fetchone()[0] == 0
   and db.execute('select count(*) from units where path=? and line>203', (PATH,)).fetchone()[0] == 34)
ck('la prima unita dopo la 203 e `Blue Optical Laser` alla 264',
   db.execute('select line,context from units where path=? and line>203 order by line limit 1', (PATH,)).fetchone()
   == (264, 'outfit:Blue Optical Laser'))
ck('il file ha 46 unita (35 DESCRIPTION + 7 TEXT + 4 VALUE), righe 25-969',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (46, 25, 969)
   and dict(db.execute('select kind,count(*) from units where path=? group by kind', (PATH,)).fetchall())
   == {'DESCRIPTION': 35, 'TEXT': 7, 'VALUE': 4})
righe = set()
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH:
            righe.add(u['line'])
seg = {l for l in righe if 25 <= l <= 203}
ck('SEGMENTO: le 12 righe del lotto sono esattamente quelle 25-203',
   seg == {u['line'] for u in tu} and len(seg) == 12, (sorted(seg - {u['line'] for u in tu}), len(seg)))
overlap = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    if os.path.basename(os.path.dirname(f)) == os.path.basename(HERE):
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH and 25 <= u['line'] <= 203:
            overlap.append((os.path.basename(os.path.dirname(f)), u['line']))
ck('nessun altro lotto rivendica le righe 25-203', not overlap, overlap)
ck('copertura: 12 righe nel segmento; totale del file stampato e non supera 46',
   len(seg) == 12 and len(righe) <= 46, '%d/46 al momento' % len(righe))
ck('tutte e 12 le unita sono tradotte', all(u['italian'] != u['english'] for u in tu))
ck('TERZINE con tab sulla seconda e sulla terza',
   all([u['line'] for u in tu if u['context'] == c] == ls for c, ls in TERZINE.items())
   and all(at[l]['english'].startswith(TAB) and at[l]['italian'].startswith(TAB)
           for ls in TERZINE.values() for l in ls[1:]))
ck('TAB: sei in tutto, righe dichiarate', sorted(u['line'] for u in tu if u['english'].startswith(TAB)) == TABBED
   and sum(u['italian'].count(TAB) for u in tu) == 6)
ck('COPPIE con tab sulla seconda', all(at[b]['context'] == at[a]['context'] for a, b in COPPIE))
ck('RIPETIZIONE: 69 e 108 identiche, e diverse da tutte le altre',
   at[69]['english'] == at[108]['english'] and at[69]['italian'] == at[108]['italian'] == NOTA)
ck('refuso non riprodotto: 174 dice `can altered` in inglese e «può essere modificata» in italiano',
   'can altered' in at[174]['english'] and 'può essere modificata' in at[174]['italian']
   and 'altered' not in at[174]['italian'])
ck('collegamento torretta -> generatore nella 203',
   'Optical Lasing Generator' in at[203]['italian'] and 'tre Green Laser' in at[203]['italian'])
ck('ASSERZIONI VUOTE: 0 virgolette, 0 segnaposto, 0 alternative',
   sum(u['english'].count(QUOTE) for u in tu) == 0 == sum(u['italian'].count(QUOTE) for u in tu)
   and sum(len(TAG.findall(u['italian'])) for u in tu) == 0
   and sum(len(ALT.findall(u['italian'])) for u in tu) == 0)
ck('apici: 1 in inglese, 10 in italiano',
   sum(u['english'].count(APOS) for u in tu) == 1 and sum(u['italian'].count(APOS) for u in tu) == 10,
   (sum(u['english'].count(APOS) for u in tu), sum(u['italian'].count(APOS) for u in tu)))
ck('terminologia: emporio, coilgun, antimissile, cannone a massa',
   'emporio' in at[69]['italian'] and 'coilgun' in at[67]['italian']
   and 'antimissile' in at[202]['italian'] and 'cannone a massa' in at[68]['italian'])
ck('nomi invariati', all(n in ''.join(u['italian'] for u in tu) for n in
                         ['Avgi', 'Speckle Coilgun', 'Optical Lasing Generator', 'Green Optical Laser']))
ck('registro: nessuna seconda persona',
   not [u['idx'] for u in tu if re.search(r'\b(tu|tuo|tua|tuoi|tue|ti|te)\b', u['italian'])])
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in tu for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessun doppio spazio (la tab iniziale non conta)',
   not [u['idx'] for u in tu if '  ' in u['italian'].lstrip(TAB)])
ck('rapporto nel gate 0,55-1,90',
   all(0.55 < u['ratio'] < 1.90 for u in tu),
   [(u['idx'], u['ratio']) for u in tu if not 0.55 < u['ratio'] < 1.90])
ck('tutte le 12 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in tu))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('SEGMENTO: 0 prima · 12 qui · 34 dopo la 203 · 2 terzine + 2 coppie + 2 singole · file %d/46' % len(righe))
print('parole EN %d -> IT %d · ratio %.2f - %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(u['ratio'] for u in tu), max(u['ratio'] for u in tu)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L307 superato' if not fail else 'verify L307 fallito')
raise SystemExit(0 if not fail else 1)
