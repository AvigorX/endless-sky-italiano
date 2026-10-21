r"""check.py — L204 (`data/hai/hai outfits.txt`, 19 unita', righe 603-788). Quarto lotto del file.

**13 `DESCRIPTION`** e **6 `VALUE`** (batterie Hai e il set `"Baellie"`). **Zero segnaposto**, **zero tab**.
**6 virgolette**, tutte in due unita': l'unita' 15 e' un `VALUE` con virgolette **dentro il nome**
(`"Baellie" Atomic Engines`), l'unita' 16 ne porta quattro (`"Basrem"`, `"Baellie."`). Vanno conservate nei `VALUE`
e nel testo.

**Apici**: 2 inglesi (`ship's` unita' 6, `don't` unita' 14) contro **6 italiani** (elisione: unita' 2, 4, 6, 10, 17).

**Lessico**: `battery pack` -> «pacco batterie» (5 volte), `heat footprint` -> «impronta termica» (2 volte),
`Ion Cannon` e `Flea` invariati, `Deep` e `Korath` invariati.
"""
import collections
import json
import os
import re
import sqlite3

TAB = chr(9)
QUOTE = chr(34)
APOS = chr(39)
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
IT_ALL = ' '.join(v['italian'] for v in cov)
EN_ALL = ' '.join(v['english'] for v in cov)
EN_T = sum(len(TAGS.findall(v['english'])) for v in cov)
IT_T = sum(len(TAGS.findall(v['italian'])) for v in cov)
EN_Q = sum(v['english'].count(QUOTE) for v in cov)
IT_Q = sum(v['italian'].count(QUOTE) for v in cov)
EN_A = sum(v['english'].count(APOS) for v in cov)
IT_A = sum(v['italian'].count(APOS) for v in cov)
KINDS = collections.Counter(u['kind'] for u in units)
NAMES = ('Ion Cannon', 'Flea', 'Pebble Core', 'Sand Cell', 'Hai Shield Beetle', 'Korath', 'Deep',
         '"Baellie"', '"Basrem"')
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 19/19", len(cov) == 19 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 13 DESCRIPTION, 6 VALUE (asserzione scritta)',
   KINDS == {'DESCRIPTION': 13, 'VALUE': 6}, dict(KINDS))
ck('ZERO TEXT, DIALOG, UI_LABEL (asserzioni vuote scritte)',
   [u['idx'] for u in units if u['kind'] in ('TEXT', 'DIALOG', 'UI_LABEL')] == [])
ctx = [u['context'].replace('outfit:', '') for u in units]
ck('13 contesti distinti, da Hai Chasm Batteries a "Biroo" Atomic Thruster',
   len(set(ctx)) == 13 and (ctx[0], ctx[-1]) == ('Hai Chasm Batteries', '"Biroo" Atomic Thruster'),
   '%d · %s · %s' % (len(set(ctx)), ctx[0], ctx[-1]))
ck('righe 603 e 788 (prima e ultima del lotto)',
   (cov[0]['line'], cov[-1]['line']) == (603, 788), (cov[0]['line'], cov[-1]['line']))
ck('ZERO segnaposto e ZERO tab in entrambe le lingue (asserzioni vuote scritte)',
   EN_T == 0 == IT_T and '<' not in IT_ALL and '<' not in EN_ALL
   and [v['idx'] for v in cov if v['english'].startswith(TAB)] == []
   and [v['idx'] for v in cov if v['italian'].startswith(TAB)] == [])
ck('6 virgolette in entrambe le lingue, nelle stesse due unita\' (15 e 16)',
   EN_Q == 6 == IT_Q
   and [v['idx'] for v in cov if QUOTE in v['english']] == [15, 16]
   and [v['idx'] for v in cov if QUOTE in v['italian']] == [15, 16], (EN_Q, IT_Q))
ck("apici: 2 inglesi (ship's, don't: unita' 6 e 14) e 6 italiani (elisione: 2, 4, 6, 10, 17)",
   EN_A == 2 and IT_A == 6
   and [v['idx'] for v in cov if APOS in v['english']] == [6, 14]
   and [v['idx'] for v in cov if APOS in v['italian']] == [2, 4, 6, 10, 17], (EN_A, IT_A))
ck('nessun caporale e nessun carattere tipografico',
   not [v['idx'] for v in cov if any(c in v['italian'] for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026')])
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' you ', ' to the ', ' will be ',
        ' is ', ' are ', ' from the ', ' its ', ' it is ', ' such as ', ' rather than ', ' for a ', ' that ')
ck('nessun residuo inglese', not [w for w in ENGW if w in IT_ALL.lower()],
   [w for w in ENGW if w in IT_ALL.lower()])
CORT = re.findall(r'\bLei\b|(?<![.!?] )\b(?:Suo|Sua|Suoi|Sue)\b', IT_ALL)
ck('nessuna forma di cortesia «Lei»', not CORT, CORT)
rs = [v['ratio'] for v in cov]
ck('rapporto nel gate 0,55-1,90', 0.55 < min(rs) and max(rs) < 1.90, '%.2f - %.2f' % (min(rs), max(rs)))
ACC = re.compile(r"\b(e|piu|perche|cosi|gia|puo|cioe|percio|fa)'", re.I)
bad = [(v['idx'], ACC.search(v['italian']).group(0)) for v in cov if ACC.search(v['italian'])]
ck('tipografia (accenti veri, nessun apostrofo al posto dell\'accento)', not bad, bad)
nonlat = [v['idx'] for v in cov for c in v['italian'] if ord(c) > 127 and not 0x00C0 <= ord(c) <= 0x024F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio',
   not [v['idx'] for v in cov if v['italian'] != v['italian'].rstrip()
        or '  ' in v['italian'] or v['english'] != v['english'].rstrip()])
ck('6 VALUE identici all\'inglese, virgolette comprese',
   [v['idx'] for v in cov if v['kind'] == 'VALUE'] == [1, 3, 5, 7, 9, 15]
   and all(v['italian'] == v['english'] for v in cov if v['kind'] == 'VALUE')
   and by[15]['italian'] == '"Baellie" Atomic Engines')
ck('i nomi di prodotto e di fazione presenti nel testo inglese restano invariati',
   not [n for n in NAMES if n in EN_ALL and n not in IT_ALL],
   [n for n in NAMES if n in EN_ALL and n not in IT_ALL])
ck('«pacco batterie» 4 volte, tante quante «battery pack» in inglese; «impronta termica» 2 volte',
   IT_ALL.count('pacco batterie') == 4 == EN_ALL.count('battery pack')
   and IT_ALL.count('impronta termica') == 2 == EN_ALL.count('heat footprint'),
   (IT_ALL.count('pacco batterie'), EN_ALL.count('battery pack'),
    IT_ALL.count('impronta termica'), EN_ALL.count('heat footprint')))
ck('le cinque batterie sono una famiglia numerata per capacita\' crescente (unita\' 2, 4, 6, 8, 10)',
   all(x in by[i]['italian'] for i, x in ((2, 'più piccolo'), (4, 'più che tripla'), (6, 'taglia media'),
                                          (8, 'grandi dimensioni'), (10, 'modello di batteria più grande'))))
c = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
st = dict(c.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('tutte le 19 unita sono PENDING (misurato)',
   c.execute('select count(*) from units where id in (%s) and state != "PENDING"'
             % ','.join('?' * len(units)), [u['id'] for u in units]).fetchone()[0] == 0)
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d' % (sum(len(v['english'].split()) for v in cov),
                                sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
