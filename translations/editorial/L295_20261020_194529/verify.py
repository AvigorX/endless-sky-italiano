r"""verify.py — L295 (`data/human/marauders.txt`, righe 548-858). **Secondo lotto del file**.

Verifica da sola: riga grezza, campi del DB, il **segmento** (12 prima, 9 qui, **8** dopo la 858), le **tre serie da tre**, la
**ripetizione del sorgente** (unita' 8 e 9 identiche in entrambe le lingue), le **frasi condivise** (`Manta` 5/6, `Quicksilver`
7/8), le **asserzioni vuote**, il **registro impersonale**, la **continuita' del `Quicksilver`** oltre il confine, e che
**nessun altro lotto** rivendichi le righe 548-858.

Indipendente da `check.py`: rilegge `source.json`, il `translation.json`, il database, il file del gioco e **tutti** i
`translation.json` dello staging.
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
PATH = 'data/human/marauders.txt'
SERIES = {'ship:Marauder Leviathan': [548, 580, 616], 'ship:Marauder Manta': [676, 710, 747],
          'ship:Marauder Quicksilver': [799, 831, 858]}
NAMES = ['Leviathan', 'Manta', 'Quicksilver', 'Betelgeuse', 'Megaparsec', 'Lionheart', 'Headhunter']
CHIUSA = 'Se il suo tonnellaggio a vuoto fosse appena più alto, sarebbe classificata come nave da guerra pesante.'
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


ck('riga grezza identica al sorgente (9/9)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = [u['idx'] for u in su
       if db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
       != (u['english'], u['kind'], u['path'], u['context'])]
ck('english/kind/path/context identici al DB', not bad, bad)
ck('9 unita, righe tutte quelle dichiarate, tutte DESCRIPTION',
   len(tu) == 9 and {u['line'] for u in tu} == {l for ls in SERIES.values() for l in ls}
   and {u['kind'] for u in tu} == {'DESCRIPTION'})
ck('tre serie da tre, contesti con le righe dichiarate',
   {(u['context'], u['line']) for u in tu} == {(c, l) for c, ls in SERIES.items() for l in ls},
   {(u['context'], u['line']) for u in tu})
ck("12 unita' prima della 548 e 8 dopo la 858",
   db.execute('select count(*) from units where path=? and line<548', (PATH,)).fetchone()[0] == 12
   and db.execute('select count(*) from units where path=? and line>858', (PATH,)).fetchone()[0] == 8)
ck('il Quicksilver continua oltre il confine (la prima unita dopo la 858 e ancora sua)',
   db.execute('select context from units where path=? and line>858 order by line limit 1', (PATH,)).fetchone()
   == ('ship:Marauder Quicksilver',))
ck('il file ha 29 unita, righe 62-1146',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (29, 62, 1146))
righe = set()
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH:
            righe.add(u['line'])
seg = {l for l in righe if 548 <= l <= 858}
ck('SEGMENTO: le 9 righe del lotto sono esattamente quelle 548-858',
   seg == {u['line'] for u in tu} and len(seg) == 9, (sorted(seg - {u['line'] for u in tu}), len(seg)))
overlap = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    if os.path.basename(os.path.dirname(f)) == os.path.basename(HERE):
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH and 548 <= u['line'] <= 858:
            overlap.append((os.path.basename(os.path.dirname(f)), u['line']))
ck('nessun altro lotto rivendica le righe 548-858', not overlap, overlap)
ck('copertura: 9 righe nel segmento, il totale del file e stampato e non supera 29',
   len(seg) == 9 and len(righe) <= 29, '%d/29 al momento' % len(righe))
ck('tutte e 9 le unita sono tradotte', all(u['italian'] != u['english'] for u in tu))
ck('RIPETIZIONE: 831 e 858 identiche in inglese e in italiano',
   at[831]['english'] == at[858]['english'] and at[831]['italian'] == at[858]['italian'])
ck('frasi condivise: `Manta` 5/6 chiudono uguale; `Quicksilver` 7/8 condividono la frase sulla torretta',
   at[710]['italian'].endswith(CHIUSA) and at[747]['italian'].endswith(CHIUSA)
   and 'in risposta alla Headhunter della Lionheart' in at[799]['italian']
   and 'in risposta alla Headhunter della Lionheart' in at[831]['italian'])
ck('asserzioni vuote: 0 tab, 0 virgolette, 0 segnaposto, 0 alternative',
   sum(u['english'].count(TAB) for u in tu) == 0 == sum(u['italian'].count(TAB) for u in tu)
   and sum(u['english'].count(QUOTE) for u in tu) == 0 == sum(u['italian'].count(QUOTE) for u in tu)
   and sum(len(TAG.findall(u['italian'])) for u in tu) == 0
   and sum(len(ALT.findall(u['italian'])) for u in tu) == 0)
ck('apici: 8 in inglese, 14 in italiano',
   sum(u['english'].count(APOS) for u in tu) == 8 and sum(u['italian'].count(APOS) for u in tu) == 14,
   (sum(u['english'].count(APOS) for u in tu), sum(u['italian'].count(APOS) for u in tu)))
ck('registro impersonale: nessuna seconda persona',
   not [u['idx'] for u in tu if re.search(r'\b(tu|tuo|tua|tuoi|tue|ti|te|possiate|sospetti)\b', u['italian'])])
ck('nomi invariati', all(n in ''.join(u['italian'] for u in tu) for n in NAMES),
   [n for n in NAMES if n not in ''.join(u['italian'] for u in tu)])
ck('`proiettori di scudi` (projectors) distinto da `emettitori di scudi` (emitters)',
   'proiettori di scudi' in at[548]['italian'] and 'emettitori di scudi' in at[676]['italian'])
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in tu for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90',
   all(0.55 < u['ratio'] < 1.90 for u in tu),
   [(u['idx'], u['ratio']) for u in tu if not 0.55 < u['ratio'] < 1.90])
ck('tutte le 9 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in tu))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('SEGMENTO: 12 prima · 9 qui · 8 dopo la 858 · 3 serie da 3 · unita 8 e 9 identiche')
print('parole EN %d -> IT %d · ratio %.2f - %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(u['ratio'] for u in tu), max(u['ratio'] for u in tu)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L295 superato' if not fail else 'verify L295 fallito')
raise SystemExit(0 if not fail else 1)
