r"""check.py — L160 (`data/human/weapons.txt`, 13 unita', righe 1640-1844). **Chiude il file.**

Controlli propri: **2 VALUE** (`Gatling Gun Ammo`, `Bullet Boxes`); **5 unita' con tab**; l'**ellissi `...`** di idx 4 resta
tre punti ASCII (mai `…`); il **trattino ` - `** di idx 10 resta un trattino semplice (mai em/en dash); idx 1 e' la stessa
stringa di L159 (idx 21) e idx 3/11/13 la riga munizioni di L157/L158/L159: si verificano contro i lotti precedenti.
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
missing = [u['idx'] for u in units if u['idx'] not in tr]
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
VAL = [v['idx'] for v in cov if v['kind'] == 'VALUE']
EARLIER = {}
for f in sorted(os.listdir(os.path.join(L10N, 'staging/editorial'))):
    p = os.path.join(L10N, 'staging/editorial', f, 'translation.json')
    if f.startswith('L160') or not os.path.exists(p):
        continue
    for u in json.load(open(p, encoding='utf-8'))['units']:
        if u['path'] == 'data/human/weapons.txt':
            EARLIER[u['english']] = u['italian']
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


NAMES = ['Heavy Rocket', 'Gatling Gun Ammo', 'Gatling Gun', 'Gatling Turret', 'Bullet Boxes', 'Energy Blaster',
         'Blaster Turret']
ck("unita' tradotte 13/13", len(cov) == 13 == len(units) and not missing, '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 11 DESCRIPTION + 2 VALUE', collections.Counter(u['kind'] for u in units)
   == {'DESCRIPTION': 11, 'VALUE': 2})
ck('UN asserzione vuota: ZERO UI_LABEL', [u['idx'] for u in units if u['kind'] == 'UI_LABEL'] == [])
ck('ZERO token nel sorgente e in traduzione (asserzione vuota scritta)',
   [v['idx'] for v in cov if TAGS.findall(v['english'])] == [] == [v['idx'] for v in cov if TAGS.findall(v['italian'])])
ck('2 VALUE identici al sorgente, uno per uno',
   len(VAL) == 2 and all(by[i]['italian'].rstrip() == by[i]['english'].rstrip() for i in VAL),
   [(i, by[i]['italian']) for i in VAL])
ck('5 unita con tab iniziale: idx 2,3,5,11,13, le stesse in traduzione',
   [v['idx'] for v in cov if v['english'].startswith('\t')] == [2, 3, 5, 11, 13]
   == [v['idx'] for v in cov if v['italian'].startswith('\t')])
ck('ZERO virgolette (asserzione vuota scritta)',
   sum(v['english'].count('"') for v in cov) == 0 == sum(v['italian'].count('"') for v in cov))
ck('l ellissi di idx 4 resta tre punti ASCII, mai U+2026',
   by[4]['english'].endswith('...') and by[4]['italian'].endswith('...')
   and '\u2026' not in by[4]['italian'] and by[4]['italian'].count('...') == 1)
ck('il trattino di idx 10 resta un trattino semplice, mai em/en dash',
   ' - ' in by[10]['italian'] and not any(c in by[10]['italian'] for c in '\u2014\u2013'))
ck('le note tra parentesi quadre restano tra parentesi quadre (idx 5)',
   by[5]['english'].lstrip('\t').startswith('[') and by[5]['english'].rstrip().endswith(']')
   and by[5]['italian'].lstrip('\t').startswith('[') and by[5]['italian'].rstrip().endswith(']'))
ck('la riga munizioni (3/11/13) riusa la resa di L157/L158/L159',
   len({by[i]['italian'] for i in (3, 11, 13)}) == 1
   and EARLIER.get(by[3]['english']) == by[3]['italian'],
   (EARLIER.get(by[3]['english']), by[3]['italian']))
ck('idx 1 riusa la resa di L159 per la stessa stringa',
   EARLIER.get(by[1]['english']) == by[1]['italian'],
   (EARLIER.get(by[1]['english']), by[1]['italian']))
ck('13 unita, 11 testi inglesi distinti', len({v['english'] for v in cov}) == 11,
   len({v['english'] for v in cov}))
ck('ogni nome proprio dell inglese resta nell italiano (unita per unita)',
   not [v['idx'] for v in cov for n in NAMES if n in v['english'] and n not in v['italian']],
   [(v['idx'], n) for v in cov for n in NAMES if n in v['english'] and n not in v['italian']])
ck('nessun nome proprio inventato in italiano (insieme uguale)',
   {(v['idx'], n) for v in cov for n in NAMES if n in v['english']}
   == {(v['idx'], n) for v in cov for n in NAMES if n in v['italian']})
ck('Southern Rim reso «Bordo Meridionale», come nei lotti precedenti',
   'Bordo Meridionale' in by[12]['italian'] and 'Southern Rim' in by[12]['english'])
ck('glossario: munizioni, emporio, scafi, cannone, caccia',
   all(t in ' '.join(v['italian'].lower() for v in cov)
       for t in ('munizion', 'emporio', 'scafi', 'cannon', 'caccia')))
ck('prima e ultima unita: righe 1640 e 1844, ultima del file',
   (cov[0]['line'], cov[-1]['line']) == (1640, 1844)
   and cov[0]['context'] == 'outfit:Heavy Rocket Pod' and cov[-1]['context'] == 'outfit:Gatling Turret',
   (cov[0]['line'], cov[-1]['line']))
ck('zero spazi iniziali e finali identici al sorgente (13/13)',
   not [v['idx'] for v in cov
        if len(v['italian']) - len(v['italian'].rstrip()) != len(v['english']) - len(v['english'].rstrip())
        or len(v['italian']) - len(v['italian'].lstrip()) != len(v['english']) - len(v['english'].lstrip())])
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' you ', ' to the ', ' will be ',
        ' is ', ' are ', ' from the ')
LONG = ' '.join(TAGS.sub('""', v['italian']) for v in cov).lower()
for s in NAMES:
    LONG = LONG.replace(s.lower(), '@@')
ck('nessun residuo inglese fuori dai nomi propri',
   not [w for w in ENGW if w in LONG], [w for w in ENGW if w in LONG])
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
      len(parts), len(missing)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
