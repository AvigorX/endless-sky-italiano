r"""check.py — L141 (`data/hai/unfettered 0 prologue.txt`, 20 unita', righe 83-132). Chiude la prima missione.

Controlli propri: **18 `MISSION_TEXT` + 2 `LOGBOOK`**; **18 tab** (le due voci di diario non sono rientrate); **58
virgolette**; **la voce di diario identica a L138** (unita' 19) verificata **identica** al lotto precedente; la
**variante** (unita' 20) resa di nuovo e **non** copiata; la frase sui «denti ottusi» (unita' 3 e 5) con la stessa resa;
**zero token**, **zero `VALUE`/`UI_LABEL`**.
"""
import collections
import json
import os
import re
import sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
PREV = os.path.join(L10N, 'staging/editorial/L138_20261019_142846/translation.json')
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
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 20/20", len(cov) == 20 == len(units) and not missing, '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 18 MISSION_TEXT, 2 LOGBOOK',
   collections.Counter(u['kind'] for u in units) == {'MISSION_TEXT': 18, 'LOGBOOK': 2},
   collections.Counter(u['kind'] for u in units))
ck('ZERO VALUE, ZERO UI_LABEL (due asserzioni vuote scritte)',
   [u['idx'] for u in units if u['kind'] in ('VALUE', 'UI_LABEL')] == [])
ck('ZERO token in questa finestra (asserzione vuota scritta)',
   collections.Counter(t for u in units for t in TAGS.findall(u['english'])) == {})
ck('tutte le unita di testo sono tradotte (20 su 20)',
   not [v['idx'] for v in cov if v['italian'].strip() == v['english'].strip()])
tabs = [v['idx'] for v in cov if v['english'].startswith('\t')]
ck('18 unita iniziano con tab, le stesse in traduzione (le due di diario no)',
   len(tabs) == 18 and tabs == [v['idx'] for v in cov if v['italian'].startswith('\t')]
   and [v['idx'] for v in cov if not v['english'].startswith('\t')] == [19, 20], len(tabs))
ck('spazi iniziali e finali identici al sorgente (20/20)',
   not [v['idx'] for v in cov
        if len(v['italian']) - len(v['italian'].rstrip()) != len(v['english']) - len(v['english'].rstrip())])
ck('58 virgolette in inglese e in italiano',
   sum(v['english'].count('"') for v in cov) == 58 == sum(v['italian'].count('"') for v in cov),
   (sum(v['english'].count('"') for v in cov), sum(v['italian'].count('"') for v in cov)))
ck('virgolette per unita: stesso numero in tutte',
   not [v['idx'] for v in cov if v['english'].count('"') != v['italian'].count('"')],
   [(v['idx'], v['english'].count('"'), v['italian'].count('"')) for v in cov
    if v['english'].count('"') != v['italian'].count('"')])
ck('unita con quattro virgolette: 1, 2, 3, 4, 5, 10, 14, 18, 19',
   [v['idx'] for v in cov if v['italian'].count('"') == 4] == [1, 2, 3, 4, 5, 10, 14, 18, 19],
   [v['idx'] for v in cov if v['italian'].count('"') == 4])
ck('nessuna unita dispari', [v['idx'] for v in cov if v['english'].count('"') % 2] == [])
ck('1 contesto: First Contact: Unfettered, 20 unita',
   list(collections.Counter(v['context'] for v in cov).items()) == [('mission:First Contact: Unfettered', 20)])
ck('prima e ultima unita: righe 83 e 132', (cov[0]['line'], cov[-1]['line']) == (83, 132),
   (cov[0]['line'], cov[-1]['line']))
ck('20 testi distinti', len({v['english'] for v in cov}) == 20)
ck('la voce di diario identica a L138 (unita 19) e riletta, non ricopiata',
   by[19]['english'] in prev and prev[by[19]['english']] == by[19]['italian'])
ck('la variante del diario (unita 20) e resa di nuovo, non copiata da L138',
   by[20]['italian'] != prev.get(by[19]['english'], None)
   and by[20]['italian'].startswith('Gli Hai Slegati dicono'))
ck('la frase sugli «antenati ottusi» ha la stessa resa in 3 e 5',
   'sopravvivono solo i loro antenati ottusi' in by[3]['italian']
   and 'sopravvivono solo i loro antenati ottusi' in by[5]['italian'])
ck('la voce telegrafica resta telegrafica: nessun articolo aggiunto nel motto degli Slegati',
   'molti mondi oltre il wormhole erano nostri' in by[1]['italian'])
ck('ZERO quadre e zero backtick (asserito)',
   not [v['idx'] for v in cov if any(c in v['english'] + v['italian'] for c in '[]`')])
LOW = ' '.join(v['italian'] for v in cov).lower()
TERMS = ('sheragi', 'drak', 'scimmia', 'wormhole', 'motore di salto', 'iperpropulsore', 'mondi-drago' if
         'mondi-drago' in LOW else 'popoli-drago', 'gabbia', 'bottino', 'verità')
ck('terminologia presente: 10 termini chiave', all(t in LOW for t in TERMS),
   [t for t in TERMS if t not in LOW])
ck('i nomi restano: Sheragi, Drak, Hai', all(t in ' '.join(v['italian'] for v in cov)
                                            for t in ('Sheragi', 'Drak', 'Hai')))
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' you ', ' to the ')
LONG = ' '.join(TAGS.sub('""', v['italian']) for v in cov).lower()
for s in ('sheragi', 'drak', 'hai', 'wormhole'):
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
