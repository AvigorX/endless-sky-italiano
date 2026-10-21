r"""verify.py — L278 (`data/human/kestrel.txt`, righe 15-54). **Primo lotto del file**.

Verifica da sola: riga grezza, campi del DB, il **segmento** (0 prima — apre il file — 16 qui, **35** dopo la 54), il **solo
contesto** `mission:Kestrel Testing`, i **13 tab** e le **42 virgolette** per unita', il `VALUE` copiato, e che **nessun altro
lotto** rivendichi queste righe.

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
TOK = {'<waypoints>': 1, '<first>': 2, '<last>': 2}
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


ck('riga grezza identica al sorgente (16/16)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = [u['idx'] for u in su
       if db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
       != (u['english'], u['kind'], u['path'], u['context'])]
ck('english/kind/path/context identici al DB', not bad, bad)
ck('16 unita, righe 15-54, 14 MISSION_TEXT + 1 DESCRIPTION + 1 VALUE',
   len(tu) == 16 and [u['line'] for u in tu] == sorted({u['line'] for u in tu})
   and collections.Counter(u['kind'] for u in tu) == {'MISSION_TEXT': 14, 'DESCRIPTION': 1, 'VALUE': 1},
   (len(tu), collections.Counter(u['kind'] for u in tu)))
ck('un solo contesto: `mission:Kestrel Testing`',
   {u['context'] for u in tu} == {'mission:Kestrel Testing'},
   {u['context'] for u in tu})
ck("ZERO unita' prima della 15: il lotto APRE il file",
   db.execute('select count(*) from units where path=? and line<15', (PATH,)).fetchone()[0] == 0)
ck("35 unita' dopo la 54",
   db.execute('select count(*) from units where path=? and line>54', (PATH,)).fetchone()[0] == 35)
ck('confine: la 56 resta in `Kestrel Testing` (stessa missione, non un cambio)',
   db.execute('select line,context from units where path=? and line>54 order by line limit 1', (PATH,)).fetchone()
   == (56, 'mission:Kestrel Testing'))
ck('il file ha 51 unita, righe 15-402',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (51, 15, 402))
per_lotto, righe = [], set()
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    us = [u for u in json.load(open(f, encoding='utf-8'))['units'] if u['path'] == PATH]
    if us:
        per_lotto.append((os.path.basename(os.path.dirname(f)), len(us)))
        righe |= {u['line'] for u in us}
seg = {l for l in righe if 15 <= l <= 54}
ck('SEGMENTO: le 16 righe del lotto sono esattamente quelle 15-54',
   seg == {u['line'] for u in tu} and len(seg) == 16, (sorted(seg - {u['line'] for u in tu}), len(seg)))
overlap = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    if os.path.basename(os.path.dirname(f)) == os.path.basename(HERE):
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH and 15 <= u['line'] <= 54:
            overlap.append((os.path.basename(os.path.dirname(f)), u['line']))
ck('nessun altro lotto rivendica le righe 15-54', not overlap, overlap)
ck('copertura del SEGMENTO: 16/16 righe; il totale del file e stampato, non asserito',
   len(seg) == 16 and 51 - len(seg) == 35, '%d/51 (file)' % len(righe))
ck('il VALUE e copiato; le altre 15 unita sono tradotte',
   all(u['italian'] == u['english'] for u in tu if u['kind'] == 'VALUE')
   and all(u['italian'] != u['english'] for u in tu if u['kind'] != 'VALUE'))
ck('TAB: tredici, sulle stesse unita, primi caratteri in entrambe le lingue',
   sum(u['english'].count(TAB) for u in tu) == 13 == sum(u['italian'].count(TAB) for u in tu)
   and [u['idx'] for u in tu if TAB in u['italian']] == [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
   and all(u['italian'].startswith(TAB) for u in tu if TAB in u['italian']))
ck('VIRGOLETTE: 42 in tutto e lo stesso numero per ogni unita',
   sum(u['english'].count(QUOTE) for u in tu) == 42 == sum(u['italian'].count(QUOTE) for u in tu)
   and all(u['english'].count(QUOTE) == u['italian'].count(QUOTE) for u in tu))
ck('segnaposto per famiglia: 5 token, tre famiglie, identici in inglese e italiano',
   {t: sum(collections.Counter(TAG.findall(u['english']))[t] for u in tu) for t in TOK} == TOK
   == {t: sum(collections.Counter(TAG.findall(u['italian']))[t] for u in tu) for t in TOK})
ck('apici: 4 in inglese, 9 in italiano',
   sum(u['english'].count(APOS) for u in tu) == 4 and sum(u['italian'].count(APOS) for u in tu) == 9,
   (sum(u['english'].count(APOS) for u in tu), sum(u['italian'].count(APOS) for u in tu)))
ck('la DESCRIPTION distingue disabilitare da distruggere',
   'disabilitare' in by[2]['italian'] and 'Non distruggere' in by[2]['italian'])
ck('nomi propri invariati: Tarazed, Wayfarer, Charles Atinoda',
   all(n in ' '.join(u['italian'] for u in tu) for n in ('Tarazed', 'Wayfarer', 'Charles Atinoda')))
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in tu for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90 per le 15 unita tradotte',
   all(0.55 < u['ratio'] < 1.90 for u in tu if u['kind'] != 'VALUE'),
   [(u['idx'], u['ratio']) for u in tu if u['kind'] != 'VALUE' and not 0.55 < u['ratio'] < 1.90])
ck('tutte le 16 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in tu))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('SEGMENTO: 0 prima (apre il file) · 16 qui · 35 dopo · 1 contesto · 13 tab · 42 virgolette')
print('parole EN %d -> IT %d · ratio %.2f - %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(u['ratio'] for u in tu if u['kind'] != 'VALUE'), max(u['ratio'] for u in tu if u['kind'] != 'VALUE')))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L278 superato' if not fail else 'verify L278 fallito')
raise SystemExit(0 if not fail else 1)
