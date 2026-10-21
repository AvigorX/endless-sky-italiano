r"""check.py — L196 (`data/hai/hai jobs.txt`, 39 unita', righe 15-489). **APRE IL FILE.**

Primo lotto del file: non una missione ma **20 missioni** (vacanze, famiglie benestanti, festival Hai,
aiuti agli Unfettered, consegne nello spazio umano). Registro: **listino di lavori**, non narrazione.

Convenzioni misurate sul workspace, non dedotte:
- **17 `VALUE` copiati alla lettera**: nei lotti L117…L195 i `VALUE` sono **300+ su 300+ identici**
  all'inglese; i `VALUE` tradotti si fermano ai lotti L16–L18. Il nome del lavoro resta inglese,
  parentesi quadre comprese.
- **6 `TEXT` tradotti**: i `TEXT` in prosa (`phrase:`) sono tradotti da L108 a L152; restano inglesi solo
  i nomi di armi/outfit sotto contesti `ship:` (L139, L176-L178). Qui sono tre battute di dialogo.
- **72 segnaposto** su 32 unita': ogni unita' conserva lo **stesso multiset** di `<...>`.
- **0 tab** · **6 virgolette** (tutte nei `TEXT` citati) · **1 apice** inglese (`didn't`) contro **3**
  italiani (`all'anno`): l'apice non si conserva, si spiega.
"""
import collections
import json
import os
import re
import sqlite3

TAB = chr(9)
QUOTE = chr(34)
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
NON_VALUE = ' '.join(v['italian'] for v in cov if v['kind'] != 'VALUE')
IT_ALL = ' '.join(v['italian'] for v in cov)
EN_Q = sum(v['english'].count(QUOTE) for v in cov)
IT_Q = sum(v['italian'].count(QUOTE) for v in cov)
KINDS = collections.Counter(u['kind'] for u in units)
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 39/39", len(cov) == 39 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 17 VALUE, 16 DESCRIPTION, 6 TEXT (asserzione scritta)',
   KINDS == {'VALUE': 17, 'DESCRIPTION': 16, 'TEXT': 6}, dict(KINDS))
ck('ZERO UI_LABEL e ZERO tab (asserzioni vuote scritte)',
   [u['idx'] for u in units if u['kind'] == 'UI_LABEL'] == []
   and [u['idx'] for u in units if u['english'].startswith(TAB)] == []
   and [v['idx'] for v in cov if v['italian'].startswith(TAB)] == [])
ctx = [u['context'].replace('mission:', '') for u in units]
ck('20 contesti distinti, da Human Vacation [1] a Delivery to Human Space [2]',
   len(set(ctx)) == 20 and (ctx[0], ctx[-1]) == ('Human Vacation [1]', 'Delivery to Human Space [2]'),
   '%d · %s · %s' % (len(set(ctx)), ctx[0], ctx[-1]))
ck('righe 15 e 489 (prima e ultima del lotto)',
   (cov[0]['line'], cov[-1]['line']) == (15, 489), (cov[0]['line'], cov[-1]['line']))
EN_T = collections.Counter(t for u in units for t in TAGS.findall(u['english']))
IT_T = collections.Counter(t for v in cov for t in TAGS.findall(v['italian']))
ck('72 segnaposto, stesso multiset in inglese e italiano',
   sum(EN_T.values()) == 72 and EN_T == IT_T, dict(EN_T))
bad_tags = [(v['idx'], sorted(TAGS.findall(v['english'])), sorted(TAGS.findall(v['italian'])))
            for v in cov
            if collections.Counter(TAGS.findall(v['english'])) != collections.Counter(TAGS.findall(v['italian']))]
ck('nessuna unita\' perde, duplica o sposta un segnaposto', not bad_tags, bad_tags)
ck('17 VALUE identici all\'inglese, uno per uno',
   [v['idx'] for v in cov if v['kind'] == 'VALUE'] == [1, 3, 5, 7, 9, 11, 13, 15, 18, 20, 22, 29, 31, 33, 35, 37, 39]
   and all(v['italian'] == v['english'] for v in cov if v['kind'] == 'VALUE'))
ck('6 TEXT tradotti (nessuno lasciato in inglese)',
   [v['idx'] for v in cov if v['kind'] == 'TEXT'] == [17, 24, 25, 26, 27, 28]
   and all(v['italian'] != v['english'] for v in cov if v['kind'] == 'TEXT'))
ck('6 virgolette in entrambe le lingue, tutte nei TEXT citati',
   EN_Q == 6 == IT_Q
   and [v['idx'] for v in cov if QUOTE in v['english']] == [24, 27, 28]
   and [v['idx'] for v in cov if QUOTE in v['italian']] == [24, 27, 28], (EN_Q, IT_Q))
ck("apici: 1 inglese (didn't, idx 17) e 3 italiani (all'anno, idx 19-21-23), causa misurata",
   sum(v['english'].count(chr(39)) for v in cov) == 1
   and [v['idx'] for v in cov if chr(39) in v['english']] == [17]
   and [v['idx'] for v in cov if chr(39) in v['italian']] == [19, 21, 23],
   (sum(v['english'].count(chr(39)) for v in cov), sum(v['italian'].count(chr(39)) for v in cov)))
ck('nessun caporale e nessun carattere tipografico',
   not [v['idx'] for v in cov if any(c in v['italian'] for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026')])
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' you ', ' to the ', ' will be ',
        ' is ', ' are ', ' from the ', ' its ', ' it is ', ' such as ', ' rather than ', ' for a ')
ck('nessun residuo inglese fuori dai VALUE (che restano inglesi per convenzione)',
   not [w for w in ENGW if w in NON_VALUE.lower()], [w for w in ENGW if w in NON_VALUE.lower()])
CORT = re.findall(r'\bLei\b|(?<![.!?] )\b(?:Suo|Sua|Suoi|Sue)\b', IT_ALL)
ck('nessuna forma di cortesia «Lei»', not CORT, CORT)
rs = [v['ratio'] for v in cov]
ck('rapporto nel gate 0,55-1,90', 0.55 < min(rs) and max(rs) < 1.90, '%.2f - %.2f' % (min(rs), max(rs)))
ACC = re.compile(r"\b(e|piu|perche|cosi|gia|puo|cioe|percio|fa)'", re.I)
bad = [(v['idx'], ACC.search(v['italian']).group(0)) for v in cov if ACC.search(v['italian'])]
ck('tipografia (accenti veri, nessun apostrofo al posto dell\'accento)', not bad, bad)
nonlat = [v['idx'] for v in cov for c in v['italian'] if ord(c) > 127 and not 0x00C0 <= ord(c) <= 0x024F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio',
   not [v['idx'] for v in cov if v['italian'] != v['italian'].rstrip()
        or '  ' in v['italian'] or v['english'] != v['english'].rstrip()])
ck('famiglia Hai Vacation [2]/[3]/[4]: 8, 10 e 12 identici fra loro',
   by[8]['italian'] == by[10]['italian'] == by[12]['italian'])
ck('famiglia Festival: 19, 21 e 23 stessa cornice, soggetto diverso (Hai / umani / Hai e umani)',
   len({by[i]['italian'].split('Questo gruppo di ')[1].split(' ti pagherà')[0] for i in (19, 21, 23)}) == 3
   and len({by[i]['italian'].split(' ti pagherà')[1] for i in (19, 21, 23)}) == 1
   and by[19]['italian'].split('Questo gruppo di ')[1].startswith('<bunks> Hai ')
   and by[21]['italian'].split('Questo gruppo di ')[1].startswith('<bunks> umani ')
   and by[23]['italian'].split('Questo gruppo di ')[1].startswith('<bunks> Hai e umani '))
ck('famiglia Unfettered Aid: 30, 32 e 34 identici fra loro',
   by[30]['italian'] == by[32]['italian'] == by[34]['italian'])
ck('Delivery [0]/[1]: 36 e 38 differiscono solo nel soggetto (umano / Hai)',
   by[36]['italian'].replace('Questo umano', 'X') == by[38]['italian'].replace('Questo Hai', 'X'))
ck('il nome del lavoro resta inglese: "Special Delivery to <planet>" (35, 37, 39)',
   all(by[i]['italian'] == 'Special Delivery to <planet>' for i in (35, 37, 39)))
c = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
st = dict(c.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('tutte le 39 unita sono PENDING (misurato)',
   c.execute('select count(*) from units where id in (%s) and state != "PENDING"'
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
