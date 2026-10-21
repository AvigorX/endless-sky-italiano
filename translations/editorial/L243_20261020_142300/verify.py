r"""verify.py — L243 (`data/hai/hai ships.txt`, 29 unita', righe 15-332). Primo lotto del file.

**Invariante di SEGMENTO** (il file NON e' chiuso: 157 unita'): **0** prima della 15 (prima riga del file), **29** qui,
**128** dopo la 332, confine misurato alla **362** (`ship:Flea`). La copertura si **stampa** (29/157, 18,5%) e non si
asserisce come elenco di lotti: si pretende che **nessun altro** `translation.json` rivendichi queste righe.

Verifica da sola: i **24 dati** copiati (1 `VALUE` + 23 `TEXT`), le **5 descrizioni** tradotte, le **48 virgolette per
unita'** (2 per nome + 2 del motto), i **4 possessivi inglesi** che in italiano diventano elisioni, e che i **nomi propri**
restino inglesi anche dentro la prosa.

Indipendente da `check.py`: rilegge `source.json`, il `translation.json`, il database e il file del gioco.
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
HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
ROOT = os.path.abspath(os.path.join(L10N, '..'))
PATH = 'data/hai/hai ships.txt'
src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
su = sorted(src['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
by = {u['idx']: u for u in tu}
raw_lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
fail = []


def ck(n, c, d=''):
    print('%-80s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente (29/29)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck("unita: 29, righe 15 - 332", len(tu) == 29 and (tu[0]['line'], tu[-1]['line']) == (15, 332))
ck('1 VALUE + 23 TEXT + 5 DESCRIPTION',
   collections.Counter(u['kind'] for u in su) == {'VALUE': 1, 'TEXT': 23, 'DESCRIPTION': 5})
ck('4 contesti (Anomalocaris, Aphid, Centipede, Cicada)',
   set(u['context'] for u in su) == {'ship:Anomalocaris', 'ship:Aphid', 'ship:Centipede', 'ship:Cicada'})
ck("ZERO unita' prima della 15: e' la prima riga del file",
   db.execute('select count(*) from units where path=? and line<15', (PATH,)).fetchone()[0] == 0)
ck("128 unita' dopo la 332: il lotto NON chiude il file",
   db.execute('select count(*) from units where path=? and line>332', (PATH,)).fetchone()[0] == 128)
nxt = db.execute('select line,context from units where path=? and line>332 order by line limit 1', (PATH,)).fetchone()
ck('confine misurato: riga 362, ship:Flea', nxt == (362, 'ship:Flea'), nxt)
ck('il file intero: 157 unita, righe 15 - 1860',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (157, 15, 1860))
per, lines = [], []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    us = [u for u in json.load(open(f, encoding='utf-8'))['units'] if u['path'] == PATH]
    if us:
        per.append((os.path.basename(os.path.dirname(f)), len(us)))
        lines += [u['line'] for u in us]
mine = set(u['line'] for u in tu)
overlap = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    lot = os.path.basename(os.path.dirname(f))
    if lot == os.path.basename(HERE):
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH and u['line'] in mine:
            overlap.append((lot, u['line']))
ck("nessun ALTRO lotto rivendica le righe di questo segmento (29 righe distinte)",
   not overlap and len(mine) == 29, (overlap, len(mine)))
DATA = [u for u in tu if u['kind'] in ('VALUE', 'TEXT')]
DES = [u for u in tu if u['kind'] == 'DESCRIPTION']
ck("i 24 dati sono copiati dal sorgente carattere per carattere (virgolette comprese)",
   all(u['italian'] == u['english'] for u in DATA) and len(DATA) == 24,
   [u['idx'] for u in DATA if u['italian'] != u['english']])
ck("le 5 descrizioni sono tradotte", all(u['italian'] != u['english'] for u in DES) and len(DES) == 5)
ck('nessun tab e nessun segnaposto',
   sum(u['english'].count(TAB) for u in su) == 0 == sum(u['italian'].count(TAB) for u in tu)
   and sum(len(TAG.findall(u['english'])) for u in su) == 0 == sum(len(TAG.findall(u['italian'])) for u in tu))
q_it = [(u['idx'], u['italian'].count(QUOTE)) for u in tu if QUOTE in u['italian']]
ck("48 virgolette, 2 per unita', su 24 unita' (23 nomi + il motto della Cicada)",
   sum(n for _, n in q_it) == 48 and len(q_it) == 24 and set(n for _, n in q_it) == {2}, q_it[:4])
ck("il motto e' fra virgolette, col punto DENTRO: «\"Al servizio per tutta la vita.\"»",
   DES[-1]['italian'].endswith('"Al servizio per tutta la vita."'),
   DES[-1]['italian'][-45:])
a_en = [(u['idx'], u['english'].count(APOS)) for u in su if APOS in u['english']]
a_it = [(u['idx'], u['italian'].count(APOS)) for u in tu if APOS in u['italian']]
ck("4 possessivi inglesi (4, 7, 20, 29) e 19 apici italiani di elisione",
   a_en == [(4, 1), (7, 1), (20, 1), (29, 1)] and sum(n for _, n in a_it) == 19, (a_en, a_it))
ck("nessun possessivo inglese sopravvive nella prosa",
   not [s for s in ("'s ", "Hai's", "project's", "shipyard's") if s in ' '.join(u['italian'] for u in DES)])
prosa = ' '.join(u['italian'] for u in DES)
ck('nomi propri invariati e parole comuni tradotte, nella stessa prosa',
   all(n in prosa for n in ('Sheragi', 'Anomalocaris', 'Aphid', 'Centipede', 'Cicada', 'Scarab', 'Yeer e Ki'))
   and all(t in prosa for t in ('navi da guerra', 'mercantile', 'spina dorsale', 'ghiande in salamoia')))
ck('la seconda scheda dell\'Anomalocaris non e\' una copia della prima: differisce solo nella coda',
   len({u['italian'] for u in DES if u['context'] == 'ship:Anomalocaris'}) == 2
   and DES[0]['italian'][:120] == DES[1]['italian'][:120]
   and DES[0]['italian'].endswith('danni maggiori.') and 'sott\'acqua' in DES[1]['italian'])
ck("PENDING su tutte e 29", not [u['idx'] for u in su
                                 if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0]
                                 != 'PENDING'])
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('nessun carattere tipografico e nessun non latino',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')
        or any(ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F for c in u['italian'])])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate 0,55-1,90 (1,00 - 1,09; 451 -> 456 parole)',
   0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print("SEGMENTO: %d/%d unita' del file (%.1f%%) · 0 prima · 29 qui · 128 dopo · confine riga 362"
      % (len(lines), 157, 100.0 * len(lines) / 157))
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L243 superato' if not fail else 'verify L243 fallito')
raise SystemExit(0 if not fail else 1)
