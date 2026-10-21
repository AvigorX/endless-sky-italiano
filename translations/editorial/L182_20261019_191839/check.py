r"""check.py — L182 (`data/human/outfits.txt`, 14 unita', righe 236-387).

Terzo lotto del file: **13 `DESCRIPTION` + 1 `VALUE`**, **1 tab** (idx 10), zero virgolette, e **6 apici inglesi** — il
numero piu' alto degli ultimi lotti. Il controllo **lega ogni apice alla sua causa** (idx 7 e 14: possessivo `ship's` /
`Republic's`; idx 8 e 12: elisione `You're` / `you're`; idx 8: `can't`) e verifica **separatamente** gli apici italiani
(elisione e troncamento: `un po'`, `l'interno`, `un'espansione`, `l'aggiunta`) — perche' il conteggio **non** si conserva
fra le lingue.
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
EN_APOS = {7: ["ship's"], 8: ["You're", "can't"], 12: ["you're"], 14: ["ship's", "Republic's"]}
IT_APOS = {6: ["dell'equipaggio"], 9: ["un po'"], 10: ["l'interno"], 11: ["un'espansione"],
           12: ["dell'equipaggio", "nell'area"], 14: ["l'aggiunta", "dell'ordine"]}
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 14/14", len(cov) == 14 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 13 DESCRIPTION + 1 VALUE', collections.Counter(u['kind'] for u in units)
   == {'DESCRIPTION': 13, 'VALUE': 1})
ck('UN asserzione vuota: ZERO UI_LABEL', [u['idx'] for u in units if u['kind'] == 'UI_LABEL'] == [])
ck('ZERO token in tutto il lotto (asserzione vuota scritta)',
   {t for u in units for t in TAGS.findall(u['english'])} == set()
   == {t for v in cov for t in TAGS.findall(v['italian'])})
ck('ZERO virgolette in inglese e in italiano (asserzione vuota scritta)',
   sum(v['english'].count('"') for v in cov) == 0 == sum(v['italian'].count('"') for v in cov))
ck('1 VALUE copiato alla lettera, parentesi comprese: `Jump Drives (Broken)`',
   [v['idx'] for v in cov if v['kind'] == 'VALUE'] == [1]
   and by[1]['italian'] == by[1]['english'] == 'Jump Drives (Broken)'
   and '(' in by[1]['english'])
ck('1 tab iniziale, idx 10, in inglese e in italiano',
   [v['idx'] for v in cov if v['english'].startswith('\t')] == [10]
   == [v['idx'] for v in cov if v['italian'].startswith('\t')])
ck('6 apici inglesi, distribuiti 1/2/1/2 su idx 7, 8, 12, 14',
   sum(v['english'].count("'") for v in cov) == 6
   and {v['idx']: v['english'].count("'") for v in cov if "'" in v['english']} == {7: 1, 8: 2, 12: 1, 14: 2})
ck('ogni apice inglese legato alla sua causa (possessivo o elisione)',
   not [(i, w) for i, ws in EN_APOS.items() for w in ws if w not in by[i]['english']],
   [(i, w) for i, ws in EN_APOS.items() for w in ws if w not in by[i]['english']])
ck('nessun possessivo inglese sopravvissuto in italiano (`ship\'s`, `Republic\'s`)',
   not [v['idx'] for v in cov if re.search(r"\b[A-Za-z]+'s\b", v['italian'])])
ck('gli apici italiani sono 9, tutti di elisione o troncamento, e NON sono la copia dei 6 inglesi',
   sum(v['italian'].count("'") for v in cov) == 9
   and {v['idx']: v['italian'].count("'") for v in cov if "'" in v['italian']}
       == {6: 1, 9: 2, 10: 1, 11: 1, 12: 2, 14: 2}
   and not [(i, w) for i, ws in IT_APOS.items() for w in ws if w not in by[i]['italian']])
ck('i due conteggi sono DIVERSI (6 EN, 9 IT): nessuna corrispondenza fra le lingue pretesa',
   sum(v['english'].count("'") for v in cov) == 6 != sum(v['italian'].count("'") for v in cov) == 9)
ck('`Kraz Cybernetics` resta invariato (nome proprio in idx 6)',
   'Kraz Cybernetics' in by[6]['english'] and 'Kraz Cybernetics' in by[6]['italian'])
ck('`Cloaking Device` -> «dispositivo di occultamento» in prosa (idx 8, dove il nome e\' il contesto)',
   'cloaking device' in by[8]['english'].lower()
   and 'dispositivo di occultamento' in by[8]['italian']
   and 'cloaking' not in by[8]['italian'].lower())
ck('i tre scanner ripetono la stessa frase finale', 
   [i for i in (3, 4, 7) if 'aumenta portata e velocità di scansione' in by[i]['italian']] == [3, 4, 7])
ck('`Republic Navy` -> «Marina della Repubblica»; `militia` -> «milizia»',
   'Marina della Repubblica' in by[4]['italian'] and 'della milizia' in by[6]['italian'])
ck('`cooling systems` (idx 10) coerente con L180: «sistemi di raffreddamento»',
   'sistemi di raffreddamento' in by[10]['italian'])
ck('14 unita, 14 testi inglesi distinti', len({v['english'] for v in cov}) == 14,
   len({v['english'] for v in cov}))
ck('12 contesti: Jump Drive (Broken) e Outfits Expansion con 2 unita, dieci con 1',
   len({u['context'] for u in units}) == 12
   and sorted(collections.Counter(u['context'] for u in units).values()) == [1] * 10 + [2, 2],
   collections.Counter(u['context'] for u in units))
ck('prima e ultima unita: righe 236 e 387',
   (cov[0]['line'], cov[-1]['line']) == (236, 387)
   and cov[0]['context'] == 'outfit:Jump Drive (Broken)' and cov[-1]['context'] == 'outfit:Brig')
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
      len(parts), len([u for u in units if u['idx'] not in tr])))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
