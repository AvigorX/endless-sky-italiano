r"""verify.py — L152 (`data/coalition/coalition jobs.txt`, 21 unita', righe 1191-1359).

Invariante di **segmento**: 197 unita' nel file, **115 prima** della riga 1191, **61 dopo** la 1359, confine alla riga
**1360** (ancora `LOGBOOK` della stessa missione).

Misure proprie: **3 `LOGBOOK`** e **3 `MISSION_TEXT`** (il cambio di carattere del file); **2 unita' con tab**;
**1 unita' con le virgolette** (la battuta dell'Arach, con l'inversione della sua specie).
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
PATH = 'data/coalition/coalition jobs.txt'
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
ck('idx 1..21 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 22)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 21 righe 1191 - 1359', len(tu) == 21 and (first, last) == (1191, 1359), (len(tu), first, last))
ck('115 unita prima della riga 1191 (L147…L151)', db.execute(
    'select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0] == 115)
ck('197 unita nel file, 61 dopo la riga 1359', db.execute(
    'select count(*) from units where path=?', (PATH,)).fetchone()[0] == 197
   and db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0] == 61)
ck('confine alla riga 1360: ancora LOGBOOK della stessa missione', db.execute(
    'select line,kind from units where path=? and line>? order by line limit 1',
    (PATH, last)).fetchone() == (1360, 'LOGBOOK'))
ck('tipi: 7 VALUE + 7 DESCRIPTION + 3 MISSION_TEXT + 3 LOGBOOK + 1 TEXT',
   collections.Counter(u['kind'] for u in su) == {'VALUE': 7, 'DESCRIPTION': 7, 'MISSION_TEXT': 3, 'LOGBOOK': 3,
                                                 'TEXT': 1})
ck('il cambio di carattere: 3 LOGBOOK e 3 MISSION_TEXT, tutti tradotti',
   len([u for u in tu if u['kind'] in ('LOGBOOK', 'MISSION_TEXT')]) == 6
   and not [u['idx'] for u in tu if u['kind'] in ('LOGBOOK', 'MISSION_TEXT')
            and u['italian'].strip() == u['english'].strip()])
ck('ZERO UI_LABEL (asserzione vuota)', [u['idx'] for u in su if u['kind'] == 'UI_LABEL'] == [])
TOK = {'<planet>': 10, '<payment>': 9, '<bunks>': 6, '<date>': 3, '<origin>': 3, '<destination>': 3}
ck('34 token su 6 simboli, stesso multiset in italiano',
   dict(collections.Counter(t for u in su for t in TAGS.findall(u['english']))) == TOK ==
   dict(collections.Counter(t for u in tu for t in TAGS.findall(u['italian'])))
   and sum(TOK.values()) == 34)
ck('parita per unita: stesso ordine di simboli in tutte le 21',
   not [u['idx'] for u in tu if TAGS.findall(u['italian']) != TAGS.findall(u['english'])])
ck('7 VALUE identici al sorgente',
   len([u for u in tu if u['kind'] == 'VALUE']) == 7
   and [u['idx'] for u in tu if u['kind'] == 'VALUE' and u['italian'].rstrip() != u['english'].rstrip()] == [])
ck('2 unita con tab (9 e 10), le stesse in traduzione',
   [u['idx'] for u in su if u['english'].startswith('\t')] == [17, 18]
   == [u['idx'] for u in tu if u['italian'].startswith('\t')])
ck('1 unita con 2 virgolette (17): la battuta dell Arach, con l inversione',
   [u['idx'] for u in su if u['english'].count('"')] == [17]
   and by[17]['italian'].count('"') == 2 and 'generosità' in by[17]['italian'])
ck('la resa dell Arach conserva l inversione («Enormemente prezioso è…»)',
   'Enormemente prezioso è' in by[17]['italian'] and 'ancora incapaci di crearne uno nostro siamo' in by[17]['italian'])
ck('13 stringhe distinte su 21 unita', len({(u['kind'], u['english']) for u in tu}) == 13)
ck('tutte PENDING', not [u['idx'] for u in su
                         if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('spazi iniziali e finali identici al sorgente (21/21)',
   not [u['idx'] for u in tu
        if len(u['italian']) - len(u['italian'].rstrip()) != len(u['english']) - len(u['english'].rstrip())])
ck('8 contesti', len(set(u['context'] for u in su)) == 8)
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
ck('le tre parti ricostruiscono translation.json (1..21)',
   sorted(merged) == list(range(1, 22)) and merged == {u['idx']: u['italian'] for u in tu})
ck('nessun altro lotto rivendica le righe 1191-1359',
   not [f for f in os.listdir(os.path.join(L10N, 'staging/editorial'))
        if f.startswith('L') and os.path.exists(os.path.join(L10N, 'staging/editorial', f, 'translation.json'))
        and os.path.abspath(os.path.join(L10N, 'staging', 'editorial', f)) != HERE
        and any(u['path'] == PATH and first <= u['line'] <= last for u in json.load(open(os.path.join(
            L10N, 'staging', 'editorial', f, 'translation.json'), encoding='utf-8'))['units'])])
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('segmento: 136/197 unita del file (69,0%) · 115 prima / 61 dopo · confine riga 1360')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L152 superato' if not fail else 'verify L152 fallito')
raise SystemExit(0 if not fail else 1)
