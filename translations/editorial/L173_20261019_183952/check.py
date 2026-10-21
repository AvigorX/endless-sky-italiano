r"""check.py — L173 (`data/human/paradise world jobs.txt`, 6 unita', righe 1356-1413). **Chiude il file.**

Ultimo lotto: 3 `VALUE` **identici** e 3 `DESCRIPTION` che differiscono **solo per lo scopo**. Controlli propri:
**`<martini relief occupations>`** (segnaposto composto, 3 volte), **12 token su 4 simboli**, e la variante di scopo
verificata in positivo **e** in negativo. L'apostrofo di `Martini's` (idx 4) **non** si propaga in italiano.
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


TOK = {'<bunks>': 3, '<martini relief occupations>': 3, '<planet>': 3, '<payment>': 3}
ck("unita' tradotte 6/6", len(cov) == 6 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 3 VALUE + 3 DESCRIPTION', collections.Counter(u['kind'] for u in units)
   == {'VALUE': 3, 'DESCRIPTION': 3})
ck('UN asserzione vuota: ZERO UI_LABEL', [u['idx'] for u in units if u['kind'] == 'UI_LABEL'] == [])
ck('12 token su 4 simboli, stesso multiset in italiano',
   dict(collections.Counter(t for u in units for t in TAGS.findall(u['english']))) == TOK
   == dict(collections.Counter(t for v in cov for t in TAGS.findall(v['italian'])))
   and sum(TOK.values()) == 12 and len(TOK) == 4)
ck('parita per UNITA: stesso ordine di simboli in tutte le 6',
   not [v['idx'] for v in cov if TAGS.findall(v['italian']) != TAGS.findall(v['english'])])
ck('`<martini relief occupations>` intero 3 volte, mai spezzato',
   [v['idx'] for v in cov if '<martini relief occupations>' in v['english']] == [2, 4, 6]
   == [v['idx'] for v in cov if '<martini relief occupations>' in v['italian']]
   and not [v['idx'] for v in cov if re.search(r'<martini>\s+relief', v['italian'])]
   and all('relief' not in TAGS.sub('', v['italian']) for v in cov))
ck('3 VALUE identici al sorgente, e sono lo stesso testo',
   by[1]['english'] == by[3]['english'] == by[5]['english'] == 'Relief workers to Martini'
   and by[1]['italian'] == by[3]['italian'] == by[5]['italian']
   and [v['idx'] for v in cov if v['kind'] == 'VALUE' and v['italian'] != v['english']] == [])
ck('6 unita, 4 testi inglesi distinti (1 VALUE + 3 DESCRIPTION)', len({v['english'] for v in cov}) == 4,
   len({v['english'] for v in cov}))
ck('le tre DESCRIPTION differiscono SOLO per lo scopo (verifica positiva)',
   'alleggerire la pressione sugli ospedali sovraccarichi' in by[2]['italian']
   and 'sforzi di soccorso di Martini' in by[4]['italian']
   and 'sforzi di accoglienza e ricostruzione' in by[6]['italian'])
ck('e in negativo: nessuno scopo compare nel testo sbagliato',
   'ospedali' not in by[4]['italian'] and 'ospedali' not in by[6]['italian']
   and 'soccorso' not in by[6]['italian'] and 'accoglienza' not in by[2]['italian'])
ck('rimuovendo lo scopo, le tre DESCRIPTION diventano UNA sola stringa',
   len({re.sub(r' per (alleggerire|dare man forte).*?\. Dovrai', ' per SCOPO. Dovrai', v['italian'])
        for v in cov if v['kind'] == 'DESCRIPTION'}) == 1)
ck('l apostrofo di Martini\'s (idx 4) NON si propaga: 1 in inglese, 0 in italiano',
   sum(v['english'].count("'") for v in cov) == 1 == by[4]['english'].count("'")
   and sum(v['italian'].count("'") for v in cov) == 0)
ck('ZERO tab e ZERO virgolette (asserzioni vuote scritte)',
   [v['idx'] for v in cov if '\t' in v['english'] or '\t' in v['italian']] == []
   and sum(v['english'].count('"') for v in cov) == 0 == sum(v['italian'].count('"') for v in cov))
ck('3 contesti distinti', len({u['context'] for u in units}) == 3)
ck('prima e ultima unita: righe 1356 e 1413 (fine file)',
   (cov[0]['line'], cov[-1]['line']) == (1356, 1413)
   and cov[0]['context'] == 'mission:Martini Relief (People) [0]'
   and cov[-1]['context'] == 'mission:Martini Relief (People) [2]')
ck('zero spazi iniziali e finali identici al sorgente (6/6)',
   not [v['idx'] for v in cov
        if len(v['italian']) - len(v['italian'].rstrip()) != len(v['english']) - len(v['english'].rstrip())
        or len(v['italian']) - len(v['italian'].lstrip()) != len(v['english']) - len(v['english'].lstrip())])
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' you ', ' to the ', ' will be ',
        ' is ', ' are ', ' from the ', ' due to ', ' in the ')
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
ck('tutte le 6 unita sono PENDING nel database (misurato)',
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
