r"""verify.py — L285 (`data/wanderer/wanderer missions.txt`, righe 169-182). **LOTTO TERMINALE**.

Verifica da sola, e verifica il **FILE INTERO**: 54 unita', **somma dei lotti 13 + 14 + 18 + 9 = 54**, **righe distinte**,
**ultima riga 182**, **zero unita' dopo**. Poi il lotto: riga grezza, campi del DB, **un solo contesto**, le **due scelte** fra
parentesi, le **6 alternative**, i **tre `sitrasanir`**, **otto tab**, **otto virgolette**, e che **nessun altro lotto**
rivendichi le righe 169-182.

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
PAR = re.compile(r'\([^()]*\)')
HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
ROOT = os.path.abspath(os.path.join(L10N, '..'))
PATH = 'data/wanderer/wanderer missions.txt'
TOK = {'<planet>': 1, '<first>': 1, '<last>': 1}
ID_OK = (6,)
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


ck('riga grezza identica al sorgente (9/9)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = [u['idx'] for u in su
       if db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
       != (u['english'], u['kind'], u['path'], u['context'])]
ck('english/kind/path/context identici al DB', not bad, bad)
ck('9 unita, righe distinte, tutte MISSION_TEXT',
   len(tu) == 9 and len({u['line'] for u in tu}) == 9 and {u['kind'] for u in tu} == {'MISSION_TEXT'})
ck('un solo contesto: `mission:Wanderers: Mereti: The Plant Epilogue`',
   {u['context'] for u in tu} == {'mission:Wanderers: Mereti: The Plant Epilogue'})
ck("45 unita' prima della 169 (13 + 14 + 18)",
   db.execute('select count(*) from units where path=? and line<169', (PATH,)).fetchone()[0] == 45)
ck("ZERO unita' dopo la 182: il lotto CHIUDE il file",
   db.execute('select count(*) from units where path=? and line>182', (PATH,)).fetchone()[0] == 0)
righe, lotti = set(), []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    us = [u for u in json.load(open(f, encoding='utf-8'))['units'] if u['path'] == PATH]
    if us:
        lotti.append((os.path.basename(os.path.dirname(f)), len(us)))
        righe |= {u['line'] for u in us}
ck('FILE: i quattro lotti del file sommano 54 unita (13 + 14 + 18 + 9)',
   [n for _, n in lotti] == [13, 14, 18, 9] and sum(n for _, n in lotti) == 54 == len(righe),
   (lotti, len(righe)))
ck('FILE: 54 unita, 54 righe distinte, ultima riga 182, nessuna oltre',
   len(righe) == 54 and max(righe) == 182
   and db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (54, 16, 182))
ck('FILE: copertura 54/54 (100%) — nessuna unita del file fuori dallo staging',
   len(righe) == db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0],
   '%d/%d' % (len(righe), db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0]))
overlap = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    if os.path.basename(os.path.dirname(f)) == os.path.basename(HERE):
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH and 169 <= u['line'] <= 182:
            overlap.append((os.path.basename(os.path.dirname(f)), u['line']))
ck('nessun altro lotto rivendica le righe 169-182', not overlap, overlap)
ck('le 8 unita di prosa sono tradotte; la sola identica e il nome proprio `"Sitrasanir?"`',
   all(u['italian'] != u['english'] for u in tu if u['idx'] not in ID_OK)
   and all(by[i]['italian'] == by[i]['english'] for i in ID_OK))
ck('TAB: otto, unita 2-9, primo carattere; la 1 no',
   sum(u['english'].count(TAB) for u in tu) == 8 == sum(u['italian'].count(TAB) for u in tu)
   and [u['idx'] for u in tu if TAB in u['italian']] == [2, 3, 4, 5, 6, 7, 8, 9]
   and not by[1]['italian'].startswith(TAB))
ck('virgolette: 8 in tutto e lo stesso numero per ogni unita',
   sum(u['english'].count(QUOTE) for u in tu) == 8 == sum(u['italian'].count(QUOTE) for u in tu)
   and all(u['english'].count(QUOTE) == u['italian'].count(QUOTE) for u in tu))
ck('scelte del giocatore: due parentesi, unita 2 e 3, punto finale DENTRO',
   [u['idx'] for u in tu if PAR.findall(u['italian'])] == [2, 3]
   and PAR.findall(by[2]['italian']) == ['(Guarda più da vicino.)']
   and PAR.findall(by[3]['italian']) == ['(Non ora.)'])
ck('alternative: 6 per lingua, tutte coppie, su unita 5 e 8',
   sum(len(ALT.findall(u['english'])) for u in tu) == 6 == sum(len(ALT.findall(u['italian'])) for u in tu)
   and [u['idx'] for u in tu if ALT.findall(u['italian'])] == [5, 8]
   and all(len(opz(a)) == 2 for u in tu for a in ALT.findall(u['italian']))
   and '[presenti? vivi?]' in by[8]['italian'])
ck('segnaposto per famiglia: tre token, tre famiglie, identici',
   {t: sum(collections.Counter(TAG.findall(u['english']))[t] for u in tu) for t in TOK} == TOK
   == {t: sum(collections.Counter(TAG.findall(u['italian']))[t] for u in tu) for t in TOK})
ck('apici: 2 in inglese, 1 in italiano',
   sum(u['english'].count(APOS) for u in tu) == 2 and sum(u['italian'].count(APOS) for u in tu) == 1,
   (sum(u['english'].count(APOS) for u in tu), sum(u['italian'].count(APOS) for u in tu)))
ck('`sitrasanir` tre volte, invariato, e `Strong Wind` invariato',
   sum(u['italian'].lower().count('sitrasanir') for u in tu) == 3
   == sum(u['english'].lower().count('sitrasanir') for u in tu)
   and 'Strong Wind' in by[4]['italian'])
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in tu for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90 su tutte e nove',
   all(0.55 < u['ratio'] < 1.90 for u in tu),
   [(u['idx'], u['ratio']) for u in tu if not 0.55 < u['ratio'] < 1.90])
ck('tutte le 9 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in tu))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('FILE: 54/54 (100%) · somma lotti 13+14+18+9 · ultima riga 182 · zero dopo')
print('parole EN %d -> IT %d · ratio %.2f - %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(u['ratio'] for u in tu), max(u['ratio'] for u in tu)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L285 superato' if not fail else 'verify L285 fallito')
raise SystemExit(0 if not fail else 1)
