r"""verify.py — L126 (`data/incipias/incipias first contact.txt`, 55 unita', righe 22-218)

Invariante di **segmento** (il file non si chiude): **161 unità** totali, **0 prima** della riga 22, **106 dopo** la
218, confine alla riga **224** (`mission:Incipias: Help The Stranded 1`). Ricalcolato dal repository e da `state.db`.

Misure proprie: **48 `MISSION_TEXT`**, **4 `UI_LABEL`** identiche, **3 `LOGBOOK`**, **6 contesti**, **52 testi
distinti**, **37 unità con tab**, **65 virgolette**, **zero token**.
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
PATH = 'data/incipias/incipias first contact.txt'
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
ck('idx 1..55 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 56)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 55 righe 22 - 218', len(tu) == 55 and (first, last) == (22, 218), (len(tu), first, last))
tot = db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0]
before = db.execute('select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0]
after = db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0]
maxl = db.execute('select max(line) from units where path=?', (PATH,)).fetchone()[0]
ck('file: 161 unita, max(line) = 439', tot == 161 and maxl == 439, (tot, maxl))
ck('0 unita prima della riga 22 (apre il file)', before == 0, before)
ck('106 unita dopo la riga 218', after == 106, after)
ck('il confine: la riga 224 apre mission:Incipias: Help The Stranded 1',
   db.execute('select line,context from units where path=? and line>? order by line limit 1',
              (PATH, last)).fetchone() == (224, 'mission:Incipias: Help The Stranded 1'))
ck('tipi: 48 MISSION_TEXT · 4 UI_LABEL · 3 LOGBOOK',
   collections.Counter(u['kind'] for u in su) == {'MISSION_TEXT': 48, 'UI_LABEL': 4, 'LOGBOOK': 3},
   collections.Counter(u['kind'] for u in su))
LAB = [u['idx'] for u in su if u['kind'] == 'UI_LABEL']
ck('le 4 UI_LABEL (30, 32, 34, 39) sono identiche al sorgente',
   LAB == [30, 32, 34, 39]
   and [by[i]['italian'] for i in LAB] == ['ut divitas', 'spec inci', 'both planets', 'new species'])
ck('tutte PENDING',
   not [u['idx'] for u in su
        if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('tutte le unita prosaiche sono tradotte',
   not [u['idx'] for u in tu if u['kind'] != 'UI_LABEL' and u['italian'].strip() == u['english'].strip()])
tabs = [u['idx'] for u in su if u['english'].startswith('\t')]
ck('37 unita con tab iniziale, le stesse in traduzione',
   len(tabs) == 37 and tabs == [u['idx'] for u in tu if u['italian'].startswith('\t')], len(tabs))
ck('conteggio dei tab identico per unita',
   not [u['idx'] for u in tu if u['english'].count('\t') != u['italian'].count('\t')])
ck('65 virgolette, con l unita 23 a 3 (una in piu nel sorgente)',
   sum(u['english'].count('"') for u in su) == 65 == sum(u['italian'].count('"') for u in tu)
   and by[23]['italian'].count('"') == 3 and by[23]['english'].count('"') == 3)
ck('ZERO token (asserito)', collections.Counter(t for u in su for t in TAGS.findall(u['english'])) == {}
   == collections.Counter(t for u in tu for t in TAGS.findall(u['italian'])))
ck('nessun backtick e nessuna quadra nella traduzione',
   not [u for u in tu if '`' in u['italian'] or '[' in u['italian'] or ']' in u['italian']])
seen = collections.Counter(u['context'] for u in su)
ck('6 contesti: 23 / 13 / 13 / 2 / 2 / 2',
   len(seen) == 6 and sorted(seen.values()) == [2, 2, 2, 13, 13, 23], sorted(seen.values()))
grp = collections.Counter(u['english'] for u in su)
ck('52 testi inglesi distinti per 55 unita', len(grp) == 52, len(grp))
ck('nessun gruppo con due rese diverse',
   not [k for k in grp if len({by[u['idx']]['italian'] for u in su if u['english'] == k}) > 1])
it_grp = {}
for u in tu:
    it_grp.setdefault(u['italian'], []).append(u)
ck('nessun duplicato italiano non spiegato dal sorgente',
   not [g for g in it_grp.values() if len(g) > 1 and len({v['english'] for v in g}) > 1])
NONLAT = re.compile(r'[^\x00-\x7F\u00C0-\u024F]')
ck('nessun carattere non latino', not [u for u in tu if NONLAT.search(u['italian'])])
ck('nessun trattino lungo, virgoletta curva o ellissi tipografica',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate', 0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
ck('registro approvato: nessun «voi»',
   not [u['idx'] for u in tu if re.search(r'\b(avete|potete|potrete|siete|vostro|vostra|vostri|vostre)\b',
                                          u['italian'])])
merged = {}
for f in sorted(os.listdir(os.path.join(HERE, 'parts'))):
    if f.endswith('.json'):
        for k, v in json.load(open(os.path.join(HERE, 'parts', f), encoding='utf-8')).items():
            merged[int(k)] = v
ck('le tre parti ricostruiscono translation.json (1..55)',
   sorted(merged) == list(range(1, 56)) and merged == {u['idx']: u['italian'] for u in tu})
ck('nessun altro lotto rivendica queste righe',
   not [f for f in os.listdir(os.path.join(L10N, 'staging/editorial'))
        if f.startswith('L') and os.path.exists(os.path.join(L10N, 'staging/editorial', f, 'translation.json'))
        and f != os.path.basename(HERE)
        and any(u['path'] == PATH and 22 <= u['line'] <= 218
                for u in json.load(open(os.path.join(L10N, 'staging/editorial', f, 'translation.json'),
                                        encoding='utf-8'))['units'])])
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('copertura file: 55/161 (34.2%) · segmento (22, 218) · 106 unita dopo')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L126 superato' if not fail else 'verify L126 fallito')
raise SystemExit(0 if not fail else 1)
