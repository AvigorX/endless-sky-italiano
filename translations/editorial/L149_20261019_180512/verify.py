r"""verify.py — L149 (`data/coalition/coalition jobs.txt`, 18 unita', righe 455-634).

Invariante di **segmento**: 197 unita' nel file, **46 prima** della riga 455, **133 dopo** la 634, confine alla riga
**639**, che apre `mission:Coalition: Tourists Out 1`.

Misure proprie: **36 token** con **due coppie di conteggi uguali** — l'ordine per unita' e' l'unico controllo che
smaschera uno scambio; **8 `VALUE`** identici; la `DESCRIPTION` dei coloni e' la stessa di L148 (stessa stringa
inglese), il `TEXT` degli operai **non** e' quello di L147.
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
PREV148 = os.path.join(L10N, 'staging/editorial/L148_20261019_174022/translation.json')
su = sorted(json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
by = {u['idx']: u for u in tu}
lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
p148 = {u['english']: u['italian'] for u in json.load(open(PREV148, encoding='utf-8'))['units']}
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
ck('idx 1..18 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 19)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 18 righe 455 - 634', len(tu) == 18 and (first, last) == (455, 634), (len(tu), first, last))
ck('46 unita prima della riga 455 (L147 + L148)', db.execute(
    'select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0] == 46)
ck('197 unita nel file, 133 dopo la riga 634', db.execute(
    'select count(*) from units where path=?', (PATH,)).fetchone()[0] == 197
   and db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0] == 133)
ck('confine alla riga 639 apre Tourists Out 1', db.execute(
    'select line,context from units where path=? and line>? order by line limit 1',
    (PATH, last)).fetchone() == (639, 'mission:Coalition: Tourists Out 1'))
ck('tipi: 8 VALUE + 8 DESCRIPTION + 2 TEXT',
   collections.Counter(u['kind'] for u in su) == {'VALUE': 8, 'DESCRIPTION': 8, 'TEXT': 2})
ck('ZERO LOGBOOK, DIALOG, UI_LABEL (tre asserzioni vuote)',
   [u['idx'] for u in su if u['kind'] in ('LOGBOOK', 'DIALOG', 'UI_LABEL')] == [])
TOK = {'<planet>': 10, '<payment>': 10, '<bunks>': 8, '<destination>': 8}
ck('36 token su 4 simboli, con DUE coppie di conteggi uguali (10/10, 8/8)',
   dict(collections.Counter(t for u in su for t in TAGS.findall(u['english']))) == TOK
   and sum(TOK.values()) == 36 and TOK['<planet>'] == TOK['<payment>'] and TOK['<bunks>'] == TOK['<destination>'])
ck('parita per unita: ordine dei simboli identico (l unico controllo che smaschera lo scambio)',
   not [u['idx'] for u in tu if TAGS.findall(u['italian']) != TAGS.findall(u['english'])])
ck('multiset italiano identico a quello inglese',
   dict(collections.Counter(t for u in tu for t in TAGS.findall(u['italian']))) == TOK)
ck('8 VALUE identici al sorgente',
   len([u for u in tu if u['kind'] == 'VALUE']) == 8
   and [u['idx'] for u in tu if u['kind'] == 'VALUE' and u['italian'].rstrip() != u['english'].rstrip()] == [])
ck('DESCRIPTION e TEXT tradotti',
   not [u['idx'] for u in tu if u['kind'] != 'VALUE' and u['italian'].strip() == u['english'].strip()])
ck('la DESCRIPTION dei coloni ripete la resa di L148 (stessa stringa inglese)',
   all(v['italian'] == p148[v['english']] for v in tu
       if v['english'].startswith('As part of the Interspecies Exchange Program')))
ck('il TEXT degli operai non ha «the»: resa con «su <planet>»',
   'su <planet>' in by[11]['italian'] and 'sul <planet>' not in by[11]['italian']
   and not [u['idx'] for u in su if 'on the <planet>' in u['english']])
ck('tutte PENDING', not [u['idx'] for u in su
                         if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('spazi iniziali e finali identici al sorgente (18/18)',
   not [u['idx'] for u in tu
        if len(u['italian']) - len(u['italian'].rstrip()) != len(u['english']) - len(u['english'].rstrip())])
ck('zero tab e zero virgolette (due asserzioni vuote)',
   sum(1 for u in su if u['english'].startswith('\t')) == 0
   and sum(u['english'].count('"') for u in su) == 0 == sum(u['italian'].count('"') for u in tu))
ck('10 contesti', len(set(u['context'] for u in su)) == 10)
ck('8 testi inglesi distinti', len({u['english'] for u in tu}) == 8)
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
ck('le tre parti ricostruiscono translation.json (1..18)',
   sorted(merged) == list(range(1, 19)) and merged == {u['idx']: u['italian'] for u in tu})
ck('nessun altro lotto rivendica le righe 455-634',
   not [f for f in os.listdir(os.path.join(L10N, 'staging/editorial'))
        if f.startswith('L') and os.path.exists(os.path.join(L10N, 'staging/editorial', f, 'translation.json'))
        and os.path.abspath(os.path.join(L10N, 'staging', 'editorial', f)) != HERE
        and any(u['path'] == PATH and first <= u['line'] <= last for u in json.load(open(os.path.join(
            L10N, 'staging', 'editorial', f, 'translation.json'), encoding='utf-8'))['units'])])
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('segmento: 64/197 unita del file (32,5%) · 46 prima / 133 dopo · confine riga 639')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L149 superato' if not fail else 'verify L149 fallito')
raise SystemExit(0 if not fail else 1)
