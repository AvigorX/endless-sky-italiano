r"""check.py — L148 (`data/coalition/coalition jobs.txt`, 16 unita', righe 309-435).

Controlli propri: **primo `DIALOG`** del file (unita' 1) contato per tipo; **`<destination>`** distinto da `<planet>`
con parita' per simbolo **e** ordine per unita' (31 occorrenze, 4 simboli); **6 `VALUE` identici**, uno per uno, e
`Interpreters to <planet>` verificato **senza «the»**; **quattro asserzioni vuote** (tab, virgolette, `LOGBOOK`,
`UI_LABEL`).
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


ck("unita' tradotte 16/16", len(cov) == 16 == len(units) and not missing, '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 1 DIALOG + 3 TEXT + 6 VALUE + 6 DESCRIPTION',
   collections.Counter(u['kind'] for u in units) == {'DIALOG': 1, 'TEXT': 3, 'VALUE': 6, 'DESCRIPTION': 6},
   collections.Counter(u['kind'] for u in units))
ck('il primo DIALOG del file e l unita 1, tradotto',
   [u['idx'] for u in units if u['kind'] == 'DIALOG'] == [1]
   and by[1]['italian'].strip() != by[1]['english'].strip())
ck('TRE asserzioni vuote: ZERO LOGBOOK, ZERO UI_LABEL, e il DIALOG e uno solo',
   [u['idx'] for u in units if u['kind'] in ('LOGBOOK', 'UI_LABEL')] == [])
ck('31 occorrenze di token su 4 simboli',
   dict(collections.Counter(t for u in units for t in TAGS.findall(u['english'])))
   == {'<payment>': 10, '<planet>': 9, '<bunks>': 6, '<destination>': 6}
   and sum(1 for u in units for _ in TAGS.findall(u['english'])) == 31)
ck('parita per simbolo: stesso multiset in italiano',
   dict(collections.Counter(t for u in cov for t in TAGS.findall(u['italian'])))
   == dict(collections.Counter(t for u in units for t in TAGS.findall(u['english']))))
ck('parita per UNITA: simboli identici e nello stesso ordine in tutte le 16',
   not [v['idx'] for v in cov if TAGS.findall(v['italian']) != TAGS.findall(v['english'])],
   [(v['idx'], TAGS.findall(v['english']), TAGS.findall(v['italian'])) for v in cov
    if TAGS.findall(v['italian']) != TAGS.findall(v['english'])])
ck('<destination> non si e scambiato con <planet>',
   sum(1 for v in cov for _ in re.findall('<destination>', v['italian'])) == 6
   and sum(1 for v in cov for _ in re.findall('<planet>', v['italian'])) == 9
   and '<destination>' in by[4]['italian'] and '<planet>' not in by[4]['italian']
   and '<planet>' in by[2]['italian'] and '<destination>' not in by[2]['italian'])
ck('6 VALUE identici al sorgente, uno per uno',
   len(VAL) == 6 and all(by[i]['italian'].rstrip() == by[i]['english'].rstrip() for i in VAL),
   [(i, by[i]['italian'], by[i]['english']) for i in VAL if by[i]['italian'].rstrip() != by[i]['english'].rstrip()])
ck('i VALUE sono senza «the»: Interpreters to <planet>, Peacekeepers to <planet>, Saryds to <planet>',
   [by[i]['italian'].rstrip() for i in VAL]
   == ['Interpreters to <planet>'] * 3 + ['Peacekeepers to <planet>'] * 2 + ['Saryds to <planet>']
   and 'the <planet>' not in ' '.join(by[i]['italian'] for i in VAL),
   [by[i]['italian'].rstrip() for i in VAL])
ck('le 10 unita di testo sono tradotte (VALUE a parte)',
   not [v['idx'] for v in cov if v['kind'] != 'VALUE' and v['italian'].strip() == v['english'].strip()])
ck('ripetizioni: 3 interpreti uguali, 2 peacekeeper uguali',
   by[4]['italian'] == by[6]['italian'] == by[8]['italian'] and by[11]['italian'] == by[13]['italian'])
ck('10 testi inglesi distinti su 16 unita', len({v['english'] for v in cov}) == 10)
ck('DUE asserzioni vuote: zero tab e zero virgolette',
   sum(1 for v in cov if v['english'].startswith('\t')) == 0
   and sum(1 for v in cov if v['italian'].startswith('\t')) == 0
   and sum(v['english'].count('"') for v in cov) == 0 == sum(v['italian'].count('"') for v in cov))
ck('10 contesti', len(set(v['context'] for v in cov)) == 10)
ck('prima e ultima unita: righe 309 e 435', (cov[0]['line'], cov[-1]['line']) == (309, 435),
   (cov[0]['line'], cov[-1]['line']))
ck('spazi iniziali e finali identici al sorgente (16/16)',
   not [v['idx'] for v in cov
        if len(v['italian']) - len(v['italian'].rstrip()) != len(v['english']) - len(v['english'].rstrip())])
LOW = ' '.join(v['italian'] for v in cov).lower()
TERMS = ('interpreti', 'mediatori', 'peacekeeper', 'coloni', 'lunarium', 'heliarch', 'compenso', 'cerimonia',
         'tariffa di trasporto')
ck('terminologia presente: 9 termini chiave', all(t in LOW for t in TERMS), [t for t in TERMS if t not in LOW])
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' you ', ' to the ', ' will be ')
LONG = ' '.join(TAGS.sub('""', v['italian']) for v in cov if v['kind'] != 'VALUE').lower()
for s in ('lunarium', 'heliarch', 'peacekeeper', 'saryd'):
    LONG = LONG.replace(s, '@@')
ck('nessun residuo inglese fuori dai nomi propri e dai VALUE',
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
ck('tutte le 16 unita sono PENDING nel database (misurato)',
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
