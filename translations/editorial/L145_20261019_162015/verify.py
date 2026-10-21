r"""verify.py — L145 (`data/hai/unfettered 0 prologue.txt`, 13 unita', righe 423-459).

Invariante di **segmento**: 147 unita' nel file, **115 prima** della riga 423, **19 dopo** la 459, confine alla riga
**460**, che e' **ancora la stessa missione** (`Unfettered Jump Drive Trading`).

Misure proprie: **1 `LOGBOOK`**, **3 token** (uno dei quali `<The engineer>`, confrontato **esatto**), **2 virgolette
dispari** lasciate aperte (12, 13), **12 tab**, **20 virgolette**.
"""
import collections
import hashlib
import json
import os
import re
import sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
ROOT = os.path.abspath(os.path.join(L10N, '..'))
PATH = 'data/hai/unfettered 0 prologue.txt'
TAGS = re.compile(r'<[^<>]+>')
su = sorted(json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
by = {u['idx']: u for u in tu}
lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
fail = []


def ck(n, c, d=''):
    print('%-70s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente', not [u for u in su if lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck('idx 1..13 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 14)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 13 righe 423 - 459', len(tu) == 13 and (first, last) == (423, 459), (len(tu), first, last))
ck('115 unita prima della riga 423 (L140…L144)', db.execute(
    'select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0] == 115)
ck('147 unita nel file, 19 dopo la riga 459', db.execute(
    'select count(*) from units where path=?', (PATH,)).fetchone()[0] == 147
   and db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0] == 19)
ck('confine alla riga 460, ancora Jump Drive Trading (finestra dentro la scena)', db.execute(
    'select line,context from units where path=? and line>? order by line limit 1',
    (PATH, last)).fetchone() == (460, 'mission:Unfettered Jump Drive Trading'))
ck('tipi: 12 MISSION_TEXT + 1 LOGBOOK',
   collections.Counter(u['kind'] for u in su) == {'MISSION_TEXT': 12, 'LOGBOOK': 1})
ck('il LOGBOOK e tradotto (non identico all inglese)',
   [u['idx'] for u in tu if u['kind'] == 'LOGBOOK'] == [3]
   and by[3]['italian'].strip() != by[3]['english'].strip())
ck('ZERO VALUE e ZERO UI_LABEL (due asserzioni vuote)',
   [u['idx'] for u in su if u['kind'] in ('VALUE', 'UI_LABEL')] == [])
ck('3 token, parita 1 = 1 per simbolo',
   dict(collections.Counter(t for u in su for t in TAGS.findall(u['english'])))
   == {'<learned>': 1, '<last>': 1, '<The engineer>': 1})
ck('i token stanno nelle stesse unita e nella stessa posizione',
   [u['idx'] for u in tu if TAGS.findall(u['italian'])] == [2, 5]
   and '<The engineer> ti conduce' in by[5]['italian'] and 'lama! <learned>Sono' in by[2]['italian']
   and 'capitano <last>!' in by[2]['italian'])
ck('<The engineer> esatto: nessuna variante minuscola', '<the engineer>' not in by[5]['italian'])
ck('2 virgolette dispari in inglese e in italiano, le stesse unita (12, 13)',
   [u['idx'] for u in su if u['english'].count('"') % 2] == [12, 13]
   and [u['idx'] for u in tu if u['italian'].count('"') % 2] == [12, 13])
ck('le dispari restano aperte: nessuna virgoletta finale aggiunta',
   not [u['idx'] for u in tu if u['idx'] in (12, 13) and u['italian'].rstrip().endswith('"')])
ck('tutte le unita di testo sono tradotte',
   not [u['idx'] for u in tu if u['italian'].strip() == u['english'].strip()])
ck('tutte PENDING', not [u['idx'] for u in su
                         if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('spazi iniziali e finali identici al sorgente (13/13)',
   not [u['idx'] for u in tu
        if len(u['italian']) - len(u['italian'].rstrip()) != len(u['english']) - len(u['english'].rstrip())])
tabs = [u['idx'] for u in su if u['english'].startswith('\t')]
ck('12 unita con tab (il LOGBOOK no)',
   len(tabs) == 12 and tabs == [u['idx'] for u in tu if u['italian'].startswith('\t')]
   and [u['idx'] for u in su if not u['english'].startswith('\t')] == [3], len(tabs))
ck('20 virgolette, stesse per unita',
   sum(u['english'].count('"') for u in su) == 20 == sum(u['italian'].count('"') for u in tu)
   and not [u['idx'] for u in tu if u['english'].count('"') != u['italian'].count('"')])
ck('1 contesto: 13 unita', list(collections.Counter(u['context'] for u in su).values()) == [13])
ck('13 testi inglesi distinti', len({u['english'] for u in tu}) == 13)
ck('i nomi restano inglesi: 5 nomi',
   all(n in ' '.join(u['italian'] for u in tu)
       for n in ('Tripulse Shredder', 'Blaster', 'Ion Cannon', 'Shield Beetle', 'Firelode')))
ck('nessun carattere tipografico e nessun non latino fuori dai token',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')
        or any(ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F for c in TAGS.sub('', u['italian']))])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate', 0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
merged = {}
for f in sorted(os.listdir(os.path.join(HERE, 'parts'))):
    if f.endswith('.json'):
        for k, v in json.load(open(os.path.join(HERE, 'parts', f), encoding='utf-8')).items():
            merged[int(k)] = v
ck('le tre parti ricostruiscono translation.json (1..13)',
   sorted(merged) == list(range(1, 14)) and merged == {u['idx']: u['italian'] for u in tu})
ck('nessun altro lotto rivendica le righe 423-459',
   not [f for f in os.listdir(os.path.join(L10N, 'staging/editorial'))
        if f.startswith('L') and os.path.exists(os.path.join(L10N, 'staging/editorial', f, 'translation.json'))
        and os.path.abspath(os.path.join(L10N, 'staging', 'editorial', f)) != HERE
        and any(u['path'] == PATH and first <= u['line'] <= last for u in json.load(open(os.path.join(
            L10N, 'staging', 'editorial', f, 'translation.json'), encoding='utf-8'))['units'])])
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('segmento: 128/147 unita del file (87,1%) · 115 prima / 19 dopo · finestra dentro Jump Drive Trading')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L145 superato' if not fail else 'verify L145 fallito')
raise SystemExit(0 if not fail else 1)
