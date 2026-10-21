r"""check.py — L129 (`data/human/boarding missions.txt`, 89 unita', righe 15-386)

Primo lotto del file. Forma nuova: **48 `TEXT`** sono frammenti di frase concatenati dal gioco, quindi il lotto ha un
invariante che i precedenti non avevano — **spazi iniziali e finali identici al sorgente**, unita' per unita'.

Controlli propri:

- **4 unita' non sono testo** (1, 2: template `${...}`; 27, 28: nomi di frase citati da `phrase`) e restano identiche;
- **6 `VALUE`** identici (nomi di missione, uno ripetuto quattro volte);
- **2 frammenti di sola punteggiatura** (29 `, `, 44 `.`) identici per necessita';
- **spazi** iniziali e finali identici su tutte le 89 unita' (senza, la frase composta si rompe);
- **43 token in 7 famiglie**, verificati per unita' e non solo in somma;
- **ripetizioni**: stesso inglese ⇒ stessa resa (80 testi distinti su 89 unita').
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


ck("unita' tradotte 89/89", len(cov) == 89 == len(units) and not missing, '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
kk = collections.Counter(u['kind'] for u in units)
ck('tipi: 48 TEXT · 21 MISSION_TEXT · 6 CONVERSATION · 6 VALUE · 6 DESCRIPTION · 2 DIALOG',
   dict(kk) == {'TEXT': 48, 'MISSION_TEXT': 21, 'CONVERSATION': 6, 'VALUE': 6, 'DESCRIPTION': 6, 'DIALOG': 2},
   dict(kk))
IDENT = [1, 2, 27, 28]
ck('le 4 unita che non sono testo restano identiche (2 template, 2 nomi di frase)',
   [by[i]['italian'] for i in IDENT] == [by[i]['english'] for i in IDENT]
   and by[1]['english'].startswith('${assist merchant 1}') and by[27]['english'] == 'assist merchant 2 simple',
   [(i, by[i]['italian'][:40]) for i in IDENT])
VAL = [u['idx'] for u in units if u['kind'] == 'VALUE']
ck('i 6 VALUE sono identici al sorgente',
   VAL == [51, 71, 82, 84, 86, 88]
   and all(by[i]['italian'] == by[i]['english'] for i in VAL)
   and by[82]['italian'] == by[84]['italian'] == by[86]['italian'] == by[88]['italian'] == 'Defend <planet>',
   [(i, by[i]['italian']) for i in VAL])
ck('i 2 frammenti di sola punteggiatura restano identici',
   by[29]['italian'] == ', ' and by[44]['italian'] == '.', (repr(by[29]['italian']), repr(by[44]['italian'])))
ck('tutte le unita prosaiche sono tradotte',
   not [v['idx'] for v in cov if v['idx'] not in IDENT + VAL and v['italian'].strip() == v['english'].strip()
        and v['idx'] not in (29, 44)])
ck('spazi iniziali identici al sorgente (89/89)',
   not [v['idx'] for v in cov
        if len(v['italian'].lstrip('\t')) - len(v['italian'].lstrip('\t').lstrip(' '))
        != len(v['english'].lstrip('\t')) - len(v['english'].lstrip('\t').lstrip(' '))])
ck('spazi finali identici al sorgente (89/89): i frammenti finiscono dove finisce il testo',
   not [v['idx'] for v in cov
        if len(v['italian']) - len(v['italian'].rstrip()) != len(v['english']) - len(v['english'].rstrip())],
   [(v['idx'], repr(v['english'][-6:]), repr(v['italian'][-6:])) for v in cov
    if len(v['italian']) - len(v['italian'].rstrip()) != len(v['english']) - len(v['english'].rstrip())])
tabs = [v['idx'] for v in cov if v['english'].startswith('\t')]
ck('22 unita iniziano con tab, le stesse in traduzione',
   len(tabs) == 22 and tabs == [v['idx'] for v in cov if v['italian'].startswith('\t')], len(tabs))
ck('10 virgolette in inglese e in italiano',
   sum(v['english'].count('"') for v in cov) == 10 == sum(v['italian'].count('"') for v in cov),
   (sum(v['english'].count('"') for v in cov), sum(v['italian'].count('"') for v in cov)))
ck('virgolette per unita: stesso numero',
   not [v['idx'] for v in cov if v['english'].count('"') != v['italian'].count('"')],
   [(v['idx'], v['english'].count('"'), v['italian'].count('"')) for v in cov
    if v['english'].count('"') != v['italian'].count('"')])
tok = collections.Counter(t for v in cov for t in TAGS.findall(v['english']))
ck('43 token in 7 famiglie',
   dict(tok) == {'<origin>': 17, '<destination>': 9, '<planet>': 7, '<payment>': 6, '<cargo>': 2, '<bunks>': 1,
                 '<commodity>': 1}, dict(tok))
ck('token per unita: sequenza identica',
   not [v['idx'] for v in cov if TAGS.findall(v['english']) != TAGS.findall(v['italian'])],
   [(v['idx'], TAGS.findall(v['english']), TAGS.findall(v['italian'])) for v in cov
    if TAGS.findall(v['english']) != TAGS.findall(v['italian'])])
ck('ZERO quadre e zero backtick (asserito)',
   not [v['idx'] for v in cov if any(c in v['english'] + v['italian'] for c in '[]`')])
seen = collections.OrderedDict()
for u in units:
    seen[u['context']] = seen.get(u['context'], 0) + 1
ck('18 contesti, distribuzione misurata',
   len(seen) == 18 and list(seen.values()) == [1, 1, 6, 3, 5, 10, 2, 1, 5, 9, 7, 20, 7, 4, 2, 2, 2, 2],
   list(seen.values()))
ck('prima e ultima unita: righe 15 e 386', (cov[0]['line'], cov[-1]['line']) == (15, 386),
   (cov[0]['line'], cov[-1]['line']))
ck('primo e ultimo contesto: assisting merchant / Assisting Syndicate',
   (cov[0]['context'], cov[-1]['context']) == ('conversation:assisting merchant', 'mission:Assisting Syndicate'),
   (cov[0]['context'], cov[-1]['context']))
grp = {}
for v in cov:
    grp.setdefault(v['english'].lstrip('\t'), set()).add(v['italian'])
ck('80 testi distinti su 89 unita', len(grp) == 80, len(grp))
ck('stesso inglese => stessa resa (3 coppie di opzioni, 4 DESC, 4 VALUE)',
   not [(k, v) for k, v in grp.items() if len(v) > 1], [(k[:40], v) for k, v in grp.items() if len(v) > 1])
LOW = ' '.join(v['italian'] for v in cov).lower()
ck('frammenti presenti: apertura, verbi, articolo, finale',
   all(t in LOW for t in ('sapendo che', 'hai cambiato rotta', 'rischiato', 'per ', 'salvare', 'capitano',
                          'ti dà', 'in segno di gratitudine')))
TERMS = ('asteroide', 'nave', 'equipaggio', 'capitano', 'carico', 'pirati', 'crediti', 'portello', 'radar',
         'flotta')
ck('terminologia presente: 10 termini chiave', all(t in LOW for t in TERMS), [t for t in TERMS if t not in LOW])
# residui inglesi: si cercano solo nei testi lunghi, perche' i frammenti sono parole singole per definizione
LONG = ' '.join(TAGS.sub('""', v['italian']) for v in cov if v['idx'] not in IDENT and len(v['english']) > 40)
for s in ('Quarg', 'Hai'):
    LONG = LONG.replace(s, '@@')
LONG = LONG.lower()
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' ship ', ' you ')
ck('nessun residuo inglese nei testi lunghi',
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
ck('tutte le 89 unita sono PENDING nel database (misurato)',
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
