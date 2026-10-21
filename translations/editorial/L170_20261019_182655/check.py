r"""check.py — L170 (`data/human/paradise world jobs.txt`, 20 unita', righe 526-691).

Quarto lotto del file. Controlli propri: **39 token su 7 simboli** con **`<martini house>`** (composto, una volta);
**12 virgolette doppie** (record della campagna) verificate **per unita'**; **quattro `VALUE` "Shipment to <planet>"
identici** in contesti diversi; e la coppia 4/7, che nel **sorgente** differisce solo per un refuso (`anyonymous`) e in
italiano deve essere **identica**.
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


TOK = {'<payment>': 11, '<planet>': 9, '<destination>': 7, '<cargo>': 5, '<bunks>': 4, '<tons>': 2,
       '<martini house>': 1}
ck("unita' tradotte 20/20", len(cov) == 20 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 8 VALUE + 8 DESCRIPTION + 3 DIALOG + 1 MISSION_TEXT',
   collections.Counter(u['kind'] for u in units)
   == {'VALUE': 8, 'DESCRIPTION': 8, 'DIALOG': 3, 'MISSION_TEXT': 1})
ck('UN asserzione vuota: ZERO UI_LABEL', [u['idx'] for u in units if u['kind'] == 'UI_LABEL'] == [])
ck('39 token su 7 simboli, stesso multiset in italiano',
   dict(collections.Counter(t for u in units for t in TAGS.findall(u['english']))) == TOK
   == dict(collections.Counter(t for v in cov for t in TAGS.findall(v['italian'])))
   and sum(TOK.values()) == 39 and len(TOK) == 7)
ck('parita per UNITA: stesso ordine di simboli in tutte le 20',
   not [v['idx'] for v in cov if TAGS.findall(v['italian']) != TAGS.findall(v['english'])],
   [(v['idx'], TAGS.findall(v['english']), TAGS.findall(v['italian']))
    for v in cov if TAGS.findall(v['italian']) != TAGS.findall(v['english'])])
ck('`<martini house>` intero, una volta sola (idx 20)',
   [v['idx'] for v in cov if '<martini house>' in v['english']] == [20] == [
       v['idx'] for v in cov if '<martini house>' in v['italian']]
   and not re.search(r'<martini>\s+house', by[20]['italian']))
ck('8 VALUE identici al sorgente',
   len([v for v in cov if v['kind'] == 'VALUE']) == 8
   and [v['idx'] for v in cov if v['kind'] == 'VALUE' and v['italian'].rstrip() != v['english'].rstrip()] == [])
ck('12 virgolette, tutte in idx 2, 3, 6, 9, 10, e la resa le conserva',
   sum(v['english'].count('"') for v in cov) == 12 == sum(v['italian'].count('"') for v in cov)
   and [v['idx'] for v in cov if '"' in v['english']] == [2, 3, 6, 9, 10]
   == [v['idx'] for v in cov if '"' in v['italian']]
   and [v['english'].count('"') for v in (by[2], by[3], by[6], by[9], by[10])] == [2, 4, 2, 2, 2]
   == [v['italian'].count('"') for v in (by[2], by[3], by[6], by[9], by[10])])
ck('le frasi citate restano citate: "pensionati", "averi più cari", "Ritiro nella Natura"',
   '"pensionati"' in by[2]['italian'] and '"averi più cari"' in by[3]['italian']
   and '"Ritiro nella Natura"' in by[9]['italian'] and '"guide naturalistiche"' in by[10]['italian'])
ck('coppia 2/6 e 1/5 e 12/14: resa identica nei contesti diversi',
   by[1]['italian'] == by[5]['italian'] and by[2]['italian'] == by[6]['italian']
   and by[12]['italian'] == by[14]['italian'])
ck('4 `VALUE` "Shipment to <planet>" identici in 4 contesti',
   len({v['context'] for v in cov if v['english'] == 'Shipment to <planet>'}) == 4
   and len({v['italian'] for v in cov if v['english'] == 'Shipment to <planet>'}) == 1)
ck('4 e 7 differiscono nel SORGENTE solo per il refuso "anyonymous": in italiano sono identici',
   by[4]['english'] != by[7]['english']
   and 'anyonymous' in by[7]['english'] and 'anonymous' in by[4]['english']
   and by[4]['italian'] == by[7]['italian'])
ck('20 unita, 14 testi inglesi distinti (il refuso di idx 7 ne crea uno in piu)',
   len({v['english'] for v in cov}) == 14, len({v['english'] for v in cov}))
ck('idx 20: bunks + martini house + cargo + planet + payment',
   TAGS.findall(by[20]['italian']) == ['<bunks>', '<martini house>', '<cargo>', '<planet>', '<payment>'])
ck('8 contesti distinti', len({u['context'] for u in units}) == 8)
ck('prima e ultima unita: righe 526 e 691',
   (cov[0]['line'], cov[-1]['line']) == (526, 691)
   and cov[0]['context'] == 'mission:Paradise Job: Pirate Retirees (Illegal)'
   and cov[-1]['context'] == 'mission:Martini Evacuation (Resident Family)')
ck('zero tab (asserzione vuota scritta)',
   [v['idx'] for v in cov if '\t' in v['english'] or '\t' in v['italian']] == [])
ck('zero spazi iniziali e finali identici al sorgente (20/20)',
   not [v['idx'] for v in cov
        if len(v['italian']) - len(v['italian'].rstrip()) != len(v['english']) - len(v['english'].rstrip())
        or len(v['italian']) - len(v['italian'].lstrip()) != len(v['english']) - len(v['english'].lstrip())])
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' you ', ' to the ', ' will be ',
        ' is ', ' are ', ' from the ', ' their ', ' they ', ' of their ')
LONG = ' '.join(TAGS.sub('""', v['italian']) for v in cov if v['kind'] != 'VALUE').lower()
ck('nessun residuo inglese fuori dai VALUE', not [w for w in ENGW if w in LONG], [w for w in ENGW if w in LONG])
ck('i nomi propri restano inglesi: Gemini Shipyards, Lovelace Labs, Polymath Nanoinstruments, Republic Navy Yard',
   all(n in by[i]['italian'] for i, n in ((12, 'Gemini Shipyards'), (16, 'Lovelace Labs'),
                                          (18, 'Polymath Nanoinstruments'), (12, 'Republic Navy Yard'))))
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
      len(parts), len([u for u in units if u['idx'] not in tr])))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
