r"""verify.py — L238 (`data/avgi/avgi news.txt`, 21 unita', righe 418-507). **LOTTO TERMINALE: chiude il file.**

**Invariante di FILE** (l'unico caso in cui e' legittimo, cfr. decisione 181): la copertura si legge da **tutti** i
`translation.json` che contengono `data/avgi/avgi news.txt` e si confronta con il database:

    22 (L233) + 20 (L234) + 15 (L235) + 23 (L236) + 14 (L237) + 21 (L238) = 115 = unita' del file

Si asserisce, in una sola condizione: **0 unita' dopo la 507**, `max(line) == 507`, **115 id distinti su 115 righe**,
**nessuna riga rivendicata due volte**, e l'elenco dei lotti con i loro conteggi **misurati** (non scritti a mano).

Verifica inoltre le cinque etichette nuove, l'etichetta a meta' frase (454) e la distinzione
`Recollection` -> «Rievocazione» / `Remembrance` -> «Ricordo».

Indipendente da `check.py`: rilegge `source.json`, i `translation.json`, il database e il file del gioco.
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
    print('%-80s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente (21/21)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck("unita: 21, righe 418 - 507", len(tu) == 21 and (tu[0]['line'], tu[-1]['line']) == (418, 507))
ck('4 contesti con i conteggi misurati',
   collections.Counter(u['context'] for u in su) == {'news:avgi engineer': 7, 'news:avgi artist': 3,
                                                     'news:avgi performer': 3, 'news:avgi doctor': 8},
   dict(collections.Counter(u['context'] for u in su)))
ck("94 unita' prima della 418 (L233-L237)",
   db.execute('select count(*) from units where path=? and line<418', (PATH,)).fetchone()[0] == 94)
ck("ZERO unita' dopo la 507: il lotto CHIUDE il file",
   db.execute('select count(*) from units where path=? and line>507', (PATH,)).fetchone()[0] == 0)
ck('il file intero: 115 unita, righe 32 - 507',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (115, 32, 507))
ck('tipi del lotto: 21 NEWS', collections.Counter(u['kind'] for u in su) == {'NEWS': 21})
ck("ZERO unita identiche all'inglese, 21 tradotte",
   sum(1 for u in tu if u['italian'] == u['english']) == 0
   and sum(1 for u in tu if u['italian'] != u['english']) == 21)
ck("42 virgolette, 2 per unita', nessun tab, nessun segnaposto",
   sum(u['english'].count(QUOTE) for u in su) == 42 == sum(u['italian'].count(QUOTE) for u in tu)
   and all(u['italian'].count(QUOTE) == 2 for u in tu)
   and sum(u['english'].count(TAB) for u in su) == 0 == sum(u['italian'].count(TAB) for u in tu)
   and sum(len(TAG.findall(u['english'])) for u in su) == 0 == sum(len(TAG.findall(u['italian'])) for u in tu))
EN_LAB = [LABEL.match(u['english']).group(1) if LABEL.match(u['english']) else None for u in su]
IT_LAB = [LABEL.match(u['italian']).group(1) if LABEL.match(u['italian']) else None for u in tu]
ck("etichette: 20 in testa + unita' 10 senza (il None e' confrontato, non ignorato)",
   EN_LAB == ['Fascination', 'Curiosity', 'Amusement', 'Appreciation', 'Advisement', 'Appreciation',
              'Annoyance', 'Pride', 'Frustration', None, 'Pride', 'Pride', 'Satisfaction', 'Appreciation',
              'Amusement', 'Fascination', 'Interest', 'Consideration', 'Consideration', 'Recollection',
              'Recollection']
   and IT_LAB == ['Fascinazione', 'Curiosità', 'Divertimento', 'Apprezzamento', 'Avviso', 'Apprezzamento',
                  'Fastidio', 'Orgoglio', 'Frustrazione', None, 'Orgoglio', 'Orgoglio', 'Soddisfazione',
                  'Apprezzamento', 'Divertimento', 'Fascinazione', 'Interesse', 'Considerazione',
                  'Considerazione', 'Rievocazione', 'Rievocazione'], (EN_LAB, IT_LAB))
ck("etichetta a META' FRASE (454): `, emphasis.` -> `, enfasi.` in minuscolo, dopo la virgola",
   ', emphasis.' in by[10]['english'] and ', enfasi.' in by[10]['italian']
   and by[10]['italian'].count('enfasi') == 1)
ck("`Recollection` -> «Rievocazione», distinta da `Remembrance` -> «Ricordo»",
   [u for u in tu if u['idx'] in (20, 21)][0]['italian'].startswith('"Rievocazione.')
   and 'Ricordo' not in ' '.join(u['italian'] for u in tu))
ck("`Advisement` -> «Avviso» (non «Avvertenza», che e' `Warning`)",
   by[5]['italian'].startswith('"Avviso.') and 'Avvertenza' not in ' '.join(u['italian'] for u in tu))
ck("`Twilight Guard` invariato, i membri tradotti: «le Guardie»",
   'Twilight Guard' in by[12]['italian'] and 'Guardie' in by[12]['italian'])
ck('PENDING su tutte e 21', not [u['idx'] for u in su
                                 if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0]
                                 != 'PENDING'])
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('nessun carattere tipografico e nessun non latino',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')
        or any(ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F for c in u['italian'])])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate 0,55-1,90 (0,95 - 1,23; 502 -> 508 parole)',
   0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
# --- invariante di FILE -------------------------------------------------------
per, lines, ids = [], [], []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    d = json.load(open(f, encoding='utf-8'))
    us = [u for u in d['units'] if u['path'] == PATH]
    if us:
        per.append((os.path.basename(os.path.dirname(f)), len(us)))
        lines += [u['line'] for u in us]
        ids += [u['id'] for u in us]
ck('INVARIANTE DI FILE: 22+20+15+23+14+21 = 115 unita su 115 righe distinte, nessun doppione',
   sum(n for _, n in per) == 115 and [n for _, n in per][:1] == [22]
   and len(lines) == 115 == len(set(lines)) and len(ids) == 115 == len(set(ids))
   and max(lines) == 507 and per[-1][1] == 21, per)
ck('copertura = database: nessuna unita\' del file resta fuori staging',
   set(ids) == set(i for (i,) in db.execute('select id from units where path=?', (PATH,))),
   len(set(ids)))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('FILE: 115/115 unita\' (100%%) in %d lotti: %s' % (len(per), ' + '.join('%s %d' % (k.split('_')[0], n) for k, n in per)))
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L238 superato' if not fail else 'verify L238 fallito')
raise SystemExit(0 if not fail else 1)
