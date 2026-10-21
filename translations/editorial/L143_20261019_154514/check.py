r"""check.py — L143 (`data/hai/unfettered 0 prologue.txt`, 30 unita', righe 214-317). Due missioni intere.

Controlli propri: **2 contesti** che si chiudono (12 + 18); **1 `VALUE`** identico che **ricompare** da L142;
**`(No.)` due volte identico** in `ID_OK` e **`(Sì.)` due volte tradotto**; **26 tab**; **46 virgolette**; **zero
token** e **zero `UI_LABEL`**.
"""
import collections
import json
import os
import re
import sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
PREV = os.path.join(L10N, 'staging/editorial/L142_20261019_153021/translation.json')
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
prev = {u['english']: u['italian'] for u in json.load(open(PREV, encoding='utf-8'))['units']}
TAGS = re.compile(r'<[^<>]+>')
ID_OK = {4: '(No.)', 14: '(No.)'}
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 30/30", len(cov) == 30 == len(units) and not missing, '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 28 MISSION_TEXT, 1 VALUE, 1 DESCRIPTION',
   collections.Counter(u['kind'] for u in units)
   == {'MISSION_TEXT': 28, 'VALUE': 1, 'DESCRIPTION': 1},
   collections.Counter(u['kind'] for u in units))
ck('ZERO UI_LABEL (asserzione vuota scritta)', [u['idx'] for u in units if u['kind'] == 'UI_LABEL'] == [])
ck('ZERO token in questa finestra (asserzione vuota scritta)',
   collections.Counter(t for u in units for t in TAGS.findall(u['english'])) == {})
ck('1 VALUE identico: More Jump Drives (ricompare, come in L142)',
   [(v['idx'], v['italian']) for v in cov if v['kind'] == 'VALUE'] == [(1, 'More Jump Drives')],
   [(v['idx'], v['italian']) for v in cov if v['kind'] == 'VALUE'])
ck('ID_OK: (No.) due volte identico, dichiarato e verificato',
   all(by[k]['italian'].lstrip('\t') == ID_OK[k] == by[k]['english'].lstrip('\t') for k in ID_OK))
ck('(Yes.) due volte, tradotto «(Sì.)» con l\'accento',
   by[5]['italian'].lstrip('\t') == by[15]['italian'].lstrip('\t') == '(Sì.)',
   (by[5]['italian'], by[15]['italian']))
ck('tutte le unita di testo sono tradotte (VALUE e ID_OK a parte)',
   not [v['idx'] for v in cov
        if v['kind'] not in ('VALUE',) and v['idx'] not in ID_OK
        and v['italian'].strip() == v['english'].strip()])
tabs = [v['idx'] for v in cov if v['english'].startswith('\t')]
ck('26 unita iniziano con tab, le stesse in traduzione',
   len(tabs) == 26 and tabs == [v['idx'] for v in cov if v['italian'].startswith('\t')]
   and [v['idx'] for v in cov if not v['english'].startswith('\t')] == [1, 2, 3, 13], len(tabs))
ck('spazi iniziali e finali identici al sorgente (30/30)',
   not [v['idx'] for v in cov
        if len(v['italian']) - len(v['italian'].rstrip()) != len(v['english']) - len(v['english'].rstrip())])
ck('46 virgolette in inglese e in italiano',
   sum(v['english'].count('"') for v in cov) == 46 == sum(v['italian'].count('"') for v in cov),
   (sum(v['english'].count('"') for v in cov), sum(v['italian'].count('"') for v in cov)))
ck('virgolette per unita: stesso numero in tutte',
   not [v['idx'] for v in cov if v['english'].count('"') != v['italian'].count('"')],
   [(v['idx'], v['english'].count('"'), v['italian'].count('"')) for v in cov
    if v['english'].count('"') != v['italian'].count('"')])
ck('unita con quattro virgolette: 9, 25, 30',
   [v['idx'] for v in cov if v['italian'].count('"') == 4] == [9, 25, 30],
   [v['idx'] for v in cov if v['italian'].count('"') == 4])
ck('nessuna unita dispari', [v['idx'] for v in cov if v['english'].count('"') % 2] == [])
ck('2 contesti: Jump Drive 2 (12) e Jump Drive 3 (18)',
   [(c, n) for c, n in collections.Counter(v['context'] for v in cov).items()]
   == [('mission:Unfettered Jump Drive 2', 12), ('mission:Unfettered Jump Drive 3', 18)],
   dict(collections.Counter(v['context'] for v in cov)))
ck('prima e ultima unita: righe 214 e 317', (cov[0]['line'], cov[-1]['line']) == (214, 317),
   (cov[0]['line'], cov[-1]['line']))
ck('28 testi distinti su 30 unita (le due scelte ripetute)', len({v['english'] for v in cov}) == 28,
   len({v['english'] for v in cov}))
ck('le due scelte hanno la stessa resa in entrambe le missioni',
   by[4]['italian'].lstrip('\t') == by[14]['italian'].lstrip('\t')
   and by[5]['italian'].lstrip('\t') == by[15]['italian'].lstrip('\t'))
ck('ZERO quadre e zero backtick (asserito)',
   not [v['idx'] for v in cov if any(c in v['english'] + v['italian'] for c in '[]`')])
LOW = ' '.join(v['italian'] for v in cov).lower()
TERMS = ('motore di salto', 'iperpropulsore', 'wanderer', 'bacheca dei lavori', 'milione di crediti', 'slegati',
         'artefatto', 'sentinelle')
ck('terminologia presente: 8 termini chiave', all(t in LOW for t in TERMS),
   [t for t in TERMS if t not in LOW])
ck('i nomi restano: Wanderer, Hai',
   all(t in ' '.join(v['italian'] for v in cov) for t in ('Wanderer', 'Hai')))
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' you ', ' to the ')
LONG = ' '.join(TAGS.sub('""', v['italian']) for v in cov).lower()
for s in ('more jump drives', 'wanderers', 'hai'):
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
ck('tutte le 30 unita sono PENDING nel database (misurato)',
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
