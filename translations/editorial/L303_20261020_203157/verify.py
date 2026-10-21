r"""verify.py — L303 (`data/remnant/remnant ships.txt`, righe 1378-1826). **LOTTO TERMINALE**.

Verifica da sola, e verifica il **FILE INTERO**: 38 unita', **somma dei lotti 12 + 12 + 14 = 38**, **righe distinte**, **prima riga
17**, **ultima 1826**, **zero unita' dopo**. Poi il lotto: riga grezza, campi del DB, **tre terzine**, **due coppie**, la
**ripetizione 1380/1490**, la **variante droni 1826**, la **famiglia dell'occultamento a cinque** (riapre L301 e L302), e la
**seconda persona** nei soli avvisi di gioco.

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
L301 = os.path.join(L10N, 'staging', 'editorial', 'L301_20261020_202040', 'translation.json')
L302 = os.path.join(L10N, 'staging', 'editorial', 'L302_20261020_202611', 'translation.json')
PATH = 'data/remnant/remnant ships.txt'
TERZINE = {'ship:Petrel': [1378, 1379, 1380], 'ship:Smew': [1488, 1489, 1490], 'ship:Tern': [1824, 1825, 1826]}
COPPIE = [(1594, 1595), (1766, 1767)]
TABBED = [1379, 1380, 1489, 1490, 1595, 1767, 1825, 1826]
TU = [3, 7, 14]
AVVISO_CACCIA = ('\tI caccia non sono dotati di iperguida. Non puoi trasportare un caccia a meno che tu non abbia '
                 'nella tua flotta una nave con una baia di caccia.')
AVVISO_DRONI = ('\tI droni non sono dotati di iperguida. Non puoi trasportare un drone a meno che tu non abbia '
                'nella tua flotta una nave con una baia per droni.')
src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
su = sorted(src['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
raw_lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
by = {u['idx']: u for u in tu}
at = {u['line']: u for u in tu}
prev = {u['line']: u for u in json.load(open(L301, encoding='utf-8'))['units']}
prev2 = {u['line']: u for u in json.load(open(L302, encoding='utf-8'))['units']}
fail = []


def ck(n, c, d=''):
    print('%-96s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente (14/14)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = [u['idx'] for u in su
       if db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
       != (u['english'], u['kind'], u['path'], u['context'])]
ck('english/kind/path/context identici al DB', not bad, bad)
grp = collections.Counter(u['context'] for u in tu)
ck('14 unita DESCRIPTION, sei contesti (3 terzine + 2 coppie + 1 singola)',
   len(tu) == 14 and {u['kind'] for u in tu} == {'DESCRIPTION'}
   and sorted(grp.values()) == [1, 2, 2, 3, 3, 3], dict(grp))
ck("24 unita' prima della 1378 (12 + 12)",
   db.execute('select count(*) from units where path=? and line<1378', (PATH,)).fetchone()[0] == 24)
ck("ZERO unita' dopo la 1826: il lotto CHIUDE il file",
   db.execute('select count(*) from units where path=? and line>1826', (PATH,)).fetchone()[0] == 0)
righe, lotti = set(), []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    us = [u for u in json.load(open(f, encoding='utf-8'))['units'] if u['path'] == PATH]
    if us:
        lotti.append((os.path.basename(os.path.dirname(f)), len(us)))
        righe |= {u['line'] for u in us}
ck('FILE: i tre lotti sommano 38 unita (12 + 12 + 14)',
   [n for _, n in lotti] == [12, 12, 14] and sum(n for _, n in lotti) == 38 == len(righe), (lotti, len(righe)))
ck('FILE: 38 unita, 38 righe distinte, prima 17, ultima 1826',
   len(righe) == 38 and min(righe) == 17 and max(righe) == 1826
   and db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (38, 17, 1826))
ck('FILE: copertura 38/38 (100%)',
   len(righe) == db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0], '%d/38' % len(righe))
overlap = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    if os.path.basename(os.path.dirname(f)) == os.path.basename(HERE):
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH and 1378 <= u['line'] <= 1826:
            overlap.append((os.path.basename(os.path.dirname(f)), u['line']))
ck('nessun altro lotto rivendica le righe 1378-1826', not overlap, overlap)
ck('tutte e 14 le unita sono tradotte', all(u['italian'] != u['english'] for u in tu))
ck('TERZINE: tre gruppi, tab sulla seconda e sulla terza',
   all([u['line'] for u in tu if u['context'] == c] == ls for c, ls in TERZINE.items())
   and all(at[l]['english'].startswith(TAB) and at[l]['italian'].startswith(TAB)
           for ls in TERZINE.values() for l in ls[1:]))
ck('TAB: otto in tutto, righe dichiarate',
   sorted(u['line'] for u in tu if u['english'].startswith(TAB)) == TABBED
   and sum(u['italian'].count(TAB) for u in tu) == 8)
ck('COPPIE con tab sulla seconda', all(at[b]['context'] == at[a]['context'] for a, b in COPPIE))
ck('RIPETIZIONE: 1380 e 1490 identiche in inglese e in italiano',
   at[1380]['english'] == at[1490]['english'] and at[1380]['italian'] == at[1490]['italian'])
ck('avvisi nella forma del corpus (baia di caccia / baia per droni)',
   at[1380]['italian'] == AVVISO_CACCIA and at[1826]['italian'] == AVVISO_DRONI)
ck('variante droni: stesso avviso a parte il sostantivo e il nome della baia',
   AVVISO_CACCIA.rsplit('una nave con una', 1)[0].replace('caccia', 'droni').replace('un droni', 'un drone')
   == AVVISO_DRONI.rsplit('una nave con una', 1)[0])
ck('FAMIGLIA occultamento: 1595 identica a `Gull` (L301) e alle tre di L302, a meno del nome',
   at[1595]['italian'].replace('Starling', 'X') == prev[549]['italian'].replace('Gull', 'X')
   and all(at[1595]['italian'].replace('Starling', 'X') == prev2[l]['italian'].replace(n, 'X')
           for l, n in {982: 'Merganser', 1202: 'Penguin', 1291: 'Peregrine'}.items()))
ck('seconda persona solo negli avvisi di gioco (unita 3, 7, 14)',
   [u['idx'] for u in tu if re.search(r'\b(tu|tuo|tua|tuoi|tue|ti|te)\b', u['italian'])] == TU)
ck('ASSERZIONI VUOTE: 0 virgolette, 0 segnaposto, 0 alternative',
   sum(u['english'].count(QUOTE) for u in tu) == 0 == sum(u['italian'].count(QUOTE) for u in tu)
   and sum(len(TAG.findall(u['italian'])) for u in tu) == 0
   and sum(len(ALT.findall(u['italian'])) for u in tu) == 0)
ck('tre punti ASCII, nessun carattere ellissi',
   '...' in at[1594]['italian'] and '\u2026' not in ''.join(u['italian'] for u in tu))
ck('apici: 3 in inglese, 12 in italiano',
   sum(u['english'].count(APOS) for u in tu) == 3 and sum(u['italian'].count(APOS) for u in tu) == 12,
   (sum(u['english'].count(APOS) for u in tu), sum(u['italian'].count(APOS) for u in tu)))
ck('lessico: ramscoop, baie per droni, navi di schermo, scialuppa di salvataggio',
   'ramscoop' in at[1766]['italian'] and 'baie per droni' in at[1767]['italian']
   and 'navi di schermo' in at[1824]['italian'] and 'scialuppa di salvataggio' in at[1489]['italian'])
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in tu for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessun doppio spazio (la tab iniziale non conta)',
   not [u['idx'] for u in tu if '  ' in u['italian'].lstrip(TAB)])
ck('rapporto nel gate 0,55-1,90',
   all(0.55 < u['ratio'] < 1.90 for u in tu),
   [(u['idx'], u['ratio']) for u in tu if not 0.55 < u['ratio'] < 1.90])
ck('tutte le 14 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in tu))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('FILE: 38/38 (100%) · somma lotti 12+12+14 · prima riga 17 · ultima 1826 · zero dopo')
print('parole EN %d -> IT %d · ratio %.2f - %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(u['ratio'] for u in tu), max(u['ratio'] for u in tu)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L303 superato' if not fail else 'verify L303 fallito')
raise SystemExit(0 if not fail else 1)
