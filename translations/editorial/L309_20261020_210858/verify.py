r"""verify.py — L309 (`data/avgi/avgi weapons.txt`, righe 716-969). **LOTTO TERMINALE**.

Verifica da sola, e verifica il **FILE INTERO**: 46 unita', **somma dei lotti 12 + 21 + 13 = 46**, **righe distinte**, **prima riga
25**, **ultima 969**, **zero unita' dopo**. Poi il lotto: riga grezza, campi del DB, i **tre tipi**, le **due terzine**, le **due
coppie**, la **frase «ammunition for» in tre varianti**, l'**assenza della nota munizioni**, la **seconda persona** nei soli avvisi,
e che **nessun altro lotto** rivendichi le righe 716-969.

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
PATH = 'data/avgi/avgi weapons.txt'
TERZINE = {"outfit:\"Orchid\" Nuclear Missile": [801, 802, 803],
           "outfit:\"Ophrys\" Nuclear Torpedo": [949, 950, 951]}
COPPIE = [(716, 717), (968, 969)]
TABBED = [717, 802, 803, 950, 951, 969]
TEXT_IDX = [4, 11]
VALUE_IDX = [3]
AMMO3 = [2, 7, 10]
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


ck('riga grezza identica al sorgente (13/13)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = [u['idx'] for u in su
       if db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
       != (u['english'], u['kind'], u['path'], u['context'])]
ck('english/kind/path/context identici al DB', not bad, bad)
kinds = collections.Counter(u['kind'] for u in tu)
grp = collections.Counter(u['context'] for u in tu)
ck('13 unita, tre tipi: 10 DESCRIPTION + 2 TEXT + 1 VALUE',
   len(tu) == 13 and kinds == {'DESCRIPTION': 10, 'TEXT': 2, 'VALUE': 1}, dict(kinds))
ck('sei contesti', len(grp) == 6, dict(grp))
ck("33 unita' prima della 716 (12 + 21)",
   db.execute('select count(*) from units where path=? and line<716', (PATH,)).fetchone()[0] == 33)
ck("ZERO unita' dopo la 969: il lotto CHIUDE il file",
   db.execute('select count(*) from units where path=? and line>969', (PATH,)).fetchone()[0] == 0)
righe, lotti = set(), []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    us = [u for u in json.load(open(f, encoding='utf-8'))['units'] if u['path'] == PATH]
    if us:
        lotti.append((os.path.basename(os.path.dirname(f)), len(us)))
        righe |= {u['line'] for u in us}
ck('FILE: i tre lotti sommano 46 unita (12 + 21 + 13)',
   [n for _, n in lotti] == [12, 21, 13] and sum(n for _, n in lotti) == 46 == len(righe), (lotti, len(righe)))
ck('FILE: 46 unita, 46 righe distinte, prima 25, ultima 969',
   len(righe) == 46 and min(righe) == 25 and max(righe) == 969
   and db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (46, 25, 969))
ck('FILE: copertura 46/46 (100%)',
   len(righe) == db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0], '%d/46' % len(righe))
overlap = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    if os.path.basename(os.path.dirname(f)) == os.path.basename(HERE):
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH and 716 <= u['line'] <= 969:
            overlap.append((os.path.basename(os.path.dirname(f)), u['line']))
ck('nessun altro lotto rivendica le righe 716-969', not overlap, overlap)
ck('tutte e 13 le unita sono tradotte o copiate coerentemente',
   all((u['italian'] != u['english']) if u['kind'] == 'DESCRIPTION' else (u['italian'] == u['english'])
       for u in tu))
ck('TERZINE con tab sulla seconda e terza',
   all([u['line'] for u in tu if u['context'] == c and u['kind'] == 'DESCRIPTION'] == ls
       for c, ls in TERZINE.items())
   and all(at[l]['english'].startswith(TAB) and at[l]['italian'].startswith(TAB)
           for ls in TERZINE.values() for l in ls[1:]))
ck('TAB: sei in tutto, righe dichiarate', sorted(u['line'] for u in tu if u['english'].startswith(TAB)) == TABBED
   and sum(u['italian'].count(TAB) for u in tu) == 6)
ck('COPPIE con tab sulla seconda e contesto `(root)` per la 788',
   all(at[b]['context'] == at[a]['context'] for a, b in COPPIE) and by[4]['context'] == '(root)')
ck('TEXT/VALUE copiati verbatim; 4 virgolette in 2 coppie',
   all(by[i]['italian'] == by[i]['english'] for i in TEXT_IDX + VALUE_IDX)
   and sum(u['italian'].count(QUOTE) for u in tu) == 4)
ck('«ammunition for» in tre varianti con contenitori diversi',
   all(('è munizione per il' in by[i]['italian']) or ('è munizione per l\'' in by[i]['italian']) for i in AMMO3)
   and 'Vertical Launch Array' in by[2]['italian'] and 'External Launch Tube' in by[7]['italian']
   and 'External Launch Rail' in by[10]['italian'])
ck('la nota munizioni di L307/L308 NON compare qui',
   'si possono rifornire in qualsiasi emporio' not in ''.join(u['italian'] for u in tu))
ck('seconda persona solo negli avvisi (2, 7, 10)',
   [u['idx'] for u in tu if re.search(r'\b(tu|tuo|tua|tuoi|tue|ti|te|puoi)\b', u['italian'])] == AMMO3)
ck('ASSERZIONI VUOTE: 0 segnaposto, 0 alternative',
   sum(len(TAG.findall(u['italian'])) for u in tu) == 0
   and sum(len(ALT.findall(u['italian'])) for u in tu) == 0)
ck('apici: 3 in inglese, 17 in italiano',
   sum(u['english'].count(APOS) for u in tu) == 3 and sum(u['italian'].count(APOS) for u in tu) == 17,
   (sum(u['english'].count(APOS) for u in tu), sum(u['italian'].count(APOS) for u in tu)))
ck('lessico: barre di tungsteno, ottazacubano, corazzatura ablativa, nave da guerra capitale',
   'barre di tungsteno' in at[716]['italian'] and 'ottazacubano' in at[716]['italian']
   and 'corazzatura ablativa' in at[949]['italian'] and 'nave da guerra capitale' in at[949]['italian'])
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in tu for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessun doppio spazio (la tab iniziale non conta)',
   not [u['idx'] for u in tu if '  ' in u['italian'].lstrip(TAB)])
ck('rapporto nel gate 0,55-1,90',
   all(0.55 < u['ratio'] < 1.90 for u in tu),
   [(u['idx'], u['ratio']) for u in tu if not 0.55 < u['ratio'] < 1.90])
ck('tutte le 13 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in tu))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('FILE: 46/46 (100%) · somma lotti 12+21+13 · prima riga 25 · ultima 969 · zero dopo')
print('parole EN %d -> IT %d · ratio %.2f - %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(u['ratio'] for u in tu), max(u['ratio'] for u in tu)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L309 superato' if not fail else 'verify L309 fallito')
raise SystemExit(0 if not fail else 1)
