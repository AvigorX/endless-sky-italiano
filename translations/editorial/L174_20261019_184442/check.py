r"""check.py — L174 (`data/avgi/avgi ships.txt`, 14 unita', righe 120-522). **Apre il file.**

Primo lotto di prosa lunga di astronavi. Controlli propri: **zero token** (asserzione vuota scritta); **8 tab iniziali**
conservati (righe 121, 122, 267, 268, 376, 377, 521, 522); **la formula dei propulsori** ripetuta 4 volte (unita' 3, 7,
10, 14) che deve essere **identica a meno del nome**; la coppia **2/9** che e' **speculare** (centrifuga→container contro
container→centrifuga); i **4 possessivi inglesi** che in italiano diventano «di + nome» (gli apici NON si contano fra le
lingue); i nomi delle astronavi **invariati**.
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
SHIPS = ('Koryfi', 'Melodikos', 'Avlaki', 'Harmonikos')
FORMULA = [3, 7, 10, 14]
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 14/14", len(cov) == 14 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 12 DESCRIPTION + 2 VALUE', collections.Counter(u['kind'] for u in units)
   == {'DESCRIPTION': 12, 'VALUE': 2})
ck('UN asserzione vuota: ZERO UI_LABEL', [u['idx'] for u in units if u['kind'] == 'UI_LABEL'] == [])
ck('ZERO token in tutto il lotto (asserzione vuota scritta)',
   {t for u in units for t in TAGS.findall(u['english'])} == set()
   == {t for v in cov for t in TAGS.findall(v['italian'])})
ck('8 unita con tab iniziale, idx 2, 3, 6, 7, 9, 10, 13, 14 — e restano in traduzione',
   [v['idx'] for v in cov if v['english'].startswith('\t')] == [2, 3, 6, 7, 9, 10, 13, 14]
   == [v['idx'] for v in cov if v['italian'].startswith('\t')])
ck('i tab non raddoppiano e le altre 6 unita non ne hanno',
   all(v['italian'].count('\t') == 1 for v in cov if v['english'].startswith('\t'))
   and not [v['idx'] for v in cov if not v['english'].startswith('\t') and '\t' in v['italian']])
ck('2 VALUE identici al sorgente (Melodikos, Harmonikos)',
   [v['idx'] for v in cov if v['kind'] == 'VALUE'] == [4, 11]
   and [v['idx'] for v in cov if v['kind'] == 'VALUE' and v['italian'] != v['english']] == [])
ck('i 4 nomi delle astronavi restano invariati in ogni unita che li nomina',
   all(n in v['italian'] for v in cov for n in SHIPS if n in v['english']),
   [(v['idx'], n) for v in cov for n in SHIPS if n in v['english'] and n not in v['italian']])
ck('la formula dei propulsori (3, 7, 10, 14) e identica a meno del nome',
   len({re.sub('|'.join(SHIPS), 'NOME', v['italian']) for v in cov if v['idx'] in FORMULA}) == 1,
   sorted({re.sub('|'.join(SHIPS), 'NOME', v['italian']) for v in cov if v['idx'] in FORMULA}))
ck('e in inglese la stessa proprieta vale (controllo di sanita sulla fonte)',
   len({re.sub('(?:' + '|'.join(SHIPS) + ")'?s?", 'NOME', v['english'])
        for v in cov if v['idx'] in FORMULA}) == 1)
ck('ogni formula nomina la PROPRIA astronave',
   all(by[i]['context'].split(':')[1] in by[i]['italian'] for i in FORMULA))
ck('2 e 9 sono speculari: una toglie la centrifuga, l altra la aggiunge',
   'sostituendo la centrifuga modulare con un set di container standard' in by[2]['italian']
   and 'sostituendo i container standard con un habitat centrifugo' in by[9]['italian'])
ck('6 e 13 si rimandano a vicenda (Melodikos↔Harmonikos)',
   'della Harmonikos' in by[6]['italian'] and 'della Melodikos' in by[13]['italian']
   and 'della Melodikos' not in by[6]['italian'] and 'della Harmonikos' not in by[13]['italian'])
ck('i 4 possessivi inglesi diventano «di + nome»: IT senza apici possessivi',
   sum(v['english'].count("'") for v in cov) == 4
   and [v['idx'] for v in cov if "'" in v['english']] == FORMULA
   and not [v['idx'] for v in cov if re.search(r"(Koryfi|Melodikos|Avlaki|Harmonikos)'", v['italian'])])
ck('14 unita, 14 testi inglesi distinti', len({v['english'] for v in cov}) == 14)
ck('4 contesti distinti, con 3+4+3+4 unita per nave',
   len({u['context'] for u in units}) == 4
   and sorted(collections.Counter(u['context'] for u in units).values()) == [3, 3, 4, 4],
   collections.Counter(u['context'] for u in units))
ck('prima e ultima unita: righe 120 e 522',
   (cov[0]['line'], cov[-1]['line']) == (120, 522)
   and cov[0]['context'] == 'ship:Koryfi' and cov[-1]['context'] == 'ship:Harmonikos')
ck('nessuno spazio finale in inglese ne in italiano (il tab iniziale e ammesso)',
   not [v['idx'] for v in cov
        if v['english'].rstrip('\t') != v['english'].rstrip('\t').rstrip()
        or v['italian'].rstrip('\t') != v['italian'].rstrip('\t').rstrip()])
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' you ', ' to the ', ' will be ',
        ' is ', ' are ', ' from the ', ' its ', ' it is ')
LONG = ' '.join(v['italian'] for v in cov if v['kind'] != 'VALUE').lower()
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
