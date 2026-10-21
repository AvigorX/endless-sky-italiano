r"""check.py — L134 (`data/hai/unfettered side missions.txt`, 8 unita', righe 494-510). **CHIUDE IL FILE.**

Coda del file, **1 contesto** (`Undeserved Anomalocaris`), **8 `MISSION_TEXT`**.

Tre asserzioni **vuote scritte**: **zero `VALUE`**, **zero `UI_LABEL`**, **zero token** — la forma che distingue «non
c'e` niente da controllare» da «non ho controllato».

Controlli propri: **7 unita' con tab**, **13 virgolette** con **una sola nell'unita' 6** (battuta non chiusa dal
sorgente), **8 testi distinti**, `Jump Drive` e `Lightning Bug` lasciati come nomi.
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
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 8/8", len(cov) == 8 == len(units) and not missing, '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 8 MISSION_TEXT', collections.Counter(u['kind'] for u in units) == {'MISSION_TEXT': 8},
   collections.Counter(u['kind'] for u in units))
ck('ZERO VALUE (asserzione vuota scritta)', [u['idx'] for u in units if u['kind'] == 'VALUE'] == [])
ck('ZERO UI_LABEL (asserzione vuota scritta)', [u['idx'] for u in units if u['kind'] == 'UI_LABEL'] == [])
ck('ZERO token (asserzione vuota scritta)',
   collections.Counter(t for u in units for t in TAGS.findall(u['english'])) == {},
   [t for u in units for t in TAGS.findall(u['english'])])
ck('tutte le unita sono tradotte',
   not [v['idx'] for v in cov if v['italian'].strip() == v['english'].strip()])
tabs = [v['idx'] for v in cov if v['english'].startswith('\t')]
ck('7 unita iniziano con tab, le stesse in traduzione',
   len(tabs) == 7 and tabs == [v['idx'] for v in cov if v['italian'].startswith('\t')], len(tabs))
ck('spazi iniziali e finali identici al sorgente (8/8)',
   not [v['idx'] for v in cov
        if len(v['italian']) - len(v['italian'].rstrip()) != len(v['english']) - len(v['english'].rstrip())])
ck('13 virgolette in inglese e in italiano',
   sum(v['english'].count('"') for v in cov) == 13 == sum(v['italian'].count('"') for v in cov),
   (sum(v['english'].count('"') for v in cov), sum(v['italian'].count('"') for v in cov)))
ck('virgolette per unita: stesso numero',
   not [v['idx'] for v in cov if v['english'].count('"') != v['italian'].count('"')],
   [(v['idx'], v['english'].count('"'), v['italian'].count('"')) for v in cov
    if v['english'].count('"') != v['italian'].count('"')])
ck('una sola unita dispari (6, una virgoletta), riprodotta',
   [v['idx'] for v in cov if v['english'].count('"') % 2] == [6] and by[6]['italian'].count('"') == 1,
   [v['idx'] for v in cov if v['english'].count('"') % 2])
ck('ZERO quadre e zero backtick (asserito)',
   not [v['idx'] for v in cov if any(c in v['english'] + v['italian'] for c in '[]`')])
ck('1 contesto: Undeserved Anomalocaris, 8 unita',
   list(collections.Counter(u['context'] for u in units).items())
   == [('mission:Undeserved Anomalocaris', 8)])
ck('prima e ultima unita: righe 494 e 510', (cov[0]['line'], cov[-1]['line']) == (494, 510),
   (cov[0]['line'], cov[-1]['line']))
ck('8 testi distinti su 8 unita', len({v['english'] for v in cov}) == 8)
LOW = ' '.join(v['italian'] for v in cov).lower()
TERMS = ('anomalocaris', 'unfettered', 'relitto', 'milizia', 'spazioporto', 'lightning bug', 'jump drive',
         'equipaggio', 'armi', 'selvaggi')
ck('terminologia presente: 10 termini chiave', all(t in LOW for t in TERMS), [t for t in TERMS if t not in LOW])
ck('nomi di equipaggiamento e modelli restano: Jump Drive, Lightning Bug, Anomalocaris',
   all(t in ' '.join(v['italian'] for v in cov) for t in ('Jump Drive', 'Lightning Bug', 'Anomalocaris')))
ck('la concessione ha il suo registro: «abbia saputo ragionare»',
   'abbia saputo ragionare' in ' '.join(v['italian'] for v in cov))
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' ship ', ' you ')
LONG = ' '.join(TAGS.sub('""', v['italian']) for v in cov).lower()
for s in ('unfettered', 'hai', 'anomalocaris', 'lightning bug', 'jump drive'):
    LONG = LONG.replace(s, '@@')
ck('nessun residuo inglese fuori dai nomi propri',
   not [w for w in ENGW if w in LONG], [w for w in ENGW if w in LONG])
CORT = re.findall(r'\bLei\b|(?<![.!?] )\b(?:Suo|Sua|Suoi|Sue)\b', ' '.join(v['italian'] for v in cov))
ck('nessuna forma di cortesia «Lei»', not CORT, CORT)
rs = [v['ratio'] for v in cov]
ck('rapporto nel gate', 0.55 < min(rs) and max(rs) < 1.90, '%.2f - %.2f' % (min(rs), max(rs)))
bad = [(v['idx'], n) for v in cov for p, n in ((r"\b(e|piu|perche|cosi|gia|puo|cioe|percio|fa)'", 'accento'),
       ('\u2026', 'ellissi'), ('\u2014', 'em dash'), ('\u2013', 'en dash'), ('\u2019', 'apostrofo curvo'),
       ('\u00ab', 'caporale'), ('\u00bb', 'caporale')) if re.search(p, v['italian'])]
ck('tipografia', not bad, bad)
nonlat = [v['idx'] for v in cov for c in v['italian'] if ord(c) > 127 and not 0x00C0 <= ord(c) <= 0x024F]
ck('caratteri non latini', not nonlat, nonlat)
c = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
st = dict(c.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('tutte le 8 unita sono PENDING nel database (misurato)',
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
