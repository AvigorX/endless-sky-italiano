r"""verify.py — L165 (`data/avgi/avgi outfits.txt`, 13 unita', righe 429-600).

Invariante di **segmento**: 63 unita' nel file, **44 prima** della riga 429 (L161…L164), **6 dopo** la 600, confine
alla riga 616 (`DESCRIPTION` di `outfit:Optical Laser Rifle`). Misure proprie: 4 `VALUE`, 2 virgolette, 2 tab.
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
PATH = 'data/avgi/avgi outfits.txt'
TAGS = re.compile(r'<[^<>]+>')
su = sorted(json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
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
ck('unita: 13 righe 429 - 600', len(tu) == 13 and (first, last) == (429, 600), (len(tu), first, last))
ck('44 unita prima della riga 429 (L161…L164)', db.execute(
    'select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0] == 44)
ck('63 unita nel file, 6 dopo la riga 600', db.execute(
    'select count(*) from units where path=?', (PATH,)).fetchone()[0] == 63
   and db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0] == 6)
ck('confine alla riga 616 (DESCRIPTION di Optical Laser Rifle)', db.execute(
    'select line,kind,context from units where path=? and line>? order by line limit 1',
    (PATH, last)).fetchone() == (616, 'DESCRIPTION', 'outfit:Optical Laser Rifle'))
ck('tipi: 9 DESCRIPTION + 4 VALUE', collections.Counter(u['kind'] for u in su)
   == {'DESCRIPTION': 9, 'VALUE': 4})
ck('ZERO UI_LABEL, ZERO token', [u['idx'] for u in su if u['kind'] == 'UI_LABEL'] == []
   and [u['idx'] for u in tu for t in TAGS.findall(u['italian'])] == [])
ck('i 4 VALUE sono identici al sorgente',
   [u['italian'] for u in tu if u['kind'] == 'VALUE'] == ['Z-999 "Arc" Fusion Torches', 'R-180 RCS Thrusters',
                                                         'R-360 RCS Thrusters', 'R-720 RCS Thrusters'])
ck('2 virgolette nel lotto, in idx 1',
   sum(u['english'].count('"') for u in su) == 2 == sum(u['italian'].count('"') for u in tu)
   and [u['idx'] for u in su if u['english'].count('"')] == [1]
   == [u['idx'] for u in tu if u['italian'].count('"')])
ck('2 unita con tab: idx 3 e 5, le stesse in traduzione',
   [u['idx'] for u in su if u['english'].startswith('\t')] == [3, 5]
   == [u['idx'] for u in tu if u['italian'].startswith('\t')])
ck('13 testi distinti, 6 contesti distinti',
   len({u['english'] for u in tu}) == 13 and len({u['context'] for u in tu}) == 6)
ck('tutte PENDING', not [u['idx'] for u in su
                         if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('spazi iniziali e finali identici al sorgente (13/13)',
   not [u['idx'] for u in tu
        if len(u['italian']) - len(u['italian'].rstrip()) != len(u['english']) - len(u['english'].rstrip())
        or len(u['italian']) - len(u['italian'].lstrip()) != len(u['english']) - len(u['english'].lstrip())])
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
ck('le parti ricostruiscono translation.json (1..13)',
   sorted(merged) == list(range(1, 14)) and merged == {u['idx']: u['italian'] for u in tu})
ck('nessun altro lotto rivendica le righe 429-600',
   not [f for f in os.listdir(os.path.join(L10N, 'staging/editorial'))
        if f.startswith('L') and os.path.exists(os.path.join(L10N, 'staging/editorial', f, 'translation.json'))
        and os.path.abspath(os.path.join(L10N, 'staging/editorial', f)) != HERE
        and any(u['path'] == PATH and first <= u['line'] <= last for u in json.load(open(os.path.join(
            L10N, 'staging/editorial', f, 'translation.json'), encoding='utf-8'))['units'])])
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('segmento: 57/63 unita del file (90,5%) · 44 prima / 13 nel lotto / 6 dopo · confine riga 616')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L165 superato' if not fail else 'verify L165 fallito')
raise SystemExit(0 if not fail else 1)
