r"""verify.py — L114 (data/_ui/tooltips.txt, 110 unita', righe 976-1309)

Invariante di **segmento**, indipendente da `check.py`: rilegge il repository originale, `state.db`, i
`parts/` e `translation.json`, e ricalcola tutto.

Misure attese: **320 unita' prima** della riga 976 (L111+L112+L113), **237 dopo** la 1309, file di **667
unita'**, `max_line = 1865`, confine alla riga **1312** (`tip:battery only?`). **110 `TUTORIAL_TIP`**, tutte
`PENDING`, **110 contesti distinti** (uno per unita'), **12 virgolette** in cinque unita', **zero tab**,
**zero token**, **zero quadre**, e **quattro coppie di ripetizioni legittime** (`/ second` contro `/ shot`)
rese **identiche**, ricalcolate dal `source.json` — non da una lista scritta a mano.
"""
import collections
import glob
import hashlib
import json
import os
import re
import sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
ROOT = os.path.abspath(os.path.join(L10N, '..'))
PATH = 'data/_ui/tooltips.txt'
su = sorted(json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
TAGS = re.compile(r'<[^<>]+>')
fail = []


def ck(n, c, d=''):
    print('%-72s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
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
ck('idx 1..110 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 111)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 110 righe 976 - 1309', len(tu) == 110 and (first, last) == (976, 1309), (len(tu), first, last))
tot = db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0]
before = db.execute('select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0]
after = db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0]
maxl = db.execute('select max(line) from units where path=?', (PATH,)).fetchone()[0]
ck('320 unita prima della riga 976 (L111+L112+L113)', before == 320, before)
ck('237 unita dopo la riga 1309', after == 237, after)
ck('file: 667 unita, max(line) = 1865', tot == 667 and maxl == 1865, (tot, maxl))
ck('il confine: la riga 1312 apre tip:battery only?',
   db.execute('select line,context from units where path=? and line>? order by line limit 1',
              (PATH, last)).fetchone() == (1312, 'tip:battery only?'))
ck('tipo unico: 110 TUTORIAL_TIP',
   collections.Counter(u['kind'] for u in su) == {'TUTORIAL_TIP': 110},
   collections.Counter(u['kind'] for u in su))
ck('tutte PENDING',
   not [u['idx'] for u in su
        if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
by = {u['idx']: u for u in tu}
ck('nessuna unita identica al sorgente',
   not [u['idx'] for u in tu if u['italian'].strip() == u['english'].strip()])
# --- contesti: 110, uno per unita' --------------------------------------------------------
seen = collections.Counter(u['context'] for u in su)
ck('110 contesti distinti (uno per unita)', len(seen) == 110 == len(su), len(seen))
ck('nessun contesto doppio', max(seen.values()) == 1, {k: v for k, v in seen.items() if v > 1})
ck('nessun tab (sorgente e traduzione)',
   not [u['idx'] for u in su if '\t' in u['english']] and not [u['idx'] for u in tu if '\t' in u['italian']])
a = sum(u['english'].count('"') for u in su)
b = sum(u['italian'].count('"') for u in tu)
ck('virgolette: %d = %d (12)' % (a, b), a == b == 12, (a, b))
ck('virgolette per unita', not [u for u in tu if u['english'].count('"') != u['italian'].count('"')],
   [(u['idx'], u['english'].count('"'), u['italian'].count('"'))
    for u in tu if u['english'].count('"') != u['italian'].count('"')])
ck('le cinque unita con virgolette: 19, 38, 52(x4), 66, 85',
   [u['idx'] for u in tu if u['italian'].count('"')] == [19, 38, 52, 66, 85]
   and by[52]['italian'].count('"') == 4, [u['idx'] for u in tu if u['italian'].count('"')])
ck('ZERO token (asserito vuoto)',
   not [t for u in su for t in TAGS.findall(u['english'])]
   and not [t for u in tu for t in TAGS.findall(u['italian'])])
ck('ZERO quadre (asserito vuoto)', not [u['idx'] for u in tu if '[' in u['italian'] or ']' in u['italian']])
ck('nessun backtick', not [u for u in tu if '`' in u['italian']])
ck('nessuna traduzione vuota', all(u['italian'].strip() for u in tu))
NONLAT = re.compile(r'[^\x00-\x7F\u00C0-\u024F]')
ck('nessun carattere non latino', not [u for u in tu if NONLAT.search(u['italian'])])
ck('nessun trattino lungo o virgoletta curva',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB')])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate', 0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
print('rapporto IT/EN: min %.2f max %.2f · media %.2f' % (min(rs), max(rs), sum(rs) / len(rs)))
# --- ripetizioni: quattro coppie ricalcolate dal sorgente --------------------------------
grp = {}
for u in su:
    grp.setdefault(u['english'], []).append(u['idx'])
pairs = sorted(v for v in grp.values() if len(v) > 1)
ck('quattro coppie di ripetizioni (nessun gruppo da tre)', pairs == [[17, 64], [18, 65], [19, 66], [36, 83]],
   pairs)
ck('le quattro coppie sono rese identiche',
   all(by[p[0]]['italian'] == by[p[1]]['italian'] for p in pairs),
   [(p, by[p[0]]['italian'][:40]) for p in pairs if by[p[0]]['italian'] != by[p[1]]['italian']])
it_grp = {}
for u in tu:
    it_grp.setdefault(u['italian'], []).append(u)
ck('nessun duplicato italiano non spiegato dal sorgente',
   not [g for g in it_grp.values() if len(g) > 1 and len({v['english'] for v in g}) > 1])
sec = [u['idx'] for u in tu if 'per second' in u['english'] and 'al secondo' not in u['italian']]
shot = [u['idx'] for u in tu if 'per shot' in u['english'] and 'per colpo' not in u['italian']]
ck('ogni «per second» reso con «al secondo»', not sec, sec)
ck('ogni «per shot» reso con «per colpo»', not shot, shot)
ck('registro approvato: nessun «voi»',
   not [u['idx'] for u in tu if re.search(r'\b(avete|potete|potrete|siete|vostro|vostra|vostri|vostre)\b',
                                          u['italian'])])
LOW = ' '.join(u['italian'] for u in tu).lower()
for t in ('scudi', 'scafo', 'energia', 'calore', 'carburante', 'virata', 'torretta', 'equipaggiament',
          'propulsor', 'postbruciatore'):
    ck('termine chiave presente: %s' % t, t in LOW)
merged = {}
for f in sorted(glob.glob(os.path.join(HERE, 'parts', 'part*.json'))):
    for kk, v in json.load(open(f, encoding='utf-8')).items():
        merged[int(kk)] = v
ck('le tre parti ricostruiscono translation.json (1..110)',
   sorted(merged) == list(range(1, 111))
   and {i: v for i, v in merged.items()} == {u['idx']: u['italian'] for u in tu})
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('parole EN %d -> IT %d · sha256[:16] %s' % (sum(len(u['english'].split()) for u in tu),
      sum(len(u['italian'].split()) for u in tu), h[:16]))
print()
print('FAIL:', len(fail), '·', 'verify L114 superato' if not fail else 'verify L114 fallito')
raise SystemExit(0 if not fail else 1)
