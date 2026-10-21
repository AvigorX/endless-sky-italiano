r"""verify.py — L237 (`data/avgi/avgi news.txt`, 14 unita', righe 369-399). Quinto lotto del file.

**Invariante di SEGMENTO**: il lotto non chiude il file (115 unita'). **80** prima (L233–L236), **14** qui, **21** dopo la
399. La copertura si **stampa** (94/115, 81,7%) e non si asserisce come elenco di lotti: il controllo raccoglie le righe
di questo segmento e pretende che **nessun altro** `translation.json` le rivendichi.

Verifica tre cose che il `check.py` non puo' verificare da solo:
il **refuso** `Frustation` letto dal sorgente e non replicato, la **normalizzazione** di `Twilight nebula` -> `Twilight
Nebula` (con la divergenza IT 3 / EN 2 asserita), e gli **otto apici** dell'unita' 398.

Indipendente da `check.py`: rilegge `source.json`, il `translation.json`, il database e il sorgente del gioco.
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
LABEL = re.compile(r'^"([A-Za-zÀ-ÿ]+)\. ')
HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
ROOT = os.path.abspath(os.path.join(L10N, '..'))
PATH = 'data/avgi/avgi news.txt'
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


ck('riga grezza identica al sorgente (14/14)', not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck('unita: 14 righe 369 - 399', len(tu) == 14 and (tu[0]['line'], tu[-1]['line']) == (369, 399))
ck("80 unita' prima della 369 (L233-L236)",
   db.execute('select count(*) from units where path=? and line<369', (PATH,)).fetchone()[0] == 80)
ck("21 unita' dopo la 399: il lotto NON chiude il file",
   db.execute('select count(*) from units where path=? and line>399', (PATH,)).fetchone()[0] == 21)
nxt = db.execute('select line,kind,context from units where path=? and line>399 order by line limit 1', (PATH,)).fetchone()
ck('confine misurato: riga 418, NEWS di news:avgi engineer',
   nxt == (418, 'NEWS', 'news:avgi engineer'), nxt)
ck('il file intero: 115 unita, righe 32 - 507',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (115, 32, 507))
per, lines = [], []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    d = json.load(open(f, encoding='utf-8'))
    us = [u for u in d['units'] if u['path'] == PATH]
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
ck("nessun ALTRO lotto rivendica le righe di questo segmento (invariante di segmento: 14 righe distinte)",
   not overlap and len(mine) == 14, (overlap, len(mine)))
ck('tipi del lotto: 14 NEWS', collections.Counter(u['kind'] for u in su) == {'NEWS': 14})
ck("ZERO unita identiche all'inglese, 14 tradotte",
   sum(1 for u in tu if u['italian'] == u['english']) == 0
   and sum(1 for u in tu if u['italian'] != u['english']) == 14)
ck("28 virgolette, 2 per unita', nessun tab",
   sum(u['english'].count(QUOTE) for u in su) == 28 == sum(u['italian'].count(QUOTE) for u in tu)
   and all(u['italian'].count(QUOTE) == 2 for u in tu)
   and sum(u['english'].count(TAB) for u in su) == 0 == sum(u['italian'].count(TAB) for u in tu))
ck("ogni unita' e' una citazione intera: comincia e finisce con le virgolette",
   all(u['italian'].startswith('"') and u['italian'].endswith('"') for u in tu))
ck('0 segnaposto', sum(len(TAG.findall(u['english'])) for u in su) == 0
   == sum(len(TAG.findall(u['italian'])) for u in tu))
ck("etichette tradotte nelle stesse posizioni (14 su 14)",
   [LABEL.match(u['italian']).group(1) if LABEL.match(u['italian']) else None for u in tu]
   == ['Gratitudine', 'Frustrazione', 'Frustrazione', 'Orgoglio', 'Divertimento', 'Curiosità', 'Informazione',
       'Stupore', 'Istruttivo', 'Curioso', 'Insegnamento', 'Frustrazione', 'Fastidio', 'Curiosità'])
ck("il refuso `Frustation` sta nel SORGENTE due volte (370, 371), non nella traduzione",
   [LABEL.match(u['english']).group(1) for u in su].count('Frustation') == 2
   and [LABEL.match(u['english']).group(1) for u in su].count('Frustration') == 1
   and 'Frustation' not in ' '.join(u['italian'] for u in tu)
   and ' '.join(u['italian'] for u in tu).count('Frustrazione') == 3)
ck("`Twilight nebula` (minuscolo) nel sorgente e' normalizzato a `Twilight Nebula`: IT 3, EN 2, divergenza dichiarata",
   'Twilight nebula' in ' '.join(u['english'] for u in su)
   and 'Twilight nebula' not in ' '.join(u['italian'] for u in tu)
   and ' '.join(u['italian'] for u in tu).count('Twilight Nebula') == 3)
ck("gli otto apici dell'unita' 398 sono quattro virgolette semplici, riprodotte",
   by[13]['english'].count(APOS) == 8 == by[13]['italian'].count(APOS)
   and by[13]['italian'].count("'") == 8)
ck('PENDING su tutte e 14', not [u['idx'] for u in su
                                 if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('nessun carattere tipografico e nessun non latino',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')
        or any(ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F for c in u['italian'])])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate 0,55-1,90 (0,94 - 1,21; 356 -> 354 parole)',
   0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('SEGMENTO: 94/115 unita\' del file (%.1f%%) · 80 prima · 14 qui · 21 dopo · confine riga 418'
      % (100.0 * len(lines) / 115))
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L237 superato' if not fail else 'verify L237 fallito')
raise SystemExit(0 if not fail else 1)
