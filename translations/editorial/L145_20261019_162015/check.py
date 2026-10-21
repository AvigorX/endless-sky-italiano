r"""check.py — L145 (`data/hai/unfettered 0 prologue.txt`, 13 unita', righe 423-459).

Controlli propri: **1 `LOGBOOK`** (unita' 3, diario e non dialogo); **3 token** in due unita' con parita' per simbolo
(`<learned>` e `<last>` nell'unita' 2, `<The engineer>` nell'unita' 5, **case-sensitive**); **2 virgolette dispari**
(unita' 12 e 13), riprodotte e **non chiuse**; **12 tab**; **20 virgolette**; **due asserzioni vuote** (`VALUE`,
`UI_LABEL`).

I nomi di armi e navi restano inglesi: `Tripulse Shredder`, `Blaster`, `Ion Cannon`, `Shield Beetle`, `Firelode`.
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


ck("unita' tradotte 13/13", len(cov) == 13 == len(units) and not missing, '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 12 MISSION_TEXT + 1 LOGBOOK',
   collections.Counter(u['kind'] for u in units) == {'MISSION_TEXT': 12, 'LOGBOOK': 1},
   collections.Counter(u['kind'] for u in units))
ck('il LOGBOOK e l\'unita 3, tradotto e non vuoto',
   [u['idx'] for u in units if u['kind'] == 'LOGBOOK'] == [3] and by[3]['italian'].strip()
   and by[3]['italian'].strip() != by[3]['english'].strip())
ck('DUE asserzioni vuote: ZERO VALUE, ZERO UI_LABEL',
   [u['idx'] for u in units if u['kind'] in ('VALUE', 'UI_LABEL')] == [])
ck('3 token, parita 1 = 1 per simbolo',
   dict(collections.Counter(t for u in units for t in TAGS.findall(u['english'])))
   == {'<learned>': 1, '<last>': 1, '<The engineer>': 1})
ck('i token stanno nelle stesse unita: 2 (<learned>, <last>) e 5 (<The engineer>)',
   [u['idx'] for u in units if TAGS.findall(u['english'])] == [2, 5]
   and [u['idx'] for u in cov if TAGS.findall(u['italian'])] == [2, 5])
ck('<The engineer> si confronta ESATTO (case-sensitive), a inizio frase',
   '<The engineer>' in by[5]['italian'] and by[5]['italian'].lstrip('\t').startswith('<The engineer> ti conduce')
   and '<the engineer>' not in by[5]['italian'])
ck('<learned> dopo il punto esclamativo, con la maiuscola che segue',
   'lama! <learned>Sono Desneeparu' in by[2]['italian'])
ck('<last> al suo posto, dentro la battuta', 'capitano <last>!' in by[2]['italian'])
ck('2 virgolette dispari (12, 13): il sorgente le lascia aperte',
   [u['idx'] for u in units if u['english'].count('"') % 2] == [12, 13]
   and [u['idx'] for u in cov if u['italian'].count('"') % 2] == [12, 13])
ck('le due unita dispari NON finiscono con una virgoletta (non si chiude)',
   [u['idx'] for u in cov if u['idx'] in (12, 13) and u['italian'].rstrip().endswith('"')] == [])
ck('le due unita dispari finiscono con lo stesso segno dell\'inglese',
   all(by[i]['italian'].rstrip()[-1] == by[i]['english'].rstrip()[-1] for i in (12, 13)),
   [(by[i]['italian'][-3:], by[i]['english'][-3:]) for i in (12, 13)])
ck('tutte le unita di testo sono tradotte',
   not [v['idx'] for v in cov if v['italian'].strip() == v['english'].strip()])
tabs = [v['idx'] for v in cov if v['english'].startswith('\t')]
ck('12 unita iniziano con tab (il LOGBOOK no)',
   len(tabs) == 12 and tabs == [v['idx'] for v in cov if v['italian'].startswith('\t')]
   and [v['idx'] for v in cov if not v['english'].startswith('\t')] == [3], len(tabs))
ck('spazi iniziali e finali identici al sorgente (13/13)',
   not [v['idx'] for v in cov
        if len(v['italian']) - len(v['italian'].rstrip()) != len(v['english']) - len(v['english'].rstrip())])
ck('20 virgolette in inglese e in italiano',
   sum(v['english'].count('"') for v in cov) == 20 == sum(v['italian'].count('"') for v in cov),
   (sum(v['english'].count('"') for v in cov), sum(v['italian'].count('"') for v in cov)))
ck('virgolette per unita: stesso numero in tutte',
   not [v['idx'] for v in cov if v['english'].count('"') != v['italian'].count('"')],
   [(v['idx'], v['english'].count('"'), v['italian'].count('"')) for v in cov
    if v['english'].count('"') != v['italian'].count('"')])
ck('1 contesto: Jump Drive Trading, 13 unita',
   list(collections.Counter(v['context'] for v in cov).items()) == [('mission:Unfettered Jump Drive Trading', 13)])
ck('prima e ultima unita: righe 423 e 459', (cov[0]['line'], cov[-1]['line']) == (423, 459),
   (cov[0]['line'], cov[-1]['line']))
ck('13 testi distinti', len({v['english'] for v in cov}) == 13)
ck('i nomi restano inglesi: 5 nomi di armi, navi e mondi',
   all(n in ' '.join(v['italian'] for v in cov)
       for n in ('Tripulse Shredder', 'Blaster', 'Ion Cannon', 'Shield Beetle', 'Firelode')))
ck('nessuna traduzione inventata dei nomi (nessun «Distruttore», «Cannone ionico», «Scarabeo»)',
   not [n for n in ('Distruttore', 'Cannone ionico', 'cannone ionico', 'Scarabeo', 'scudo Scarabeo')
        if n in ' '.join(v['italian'] for v in cov)])
LOW = ' '.join(v['italian'] for v in cov).lower()
TERMS = ('duella', 'lama', 'prototipo', 'collaudi', 'sezione avanzata', 'torretta', 'batterie', 'gittata',
         'ionizzazione', 'disabilitare')
ck('terminologia presente: 10 termini chiave', all(t in LOW for t in TERMS), [t for t in TERMS if t not in LOW])
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' you ', ' to the ')
LONG = ' '.join(TAGS.sub('""', v['italian']) for v in cov).lower()
for s in ('tripulse shredder', 'blaster', 'ion cannon', 'shield beetle', 'firelode', 'hai', 'desneeparu',
          'capitano <last>'):
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
nonlat = [v['idx'] for v in cov for c in TAGS.sub('', v['italian'])
          if ord(c) > 127 and not 0x00C0 <= ord(c) <= 0x024F]
ck('caratteri non latini (fuori dai token)', not nonlat, nonlat)
c = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
st = dict(c.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('tutte le 13 unita sono PENDING nel database (misurato)',
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
