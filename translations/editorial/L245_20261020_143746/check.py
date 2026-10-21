r"""check.py — L245 (`data/hai/hai ships.txt`, 46 unita', righe 901-1516). Terzo lotto del file.

**Nessun `VALUE`**: il secondo valore del file (`Geocoris`) e' passato in L244, quindi qui ci sono solo **41 `TEXT`**
(nomi di equipaggiamento con le virgolette dentro) e **5 `DESCRIPTION`** (prosa). Il controllo e' scritto perche' il
`Counter` **non** contenga la chiave `VALUE`, non solo perche' i due conteggi tornino.

**Un solo tab, all'inizio della unita' 46**: e' il secondo paragrafo della scheda dell'Emperor Beetle, che il gioco mostra
rientrato. Va conservato **come primo carattere**, in entrambe le lingue.

**82 virgolette** = 2 per ciascuno dei 41 nomi; **nessuna nella prosa**. Confronto **per unita'**.

**0 apici in inglese, 2 in italiano** (`l'unica` all'unita' 27, `L'Emperor` alla 45).
"""
import collections
import json
import os
import re
import sqlite3

TAB = chr(9)
QUOTE = chr(34)
APOS = chr(39)
TAG = re.compile(r'<[^<>]+>')
HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
PATH = 'data/hai/hai ships.txt'
src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
units = sorted(src['units'], key=lambda x: x['line'])
tr = {}
for p in sorted(f for f in os.listdir(os.path.join(HERE, 'parts')) if f.endswith('.json')):
    for k, v in json.load(open(os.path.join(HERE, 'parts', p), encoding='utf-8')).items():
        tr[int(k)] = v
out = {'block': src['block'], 'note': src['note'], 'units': []}
for u in units:
    if u['idx'] in tr:
        it = tr[u['idx']]
        out['units'].append({"idx": u['idx'], "id": u['id'], "path": u['path'], "line": u['line'],
                             "kind": u['kind'], "context": u['context'], "english": u['english'],
                             "italian": it, "ratio": round(len(it) / max(1, len(u['english'])), 3)})
open(os.path.join(HERE, 'translation.json'), 'w', encoding='utf-8').write(
    json.dumps(out, ensure_ascii=False, indent=1))
cov = out['units']
KINDS = collections.Counter(u['kind'] for u in units)
DATA = [v for v in cov if v['kind'] in ('VALUE', 'TEXT')]
DES = [v for v in cov if v['kind'] == 'DESCRIPTION']
TAB_UNITS = [(v['idx'], v['english'].count(TAB), v['italian'].count(TAB)) for v in cov
             if TAB in v['english'] or TAB in v['italian']]
Q_EN = [(v['idx'], v['english'].count(QUOTE)) for v in cov if QUOTE in v['english']]
Q_IT = [(v['idx'], v['italian'].count(QUOTE)) for v in cov if QUOTE in v['italian']]
A_IT = [(v['idx'], v['italian'].count(APOS)) for v in cov if APOS in v['italian']]
prosa = ' '.join(v['italian'] for v in DES)
ctx = collections.Counter(u['context'] for u in units)
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 46/46", len(cov) == 46 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna unita\' vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 41 TEXT + 5 DESCRIPTION e NESSUN VALUE (il file ne ha 2, il secondo e\' passato in L244)',
   dict(KINDS) == {'TEXT': 41, 'DESCRIPTION': 5} and 'VALUE' not in KINDS, dict(KINDS))
ck('5 contesti: Pond Strider 8, Sea Scorpion 13, Scarab 3, Shield Beetle 20, Emperor Beetle 2',
   dict(ctx) == {'ship:Pond Strider': 8, 'ship:Sea Scorpion': 13, 'ship:Scarab': 3,
                 'ship:Shield Beetle': 20, 'ship:Emperor Beetle': 2} and len(ctx) == 5, dict(ctx))
ck('righe 901 e 1516 (prima e ultima del lotto)',
   (cov[0]['line'], cov[-1]['line']) == (901, 1516), (cov[0]['line'], cov[-1]['line']))
ck("il tab e' UNO, all'inizio della unita' 46 (secondo paragrafo della scheda dell'Emperor Beetle)",
   TAB_UNITS == [(46, 1, 1)] and cov[-1]['italian'].startswith(TAB) and cov[-1]['english'].startswith(TAB),
   TAB_UNITS)
ck('il paragrafo col tab e\' tradotto, non copiato',
   cov[-1]['italian'] != cov[-1]['english'] and 'plunder' not in cov[-1]['italian'])
ck("i 41 TEXT sono IDENTICI all'inglese, per indice",
   all(v['italian'] == v['english'] for v in DATA) and len(DATA) == 41,
   [v['idx'] for v in DATA if v['italian'] != v['english']])
ck("le 5 DESCRIPTION sono TUTTE tradotte (0 identiche)",
   all(v['italian'] != v['english'] for v in DES) and len(DES) == 5)
ck('82 virgolette: 2 per ciascuno dei 41 nomi, per unita\'',
   Q_EN == Q_IT and len(Q_IT) == 41 and set(n for _, n in Q_IT) == {2}
   and sum(n for _, n in Q_IT) == 82, (len(Q_EN), len(Q_IT)))
ck('nessuna virgoletta nella prosa (le 5 schede non citano nulla)',
   all(v['italian'].count(QUOTE) == 0 for v in DES) and all(v['english'].count(QUOTE) == 0 for v in DES))
ck("apici: 0 in inglese, 2 in italiano (unita' 27 e 45: elisioni)",
   sum(v['english'].count(APOS) for v in cov) == 0 and A_IT == [(27, 1), (45, 1)], A_IT)
ck("nessun possessivo inglese ('s) in nessuna delle 46 unita'",
   "'s " not in ' '.join(v['italian'] for v in cov))
NAMES = ('Sea Scorpion', 'Scarab', 'Shield Beetle', 'Emperor Beetle', 'Lightning Bug', 'Grasshopper',
         'Titan Beetle', 'Titan', 'Tracker')
lost = [(v['idx'], n) for v in DES for n in NAMES if n in v['english'] and n not in v['italian']]
ck('ogni nome proprio che l\'inglese nomina resta in italiano, unita\' per unita\'',
   not lost and sum(1 for v in DES for n in NAMES if n in v['english']) >= 10,
   (lost, sum(1 for v in DES for n in NAMES if n in v['english'])))
ck("i plurali inglesi dei nomi non si copiano: «Shield Beetle», «i Tracker»",
   'Shield Beetles' not in ' '.join(v['italian'] for v in cov)
   and 'Trackers' not in ' '.join(v['italian'] for v in cov)
   and 'i Tracker' in prosa and 'Shield Beetle' in prosa)
ck('lessico consolidato: «Slegati», «convogli mercantili», «baie di carico», «ammiraglie», «navi trofeo»',
   all(t in prosa for t in ('Slegati', 'convogli mercantili', 'baie di carico',
                            'ammiraglie', 'navi trofeo', 'corazzatura')))
ck("`Unfettered` non compare mai in italiano (resa «Slegati»)",
   'Unfettered' not in ' '.join(v['italian'] for v in cov))
ck('stesso inglese => stessa resa, nei 6 gruppi di nomi ripetuti',
   all(len({v['italian'] for v in cov if v['english'] == k}) == 1
       for k, n in collections.Counter(v['english'] for v in cov).items() if n > 1)
   and sum(1 for k, n in collections.Counter(v['english'] for v in cov).items() if n > 1) == 6,
   sum(1 for k, n in collections.Counter(v['english'] for v in cov).items() if n > 1))
ck("NESSUN segnaposto (asserzione negativa scritta)",
   sum(len(TAG.findall(v['english'])) for v in cov) == 0 == sum(len(TAG.findall(v['italian'])) for v in cov))
ck('nessun residuo inglese di struttura (the, and, with, that, from)',
   not [w for w in (' the ', ' and ', ' with ', ' that ', ' from ') if w in prosa.lower()],
   [w for w in (' the ', ' and ', ' with ', ' that ', ' from ') if w in prosa.lower()])
ck('registro: nessun «Lei» e nessuna cortesia',
   not re.search(r'\bLei\b|\bSuo\b|\bSua\b|mi scusi', ' '.join(v['italian'] for v in cov)))
ck('nessun caporale e nessun carattere tipografico',
   not [v['idx'] for v in cov if any(c in v['italian'] for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026')])
rs = [v['ratio'] for v in cov]
ck('rapporto nel gate 0,55-1,90 (0,98-1,10; 442 -> 441 parole)',
   0.55 < min(rs) and max(rs) < 1.90, '%.2f - %.2f' % (min(rs), max(rs)))
ACC = re.compile(r"\b(e|piu|perche|cosi|gia|puo|cioe|percio)'(?![a-z])", re.I)
bad = [(v['idx'], ACC.search(v['italian']).group(0)) for v in cov if ACC.search(v['italian'])]
ck("tipografia (accenti veri, nessun apostrofo al posto dell'accento)", not bad, bad)
nonlat = [v['idx'] for v in cov for c in v['italian'] if ord(c) > 127 and not 0x00C0 <= ord(c) <= 0x024F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio',
   not [v['idx'] for v in cov if v['italian'] != v['italian'].rstrip() or '  ' in v['italian']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("74 unita' prima della 901: sono L243 (29) + L244 (45)",
   db.execute('select count(*) from units where path=? and line<901', (PATH,)).fetchone()[0] == 74)
ck("37 unita' dopo la 1516: il lotto NON chiude il file",
   db.execute('select count(*) from units where path=? and line>1516', (PATH,)).fetchone()[0] == 37)
ck("confine misurato: riga 1517, ship:Emperor Beetle (STESSO contesto dell'ultima unita')",
   db.execute('select line,context from units where path=? and line>1516 order by line limit 1', (PATH,)).fetchone()
   == (1517, 'ship:Emperor Beetle') and cov[-1]['context'] == 'ship:Emperor Beetle')
ck('il file intero: 157 unita, righe 15 - 1860',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (157, 15, 1860))
st = dict(db.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('le 46 unita sono PENDING (misurato)',
   db.execute('select count(*) from units where id in (%s) and state != "PENDING"'
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
