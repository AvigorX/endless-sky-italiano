r"""verify.py — L148 (`data/coalition/coalition jobs.txt`, 16 unita', righe 309-435).

Invariante di **segmento**: 197 unita' nel file, **30 prima** della riga 309, **151 dopo** la 435, confine alla riga
**455**, che apre `mission:Coalition: Saryd Interspecies 2` (la finestra finisce **dentro** `Saryd Interspecies 1`).

Misure proprie: primo **`DIALOG`** del file, **`<destination>`** distinto da `<planet>`, **6 `VALUE`** identici senza
«the», 31 token con parita' per simbolo e per unita'.
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
ck('idx 1..16 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 17)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 16 righe 309 - 435', len(tu) == 16 and (first, last) == (309, 435), (len(tu), first, last))
ck('30 unita prima della riga 309 (L147)', db.execute(
    'select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0] == 30)
ck('197 unita nel file, 151 dopo la riga 435', db.execute(
    'select count(*) from units where path=?', (PATH,)).fetchone()[0] == 197
   and db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0] == 151)
ck('confine alla riga 455 apre Saryd Interspecies 2', db.execute(
    'select line,context from units where path=? and line>? order by line limit 1',
    (PATH, last)).fetchone() == (455, 'mission:Coalition: Saryd Interspecies 2'))
ck('tipi: 1 DIALOG + 3 TEXT + 6 VALUE + 6 DESCRIPTION',
   collections.Counter(u['kind'] for u in su) == {'DIALOG': 1, 'TEXT': 3, 'VALUE': 6, 'DESCRIPTION': 6})
ck('il DIALOG e l unita 1 ed e tradotto',
   [u['idx'] for u in su if u['kind'] == 'DIALOG'] == [1]
   and by[1]['italian'].strip() != by[1]['english'].strip())
ck('ZERO LOGBOOK e ZERO UI_LABEL (due asserzioni vuote)',
   [u['idx'] for u in su if u['kind'] in ('LOGBOOK', 'UI_LABEL')] == [])
TOK = {'<payment>': 10, '<planet>': 9, '<bunks>': 6, '<destination>': 6}
ck('31 token su 4 simboli, stesso multiset in italiano',
   dict(collections.Counter(t for u in su for t in TAGS.findall(u['english']))) == TOK ==
   dict(collections.Counter(t for u in tu for t in TAGS.findall(u['italian'])))
   and sum(TOK.values()) == 31)
ck('parita per unita: simboli identici e nello stesso ordine',
   not [u['idx'] for u in tu if TAGS.findall(u['italian']) != TAGS.findall(u['english'])])
ck('<destination> (6) distinto da <planet> (9), anche per unita',
   sum(1 for u in tu for _ in re.findall('<destination>', u['italian'])) == 6
   and sum(1 for u in tu for _ in re.findall('<planet>', u['italian'])) == 9
   and '<destination>' in by[4]['italian'] and '<planet>' not in by[4]['italian'])
ck('6 VALUE identici, senza «the»',
   [u['idx'] for u in tu if u['kind'] == 'VALUE' and u['italian'].rstrip() != u['english'].rstrip()] == []
   and 'the <planet>' not in ' '.join(u['italian'] for u in tu if u['kind'] == 'VALUE'))
ck('DESCRIPTION e TEXT tradotti',
   not [u['idx'] for u in tu if u['kind'] != 'VALUE' and u['italian'].strip() == u['english'].strip()])
ck('tutte PENDING', not [u['idx'] for u in su
                         if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('spazi iniziali e finali identici al sorgente (16/16)',
   not [u['idx'] for u in tu
        if len(u['italian']) - len(u['italian'].rstrip()) != len(u['english']) - len(u['english'].rstrip())])
ck('zero tab e zero virgolette (due asserzioni vuote)',
   sum(1 for u in su if u['english'].startswith('\t')) == 0
   and sum(u['english'].count('"') for u in su) == 0 == sum(u['italian'].count('"') for u in tu))
ck('10 contesti', len(set(u['context'] for u in su)) == 10)
ck('10 testi inglesi distinti', len({u['english'] for u in tu}) == 10)
ck('i nomi restano: Lunarium, Heliarch',
   all(t in ' '.join(u['italian'] for u in tu) for t in ('Lunarium', 'Heliarch')))
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
ck('le tre parti ricostruiscono translation.json (1..16)',
   sorted(merged) == list(range(1, 17)) and merged == {u['idx']: u['italian'] for u in tu})
ck('nessun altro lotto rivendica le righe 309-435',
   not [f for f in os.listdir(os.path.join(L10N, 'staging/editorial'))
        if f.startswith('L') and os.path.exists(os.path.join(L10N, 'staging/editorial', f, 'translation.json'))
        and os.path.abspath(os.path.join(L10N, 'staging', 'editorial', f)) != HERE
        and any(u['path'] == PATH and first <= u['line'] <= last for u in json.load(open(os.path.join(
            L10N, 'staging', 'editorial', f, 'translation.json'), encoding='utf-8'))['units'])])
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('segmento: 46/197 unita del file (23,4%) · 30 prima / 151 dopo · confine riga 455')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L148 superato' if not fail else 'verify L148 fallito')
raise SystemExit(0 if not fail else 1)
