r"""verify.py — L241 (`data/successors/successor jobs.txt`, 86 unita', righe 16-280). Primo lotto del file.

**Invariante di SEGMENTO** (il file NON e' chiuso: 124 unita'): **0** prima della 16 (e' la prima riga del file), **86**
qui, **38** dopo la 280, confine misurato alla **306** (`VALUE` di `mission:Successors: Students In`). La copertura si
**stampa** (86/124, 69,4%) e non si asserisce come elenco di lotti: si pretende che **nessun altro** `translation.json`
rivendichi queste righe.

Verifica da sola cio' che il `check.py` potrebbe sbagliare: i **VALUE copiati dal sorgente**, la coerenza dei **21 gruppi
di inglese identico**, i **4 frammenti con uno spazio in meno** e — soprattutto — la **composizione**: ricostruisce i
gruppi dal `source.json` leggendo i blocchi `phrase` del file del gioco, compone tutte le combinazioni e pretende che
nessuna frase italiana abbia doppi spazi o punteggiatura attaccata male.
"""
import collections
import glob
import hashlib
import itertools
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
PATH = 'data/successors/successor jobs.txt'
src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
su = sorted(src['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
by = {u['idx']: u for u in tu}
raw_lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
raw_all = '\n'.join(raw_lines)
fail = []


def ck(n, c, d=''):
    print('%-82s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente (86/86)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck("unita: 86, righe 16 - 280", len(tu) == 86 and (tu[0]['line'], tu[-1]['line']) == (16, 280))
ck('76 TEXT + 5 VALUE + 5 DESCRIPTION',
   collections.Counter(u['kind'] for u in su) == {'TEXT': 76, 'VALUE': 5, 'DESCRIPTION': 5})
ck("ZERO unita' prima della 16: e' la prima riga del file",
   db.execute('select count(*) from units where path=? and line<16', (PATH,)).fetchone()[0] == 0)
ck("38 unita' dopo la 280: il lotto NON chiude il file",
   db.execute('select count(*) from units where path=? and line>280', (PATH,)).fetchone()[0] == 38)
nxt = db.execute('select line,kind,context from units where path=? and line>280 order by line limit 1', (PATH,)).fetchone()
ck('confine misurato: riga 306, VALUE di mission:Successors: Students In',
   nxt == (306, 'VALUE', 'mission:Successors: Students In'), nxt)
ck('il file intero: 124 unita, righe 16 - 802',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (124, 16, 802))
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
ck("nessun ALTRO lotto rivendica le righe di questo segmento (86 righe distinte)",
   not overlap and len(mine) == 86, (overlap, len(mine)))
VAL = [u for u in tu if u['kind'] == 'VALUE']
ck("i 5 VALUE sono copiati dal sorgente carattere per carattere",
   all(u['italian'] == u['english'] for u in VAL), [u['idx'] for u in VAL if u['italian'] != u['english']])
ck("le 81 unita' di prosa sono tutte tradotte",
   all(u['italian'] != u['english'] for u in tu if u['kind'] != 'VALUE'))
ck('nessun tab, nessuna virgoletta',
   sum(u['english'].count(TAB) for u in su) == 0 == sum(u['italian'].count(TAB) for u in tu)
   and sum(u['english'].count(QUOTE) for u in su) == 0 == sum(u['italian'].count(QUOTE) for u in tu))
tok_en = collections.Counter(t for u in su for t in TAG.findall(u['english']))
tok_it = collections.Counter(t for u in tu for t in TAG.findall(u['italian']))
ck("segnaposto: 45 su 8 famiglie, parita' per simbolo",
   tok_en == tok_it == {'<payment>': 15, '<planet>': 7, '<bunks>': 5, '<destination>': 5,
                        '<date>': 5, '<planet stopovers>': 3, '<stopovers>': 3, '<commodity>': 2},
   (dict(tok_en), dict(tok_it)))
ck("segnaposto: ordine identico in ogni unita'",
   all(tuple(TAG.findall(u['english'])) == tuple(TAG.findall(u['italian'])) for u in tu),
   [(u['idx'], TAG.findall(u['english']), TAG.findall(u['italian'])) for u in tu
    if TAG.findall(u['english']) != TAG.findall(u['italian'])])
ck("stesso inglese => stessa resa: 21 gruppi, tutti con una sola resa",
   sum(1 for k, n in collections.Counter(u['english'] for u in tu).items() if n > 1) == 21
   and all(len({u['italian'] for u in tu if u['english'] == k}) == 1
           for k, n in collections.Counter(u['english'] for u in tu).items() if n > 1))
ck("spazi: solo le 4 unita' 43/44/65/66 differiscono dall'inglese, e di UNO spazio finale in meno",
   [u['idx'] for u in tu if (len(u['english']) - len(u['english'].strip(' ')))
    != (len(u['italian']) - len(u['italian'].strip(' ')))] == [43, 44, 65, 66]
   and all(by[i]['english'].endswith(' ') and not by[i]['italian'].endswith(' ') for i in (43, 44, 65, 66)))
# --- struttura dei blocchi phrase letta dal FILE DEL GIOCO (indipendente dal check.py) ---
blocchi, cur, gruppo = {}, None, None
for ln in raw_lines:
    m = re.match(r'^phrase "([^"]+)"$', ln.rstrip())
    if m:
        cur = m.group(1)
        blocchi[cur] = []
        gruppo = None
        continue
    if cur is None:
        continue
    if ln.strip() == 'word':
        gruppo = []
        blocchi[cur].append(gruppo)
        continue
    m = re.match(r'^\t\t`(.*)`$', ln.rstrip('\n'))
    if m and gruppo is not None:
        gruppo.append(m.group(1))
att = {k: len(v) for k, v in blocchi.items()}
ck('i quattro blocchi phrase del lotto hanno 6 · 7 · 7 · 7 gruppi (gli altri 9 blocchi del file non sono nel lotto)',
   {k: att[k] for k in ('successor data', 'high houses delivery',
                        'predecessor researchers out', 'successor researchers out')} ==
   {'successor data': 6, 'high houses delivery': 7,
    'predecessor researchers out': 7, 'successor researchers out': 7}
   and len(att) == 13, (att, len(att)))
ck("il quarto gruppo dei due blocchi «researchers» ha 4 opzioni nel sorgente, una delle quali VUOTA",
   '' in blocchi['predecessor researchers out'][3] and '' in blocchi['successor researchers out'][3]
   and len(blocchi['predecessor researchers out'][3]) == 4)
CAMPIONE = {'<payment>': '1.000 crediti', '<commodity>': 'ferro', '<planet stopovers>': 'Korell e Vail',
            '<stopovers>': 'Korell', '<planet>': 'Korell', '<destination>': 'Korell', '<date>': '12 marzo',
            '<bunks>': '4'}
# mappa: per ogni blocco, gli indici delle unita' nell'ordine dei gruppi del sorgente
IDX = {
 'successor data': [[8], [9, 10, 11], [12, 13, 14, 15], [16], [17, 18], [19, 20]],
 'high houses delivery': [[21], [22, 23, 24, 25], [26, 27], [28, 29], [30], [31, 32, 33], [34]],
 'predecessor researchers out': [[35], [36, 37, 38], [39], [40, 41, 42, None], [43, 44],
                                 [45, 46, 47, 48, 49, 50, 51, 52, 53], [54, 55, 56]],
 'successor researchers out': [[57], [58, 59, 60], [61], [62, 63, 64, None], [65, 66],
                               [67, 68, 69, 70, 71], [72, 73, 74]],
}
ck("la mappa dei gruppi combacia col numero di opzioni del sorgente, per ogni blocco",
   all([len(g) for g in IDX[b]] == [len(g) for g in blocchi[b]] for b in IDX), None)
tot_en = tot_it = 0
dif = []
for b in IDX:
    campi_it = [['' if i is None else by[i]['italian'] for i in g] for g in IDX[b]]
    campi_en = [['' if i is None else by[i]['english'] for i in g] for g in IDX[b]]
    for combo in itertools.product(*campi_en):
        tot_en += 1
    for combo in itertools.product(*campi_it):
        tot_it += 1
        t = ''.join(combo)
        for k, v in CAMPIONE.items():
            t = t.replace(k, v)
        if '  ' in t or re.search(r'\s[.,;:!]', t) or not t[:1].isupper() or not t.endswith('.') or '<' in t:
            dif.append((b, t[:80]))
ck('composizione: 1104 frasi per lingua (48 + 48 + 648 + 360)', tot_en == 1104 == tot_it, (tot_en, tot_it))
ck('composizione: nessun difetto di spaziatura o punteggiatura nelle 1104 frasi italiane', not dif, dif[:3])
ck("composizione: «Consegni i ricercatori a Korell e Vail, dove subito prendono a catalogare…»",
   ''.join([by[35]['italian'], by[36]['italian'], by[39]['italian'], by[40]['italian'],
            by[44]['italian'], by[45]['italian'], by[54]['italian']]).replace('<planet stopovers>', 'Korell e Vail')
   == 'Tu consegni i ricercatori a Korell e Vail, dove subito prendono a catalogare alcune formazioni rocciose vicine. '
      'Dopo qualche ora, sono pronti a tornare a casa.')
ck("composizione: «Tu consegni a mano le banche dati criptate e poi ricevi…»",
   ''.join([by[8]['italian'], by[10]['italian'], by[12]['italian'], by[16]['italian'],
            by[17]['italian'], by[19]['italian']]).replace('<payment>', '1.000 crediti')
   == 'Tu consegni a mano le banche dati criptate e poi ricevi 1.000 crediti in pagamento.')
# accordo articolo + nome, controllato sulle frasi composte (indipendente dal check.py)
NOMI = {'ricercatori', 'scienziati', 'studiosi', 'sperimentatori', 'carico', 'lotto',
        'pagamento', 'banche', 'dati'}
OK_ART = {('i', 'ricercatori'), ('gli', 'scienziati'), ('gli', 'studiosi'), ('gli', 'sperimentatori'),
          ('il', 'carico'), ('il', 'lotto'), ('il', 'pagamento'), ('le', 'banche'), ('i', 'dati')}
male = []
for b in IDX:
    campi = [['' if i is None else by[i]['italian'] for i in g] for g in IDX[b]]
    for combo in itertools.product(*campi):
        t = ''.join(combo)
        for k, v in CAMPIONE.items():
            t = t.replace(k, v)
        for m in re.finditer(r'\b(il|lo|la|i|gli|le)\s+(?:tuo\s+|tua\s+)?(\w+)', t):
            if m.group(2) in NOMI and (m.group(1), m.group(2)) not in OK_ART:
                male.append((m.group(0), b))
ck("accordo articolo+nome nelle frasi composte: nessuna coppia fuori dalla lista ammessa", not male, male[:3])
ck("PENDING su tutte e 86", not [u['idx'] for u in su
                                 if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0]
                                 != 'PENDING'])
ck('nessun doppio spazio nelle singole unita\'', not [u['idx'] for u in tu if '  ' in u['italian']])
ck('nessun carattere tipografico e nessun non latino',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')
        or any(ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F for c in u['italian'])])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate 0,55-1,90 (0,67 - 1,70; 428 -> 445 parole)',
   0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print("SEGMENTO: %d/%d unita' del file (%.1f%%) · 0 prima · 86 qui · 38 dopo · confine riga 306"
      % (len(lines), 124, 100.0 * len(lines) / 124))
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L241 superato' if not fail else 'verify L241 fallito')
raise SystemExit(0 if not fail else 1)
