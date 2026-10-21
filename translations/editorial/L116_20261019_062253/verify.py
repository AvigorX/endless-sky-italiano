r"""verify.py — L116 (data/_ui/tooltips.txt, 133 unita', righe 1569-1865) — **invariante di FILE**

Questo lotto **chiude il file**, quindi il verify non si limita al segmento: legge **tutti** i
`translation.json` dello staging che riguardano `data/_ui/tooltips.txt` (sei lotti, L111-L116) e dimostra che

- le unita' coperte sono **667 su 667** (nessuna mancante, nessuna doppia: `sovrapposti = 0`);
- i lotti sono **sei** e il segmento di questo lotto e' la coda `(1569, 1865)`, con **0 unita' dopo**;
- `max(line) = 1865`;
- il file originale non e' stato toccato (riga grezza identica) e il DB non e' stato scritto (tutte `PENDING`).

Misure del lotto: **133 `TUTORIAL_TIP`**, **80 contesti** (62/1/4/8/5), **144 virgolette** in 66 unita' con i
testi citati identici all'inglese (compresa la virgola interna di `"ship cap,"`), **1 token** `<shift>`,
**zero tab**, **zero quadre**, **zero ripetizioni**.
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
QUOTED = re.compile(r'"([^"]*)"')
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
ck('idx 1..133 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 134)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 133 righe 1569 - 1865', len(tu) == 133 and (first, last) == (1569, 1865), (len(tu), first, last))
tot = db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0]
before = db.execute('select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0]
after = db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0]
maxl = db.execute('select max(line) from units where path=?', (PATH,)).fetchone()[0]
ck('534 unita prima della riga 1569 (L111-L115)', before == 534, before)
ck('0 unita dopo la riga 1865: e la coda del file', after == 0, after)
ck('file: 667 unita, max(line) = 1865', tot == 667 and maxl == 1865, (tot, maxl))
ck('nessuna unita del file dopo la riga finale dichiarata',
   db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0] == 0)
ck('tipo unico: 133 TUTORIAL_TIP',
   collections.Counter(u['kind'] for u in su) == {'TUTORIAL_TIP': 133},
   collections.Counter(u['kind'] for u in su))
ck('tutte PENDING',
   not [u['idx'] for u in su
        if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
# --- invariante di FILE: i sei lotti coprono tutte le 667 unita', senza sovrapporsi ---------
allu = db.execute('select id from units where path=?', (PATH,)).fetchall()
ids_path = {r[0] for r in allu}
lots = {}
for f in sorted(glob.glob(os.path.join(L10N, 'staging/editorial/L*', 'translation.json'))):
    d = json.load(open(f, encoding='utf-8'))['units']
    if not d or d[0]['path'] != PATH:
        continue
    lots[os.path.basename(os.path.dirname(f))] = {u['id'] for u in d}
covered = collections.Counter(i for s in lots.values() for i in s)
ck('sei lotti su tooltips.txt (L111-L116)', len(lots) == 6, sorted(lots))
ck('le unita coperte sono 667 su 667',
   len(covered) == 667 == len(ids_path) and set(covered) == ids_path,
   (len(covered), len(ids_path), len(ids_path - set(covered))))
ck('nessuna unita coperta due volte (sovrapposti = 0)', max(covered.values()) == 1,
   [i for i, n in covered.items() if n > 1][:5])
ck('questo lotto copre la coda 1569-1865',
   {u['id'] for u in tu} == lots[os.path.basename(HERE)],
   (len(lots[os.path.basename(HERE)]), len(tu)))
by = {u['idx']: u for u in tu}
ck('nessuna unita identica al sorgente',
   not [u['idx'] for u in tu if u['italian'].strip() == u['english'].strip()])
# --- contesti: 80 per 133 unita' ----------------------------------------------------------
seen = collections.Counter(u['context'] for u in su)
ck('80 contesti distinti (133 unita)', len(seen) == 80, len(seen))
ck('distribuzione 62/1/4/8/5 e massimo 5',
   collections.Counter(seen.values()) == {1: 62, 2: 1, 3: 4, 4: 8, 5: 5},
   collections.Counter(seen.values()))
ck('i primi contesti hanno tre spazi iniziali',
   su[0]['context'] == 'tip:   Show flagship overlay' and tu[0]['context'] == su[0]['context'],
   tu[0]['context'])
ck('nessun tab (sorgente e traduzione)',
   not [u['idx'] for u in su if '\t' in u['english']] and not [u['idx'] for u in tu if '\t' in u['italian']])
a = sum(u['english'].count('"') for u in su)
b = sum(u['italian'].count('"') for u in tu)
ck('virgolette: %d = %d (144)' % (a, b), a == b == 144, (a, b))
ck('virgolette per unita', not [u for u in tu if u['english'].count('"') != u['italian'].count('"')],
   [(u['idx'], u['english'].count('"'), u['italian'].count('"'))
    for u in tu if u['english'].count('"') != u['italian'].count('"')])
ck('66 unita citano (61x2, 4x4, 1x6)',
   collections.Counter(u['italian'].count('"') for u in tu if u['italian'].count('"')) == {2: 61, 4: 4, 6: 1},
   collections.Counter(u['italian'].count('"') for u in tu if u['italian'].count('"')))
ck('le citazioni sono identiche all\'inglese (nessuna eccezione)',
   not [u['idx'] for u in tu if QUOTED.findall(u['italian']) != QUOTED.findall(u['english'])])
ck('virgola interna riprodotta in 122-124',
   [QUOTED.findall(by[i]['italian'])[0] for i in (122, 123, 124)] == ['ship cap,', 'crew cap,', 'admin cap,'])
ck('UN token <shift> (1 = 1), nella stessa unita',
   collections.Counter(t for u in su for t in TAGS.findall(u['english']))
   == collections.Counter(t for u in tu for t in TAGS.findall(u['italian'])) == {'<shift>': 1}
   and [u['idx'] for u in tu if '<shift>' in u['italian']] == [u['idx'] for u in su if '<shift>' in u['english']],
   collections.Counter(t for u in tu for t in TAGS.findall(u['italian'])))
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
grp = collections.Counter(u['english'] for u in su)
ck('ZERO ripetizioni (asserito vuoto)', not [k for k, v in grp.items() if v > 1])
it_grp = {}
for u in tu:
    it_grp.setdefault(u['italian'], []).append(u)
ck('nessun duplicato italiano non spiegato dal sorgente',
   not [g for g in it_grp.values() if len(g) > 1 and len({v['english'] for v in g}) > 1])
ck('registro approvato: nessun «voi»',
   not [u['idx'] for u in tu if re.search(r'\b(avete|potete|potrete|siete|vostro|vostra|vostri|vostre)\b',
                                          u['italian'])])
LOW = ' '.join(u['italian'] for u in tu).lower()
for t in ('ammiraglia', 'scorte', 'flotta', 'detrito', 'munizioni', 'carburante', 'scudi', 'scafo',
          'sovrapposizione', 'impostazione', 'salvataggio', 'pilota'):
    ck('termine chiave presente: %s' % t, t in LOW)
merged = {}
for f in sorted(glob.glob(os.path.join(HERE, 'parts', 'part*.json'))):
    for kk, v in json.load(open(f, encoding='utf-8')).items():
        merged[int(kk)] = v
ck('le quattro parti ricostruiscono translation.json (1..133)',
   sorted(merged) == list(range(1, 134))
   and {i: v for i, v in merged.items()} == {u['idx']: u['italian'] for u in tu})
print('copertura file: 667/667 (100.0%) · prima 534 + lotto 133')
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('parole EN %d -> IT %d · sha256[:16] %s' % (sum(len(u['english'].split()) for u in tu),
      sum(len(u['italian'].split()) for u in tu), h[:16]))
print()
print('FAIL:', len(fail), '·', 'verify L116 superato: file chiuso' if not fail else 'verify L116 fallito')
raise SystemExit(0 if not fail else 1)
