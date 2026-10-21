r"""verify.py — L140 (`data/hai/unfettered 0 prologue.txt`, 25 unita', righe 22-81).

Invariante di **segmento**: 147 unita' nel file, **zero prima** della riga 22, **122 dopo** la 81, confine alla riga
**83** (`mission:First Contact: Unfettered`, cioe' la stessa missione: la finestra finisce dentro la scena).

Misure proprie: **1 contesto**, **23 tab**, **50 virgolette**, **21 testi distinti**, il **motto degli Slegati** cinque
volte identico.
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
MOTTO = "Eravamo padroni di cento mondi quando le scimmie umane non avevano ancora imparato a usare i pollici."
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
ck('idx 1..25 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 26)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 25 righe 22 - 81', len(tu) == 25 and (first, last) == (22, 81), (len(tu), first, last))
ck('ZERO unita prima della riga 22 (il lotto apre il file)', db.execute(
    'select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0] == 0)
ck('147 unita nel file, 122 dopo la riga 81', db.execute(
    'select count(*) from units where path=?', (PATH,)).fetchone()[0] == 147
   and db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0] == 122)
ck('confine alla riga 83, stessa missione', db.execute(
    'select line,context from units where path=? and line>? order by line limit 1',
    (PATH, last)).fetchone() == (83, 'mission:First Contact: Unfettered'))
ck('tipi: 25 MISSION_TEXT', collections.Counter(u['kind'] for u in su) == {'MISSION_TEXT': 25})
ck('ZERO VALUE, ZERO UI_LABEL, ZERO token (tre asserzioni vuote)',
   [u['idx'] for u in su if u['kind'] in ('VALUE', 'UI_LABEL')] == []
   and collections.Counter(t for u in su for t in TAGS.findall(u['english'])) == {})
ck('tutte le unita sono tradotte',
   not [u['idx'] for u in tu if u['italian'].strip() == u['english'].strip()])
ck('tutte PENDING', not [u['idx'] for u in su
                         if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('spazi iniziali e finali identici al sorgente (25/25)',
   not [u['idx'] for u in tu
        if len(u['italian']) - len(u['italian'].rstrip()) != len(u['english']) - len(u['english'].rstrip())])
tabs = [u['idx'] for u in su if u['english'].startswith('\t')]
ck('23 unita con tab iniziale, le stesse in traduzione (senza tab: 1 e 8)',
   len(tabs) == 23 and tabs == [u['idx'] for u in tu if u['italian'].startswith('\t')]
   and [u['idx'] for u in su if not u['english'].startswith('\t')] == [1, 8], len(tabs))
ck('50 virgolette, stesse per unita, sei unita con quattro',
   sum(u['english'].count('"') for u in su) == 50 == sum(u['italian'].count('"') for u in tu)
   and not [u['idx'] for u in tu if u['english'].count('"') != u['italian'].count('"')]
   and [u['idx'] for u in tu if u['italian'].count('"') == 4] == [4, 11, 19, 20, 22, 23])
ck('nessuna unita dispari', [u['idx'] for u in su if u['english'].count('"') % 2] == [])
ck('1 contesto: mission:First Contact: Unfettered, 25 unita',
   list(collections.Counter(u['context'] for u in su).items()) == [('mission:First Contact: Unfettered', 25)])
ck('21 testi inglesi distinti su 25 unita', len({u['english'] for u in tu}) == 21,
   len({u['english'] for u in tu}))
ck('le scelte ripetute hanno la stessa resa (2-9, 3-10)',
   by[2]['italian'].lstrip('\t') == by[9]['italian'].lstrip('\t') == '(Certo.)'
   and by[3]['italian'] == by[10]['italian'])
ck('la battuta sull\'estinzione ha la stessa resa (18 e 21)', by[18]['italian'] == by[21]['italian'])
ck('il motto degli Slegati compare 5 volte identico',
   ' '.join(u['italian'] for u in tu).count(MOTTO) == 5)
ck('monkey reso «scimmia», mai «scimmie umane» al singolare sbagliato',
   'scimmia' in ' '.join(u['italian'] for u in tu) and 'la scimmia è curiosa' in ' '.join(u['italian'] for u in tu))
ck('nessun carattere non latino, nessun carattere tipografico',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')
        or any(ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F for c in u['italian'])])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate', 0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
merged = {}
for f in sorted(os.listdir(os.path.join(HERE, 'parts'))):
    if f.endswith('.json'):
        for k, v in json.load(open(os.path.join(HERE, 'parts', f), encoding='utf-8')).items():
            merged[int(k)] = v
ck('le tre parti ricostruiscono translation.json (1..25)',
   sorted(merged) == list(range(1, 26)) and merged == {u['idx']: u['italian'] for u in tu})
ck('nessun altro lotto rivendica le righe 22-81', not [f for f in os.listdir(os.path.join(L10N, 'staging/editorial'))
    if f.startswith('L') and os.path.exists(os.path.join(L10N, 'staging/editorial', f, 'translation.json'))
    and os.path.abspath(os.path.join(L10N, 'staging', 'editorial', f)) != HERE
    and any(u['path'] == PATH and first <= u['line'] <= last for u in json.load(open(os.path.join(
        L10N, 'staging', 'editorial', f, 'translation.json'), encoding='utf-8'))['units'])])
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('segmento: 25/147 unita del file (17,0%) · 0 prima / 122 dopo · confine riga 83 (stessa missione)')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L140 superato' if not fail else 'verify L140 fallito')
raise SystemExit(0 if not fail else 1)
