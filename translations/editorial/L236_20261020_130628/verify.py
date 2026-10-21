r"""verify.py — L236 (`data/avgi/avgi news.txt`, 23 unita', righe 301-344). Quarto lotto del file.

**Invariante di SEGMENTO**: il lotto non chiude il file (115 unita'). **57** prima (L233 22 + L234 20 + L235 15),
**23** qui, **35** dopo la 344. La copertura si **stampa** (80/115, 69,6%), non si asserisce; e soprattutto **non** si
asserisce come elenco di lotti: il controllo raccoglie le righe di questo segmento e pretende che **nessun altro**
`translation.json` le rivendichi (lezione pagata in L233/L234).

Le relazioni del lotto sono verificate come relazioni: le tre coppie di inglese identico (10/20, 12/22, 13/23) devono
avere la stessa resa, la coppia 11/21 deve differire **solo** nell'etichetta in coda, e le sei unita' 1-6 devono
condividere la stessa formula cambiando la sola disciplina.

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
TAG = re.compile(r'<[^<>]+>')
LABEL = re.compile(r'^"([A-Za-zÀ-ÿ]+)\. ')
HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
ROOT = os.path.abspath(os.path.join(L10N, '..'))
PATH = 'data/avgi/avgi news.txt'
DUP_PAIRS = [(10, 20), (12, 22), (13, 23)]
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


ck('riga grezza identica al sorgente (23/23)', not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck('unita: 23 righe 301 - 344', len(tu) == 23 and (tu[0]['line'], tu[-1]['line']) == (301, 344))
ck("57 unita' prima della 301 (L233 22 + L234 20 + L235 15)",
   db.execute('select count(*) from units where path=? and line<301', (PATH,)).fetchone()[0] == 57)
ck("35 unita' dopo la 344: il lotto NON chiude il file",
   db.execute('select count(*) from units where path=? and line>344', (PATH,)).fetchone()[0] == 35)
nxt = db.execute('select line,kind,context from units where path=? and line>344 order by line limit 1', (PATH,)).fetchone()
ck('confine misurato: riga 369, NEWS di news:avgi physicist',
   nxt == (369, 'NEWS', 'news:avgi physicist'), nxt)
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
ck("nessun ALTRO lotto rivendica le righe di questo segmento (invariante di segmento: 23 righe distinte)",
   not overlap and len(mine) == 23, (overlap, len(mine)))
ck('tipi del lotto: 23 NEWS', collections.Counter(u['kind'] for u in su) == {'NEWS': 23})
ck("ZERO unita identiche all'inglese, 23 tradotte",
   sum(1 for u in tu if u['italian'] == u['english']) == 0
   and sum(1 for u in tu if u['italian'] != u['english']) == 23)
ck("46 virgolette, 2 per unita', nessun tab",
   sum(u['english'].count(QUOTE) for u in su) == 46 == sum(u['italian'].count(QUOTE) for u in tu)
   and all(u['italian'].count(QUOTE) == 2 for u in tu)
   and sum(u['english'].count(TAB) for u in su) == 0 == sum(u['italian'].count(TAB) for u in tu))
ck("ogni unita' e' una citazione intera: comincia e finisce con le virgolette",
   all(u['italian'].startswith('"') and u['italian'].endswith('"') for u in tu))
ck('0 segnaposto', sum(len(TAG.findall(u['english'])) for u in su) == 0
   == sum(len(TAG.findall(u['italian'])) for u in tu))
ck("19 etichette in testa (tradotte) e 4 None nelle stesse posizioni (10, 11, 20, 21)",
   [LABEL.match(u['italian']).group(1) if LABEL.match(u['italian']) else None for u in tu]
   == ['Felicità', 'Felicità', 'Felicità', 'Felicità', 'Felicità', 'Felicità', 'Entusiasmo', 'Gratitudine',
       'Gioia', None, None, 'Fastidio', 'Fastidio', 'Frustrazione', 'Abbattimento', 'Rabbia', 'Rabbia',
       'Preoccupazione', 'Preoccupazione', None, None, 'Fastidio', 'Fastidio']
   and [LABEL.match(u['english']).group(1) if LABEL.match(u['english']) else None for u in su]
   == ['Happiness', 'Happiness', 'Happiness', 'Happiness', 'Happiness', 'Happiness', 'Enthusiasm', 'Gratitude',
       'Joy', None, None, 'Annoyance', 'Annoyance', 'Frustration', 'Depression', 'Anger', 'Anger', 'Worry',
       'Worry', None, None, 'Annoyance', 'Annoyance'],
   [LABEL.match(u['italian']).group(1) if LABEL.match(u['italian']) else None for u in tu])
ck("le tre coppie di inglese identico hanno la stessa resa (10/20, 12/22, 13/23)",
   all(by[a]['english'] == by[b]['english'] and by[a]['italian'] == by[b]['italian'] for a, b in DUP_PAIRS))
ck("la coppia 11/21 differisce SOLO nell'etichetta in coda (`divertimento.` / `scoramento.`)",
   by[11]['italian'].rsplit(' ', 1)[0] == by[21]['italian'].rsplit(' ', 1)[0]
   and by[11]['italian'] != by[21]['italian']
   and by[11]['english'].rsplit(' ', 1)[0] == by[21]['english'].rsplit(' ', 1)[0])
ck("le sei unita' 1-6 condividono la formula e cambiano solo la disciplina",
   len({re.sub(r'(fisica|economia|ingegneria|nanotecnologia|genetica|aerodinamica)', 'X', u['italian'])
        for u in tu[:6]}) == 1)
ck('PENDING su tutte e 23', not [u['idx'] for u in su
                                 if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('nessun carattere tipografico e nessun non latino',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')
        or any(ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F for c in u['italian'])])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate 0,55-1,90 (0,88 - 1,58; 348 -> 320 parole)',
   0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('SEGMENTO: 80/115 unita\' del file (%.1f%%) · 57 prima · 23 qui · 35 dopo · confine riga 369'
      % (100.0 * len(lines) / 115))
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L236 superato' if not fail else 'verify L236 fallito')
raise SystemExit(0 if not fail else 1)
