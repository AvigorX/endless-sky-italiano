r"""verify.py — L308 (`data/avgi/avgi weapons.txt`, righe 264-703). **Secondo lotto del file**.

Verifica da sola: riga grezza, campi del DB, il **segmento** (**12** prima, **21** qui, **13** dopo la 703), **i tre tipi**
(13 `DESCRIPTION` + 5 `TEXT` + 3 `VALUE`), i **TEXT/VALUE copiati verbatim**, le **10 virgolette**, le **tre terzine VLS**, il
**paragrafo VLS identico x3**, la **nota munizioni** confrontata con **L307** (famiglia a cinque), la **coppia 264/265** e la
**sorellanza 265/203**, e che **nessun altro lotto** rivendichi le righe 264-703.

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
PREV = os.path.join(L10N, 'staging', 'editorial', 'L307_20261020_205626', 'translation.json')
PATH = 'data/avgi/avgi weapons.txt'
TERZINE = {'outfit:Tiny VLS': [613, 614, 615], 'outfit:Small VLS': [657, 658, 659],
           'outfit:Medium VLS': [701, 702, 703]}
TABBED = [265, 614, 615, 658, 659, 702, 703]
VLS = [10, 15, 20]
AMMO = [11, 16, 21]
TEXT_IDX = [3, 5, 8, 13, 18]
VALUE_IDX = [7, 12, 17]
NOTA = '\tLe munizioni di quest\'arma si possono rifornire in qualsiasi emporio.'
src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
su = sorted(src['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
raw_lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
by = {u['idx']: u for u in tu}
at = {u['line']: u for u in tu}
prev = {u['line']: u for u in json.load(open(PREV, encoding='utf-8'))['units']}
fail = []


def ck(n, c, d=''):
    print('%-96s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente (21/21)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = [u['idx'] for u in su
       if db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
       != (u['english'], u['kind'], u['path'], u['context'])]
ck('english/kind/path/context identici al DB', not bad, bad)
kinds = collections.Counter(u['kind'] for u in tu)
grp = collections.Counter(u['context'] for u in tu)
ck('21 unita, tre tipi: 13 DESCRIPTION + 5 TEXT + 3 VALUE',
   len(tu) == 21 and kinds == {'DESCRIPTION': 13, 'TEXT': 5, 'VALUE': 3}, dict(kinds))
ck('sei contesti (tre VLS da cinque unita, due doppi, una coppia)',
   len(grp) == 6 and sorted(grp.values()) == [2, 2, 2, 5, 5, 5], dict(grp))
ck("12 unita' prima della 264 e 13 dopo la 703",
   db.execute('select count(*) from units where path=? and line<264', (PATH,)).fetchone()[0] == 12
   and db.execute('select count(*) from units where path=? and line>703', (PATH,)).fetchone()[0] == 13)
ck('la prima unita dopo la 703 apre `Nettle KKV` alla 716',
   db.execute('select line,context from units where path=? and line>703 order by line limit 1', (PATH,)).fetchone()
   == (716, 'outfit:"Nettle" KKV'))
righe = set()
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH:
            righe.add(u['line'])
seg = {l for l in righe if 264 <= l <= 703}
ck('SEGMENTO: le 21 righe del lotto sono esattamente quelle 264-703',
   seg == {u['line'] for u in tu} and len(seg) == 21, (sorted(seg - {u['line'] for u in tu}), len(seg)))
overlap = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    if os.path.basename(os.path.dirname(f)) == os.path.basename(HERE):
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH and 264 <= u['line'] <= 703:
            overlap.append((os.path.basename(os.path.dirname(f)), u['line']))
ck('nessun altro lotto rivendica le righe 264-703', not overlap, overlap)
ck('copertura: 21 righe nel segmento; totale del file stampato e non supera 46',
   len(seg) == 21 and len(righe) <= 46, '%d/46 al momento' % len(righe))
ck('TEXT copiati verbatim', all(by[i]['italian'] == by[i]['english'] for i in TEXT_IDX))
ck('VALUE copiati verbatim', all(by[i]['italian'] == by[i]['english'] for i in VALUE_IDX))
ck('10 virgolette in 5 coppie (una per TEXT)', sum(u['italian'].count(QUOTE) for u in tu) == 10
   and all(by[i]['italian'].count(QUOTE) == 2 for i in TEXT_IDX))
ck('le 13 DESCRIPTION sono tutte tradotte',
   all(u['italian'] != u['english'] for u in tu if u['kind'] == 'DESCRIPTION'))
ck('TERZINE VLS con tab sulla seconda e terza',
   all([u['line'] for u in tu if u['context'] == c and u['kind'] == 'DESCRIPTION'] == ls
       for c, ls in TERZINE.items())
   and all(at[l]['english'].startswith(TAB) and at[l]['italian'].startswith(TAB)
           for ls in TERZINE.values() for l in ls[1:]))
ck('TAB: sette in tutto, righe dichiarate', sorted(u['line'] for u in tu if u['english'].startswith(TAB)) == TABBED
   and sum(u['italian'].count(TAB) for u in tu) == 7)
ck('paragrafo VLS identico nelle tre colonne', len({by[i]['italian'] for i in VLS}) == 1)
ck('nota munizioni: tre qui identiche e uguali alle due di L307',
   len({by[i]['italian'] for i in AMMO}) == 1 and by[AMMO[0]]['italian'] == NOTA
   and prev[69]['italian'] == NOTA and prev[108]['italian'] == NOTA)
ck('265 sorella di 203 (L307): stessa frase, `un solo Blue Laser` vs `tre Green Laser`',
   at[265]['italian'].replace('un solo Blue Laser', 'X') == prev[203]['italian'].replace('tre Green Laser', 'X'))
ck('ASSERZIONI VUOTE: 0 segnaposto, 0 alternative',
   sum(len(TAG.findall(u['italian'])) for u in tu) == 0
   and sum(len(ALT.findall(u['italian'])) for u in tu) == 0)
ck('apici: 3 in inglese, 9 in italiano',
   sum(u['english'].count(APOS) for u in tu) == 3 and sum(u['italian'].count(APOS) for u in tu) == 9,
   (sum(u['english'].count(APOS) for u in tu), sum(u['italian'].count(APOS) for u in tu)))
ck('lessico: pilone, catapulta elettromagnetica, celle di lancio, alloggiamento per torrette',
   'pilone' in at[531]['italian'] and 'catapulta elettromagnetica' in at[531]['italian']
   and 'celle di lancio' in at[613]['italian'] and 'alloggiamento per torrette' in at[613]['italian'])
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in tu for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessun doppio spazio (la tab iniziale non conta)',
   not [u['idx'] for u in tu if '  ' in u['italian'].lstrip(TAB)])
ck('rapporto nel gate 0,55-1,90',
   all(0.55 < u['ratio'] < 1.90 for u in tu),
   [(u['idx'], u['ratio']) for u in tu if not 0.55 < u['ratio'] < 1.90])
ck('tutte le 21 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in tu))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('SEGMENTO: 12 prima · 21 qui · 13 dopo la 703 · 13 DESC + 5 TEXT + 3 VALUE · file %d/46' % len(righe))
print('parole EN %d -> IT %d · ratio %.2f - %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(u['ratio'] for u in tu), max(u['ratio'] for u in tu)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L308 superato' if not fail else 'verify L308 fallito')
raise SystemExit(0 if not fail else 1)
