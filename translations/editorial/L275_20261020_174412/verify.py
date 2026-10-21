r"""verify.py — L275 (`data/korath/korath ships.txt`, righe 606-1311). **Terzo lotto del file**.

Verifica da sola: riga grezza, campi del DB, il **segmento** (17 prima, 14 qui, **19** dopo la 1311), i **sette contesti** con
le righe, i **due tab**, le **due virgolette**, i cinque `VALUE` copiati, e che **nessun altro lotto** rivendichi queste righe.

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
HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
ROOT = os.path.abspath(os.path.join(L10N, '..'))
PATH = 'data/korath/korath ships.txt'
CTX = ["Lor'kas Ik 577", "Ra'gru Ik 618", "Kas'lor Ik 582", "Lor'nag Ik 590", "Ra'at Ik 621",
       "Kasichara A'awoj", "Korsmanath A'awoj"]
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


ck('riga grezza identica al sorgente (14/14)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = [u['idx'] for u in su
       if db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
       != (u['english'], u['kind'], u['path'], u['context'])]
ck('english/kind/path/context identici al DB', not bad, bad)
ck('14 unita, righe 606-1311, 9 DESCRIPTION + 5 VALUE',
   len(tu) == 14 and [u['line'] for u in tu] == sorted({u['line'] for u in tu})
   and collections.Counter(u['kind'] for u in tu) == {'DESCRIPTION': 9, 'VALUE': 5},
   (len(tu), collections.Counter(u['kind'] for u in tu)))
ck('i sette contesti compaiono in quest ordine, senza altri',
   [c.replace('ship:', '', 1) for c in dict.fromkeys(u['context'] for u in tu)] == CTX,
   [c for c in dict.fromkeys(u['context'] for u in tu)])
ck("17 unita' prima (L273 + L274)",
   db.execute('select count(*) from units where path=? and line<606', (PATH,)).fetchone()[0] == 17)
ck("19 unita' dopo la 1311",
   db.execute('select count(*) from units where path=? and line>1311', (PATH,)).fetchone()[0] == 19)
ck('confine: la 1375 apre `Echo-Galleon`',
   db.execute('select line,context from units where path=? and line>1311 order by line limit 1', (PATH,)).fetchone()
   == (1375, 'ship:Echo-Galleon'))
ck('il file ha 50 unita, righe 95-2363',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (50, 95, 2363))
per_lotto, righe = [], set()
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    us = [u for u in json.load(open(f, encoding='utf-8'))['units'] if u['path'] == PATH]
    if us:
        per_lotto.append((os.path.basename(os.path.dirname(f)), len(us)))
        righe |= {u['line'] for u in us}
seg = {l for l in righe if 606 <= l <= 1311}
ck('SEGMENTO: le 14 righe del lotto sono esattamente quelle 606-1311',
   seg == {u['line'] for u in tu} and len(seg) == 14, (sorted(seg - {u['line'] for u in tu}), len(seg)))
overlap = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    if os.path.basename(os.path.dirname(f)) == os.path.basename(HERE):
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH and 606 <= u['line'] <= 1311:
            overlap.append((os.path.basename(os.path.dirname(f)), u['line']))
ck('nessun altro lotto rivendica le righe 606-1311', not overlap, overlap)
ck('copertura del SEGMENTO: 14/14 righe; il totale del file e stampato, non asserito',
   len(seg) == 14 and 50 - len(seg) == 36, '%d/50 (file)' % len(righe))
ck('i cinque VALUE sono copiati; le nove DESCRIPTION sono tradotte',
   sorted(u['idx'] for u in tu if u['italian'] == u['english']) == [1, 3, 5, 7, 9]
   and all(u['italian'] != u['english'] for u in tu if u['idx'] not in (1, 3, 5, 7, 9)),
   sorted(u['idx'] for u in tu if u['italian'] == u['english']))
ck('TAB: due, alle unita 12 e 14, primi caratteri in entrambe le lingue',
   sum(u['english'].count(TAB) for u in tu) == 2 == sum(u['italian'].count(TAB) for u in tu)
   and [u['idx'] for u in tu if TAB in u['italian']] == [12, 14]
   and all(u['italian'].startswith(TAB) for u in tu if TAB in u['italian']))
ck('VIRGOLETTE: due, all unita 11, dritte',
   sum(u['english'].count(QUOTE) for u in tu) == 2 == sum(u['italian'].count(QUOTE) for u in tu)
   and [u['idx'] for u in tu if QUOTE in u['italian']] == [11])
ck('apici: 9 in inglese, 16 in italiano',
   sum(u['english'].count(APOS) for u in tu) == 9 and sum(u['italian'].count(APOS) for u in tu) == 16,
   (sum(u['english'].count(APOS) for u in tu), sum(u['italian'].count(APOS) for u in tu)))
ck('lessico: navi da produzione, telaio, motore di salto, portatrici, navi-città, navarchi',
   'navi da produzione' in by[2]['italian'] and 'telaio' in by[2]['italian']
   and 'motore di salto' in by[8]['italian'] and 'portatrici' in by[10]['italian']
   and 'navi-città' in by[12]['italian'] and 'navarchi' in by[14]['italian'])
ck('i nomi Korath restano dove l inglese li nomina',
   not [(u['idx'], n) for u in tu for n in ('Efreti', 'Mereti', 'Sestor', 'Korsmanathi', 'Anatruskor',
                                            'Deka Dathnak', "Kasichara A'awoj", "Korsmanath A'awoj")
        if n in u['english'] and n not in u['italian']])
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in tu for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90 per le nove DESCRIPTION',
   all(0.55 < u['ratio'] < 1.90 for u in tu if u['idx'] not in (1, 3, 5, 7, 9)),
   [(u['idx'], u['ratio']) for u in tu if u['idx'] not in (1, 3, 5, 7, 9) and not 0.55 < u['ratio'] < 1.90])
ck('tutte le 14 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in tu))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('SEGMENTO: 17 prima · 14 qui · 19 dopo · 7 contesti · 2 tab · 2 virgolette')
print('parole EN %d -> IT %d · ratio %.2f - %.2f (DESCRIPTION)' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(u['ratio'] for u in tu if u['idx'] not in (1, 3, 5, 7, 9)),
    max(u['ratio'] for u in tu if u['idx'] not in (1, 3, 5, 7, 9))))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L275 superato' if not fail else 'verify L275 fallito')
raise SystemExit(0 if not fail else 1)
