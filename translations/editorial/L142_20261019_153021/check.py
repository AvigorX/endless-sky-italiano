r"""check.py — L142 (`data/hai/unfettered 0 prologue.txt`, 20 unita', righe 139-201). Chiude `Unfettered Jump Drive 1`.

Controlli propri: **1 `VALUE`** identico (`More Jump Drives`); **`(No.)` identico in `ID_OK`** con controllo dedicato
(«No» e' italiano, l'identita' e' legittima e va dichiarata); **il rifiuto** (unita' 13 e 18) con la **stessa resa**;
**17 tab**; **38 virgolette**; **zero token** e **zero `UI_LABEL`**.
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
ID_OK = {4: '(No.)'}
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 20/20", len(cov) == 20 == len(units) and not missing, '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 18 MISSION_TEXT, 1 VALUE, 1 DESCRIPTION',
   collections.Counter(u['kind'] for u in units)
   == {'MISSION_TEXT': 18, 'VALUE': 1, 'DESCRIPTION': 1},
   collections.Counter(u['kind'] for u in units))
ck('ZERO UI_LABEL (asserzione vuota scritta)', [u['idx'] for u in units if u['kind'] == 'UI_LABEL'] == [])
ck('ZERO token in questa finestra (asserzione vuota scritta)',
   collections.Counter(t for u in units for t in TAGS.findall(u['english'])) == {})
ck('1 VALUE identico al sorgente (nome della missione)',
   [(v['idx'], v['italian']) for v in cov if v['kind'] == 'VALUE'] == [(1, 'More Jump Drives')],
   [(v['idx'], v['italian']) for v in cov if v['kind'] == 'VALUE'])
ck('ID_OK: (No.) identico, dichiarato e verificato uno per uno',
   by[4]['italian'].lstrip('\t') == ID_OK[4] == by[4]['english'].lstrip('\t'))
ck('tutte le unita di testo sono tradotte (18 su 18, oltre a VALUE e ID_OK)',
   not [v['idx'] for v in cov
        if v['kind'] not in ('VALUE',) and v['idx'] not in ID_OK
        and v['italian'].strip() == v['english'].strip()])
tabs = [v['idx'] for v in cov if v['english'].startswith('\t')]
ck('17 unita iniziano con tab, le stesse in traduzione (VALUE, DESCRIPTION e la prima no)',
   len(tabs) == 17 and tabs == [v['idx'] for v in cov if v['italian'].startswith('\t')]
   and [v['idx'] for v in cov if not v['english'].startswith('\t')] == [1, 2, 3], len(tabs))
ck('spazi iniziali e finali identici al sorgente (20/20)',
   not [v['idx'] for v in cov
        if len(v['italian']) - len(v['italian'].rstrip()) != len(v['english']) - len(v['english'].rstrip())])
ck('38 virgolette in inglese e in italiano',
   sum(v['english'].count('"') for v in cov) == 38 == sum(v['italian'].count('"') for v in cov),
   (sum(v['english'].count('"') for v in cov), sum(v['italian'].count('"') for v in cov)))
ck('virgolette per unita: stesso numero in tutte',
   not [v['idx'] for v in cov if v['english'].count('"') != v['italian'].count('"')],
   [(v['idx'], v['english'].count('"'), v['italian'].count('"')) for v in cov
    if v['english'].count('"') != v['italian'].count('"')])
ck('unita con quattro virgolette: 10, 15, 19, 20',
   [v['idx'] for v in cov if v['italian'].count('"') == 4] == [10, 15, 19, 20],
   [v['idx'] for v in cov if v['italian'].count('"') == 4])
ck('nessuna unita dispari', [v['idx'] for v in cov if v['english'].count('"') % 2] == [])
ck('1 contesto: Unfettered Jump Drive 1, 20 unita',
   list(collections.Counter(v['context'] for v in cov).items()) == [('mission:Unfettered Jump Drive 1', 20)])
ck('prima e ultima unita: righe 139 e 201', (cov[0]['line'], cov[-1]['line']) == (139, 201),
   (cov[0]['line'], cov[-1]['line']))
ck('19 testi distinti su 20 unita', len({v['english'] for v in cov}) == 19,
   len({v['english'] for v in cov}))
ck('il rifiuto (13 e 18) ha la stessa resa, parola per parola',
   by[13]['italian'] == by[18]['italian'] and 'perderò la capacità di catturarne altri' in by[13]['italian'])
ck('ZERO quadre e zero backtick (asserito)',
   not [v['idx'] for v in cov if any(c in v['english'] + v['italian'] for c in '[]`')])
LOW = ' '.join(v['italian'] for v in cov).lower()
TERMS = ('motore di salto', 'iperpropulsore', 'anomalocaris', 'milione di crediti', 'vera hai' if 'vera hai' in LOW
         else 'vero popolo hai', 'amicizia', 'ingegneri', 'tecnologia')
ck('terminologia presente: 8 termini chiave', all(t in LOW for t in TERMS),
   [t for t in TERMS if t not in LOW])
ck('i nomi restano: Anomalocaris, Hai',
   all(t in ' '.join(v['italian'] for v in cov) for t in ('Anomalocaris', 'Hai')))
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' you ', ' to the ')
LONG = ' '.join(TAGS.sub('""', v['italian']) for v in cov).lower()
for s in ('more jump drives', 'anomalocaris', 'hai'):
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
ck('tutte le 20 unita sono PENDING nel database (misurato)',
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
