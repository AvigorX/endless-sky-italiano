r"""check.py — L184 (`data/human/outfits.txt`, 13 unita', righe 520-606). **CHIUDE IL FILE.**

Ultimo lotto: **12 `DESCRIPTION` + 1 `VALUE`**, **1 tab** (idx 3) e — primo caso del file — **2 virgolette**, che pero'
**non sono tipografia**: stanno nel `VALUE` `"Puny"`, cioe' **dentro il nome dell'oggetto**. Il `VALUE` si copia alla
lettera, virgolette comprese, e una sola unita' le contiene. **7 apici inglesi** in tre unita' (idx 3, 7, 10, 13), tutti
possessivi o elisione: legati uno per uno alla causa e verificati separatamente in italiano.
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
EN_APOS = {3: ["Pookie's", "Pookie's"], 7: ["Republic's", "pilot's"], 10: ["Cruiser's", "Republic's"], 13: ["can't"]}
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 13/13", len(cov) == 13 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 12 DESCRIPTION + 1 VALUE', collections.Counter(u['kind'] for u in units)
   == {'DESCRIPTION': 12, 'VALUE': 1})
ck('UN asserzione vuota: ZERO UI_LABEL', [u['idx'] for u in units if u['kind'] == 'UI_LABEL'] == [])
ck('ZERO token in tutto il lotto (asserzione vuota scritta)',
   {t for u in units for t in TAGS.findall(u['english'])} == set()
   == {t for v in cov for t in TAGS.findall(v['italian'])})
ck('il VALUE e\' `"Puny"`: le 2 virgolette stanno DENTRO il nome, copiate alla lettera',
   by[1]['italian'] == by[1]['english'] == '"Puny"' and by[1]['english'].count('"') == 2)
ck('le 2 virgolette del lotto sono TUTTE e SOLE in idx 1 (non sono discorso diretto)',
   sum(v['english'].count('"') for v in cov) == 2 == sum(v['italian'].count('"') for v in cov)
   and [v['idx'] for v in cov if '"' in v['english']] == [1] == [v['idx'] for v in cov if '"' in v['italian']])
ck('1 tab iniziale, idx 3, in inglese e in italiano',
   [v['idx'] for v in cov if v['english'].startswith('\t')] == [3]
   == [v['idx'] for v in cov if v['italian'].startswith('\t')])
ck('7 apici inglesi, distribuiti 2/2/2/1 su idx 3, 7, 10, 13',
   sum(v['english'].count("'") for v in cov) == 7
   and {v['idx']: v['english'].count("'") for v in cov if "'" in v['english']} == {3: 2, 7: 2, 10: 2, 13: 1})
ck('ogni apice inglese legato alla sua causa (possessivo o elisione)',
   all(w in by[i]['english'] for i, ws in EN_APOS.items() for w in ws),
   [(i, w) for i, ws in EN_APOS.items() for w in ws if w not in by[i]['english']])
ck('nessun possessivo inglese sopravvissuto in italiano',
   not [v['idx'] for v in cov if re.search(r"\b[A-Za-z]+'s\b", v['italian'])])
ck('gli apici italiani NON sono la copia dei 7 inglesi: 3, tutti elisione (idx 9 e 13)',
   {v['idx']: v['italian'].count("'") for v in cov if "'" in v['italian']} == {9: 1, 13: 2},
   {v['idx']: v['italian'].count("'") for v in cov if "'" in v['italian']})
ck('`Puny`, `Pookie`, `Freedom`, `Skadenga`, `Ildico Drifa`, `Free Worlds` restano invariati',
   all(n in ' '.join(v['italian'] for v in cov) for n in
       ('Puny', 'Pookie', 'Freedom', 'Skadenga', 'Ildico Drifa', 'Free Worlds')))
ck('le due pietre si distinguono: Tear of Skade fredda, Blood of Surtr calda',
   'piuttosto fredda' in by[4]['italian'] and 'energia e calore' in by[5]['italian'])
ck('la fila delle licenze sale di rarita\': standard, raro, molto raro, manciata',
   'standard' in by[12]['italian'] and 'particolarmente raro' in by[9]['italian']
   and 'privilegio molto raro' in by[10]['italian'] and 'manciata di persone' in by[11]['italian'])
ck('idx 13 chiude il file con la sagoma non identificata',
   'sagoma' in by[13]['italian'] and 'astronave-città' in by[13]['italian'])
ck('13 unita, 13 testi inglesi distinti', len({v['english'] for v in cov}) == 13,
   len({v['english'] for v in cov}))
ck('11 contesti: Puny con 3 unita, dieci con 1',
   len({u['context'] for u in units}) == 11
   and sorted(collections.Counter(u['context'] for u in units).values()) == [1] * 10 + [3],
   collections.Counter(u['context'] for u in units))
ck('prima e ultima unita: righe 520 e 606 (max(line) del file)',
   (cov[0]['line'], cov[-1]['line']) == (520, 606)
   and cov[0]['context'] == 'outfit:Puny' and cov[-1]['context'] == 'outfit:City-Ship License')
ck('nessuno spazio finale, tab iniziale ammesso',
   not [v['idx'] for v in cov
        if v['english'].rstrip('\t') != v['english'].rstrip('\t').rstrip()
        or v['italian'].rstrip('\t') != v['italian'].rstrip('\t').rstrip()])
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' you ', ' to the ', ' will be ',
        ' is ', ' are ', ' from the ', ' its ', ' it is ', ' such as ', ' rather than ')
LONG = ' '.join(v['italian'] for v in cov).lower()
ck('nessun residuo inglese fuori dai nomi propri', not [w for w in ENGW if w in LONG],
   [w for w in ENGW if w in LONG])
CORT = re.findall(r'\bLei\b|(?<![.!?] )\b(?:Suo|Sua|Suoi|Sue)\b', ' '.join(v['italian'] for v in cov))
ck('nessuna forma di cortesia «Lei»', not CORT, CORT)
rs = [v['ratio'] for v in cov]
ck('rapporto nel gate 0,55-1,90', 0.55 < min(rs) and max(rs) < 1.90, '%.2f - %.2f' % (min(rs), max(rs)))
bad = [(v['idx'], n) for v in cov for p, n in ((r"\b(e|piu|perche|cosi|gia|puo|cioe|percio|fa)'", 'accento'),
       ('\u2026', 'ellissi'), ('\u2014', 'em dash'), ('\u2013', 'en dash'), ('\u2019', 'apostrofo curvo'),
       ('\u00ab', 'caporale'), ('\u00bb', 'caporale')) if re.search(p, v['italian'])]
ck('tipografia (accenti veri, nessun carattere tipografico)', not bad, bad)
nonlat = [v['idx'] for v in cov for c in v['italian']
          if ord(c) > 127 and not 0x00C0 <= ord(c) <= 0x024F]
ck('caratteri non latini', not nonlat, nonlat)
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
      len(parts), len([u for u in units if u['idx'] not in tr])))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
