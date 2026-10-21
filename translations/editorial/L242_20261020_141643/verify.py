r"""verify.py — L242 (`data/successors/successor jobs.txt`, 38 unita', righe 306-802). **LOTTO TERMINALE: chiude il file.**

**Invariante di FILE**: la copertura si legge da **tutti** i `translation.json` del percorso e si confronta col database:

    86 (L241) + 38 (L242) = 124 = unita' del file

Si asserisce insieme: **0 unita' dopo la 802**, `max(line) == 802`, **124 id distinti su 124 righe distinte**, nessuna riga
rivendicata due volte, e i conteggi **misurati** per lotto.

Verifica inoltre: i `VALUE` copiati dal **sorgente**, `<tons>` senza articolo (quantita' del motore), `<origin>` prima di
`<planet>`, Vecchie/Nuove Casate tradotte solo nella prosa, e la coerenza cross-lot con le formule di L241 e degli altri
lavori («Riceverai `<payment>`…», «entro il `<date>`»).

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
HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
ROOT = os.path.abspath(os.path.join(L10N, '..'))
PATH = 'data/successors/successor jobs.txt'
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


ck('riga grezza identica al sorgente (38/38)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck("unita: 38, righe 306 - 802", len(tu) == 38 and (tu[0]['line'], tu[-1]['line']) == (306, 802))
ck('19 VALUE + 19 DESCRIPTION', collections.Counter(u['kind'] for u in su) == {'VALUE': 19, 'DESCRIPTION': 19})
ck("86 unita' prima della 306 (L241)",
   db.execute('select count(*) from units where path=? and line<306', (PATH,)).fetchone()[0] == 86)
ck("ZERO unita' dopo la 802: il lotto CHIUDE il file",
   db.execute('select count(*) from units where path=? and line>802', (PATH,)).fetchone()[0] == 0)
ck('il file intero: 124 unita, righe 16 - 802',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (124, 16, 802))
VAL = [u for u in tu if u['kind'] == 'VALUE']
DES = [u for u in tu if u['kind'] == 'DESCRIPTION']
ck("i 19 VALUE sono copiati dal sorgente carattere per carattere",
   all(u['italian'] == u['english'] for u in VAL) and len(VAL) == 19,
   [u['idx'] for u in VAL if u['italian'] != u['english']])
ck("le 19 DESCRIPTION sono tutte tradotte", all(u['italian'] != u['english'] for u in DES))
ck('nessun tab, nessuna virgoletta, nessun apice',
   sum(u['english'].count(TAB) for u in su) == 0 == sum(u['italian'].count(TAB) for u in tu)
   and sum(u['english'].count(QUOTE) for u in su) == 0 == sum(u['italian'].count(QUOTE) for u in tu)
   and sum(u['english'].count(APOS) for u in su) == 0 == sum(u['italian'].count(APOS) for u in tu))
tok_en = collections.Counter(t for u in su for t in TAG.findall(u['english']))
tok_it = collections.Counter(t for u in tu for t in TAG.findall(u['italian']))
ck("segnaposto: 98 su 10 simboli, parita' per simbolo",
   tok_en == tok_it == {'<planet>': 28, '<payment>': 19, '<date>': 11, '<tons>': 11, '<origin>': 11,
                        '<bunks>': 7, '<destination>': 4, '<planet stopovers>': 3, '<stopovers>': 3,
                        '<cargo>': 1}, (dict(tok_en), dict(tok_it)))
ck("segnaposto: ordine identico in ogni unita'",
   all(tuple(TAG.findall(u['english'])) == tuple(TAG.findall(u['italian'])) for u in tu),
   [(u['idx'], TAG.findall(u['english']), TAG.findall(u['italian'])) for u in tu
    if TAG.findall(u['english']) != TAG.findall(u['italian'])])
ck("<origin> precede <planet> in tutte le unita' che li hanno entrambi",
   sum(1 for u in tu if '<origin>' in TAG.findall(u['english'])) == 11
   and all(TAG.findall(u['italian']).index('<origin>') < TAG.findall(u['italian']).index('<planet>')
           for u in tu if '<origin>' in TAG.findall(u['english'])))
prosa = ' '.join(u['italian'] for u in DES)
ck("<tons> senza articolo davanti, 11 volte (e' una quantita' del motore)",
   sum(u['italian'].count('<tons>') for u in DES) == 11
   and not re.search(r'\b(il|lo|la|i|gli|le|un|uno|una)\s+<tons>', prosa))
fam = collections.Counter(u['english'] for u in DES)
ck('14 formule distinte (una da 4, due da 2, undici da 1)', len(fam) == 14
   and sorted(fam.values()) == [1] * 11 + [2, 2, 4], sorted(fam.values()))
ck('una sola resa per famiglia',
   all(len({u['italian'] for u in DES if u['english'] == k}) == 1 for k in fam))
ck("Vecchie e Nuove Casate: tradotte con la maiuscola nella prosa, inglesi nei VALUE",
   prosa.count('Vecchie Casate') == 1 and prosa.count('Nuove Casate') == 1
   and 'Old Houses' not in prosa and 'New Houses' not in prosa
   and any(u['italian'] == 'Old Houses courier to <planet>' for u in VAL))
ck("coerenza cross-lot: «Riceverai <payment>» 12 volte (11 + «alla consegna», 1 da solo), «entro il <date>» 10, «su <destination>» 4",
   prosa.count('Riceverai <payment>') == 12 and prosa.count('Riceverai <payment> alla consegna') == 11
   and prosa.count('entro il <date>') == 10 and prosa.count('su <destination>') == 4,
   (prosa.count('Riceverai <payment>'), prosa.count('entro il <date>'), prosa.count('su <destination>')))
ck("PENDING su tutte e 38", not [u['idx'] for u in su
                                 if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0]
                                 != 'PENDING'])
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('nessun carattere tipografico e nessun non latino',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')
        or any(ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F for c in u['italian'])])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate 0,55-1,90 (0,92 - 1,09; 480 -> 435 parole)',
   0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
per, lines, ids, wen, wit = [], [], [], 0, 0
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    us = [u for u in json.load(open(f, encoding='utf-8'))['units'] if u['path'] == PATH]
    if us:
        per.append((os.path.basename(os.path.dirname(f)), len(us)))
        lines += [u['line'] for u in us]
        ids += [u['id'] for u in us]
        wen += sum(len(u['english'].split()) for u in us)
        wit += sum(len(u['italian'].split()) for u in us)
ck("INVARIANTE DI FILE: 86 + 38 = 124 unita' su 124 righe distinte, nessun doppione",
   sum(n for _, n in per) == 124 and per[-1][1] == 38
   and len(lines) == 124 == len(set(lines)) and len(ids) == 124 == len(set(ids))
   and max(lines) == 802, per)
ck("copertura = database: nessuna unita' del file resta fuori staging",
   set(ids) == set(i for (i,) in db.execute('select id from units where path=?', (PATH,))), len(set(ids)))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print("FILE: 124/124 unita' (100%%) in %d lotti: %s" % (len(per), ' + '.join('%s %d' % (k.split('_')[0], n) for k, n in per)))
print('FILE parole EN %d -> IT %d' % (wen, wit))
print('parole L242 EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L242 superato' if not fail else 'verify L242 fallito')
raise SystemExit(0 if not fail else 1)
