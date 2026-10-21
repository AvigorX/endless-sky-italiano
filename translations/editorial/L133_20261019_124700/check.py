r"""check.py — L133 (`data/hai/unfettered side missions.txt`, 67 unita', righe 237-477)

Due contesti: **`Hai Legacy 2`** (10) e **`Hai Legacy 3`** (57). **50 `MISSION_TEXT`**, **9 `DIALOG`**, **2 `VALUE`**,
**2 `DESCRIPTION`**, **2 `LOGBOOK`**, **2 `UI_LABEL`**.

Controlli propri:

- **98 virgolette** in 67 unita' — il record del progetto — con distribuzione **18 / 44 / 1 / 3 / 1** (0, 2, 4, 1, 3
  virgolette) e **quattro unita' dispari** (47, 48, 64, 65);
- **2 `VALUE`** (`Heritage Reclaimed`, `Ancient Claim`) e **2 `UI_LABEL`** (`too many ships`, ripetuta) identici;
- **`<date>` e `<system>`** per la prima volta in questo file: parita' per unita';
- **l'incoerenza del sorgente** (`food shipment` nel diario, `medical supplies` nel testo) e' **riprodotta** e
  verificata: il diario dice «cibo», il testo «forniture mediche».
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
VAL = [1, 11]
LAB = [40, 44]
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 67/67", len(cov) == 67 == len(units) and not missing, '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
kk = collections.Counter(u['kind'] for u in units)
ck('tipi: 50 MISSION_TEXT · 9 DIALOG · 2 VALUE · 2 DESCRIPTION · 2 LOGBOOK · 2 UI_LABEL',
   dict(kk) == {'MISSION_TEXT': 50, 'DIALOG': 9, 'VALUE': 2, 'DESCRIPTION': 2, 'LOGBOOK': 2, 'UI_LABEL': 2},
   dict(kk))
ck('i 2 VALUE sono identici al sorgente',
   [u['idx'] for u in units if u['kind'] == 'VALUE'] == VAL
   and [by[i]['italian'] for i in VAL] == ['Heritage Reclaimed', 'Ancient Claim'],
   [(i, by[i]['italian']) for i in VAL])
ck('le 2 UI_LABEL sono identiche e ripetono lo stesso nome di nodo',
   [u['idx'] for u in units if u['kind'] == 'UI_LABEL'] == LAB
   and [by[i]['italian'] for i in LAB] == ['too many ships', 'too many ships'])
ck('tutte le unita prosaiche sono tradotte',
   not [v['idx'] for v in cov if v['idx'] not in VAL + LAB and v['italian'].strip() == v['english'].strip()])
tabs = [v['idx'] for v in cov if v['english'].startswith('\t')]
ck('34 unita iniziano con tab, le stesse in traduzione',
   len(tabs) == 34 and tabs == [v['idx'] for v in cov if v['italian'].startswith('\t')], len(tabs))
ck('spazi iniziali e finali identici al sorgente (67/67)',
   not [v['idx'] for v in cov
        if len(v['italian']) - len(v['italian'].rstrip()) != len(v['english']) - len(v['english'].rstrip())])
ck('98 virgolette in inglese e in italiano',
   sum(v['english'].count('"') for v in cov) == 98 == sum(v['italian'].count('"') for v in cov),
   (sum(v['english'].count('"') for v in cov), sum(v['italian'].count('"') for v in cov)))
ck('virgolette per unita: stesso numero',
   not [v['idx'] for v in cov if v['english'].count('"') != v['italian'].count('"')],
   [(v['idx'], v['english'].count('"'), v['italian'].count('"')) for v in cov
    if v['english'].count('"') != v['italian'].count('"')])
odd = [v['idx'] for v in cov if v['english'].count('"') % 2]
ck('quattro unita dispari (47, 48, 64, 65), riprodotte',
   odd == [47, 48, 64, 65] and [by[i]['italian'].count('"') for i in odd] == [1, 1, 3, 1],
   (odd, [by[i]['italian'].count('"') for i in odd]))
ck('distribuzione delle virgolette: 18 senza, 44 con 2, 1 con 4, 3 con 1, 1 con 3',
   collections.Counter(v['english'].count('"') for v in cov) == {0: 18, 2: 44, 4: 1, 1: 3, 3: 1},
   collections.Counter(v['english'].count('"') for v in cov))
tok = collections.Counter(t for v in cov for t in TAGS.findall(v['english']))
ck('8 token in 6 famiglie', dict(tok) == {'<planet>': 2, '<date>': 2, '<destination>': 1, '<last>': 1,
                                          '<payment>': 1, '<system>': 1}, dict(tok))
ck('token per unita: sequenza identica',
   not [v['idx'] for v in cov if TAGS.findall(v['english']) != TAGS.findall(v['italian'])],
   [(v['idx'], TAGS.findall(v['english']), TAGS.findall(v['italian'])) for v in cov
    if TAGS.findall(v['english']) != TAGS.findall(v['italian'])])
ck('<date> presente in 2 unita e <system> in 1, come nel sorgente',
   [v['idx'] for v in cov if '<date>' in v['english']] == [2, 3]
   and [v['idx'] for v in cov if '<system>' in v['english']] == [12],
   ([v['idx'] for v in cov if '<date>' in v['english']], [v['idx'] for v in cov if '<system>' in v['english']]))
ck('ZERO quadre e zero backtick (asserito)',
   not [v['idx'] for v in cov if any(c in v['english'] + v['italian'] for c in '[]`')])
seen = collections.OrderedDict()
for u in units:
    seen[u['context']] = seen.get(u['context'], 0) + 1
ck('2 contesti: 10 / 57',
   list(seen.items()) == [('mission:Hai Legacy 2', 10), ('mission:Hai Legacy 3', 57)], list(seen.items()))
ck('prima e ultima unita: righe 237 e 477', (cov[0]['line'], cov[-1]['line']) == (237, 477),
   (cov[0]['line'], cov[-1]['line']))
grp = {}
for v in cov:
    grp.setdefault(v['english'].lstrip('\t'), set()).add(v['italian'])
ck('64 testi distinti su 67 unita', len(grp) == 64, len(grp))
ck('stesso inglese => stessa resa',
   not [(k, v) for k, v in grp.items() if len(v) > 1], [(k[:40], v) for k, v in grp.items() if len(v) > 1])
LOW = ' '.join(v['italian'] for v in cov).lower()
TERMS = ('anomalocaris', 'unfettered', 'mera', 'ehma ti', 'firelode', 'veri hai', 'duello', 'relitto',
         'forniture mediche', 'scimmia', 'ingegnere', 'equipaggio')
ck('terminologia presente: 12 termini chiave', all(t in LOW for t in TERMS), [t for t in TERMS if t not in LOW])
ck('i nomi propri restano: Ehma Ti, Firelode, Lightning Bug, Mera',
   all(t in ' '.join(v['italian'] for v in cov) for t in ('Ehma Ti', 'Firelode', 'Lightning Bug', 'Mera')))
ck('incoerenza del sorgente riprodotta: il diario dice cibo, il testo forniture mediche',
   'carico urgente di cibo' in by[10]['italian'] and 'forniture mediche' in by[9]['italian'])
LONG = ' '.join(TAGS.sub('""', v['italian']) for v in cov if v['idx'] not in VAL + LAB)
for s in ('Unfettered', 'Hai', 'Anomalocaris', 'Korath', 'Mera', 'Firelode', 'Ehma Ti', 'Lightning Bug'):
    LONG = LONG.replace(s, '@@')
LONG = LONG.lower()
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' ship ', ' you ')
ck('nessun residuo inglese fuori dai nomi propri',
   not [w for w in ENGW if w in LONG], [w for w in ENGW if w in LONG])
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
ck('tutte le 67 unita sono PENDING nel database (misurato)',
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
