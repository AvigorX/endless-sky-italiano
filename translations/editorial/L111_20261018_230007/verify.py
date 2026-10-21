r"""verify.py — L111 (data/_ui/tooltips.txt, 104 unita', righe 16-328)

Invariante di **segmento**, indipendente da `check.py`: rilegge il repository originale, `state.db` e i `parts/`.

Misure attese: **0 unita' prima** della riga 16 (primo lotto del file), **563 dopo la 328**, file di **667**
unita', `max(line) = 1865`, confine alla riga **331** (`tip:hull heat:`). **104 `TUTORIAL_TIP`**, **104 contesti**
distinti, **zero token**, **zero tab**, **14 virgolette**, zero ripetizioni.

**Il lotto attraversa due stati**: le prime **52** unita' sono `APPROVED` nel database e il loro testo va
riprodotto **alla lettera**; le altre **52** sono `PENDING` e sono tradotte qui. Il `verify.py` lo verifica
rileggendo il database, non fidandosi del `check.py`.
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
ck('idx 1..104 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 105)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 104 righe 16 - 328', len(tu) == 104 and (first, last) == (16, 328), (len(tu), first, last))
tot = db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0]
before = db.execute('select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0]
after = db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0]
maxl = db.execute('select max(line) from units where path=?', (PATH,)).fetchone()[0]
ck('0 unita prima della riga 16 (primo lotto del file)', before == 0, before)
ck('563 unita dopo la riga 328', after == 563, after)
ck('file: 667 unita, max(line) = 1865', tot == 667 and maxl == 1865, (tot, maxl))
ck('il confine: la riga 331 apre tip:hull heat:',
   db.execute('select line,context from units where path=? and line>? order by line limit 1',
              (PATH, last)).fetchone() == (331, 'tip:hull heat:'))
ck('tipo unico: 104 TUTORIAL_TIP',
   collections.Counter(u['kind'] for u in su) == {'TUTORIAL_TIP': 104},
   collections.Counter(u['kind'] for u in su))
by = {u['idx']: u for u in tu}
# --- APPROVED / PENDING, ricalcolati qui ---------------------------------------------------
dbst, dbit = {}, {}
for u in su:
    r = db.execute('select state, italian from units where id=?', (u['id'],)).fetchone()
    dbst[u['idx']], dbit[u['idx']] = r[0], r[1]
appr = sorted(i for i in dbst if dbst[i] == 'APPROVED')
pend = sorted(i for i in dbst if dbst[i] == 'PENDING')
ck('52 APPROVED (1-52) e 52 PENDING (53-104)',
   appr == list(range(1, 53)) and pend == list(range(53, 105)), (len(appr), len(pend)))
ck('i 52 APPROVED riproducono il testo del DB, carattere per carattere',
   all(by[i]['italian'].strip() == (dbit[i] or '').strip() for i in appr)
   and all((dbit[i] or '').strip() for i in appr),
   [i for i in appr if by[i]['italian'].strip() != (dbit[i] or '').strip()])
ck('i 52 PENDING sono tradotti e diversi dal sorgente',
   all(by[i]['italian'].strip() != by[i]['english'].strip() for i in pend),
   [i for i in pend if by[i]['italian'].strip() == by[i]['english'].strip()])
ck('le PENDING non usano il «voi» (coerenza col blocco approvato)',
   not [i for i in pend if re.search(r'\b(avete|potete|potrete|siete|vostro|vostra|vostri|vostre)\b',
                                     by[i]['italian'])])
ck('nessuna unita PENDING resta in inglese e nessuna APPROVED e vuota',
   all(by[i]['italian'].strip() for i in dbst))
# ----------------------------------------------------------------------------------------
ctxs = []
for u in su:
    if u['context'] not in ctxs:
        ctxs.append(u['context'])
ck('104 contesti, uno per unita, tutti distinti e tutti tip:',
   len(ctxs) == 104 == len(set(ctxs)) and all(c.startswith('tip:') for c in ctxs), len(ctxs))
ck('nessun tab in tutto il lotto (sorgente e traduzione)',
   not [u['idx'] for u in su if '\t' in u['english']] and not [u['idx'] for u in tu if '\t' in u['italian']])
a = sum(u['english'].count('"') for u in su)
b = sum(u['italian'].count('"') for u in tu)
ck('virgolette: %d = %d (14)' % (a, b), a == b == 14, (a, b))
ck('virgolette per unita', not [u for u in tu if u['english'].count('"') != u['italian'].count('"')])
ck('ZERO token (asserito vuoto)',
   not [t for u in su for t in TAGS.findall(u['english'])]
   and not [t for u in tu for t in TAGS.findall(u['italian'])])
ck('ZERO quadre (asserito vuoto)', not [u['idx'] for u in tu if '[' in u['italian'] or ']' in u['italian']])
ck('nessun backtick', not [u for u in tu if '`' in u['italian']])
ck('nessuna traduzione vuota', all(u['italian'].strip() for u in tu))
NONLAT = re.compile(r'[^\x00-\x7F\u00C0-\u024F]')
ck('nessun carattere non latino', not [u for u in tu if NONLAT.search(u['italian'])])
ck('nessun trattino lungo o virgoletta curva nelle PENDING',
   not [i for i in pend if any(c in by[i]['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB')])
rs = [by[i]['ratio'] for i in pend]
ck('rapporto nel gate, sole unita PENDING', 0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
print('rapporto IT/EN (PENDING): min %.2f max %.2f' % (min(rs), max(rs)))
grp = {}
for u in su:
    grp.setdefault(u['english'], []).append(u['idx'])
ck('ZERO ripetizioni (asserito vuoto)', not [v for v in grp.values() if len(v) > 1])
LOW = ' '.join(u['italian'] for u in tu).lower()
TERMS = ('massa', 'accelerazione', 'energia', 'calore', 'raffreddamento', 'carburante', 'scafo',
         'scudi', 'occultamento', 'equipaggiamento', 'tonnellate', 'equipaggio')
ck('terminologia dei pannelli presente (12 termini)', all(t in LOW for t in TERMS),
   [t for t in TERMS if t not in LOW])
merged = {}
for f in sorted(glob.glob(os.path.join(HERE, 'parts', 'part*.json'))):
    for kk, v in json.load(open(f, encoding='utf-8')).items():
        merged[int(kk)] = v
ck('le quattro parti ricostruiscono translation.json (1..104)',
   sorted(merged) == list(range(1, 105))
   and {i: v for i, v in merged.items()} == {u['idx']: u['italian'] for u in tu})
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('parole EN %d -> IT %d · sha256[:16] %s' % (sum(len(u['english'].split()) for u in tu),
      sum(len(u['italian'].split()) for u in tu), h[:16]))
print()
print('FAIL:', len(fail), '·', 'verify L111 superato' if not fail else 'verify L111 fallito')
raise SystemExit(0 if not fail else 1)
