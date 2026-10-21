r"""check.py — L318 (`data/korath/korath weapons.txt`, righe 53-603). **Primo lotto** del file.

Diciassette `DESCRIPTION` in **15 contesti**: armi Korath, dalle torrette gravitazionali ai ripetitori termici, fino ai missili
`Piercer` e alla **munizione** `Cluster Mine`.

Il test difende quattro cose dichiarate nel contratto:

1. **la nota dei rifornimenti** (riga 473) ha **gia' una resa unica** nel corpus, usata in **25 unita'**: si verifica
   **per uguaglianza con un lotto precedente**, non a parole;
2. **la riga 154** — il contratto la dichiarava con **due punti finali** (`close..`): **la misura dice il contrario**, e' un'
   **ellissi** (`close... but not too close.`). La resa usa i **tre punti** `...` e **non** riproduce nessun refuso: il contratto si
   corregge sulla misura;
3. **la riga 603 e' una MUNIZIONE** e deve nominare il **suo** contenitore (`Cluster Mine Layer`);
4. **due tab** (109, 473) come primo carattere, e **zero** altrove.
"""
import collections
import glob
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
PATH = 'data/korath/korath weapons.txt'
NOTA_EN = TAB + 'Ammunition for this weapon can be restocked at any outfitter.'
ARMI = ['Grab-Strike', 'Shunt-Strike', 'Banisher', 'Expeller', 'Warder', 'Fire-Lance', 'Blaze-Pike',
        'Inferno', 'Thermal Repeater', 'Piercer', 'Detainer', 'Cluster Mine']
src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
units = sorted(src['units'], key=lambda x: x['line'])
tr = {}
for p in sorted(f for f in os.listdir(os.path.join(HERE, 'parts')) if f.endswith('.json')):
    for k, v in json.load(open(os.path.join(HERE, 'parts', p), encoding='utf-8')).items():
        tr[int(k)] = v
out = {'block': src['block'], 'note': src['note'], 'units': []}
for u in units:
    if u['idx'] in tr:
        it = tr[u['idx']]
        out['units'].append({"idx": u['idx'], "id": u['id'], "path": u['path'], "line": u['line'],
                             "kind": u['kind'], "context": u['context'], "english": u['english'],
                             "italian": it, "ratio": round(len(it) / max(1, len(u['english'])), 3)})
open(os.path.join(HERE, 'translation.json'), 'w', encoding='utf-8').write(
    json.dumps(out, ensure_ascii=False, indent=1))
cov = out['units']
by = {u['idx']: u for u in cov}
at = {u['line']: u for u in cov}
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else 'FAIL'), c))


ck('unita tradotte 17/17', len(cov) == 17 == len(units), '%d/%d' % (len(cov), len(units)))
ck('tutte e 17 sono DESCRIPTION',
   collections.Counter(u['kind'] for u in cov) == {'DESCRIPTION': 17})
ck('15 contesti: Shunt-Strike e Piercer Launcher doppi, tredici singoli',
   len({u['context'] for u in cov}) == 15
   and [c for c, n in collections.Counter(u['context'] for u in cov).items() if n == 2]
   == ['outfit:Shunt-Strike Turret', 'outfit:Piercer Missile Launcher'],
   collections.Counter(u['context'] for u in cov).most_common(3))
# la nota dei rifornimenti: uguaglianza con il corpus
ref = None
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    if os.path.basename(os.path.dirname(f)) == os.path.basename(HERE):
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['english'] == NOTA_EN:
            ref = u['italian']
            break
    if ref:
        break
ck('la nota dei rifornimenti e IDENTICA alla resa gia fissata nel corpus',
   at[473]['english'] == NOTA_EN and ref is not None and at[473]['italian'] == ref,
   (at[473]['italian'], ref))
ck('la 154 e un ELLISSI, non un refuso: tre punti e nessun «..»',
   at[154]['english'] == 'The Korath like to keep their enemies close... but not too close.'
   and '...' in at[154]['italian'] and '..' not in at[154]['italian'].replace('...', '')
   and '\u2026' not in at[154]['italian'],
   repr(at[154]['italian']))
ck('due tab, righe 109 e 473, come primo carattere',
   [u['line'] for u in cov if u['italian'].startswith(TAB)] == [109, 473],
   [u['line'] for u in cov if u['italian'].startswith(TAB)])
ck('la 603 e munizione per il CLUSTER MINE LAYER, non per altro',
   'munizione per un Cluster Mine Layer' in at[603]['italian']
   and 'undici' in at[603]['italian'])
ck('la 423 e il launcher: missile lanciato da un Piercer Missile Launcher',
   'Piercer Missile Launcher' in at[423]['italian'])
ck('la 435 e lo stivaggio per i launcher',
   'Piercer Missile Rack' in at[435]['italian'] and 'munizioni supplementari' in at[435]['italian'])
ck('nomi delle armi INVARIATI dove compaiono',
   all(n in u['italian'] for u in cov for n in ARMI if n in u['english']),
   [(u['line'], n) for u in cov for n in ARMI if n in u['english'] and n not in u['italian']])
ck('`Systems Core` resta invariato e `Exile` e «Esilio»',
   'Systems Core' in at[108]['italian'] and "dell'Esilio" in at[108]['italian'])
ck('la gestalt delle due Fire-Lance e la sinergia delle tre',
   'gestalt' in at[287]['italian'] and 'sinergia' in at[327]['italian'])
ck('il Detainer: portata lunga e propulsione, e il nome dei Korath',
   'portata eccezionalmente lunga' in at[563]['italian']
   and 'sistemi di propulsione' in at[563]['italian']
   and 'nome dei Korath' in at[563]['italian'])
ck('VIRGOLETTE: zero · SEGNAPOSTO: nessuno · ALTERNATIVE: nessuna (asserzioni vuote)',
   sum(u['italian'].count(QUOTE) for u in cov) == 0
   and not TAG.findall(''.join(u['italian'] for u in cov))
   and sum(len(ALT.findall(u['italian'])) for u in cov) == 0)
ck('APICI: tre in inglese (108, 109, 472)',
   [u['line'] for u in cov if u['english'].count(APOS)] == [108, 109, 472],
   {u['line']: u['english'].count(APOS) for u in cov if u['english'].count(APOS)})
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in cov for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessun doppio spazio (la tab iniziale non conta)',
   not [u['idx'] for u in cov if '  ' in u['italian'].lstrip(TAB)])
ck('rapporto nel gate 0,55-1,90',
   all(0.55 < u['ratio'] < 1.90 for u in cov),
   [(u['idx'], u['ratio']) for u in cov if not 0.55 < u['ratio'] < 1.90])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("SEGMENTO: zero unita' prima della 53 — il lotto APRE il file",
   db.execute('select count(*) from units where path=? and line<53', (PATH,)).fetchone()[0] == 0)
ck("SEGMENTO: 22 unita' dopo la 603 (la prossima alla 615)",
   db.execute('select count(*) from units where path=? and line>603', (PATH,)).fetchone()[0] == 22
   and db.execute('select min(line) from units where path=? and line>603', (PATH,)).fetchone()[0] == 615)
ck('FILE: 17 unita qui su 39 del file',
   db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0] == 39)
ck('tutte le 17 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · 17 DESCRIPTION in 15 contesti · 2 tab · 0 virgolette' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
