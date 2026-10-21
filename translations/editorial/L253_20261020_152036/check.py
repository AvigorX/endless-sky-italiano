r"""check.py — L253 (`data/wanderer/wanderer jobs.txt`, 24 unita', righe 264-442). Secondo lotto del file.

**Otto missioni, otto terne**: ognuna ha `VALUE` + `DESCRIPTION` + `DIALOG` in due contesti. **14 stringhe distinte** e
**10 gruppi di inglese identico**, tutti con **due copie**; i quattro singolari sono le due schede e le due battute della
missione «Quarantine an invasive species», che differiscono per una parola (animale / pianta) o per il contenuto.

**56 segnaposto in 8 famiglie** (`<payment>` 15, `<planet>` 13, `<bunks>` 9, `<destination>` 6, `<cargo>` 6, `<origin>` 3,
`<stopovers>` 2, `<date>` 2), per famiglia **e** per ordine. **`<stopovers>` e' un simbolo intero** e va distinto da
`<planet stopovers>`, che in questo lotto **non compare**: il controllo lo verifica in entrambe le direzioni.

**Zero tab, zero virgolette**, **zero apici inglesi** contro **1 italiano** (unita' 21, `un'ora`).
"""
import collections
import json
import os
import re
import sqlite3

TAB = chr(9)
QUOTE = chr(34)
APOS = chr(39)
TAG = re.compile(r'<[^<>]+>')
HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
PATH = 'data/wanderer/wanderer jobs.txt'
src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
units = sorted(src['units'], key=lambda x: x['line'])
tr = {}
for p in sorted(f for f in os.listdir(os.path.join(HERE, 'parts')) if f.endswith('.json')):
    for k, v in json.load(open(os.path.join(HERE, 'parts', p), encoding='utf-8')).items():
        tr[int(k)] = v
out = {'block': src['block'], 'note': src['note'], 'units': []}
for u in units:
    if u['idx'] in tr:
        it = tr[u['idx']]
        out['units'].append({"idx": u['idx'], "id": u['id'], "path": u['path'], "line": u['line'],
                             "kind": u['kind'], "context": u['context'], "english": u['english'],
                             "italian": it, "ratio": round(len(it) / max(1, len(u['english'])), 3)})
open(os.path.join(HERE, 'translation.json'), 'w', encoding='utf-8').write(
    json.dumps(out, ensure_ascii=False, indent=1))
cov = out['units']
KINDS = collections.Counter(u['kind'] for u in units)
VAL = [v for v in cov if v['kind'] == 'VALUE']
PROSA = [v for v in cov if v['kind'] in ('DESCRIPTION', 'DIALOG')]
TOK_EN = collections.Counter(t for v in cov for t in TAG.findall(v['english']))
TOK_IT = collections.Counter(t for v in cov for t in TAG.findall(v['italian']))
SEQ = [v['idx'] for v in cov if TAG.findall(v['english']) != TAG.findall(v['italian'])]
A_EN = [(v['idx'], v['english'].count(APOS)) for v in cov if APOS in v['english']]
A_IT = [(v['idx'], v['italian'].count(APOS)) for v in cov if APOS in v['italian']]
prosa = ' '.join(v['italian'] for v in PROSA)
ctx = collections.Counter(u['context'] for u in units)
mult = collections.Counter(v['english'] for v in cov)
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 24/24", len(cov) == 24 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna unita\' vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 8 VALUE + 8 DESCRIPTION + 8 DIALOG',
   dict(KINDS) == {'VALUE': 8, 'DESCRIPTION': 8, 'DIALOG': 8}, dict(KINDS))
ck('8 contesti: quattro missioni × due contatori',
   len(ctx) == 8 and set(ctx) == {
       'mission:Wanderer Biologists [0]', 'mission:Wanderer Biologists [1]',
       'mission:Wanderer Botanists [0]', 'mission:Wanderer Botanists [1]',
       'mission:Wanderer Harvest [0]', 'mission:Wanderer Harvest [1]',
       'mission:Wanderer Invasive Species [0]', 'mission:Wanderer Invasive Species [1]'}, dict(ctx))
ck('righe 264 e 442 (prima e ultima del lotto)',
   (cov[0]['line'], cov[-1]['line']) == (264, 442), (cov[0]['line'], cov[-1]['line']))
ck("gli 8 VALUE sono IDENTICI all'inglese (4 distinti)",
   len(VAL) == 8 and all(v['italian'] == v['english'] for v in VAL)
   and len({v['english'] for v in VAL}) == 4,
   [v['idx'] for v in VAL if v['italian'] != v['english']])
ck("le 16 unita' di prosa sono TUTTE tradotte (0 identiche)",
   all(v['italian'] != v['english'] for v in PROSA) and len(PROSA) == 16)
ck('14 stringhe distinte, 10 gruppi identici da DUE copie, una resa ciascuno',
   len(mult) == 14 and sum(1 for e, n in mult.items() if n > 1) == 10
   and set(n for e, n in mult.items() if n > 1) == {2}
   and all(len({v['italian'] for v in cov if v['english'] == e}) == 1 for e, n in mult.items() if n > 1),
   (len(mult), sorted(n for e, n in mult.items() if n > 1)))
ck('i quattro singolari sono le due schede e le due battute degli invasivi (20, 21, 22, 24)',
   sorted(v['idx'] for v in PROSA if mult[v['english']] == 1) == [20, 21, 22, 24],
   sorted(v['idx'] for v in PROSA if mult[v['english']] == 1))
ck('56 segnaposto in 8 famiglie, multiset identico',
   TOK_EN == TOK_IT and sum(TOK_EN.values()) == 56 and len(TOK_EN) == 8,
   (dict(TOK_EN), sum(TOK_EN.values())))
ck("l'ORDINE dei segnaposto e' identico dentro ogni unita'", not SEQ, SEQ)
ck('`<stopovers>` e\' un simbolo intero e `<planet stopovers>` NON compare in questo lotto',
   TOK_EN.get('<stopovers>') == 2 and TOK_EN.get('<planet stopovers>') is None
   and TOK_IT.get('<stopovers>') == 2 and TOK_IT.get('<planet stopovers>') is None)
ck('ZERO tab (asserzione negativa scritta)',
   sum(v['english'].count(TAB) for v in cov) == 0 == sum(v['italian'].count(TAB) for v in cov))
ck('ZERO virgolette (asserzione negativa scritta)',
   sum(v['english'].count(QUOTE) for v in cov) == 0 == sum(v['italian'].count(QUOTE) for v in cov))
ck("apici: ZERO in inglese, 1 in italiano (unita' 21, `un'ora`)",
   A_EN == [] and A_IT == [(21, 1)], (A_EN, A_IT))
ck('«Il pagamento sarà <payment>.» nelle 4 schede degli studiosi (2, 5, 8, 11)',
   [v['idx'] for v in PROSA if 'Il pagamento sarà <payment>.' in v['italian']] == [2, 5, 8, 11])
ck('«Il pagamento è <payment>.» nelle 2 schede del raccolto (14, 17)',
   [v['idx'] for v in PROSA if 'Il pagamento è <payment>.' in v['italian']] == [14, 17])
ck('«in cambio di un pagamento di <payment>» nelle 2 schede degli invasivi (20, 24)',
   [v['idx'] for v in PROSA if 'in cambio di un pagamento di <payment>' in v['italian']] == [20, 24])
ck('«Fai gli auguri ai …» in tutte e 6 le battute con questa formula (3, 6, 9, 12, 15, 18)',
   [v['idx'] for v in PROSA if 'Fai gli auguri ai' in v['italian']] == [3, 6, 9, 12, 15, 18])
ck('`Wanderer` invariato al plurale (`Wanderers` non compare)',
   prosa.count('Wanderer') >= 8 and 'Wanderers' not in prosa)
ck('lessico: «biologi», «botanici», «raccolta del cibo», «specie animale/vegetale invasiva», «stiva», «gabbie»',
   all(t in prosa for t in ('biologi', 'botanici', 'raccolta del cibo', 'specie animale invasiva',
                            'specie vegetale invasiva', 'stiva', 'gabbie')))
ck('nessun residuo inglese di struttura (the, and, with, their, these)',
   not [w for w in (' the ', ' and ', ' with ', ' their ', ' these ') if w in prosa.lower()],
   [w for w in (' the ', ' and ', ' with ', ' their ', ' these ') if w in prosa.lower()])
ck('registro: nessun «Lei» e nessuna cortesia',
   not re.search(r'\bLei\b|\bSuo\b|\bSua\b|mi scusi', prosa))
ck('nessun caporale e nessun carattere tipografico',
   not [v['idx'] for v in cov if any(c in v['italian'] for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026')])
rs = [v['ratio'] for v in cov]
ck('rapporto nel gate 0,55-1,90 (0,84-1,12; 427 -> 406 parole)',
   0.55 < min(rs) and max(rs) < 1.90, '%.2f - %.2f' % (min(rs), max(rs)))
ACC = re.compile(r"\b(e|piu|perche|cosi|gia|puo|cioe|percio)'(?![a-z])", re.I)
bad = [(v['idx'], ACC.search(v['italian']).group(0)) for v in cov if ACC.search(v['italian'])]
ck("tipografia (accenti veri, nessun apostrofo al posto dell'accento)", not bad, bad)
nonlat = [v['idx'] for v in cov for c in v['italian'] if ord(c) > 127 and not 0x00C0 <= ord(c) <= 0x024F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio',
   not [v['idx'] for v in cov if v['italian'] != v['italian'].rstrip() or '  ' in v['italian']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("26 unita' prima della 264: e' L252",
   db.execute('select count(*) from units where path=? and line<264', (PATH,)).fetchone()[0] == 26)
ck("42 unita' dopo la 442: il lotto NON chiude il file",
   db.execute('select count(*) from units where path=? and line>442', (PATH,)).fetchone()[0] == 42)
ck("confine misurato: riga 458, mission:Wanderer Invasive Species [1] (STESSO contesto)",
   db.execute('select line,context from units where path=? and line>442 order by line limit 1', (PATH,)).fetchone()
   == (458, 'mission:Wanderer Invasive Species [1]') and cov[-1]['context'] == 'mission:Wanderer Invasive Species [1]')
ck('il file intero: 92 unita, righe 15 - 891',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (92, 15, 891))
st = dict(db.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('le 24 unita sono PENDING (misurato)',
   db.execute('select count(*) from units where id in (%s) and state != "PENDING"'
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
