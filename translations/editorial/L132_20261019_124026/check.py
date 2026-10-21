r"""check.py — L132 (`data/hai/unfettered side missions.txt`, 84 unita', righe 17-229)

Primo lotto del file: **2 contesti** (`Unfettered returning home` 18, `Hai Legacy 1` 66), **78 `MISSION_TEXT`**, **3
`UI_LABEL`**, **1 `DESCRIPTION`**, **1 `DIALOG`**, **1 `LOGBOOK`**, **zero `VALUE`**.

Controlli propri:

- **89 virgolette** su 84 unita' (43 senza, 33 con 2, 5 con 4, **3 con una sola**: 57, 62, 73 — battute non chiuse
  dal sorgente, riprodotte);
- **3 `UI_LABEL`** (`train back`, `tell me`, `try again`) identiche;
- **una resa identica dichiarata**: `(No.)` -> `(No.)`, perche' in italiano e' la stessa stringa (`ID_OK`);
- **zero `VALUE`**: asserzione vuota scritta;
- **8 token in 4 famiglie**, con `<last>` quattro volte: sequenza per unita'.
"""
import collections
import json
import os
import re
import sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
units = sorted(src['units'], key=lambda x: x['line'])
tr = {}
parts = sorted(f for f in os.listdir(os.path.join(HERE, 'parts')) if f.endswith('.json'))
for p in parts:
    for k, v in json.load(open(os.path.join(HERE, 'parts', p), encoding='utf-8')).items():
        tr[int(k)] = v
out = {'block': src['block'], 'note': src['note'], 'units': []}
missing = [u['idx'] for u in units if u['idx'] not in tr]
for u in units:
    if u['idx'] not in tr:
        continue
    it = tr[u['idx']]
    out['units'].append({"idx": u['idx'], "id": u['id'], "path": u['path'], "line": u['line'],
                         "kind": u['kind'], "context": u['context'], "english": u['english'],
                         "italian": it, "ratio": round(len(it) / max(1, len(u['english'])), 3)})
open(os.path.join(HERE, 'translation.json'), 'w', encoding='utf-8').write(
    json.dumps(out, ensure_ascii=False, indent=1))
cov = out['units']
by = {v['idx']: v for v in cov}
TAGS = re.compile(r'<[^<>]+>')
LAB = [39, 43, 48]
ID_OK = [4]
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 84/84", len(cov) == 84 == len(units) and not missing, '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
kk = collections.Counter(u['kind'] for u in units)
ck('tipi: 78 MISSION_TEXT · 3 UI_LABEL · 1 DESCRIPTION · 1 DIALOG · 1 LOGBOOK',
   dict(kk) == {'MISSION_TEXT': 78, 'UI_LABEL': 3, 'DESCRIPTION': 1, 'DIALOG': 1, 'LOGBOOK': 1}, dict(kk))
ck('le 3 UI_LABEL sono identiche al sorgente',
   [u['idx'] for u in units if u['kind'] == 'UI_LABEL'] == LAB
   and [by[i]['italian'] for i in LAB] == ['train back', 'tell me', 'try again'],
   [(i, by[i]['italian']) for i in LAB])
ck('la resa identica dichiarata: (No.) -> (No.)',
   by[4]['italian'].lstrip('\t') == by[4]['english'].lstrip('\t') == '(No.)')
ck('ZERO VALUE (asserzione vuota scritta)', [u['idx'] for u in units if u['kind'] == 'VALUE'] == [])
ck('tutte le unita prosaiche sono tradotte',
   not [v['idx'] for v in cov if v['idx'] not in LAB + ID_OK and v['italian'].strip() == v['english'].strip()])
tabs = [v['idx'] for v in cov if v['english'].startswith('\t')]
ck('74 unita iniziano con tab, le stesse in traduzione',
   len(tabs) == 74 and tabs == [v['idx'] for v in cov if v['italian'].startswith('\t')], len(tabs))
ck('spazi iniziali e finali identici al sorgente (84/84)',
   not [v['idx'] for v in cov
        if len(v['italian']) - len(v['italian'].rstrip()) != len(v['english']) - len(v['english'].rstrip())])
ck('89 virgolette in inglese e in italiano',
   sum(v['english'].count('"') for v in cov) == 89 == sum(v['italian'].count('"') for v in cov),
   (sum(v['english'].count('"') for v in cov), sum(v['italian'].count('"') for v in cov)))
ck('virgolette per unita: stesso numero',
   not [v['idx'] for v in cov if v['english'].count('"') != v['italian'].count('"')],
   [(v['idx'], v['english'].count('"'), v['italian'].count('"')) for v in cov
    if v['english'].count('"') != v['italian'].count('"')])
odd = [v['idx'] for v in cov if v['english'].count('"') % 2]
ck('tre unita con una sola virgoletta (57, 62, 73), riprodotte',
   odd == [57, 62, 73] and all(by[i]['italian'].count('"') == 1 for i in odd), odd)
ck('distribuzione delle virgolette: 43 senza, 33 con 2, 5 con 4, 3 con 1',
   collections.Counter(v['english'].count('"') for v in cov) == {0: 43, 2: 33, 4: 5, 1: 3},
   collections.Counter(v['english'].count('"') for v in cov))
tok = collections.Counter(t for v in cov for t in TAGS.findall(v['english']))
ck('8 token in 4 famiglie', dict(tok) == {'<last>': 4, '<destination>': 2, '<first>': 1, '<payment>': 1}, dict(tok))
ck('token per unita: sequenza identica',
   not [v['idx'] for v in cov if TAGS.findall(v['english']) != TAGS.findall(v['italian'])],
   [(v['idx'], TAGS.findall(v['english']), TAGS.findall(v['italian'])) for v in cov
    if TAGS.findall(v['english']) != TAGS.findall(v['italian'])])
ck('ZERO quadre e zero backtick (asserito)',
   not [v['idx'] for v in cov if any(c in v['english'] + v['italian'] for c in '[]`')])
seen = collections.OrderedDict()
for u in units:
    seen[u['context']] = seen.get(u['context'], 0) + 1
ck('2 contesti: 18 / 66',
   list(seen.items()) == [('mission:Unfettered returning home', 18), ('mission:Hai Legacy 1', 66)],
   list(seen.items()))
ck('prima e ultima unita: righe 17 e 229', (cov[0]['line'], cov[-1]['line']) == (17, 229),
   (cov[0]['line'], cov[-1]['line']))
grp = {}
for v in cov:
    grp.setdefault(v['english'].lstrip('\t'), set()).add(v['italian'])
ck('82 testi distinti su 84 unita', len(grp) == 82, len(grp))
ck('stesso inglese => stessa resa',
   not [(k, v) for k, v in grp.items() if len(v) > 1], [(k[:40], v) for k, v in grp.items() if len(v) > 1])
LOW = ' '.join(v['italian'] for v in cov).lower()
TERMS = ('unfettered', 'hai-home', 'anomalocaris', 'korath', 'cantiere', 'spiaggia', 'grotta', 'portello',
         'tributo', 'crediti', 'capitano', 'flotta')
ck('terminologia presente: 12 termini chiave', all(t in LOW for t in TERMS), [t for t in TERMS if t not in LOW])
ck('Hai-home resta nome proprio (non tradotto)', 'hai-home' in LOW and 'casa degli hai' not in LOW)
NOSCRUB = ' '.join(TAGS.sub('""', v['italian']) for v in cov if v['idx'] not in LAB)
for s in ('Hai', 'Unfettered', 'Unfettered', 'Anomalocaris', 'Korath', 'Hai-home'):
    NOSCRUB = NOSCRUB.replace(s, '@@')
NOSCRUB = NOSCRUB.lower()
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' ship ', ' you ')
ck('nessun residuo inglese fuori dai nomi propri',
   not [w for w in ENGW if w in NOSCRUB], [w for w in ENGW if w in NOSCRUB])
CORT = re.findall(r'\bLei\b|(?<![.!?] )\b(?:Suo|Sua|Suoi|Sue)\b', ' '.join(v['italian'] for v in cov))
ck('nessuna forma di cortesia «Lei»', not CORT, CORT)
rs = [v['ratio'] for v in cov]
ck('rapporto nel gate', 0.55 < min(rs) and max(rs) < 1.90, '%.2f - %.2f' % (min(rs), max(rs)))
bad = [(v['idx'], n) for v in cov for p, n in ((r"\b(e|piu|perche|cosi|gia|puo|cioe|percio|fa)'", 'accento'),
       ('\u2026', 'ellissi'), ('\u2014', 'em dash'), ('\u2019', 'apostrofo curvo'), ('\u00ab', 'caporale'),
       ('\u00bb', 'caporale')) if re.search(p, v['italian'])]
ck('tipografia', not bad, bad)
nonlat = [v['idx'] for v in cov for c in v['italian'] if ord(c) > 127 and not 0x00C0 <= ord(c) <= 0x024F]
ck('caratteri non latini', not nonlat, nonlat)
c = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
st = dict(c.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('tutte le 84 unita sono PENDING nel database (misurato)',
   c.execute('select count(*) from units where id in (%s) and state != "PENDING"'
             % ','.join('?' * len(units)), [u['id'] for u in units]).fetchone()[0] == 0)
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d' % (sum(len(v['english'].split()) for v in cov),
                                 sum(len(v['italian'].split()) for v in cov)))
print('righe %d/%d · parti %d · mancanti %d' % (min(u['line'] for u in units), max(u['line'] for u in units),
      len(parts), len(missing)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
