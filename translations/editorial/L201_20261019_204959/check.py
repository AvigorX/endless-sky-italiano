r"""check.py — L201 (`data/hai/hai outfits.txt`, 8 unita', righe 27-164). **APRE IL FILE.**

Descrizioni di equipaggiamento, non lavori: **8 `DESCRIPTION`**, nessun `VALUE`, nessun `DIALOG`, nessun `TEXT`.
**Zero segnaposto** in tutto il file — e' un'asserzione negativa e va scritta. **2 tab** (unita' 3 e 4) e **2
virgolette** (unita' 1, intorno a `"holopads"`). **Zero apici inglesi** contro **5 italiani**, tutti da elisione
(`l'arma`, `l'alloggiamento`, `un'arma`, `l'energia`, `l'effetto`): il numero non torna perche' non deve tornare.

**Nomi di prodotto invariati**: `Phantom Pallet`, `Holovid Zone`, `Pulse Cannon`, `Pulse Turret`, `Tripulse Shredder`,
`Ion Cannon`, `Deathsticks`, `Unfettered`, `Wanderer`. **`holopad` -> `olopad`** e' la resa gia' presente in staging.
"""
import collections
import json
import os
import re
import sqlite3

TAB = chr(9)
QUOTE = chr(34)
APOS = chr(39)
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
EN_T = sum(len(TAGS.findall(v['english'])) for v in cov)
IT_T = sum(len(TAGS.findall(v['italian'])) for v in cov)
EN_Q = sum(v['english'].count(QUOTE) for v in cov)
IT_Q = sum(v['italian'].count(QUOTE) for v in cov)
EN_A = sum(v['english'].count(APOS) for v in cov)
IT_A = sum(v['italian'].count(APOS) for v in cov)
KINDS = collections.Counter(u['kind'] for u in units)
NAMES = ('Phantom Pallet', 'Holovid Zone', 'Pulse Cannon', 'Pulse Turret', 'Tripulse Shredder',
         'Ion Cannon', 'Deathsticks', 'Unfettered', 'Wanderer')
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 8/8", len(cov) == 8 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 8 DESCRIPTION (asserzione scritta)', KINDS == {'DESCRIPTION': 8}, dict(KINDS))
ck('ZERO VALUE, TEXT, DIALOG, UI_LABEL (asserzioni vuote scritte)',
   [u['idx'] for u in units if u['kind'] != 'DESCRIPTION'] == [])
ctx = [u['context'].replace('outfit:', '') for u in units]
ck('6 contesti distinti, da Phantom Pallet a Ion Cannon',
   len(set(ctx)) == 6 and (ctx[0], ctx[-1]) == ('Phantom Pallet', 'Ion Cannon'),
   '%d · %s · %s' % (len(set(ctx)), ctx[0], ctx[-1]))
ck('righe 27 e 164 (prima e ultima del lotto)',
   (cov[0]['line'], cov[-1]['line']) == (27, 164), (cov[0]['line'], cov[-1]['line']))
ck('ZERO segnaposto in inglese e in italiano (asserzione negativa scritta)',
   EN_T == 0 == IT_T and '<' not in IT_ALL and '<' not in ' '.join(v['english'] for v in cov))
ck('2 tab, nelle stesse due unita\' (3 e 4) in entrambe le lingue',
   [v['idx'] for v in cov if v['english'].startswith(TAB)] == [3, 4]
   and [v['idx'] for v in cov if v['italian'].startswith(TAB)] == [3, 4])
ck('2 virgolette in entrambe le lingue, tutte nell\'unita\' 1',
   EN_Q == 2 == IT_Q
   and [v['idx'] for v in cov if QUOTE in v['english']] == [1]
   and [v['idx'] for v in cov if QUOTE in v['italian']] == [1], (EN_Q, IT_Q))
ck("apici: 0 inglesi e 5 italiani (elisione: l'arma, l'alloggiamento, un'arma, l'energia, l'effetto)",
   EN_A == 0 and IT_A == 5 and [v['idx'] for v in cov if APOS in v['italian']] == [6, 7, 8],
   (EN_A, IT_A))
ck('nessun caporale e nessun carattere tipografico (i puntini sono tre punti)',
   not [v['idx'] for v in cov if any(c in v['italian'] for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026')])
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' you ', ' to the ', ' will be ',
        ' is ', ' are ', ' from the ', ' its ', ' it is ', ' such as ', ' rather than ', ' for a ', ' that ')
ck('nessun residuo inglese', not [w for w in ENGW if w in IT_ALL.lower()],
   [w for w in ENGW if w in IT_ALL.lower()])
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
EN_ALL = ' '.join(v['english'] for v in cov)
missing = [n for n in NAMES if n in EN_ALL and n not in IT_ALL]
ck('i nomi di prodotto presenti nel testo inglese restano invariati in italiano', not missing, missing)
ck('«Pulse Turret» e «Ion Cannon» non compaiono nel testo inglese (stanno solo nei contesti): asserzione dichiarata',
   'Pulse Turret' not in EN_ALL and 'Ion Cannon' not in EN_ALL)
ck('«olopad» per holopad, «corsaro» per privateer, «contrabbandiere» per smuggler, «equipaggiamenti»',
   'olopad' in IT_ALL and 'corsaro' in IT_ALL and 'contrabbandiere' in IT_ALL
   and IT_ALL.count('equipaggiamenti') >= 2)
ck('«torretta» per turret (glossario), mai «torretta» al posto di «cannone»',
   'torretta' in by[6]['italian'] and 'Cannon' in by[6]['italian'])
ck('il testo generico sui cannoni a ioni non capitalizza il nome del prodotto',
   by[8]['italian'].startswith('I cannoni a ioni') and 'Ion Cannon' not in by[8]['italian'])
c = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
st = dict(c.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('tutte le 8 unita sono PENDING (misurato)',
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
