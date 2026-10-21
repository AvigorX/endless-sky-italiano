r"""verify.py — L181 (`data/human/outfits.txt`, 9 unita', righe 158-233).

Invariante di **segmento**: 12 unita' prima (L180), 9 nel lotto, **42 dopo** (63 - 12 - 9); confine alla riga 236, tipo
**`VALUE`** (`outfit:Jump Drive (Broken)`) — **misurato**, non ereditato da L180 (dove era una `DESCRIPTION`).
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
PATH = 'data/human/outfits.txt'
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


ck('riga grezza identica al sorgente (9/9)', not [u for u in su if lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck('idx 1..9 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 10)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 9 righe 158 - 233', len(tu) == 9 and (first, last) == (158, 233), (len(tu), first, last))
ck('12 unita prima (chiuse da L180)', db.execute(
    'select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0] == 12)
ck('63 unita nel file, 42 dopo la riga 233 (63 - 12 - 9)', db.execute(
    'select count(*) from units where path=?', (PATH,)).fetchone()[0] == 63
   and db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0] == 42)
ck('confine alla riga 236, tipo VALUE (misurato: non e\' una DESCRIPTION come in L180)', db.execute(
    'select line,kind,context from units where path=? and line>? order by line limit 1',
    (PATH, last)).fetchone() == (236, 'VALUE', 'outfit:Jump Drive (Broken)'))
ck('tipi: 9 DESCRIPTION, zero VALUE, zero UI_LABEL',
   collections.Counter(u['kind'] for u in su) == {'DESCRIPTION': 9})
ck('2 tab (idx 4 e 7), ZERO virgolette, ZERO token',
   [u['idx'] for u in su if u['english'].startswith('\t')] == [4, 7]
   == [u['idx'] for u in tu if u['italian'].startswith('\t')]
   and sum(u['english'].count('"') for u in su) == 0 == sum(u['italian'].count('"') for u in tu)
   and {t for u in su for t in TAGS.findall(u['english'])} == set())
ck('1 apice inglese in idx 2; nessun possessivo inglese in italiano',
   sum(u['english'].count("'") for u in su) == 1 == by[2]['english'].count("'")
   and not [u['idx'] for u in tu if re.search(r"[A-Za-z]+'s\b", u['italian'])])
ck('9 testi distinti, 7 contesti (Ramscoop e Hyperdrive con 2 unita)',
   len({u['english'] for u in tu}) == 9 and len({u['context'] for u in tu}) == 7)
ck('nomi tecnici invariati: Sidewinders, ramscoop, scram drive, jump drive, Free Worlds, Deep',
   all(n in ' '.join(u['italian'] for u in tu) for n in
       ('Sidewinders', 'ramscoop', 'scram drive', 'jump drive', 'Free Worlds', 'Deep')))
ck('iperguida per hyperdrive (idx 7), e idx 6 non nomina l\'iperguida (ne\' in EN ne\' in IT)',
   'iperguida' in by[7]['italian'] and 'hyperdrive' not in by[7]['italian']
   and 'hyperdrive' not in by[6]['english'] and 'iperguida' not in by[6]['italian'])
ck('tutte PENDING', not [u['idx'] for u in su
                         if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('nessuno spazio finale (tab iniziale ammesso)',
   not [u['idx'] for u in tu if u['english'].rstrip('\t') != u['english'].rstrip('\t').rstrip()
        or u['italian'].rstrip('\t') != u['italian'].rstrip('\t').rstrip()])
ck('nessun carattere tipografico e nessun non latino',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')
        or any(ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F for c in u['italian'])])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate', 0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
merged = {}
for f in sorted(os.listdir(os.path.join(HERE, 'parts'))):
    if f.endswith('.json'):
        for k, v in json.load(open(os.path.join(HERE, 'parts', f), encoding='utf-8')).items():
            merged[int(k)] = v
ck('le parti ricostruiscono translation.json (1..9)',
   sorted(merged) == list(range(1, 10)) and merged == {u['idx']: u['italian'] for u in tu})
ck('nessun altro lotto rivendica le righe 158-233',
   not [f for f in os.listdir(os.path.join(L10N, 'staging/editorial'))
        if f.startswith('L') and os.path.exists(os.path.join(L10N, 'staging/editorial', f, 'translation.json'))
        and os.path.abspath(os.path.join(L10N, 'staging/editorial', f)) != HERE
        and any(u['path'] == PATH and first <= u['line'] <= last for u in json.load(open(os.path.join(
            L10N, 'staging/editorial', f, 'translation.json'), encoding='utf-8'))['units'])])
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('segmento: 21/63 unita del file (33,3%) · 12 prima / 9 nel lotto / 42 dopo · confine riga 236 (~VALUE)')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L181 superato' if not fail else 'verify L181 fallito')
raise SystemExit(0 if not fail else 1)
