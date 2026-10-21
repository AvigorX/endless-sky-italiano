r"""verify.py — L185 (`data/gegno/gegno outfits.txt`, 13 unita', righe 17-157). Apre il file.

Invariante di **segmento**: 0 unita' prima della riga 17 (il lotto apre il file), 60 nel file, **47 dopo**; confine alla
riga 179, tipo **`DESCRIPTION`** (`outfit:RG15 Torch Thruster`), misurato.
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
PATH = 'data/gegno/gegno outfits.txt'
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


ck('riga grezza identica al sorgente (13/13)', not [u for u in su if lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck('idx 1..13 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 14)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 13 righe 17 - 157', len(tu) == 13 and (first, last) == (17, 157), (len(tu), first, last))
ck('il lotto APRE il file: 0 unita prima della riga 17',
   db.execute('select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0] == 0)
ck('60 unita nel file, 47 dopo la riga 157', db.execute(
    'select count(*) from units where path=?', (PATH,)).fetchone()[0] == 60
   and db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0] == 47)
ck('max(line) del file = 1137, min(line) = 17', db.execute(
    'select min(line),max(line) from units where path=?', (PATH,)).fetchone() == (17, 1137))
ck('confine alla riga 179, tipo DESCRIPTION (misurato)', db.execute(
    'select line,kind,context from units where path=? and line>? order by line limit 1',
    (PATH, last)).fetchone() == (179, 'DESCRIPTION', 'outfit:RG15 Torch Thruster'))
ck('tipi: 9 DESCRIPTION + 4 VALUE', collections.Counter(u['kind'] for u in su)
   == {'DESCRIPTION': 9, 'VALUE': 4})
ck('i 4 VALUE identici al sorgente (plurali)', {u['idx']: u['italian'] for u in tu if u['kind'] == 'VALUE'}
   == {1: 'R01 Skirmish Batteries', 3: 'R02 Battlezone Batteries', 5: 'R03 Warforge Batteries',
       7: 'R04 Crusade Batteries'})
ck('ZERO tab, ZERO virgolette, ZERO token, ZERO UI_LABEL',
   [u['idx'] for u in su if u['kind'] == 'UI_LABEL'] == []
   and [u['idx'] for u in su if '\t' in u['english']] == [] == [u['idx'] for u in tu if '\t' in u['italian']]
   and sum(u['english'].count('"') for u in su) == 0 == sum(u['italian'].count('"') for u in tu)
   and {t for u in su for t in TAGS.findall(u['english'])} == set())
ck("5 apici inglesi (3 `Gegno's` + `It's` + `Halite's`), nessun possessivo in italiano",
   sum(u['english'].count("'") for u in su) == 5
   and {u['idx']: u['english'].count("'") for u in su if "'" in u['english']} == {4: 1, 9: 1, 11: 1, 12: 1, 13: 1}
   and not [u['idx'] for u in tu if re.search(r"\b[A-Za-z]+'s\b", u['italian'])])
ck('13 testi distinti, 9 contesti (quattro con 2 unita)',
   len({u['english'] for u in tu}) == 13 and len({u['context'] for u in tu}) == 9
   and sorted(collections.Counter(u['context'] for u in tu).values()) == [1] * 5 + [2, 2, 2, 2])
EN_ALL = ' '.join(u['english'] for u in tu)
CODES = ('R01', 'R02', 'R03', 'R04', 'C3', 'C7', 'C17', 'C27', 'I70')
IT_ALL = ' '.join(u['italian'] for u in tu)
ck('i codici presenti nel testo inglese restano invariati (C17 e C27 vivono solo nei contesti)',
   all(c in IT_ALL for c in CODES if c in EN_ALL)
   and not [c for c in CODES if c in EN_ALL and c not in IT_ALL],
   [c for c in CODES if c in EN_ALL and c not in IT_ALL])
ck('tutte PENDING', not [u['idx'] for u in su
                         if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('nessuno spazio finale', not [u['idx'] for u in tu
                                 if u['english'] != u['english'].rstrip() or u['italian'] != u['italian'].rstrip()])
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
ck('le parti ricostruiscono translation.json (1..13)',
   sorted(merged) == list(range(1, 14)) and merged == {u['idx']: u['italian'] for u in tu})
ck('nessun altro lotto rivendica le righe 17-157',
   not [f for f in os.listdir(os.path.join(L10N, 'staging/editorial'))
        if f.startswith('L') and os.path.exists(os.path.join(L10N, 'staging/editorial', f, 'translation.json'))
        and os.path.abspath(os.path.join(L10N, 'staging/editorial', f)) != HERE
        and any(u['path'] == PATH and first <= u['line'] <= last for u in json.load(open(os.path.join(
            L10N, 'staging/editorial', f, 'translation.json'), encoding='utf-8'))['units'])])
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('segmento: 13/60 unita del file (21,7%) · 0 prima / 13 nel lotto / 47 dopo · confine riga 179 (~DESCRIPTION)')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L185 superato' if not fail else 'verify L185 fallito')
raise SystemExit(0 if not fail else 1)
