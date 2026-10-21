r"""check.py — L127 (`data/incipias/incipias first contact.txt`, 63 unita', righe 224-331)

Tutto il contesto `Help The Stranded 1`: **58 `MISSION_TEXT`**, **3 `LOGBOOK`**, **1 `VALUE`**, **1 `DESCRIPTION`**,
**1 contesto**, **55 unita' con tab**, **98 virgolette**, **2 token**, **63 testi distinti**.

Controlli propri del lotto:

- **il `VALUE`** (`Seek help from the Incipias`) e' **identico al sorgente**: elencato, non «tutti tranne»;
- **i 2 token** (`<first>`, `<last>`) stanno nella **sola unita' 38**: parita' per simbolo e per unita';
- **lo stile degli Incipias** e' di composti con trattino, e il controllo pretende che ce ne siano almeno sei
  (`intenzione-scopo`, `stazione-capitale`, `essere-esterno`, `viaggiatore-di-mondi`, `pianeta-d'aria`,
  `luoghi-sistema`);
- **il Quarg parla di se' in terza persona**: «questo uno» almeno sei volte.
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


ck("unita' tradotte 63/63", len(cov) == 63 == len(units) and not missing, '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
kk = collections.Counter(u['kind'] for u in units)
ck('tipi: 58 MISSION_TEXT · 3 LOGBOOK · 1 VALUE · 1 DESCRIPTION',
   dict(kk) == {'MISSION_TEXT': 58, 'LOGBOOK': 3, 'VALUE': 1, 'DESCRIPTION': 1}, dict(kk))
VAL = [u['idx'] for u in units if u['kind'] == 'VALUE']
ck('il VALUE (unita 1) e identico al sorgente',
   VAL == [1] and by[1]['italian'] == 'Seek help from the Incipias'
   and by[1]['english'] == by[1]['italian'], [(i, by[i]['italian']) for i in VAL])
ck('tutte le unita prosaiche sono tradotte',
   not [v['idx'] for v in cov if v['kind'] != 'VALUE' and v['italian'].strip() == v['english'].strip()],
   [v['idx'] for v in cov if v['kind'] != 'VALUE' and v['italian'].strip() == v['english'].strip()])
ck('i 3 LOGBOOK sono tradotti',
   not [v['idx'] for v in cov if v['kind'] == 'LOGBOOK' and v['italian'] == v['english']])
tok = collections.Counter(t for v in cov for t in TAGS.findall(v['english']))
ck('2 token: <first> 1, <last> 1', dict(tok) == {'<first>': 1, '<last>': 1}, dict(tok))
ck('i token stanno nella sola unita 38, gli stessi in traduzione',
   [v['idx'] for v in cov if TAGS.findall(v['english'])] == [38]
   and TAGS.findall(by[38]['italian']) == TAGS.findall(by[38]['english'])
   and 'capitano <first> <last>' in by[38]['italian'],
   (TAGS.findall(by[38]['italian']), by[38]['italian'][:70]))
tabs = [v['idx'] for v in cov if v['english'].startswith('\t')]
ck('55 unita iniziano con tab, le stesse in traduzione',
   len(tabs) == 55 and tabs == [v['idx'] for v in cov if v['italian'].startswith('\t')], len(tabs))
ck('conteggio dei tab identico per unita',
   not [v['idx'] for v in cov if v['english'].count('\t') != v['italian'].count('\t')])
ck('98 virgolette in inglese e in italiano',
   sum(v['english'].count('"') for v in cov) == 98 == sum(v['italian'].count('"') for v in cov),
   (sum(v['english'].count('"') for v in cov), sum(v['italian'].count('"') for v in cov)))
ck('virgolette per unita: stesso numero',
   not [v['idx'] for v in cov if v['english'].count('"') != v['italian'].count('"')],
   [(v['idx'], v['english'].count('"'), v['italian'].count('"')) for v in cov
    if v['english'].count('"') != v['italian'].count('"')])
ck('nessuna unita con virgolette dispari',
   not [v['idx'] for v in cov if v['english'].count('"') % 2], [v['idx'] for v in cov if v['english'].count('"') % 2])
ck('ZERO quadre · ZERO backtick (asserito)',
   not [v['idx'] for v in cov if any(c in v['english'] + v['italian'] for c in '[]`')])
seen = collections.Counter(u['context'] for u in units)
ck('un solo contesto: Help The Stranded 1',
   list(seen) == ['mission:Incipias: Help The Stranded 1'] and list(seen.values()) == [63],
   list(seen.items()))
ck('prima e ultima unita: righe 224 e 331', (cov[0]['line'], cov[-1]['line']) == (224, 331),
   (cov[0]['line'], cov[-1]['line']))
grp = collections.Counter(u['english'] for u in units)
ck('63 testi distinti per 63 unita', len(grp) == 63, len(grp))
it_grp = {}
for v in cov:
    it_grp.setdefault(v['italian'], []).append(v)
ck('nessun duplicato italiano',
   not [g for g in it_grp.values() if len(g) > 1], [[v['idx'] for v in g] for g in it_grp.values() if len(g) > 1])
LOW = ' '.join(v['italian'] for v in cov).lower()
COMP = ('intenzione-scopo', 'stazione-capitale', 'essere-esterno', 'viaggiatore-di-mondi', 'pianeta-d\'aria',
        'luoghi-sistema')
ck('stile Incipias: 6 composti con trattino', all(c in LOW for c in COMP), [c for c in COMP if c not in LOW])
ck('il Quarg parla di se in terza persona: «questo uno» almeno 6 volte',
   LOW.count('questo uno') >= 6, LOW.count('questo uno'))
TERMS = ('incipias', 'quarg', 'traduttore', 'stazione', 'gigante gassoso', 'iperguida', 'scaglie', 'tentacoli',
         'portello', 'stazione-capitale')
ck('terminologia presente: 10 termini chiave', all(t in LOW for t in TERMS), [t for t in TERMS if t not in LOW])
# «Le tue intenzioni» e «Le stelle» sono articoli, non cortesia: si cercano solo le forme di cortesia
# (il pronome «Lei/lei» e i possessivi maiuscoli in mezzo alla frase), dichiarando il motivo.
CORT = re.findall(r'\b(?:Lei|lei)\b|(?<![.!?] )\b(?:Suo|Sua|Suoi|Sue)\b', ' '.join(v['italian'] for v in cov))
ck('nessuna forma di cortesia «Lei» (il lotto usa tu e voi)', not CORT, CORT)
ck('il voi e plurale e resta (Vi saluto / Vi ringrazio)',
   'Vi saluto' in ' '.join(v['italian'] for v in cov) and 'Vi ringrazio' in ' '.join(v['italian'] for v in cov))
NOSCRUB = ' '.join(TAGS.sub('""', v['italian']) for v in cov if v['kind'] != 'VALUE')
for s in ('Quarg', 'Hai', 'Incipias'):
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
ck('tutte le 63 unita sono PENDING nel database (misurato)',
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
