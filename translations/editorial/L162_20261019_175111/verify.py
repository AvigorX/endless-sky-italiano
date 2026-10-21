r"""verify.py — L162 (`data/avgi/avgi outfits.txt`, 10 unita', righe 112-193).

Invariante di **segmento**: 63 unita' nel file, **11 prima** della riga 112 (L161), **42 dopo** la 193, confine alla
riga 209 (`DESCRIPTION` di `outfit:Concentrating Solar Cell`). Misure proprie: 4 tab, zero token, 10 testi distinti.
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
by = {u['idx']: u for u in tu}
lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
fail = []


def ck(n, c, d=''):
    print('%-70s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente (10/10)', not [u for u in su if lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck('idx 1..10 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 11)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 10 righe 112 - 193', len(tu) == 10 and (first, last) == (112, 193), (len(tu), first, last))
ck('11 unita prima della riga 112 (L161)', db.execute(
    'select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0] == 11)
ck('63 unita nel file, 42 dopo la riga 193', db.execute(
    'select count(*) from units where path=?', (PATH,)).fetchone()[0] == 63
   and db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0] == 42)
ck('confine alla riga 209 (DESCRIPTION di Concentrating Solar Cell)', db.execute(
    'select line,kind,context from units where path=? and line>? order by line limit 1',
    (PATH, last)).fetchone() == (209, 'DESCRIPTION', 'outfit:Concentrating Solar Cell'))
ck('tipi: 10 DESCRIPTION, zero VALUE', collections.Counter(u['kind'] for u in su) == {'DESCRIPTION': 10})
ck('ZERO UI_LABEL, ZERO token, ZERO virgolette',
   [u['idx'] for u in su if u['kind'] == 'UI_LABEL'] == []
   and [u['idx'] for u in tu for t in TAGS.findall(u['italian'])] == []
   and sum(u['english'].count('"') for u in su) == 0 == sum(u['italian'].count('"') for u in tu))
ck('4 unita con tab: idx 4, 6, 8, 10, le stesse in traduzione',
   [u['idx'] for u in su if u['english'].startswith('\t')] == [4, 6, 8, 10]
   == [u['idx'] for u in tu if u['italian'].startswith('\t')])
ck('10 testi distinti, 6 contesti distinti',
   len({u['english'] for u in tu}) == 10 and len({u['context'] for u in tu}) == 6)
ck('i due generatori restano distinti per contenuto',
   len({by[i]['italian'] for i in (7, 8, 9, 10)}) == 4
   and 'anemico' in by[8]['italian']
   and 'Il più grande generatore di scudi' in by[9]['italian'])
ck('tutte PENDING', not [u['idx'] for u in su
                         if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('spazi iniziali e finali identici al sorgente (10/10)',
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
ck('le parti ricostruiscono translation.json (1..10)',
   sorted(merged) == list(range(1, 11)) and merged == {u['idx']: u['italian'] for u in tu})
ck('nessun altro lotto rivendica le righe 112-193',
   not [f for f in os.listdir(os.path.join(L10N, 'staging/editorial'))
        if f.startswith('L') and os.path.exists(os.path.join(L10N, 'staging/editorial', f, 'translation.json'))
        and os.path.abspath(os.path.join(L10N, 'staging/editorial', f)) != HERE
        and any(u['path'] == PATH and first <= u['line'] <= last for u in json.load(open(os.path.join(
            L10N, 'staging/editorial', f, 'translation.json'), encoding='utf-8'))['units'])])
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('segmento: 21/63 unita del file (33,3%) · 11 prima / 10 nel lotto / 42 dopo · confine riga 209')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L162 superato' if not fail else 'verify L162 fallito')
raise SystemExit(0 if not fail else 1)
