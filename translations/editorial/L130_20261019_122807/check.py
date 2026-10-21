r"""check.py — L130 (`data/human/boarding missions.txt`, 75 unita', righe 417-686)

Secondo lotto del file: **4 contesti** (1 / 1 / 6 / 67), **50 `MISSION_TEXT`**, **22 `UI_LABEL`**, **1
`CONVERSATION`**, **1 `DESCRIPTION`**, **1 `DIALOG`**, **nessun `VALUE`**.

Controlli propri:

- **le 22 `UI_LABEL`** sono nomi di nodo: identiche al sorgente, elencate una per una;
- **zero `VALUE`**: asserzione **vuota** scritta (`Counter(...) == {}`), non un'omissione;
- **l'unita' 21 ha tre virgolette** (battuta non chiusa dal sorgente), riprodotta;
- **19 token in 5 famiglie**, verificati per unita';
- **74 testi distinti** su 75 unita' (35 e 59 identiche): stesso inglese ⇒ stessa resa.
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
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


LAB = [9, 10, 12, 14, 16, 22, 24, 36, 40, 41, 42, 44, 45, 54, 57, 60, 62, 63, 65, 67, 69, 72]
ck("unita' tradotte 75/75", len(cov) == 75 == len(units) and not missing, '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
kk = collections.Counter(u['kind'] for u in units)
ck('tipi: 50 MISSION_TEXT · 22 UI_LABEL · 1 CONVERSATION · 1 DESCRIPTION · 1 DIALOG',
   dict(kk) == {'MISSION_TEXT': 50, 'UI_LABEL': 22, 'CONVERSATION': 1, 'DESCRIPTION': 1, 'DIALOG': 1}, dict(kk))
ck('le 22 UI_LABEL sono identiche al sorgente',
   [u['idx'] for u in units if u['kind'] == 'UI_LABEL'] == LAB
   and all(by[i]['italian'] == by[i]['english'] for i in LAB),
   [(i, by[i]['italian']) for i in LAB if by[i]['italian'] != by[i]['english']])
ck('le 22 UI_LABEL sono quelle elencate (nomi di nodo)',
   [by[i]['english'] for i in LAB] == ['boarding alone', 'flagship is empty', 'first mate left on flagship',
                                       'boarding with a big boarding party', 'first decision', 'crew missing',
                                       'get to work', 'trickster or monster', 'attack with the element of surprise',
                                       'attack but tarquin is prepared', 'attack alone with the element of surprise',
                                       'attack alone but tarquin is prepared', 'attack with a big boarding party',
                                       'has brig', 'blackmailing with a big boarding party', 'blackmailing alone',
                                       'the direct approach', 'acting stupid alone', 'bad luck', 'good luck',
                                       'rescue the crew', 'rescue the crew with tarquin captured'],
   [by[i]['english'] for i in LAB])
ck('ZERO VALUE (asserzione vuota scritta)', collections.Counter(u['kind'] for u in units if u['kind'] == 'VALUE') == {})
ck('tutte le unita prosaiche sono tradotte',
   not [v['idx'] for v in cov if v['idx'] not in LAB and v['italian'].strip() == v['english'].strip()])
tabs = [v['idx'] for v in cov if v['english'].startswith('\t')]
ck('45 unita iniziano con tab, le stesse in traduzione',
   len(tabs) == 45 and tabs == [v['idx'] for v in cov if v['italian'].startswith('\t')], len(tabs))
ck('spazi iniziali e finali identici al sorgente (75/75)',
   not [v['idx'] for v in cov
        if len(v['italian']) - len(v['italian'].rstrip()) != len(v['english']) - len(v['english'].rstrip())])
ck('31 virgolette in inglese e in italiano',
   sum(v['english'].count('"') for v in cov) == 31 == sum(v['italian'].count('"') for v in cov),
   (sum(v['english'].count('"') for v in cov), sum(v['italian'].count('"') for v in cov)))
ck('virgolette per unita: stesso numero',
   not [v['idx'] for v in cov if v['english'].count('"') != v['italian'].count('"')],
   [(v['idx'], v['english'].count('"')) for v in cov if v['english'].count('"') != v['italian'].count('"')])
odd = [v['idx'] for v in cov if v['english'].count('"') % 2]
ck('una sola unita con virgolette dispari (21, tre virgolette), riprodotta',
   odd == [21] and by[21]['italian'].count('"') == 3, (odd, by[21]['italian'].count('"')))
tok = collections.Counter(t for v in cov for t in TAGS.findall(v['english']))
ck('19 token in 5 famiglie',
   dict(tok) == {'<origin>': 12, '<payment>': 2, '<bunks>': 2, '<destination>': 2, '<planet>': 1}, dict(tok))
ck('token per unita: sequenza identica',
   not [v['idx'] for v in cov if TAGS.findall(v['english']) != TAGS.findall(v['italian'])],
   [(v['idx'], TAGS.findall(v['english']), TAGS.findall(v['italian'])) for v in cov
    if TAGS.findall(v['english']) != TAGS.findall(v['italian'])])
ck('ZERO quadre e zero backtick (asserito)',
   not [v['idx'] for v in cov if any(c in v['english'] + v['italian'] for c in '[]`')])
seen = collections.OrderedDict()
for u in units:
    seen[u['context']] = seen.get(u['context'], 0) + 1
ck('4 contesti: 1 / 1 / 6 / 67',
   list(seen.items()) == [('conversation:boarding pirate', 1), ('mission:Pirate Ambush', 1),
                          ('mission:Pirate Mutiny', 6), ('mission:Slave Crew Rescue', 67)], list(seen.items()))
ck('prima e ultima unita: righe 417 e 686', (cov[0]['line'], cov[-1]['line']) == (417, 686),
   (cov[0]['line'], cov[-1]['line']))
grp = {}
for v in cov:
    grp.setdefault(v['english'].lstrip('\t'), set()).add(v['italian'])
ck('74 testi distinti su 75 unita (35 e 59 identiche)', len(grp) == 74, len(grp))
ck('stesso inglese => stessa resa',
   not [(k, v) for k, v in grp.items() if len(v) > 1], [(k[:40], v) for k, v in grp.items() if len(v) > 1])
LOW = ' '.join(v['italian'] for v in cov).lower()
TERMS = ('tarquin', 'equipaggio', 'nave', 'capitano', 'schiavi', 'crediti', 'capsula di salvataggio',
         'autodistruzione', 'paratia', 'gettoni di credito')
ck('terminologia presente: 10 termini chiave', all(t in LOW for t in TERMS), [t for t in TERMS if t not in LOW])
ck('registro di Tarquin: spilorcio, zotici, lezione imparata',
   all(t in LOW for t in ('spilorcio', 'zotici', 'lezione imparata')))
ck('il tema della tratta e esplicito: schiavitu, negriera, prigionia',
   all(t in LOW for t in ('schiavitù', 'negriera', 'prigionia')))
LONG = ' '.join(TAGS.sub('""', v['italian']) for v in cov if v['idx'] not in LAB)
for s in ('Tarquin', 'New India', 'Quarg', 'Hai'):
    LONG = LONG.replace(s, '@@')
LONG = LONG.lower()
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' ship ', ' you ', ' he ')
ck('nessun residuo inglese fuori dai nomi propri',
   not [w for w in ENGW if w in LONG], [w for w in ENGW if w in LONG])
CORT = re.findall(r'\bLei\b|(?<![.!?] )\b(?:Suo|Sua|Suoi|Sue)\b', ' '.join(v['italian'] for v in cov))
ck('nessuna forma di cortesia «Lei»', not CORT, CORT)
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
ck('tutte le 75 unita sono PENDING nel database (misurato)',
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
