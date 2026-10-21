r"""verify.py — L306 (`data/quarg/quarg outfits.txt`, righe 257-579). **LOTTO TERMINALE**.

Verifica da sola, e verifica il **FILE INTERO**: 31 unita', **somma dei lotti 11 + 10 + 10 = 31**, **righe distinte**, **prima riga
37**, **ultima 579**, **zero unita' dopo**. Poi il lotto: riga grezza, campi del DB, **dieci contesti singoli**, **zero tab**, i
**nomi invariati** e le **traduzioni tentatrici assenti**, e che **nessun altro lotto** rivendichi le righe 257-579.

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
PATH = 'data/quarg/quarg outfits.txt'
ARMI = ['Skydagger', 'Skylance', 'Stratospear', 'Elysian Ranseur', 'Celestial Culverin', 'Astral Ribault',
        'Slipstream Projector', 'Phalanx System']
HUB = ['Peripheral Repair Hub', 'Central Repair Hub']
VIETATI = ['Pugnale del cielo', 'Lancia delle stelle', 'Falange', 'Proiettore della scia',
           'Culverina celeste', 'Ribault astrale']
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
grp = collections.Counter(u['context'] for u in tu)
ck('10 unita DESCRIPTION, dieci contesti da una unita ciascuno',
   len(tu) == 10 and {u['kind'] for u in tu} == {'DESCRIPTION'}
   and len(grp) == 10 and set(grp.values()) == {1}, dict(grp))
ck("21 unita' prima della 257 (11 + 10)",
   db.execute('select count(*) from units where path=? and line<257', (PATH,)).fetchone()[0] == 21)
ck("ZERO unita' dopo la 579: il lotto CHIUDE il file",
   db.execute('select count(*) from units where path=? and line>579', (PATH,)).fetchone()[0] == 0)
righe, lotti = set(), []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    us = [u for u in json.load(open(f, encoding='utf-8'))['units'] if u['path'] == PATH]
    if us:
        lotti.append((os.path.basename(os.path.dirname(f)), len(us)))
        righe |= {u['line'] for u in us}
ck('FILE: i tre lotti sommano 31 unita (11 + 10 + 10)',
   [n for _, n in lotti] == [11, 10, 10] and sum(n for _, n in lotti) == 31 == len(righe), (lotti, len(righe)))
ck('FILE: 31 unita, 31 righe distinte, prima 37, ultima 579',
   len(righe) == 31 and min(righe) == 37 and max(righe) == 579
   and db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (31, 37, 579))
ck('FILE: copertura 31/31 (100%)',
   len(righe) == db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0], '%d/31' % len(righe))
overlap = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    if os.path.basename(os.path.dirname(f)) == os.path.basename(HERE):
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH and 257 <= u['line'] <= 579:
            overlap.append((os.path.basename(os.path.dirname(f)), u['line']))
ck('nessun altro lotto rivendica le righe 257-579', not overlap, overlap)
ck('tutte e 10 le unita sono tradotte', all(u['italian'] != u['english'] for u in tu))
ck('ASSERZIONI VUOTE: nessuna coppia, nessuna tab, 0 virgolette, 0 segnaposto, 0 alternative',
   set(grp.values()) == {1}
   and sum(u['english'].count(TAB) for u in tu) == 0 == sum(u['italian'].count(TAB) for u in tu)
   and sum(u['english'].count(QUOTE) for u in tu) == 0 == sum(u['italian'].count(QUOTE) for u in tu)
   and sum(len(TAG.findall(u['italian'])) for u in tu) == 0
   and sum(len(ALT.findall(u['italian'])) for u in tu) == 0)
ck('i dieci contesti sono i due hub e le otto armi',
   {u['context'].split(':', 1)[1] for u in tu} == set(HUB + ARMI))
ck('nessuna traduzione tentatrice dei nomi compare nel testo',
   not [v for v in VIETATI if v.lower() in ''.join(u['italian'] for u in tu).lower()],
   [v for v in VIETATI if v.lower() in ''.join(u['italian'] for u in tu).lower()])
ck('l unica arma nominata in prosa (`Skylance`) resta invariata ed e solo alla 336',
   'Skylance' in at[336]['italian']
   and 'Skylance' not in ''.join(u['italian'] for u in tu if u['line'] != 336))
ck('il trattino ` - ` dell unita 1 e conservato',
   ' - durabilità, longevità e' in at[257]['italian'])
ck('apici: 5 in inglese, 10 in italiano',
   sum(u['english'].count(APOS) for u in tu) == 5 and sum(u['italian'].count(APOS) for u in tu) == 10,
   (sum(u['english'].count(APOS) for u in tu), sum(u['italian'].count(APOS) for u in tu)))
ck('lessico: spaziotempo, energia negativa, mondi ad anello, antimissile, abbordaggi',
   'spaziotempo' in at[402]['italian'] and 'energia negativa' in at[496]['italian']
   and 'mondi ad anello' in at[566]['italian'] and 'antimissile' in at[366]['italian']
   and 'abbordaggi' in at[579]['italian'])
ck('registro: nessuna seconda persona',
   not [u['idx'] for u in tu if re.search(r'\b(tu|tuo|tua|tuoi|tue|ti|te)\b', u['italian'])])
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in tu for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessun doppio spazio', not [u['idx'] for u in tu if '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90',
   all(0.55 < u['ratio'] < 1.90 for u in tu),
   [(u['idx'], u['ratio']) for u in tu if not 0.55 < u['ratio'] < 1.90])
ck('tutte le 10 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in tu))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('FILE: 31/31 (100%) · somma lotti 11+10+10 · prima riga 37 · ultima 579 · zero dopo')
print('parole EN %d -> IT %d · ratio %.2f - %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(u['ratio'] for u in tu), max(u['ratio'] for u in tu)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L306 superato' if not fail else 'verify L306 fallito')
raise SystemExit(0 if not fail else 1)
