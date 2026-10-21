r"""check.py — L169 (`data/human/paradise world jobs.txt`, 17 unita', righe 376-522).

Terzo lotto del file. Controlli propri: **38 token su 8 simboli**, con **`<npc>`** (4, segnaposto e non nome proprio);
**due coppie di unita' identiche in contesti diversi** (1/3 e 2/4: `high-class tourists` e `tourist group`); le
**2 virgolette doppie** in idx 13 (`"si rendano utili"`) e gli **apici semplici** in idx 1/3 (`'strutture adeguate'`).
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


TOK = {'<payment>': 12, '<destination>': 7, '<planet>': 5, '<bunks>': 5, '<npc>': 4, '<stopovers>': 2,
       '<tons>': 2, '<commodity>': 1}
ck("unita' tradotte 17/17", len(cov) == 17 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 3 VALUE + 6 DESCRIPTION + 8 DIALOG',
   collections.Counter(u['kind'] for u in units) == {'VALUE': 3, 'DESCRIPTION': 6, 'DIALOG': 8})
ck('UN asserzione vuota: ZERO UI_LABEL', [u['idx'] for u in units if u['kind'] == 'UI_LABEL'] == [])
ck('38 token su 8 simboli, stesso multiset in italiano',
   dict(collections.Counter(t for u in units for t in TAGS.findall(u['english']))) == TOK
   == dict(collections.Counter(t for v in cov for t in TAGS.findall(v['italian'])))
   and sum(TOK.values()) == 38 and len(TOK) == 8)
ck('parita per UNITA: stesso ordine di simboli in tutte le 17',
   not [v['idx'] for v in cov if TAGS.findall(v['italian']) != TAGS.findall(v['english'])],
   [(v['idx'], TAGS.findall(v['english']), TAGS.findall(v['italian']))
    for v in cov if TAGS.findall(v['italian']) != TAGS.findall(v['english'])])
ck('`<npc>` e un segnaposto: 4 volte, mai nel testo fuori dai tag',
   sum(v['english'].count('<npc>') for v in cov) == 4 == sum(v['italian'].count('<npc>') for v in cov)
   and not [v['idx'] for v in cov if re.search(r'<npc>\s*\w*\s*npc', v['italian'], re.I)])
ck('3 VALUE identici al sorgente',
   [v['idx'] for v in cov if v['kind'] == 'VALUE' and v['italian'].rstrip() != v['english'].rstrip()] == []
   and [v['idx'] for v in cov if v['kind'] == 'VALUE'] == [9, 12, 15])
ck('1 e 3 sono lo stesso testo in due contesti, e la resa e identica',
   by[1]['english'] == by[3]['english'] and by[1]['italian'] == by[3]['italian']
   and by[1]['context'] != by[3]['context'])
ck('2 e 4 sono lo stesso testo in due contesti, e la resa e identica',
   by[2]['english'] == by[4]['english'] and by[2]['italian'] == by[4]['italian']
   and by[2]['context'] != by[4]['context'])
ck('17 unita, 15 testi inglesi distinti (le coppie 1/3 e 2/4)', len({v['english'] for v in cov}) == 15,
   len({v['english'] for v in cov}))
ck('2 virgolette doppie, in idx 13, e la frase citata resta citata',
   sum(v['english'].count('"') for v in cov) == 2 == sum(v['italian'].count('"') for v in cov)
   and by[13]['english'].count('"') == 2 == by[13]['italian'].count('"')
   and '"si rendano utili"' in by[13]['italian'])
ck('la frase fra apici di idx 1/3 resta fra apici (2 apici in italiano, 3 in inglese)',
   all(by[i]['english'].count("'") == 3 for i in (1, 3))
   and all(by[i]['italian'].count("'") == 2 for i in (1, 3))
   and "'appropriate facilities'" in by[1]['english']
   and all("'strutture adeguate'" in by[i]['italian'] for i in (1, 3)))
ck('idx 5 (crociera) ha 6 token nell ordine giusto',
   TAGS.findall(by[5]['english']) == ['<npc>', '<stopovers>', '<tons>', '<commodity>', '<destination>', '<payment>']
   == TAGS.findall(by[5]['italian']))
ck('idx 7: planet + npc + stopovers (ordine invariato)',
   TAGS.findall(by[7]['italian']) == ['<planet>', '<npc>', '<stopovers>'])
ck('nessun tab (asserzione vuota scritta)',
   [v['idx'] for v in cov if '\t' in v['english'] or '\t' in v['italian']] == [])
ck('6 contesti distinti', len({u['context'] for u in units}) == 6,
   sorted({u['context'] for u in units}))
ck('prima e ultima unita: righe 376 e 522',
   (cov[0]['line'], cov[-1]['line']) == (376, 522)
   and cov[0]['context'] == 'mission:Transport high-class tourists'
   and cov[-1]['context'] == 'mission:Paradise Job: Retirees')
ck('zero spazi iniziali e finali identici al sorgente (17/17)',
   not [v['idx'] for v in cov
        if len(v['italian']) - len(v['italian'].rstrip()) != len(v['english']) - len(v['english'].rstrip())
        or len(v['italian']) - len(v['italian'].lstrip()) != len(v['english']) - len(v['english'].lstrip())])
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' you ', ' to the ', ' will be ',
        ' is ', ' are ', ' from the ', ' their ', ' they ')
LONG = ' '.join(TAGS.sub('""', v['italian']) for v in cov if v['kind'] != 'VALUE').lower()
ck('nessun residuo inglese fuori dai VALUE', not [w for w in ENGW if w in LONG], [w for w in ENGW if w in LONG])
CORT = re.findall(r'\bLei\b|(?<![.!?] )\b(?:Suo|Sua|Suoi|Sue)\b', ' '.join(v['italian'] for v in cov))
ck('nessuna forma di cortesia «Lei»', not CORT, CORT)
rs = [v['ratio'] for v in cov]
ck('rapporto nel gate 0,55-1,90', 0.55 < min(rs) and max(rs) < 1.90, '%.2f - %.2f' % (min(rs), max(rs)))
bad = [(v['idx'], n) for v in cov for p, n in ((r"\b(e|piu|perche|cosi|gia|puo|cioe|percio|fa)'", 'accento'),
       ('\u2026', 'ellissi'), ('\u2014', 'em dash'), ('\u2013', 'en dash'), ('\u2019', 'apostrofo curvo'),
       ('\u00ab', 'caporale'), ('\u00bb', 'caporale')) if re.search(p, v['italian'])]
ck('tipografia (accenti veri, nessun carattere tipografico)', not bad, bad)
nonlat = [v['idx'] for v in cov for c in TAGS.sub('', v['italian'])
          if ord(c) > 127 and not 0x00C0 <= ord(c) <= 0x024F]
ck('caratteri non latini (fuori dai token)', not nonlat, nonlat)
c = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
st = dict(c.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('tutte le 17 unita sono PENDING nel database (misurato)',
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
      len(parts), len([u for u in units if u['idx'] not in tr])))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
