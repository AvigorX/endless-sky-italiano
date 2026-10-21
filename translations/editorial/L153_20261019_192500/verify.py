r"""verify.py — L153 (`data/coalition/coalition jobs.txt`, 20 unita', righe 1360-1469).

Invariante di **segmento**: 197 unita' nel file, **136 prima** della riga 1360, **41 dopo** la 1469, confine alla riga
**1475** (`VALUE` della famiglia successiva).

Misure proprie: **l'inversione dell'Arach** (due frasi), le due descrizioni `Contain Criminals` che differiscono per una
parola e hanno **rese diverse** («sul posto» / «sul luogo»), 7 unita' con tab, 20 virgolette, 16 token.
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
ck('idx 1..20 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 21)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 20 righe 1360 - 1469', len(tu) == 20 and (first, last) == (1360, 1469), (len(tu), first, last))
ck('136 unita prima della riga 1360 (L147…L152)', db.execute(
    'select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0] == 136)
ck('197 unita nel file, 41 dopo la riga 1469', db.execute(
    'select count(*) from units where path=?', (PATH,)).fetchone()[0] == 197
   and db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0] == 41)
ck('confine alla riga 1475 (VALUE, nessuna coppia spezzata)', db.execute(
    'select line,kind from units where path=? and line>? order by line limit 1',
    (PATH, last)).fetchone() == (1475, 'VALUE'))
ck('tipi: 1 LOGBOOK + 7 MISSION_TEXT + 4 VALUE + 4 DESCRIPTION + 4 DIALOG',
   collections.Counter(u['kind'] for u in su) == {'LOGBOOK': 1, 'MISSION_TEXT': 7, 'VALUE': 4, 'DESCRIPTION': 4,
                                                 'DIALOG': 4})
ck('ZERO UI_LABEL (asserzione vuota)', [u['idx'] for u in su if u['kind'] == 'UI_LABEL'] == [])
TOK = {'<payment>': 7, '<destination>': 3, '<date>': 3, '<bunks>': 3}
ck('16 token su 4 simboli, stesso multiset in italiano',
   dict(collections.Counter(t for u in su for t in TAGS.findall(u['english']))) == TOK ==
   dict(collections.Counter(t for u in tu for t in TAGS.findall(u['italian'])))
   and sum(TOK.values()) == 16)
ck('parita per unita: stesso ordine di simboli in tutte le 20',
   not [u['idx'] for u in tu if TAGS.findall(u['italian']) != TAGS.findall(u['english'])])
ck('4 VALUE identici al sorgente',
   len([u for u in tu if u['kind'] == 'VALUE']) == 4
   and [u['idx'] for u in tu if u['kind'] == 'VALUE' and u['italian'].rstrip() != u['english'].rstrip()] == [])
ck('7 unita con tab, le stesse in traduzione',
   [u['idx'] for u in su if u['english'].startswith('\t')] == [2, 3, 4, 5, 6, 7, 8]
   == [u['idx'] for u in tu if u['italian'].startswith('\t')])
ck('20 virgolette, nessuna unita dispari',
   sum(u['english'].count('"') for u in su) == 20 == sum(u['italian'].count('"') for u in tu)
   and [u['idx'] for u in su if u['english'].count('"') % 2] == []
   and not [u['idx'] for u in tu if u['english'].count('"') != u['italian'].count('"')])
ck('l Arach inverte: «ancora non possiamo vendere» (unita 4)',
   'ancora non possiamo vendere' in by[4]['italian'])
ck('il Saryd inverte anche lui: «… è.» e «… è impegnato» (unita 7)',
   "per giustizia, è." in by[7]['italian'] and 'ogniuno è impegnato' not in by[7]['italian']
   and 'ognuno è impegnato' in by[7]['italian'])
ck('le due descrizioni Contain Criminals hanno rese DIVERSE (sul posto / sul luogo)',
   by[13]['italian'] != by[19]['italian']
   and 'sul posto' in by[13]['italian'] and 'sul luogo' in by[19]['italian'],
   (by[13]['italian'][:60], by[19]['italian'][:60]))
ck('i tre DIALOG di Contain raccontano esiti diversi',
   len({by[14]['italian'], by[17]['italian'], by[20]['italian']}) == 3)
ck('17 stringhe distinte su 20 unita', len({(u['kind'], u['english'].lstrip('\t')) for u in tu}) == 17)
ck('tutte PENDING', not [u['idx'] for u in su
                         if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('spazi iniziali e finali identici al sorgente (20/20)',
   not [u['idx'] for u in tu
        if len(u['italian']) - len(u['italian'].rstrip()) != len(u['english']) - len(u['english'].rstrip())])
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
ck('nessun altro lotto rivendica le righe 1360-1469',
   not [f for f in os.listdir(os.path.join(L10N, 'staging/editorial'))
        if f.startswith('L') and os.path.exists(os.path.join(L10N, 'staging/editorial', f, 'translation.json'))
        and os.path.abspath(os.path.join(L10N, 'staging', 'editorial', f)) != HERE
        and any(u['path'] == PATH and first <= u['line'] <= last for u in json.load(open(os.path.join(
            L10N, 'staging', 'editorial', f, 'translation.json'), encoding='utf-8'))['units'])])
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('segmento: 156/197 unita del file (79,2%) · 136 prima / 41 dopo · confine riga 1475')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L153 superato' if not fail else 'verify L153 fallito')
raise SystemExit(0 if not fail else 1)
