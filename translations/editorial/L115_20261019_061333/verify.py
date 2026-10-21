r"""verify.py — L115 (data/_ui/tooltips.txt, 104 unita', righe 1312-1566)

Invariante di **segmento**, indipendente da `check.py`: rilegge il repository originale, `state.db`, i
`parts/` e `translation.json`, e ricalcola tutto.

Misure attese: **430 unita' prima** della riga 1312 (L111-L114), **133 dopo** la 1566, file di **667 unita'**,
`max_line = 1865`, confine alla riga **1569** (`tip:   Show flagship overlay`). **104 `TUTORIAL_TIP`**, tutte
`PENDING`, **72 contesti** (56/7/5/2/1/1, massimo 6), **82 virgolette** in 38 unita' con i testi citati
identici all'inglese (eccezione dichiarata: unita' 10), **8 token** `<shift>`, **zero tab**, **zero quadre**,
**una coppia** di ripetizioni (89/92) resa identica.
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
ck('idx 1..104 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 105)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 104 righe 1312 - 1566', len(tu) == 104 and (first, last) == (1312, 1566), (len(tu), first, last))
tot = db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0]
before = db.execute('select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0]
after = db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0]
maxl = db.execute('select max(line) from units where path=?', (PATH,)).fetchone()[0]
ck('430 unita prima della riga 1312 (L111-L114)', before == 430, before)
ck('133 unita dopo la riga 1566', after == 133, after)
ck('file: 667 unita, max(line) = 1865', tot == 667 and maxl == 1865, (tot, maxl))
ck('il confine: la riga 1569 apre tip:   Show flagship overlay',
   db.execute('select line,context from units where path=? and line>? order by line limit 1',
              (PATH, last)).fetchone() == (1569, 'tip:   Show flagship overlay'))
ck('tipo unico: 104 TUTORIAL_TIP',
   collections.Counter(u['kind'] for u in su) == {'TUTORIAL_TIP': 104},
   collections.Counter(u['kind'] for u in su))
ck('tutte PENDING',
   not [u['idx'] for u in su
        if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
by = {u['idx']: u for u in tu}
ck('nessuna unita identica al sorgente',
   not [u['idx'] for u in tu if u['italian'].strip() == u['english'].strip()])
# --- contesti: 72 per 104 unita' ----------------------------------------------------------
seen = collections.Counter(u['context'] for u in su)
ck('72 contesti distinti (104 unita)', len(seen) == 72, len(seen))
ck('distribuzione 56/7/5/2/1/1 e massimo 6',
   collections.Counter(seen.values()) == {1: 56, 2: 7, 3: 5, 4: 2, 5: 1, 6: 1},
   collections.Counter(seen.values()))
ck('nessun tab (sorgente e traduzione)',
   not [u['idx'] for u in su if '\t' in u['english']] and not [u['idx'] for u in tu if '\t' in u['italian']])
a = sum(u['english'].count('"') for u in su)
b = sum(u['italian'].count('"') for u in tu)
ck('virgolette: %d = %d (82)' % (a, b), a == b == 82, (a, b))
ck('virgolette per unita', not [u for u in tu if u['english'].count('"') != u['italian'].count('"')],
   [(u['idx'], u['english'].count('"'), u['italian'].count('"'))
    for u in tu if u['english'].count('"') != u['italian'].count('"')])
ck('38 unita citano, la 35 con otto virgolette',
   sum(1 for u in tu if u['italian'].count('"')) == 38
   and [u['idx'] for u in tu if u['italian'].count('"') == 8] == [35])
ck('le citazioni sono chiavi/valori identici all\'inglese (eccezione: 10)',
   not [u['idx'] for u in tu if u['idx'] != 10 and QUOTED.findall(u['italian']) != QUOTED.findall(u['english'])]
   and QUOTED.findall(by[10]['italian']) == ['picco']
   and QUOTED.findall(by[10]['english']) == ['surge'],
   (QUOTED.findall(by[10]['italian']), QUOTED.findall(by[10]['english'])))
ck('ZERO token estranei: solo <shift> (8 = 8)',
   collections.Counter(t for u in su for t in TAGS.findall(u['english']))
   == collections.Counter(t for u in tu for t in TAGS.findall(u['italian'])) == {'<shift>': 8},
   collections.Counter(t for u in tu for t in TAGS.findall(u['italian'])))
ck('token per unita', [u['idx'] for u in tu if '<shift>' in u['italian']]
   == [u['idx'] for u in su if '<shift>' in u['english']])
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
# --- ripetizioni: una coppia ricalcolata dal sorgente ------------------------------------
grp = {}
for u in su:
    grp.setdefault(u['english'], []).append(u['idx'])
pairs = sorted(v for v in grp.values() if len(v) > 1)
ck('una sola coppia di ripetizioni (89/92)', pairs == [[89, 92]], pairs)
ck('la coppia e resa identica', by[89]['italian'] == by[92]['italian'])
it_grp = {}
for u in tu:
    it_grp.setdefault(u['italian'], []).append(u)
ck('nessun duplicato italiano non spiegato dal sorgente',
   not [g for g in it_grp.values() if len(g) > 1 and len({v['english'] for v in g}) > 1])
ck('registro approvato: nessun «voi»',
   not [u['idx'] for u in tu if re.search(r'\b(avete|potete|potrete|siete|vostro|vostra|vostri|vostre)\b',
                                          u['italian'])])
LOW = ' '.join(u['italian'] for u in tu).lower()
for t in ('ammiraglia', 'propulsori', 'virata', 'scudi', 'scafo', 'flotta', 'scorte', 'caccia', 'detrito',
          'carburante', 'energia', 'occultamento', 'impostazione', 'pannello', 'zoom', 'postbruciatore'):
    ck('termine chiave presente: %s' % t, t in LOW)
merged = {}
for f in sorted(glob.glob(os.path.join(HERE, 'parts', 'part*.json'))):
    for kk, v in json.load(open(f, encoding='utf-8')).items():
        merged[int(kk)] = v
ck('le tre parti ricostruiscono translation.json (1..104)',
   sorted(merged) == list(range(1, 105))
   and {i: v for i, v in merged.items()} == {u['idx']: u['italian'] for u in tu})
print('copertura file: %d/667 (%.1f%%)' % (430 + 104, 100.0 * 534 / 667))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('parole EN %d -> IT %d · sha256[:16] %s' % (sum(len(u['english'].split()) for u in tu),
      sum(len(u['italian'].split()) for u in tu), h[:16]))
print()
print('FAIL:', len(fail), '·', 'verify L115 superato' if not fail else 'verify L115 fallito')
raise SystemExit(0 if not fail else 1)
