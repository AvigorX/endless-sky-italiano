r"""check.py — L282 (`data/wanderer/wanderer missions.txt`, righe 16-41). **Primo lotto del file**.

La missione **«Mereti: The Plant 1»**: i Mereti chiedono aiuto per una pianta che non cresce, e due Wanderer propongono di
portarla su <planet>. Il testo ha una caratteristica che va **conservata alla lettera**: **nove alternative fra parentesi
quadre** (`[difenderci, proteggerci]`, `[genitori? antenati?]`, …), che il gioco sceglie a runtime. Il test verifica:

1. **le nove alternative**: stesse posizioni, **due opzioni ciascuna**, stesse parentesi quadre;
2. **nove tab** (unità 4-12) e **sedici virgolette**, contate **per unità**;
3. **il `VALUE`** (`Plant to <planet>`) è **copiato**, le altre dodici unità sono tradotte;
4. **`Unfettered`** nella prosa diventa **«Slegati»** (forma maggioritaria del corpus: 221 contro 61), e `Wanderer`/`Mereti`
   restano invariati.
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
ALT = re.compile(r'\[[^\]]*\]')
HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
PATH = 'data/wanderer/wanderer missions.txt'
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
by = {u['idx']: u for u in cov}
TABBED = [4, 5, 6, 7, 8, 9, 10, 11, 12]
TOK = {'<planet>': 3, '<destination>': 1}
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck('unita tradotte 13/13', len(cov) == 13 == len(units), '%d/%d' % (len(cov), len(units)))
ck('tipi: 11 MISSION_TEXT + 1 DESCRIPTION + 1 VALUE',
   collections.Counter(u['kind'] for u in units) == {'MISSION_TEXT': 11, 'DESCRIPTION': 1, 'VALUE': 1},
   dict(collections.Counter(u['kind'] for u in units)))
ck('un solo contesto, `mission:Wanderers: Mereti: The Plant 1`, righe 16-41',
   {u['context'] for u in cov} == {'mission:Wanderers: Mereti: The Plant 1'}
   and cov[0]['line'] == 16 and cov[-1]['line'] == 41)
ck('il VALUE e COPIATO (`Plant to <planet>`)',
   by[1]['kind'] == 'VALUE' and by[1]['italian'] == by[1]['english'] == 'Plant to <planet>')
ck('le 12 unita di prosa sono TRADOTTE, nessuna copiata',
   all(by[i]['italian'] != by[i]['english'] for i in by if i != 1),
   [i for i in by if i != 1 and by[i]['italian'] == by[i]['english']])
ck('TAB: nove in inglese e nove in italiano, sulle stesse unita, come PRIMO carattere',
   sum(u['english'].count(TAB) for u in cov) == 9 == sum(u['italian'].count(TAB) for u in cov)
   and [u['idx'] for u in cov if TAB in u['english']] == TABBED == [u['idx'] for u in cov if TAB in u['italian']]
   and all(u['italian'].startswith(TAB) for u in cov if u['idx'] in TABBED))
ck('VIRGOLETTE: 16 in inglese e 16 in italiano, con lo STESSO numero per ogni unita',
   sum(u['english'].count(QUOTE) for u in cov) == 16 == sum(u['italian'].count(QUOTE) for u in cov)
   and all(u['english'].count(QUOTE) == u['italian'].count(QUOTE) for u in cov))
def opzioni(x):
    return len([p for p in re.split(r'[,?]', x.strip('[]')) if p.strip()])


ck('ALTERNATIVE fra parentesi quadre: nove per lingua, e ogni coppia ha lo STESSO numero di opzioni',
   sum(len(ALT.findall(u['english'])) for u in cov) == 9 == sum(len(ALT.findall(u['italian'])) for u in cov)
   and [opzioni(a) for u in cov for a in ALT.findall(u['english'])]
   == [opzioni(a) for u in cov for a in ALT.findall(u['italian'])]
   and [opzioni(a) for u in cov for a in ALT.findall(u['italian'])] == [2] * 8 + [2],
   [(a, opzioni(a)) for u in cov for a in ALT.findall(u['italian']) if opzioni(a) != 2])
ck('le alternative stanno nelle stesse tre unita (5, 8, 11), nello stesso ordine',
   [u['idx'] for u in cov if '[' in u['english']] == [5, 8, 11]
   == [u['idx'] for u in cov if '[' in u['italian']]
   and [len(ALT.findall(by[i]['english'])) for i in (5, 8, 11)] == [2, 2, 5]
   == [len(ALT.findall(by[i]['italian'])) for i in (5, 8, 11)])
ck('SEGNAPOSTO: `<planet>` tre e `<destination>` uno, identici in inglese e italiano',
   {t: sum(collections.Counter(TAG.findall(u['english']))[t] for u in cov) for t in TOK} == TOK
   == {t: sum(collections.Counter(TAG.findall(u['italian']))[t] for u in cov) for t in TOK})
ck('APICI: quattro in inglese, cinque in italiano',
   sum(u['english'].count(APOS) for u in cov) == 4 and sum(u['italian'].count(APOS) for u in cov) == 5,
   (sum(u['english'].count(APOS) for u in cov), sum(u['italian'].count(APOS) for u in cov)))
ck("`'mentori'` fra apici semplici nella DESCRIPTION: due apici, conservati",
   "'mentori'" in by[2]['italian'])
ck('`Unfettered` nella prosa diventa «Slegati»; `Wanderer` e `Mereti` restano invariati',
   'agli Slegati' in by[11]['italian'] and 'Unfettered' not in by[11]['italian']
   and 'Wanderer' in by[11]['italian'] and 'Mereti' in by[3]['italian'])
ck('lessico: serre, vaso, petali blu intenso, foglie verde acqua, droni',
   'serre' in by[3]['italian'] and 'vaso' in by[4]['italian']
   and 'blu intenso' in by[4]['italian'] and 'verde acqua' in by[4]['italian']
   and 'drone' in by[3]['italian'] and 'droni' in by[12]['italian'])
ck('la richiesta dei Mereti e la soluzione dei Wanderer: portarla su <planet> per ora',
   'aiutaci ancora' in by[5]['italian'] and 'portiamola lì per ora' in by[11]['italian']
   and 'breve periodo' in by[11]['italian'])
ck('nessun caporale, nessun carattere tipografico',
   not [u['idx'] for u in cov for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026' if c in u['italian']])
nonlat = [(u['idx'], c) for u in cov for c in u['italian'] if ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']],
   [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90 sulle 12 unita tradotte (0,74-1,24)',
   all(0.55 < by[i]['ratio'] < 1.90 for i in by if i != 1),
   [(i, by[i]['ratio']) for i in by if i != 1 and not 0.55 < by[i]['ratio'] < 1.90])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("ZERO unita' prima della 16: il lotto APRE il file",
   db.execute('select count(*) from units where path=? and line<16', (PATH,)).fetchone()[0] == 0)
ck("41 unita' dopo la 41",
   db.execute('select count(*) from units where path=? and line>41', (PATH,)).fetchone()[0] == 41)
ck('il file ha 54 unita, righe 16-182',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (54, 16, 182),
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone())
st = dict(db.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('tutte le 13 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · 1 contesto · 9 tab · 16 virgolette · 9 alternative' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
