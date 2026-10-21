r"""check.py — L154 (`data/coalition/coalition jobs.txt`, 41 unita', righe 1475-1807).

Lotto che **chiude il file**. Controlli propri: le 9 famiglie `Lunarium: X Delivery` (regolarita' delle forme, non solo
dei totali); le due `Rescue Lunarium Members` (VALUE identiche, descrizioni diverse per l'articolo); assenza incrociata
`<destination>` / `<planet>`; **0 tab** e **0 virgolette** (asserzioni vuote scritte); **57 token su 7 simboli**.
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
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


# le 9 famiglie Lunarium: idx VALUE, idx DESCRIPTION, idx DIALOG, nome dell'oggetto
FAM = [
    ('Armageddon Core', 17), ('Fusion Reactor', 20), ('Breeder Reactor', 23), ('Torpedo Launcher', 26),
    ('Typhoon Launcher', 29), ('Plasma Turret', 32), ('Flamethrowers', 35),
    ('Fragmentation Grenades', 38), ('Heavy Anti-Missile Turret', 41),
]
TAIL = {17: 'il reattore', 20: 'il reattore', 23: 'il reattore', 26: 'il carico', 29: 'il carico',
        32: 'la torretta', 35: 'i Flamethrowers', 38: 'le granate', 41: 'la torretta'}

ck("unita' tradotte 41/41", len(cov) == 41 == len(units) and not missing, '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 13 VALUE + 13 DESCRIPTION + 15 DIALOG',
   collections.Counter(u['kind'] for u in units) == {'VALUE': 13, 'DESCRIPTION': 13, 'DIALOG': 15})
ck('UN asserzione vuota: ZERO UI_LABEL', [u['idx'] for u in units if u['kind'] == 'UI_LABEL'] == [])
TOK = {'<payment>': 23, '<destination>': 14, '<planet>': 9, '<bunks>': 4, '<stopovers>': 3,
       '<origin>': 2, '<date>': 2}
ck('57 token su 7 simboli, stesso multiset in italiano',
   dict(collections.Counter(t for u in units for t in TAGS.findall(u['english']))) == TOK
   == dict(collections.Counter(t for v in cov for t in TAGS.findall(v['italian'])))
   and sum(TOK.values()) == 57 and len(TOK) == 7)
ck('parita per UNITA: stesso ordine di simboli in tutte le 41',
   not [v['idx'] for v in cov if TAGS.findall(v['italian']) != TAGS.findall(v['english'])],
   [(v['idx'], TAGS.findall(v['english']), TAGS.findall(v['italian']))
    for v in cov if TAGS.findall(v['italian']) != TAGS.findall(v['english'])])
ck('13 VALUE identici al sorgente, uno per uno',
   len(VAL) == 13 and all(by[i]['italian'].rstrip() == by[i]['english'].rstrip() for i in VAL),
   [(i, by[i]['italian']) for i in VAL if by[i]['italian'].rstrip() != by[i]['english'].rstrip()])
ck('le 28 unita di testo sono tradotte (VALUE a parte)',
   not [v['idx'] for v in cov if v['kind'] != 'VALUE' and v['italian'].strip() == v['english'].strip()])
ck('ZERO tab nel sorgente e in traduzione (asserzione vuota scritta)',
   [v['idx'] for v in cov if '\t' in v['english']] == [] == [v['idx'] for v in cov if '\t' in v['italian']])
ck('ZERO virgolette nel sorgente e in traduzione (asserzione vuota scritta)',
   sum(v['english'].count('"') for v in cov) == 0 == sum(v['italian'].count('"') for v in cov))
PLANET = [v['idx'] for v in cov if '<planet>' in v['english']]
ck('9 unita con <planet>: sono esattamente i 9 DIALOG di consegna',
   PLANET == [17, 20, 23, 26, 29, 32, 35, 38, 41]
   and all(by[i]['kind'] == 'DIALOG' for i in PLANET), PLANET)
ck('assenza incrociata: nessuna unita con <planet> ha <destination> e viceversa',
   not [v['idx'] for v in cov if ('<planet>' in v['english']) == ('<destination>' in v['english'])
        and ('<planet>' in v['english'] or '<destination>' in v['english'])])
ck('le due VALUE Rescue Lunarium Members sono identiche anche in italiano',
   by[8]['english'] == by[12]['english'] and by[8]['italian'] == by[12]['italian'])
ck('le due DESCRIPTION Evacuate differiscono per l articolo (9 senza, 13 con)',
   by[9]['english'] != by[13]['english'] and by[9]['italian'] != by[13]['italian']
   and by[13]['italian'].startswith('Preleva i <bunks>') and not by[9]['italian'].startswith('Preleva i '))
ck('le 9 DIALOG di consegna condividono le tre giunture fisse',
   not [i for _, i in FAM
        if 'Alcuni membri del Lunarium scaricano ' not in by[i]['italian']
        or 'dopo che atterri su una parte isolata di <planet>, come richiesto' not in by[i]['italian']
        or 'Ti consegnano <payment> prima di portare via ' not in by[i]['italian']])
ck('le 9 DIALOG nominano ciascuna il proprio oggetto e la propria coda',
   not [i for name, i in FAM if name not in by[i]['italian']
        or not by[i]['italian'].rstrip().endswith(TAIL[i] + ' in silenzio.')])
ck('le 7 DESCRIPTION semplici nominano il proprio oggetto e offrono <payment> per <destination>',
   not [i for name, i in FAM[:3] + FAM[5:]
        if (' %s a <destination>.' % name) not in by[i - 1]['italian']
        or not by[i - 1]['italian'].startswith('Il Lunarium offre <payment> per consegnare ')])
ck('le 2 DESCRIPTION con "complete with" sono Torpedo e Typhoon (idx 25, 28)',
   [v['idx'] for v in cov if 'completo di' in v['italian']] == [25, 28]
   and '30 siluri' in by[25]['italian'] and '30 Typhoon Torpedoes' in by[28]['italian']
   and [v['idx'] for v in cov if 'complete with' in v['english']] == [25, 28])
ck('40 stringhe distinte su 41 unita', len({(v['kind'], v['english']) for v in cov}) == 40)
ck('zero spazi iniziali e finali identici al sorgente (41/41)',
   not [v['idx'] for v in cov
        if len(v['italian']) - len(v['italian'].rstrip()) != len(v['english']) - len(v['english'].rstrip())]
   and not [v['idx'] for v in cov
            if len(v['italian']) - len(v['italian'].lstrip()) != len(v['english']) - len(v['english'].lstrip())])
ck('prima e ultima unita: righe 1475 e 1807', (cov[0]['line'], cov[-1]['line']) == (1475, 1807),
   (cov[0]['line'], cov[-1]['line']))
LOW = ' '.join(v['italian'] for v in cov).lower()
ck('terminologia presente: 7 termini chiave',
   all(t in LOW for t in ('lunarium', 'heliarch', 'reattore', 'torretta', 'granate', 'carico', 'criminali')))
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' you ', ' to the ', ' will be ')
LONG = ' '.join(TAGS.sub('""', v['italian']) for v in cov if v['kind'] != 'VALUE').lower()
for s in ('lunarium', 'heliarch', 'armageddon core', 'fusion reactor', 'breeder reactor', 'torpedo launcher',
          'typhoon launcher', 'typhoon torpedoes', 'plasma turret', 'flamethrowers', 'fragmentation grenades',
          'heavy anti-missile turret'):
    LONG = LONG.replace(s, '@@')
ck('nessun residuo inglese fuori dai nomi propri e dai VALUE',
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
ck('tutte le 41 unita sono PENDING nel database (misurato)',
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
