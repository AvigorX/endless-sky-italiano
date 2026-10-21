r"""verify.py — L239 (`data/avgi/avgi jobs.txt`, 62 unita', righe 20-656). Primo lotto del file.

**Invariante di SEGMENTO** (il file NON e' chiuso: 102 unita'): **0** prima della 20 (e' la prima riga del file), **62**
qui, **40** dopo la 656, confine misurato alla **684** (`mission:Avgi: Doctors 1`). La copertura si **stampa**
(62/102, 60,8%) e non si asserisce come elenco di lotti: il controllo raccoglie le righe di questo segmento e pretende che
**nessun altro** `translation.json` le rivendichi.

Verifica quello che il `check.py` non puo' verificare da solo: la **parita' dei segnaposto per simbolo e nell'ordine**,
il fatto che i `VALUE` siano copiati **dal sorgente** e non riscritti, e la coerenza cross-lot della stringa piu'
frequente del file.

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
TAG = re.compile(r'<[^<>]+>')
HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
ROOT = os.path.abspath(os.path.join(L10N, '..'))
PATH = 'data/avgi/avgi jobs.txt'
src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
su = sorted(src['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
by = {u['idx']: u for u in tu}
raw_lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
fail = []


def ck(n, c, d=''):
    print('%-78s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente (62/62)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck("unita: 62, righe 20 - 656", len(tu) == 62 and (tu[0]['line'], tu[-1]['line']) == (20, 656))
ck('31 VALUE + 31 DESCRIPTION', collections.Counter(u['kind'] for u in su) == {'VALUE': 31, 'DESCRIPTION': 31})
ck("ZERO unita' prima della 20: e' la prima riga del file",
   db.execute('select count(*) from units where path=? and line<20', (PATH,)).fetchone()[0] == 0)
ck("40 unita' dopo la 656: il lotto NON chiude il file",
   db.execute('select count(*) from units where path=? and line>656', (PATH,)).fetchone()[0] == 40)
nxt = db.execute('select line,kind,context from units where path=? and line>656 order by line limit 1', (PATH,)).fetchone()
ck('confine misurato: riga 684, VALUE di mission:Avgi: Doctors 1',
   nxt == (684, 'VALUE', 'mission:Avgi: Doctors 1'), nxt)
ck('il file intero: 102 unita, righe 20 - 1156',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (102, 20, 1156))
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
ck("nessun ALTRO lotto rivendica le righe di questo segmento (invariante di segmento: 62 righe distinte)",
   not overlap and len(mine) == 62, (overlap, len(mine)))
VAL = [u for u in tu if u['kind'] == 'VALUE']
DES = [u for u in tu if u['kind'] == 'DESCRIPTION']
ck("i 31 VALUE sono copiati dal sorgente, carattere per carattere",
   all(u['italian'] == u['english'] for u in VAL), [u['idx'] for u in VAL if u['italian'] != u['english']])
ck("le 31 DESCRIPTION sono tutte tradotte", all(u['italian'] != u['english'] for u in DES))
ck('nessun tab, nessuna virgoletta in tutto il lotto',
   sum(u['english'].count(TAB) for u in su) == 0 == sum(u['italian'].count(TAB) for u in tu)
   and sum(u['english'].count(QUOTE) for u in su) == 0 == sum(u['italian'].count(QUOTE) for u in tu))
tok_en = collections.Counter(t for u in su for t in TAG.findall(u['english']))
tok_it = collections.Counter(t for u in tu for t in TAG.findall(u['italian']))
ck('segnaposto: 133 su 6 simboli, parita\' per simbolo',
   tok_en == tok_it == {'<planet>': 31, '<destination>': 31, '<payment>': 31, '<cargo>': 24,
                        '<date>': 9, '<bunks>': 7}, (dict(tok_en), dict(tok_it)))
ck("segnaposto: ordine identico in ogni unita' (due simboli hanno lo stesso conteggio: 31 e 31)",
   all(tuple(TAG.findall(u['english'])) == tuple(TAG.findall(u['italian'])) for u in tu),
   [(u['idx'], TAG.findall(u['english']), TAG.findall(u['italian'])) for u in tu
    if TAG.findall(u['english']) != TAG.findall(u['italian'])])
ck("nessuna unita' con segnaposto solo in una lingua",
   [u['idx'] for u in tu if bool(TAG.findall(u['english'])) != bool(TAG.findall(u['italian']))] == [])
fam = collections.Counter(u['english'] for u in DES)
ck('6 famiglie di DESCRIPTION (15 · 9 · 2 · 2 · 1 · 2)',
   sorted(fam.values()) == [1, 2, 2, 2, 9, 15], dict(fam))
ck('una sola resa per famiglia',
   all(len({u['italian'] for u in DES if u['english'] == k}) == 1 for k in fam))
gold = 'Consegna <cargo> su <destination>. Il pagamento è <payment>.'
prev = set()
for f in glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json')):
    if os.path.dirname(f) == HERE:
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['english'] == 'Deliver <cargo> to <destination>. Payment is <payment>.':
            prev.add(u['italian'])
ck('coerenza cross-lot: la resa della stringa piu\' frequente (15x) e\' gia\' nel corpus',
   gold in prev and gold in {u['italian'] for u in DES}, len(prev))
ck("PENDING su tutte e 62", not [u['idx'] for u in su
                                 if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0]
                                 != 'PENDING'])
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('nessun carattere tipografico e nessun non latino',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')
        or any(ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F for c in u['italian'])])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate 0,55-1,90 (0,97 - 1,22; 432 -> 483 parole)',
   0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('SEGMENTO: %d/%d unita\' del file (%.1f%%) · 0 prima · 62 qui · 40 dopo · confine riga 684'
      % (len(lines), 102, 100.0 * len(lines) / 102))
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L239 superato' if not fail else 'verify L239 fallito')
raise SystemExit(0 if not fail else 1)
