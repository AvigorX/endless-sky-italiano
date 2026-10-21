r"""verify.py — L113 (data/_ui/tooltips.txt, 96 unita', righe 691-973)

Invariante di **segmento**, indipendente da `check.py`: rilegge il repository originale, `state.db` e i `parts/`.

Misure attese: **224 unita' prima** della riga 691 (L111+L112), **347 dopo la 973**, file di **667 unita'**,
`max_line = 1865`, confine alla riga **976** (`tip:Engines:`). **96 `TUTORIAL_TIP`**, **87 contesti** con **nove
contesti doppi**, **22 virgolette**, **zero tab**, **zero token**, **zero quadre**, **zero ripetizioni**, e tutte
`PENDING`.
"""
import collections, glob, hashlib, json, os, re, sqlite3

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
ck('idx 1..96 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 97)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 96 righe 691 - 973', len(tu) == 96 and (first, last) == (691, 973), (len(tu), first, last))
tot = db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0]
before = db.execute('select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0]
after = db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0]
maxl = db.execute('select max(line) from units where path=?', (PATH,)).fetchone()[0]
ck('224 unita prima della riga 691 (L111+L112)', before == 224, before)
ck('347 unita dopo la riga 973', after == 347, after)
ck('file: 667 unita, max(line) = 1865', tot == 667 and maxl == 1865, (tot, maxl))
ck('il confine: la riga 976 apre tip:Engines:',
   db.execute('select line,context from units where path=? and line>? order by line limit 1',
              (PATH, last)).fetchone() == (976, 'tip:Engines:'))
ck('tipo unico: 96 TUTORIAL_TIP',
   collections.Counter(u['kind'] for u in su) == {'TUTORIAL_TIP': 96},
   collections.Counter(u['kind'] for u in su))
ck('tutte PENDING',
   not [u['idx'] for u in su
        if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
by = {u['idx']: u for u in tu}
ck('nessuna unita identica al sorgente',
   not [u['idx'] for u in tu if u['italian'].strip() == u['english'].strip()])
# --- contesti: 87 con nove doppi ----------------------------------------------------------
seen = {}
for u in su:
    seen.setdefault(u['context'], []).append(u['idx'])
doubles = sorted((k, v) for k, v in seen.items() if len(v) == 2)
ck('87 contesti distinti (meno delle 96 unita)', len(seen) == 87, len(seen))
ck('nove contesti doppi, nessuno triplo',
   len(doubles) == 9 and not [v for v in seen.values() if len(v) > 2],
   [k for k, _v in doubles])
ck('i doppi sono quelli attesi (turning, 6 outfitter, shipyard b, capacity)',
   [k for k, _v in doubles] == ['tip:capacity:', 'tip:outfitter: b', 'tip:outfitter: c', 'tip:outfitter: i',
                                'tip:outfitter: r', 'tip:outfitter: s', 'tip:outfitter: u',
                                'tip:shipyard: b', 'tip:turning:'],
   [k for k, _v in doubles])
ck('nessun tab (sorgente e traduzione)',
   not [u['idx'] for u in su if '\t' in u['english']] and not [u['idx'] for u in tu if '\t' in u['italian']])
a = sum(u['english'].count('"') for u in su)
b = sum(u['italian'].count('"') for u in tu)
ck('virgolette: %d = %d (22)' % (a, b), a == b == 22, (a, b))
ck('virgolette per unita', not [u for u in tu if u['english'].count('"') != u['italian'].count('"')])
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
grp = {}
for u in su:
    grp.setdefault(u['english'], []).append(u['idx'])
ck('ZERO ripetizioni (asserito vuoto)', not [v for v in grp.values() if len(v) > 1])
ck('registro approvato: nessun «voi»',
   not [u['idx'] for u in tu if re.search(r'\b(avete|potete|potrete|siete|vostro|vostra|vostri|vostre)\b',
                                          u['italian'])])
LOW = ' '.join(u['italian'] for u in tu).lower()
for t in ('scudi', 'scafo', 'energia', 'calore', 'carburante', 'spinta', 'virata', 'torrette', 'cannoni',
          'emporio', 'deposito'):
    ck('termine chiave presente: %s' % t, t in LOW)
merged = {}
for f in sorted(glob.glob(os.path.join(HERE, 'parts', 'part*.json'))):
    for kk, v in json.load(open(f, encoding='utf-8')).items():
        merged[int(kk)] = v
ck('le tre parti ricostruiscono translation.json (1..96)',
   sorted(merged) == list(range(1, 97))
   and {i: v for i, v in merged.items()} == {u['idx']: u['italian'] for u in tu})
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('parole EN %d -> IT %d · sha256[:16] %s' % (sum(len(u['english'].split()) for u in tu),
      sum(len(u['italian'].split()) for u in tu), h[:16]))
print()
print('FAIL:', len(fail), '·', 'verify L113 superato' if not fail else 'verify L113 fallito')
raise SystemExit(0 if not fail else 1)
