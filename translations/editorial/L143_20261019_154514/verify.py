r"""verify.py — L143 (`data/hai/unfettered 0 prologue.txt`, 30 unita', righe 214-317). Due missioni intere.

Invariante di **segmento**: 147 unita' nel file, **65 prima** della riga 214, **52 dopo** la 317, confine alla riga
**367** (cambio di missione verso `Unfettered Jump Drive Trading`). Le due missioni coperte si chiudono entrambe
(12/12 e 18/18).
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
ck('idx 1..30 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 31)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 30 righe 214 - 317', len(tu) == 30 and (first, last) == (214, 317), (len(tu), first, last))
ck('65 unita prima della riga 214 (L140 + L141 + L142)', db.execute(
    'select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0] == 65)
ck('147 unita nel file, 52 dopo la riga 317', db.execute(
    'select count(*) from units where path=?', (PATH,)).fetchone()[0] == 147
   and db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0] == 52)
ck('confine alla riga 367: cambio di missione verso Unfettered Jump Drive Trading', db.execute(
    'select line,context from units where path=? and line>? order by line limit 1',
    (PATH, last)).fetchone() == (367, 'mission:Unfettered Jump Drive Trading'))
ck('le due missioni sono chiuse: Jump Drive 2 12/12, Jump Drive 3 18/18',
   db.execute('select count(*) from units where path=? and context=?',
              (PATH, 'mission:Unfettered Jump Drive 2')).fetchone()[0] == 12
   and db.execute('select count(*) from units where path=? and context=?',
                  (PATH, 'mission:Unfettered Jump Drive 3')).fetchone()[0] == 18)
ck('tipi: 28 MISSION_TEXT, 1 VALUE, 1 DESCRIPTION',
   collections.Counter(u['kind'] for u in su) == {'MISSION_TEXT': 28, 'VALUE': 1, 'DESCRIPTION': 1})
ck('ZERO UI_LABEL, ZERO token (due asserzioni vuote)',
   [u['idx'] for u in su if u['kind'] == 'UI_LABEL'] == []
   and collections.Counter(t for u in su for t in TAGS.findall(u['english'])) == {})
ck('il VALUE e identico al sorgente e ripete quello di L142',
   [u['italian'] for u in tu if u['kind'] == 'VALUE'] == ['More Jump Drives'])
ck('(No.) identico due volte, (Sì.) tradotto due volte',
   by[4]['italian'].lstrip('\t') == by[14]['italian'].lstrip('\t') == '(No.)'
   and by[5]['italian'].lstrip('\t') == by[15]['italian'].lstrip('\t') == '(Sì.)')
ck('tutte le unita di testo sono tradotte',
   not [u['idx'] for u in tu
        if u['kind'] != 'VALUE' and u['idx'] not in (4, 14) and u['italian'].strip() == u['english'].strip()])
ck('tutte PENDING', not [u['idx'] for u in su
                         if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('spazi iniziali e finali identici al sorgente (30/30)',
   not [u['idx'] for u in tu
        if len(u['italian']) - len(u['italian'].rstrip()) != len(u['english']) - len(u['english'].rstrip())])
tabs = [u['idx'] for u in su if u['english'].startswith('\t')]
ck('26 unita con tab (senza: 1, 2, 3, 13)',
   len(tabs) == 26 and tabs == [u['idx'] for u in tu if u['italian'].startswith('\t')]
   and [u['idx'] for u in su if not u['english'].startswith('\t')] == [1, 2, 3, 13], len(tabs))
ck('46 virgolette, stesse per unita',
   sum(u['english'].count('"') for u in su) == 46 == sum(u['italian'].count('"') for u in tu)
   and not [u['idx'] for u in tu if u['english'].count('"') != u['italian'].count('"')])
ck('nessuna unita dispari', [u['idx'] for u in su if u['english'].count('"') % 2] == [])
ck('2 contesti con le cardinalita attese',
   [(c, len([u for u in su if u['context'] == c])) for c in ('mission:Unfettered Jump Drive 2',
    'mission:Unfettered Jump Drive 3')] == [('mission:Unfettered Jump Drive 2', 12),
                                           ('mission:Unfettered Jump Drive 3', 18)])
ck('28 testi inglesi distinti', len({u['english'] for u in tu}) == 28)
ck('i nomi restano: Wanderer, Hai',
   all(t in ' '.join(u['italian'] for u in tu) for t in ('Wanderer', 'Hai')))
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
ck('le quattro parti ricostruiscono translation.json (1..30)',
   sorted(merged) == list(range(1, 31)) and merged == {u['idx']: u['italian'] for u in tu})
ck('nessun altro lotto rivendica le righe 214-317',
   not [f for f in os.listdir(os.path.join(L10N, 'staging/editorial'))
        if f.startswith('L') and os.path.exists(os.path.join(L10N, 'staging/editorial', f, 'translation.json'))
        and os.path.abspath(os.path.join(L10N, 'staging', 'editorial', f)) != HERE
        and any(u['path'] == PATH and first <= u['line'] <= last for u in json.load(open(os.path.join(
            L10N, 'staging', 'editorial', f, 'translation.json'), encoding='utf-8'))['units'])])
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('segmento: 95/147 unita del file (64,6%) · 65 prima / 52 dopo · due missioni chiuse (12/12, 18/18)')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L143 superato' if not fail else 'verify L143 fallito')
raise SystemExit(0 if not fail else 1)
