r"""verify.py — L283 (`data/wanderer/wanderer missions.txt`, righe 42-88). **Secondo lotto del file**.

Verifica da sola: riga grezza, campi del DB, il **segmento** (13 prima, 14 qui, **27** dopo la 88), i **tre contesti** con le
loro righe, le **18 alternative** (numero e opzioni), i **sette tab**, le **diciotto virgolette**, i due `VALUE` copiati, e che
**nessun altro lotto** rivendichi le righe 42-88.

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
PATH = 'data/wanderer/wanderer missions.txt'
TOK = {'<origin>': 1, '<planet>': 2, '<system>': 1}
VALUES = (3, 12)
src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
su = sorted(src['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
raw_lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
by = {u['idx']: u for u in tu}
fail = []


def ck(n, c, d=''):
    print('%-96s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


def opz(x):
    return [p.strip() for p in re.split(r'[,?]', x.strip('[]')) if p.strip()]


ck('riga grezza identica al sorgente (14/14)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = [u['idx'] for u in su
       if db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
       != (u['english'], u['kind'], u['path'], u['context'])]
ck('english/kind/path/context identici al DB', not bad, bad)
ck('14 unita, righe distinte, 9 MISSION_TEXT + 2 DESCRIPTION + 2 VALUE + 1 DIALOG',
   len(tu) == 14 and len({u['line'] for u in tu}) == 14
   and collections.Counter(u['kind'] for u in tu) == {'MISSION_TEXT': 9, 'DESCRIPTION': 2, 'VALUE': 2, 'DIALOG': 1},
   (len(tu), collections.Counter(u['kind'] for u in tu)))
ck('tre contesti: `The Plant 1` (42-45), `2` (56-74), `3` (79-88)',
   {(c, min(u['line'] for u in tu if u['context'] == c), max(u['line'] for u in tu if u['context'] == c))
    for c in {u['context'] for u in tu}}
   == {('mission:Wanderers: Mereti: The Plant 1', 42, 45), ('mission:Wanderers: Mereti: The Plant 2', 56, 74),
       ('mission:Wanderers: Mereti: The Plant 3', 79, 88)},
   {(c, min(u['line'] for u in tu if u['context'] == c), max(u['line'] for u in tu if u['context'] == c))
    for c in {u['context'] for u in tu}})
ck("13 unita' prima della 42 e 27 dopo la 88",
   db.execute('select count(*) from units where path=? and line<42', (PATH,)).fetchone()[0] == 13
   and db.execute('select count(*) from units where path=? and line>88', (PATH,)).fetchone()[0] == 27)
ck('confine dopo: la 93 apre `The Plant 4`',
   db.execute('select line,context from units where path=? and line>88 order by line limit 1', (PATH,)).fetchone()
   == (93, 'mission:Wanderers: Mereti: The Plant 4'))
ck('il file ha 54 unita, righe 16-182',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (54, 16, 182))
righe = set()
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH:
            righe.add(u['line'])
seg = {l for l in righe if 42 <= l <= 88}
ck('SEGMENTO: le 14 righe del lotto sono esattamente quelle 42-88',
   seg == {u['line'] for u in tu} and len(seg) == 14, (sorted(seg - {u['line'] for u in tu}), len(seg)))
overlap = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    if os.path.basename(os.path.dirname(f)) == os.path.basename(HERE):
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH and 42 <= u['line'] <= 88:
            overlap.append((os.path.basename(os.path.dirname(f)), u['line']))
ck('nessun altro lotto rivendica le righe 42-88', not overlap, overlap)
ck('copertura: il lotto copre 14 righe del segmento e la copertura del file non PUO calare sotto 27',
   len(seg) == 14 and 27 <= len(righe) <= 54, '%d/54 (stampata, non asserita)' % len(righe))
ck('i due VALUE copiati e identici; le 12 unita non-VALUE tradotte',
   all(by[i]['italian'] == by[i]['english'] == 'A Home for the Plant' for i in VALUES)
   and all(u['italian'] != u['english'] for u in tu if u['idx'] not in VALUES))
ck('le due DESCRIPTION identiche fra loro in inglese e in italiano',
   by[4]['english'] == by[13]['english'] and by[4]['italian'] == by[13]['italian'])
ck('TAB: sette, unita 1 e 6-11, primo carattere in entrambe le lingue',
   sum(u['english'].count(TAB) for u in tu) == 7 == sum(u['italian'].count(TAB) for u in tu)
   and [u['idx'] for u in tu if TAB in u['italian']] == [1, 6, 7, 8, 9, 10, 11]
   and all(u['italian'].startswith(TAB) for u in tu if TAB in u['italian']))
ck('virgolette: 18 in tutto e lo stesso numero per ogni unita',
   sum(u['english'].count(QUOTE) for u in tu) == 18 == sum(u['italian'].count(QUOTE) for u in tu)
   and all(u['english'].count(QUOTE) == u['italian'].count(QUOTE) for u in tu))
ck('alternative: 18 per lingua, sei unita, due opzioni per coppia',
   sum(len(ALT.findall(u['english'])) for u in tu) == 18 == sum(len(ALT.findall(u['italian'])) for u in tu)
   and [u['idx'] for u in tu if ALT.findall(u['italian'])] == [1, 6, 7, 10, 11, 14]
   == [u['idx'] for u in tu if ALT.findall(u['english'])]
   and all(len(opz(a)) == 2 for u in tu for a in ALT.findall(u['italian']))
   and all(len(opz(a)) == 2 for u in tu for a in ALT.findall(u['english'])))
ck('alternative: nessuna coppia resta in inglese',
   not [a for u in tu for a in ALT.findall(u['italian']) if a == '[' + a[1:-1] + ']' and a[1:-1] in u['english']],
   [a for u in tu for a in ALT.findall(u['italian']) if a[1:-1] in u['english']])
ck('segnaposto per famiglia: quattro token, tre famiglie, identici',
   {t: sum(collections.Counter(TAG.findall(u['english']))[t] for u in tu) for t in TOK} == TOK
   == {t: sum(collections.Counter(TAG.findall(u['italian']))[t] for u in tu) for t in TOK})
ck('apici: 9 in inglese, 15 in italiano',
   sum(u['english'].count(APOS) for u in tu) == 9 and sum(u['italian'].count(APOS) for u in tu) == 15,
   (sum(u['english'].count(APOS) for u in tu), sum(u['italian'].count(APOS) for u in tu)))
ck("`Va'ika` nove volte in entrambe le lingue, invariato",
   sum(u['english'].count("Va'ika") for u in tu) == 9 == sum(u['italian'].count("Va'ika") for u in tu))
ck('`Unfettered` -> «Slegati»; `Sopi Lefarkata` invariato',
   'Slegati' in by[8]['italian'] and 'Unfettered' not in by[8]['italian']
   and 'Sopi Lefarkata' in by[14]['italian'])
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in tu for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90 per le 12 unita tradotte',
   all(0.55 < u['ratio'] < 1.90 for u in tu if u['idx'] not in VALUES),
   [(u['idx'], u['ratio']) for u in tu if u['idx'] not in VALUES and not 0.55 < u['ratio'] < 1.90])
ck('tutte le 14 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in tu))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('SEGMENTO: 13 prima · 14 qui · 27 dopo · 3 contesti · file 27/54')
print('parole EN %d -> IT %d · ratio %.2f - %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(u['ratio'] for u in tu if u['idx'] not in VALUES),
    max(u['ratio'] for u in tu if u['idx'] not in VALUES)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L283 superato' if not fail else 'verify L283 fallito')
raise SystemExit(0 if not fail else 1)
