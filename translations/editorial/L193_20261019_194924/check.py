r"""check.py — L193 (`data/bunrodea/bunrodea missions.txt`, 30 unita', righe 92-150).

Terzo lotto: l'incontro con l'interprete, la scala del palazzo, la sala del trono e l'interrogatorio della Regina.
**30 `MISSION_TEXT`**, **30 tab**, **60 virgolette** (30 coppie di dialogo), zero `VALUE`, zero token. Controlli propri:
le tre battute ripetute nella seconda serie (idx 23=27, 24=28, 25=29) devono avere la **stessa resa**, e la parola
`Megasa` resta invariata (nome di specie, non descrittore).
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
IT_ALL = ' '.join(v['italian'] for v in cov)
EN_Q = sum(v['english'].count(QUOTE) for v in cov)
IT_Q = sum(v['italian'].count(QUOTE) for v in cov)
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 30/30", len(cov) == 30 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 30 MISSION_TEXT, ZERO VALUE (asserzione scritta)',
   collections.Counter(u['kind'] for u in units) == {'MISSION_TEXT': 30})
ck('ZERO UI_LABEL e ZERO token (asserzioni vuote scritte)',
   [u['idx'] for u in units if u['kind'] == 'UI_LABEL'] == []
   and {t for u in units for t in TAGS.findall(u['english'])} == set())
ck('30 tab iniziali, uno per unita', [v['idx'] for v in cov if v['english'].startswith(TAB)]
   == list(range(1, 31)) == [v['idx'] for v in cov if v['italian'].startswith(TAB)])
ck('60 virgolette (30 coppie) in inglese e in italiano',
   EN_Q == 60 == IT_Q, (EN_Q, IT_Q))
ck('ogni unita ha un numero PARI di virgolette (coppie chiuse)',
   not [v['idx'] for v in cov if v['english'].count(QUOTE) % 2 or v['italian'].count(QUOTE) % 2])
ck('nessun caporale e nessuna virgoletta tipografica in italiano',
   not [v['idx'] for v in cov if any(c in v['italian'] for c in '\u00ab\u00bb\u201c\u201d')])
ck('le tre battute ripetute hanno la STESSA resa (idx 23=27, 24=28, 25=29)',
   by[23]['italian'] == by[27]['italian'] and by[24]['italian'] == by[28]['italian']
   and by[25]['italian'] == by[29]['italian'])
ck('`Megasa` resta invariato (idx 21)', 'Megasa' in by[21]['italian'])
ck('la creatura parla piu\' lingue e dice «Salve» (idx 1 e 4)',
   'varie lingue diverse' in by[1]['italian'] and 'Salve' in by[1]['italian']
   and by[4]['italian'].count('Salve') == 4)
ck("idx 13 dice «Umano» cinque volte (come in inglese) e cita i cento anni",
   by[13]['italian'].count('Umano') == by[13]['english'].count('Human') == 5
   and 'Cento... anni fa' in by[13]['italian'])
ck('la Regina e\' della stessa specie delle guardie ma piu\' grande (idx 19)',
   'simile alle mantidi' in by[19]['italian'] and 'più grande' in by[19]['italian'])
ck('30 unita, 27 testi inglesi distinti (tre ripetizioni)', len({v['english'] for v in cov}) == 27,
   len({v['english'] for v in cov}))
ck('un solo contesto, righe 92 e 150', len({u['context'] for u in units}) == 1
   and (cov[0]['line'], cov[-1]['line']) == (92, 150))
ck('nessuno spazio finale (tab iniziali ammessi)',
   not [v['idx'] for v in cov if v['english'].rstrip(TAB) != v['english'].rstrip(TAB).rstrip()
        or v['italian'].rstrip(TAB) != v['italian'].rstrip(TAB).rstrip()])
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' you ', ' to the ', ' will be ',
        ' is ', ' are ', ' from the ', ' its ', ' it is ', ' such as ', ' rather than ')
ck('nessun residuo inglese', not [w for w in ENGW if w in IT_ALL.lower()],
   [w for w in ENGW if w in IT_ALL.lower()])
CORT = re.findall(r'\bLei\b|(?<![.!?] )\b(?:Suo|Sua|Suoi|Sue)\b', IT_ALL)
ck('nessuna forma di cortesia «Lei»', not CORT, CORT)
rs = [v['ratio'] for v in cov]
ck('rapporto nel gate 0,55-1,90', 0.55 < min(rs) and max(rs) < 1.90, '%.2f - %.2f' % (min(rs), max(rs)))
bad = [(v['idx'], n) for v in cov for p, n in ((r"\b(e|piu|perche|cosi|gia|puo|cioe|percio|fa)'", 'accento'),
       ('\u2026', 'ellissi'), ('\u2014', 'em dash'), ('\u2013', 'en dash'), ('\u2019', 'apostrofo curvo')) if re.search(p, v['italian'])]
ck('tipografia (accenti veri, nessun carattere tipografico)', not bad, bad)
nonlat = [v['idx'] for v in cov for c in v['italian'] if ord(c) > 127 and not 0x00C0 <= ord(c) <= 0x024F]
ck('caratteri non latini', not nonlat, nonlat)
c = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
st = dict(c.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('tutte le 30 unita sono PENDING (misurato)',
   c.execute('select count(*) from units where id in (%s) and state != "PENDING"'
             % ','.join('?' * len(units)), [u['id'] for u in units]).fetchone()[0] == 0)
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d' % (sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('righe %d/%d · parti %d · mancanti %d' % (min(u['line'] for u in units), max(u['line'] for u in units),
      len(parts), len([u for u in units if u['idx'] not in tr])))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
