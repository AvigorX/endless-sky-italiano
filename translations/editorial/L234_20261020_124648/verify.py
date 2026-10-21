r"""verify.py — L234 (`data/avgi/avgi news.txt`, 20 unita', righe 115-180). Secondo lotto del file.

**Invariante di SEGMENTO**: il lotto non chiude il file (115 unita'). **22** prima della 115 (L233), **20** qui,
**73** dopo la 180. La copertura si **stampa** (42/115, 36,5%), non si asserisce: si asserisce solo nel lotto che chiude
il file (decisione 85).

**Il confine e' anche il documento di una trappola**: la prima unita' dopo la 180 e' la **197**, e il suo inglese e' il
frammento di una parola `"Caution. ` — una citazione che si apre e **non** e' una citazione, perche' il gioco la
concatena con i messaggi delle righe 204-210. Il controllo lo asserisce qui, cosi' chi apre L235 trova la premessa
scritta invece di scoprirla a proprie spese.

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
su = sorted(json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
raw_lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
fail = []


def ck(n, c, d=''):
    print('%-78s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente (20/20)', not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck('unita: 20 righe 115 - 180', len(tu) == 20 and (tu[0]['line'], tu[-1]['line']) == (115, 180))
ck("22 unita' prima della 115 (L233: 32-91)",
   db.execute('select count(*) from units where path=? and line<115', (PATH,)).fetchone()[0] == 22)
ck("73 unita' dopo la 180: il lotto NON chiude il file",
   db.execute('select count(*) from units where path=? and line>180', (PATH,)).fetchone()[0] == 73)
nxt = db.execute('select line,kind,context,english from units where path=? and line>180 order by line limit 1',
                 (PATH,)).fetchone()
ck('confine misurato: riga 197, NEWS di news:avgi safety advisory',
   nxt[:3] == (197, 'NEWS', 'news:avgi safety advisory'), nxt[:3])
ck("il confine e' un FRAMMENTO, non una citazione: l'inglese e' `\"Caution. ` (una parola, virgoletta aperta)",
   nxt[3] == '"Caution. ' and len(nxt[3].split()) == 1, repr(nxt[3]))
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
ck("nessun ALTRO lotto rivendica le righe di questo segmento (invariante di segmento: 20 righe distinte)",
   not overlap and len(mine) == 20, (overlap, len(mine)))
ck('tipi del lotto: 20 NEWS', collections.Counter(u['kind'] for u in su) == {'NEWS': 20})
ck("ZERO unita identiche all'inglese, 20 tradotte",
   sum(1 for u in tu if u['italian'] == u['english']) == 0
   and sum(1 for u in tu if u['italian'] != u['english']) == 20)
ck('40 virgolette, 2 per unita\', e nessun tab (per unita\')',
   sum(u['english'].count(QUOTE) for u in su) == 40 == sum(u['italian'].count(QUOTE) for u in tu)
   and all(u['italian'].count(QUOTE) == 2 for u in tu)
   and sum(u['english'].count(TAB) for u in su) == 0 == sum(u['italian'].count(TAB) for u in tu))
ck('ogni unita\' e\' una citazione intera: comincia e finisce con le virgolette',
   all(u['italian'].startswith('"') and u['italian'].endswith('"') for u in tu))
ck('0 segnaposto', sum(len(TAG.findall(u['english'])) for u in su) == 0
   == sum(len(TAG.findall(u['italian'])) for u in tu))
ck("19 etichette tradotte e un None in posizione 17 (unita' senza etichetta: la domanda Avgi)",
   [LABEL.match(u['italian']).group(1) if LABEL.match(u['italian']) else None for u in tu]
   == ['Scoramento', 'Sollievo', 'Segretezza', 'Sfida', 'Dubbio', 'Ironia', 'Interesse', 'Orgoglio',
       'Soddisfazione', 'Tristezza', 'Esasperazione', 'Orgoglio', 'Derisione', 'Umorismo', 'Riserva',
       'Rassicurazione', None, 'Riflessione', 'Determinazione', 'Orgoglio'])
ck("la 17 conserva il dispositivo della domanda Avgi: finisce con «, domanda?»",
   tu[16]['italian'].endswith(', domanda?"') and tu[16]['english'].endswith(', question?"'))
ck('nomi invariati con gli stessi conteggi (Consonance, Avgi, Tangled Shroud, Stilacrest, skyhook)',
   all(' '.join(u['italian'] for u in tu).count(w) == ' '.join(u['english'] for u in su).count(w)
       for w in ('Consonance', 'Avgi', 'Tangled Shroud', 'Stilacrest', 'skyhook')),
   [(w, ' '.join(u['italian'] for u in tu).count(w), ' '.join(u['english'] for u in su).count(w))
    for w in ('Consonance', 'Avgi', 'Tangled Shroud', 'Stilacrest', 'skyhook')])
ck('PENDING su tutte e 20', not [u['idx'] for u in su
                                 if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('nessun carattere tipografico e nessun non latino',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')
        or any(ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F for c in u['italian'])])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate 0,55-1,90 (0,90 - 1,28; 439 -> 433 parole)',
   0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('SEGMENTO: 42/115 unita\' del file (%.1f%%) · 22 prima · 20 qui · 73 dopo · confine riga 197 (frammento)'
      % (100.0 * len(lines) / 115))
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L234 superato' if not fail else 'verify L234 fallito')
raise SystemExit(0 if not fail else 1)
