r"""check.py — L128 (`data/incipias/incipias first contact.txt`, 43 unita', righe 343-439). **CHIUDE IL FILE.**

Coda del file: **3 contesti** (2 + 1 + 40), **33 `MISSION_TEXT`**, **4 `UI_LABEL`**, **3 `LOGBOOK`**, **1 `DIALOG`**,
**1 `VALUE`**, **1 `DESCRIPTION`**, **30 unita' con tab**, **43 virgolette**, **6 token** in **5 famiglie**.

Controlli propri del lotto:

- **le 4 `UI_LABEL`** (`has incipias ship`, `initial choice`, `odd question`, `end no time`) sono identiche;
- **il `VALUE`** (`Bring Incipias back to <planet>`) e' identico **token compreso**;
- **i 6 token** stanno nelle unita' 1, 4, 5, 6, 19: parita' per unita', non solo per somma;
- **la voce di diario dell'unita' 2** e' **identica alla resa di L127 unita' 24**: il controllo la rilegge dal
  `translation.json` di L127 e confronta, invece di fidarsi della memoria;
- **tre unita' con una sola virgoletta** (28, 30, 36): il sorgente apre la battuta e non la chiude.
"""
import collections
import json
import os
import re
import sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
PREV = os.path.join(L10N, 'staging/editorial/L127_20261019_073900/translation.json')
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
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 43/43", len(cov) == 43 == len(units) and not missing, '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
kk = collections.Counter(u['kind'] for u in units)
ck('tipi: 33 MISSION_TEXT · 4 UI_LABEL · 3 LOGBOOK · 1 DIALOG · 1 VALUE · 1 DESCRIPTION',
   dict(kk) == {'MISSION_TEXT': 33, 'UI_LABEL': 4, 'LOGBOOK': 3, 'DIALOG': 1, 'VALUE': 1, 'DESCRIPTION': 1},
   dict(kk))
LAB = [u['idx'] for u in units if u['kind'] == 'UI_LABEL']
ck('le 4 UI_LABEL (11, 13, 38, 42) sono identiche al sorgente',
   LAB == [11, 13, 38, 42]
   and [by[i]['italian'] for i in LAB] == ['has incipias ship', 'initial choice', 'odd question', 'end no time'],
   [(i, by[i]['italian']) for i in LAB])
ck('il VALUE (unita 4) e identico al sorgente, token compreso',
   by[4]['kind'] == 'VALUE' and by[4]['italian'] == by[4]['english'] == 'Bring Incipias back to <planet>',
   by[4]['italian'])
ck('tutte le unita prosaiche sono tradotte',
   not [v['idx'] for v in cov if v['kind'] not in ('UI_LABEL', 'VALUE')
        and v['italian'].strip() == v['english'].strip()])
ck('i 3 LOGBOOK e il DIALOG sono tradotti',
   not [v['idx'] for v in cov if v['kind'] in ('LOGBOOK', 'DIALOG') and v['italian'] == v['english']])
tok = collections.Counter(t for v in cov for t in TAGS.findall(v['english']))
ck('6 token in 5 famiglie', dict(tok) == {'<ship>': 2, '<planet>': 1, '<destination>': 1, '<origin>': 1,
                                          '<bunks>': 1}, dict(tok))
ck('i token stanno nelle unita 1, 4, 5, 6, 19 e sono gli stessi in traduzione',
   [v['idx'] for v in cov if TAGS.findall(v['english'])] == [1, 4, 5, 6, 19]
   and not [v['idx'] for v in cov if TAGS.findall(v['english']) != TAGS.findall(v['italian'])],
   [(v['idx'], TAGS.findall(v['english']), TAGS.findall(v['italian'])) for v in cov
    if TAGS.findall(v['english']) != TAGS.findall(v['italian'])])
prev = {u['english']: u['italian'] for u in json.load(open(PREV, encoding='utf-8'))['units']}
ck('la voce di diario dell unita 2 riproduce alla lettera quella di L127 (unita 24)',
   by[2]['english'] in prev and by[2]['italian'] == prev[by[2]['english']],
   (by[2]['italian'][:60], prev.get(by[2]['english'], '')[:60]))
tabs = [v['idx'] for v in cov if v['english'].startswith('\t')]
ck('30 unita iniziano con tab, le stesse in traduzione',
   len(tabs) == 30 and tabs == [v['idx'] for v in cov if v['italian'].startswith('\t')], len(tabs))
ck('conteggio dei tab identico per unita',
   not [v['idx'] for v in cov if v['english'].count('\t') != v['italian'].count('\t')])
ck('43 virgolette in inglese e in italiano',
   sum(v['english'].count('"') for v in cov) == 43 == sum(v['italian'].count('"') for v in cov),
   (sum(v['english'].count('"') for v in cov), sum(v['italian'].count('"') for v in cov)))
ck('virgolette per unita: stesso numero',
   not [v['idx'] for v in cov if v['english'].count('"') != v['italian'].count('"')],
   [(v['idx'], v['english'].count('"')) for v in cov if v['english'].count('"') != v['italian'].count('"')])
odd = [v['idx'] for v in cov if v['english'].count('"') % 2]
ck('una sola virgoletta nelle unita 28, 30, 36 (battute non chiuse dal sorgente), riprodotta',
   odd == [28, 30, 36] and all(by[i]['italian'].count('"') == 1 for i in odd), odd)
ck('ZERO quadre · ZERO backtick (asserito)',
   not [v['idx'] for v in cov if any(c in v['english'] + v['italian'] for c in '[]`')])
seen = collections.OrderedDict()
for u in units:
    seen[u['context']] = seen.get(u['context'], 0) + 1
ck('3 contesti: 2 / 1 / 40',
   list(seen.items()) == [('mission:Incipias: Fix Saves Missing Language', 2),
                          ('mission:Incipias: No Help For The Stranded', 1),
                          ('mission:Incipias: Help The Stranded 2', 40)], list(seen.items()))
ck('prima e ultima unita: righe 343 e 439', (cov[0]['line'], cov[-1]['line']) == (343, 439),
   (cov[0]['line'], cov[-1]['line']))
grp = collections.Counter(u['english'] for u in units)
ck('43 testi distinti per 43 unita', len(grp) == 43, len(grp))
it_grp = {}
for v in cov:
    it_grp.setdefault(v['italian'], []).append(v)
ck('nessun duplicato italiano',
   not [g for g in it_grp.values() if len(g) > 1], [[v['idx'] for v in g] for g in it_grp.values() if len(g) > 1])
LOW = ' '.join(v['italian'] for v in cov).lower()
COMP = ('giorno-momento', 'protettore-di-vite', 'calamità-meteo', 'aiutante-esterno', 'capi-governatori',
        'domande-quesiti', 'tempo-pazienza', 'vuoto-spazio', 'osservare-studiare', 'mondo-origine',
        'orgoglio-azione', 'ponte-stellare', 'sale-nuvole', 'incontro-colloquio', 'comprensione-triste')
ck('stile Incipias: 15 composti con trattino', all(c in LOW for c in COMP), [c for c in COMP if c not in LOW])
TERMS = ('incipias', 'quarg', 'hicemus', 'conlatio', 'gigante gassoso', 'portello', 'traduttore', 'scaglie',
         'tentacoli', 'scafo')
ck('terminologia presente: 10 termini chiave', all(t in LOW for t in TERMS), [t for t in TERMS if t not in LOW])
# la cortesia si scrive con la maiuscola («Lei», «Suo»); «su di lei» riferito alla nave e' un pronome, non
# cortesia, e non va vietato: il controllo cerca solo le forme di cortesia.
CORT = re.findall(r'\bLei\b|(?<![.!?] )\b(?:Suo|Sua|Suoi|Sue)\b', ' '.join(v['italian'] for v in cov))
ck('nessuna forma di cortesia «Lei»', not CORT, CORT)
NOSCRUB = ' '.join(TAGS.sub('""', v['italian']) for v in cov if v['kind'] not in ('UI_LABEL', 'VALUE'))
for s in ('Quarg', 'Hai', 'Incipias', 'Hicemus', 'Conlatio'):
    NOSCRUB = NOSCRUB.replace(s, '@@')
NOSCRUB = NOSCRUB.lower()
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' ship ', ' voice ')
ck('nessun residuo inglese fuori dai nomi propri e dai token',
   not [w for w in ENGW if w in NOSCRUB], [w for w in ENGW if w in NOSCRUB])
rs = [v['ratio'] for v in cov]
ck('rapporto nel gate', 0.55 < min(rs) and max(rs) < 1.90, '%.2f - %.2f' % (min(rs), max(rs)))
bad = [(v['idx'], n) for v in cov for p, n in ((r"\b(e|piu|perche|cosi|gia|puo|cioe|percio|fa)'", 'accento'),
       ('\u2026', 'ellissi'), ('\u2014', 'em dash'), ('\u2019', 'apostrofo curvo'), ('\u00ab', 'caporale'),
       ('\u00bb', 'caporale')) if re.search(p, v['italian'])]
ck('tipografia', not bad, bad)
nonlat = [v['idx'] for v in cov for c in v['italian'] if ord(c) > 127 and not 0x00C0 <= ord(c) <= 0x024F]
ck('caratteri non latini', not nonlat, nonlat)
c = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
st = dict(c.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('tutte le 43 unita sono PENDING nel database (misurato)',
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
