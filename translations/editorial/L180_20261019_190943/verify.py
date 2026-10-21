r"""verify.py — L180 (`data/human/outfits.txt`, 12 unita', righe 15-146).

Invariante di **segmento**: il lotto **apre il file** (0 unita' prima della riga 15), 63 unita' nel file, **51 dopo** la
146; confine alla riga 158, tipo **`DESCRIPTION`** (`outfit:Small Radar Jammer`) — **misurato**.
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


ck('riga grezza identica al sorgente (12/12)', not [u for u in su if lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck('idx 1..12 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 13)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 12 righe 15 - 146', len(tu) == 12 and (first, last) == (15, 146), (len(tu), first, last))
ck('il lotto APRE il file: 0 unita prima della riga 15', db.execute(
    'select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0] == 0)
ck('63 unita nel file, 51 dopo la riga 146', db.execute(
    'select count(*) from units where path=?', (PATH,)).fetchone()[0] == 63
   and db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0] == 51)
ck('max(line) del file = 606, min(line) = 15', db.execute(
    'select min(line),max(line) from units where path=?', (PATH,)).fetchone() == (15, 606))
ck('confine alla riga 158, tipo DESCRIPTION (misurato)', db.execute(
    'select line,kind,context from units where path=? and line>? order by line limit 1',
    (PATH, last)).fetchone() == (158, 'DESCRIPTION', 'outfit:Small Radar Jammer'))
ck('tipi: 11 DESCRIPTION + 1 VALUE', collections.Counter(u['kind'] for u in su)
   == {'DESCRIPTION': 11, 'VALUE': 1})
ck('ZERO UI_LABEL, ZERO tab, ZERO virgolette, ZERO token',
   [u['idx'] for u in su if u['kind'] == 'UI_LABEL'] == []
   and [u['idx'] for u in su if '\t' in u['english']] == [] == [u['idx'] for u in tu if '\t' in u['italian']]
   and sum(u['english'].count('"') for u in su) == 0 == sum(u['italian'].count('"') for u in tu)
   and {t for u in su for t in TAGS.findall(u['english'])} == set())
ck('l VALUE e identico al sorgente', [u['idx'] for u in tu if u['kind'] == 'VALUE'
                                      and u['italian'] != u['english']] == [])
ck('1 apice inglese in idx 3; nessun possessivo inglese in italiano',
   sum(u['english'].count("'") for u in su) == 1 == by[3]['english'].count("'")
   and not [u['idx'] for u in tu if re.search(r"[A-Za-z]+'s\b", u['italian'])])
ck('12 testi distinti, 11 contesti (Cooling Ducts ha 2 unita)',
   len({u['english'] for u in tu}) == 12 and len({u['context'] for u in tu}) == 11)
ck('human space -> spazio umano', 'spazio umano' in by[10]['italian'])
ck('tutte PENDING', not [u['idx'] for u in su
                         if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('nessuno spazio finale', not [u['idx'] for u in tu
                                 if u['english'] != u['english'].rstrip() or u['italian'] != u['italian'].rstrip()])
ck('nessun carattere tipografico e nessun non latino',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')
        or any(ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F for c in u['italian'])])
rs = [u['ratio'] for u in tu if u['kind'] == 'DESCRIPTION']
ck('rapporto nel gate (solo DESCRIPTION)', 0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
merged = {}
for f in sorted(os.listdir(os.path.join(HERE, 'parts'))):
    if f.endswith('.json'):
        for k, v in json.load(open(os.path.join(HERE, 'parts', f), encoding='utf-8')).items():
            merged[int(k)] = v
ck('le parti ricostruiscono translation.json (1..12)',
   sorted(merged) == list(range(1, 13)) and merged == {u['idx']: u['italian'] for u in tu})
ck('nessun altro lotto rivendica le righe 15-146',
   not [f for f in os.listdir(os.path.join(L10N, 'staging/editorial'))
        if f.startswith('L') and os.path.exists(os.path.join(L10N, 'staging/editorial', f, 'translation.json'))
        and os.path.abspath(os.path.join(L10N, 'staging/editorial', f)) != HERE
        and any(u['path'] == PATH and first <= u['line'] <= last for u in json.load(open(os.path.join(
            L10N, 'staging/editorial', f, 'translation.json'), encoding='utf-8'))['units'])])
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('segmento: 12/63 unita del file (19,0%) · 0 prima / 12 nel lotto / 51 dopo · confine riga 158 (~DESCRIPTION)')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L180 superato' if not fail else 'verify L180 fallito')
raise SystemExit(0 if not fail else 1)
