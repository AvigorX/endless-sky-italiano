r"""verify.py — L298 (`data/coalition/coalition outfits.txt`, righe 202-337). **Secondo lotto del file**.

Verifica da sola: riga grezza, campi del DB, il **segmento** (**15** prima, **15** qui, **19** dopo la 337), le **cinque coppie
con tab**, le **cinque singole**, la **coppia a cavallo del confine** (336-337 interamente dentro, l'unita' dopo e' alla 356 e ha
un altro contesto), le asserzioni vuote, i nomi delle fazioni, e che **nessun altro lotto** rivendichi le righe 202-337.

Indipendente da `check.py`: rilegge `source.json`, il `translation.json`, il database, il file del gioco e **tutti** i
`translation.json` dello staging. La copertura del **FILE** e' **stampata, non asserita**.
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
PATH = 'data/coalition/coalition outfits.txt'
PAIRS = [(246, 247), (259, 260), (273, 274), (289, 290), (336, 337)]
TABBED = [247, 260, 274, 290, 337]
SINGOLE = [202, 218, 232, 306, 323]
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


ck('riga grezza identica al sorgente (15/15)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = [u['idx'] for u in su
       if db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
       != (u['english'], u['kind'], u['path'], u['context'])]
ck('english/kind/path/context identici al DB', not bad, bad)
ck('15 unita, tutte DESCRIPTION, dieci contesti (cinque doppi + cinque singoli)',
   len(tu) == 15 and {u['kind'] for u in tu} == {'DESCRIPTION'} and len({u['context'] for u in tu}) == 10
   and sum(1 for n in collections.Counter(u['context'] for u in tu).values() if n == 2) == 5)
ck("15 unita' prima della 202 e 19 dopo la 337",
   db.execute('select count(*) from units where path=? and line<202', (PATH,)).fetchone()[0] == 15
   and db.execute('select count(*) from units where path=? and line>337', (PATH,)).fetchone()[0] == 19)
ck('la prima unita dopo la 337 e `Small Thrust Module` alla 356',
   db.execute('select line,context from units where path=? and line>337 order by line limit 1', (PATH,)).fetchone()
   == (356, 'outfit:Small Thrust Module'))
ck('la coppia 336-337 e INTERA nel lotto e il contesto dopo il confine e diverso',
   336 in at and 337 in at and at[336]['context'] == at[337]['context'] == 'outfit:Outskirts Gauger'
   and db.execute('select context from units where path=? and line>337 order by line limit 1', (PATH,)).fetchone()[0]
   != 'outfit:Outskirts Gauger')
ck('il file ha 49 unita, righe 26-533',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (49, 26, 533))
righe = set()
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH:
            righe.add(u['line'])
seg = {l for l in righe if 202 <= l <= 337}
ck('SEGMENTO: le 15 righe del lotto sono esattamente quelle 202-337',
   seg == {u['line'] for u in tu} and len(seg) == 15, (sorted(seg - {u['line'] for u in tu}), len(seg)))
overlap = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    if os.path.basename(os.path.dirname(f)) == os.path.basename(HERE):
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH and 202 <= u['line'] <= 337:
            overlap.append((os.path.basename(os.path.dirname(f)), u['line']))
ck('nessun altro lotto rivendica le righe 202-337', not overlap, overlap)
ck('copertura: 15 righe nel segmento; totale del file stampato e non supera 49',
   len(seg) == 15 and len(righe) <= 49, '%d/49 al momento' % len(righe))
ck('tutte e 15 le unita sono tradotte', all(u['italian'] != u['english'] for u in tu))
ck('TAB: cinque unita, righe dichiarate, primo carattere conservato',
   sorted(u['line'] for u in tu if u['english'].startswith(TAB)) == TABBED
   and all(at[l]['italian'].startswith(TAB) for l in TABBED)
   and sum(u['italian'].count(TAB) for u in tu) == 5)
ck('le cinque coppie hanno lo stesso contesto e la tab sulla seconda',
   all(at[b]['context'] == at[a]['context'] and at[b]['english'].startswith(TAB) and b - a == 1 for a, b in PAIRS))
ck('le cinque singole sono quelle dichiarate',
   [l for l, u in at.items() if collections.Counter(x['context'] for x in tu)[u['context']] == 1] == SINGOLE)
ck('ASSERZIONI VUOTE: 0 virgolette, 0 segnaposto, 0 alternative',
   sum(u['english'].count(QUOTE) for u in tu) == 0 == sum(u['italian'].count(QUOTE) for u in tu)
   and sum(len(TAG.findall(u['italian'])) for u in tu) == 0
   and sum(len(ALT.findall(u['italian'])) for u in tu) == 0)
ck('apici: 7 in inglese, 6 in italiano',
   sum(u['english'].count(APOS) for u in tu) == 7 and sum(u['italian'].count(APOS) for u in tu) == 6,
   (sum(u['english'].count(APOS) for u in tu), sum(u['italian'].count(APOS) for u in tu)))
ck('nomi: Lunarium e Saros invariati, `Casa Idriss`, `i Saryd`',
   'Lunarium' in ''.join(u['italian'] for u in tu) and 'Saros' in at[246]['italian']
   and 'Casa Idriss' in at[336]['italian'] and 'i Saryd' in at[246]['italian']
   and 'House Idriss' not in ''.join(u['italian'] for u in tu))
ck('registro: nessuna seconda persona',
   not [u['idx'] for u in tu if re.search(r'\b(tu|tuo|tua|tuoi|tue|ti|te)\b', u['italian'])])
ck('terminologia: rivestimento, siluri Heliarch, generatori di scudi, disturbo radar',
   'rivestimento' in at[259]['italian'] and 'siluri Heliarch' in at[260]['italian']
   and 'generatori di scudi' in at[289]['italian'] and 'disturbo radar' in at[260]['italian'])
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in tu for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessun doppio spazio', not [u['idx'] for u in tu if '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90',
   all(0.55 < u['ratio'] < 1.90 for u in tu),
   [(u['idx'], u['ratio']) for u in tu if not 0.55 < u['ratio'] < 1.90])
ck('tutte le 15 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in tu))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('SEGMENTO: 15 prima · 15 qui · 19 dopo la 337 · 5 coppie + 5 singole · file %d/49' % len(righe))
print('parole EN %d -> IT %d · ratio %.2f - %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(u['ratio'] for u in tu), max(u['ratio'] for u in tu)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L298 superato' if not fail else 'verify L298 fallito')
raise SystemExit(0 if not fail else 1)
