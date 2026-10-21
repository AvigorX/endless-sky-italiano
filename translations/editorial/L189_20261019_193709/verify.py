r"""verify.py — L189_20261019_193709 (`data/gegno/gegno outfits.txt`).

Invariante di **segmento**: 47 unita' prima, il lotto, **N dopo**; confine alla riga 1137, tipo **`DESCRIPTION`** (`outfit:Scin Adjutant License`) — misurato.
"""
import collections
import hashlib
import json
import os
import re
import sqlite3

TAB = chr(9)
HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
ROOT = os.path.abspath(os.path.join(L10N, '..'))
PATH = 'data/gegno/gegno outfits.txt'
TAGS = re.compile(r'<[^<>]+>')
su = sorted(json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
fail = []


def ck(n, c, d=''):
    print('%-70s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente', not [u for u in su if lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck('idx consecutivi e ordine = sorgente',
   [u['idx'] for u in tu] == list(range(1, len(tu) + 1)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
tot = db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0]
after = tot - 47 - len(tu)
ck('unita: %d righe %d - %d' % (len(tu), first, last), (first, last) == (su[0]['line'], su[-1]['line']))
ck('47 unita prima della riga %d' % first, db.execute(
    'select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0] == 47)
ck('%d unita nel file, %d dopo la riga %d (totale - 47 - lotto)' % (tot, after, last), after == 1 and tot == 60)
ck('confine alla riga 1137, tipo DESCRIPTION (misurato)', db.execute(
    'select line,kind,context from units where path=? and line>? order by line limit 1',
    (PATH, last)).fetchone() == (1137, 'DESCRIPTION', 'outfit:Scin Adjutant License'))
ck('min/max del file invariati', db.execute(
    'select min(line),max(line) from units where path=?', (PATH,)).fetchone() == (17, 1137))
ck('tipi coerenti fra sorgente e DB',
   dict(collections.Counter(u['kind'] for u in su)) == dict(db.execute(
       'select kind,count(*) from units where id in (%s) group by kind'
       % ','.join('?' * len(su)), [u['id'] for u in su]).fetchall()))
ck("VALUE: identita' al sorgente e conteggio atteso",
   [u['idx'] for u in tu if u['kind'] == 'VALUE' and u['italian'] != u['english']] == []
   and len([u for u in su if u['kind'] == 'VALUE']) == 1)
ck('ZERO UI_LABEL e ZERO token',
   [u['idx'] for u in su if u['kind'] == 'UI_LABEL'] == []
   and {t for u in su for t in TAGS.findall(u['english'])} == set())
ck('0 tab e 0 virgolette, come misurato',
   [u['idx'] for u in su if u['english'].startswith(TAB)] == []
   == [u['idx'] for u in tu if u['italian'].startswith(TAB)]
   and sum(u['english'].count('"') for u in su) == 0 == sum(u['italian'].count('"') for u in tu))
ck('6 apici inglesi con la distribuzione misurata',
   sum(u['english'].count("'") for u in su) == 6
   and {u['idx']: u['english'].count("'") for u in su if "'" in u['english']} == {2: 1, 3: 1, 8: 1, 9: 2, 12: 1})
ck('11 apici italiani (elisioni), nessun possessivo inglese sopravvissuto',
   {u['idx']: u['italian'].count("'") for u in tu if "'" in u['italian']} == {1: 5, 2: 1, 5: 1, 6: 1, 9: 2, 11: 1}
   and not [u['idx'] for u in tu if re.search(r"\b[A-Za-z]+'s\b", u['italian'])])
ck('testi distinti e contesti coerenti col sorgente',
   len({u['english'] for u in tu}) == 12
   and len({u['context'] for u in tu}) == 11
   and sorted(collections.Counter(u['context'] for u in tu).values()) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2])
ck('tutte PENDING', not [u['idx'] for u in su
                         if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('nessuno spazio finale (tab iniziali ammessi)',
   not [u['idx'] for u in tu if u['english'].rstrip(TAB) != u['english'].rstrip(TAB).rstrip()
        or u['italian'].rstrip(TAB) != u['italian'].rstrip(TAB).rstrip()])
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
ck('le parti ricostruiscono translation.json',
   sorted(merged) == sorted(u['idx'] for u in tu) and merged == {u['idx']: u['italian'] for u in tu})
ck('nessun altro lotto rivendica le stesse righe',
   not [f for f in os.listdir(os.path.join(L10N, 'staging/editorial'))
        if f.startswith('L') and os.path.exists(os.path.join(L10N, 'staging/editorial', f, 'translation.json'))
        and os.path.abspath(os.path.join(L10N, 'staging/editorial', f)) != HERE
        and any(u['path'] == PATH and first <= u['line'] <= last for u in json.load(open(os.path.join(
            L10N, 'staging/editorial', f, 'translation.json'), encoding='utf-8'))['units'])])
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('segmento: %d/%d unita del file · 47 prima / %d nel lotto / %d dopo · confine riga 1137 (~DESCRIPTION)'
      % (len(tu) + 47, tot, len(tu), after))
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L189 superato' if not fail else 'verify L189 fallito')
raise SystemExit(0 if not fail else 1)
