r"""check.py — L149 (`data/coalition/coalition jobs.txt`, 18 unita', righe 455-634).

Controlli propri: **36 token** su 4 simboli con **due coppie di conteggi uguali** (`<planet>`/`<payment>` 10,
`<bunks>`/`<destination>` 8) — quindi l'**ordine per unita'** e' obbligatorio, il multiset da solo e' cieco;
**8 `VALUE` identici**; la `DESCRIPTION` dei coloni e' **identica a L148** (inglese uguale -> resa uguale) e il `TEXT`
degli operai e' **diverso** da L147 (la' «on the <planet>», qui «on <planet>»); **cinque asserzioni vuote**.
"""
import collections
import json
import os
import re
import sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
PREV148 = os.path.join(L10N, 'staging/editorial/L148_20261019_174022/translation.json')
PREV147 = os.path.join(L10N, 'staging/editorial/L147_20261019_171044/translation.json')
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
p148 = {u['english']: u['italian'] for u in json.load(open(PREV148, encoding='utf-8'))['units']}
p147 = {u['english']: u['italian'] for u in json.load(open(PREV147, encoding='utf-8'))['units']}
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 18/18", len(cov) == 18 == len(units) and not missing, '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 8 VALUE + 8 DESCRIPTION + 2 TEXT',
   collections.Counter(u['kind'] for u in units) == {'VALUE': 8, 'DESCRIPTION': 8, 'TEXT': 2},
   collections.Counter(u['kind'] for u in units))
ck('CINQUE asserzioni vuote: ZERO LOGBOOK, DIALOG, UI_LABEL (e zero tab, zero virgolette sotto)',
   [u['idx'] for u in units if u['kind'] in ('LOGBOOK', 'DIALOG', 'UI_LABEL')] == [])
ck('36 token su 4 simboli, con due coppie di conteggi uguali',
   dict(collections.Counter(t for u in units for t in TAGS.findall(u['english'])))
   == {'<planet>': 10, '<payment>': 10, '<bunks>': 8, '<destination>': 8}
   and sum(1 for u in units for _ in TAGS.findall(u['english'])) == 36)
ck('il multiset da solo e cieco: 10 = 10 e 8 = 8 (dichiarato)',
   collections.Counter(t for u in units for t in TAGS.findall(u['english']))['<planet>']
   == collections.Counter(t for u in units for t in TAGS.findall(u['english']))['<payment>'] == 10
   and collections.Counter(t for u in units for t in TAGS.findall(u['english']))['<bunks>']
   == collections.Counter(t for u in units for t in TAGS.findall(u['english']))['<destination>'] == 8)
ck('parita per UNITA: ordine dei simboli identico in tutte le 18 (il controllo che conta)',
   not [v['idx'] for v in cov if TAGS.findall(v['italian']) != TAGS.findall(v['english'])],
   [(v['idx'], TAGS.findall(v['english']), TAGS.findall(v['italian'])) for v in cov
    if TAGS.findall(v['italian']) != TAGS.findall(v['english'])])
ck('<planet> = 10 e <payment> = 10 anche in italiano, per simbolo',
   sum(1 for v in cov for _ in re.findall('<planet>', v['italian'])) == 10
   and sum(1 for v in cov for _ in re.findall('<payment>', v['italian'])) == 10)
ck('<destination> = 8 e <bunks> = 8 anche in italiano, per simbolo',
   sum(1 for v in cov for _ in re.findall('<destination>', v['italian'])) == 8
   and sum(1 for v in cov for _ in re.findall('<bunks>', v['italian'])) == 8)
ck('8 VALUE identici al sorgente, uno per uno',
   len(VAL) == 8 and all(by[i]['italian'].rstrip() == by[i]['english'].rstrip() for i in VAL),
   [(i, by[i]['italian'], by[i]['english']) for i in VAL if by[i]['italian'].rstrip() != by[i]['english'].rstrip()])
ck('i VALUE: Saryds, Kimek x2, Arachi x2, Transfer x3, tutti «to <planet>»',
   [by[i]['italian'].rstrip() for i in VAL]
   == ['Saryds to <planet>', 'Kimek to <planet>', 'Kimek to <planet>', 'Arachi to <planet>',
       'Arachi to <planet>', 'Transfer to <planet>', 'Transfer to <planet>', 'Transfer to <planet>'])
ck('le 10 unita di testo sono tradotte (VALUE a parte)',
   not [v['idx'] for v in cov if v['kind'] != 'VALUE' and v['italian'].strip() == v['english'].strip()])
DESC_SET = [v for v in cov if v['english'].startswith('As part of the Interspecies Exchange Program')]
ck('la DESCRIPTION dei coloni e identica a L148 (inglese uguale -> resa uguale)',
   len(DESC_SET) == 5 and all(v['italian'] == p148[v['english']] for v in DESC_SET), len(DESC_SET))
ck('il TEXT degli operai ha una stringa che in L147 NON esiste (la «on the <planet>»)',
   by[11]['english'] not in p147
   and 'You drop off the workers on the <planet>. A few minutes later you receive a transfer of <payment>.' in p147)
ck('la variante con «the» non esiste in questo lotto',
   not [v['idx'] for v in cov if 'on the <planet>' in v['english']])
ck('la resa del TEXT usa «su <planet>», non «sul <planet>»',
   'su <planet>' in by[11]['italian'] and 'sul <planet>' not in by[11]['italian'])
ck('le tre DESCRIPTION del Programma di Piena Occupazione sono identiche fra loro',
   by[13]['italian'] == by[15]['italian'] == by[17]['italian'])
ck('8 testi inglesi distinti su 18 unita', len({v['english'] for v in cov}) == 8)
ck('zero tab e zero virgolette (asserite)',
   sum(1 for v in cov if v['english'].startswith('\t')) == 0
   and sum(1 for v in cov if v['italian'].startswith('\t')) == 0
   and sum(v['english'].count('"') for v in cov) == 0 == sum(v['italian'].count('"') for v in cov))
ck('10 contesti', len(set(v['context'] for v in cov)) == 10)
ck('prima e ultima unita: righe 455 e 634', (cov[0]['line'], cov[-1]['line']) == (455, 634),
   (cov[0]['line'], cov[-1]['line']))
ck('spazi iniziali e finali identici al sorgente (18/18)',
   not [v['idx'] for v in cov
        if len(v['italian']) - len(v['italian'].rstrip()) != len(v['english']) - len(v['english'].rstrip())])
LOW = ' '.join(v['italian'] for v in cov).lower()
TERMS = ('coloni volontari', 'lavoratori', 'tariffa di trasporto', 'piena occupazione', 'turisti',
         'programma di scambio tra specie', 'bonifico', 'ringraziano')
ck('terminologia presente: 8 termini chiave', all(t in LOW for t in TERMS), [t for t in TERMS if t not in LOW])
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' you ', ' to the ', ' will be ')
LONG = ' '.join(TAGS.sub('""', v['italian']) for v in cov if v['kind'] != 'VALUE').lower()
for s in ('arachi', 'kimek', 'saryd'):
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
ck('tutte le 18 unita sono PENDING nel database (misurato)',
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
