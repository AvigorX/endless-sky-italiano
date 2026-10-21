r"""verify.py — L144 (`data/hai/unfettered 0 prologue.txt`, 20 unita', righe 367-420).

Invariante di **segmento**: 147 unita' nel file, **95 prima** della riga 367, **52 dopo** la 420 (contando la finestra),
confine alla riga **423**, che e' **ancora la stessa missione** (`Unfettered Jump Drive Trading`): la finestra finisce
dentro la scena.

Misure proprie: **2 token** con parita' per simbolo e per unita', **19 tab**, **12 virgolette**, **20 testi distinti**.
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
ck('idx 1..20 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 21)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 20 righe 367 - 420', len(tu) == 20 and (first, last) == (367, 420), (len(tu), first, last))
ck('95 unita prima della riga 367 (L140…L143)', db.execute(
    'select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0] == 95)
ck('147 unita nel file, 32 dopo la riga 420', db.execute(
    'select count(*) from units where path=?', (PATH,)).fetchone()[0] == 147
   and db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0] == 32)
ck('confine alla riga 423, ancora Jump Drive Trading (finestra dentro la scena)', db.execute(
    'select line,context from units where path=? and line>? order by line limit 1',
    (PATH, last)).fetchone() == (423, 'mission:Unfettered Jump Drive Trading'))
ck('tipi: 20 MISSION_TEXT', collections.Counter(u['kind'] for u in su) == {'MISSION_TEXT': 20})
ck('TRE asserzioni vuote: VALUE, LOGBOOK, UI_LABEL',
   [u['idx'] for u in su if u['kind'] in ('VALUE', 'LOGBOOK', 'UI_LABEL')] == [])
ck('2 token, parita 1 = 1 per simbolo',
   dict(collections.Counter(t for u in su for t in TAGS.findall(u['english'])))
   == {'<hood>': 1, '<learned>': 1})
ck('i token stanno nelle stesse unita (1 e 20) e nella stessa posizione',
   [u['idx'] for u in tu if TAGS.findall(u['italian'])] == [1, 20]
   and 'Slegato<hood>' in by[1]['italian'] and '. <learned>Sono Desneeparu' in by[20]['italian'])
ck('(No.) identico e (Sì.) tradotto',
   by[4]['italian'].lstrip('\t') == '(No.)' and by[5]['italian'].lstrip('\t') == '(Sì.)')
ck('tutte le unita di testo sono tradotte',
   not [u['idx'] for u in tu if u['idx'] != 4 and u['italian'].strip() == u['english'].strip()])
ck('tutte PENDING', not [u['idx'] for u in su
                         if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('spazi iniziali e finali identici al sorgente (20/20)',
   not [u['idx'] for u in tu
        if len(u['italian']) - len(u['italian'].rstrip()) != len(u['english']) - len(u['english'].rstrip())])
tabs = [u['idx'] for u in su if u['english'].startswith('\t')]
ck('19 unita con tab (la prima no)',
   len(tabs) == 19 and tabs == [u['idx'] for u in tu if u['italian'].startswith('\t')]
   and [u['idx'] for u in su if not u['english'].startswith('\t')] == [1], len(tabs))
ck('12 virgolette, stesse per unita',
   sum(u['english'].count('"') for u in su) == 12 == sum(u['italian'].count('"') for u in tu)
   and not [u['idx'] for u in tu if u['english'].count('"') != u['italian'].count('"')])
ck('nessuna unita dispari', [u['idx'] for u in su if u['english'].count('"') % 2] == [])
ck('1 contesto: 20 unita', list(collections.Counter(u['context'] for u in su).values()) == [20])
ck('20 testi inglesi distinti', len({u['english'] for u in tu}) == 20)
ck('i nomi restano: Desneeparu, Hai',
   all(t in ' '.join(u['italian'] for u in tu) for t in ('Desneeparu', 'Hai')))
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
ck('le tre parti ricostruiscono translation.json (1..20)',
   sorted(merged) == list(range(1, 21)) and merged == {u['idx']: u['italian'] for u in tu})
ck('nessun altro lotto rivendica le righe 367-420',
   not [f for f in os.listdir(os.path.join(L10N, 'staging/editorial'))
        if f.startswith('L') and os.path.exists(os.path.join(L10N, 'staging/editorial', f, 'translation.json'))
        and os.path.abspath(os.path.join(L10N, 'staging', 'editorial', f)) != HERE
        and any(u['path'] == PATH and first <= u['line'] <= last for u in json.load(open(os.path.join(
            L10N, 'staging', 'editorial', f, 'translation.json'), encoding='utf-8'))['units'])])
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('segmento: 115/147 unita del file (78,2%) · 95 prima / 32 dopo · finestra dentro Jump Drive Trading')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L144 superato' if not fail else 'verify L144 fallito')
raise SystemExit(0 if not fail else 1)
