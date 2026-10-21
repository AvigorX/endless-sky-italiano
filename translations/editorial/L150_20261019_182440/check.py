r"""check.py — L150 (`data/coalition/coalition jobs.txt`, 14 unita', righe 639-794).

Controlli propri: **33 token su 6 simboli**, con `<commodity>` **una sola volta** e al suo posto; le due famiglie di
turisti differiscono per «home» e hanno **rese diverse**; **6 `VALUE` identici**; **cinque asserzioni vuote**
(tab, virgolette, `LOGBOOK`, `DIALOG`, `UI_LABEL`).
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
VAL = [v['idx'] for v in cov if v['kind'] == 'VALUE']
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 14/14", len(cov) == 14 == len(units) and not missing, '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 6 VALUE + 6 DESCRIPTION + 2 TEXT',
   collections.Counter(u['kind'] for u in units) == {'VALUE': 6, 'DESCRIPTION': 6, 'TEXT': 2})
ck('CINQUE asserzioni vuote: ZERO LOGBOOK, DIALOG, UI_LABEL (e zero tab, zero virgolette sotto)',
   [u['idx'] for u in units if u['kind'] in ('LOGBOOK', 'DIALOG', 'UI_LABEL')] == [])
ck('33 token su 6 simboli, stesso multiset in italiano',
   dict(collections.Counter(t for u in units for t in TAGS.findall(u['english'])))
   == {'<payment>': 8, '<planet>': 6, '<bunks>': 6, '<destination>': 6, '<date>': 6, '<commodity>': 1}
   == dict(collections.Counter(t for u in cov for t in TAGS.findall(u['italian']))))
ck('`<commodity>` una volta sola, nell unita 14',
   sum(1 for v in cov for _ in re.findall('<commodity>', v['italian'])) == 1
   and '<commodity>' in by[14]['italian'])
ck('parita per UNITA: stesso ordine di simboli in tutte le 14',
   not [v['idx'] for v in cov if TAGS.findall(v['italian']) != TAGS.findall(v['english'])],
   [(v['idx'], TAGS.findall(v['english']), TAGS.findall(v['italian'])) for v in cov
    if TAGS.findall(v['italian']) != TAGS.findall(v['english'])])
ck('6 VALUE identici al sorgente, tutti «Vacationers to <planet>»',
   len(VAL) == 6 and all(by[i]['italian'].rstrip() == by[i]['english'].rstrip() for i in VAL)
   and {by[i]['italian'].rstrip() for i in VAL} == {'Vacationers to <planet>'},
   [(i, by[i]['italian']) for i in VAL])
ck('le 8 unita di testo sono tradotte (VALUE a parte)',
   not [v['idx'] for v in cov if v['kind'] != 'VALUE' and v['italian'].strip() == v['english'].strip()])
ck('le tre DESCRIPTION «in partenza» sono identiche fra loro',
   by[2]['italian'] == by[4]['italian'] == by[6]['italian'])
ck('le tre DESCRIPTION «in rientro» sono identiche fra loro',
   by[9]['italian'] == by[11]['italian'] == by[13]['italian'])
ck('le due famiglie hanno rese DIVERSE (c e «a casa» solo in quella di rientro)',
   by[2]['italian'] != by[9]['italian']
   and 'riportarli a casa' in by[9]['italian'] and 'riportarli a casa' not in by[2]['italian'])
ck('i due TEXT sono diversi e tradotti',
   by[7]['italian'] != by[14]['italian']
   and by[7]['italian'].strip() != by[7]['english'].strip()
   and by[14]['italian'].strip() != by[14]['english'].strip())
ck('5 testi inglesi distinti su 14 unita', len({v['english'] for v in cov}) == 5)
ck('zero tab e zero virgolette (asserite)',
   sum(1 for v in cov if v['english'].startswith('\t')) == 0
   and sum(1 for v in cov if v['italian'].startswith('\t')) == 0
   and sum(v['english'].count('"') for v in cov) == 0 == sum(v['italian'].count('"') for v in cov))
ck('8 contesti', len(set(v['context'] for v in cov)) == 8)
ck('prima e ultima unita: righe 639 e 794', (cov[0]['line'], cov[-1]['line']) == (639, 794),
   (cov[0]['line'], cov[-1]['line']))
ck('spazi iniziali e finali identici al sorgente (14/14)',
   not [v['idx'] for v in cov
        if len(v['italian']) - len(v['italian'].rstrip()) != len(v['english']) - len(v['english'].rstrip())])
LOW = ' '.join(v['italian'] for v in cov).lower()
TERMS = ('turisti', 'nave molto confortevole', 'compenso decade', 'destinatario', 'riportati a casa')
ck('terminologia presente: 5 termini chiave', all(t in LOW for t in TERMS), [t for t in TERMS if t not in LOW])
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' you ', ' to the ', ' will be ')
LONG = ' '.join(TAGS.sub('""', v['italian']) for v in cov if v['kind'] != 'VALUE').lower()
ck('nessun residuo inglese fuori dai VALUE',
   not [w for w in ENGW if w in LONG], [w for w in ENGW if w in LONG])
CORT = re.findall(r'\bLei\b|(?<![.!?] )\b(?:Suo|Sua|Suoi|Sue)\b', ' '.join(v['italian'] for v in cov))
ck('nessuna forma di cortesia «Lei»', not CORT, CORT)
rs = [v['ratio'] for v in cov]
ck('rapporto nel gate', 0.55 < min(rs) and max(rs) < 1.90, '%.2f - %.2f' % (min(rs), max(rs)))
bad = [(v['idx'], n) for v in cov for p, n in ((r"\b(e|piu|perche|cosi|gia|puo|cioe|percio|fa)'", 'accento'),
       ('\u2026', 'ellissi'), ('\u2014', 'em dash'), ('\u2013', 'en dash'), ('\u2019', 'apostrofo curvo'),
       ('\u00ab', 'caporale'), ('\u00bb', 'caporale')) if re.search(p, v['italian'])]
ck('tipografia', not bad, bad)
nonlat = [v['idx'] for v in cov for c in TAGS.sub('', v['italian'])
          if ord(c) > 127 and not 0x00C0 <= ord(c) <= 0x024F]
ck('caratteri non latini (fuori dai token)', not nonlat, nonlat)
c = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
st = dict(c.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('tutte le 14 unita sono PENDING nel database (misurato)',
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
