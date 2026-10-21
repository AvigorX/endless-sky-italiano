r"""verify.py — L151 (`data/coalition/coalition jobs.txt`, 37 unita', righe 799-1171).

Invariante di **segmento**: 197 unita' nel file, **78 prima** della riga 799, **82 dopo** la 1171, confine alla riga
**1191** (`TEXT` della famiglia successiva).

Misure proprie: **81 token su 7 simboli**; 14 stringhe distinte su 37 unita'; le **8 copie** di
`Deliver <cargo> to <destination>. Payment is <payment>.` hanno una sola resa; 17 `VALUE` identici.
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
ck('idx 1..37 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 38)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 37 righe 799 - 1171', len(tu) == 37 and (first, last) == (799, 1171), (len(tu), first, last))
ck('78 unita prima della riga 799 (L147…L150)', db.execute(
    'select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0] == 78)
ck('197 unita nel file, 82 dopo la riga 1171', db.execute(
    'select count(*) from units where path=?', (PATH,)).fetchone()[0] == 197
   and db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0] == 82)
ck('confine alla riga 1191 e un TEXT (nessuna coppia spezzata)', db.execute(
    'select line,kind from units where path=? and line>? order by line limit 1',
    (PATH, last)).fetchone() == (1191, 'TEXT'))
ck('tipi: 17 VALUE + 17 DESCRIPTION + 2 TEXT + 1 DIALOG',
   collections.Counter(u['kind'] for u in su) == {'VALUE': 17, 'DESCRIPTION': 17, 'TEXT': 2, 'DIALOG': 1})
ck('il DIALOG e l unita 32 (i medici) ed e tradotto',
   [u['idx'] for u in su if u['kind'] == 'DIALOG'] == [32]
   and by[32]['italian'].strip() != by[32]['english'].strip())
ck('due asserzioni vuote: ZERO LOGBOOK, ZERO UI_LABEL',
   [u['idx'] for u in su if u['kind'] in ('LOGBOOK', 'UI_LABEL')] == [])
TOK = {'<planet>': 19, '<payment>': 20, '<destination>': 17, '<cargo>': 14, '<date>': 7,
       '<bunks>': 3, '<commodity>': 1}
ck('81 token su 7 simboli, stesso multiset in italiano',
   dict(collections.Counter(t for u in su for t in TAGS.findall(u['english']))) == TOK ==
   dict(collections.Counter(t for u in tu for t in TAGS.findall(u['italian'])))
   and sum(TOK.values()) == 81)
ck('parita per unita: stesso ordine di simboli in tutte le 37',
   not [u['idx'] for u in tu if TAGS.findall(u['italian']) != TAGS.findall(u['english'])])
ck('17 VALUE identici al sorgente',
   len([u for u in tu if u['kind'] == 'VALUE']) == 17
   and [u['idx'] for u in tu if u['kind'] == 'VALUE' and u['italian'].rstrip() != u['english'].rstrip()] == [])
ck('DESCRIPTION, TEXT e DIALOG tradotti (20 unita)',
   not [u['idx'] for u in tu if u['kind'] != 'VALUE' and u['italian'].strip() == u['english'].strip()])
cargo = [u for u in tu if u['english'] == 'Deliver <cargo> to <destination>. Payment is <payment>.']
ck('le 8 copie di Cargo/Bulk condividono UNA resa', len(cargo) == 8
   and len({u['italian'] for u in cargo}) == 1, (len(cargo), len({u['italian'] for u in cargo})))
ck('14 stringhe distinte su 37 unita', len({(u['kind'], u['english']) for u in tu}) == 14)
ck('tutte PENDING', not [u['idx'] for u in su
                         if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('spazi iniziali e finali identici al sorgente (37/37)',
   not [u['idx'] for u in tu
        if len(u['italian']) - len(u['italian'].rstrip()) != len(u['english']) - len(u['english'].rstrip())])
ck('zero tab e zero virgolette (due asserzioni vuote)',
   sum(1 for u in su if u['english'].startswith('\t')) == 0
   and sum(u['english'].count('"') for u in su) == 0 == sum(u['italian'].count('"') for u in tu))
ck('19 contesti', len(set(u['context'] for u in su)) == 19)
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
ck('le tre parti ricostruiscono translation.json (1..37)',
   sorted(merged) == list(range(1, 38)) and merged == {u['idx']: u['italian'] for u in tu})
ck('nessun altro lotto rivendica le righe 799-1171',
   not [f for f in os.listdir(os.path.join(L10N, 'staging/editorial'))
        if f.startswith('L') and os.path.exists(os.path.join(L10N, 'staging/editorial', f, 'translation.json'))
        and os.path.abspath(os.path.join(L10N, 'staging', 'editorial', f)) != HERE
        and any(u['path'] == PATH and first <= u['line'] <= last for u in json.load(open(os.path.join(
            L10N, 'staging', 'editorial', f, 'translation.json'), encoding='utf-8'))['units'])])
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('segmento: 115/197 unita del file (58,4%) · 78 prima / 82 dopo · confine riga 1191')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L151 superato' if not fail else 'verify L151 fallito')
raise SystemExit(0 if not fail else 1)
