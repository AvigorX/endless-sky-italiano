r"""check.py — L168 (`data/human/paradise world jobs.txt`, 24 unita', righe 225-372).

Secondo lotto del file. Controlli propri: **55 token su 11 simboli**, compreso **`<planet stopovers>`**, un segnaposto
**unico** che contiene una frase: se venisse spezzato in `<planet>` + ` stopovers` il multiset cambierebbe e il controllo
lo vede. Piu' **7 `VALUE`** alla lettera, una sequenza di tre `DESCRIPTION` che differiscono per una sola frase e una
coppia di `DIALOG` che si somigliano (qualita' degli abiti / salute / elettronica).
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


TOK = {'<payment>': 14, '<commodity>': 9, '<planet>': 8, '<destination>': 6, '<origin>': 5, '<cargo>': 5,
       '<stopovers>': 3, '<planet stopovers>': 2, '<tons>': 1, '<date>': 1, '<bunks>': 1}
ck("unita' tradotte 24/24", len(cov) == 24 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 7 VALUE + 7 DESCRIPTION + 10 DIALOG',
   collections.Counter(u['kind'] for u in units) == {'VALUE': 7, 'DESCRIPTION': 7, 'DIALOG': 10})
ck('UN asserzione vuota: ZERO UI_LABEL', [u['idx'] for u in units if u['kind'] == 'UI_LABEL'] == [])
ck('55 token su 11 simboli, stesso multiset in italiano',
   dict(collections.Counter(t for u in units for t in TAGS.findall(u['english']))) == TOK
   == dict(collections.Counter(t for v in cov for t in TAGS.findall(v['italian'])))
   and sum(TOK.values()) == 55 and len(TOK) == 11)
ck('parita per UNITA: stesso ordine di simboli in tutte le 24',
   not [v['idx'] for v in cov if TAGS.findall(v['italian']) != TAGS.findall(v['english'])],
   [(v['idx'], TAGS.findall(v['english']), TAGS.findall(v['italian']))
    for v in cov if TAGS.findall(v['italian']) != TAGS.findall(v['english'])])
ck('`<planet stopovers>` resta UN segnaposto: 2 occorrenze, nessuna spezzata',
   sum(v['english'].count('<planet stopovers>') for v in cov) == 2
   == sum(v['italian'].count('<planet stopovers>') for v in cov)
   and sum(v['english'].count('<planet stopovers>') for v in cov) == sum(
       t == '<planet stopovers>' for v in cov for t in TAGS.findall(v['english']))
   and sum(v['italian'].count('<planet stopovers>') for v in cov) == sum(
       t == '<planet stopovers>' for v in cov for t in TAGS.findall(v['italian']))
   and not [v['idx'] for v in cov if re.search(r'<planet>\s+stopovers', v['italian'])])
ck('7 VALUE identici al sorgente, uno per uno',
   [v['idx'] for v in cov if v['kind'] == 'VALUE' and v['italian'].rstrip() != v['english'].rstrip()] == []
   and len([v for v in cov if v['kind'] == 'VALUE']) == 7)
ck('le tre DESCRIPTION 2/5/8 differiscono solo per le anime (malvestite / sofferenti / ingenue)',
   'malvestite' in by[2]['italian'] and 'sofferenti' in by[5]['italian'] and 'ingenue' in by[8]['italian']
   and 'malvestite' not in by[5]['italian'] and 'sofferenti' not in by[8]['italian']
   and by[2]['italian'].replace('malvestite e prive di stile', '') ==
   by[5]['italian'].replace('sofferenti', ''))
ck('i tre DIALOG 3/6/9 differiscono solo per cosa si nota (abiti / salute / elettronica)',
   'qualità degli abiti indossati' in by[3]['italian'] and 'salute e il vigore' in by[6]['italian']
   and 'elettronica personale' in by[9]['italian'])
ck('idx 11 (Party Goods) ha 6 token nell ordine giusto',
   TAGS.findall(by[11]['english']) == ['<commodity>', '<tons>', '<stopovers>', '<origin>', '<date>', '<payment>']
   == TAGS.findall(by[11]['italian']))
ck('idx 13: planet + commodity + stopovers (l ordine non si inverte)',
   TAGS.findall(by[13]['italian']) == ['<planet>', '<commodity>', '<stopovers>'])
ck('idx 19: destination + bunks + stopovers + payment',
   TAGS.findall(by[19]['italian']) == ['<destination>', '<bunks>', '<stopovers>', '<payment>'])
ck('ZERO tab e ZERO virgolette (asserzioni vuote scritte)',
   [v['idx'] for v in cov if '\t' in v['english'] or '\t' in v['italian']] == []
   and sum(v['english'].count('"') for v in cov) == 0 == sum(v['italian'].count('"') for v in cov))
ck('7 contesti distinti, 24 testi inglesi distinti',
   len({u['context'] for u in units}) == 7 and len({v['english'] for v in cov}) == 24)
ck('prima e ultima unita: righe 225 e 372',
   (cov[0]['line'], cov[-1]['line']) == (225, 372)
   and cov[0]['context'] == 'mission:Paradise Job: Clothing Donations'
   and cov[-1]['context'] == 'mission:Paradise Job: Waste Disposal')
ck('zero spazi iniziali e finali identici al sorgente (24/24)',
   not [v['idx'] for v in cov
        if len(v['italian']) - len(v['italian'].rstrip()) != len(v['english']) - len(v['english'].rstrip())
        or len(v['italian']) - len(v['italian'].lstrip()) != len(v['english']) - len(v['english'].lstrip())])
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' you ', ' to the ', ' will be ',
        ' is ', ' are ', ' from the ', ' their ')
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
ck('tutte le 24 unita sono PENDING nel database (misurato)',
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
