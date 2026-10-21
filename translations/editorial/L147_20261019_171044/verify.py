r"""verify.py — L147 (`data/coalition/coalition jobs.txt`, 30 unita', righe 16-293).

Invariante di **segmento**: 197 unita' nel file, **0 prima** della riga 16, **167 dopo** la 293, confine alla riga
**309**, che apre `mission:Coalition: Heliarch Candidate`.

Misure proprie: **65 occorrenze di token su 7 simboli** con parita' per simbolo **e** per unita'; **13 `VALUE`
identici**; **14 testi distinti** con **4 gruppi tripli** a resa unica; zero tab, zero virgolette.
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
ck('idx 1..30 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 31)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 30 righe 16 - 293', len(tu) == 30 and (first, last) == (16, 293), (len(tu), first, last))
ck('0 unita prima della riga 16 (il file comincia qui in staging)', db.execute(
    'select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0] == 0)
ck('197 unita nel file, 167 dopo la riga 293', db.execute(
    'select count(*) from units where path=?', (PATH,)).fetchone()[0] == 197
   and db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0] == 167)
ck('confine alla riga 309 apre Heliarch Candidate', db.execute(
    'select line,context from units where path=? and line>? order by line limit 1',
    (PATH, last)).fetchone() == (309, 'mission:Coalition: Heliarch Candidate'))
ck('tipi: 13 VALUE + 13 DESCRIPTION + 4 TEXT',
   collections.Counter(u['kind'] for u in su) == {'VALUE': 13, 'DESCRIPTION': 13, 'TEXT': 4})
ck('tre asserzioni vuote: ZERO LOGBOOK, ZERO DIALOG, ZERO UI_LABEL',
   [u['idx'] for u in su if u['kind'] in ('LOGBOOK', 'DIALOG', 'UI_LABEL')] == [])
TOK = {'<planet>': 28, '<payment>': 17, '<bunks>': 6, '<tons>': 6, '<date>': 4, '<origin>': 3, '<commodity>': 1}
ck('65 occorrenze di token, 7 simboli',
   dict(collections.Counter(t for u in su for t in TAGS.findall(u['english']))) == TOK
   and sum(TOK.values()) == 65)
ck('parita per simbolo: 65 e 65, stesso multiset',
   dict(collections.Counter(t for u in tu for t in TAGS.findall(u['italian']))) == TOK)
ck('parita per unita: simboli identici e nello stesso ordine in tutte le 30',
   not [u['idx'] for u in tu if TAGS.findall(u['italian']) != TAGS.findall(u['english'])])
ck('<payment> = 17 e <date> = 4 anche in italiano (nessuno scambio)',
   sum(1 for u in tu for _ in re.findall('<payment>', u['italian'])) == 17
   and sum(1 for u in tu for _ in re.findall('<date>', u['italian'])) == 4)
ck('13 VALUE identici al sorgente',
   [u['idx'] for u in tu if u['kind'] == 'VALUE' and u['italian'].rstrip() != u['english'].rstrip()] == []
   and len([u for u in tu if u['kind'] == 'VALUE']) == 13)
ck('i 5 nomi di lavoro, tre volte ciascuno',
   [u['italian'].rstrip() for u in tu if u['kind'] == 'VALUE']
   == ['Workers to the <planet>'] * 3 + ['Volunteers to the <planet>'] * 3
   + ['Materials to the <planet>'] * 3 + ['Supplies to the <planet>'] * 3 + ['Candidate to the <planet>'])
ck('DESCRIPTION e TEXT tradotti (17 unita)',
   not [u['idx'] for u in tu if u['kind'] != 'VALUE' and u['italian'].strip() == u['english'].strip()])
ck('4 gruppi di ripetizioni triple con resa unica',
   by[3]['italian'] == by[5]['italian'] == by[7]['italian']
   and by[10]['italian'] == by[12]['italian'] == by[14]['italian']
   and by[17]['italian'] == by[19]['italian'] == by[21]['italian']
   and by[24]['italian'] == by[26]['italian'] == by[28]['italian'])
ck('14 testi inglesi distinti', len({u['english'] for u in tu}) == 14)
ck('zero tab e zero virgolette (due asserzioni vuote)',
   sum(1 for u in su if u['english'].startswith('\t')) == 0
   and sum(1 for u in tu if u['italian'].startswith('\t')) == 0
   and sum(u['english'].count('"') for u in su) == 0 == sum(u['italian'].count('"') for u in tu))
ck('17 contesti', len(set(u['context'] for u in su)) == 17)
ck('tutte PENDING', not [u['idx'] for u in su
                         if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('spazi iniziali e finali identici al sorgente (30/30)',
   not [u['idx'] for u in tu
        if len(u['italian']) - len(u['italian'].rstrip()) != len(u['english']) - len(u['english'].rstrip())])
ck('i nomi restano: Heliarch', 'Heliarch' in ' '.join(u['italian'] for u in tu))
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
ck('le tre parti ricostruiscono translation.json (1..30)',
   sorted(merged) == list(range(1, 31)) and merged == {u['idx']: u['italian'] for u in tu})
ck('nessun altro lotto rivendica le righe 16-293',
   not [f for f in os.listdir(os.path.join(L10N, 'staging/editorial'))
        if f.startswith('L') and os.path.exists(os.path.join(L10N, 'staging/editorial', f, 'translation.json'))
        and os.path.abspath(os.path.join(L10N, 'staging', 'editorial', f)) != HERE
        and any(u['path'] == PATH and first <= u['line'] <= last for u in json.load(open(os.path.join(
            L10N, 'staging', 'editorial', f, 'translation.json'), encoding='utf-8'))['units'])])
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('segmento: 30/197 unita del file (15,2%) · 0 prima / 167 dopo · confine riga 309')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L147 superato' if not fail else 'verify L147 fallito')
raise SystemExit(0 if not fail else 1)
