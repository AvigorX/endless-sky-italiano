r"""verify.py — L279 (`data/human/kestrel.txt`, righe 56-164). **Secondo lotto del file**.

Verifica da sola: riga grezza, campi del DB, il **segmento** (16 prima, 33 qui, **2** dopo la 164), il **solo contesto**
`mission:Kestrel Testing`, i **32 tab** e le **94 virgolette** per unita', e che **nessun altro lotto** rivendichi queste
righe.

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
PATH = 'data/human/kestrel.txt'
TOK = {'<waypoints>': 1, '<first>': 1, '<last>': 1}
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


ck('riga grezza identica al sorgente (33/33)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = [u['idx'] for u in su
       if db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
       != (u['english'], u['kind'], u['path'], u['context'])]
ck('english/kind/path/context identici al DB', not bad, bad)
ck('33 unita, righe 56-164, tutte MISSION_TEXT',
   len(tu) == 33 and [u['line'] for u in tu] == sorted({u['line'] for u in tu})
   and {u['kind'] for u in tu} == {'MISSION_TEXT'}, (len(tu), {u['kind'] for u in tu}))
ck('un solo contesto: `mission:Kestrel Testing`',
   {u['context'] for u in tu} == {'mission:Kestrel Testing'}, {u['context'] for u in tu})
ck("16 unita' prima (L278)",
   db.execute('select count(*) from units where path=? and line<56', (PATH,)).fetchone()[0] == 16)
ck("2 unita' dopo la 164",
   db.execute('select count(*) from units where path=? and line>164', (PATH,)).fetchone()[0] == 2)
ck('confine: la 252 apre un contesto nuovo (`Kestrel Available`)',
   db.execute('select line,context from units where path=? and line>164 order by line limit 1', (PATH,)).fetchone()
   == (252, 'mission:Kestrel Available'))
ck('il file ha 51 unita, righe 15-402',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (51, 15, 402))
per_lotto, righe = [], set()
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    us = [u for u in json.load(open(f, encoding='utf-8'))['units'] if u['path'] == PATH]
    if us:
        per_lotto.append((os.path.basename(os.path.dirname(f)), len(us)))
        righe |= {u['line'] for u in us}
seg = {l for l in righe if 56 <= l <= 164}
ck('SEGMENTO: le 33 righe del lotto sono esattamente quelle 56-164',
   seg == {u['line'] for u in tu} and len(seg) == 33, (sorted(seg - {u['line'] for u in tu}), len(seg)))
overlap = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    if os.path.basename(os.path.dirname(f)) == os.path.basename(HERE):
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH and 56 <= u['line'] <= 164:
            overlap.append((os.path.basename(os.path.dirname(f)), u['line']))
ck('nessun altro lotto rivendica le righe 56-164', not overlap, overlap)
ck('copertura del SEGMENTO: 33/33 righe; il totale del file e stampato, non asserito',
   len(seg) == 33 and 51 - len(seg) == 18, '%d/51 (file)' % len(righe))
ck('tutte tradotte, nessuna copiata',
   not [u['idx'] for u in tu if u['italian'] == u['english']],
   [u['idx'] for u in tu if u['italian'] == u['english']])
ck('TAB: 32, e non rientrata solo la 4 (narrazione)',
   sum(u['english'].count(TAB) for u in tu) == 32 == sum(u['italian'].count(TAB) for u in tu)
   and [u['idx'] for u in tu if TAB not in u['italian']] == [4])
ck('VIRGOLETTE: 94 in tutto e lo stesso numero per ogni unita',
   sum(u['english'].count(QUOTE) for u in tu) == 94 == sum(u['italian'].count(QUOTE) for u in tu)
   and all(u['english'].count(QUOTE) == u['italian'].count(QUOTE) for u in tu))
ck('segnaposto per famiglia: 3 token, tre famiglie, identici',
   {t: sum(collections.Counter(TAG.findall(u['english']))[t] for u in tu) for t in TOK} == TOK
   == {t: sum(collections.Counter(TAG.findall(u['italian']))[t] for u in tu) for t in TOK})
ck('apici: 16 in inglese, 10 in italiano',
   sum(u['english'].count(APOS) for u in tu) == 16 and sum(u['italian'].count(APOS) for u in tu) == 10,
   (sum(u['english'].count(APOS) for u in tu), sum(u['italian'].count(APOS) for u in tu)))
ck('il nome scelto: `Kestrel` quattro volte, e vince nella scena finale',
   sum(1 for u in tu if u['italian'] == '\t"La Kestrel."') == 4
   and "'Kestrel'" in by[33]['italian'] and 'la Kestrel sarà in vendita' in by[33]['italian'])
ck('la regola del collaudo e il pagamento finale',
   'disabilitala senza distruggerla' in by[3]['italian']
   and 'due milioni di crediti' in by[33]['italian'])
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in tu for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90 per ogni unita',
   all(0.55 < u['ratio'] < 1.90 for u in tu),
   [(u['idx'], u['ratio']) for u in tu if not 0.55 < u['ratio'] < 1.90])
ck('tutte le 33 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in tu))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('SEGMENTO: 16 prima · 33 qui · 2 dopo · 1 contesto · 32 tab · 94 virgolette')
print('parole EN %d -> IT %d · ratio %.2f - %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(u['ratio'] for u in tu), max(u['ratio'] for u in tu)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L279 superato' if not fail else 'verify L279 fallito')
raise SystemExit(0 if not fail else 1)
