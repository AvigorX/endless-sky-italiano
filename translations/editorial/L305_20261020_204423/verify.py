r"""verify.py — L305 (`data/quarg/quarg outfits.txt`, righe 138-243). **Secondo lotto del file**.

Verifica da sola: riga grezza, campi del DB, il **segmento** (**11** prima, **10** qui, **10** dopo la 243), la **continuita'**
`Large Graviton Steering` (137 in L304 / 138 qui), il **ritornello** confrontato con L304, le **due coppie**, le **tre schede dei
generatori di scudi**, e che **nessun altro lotto** rivendichi le righe 138-243.

Indipendente da `check.py`. La copertura del **FILE** e' **stampata, non asserita**.
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
ALT = re.compile(r'\[[^\]]*\]')
HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
ROOT = os.path.abspath(os.path.join(L10N, '..'))
PREV = os.path.join(L10N, 'staging', 'editorial', 'L304_20261020_203826', 'translation.json')
PATH = 'data/quarg/quarg outfits.txt'
COPPIE = [(180, 181), (195, 196)]
TABBED = [138, 181, 196]
SCUDI = [213, 228, 243]
src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
su = sorted(src['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
raw_lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
by = {u['idx']: u for u in tu}
at = {u['line']: u for u in tu}
prev = {u['line']: u for u in json.load(open(PREV, encoding='utf-8'))['units']}
fail = []


def ck(n, c, d=''):
    print('%-96s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente (10/10)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = [u['idx'] for u in su
       if db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
       != (u['english'], u['kind'], u['path'], u['context'])]
ck('english/kind/path/context identici al DB', not bad, bad)
grp = collections.Counter(u['context'] for u in tu)
ck('10 unita DESCRIPTION, otto contesti (6 singole + 2 coppie)',
   len(tu) == 10 and {u['kind'] for u in tu} == {'DESCRIPTION'}
   and sorted(grp.values()) == [1] * 6 + [2, 2], dict(grp))
ck("11 unita' prima della 138 e 10 dopo la 243",
   db.execute('select count(*) from units where path=? and line<138', (PATH,)).fetchone()[0] == 11
   and db.execute('select count(*) from units where path=? and line>243', (PATH,)).fetchone()[0] == 10)
ck('la prima unita dopo la 243 e `Peripheral Repair Hub` alla 257',
   db.execute('select line,context from units where path=? and line>243 order by line limit 1', (PATH,)).fetchone()
   == (257, 'outfit:Peripheral Repair Hub'))
ck('il file ha 31 unita, righe 37-579',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (31, 37, 579))
righe = set()
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH:
            righe.add(u['line'])
seg = {l for l in righe if 138 <= l <= 243}
ck('SEGMENTO: le 10 righe del lotto sono esattamente quelle 138-243',
   seg == {u['line'] for u in tu} and len(seg) == 10, (sorted(seg - {u['line'] for u in tu}), len(seg)))
overlap = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    if os.path.basename(os.path.dirname(f)) == os.path.basename(HERE):
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH and 138 <= u['line'] <= 243:
            overlap.append((os.path.basename(os.path.dirname(f)), u['line']))
ck('nessun altro lotto rivendica le righe 138-243', not overlap, overlap)
ck('copertura: 10 righe nel segmento; totale del file stampato e non supera 31',
   len(seg) == 10 and len(righe) <= 31, '%d/31 al momento' % len(righe))
ck('tutte e 10 le unita sono tradotte', all(u['italian'] != u['english'] for u in tu))
ck('CONTINUITA 137/138: prima meta senza tab, seconda con tab, stesso contesto',
   prev[137]['context'] == at[138]['context'] == 'outfit:Large Graviton Steering'
   and not prev[137]['english'].startswith(TAB) and at[138]['english'].startswith(TAB)
   and at[138]['italian'].startswith(TAB))
ck('RITORNELLO: la 138 identica alle quattro di L304',
   at[138]['italian'] == prev[55]['italian'] == prev[78]['italian'] == prev[96]['italian'] == prev[120]['italian'])
ck('COPPIE con tab sulla seconda e secondi paragrafi DIVERSI',
   all(at[b]['context'] == at[a]['context'] and at[b]['english'].startswith(TAB) for a, b in COPPIE)
   and at[181]['italian'] != at[196]['italian'])
ck('TAB: tre unita, righe dichiarate', sorted(u['line'] for u in tu if u['english'].startswith(TAB)) == TABBED
   and sum(u['italian'].count(TAB) for u in tu) == 3)
ck('tre schede singole per i generatori di scudi',
   [u['line'] for u in tu if 'Shield Generator' in u['context']] == SCUDI)
ck('ASSERZIONI VUOTE: 0 virgolette, 0 segnaposto, 0 alternative',
   sum(u['english'].count(QUOTE) for u in tu) == 0 == sum(u['italian'].count(QUOTE) for u in tu)
   and sum(len(TAG.findall(u['italian'])) for u in tu) == 0
   and sum(len(ALT.findall(u['italian'])) for u in tu) == 0)
ck('apici: 2 in inglese, 6 in italiano',
   sum(u['english'].count(APOS) for u in tu) == 2 and sum(u['italian'].count(APOS) for u in tu) == 6,
   (sum(u['english'].count(APOS) for u in tu), sum(u['italian'].count(APOS) for u in tu)))
ck('lessico tecnico: buco nero, Hawking, orizzonte degli eventi, disco di accrescimento, vuoto quantistico',
   'buco nero' in at[180]['italian'] and 'radiazione di Hawking' in at[180]['italian']
   and 'orizzonte degli eventi' in at[195]['italian'] and 'disco di accrescimento' in at[195]['italian']
   and 'vuoto quantistico' in at[153]['italian'])
ck('nomi nel testo invariati, nessuna italianizzazione',
   all(n in ''.join(u['italian'] for u in tu) for n in ['Quarg', 'Singularity Core', 'Quasar Core', 'Antimatter Core'])
   and not any(x in ''.join(u['italian'] for u in tu) for x in ['Aspide', 'Egida']))
ck('registro: nessuna seconda persona',
   not [u['idx'] for u in tu if re.search(r'\b(tu|tuo|tua|tuoi|tue|ti|te)\b', u['italian'])])
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in tu for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessun doppio spazio (la tab iniziale non conta)',
   not [u['idx'] for u in tu if '  ' in u['italian'].lstrip(TAB)])
ck('rapporto nel gate 0,55-1,90',
   all(0.55 < u['ratio'] < 1.90 for u in tu),
   [(u['idx'], u['ratio']) for u in tu if not 0.55 < u['ratio'] < 1.90])
ck('tutte le 10 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in tu))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('SEGMENTO: 11 prima · 10 qui · 10 dopo la 243 · 2 coppie + 6 singole · file %d/31' % len(righe))
print('parole EN %d -> IT %d · ratio %.2f - %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(u['ratio'] for u in tu), max(u['ratio'] for u in tu)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L305 superato' if not fail else 'verify L305 fallito')
raise SystemExit(0 if not fail else 1)
