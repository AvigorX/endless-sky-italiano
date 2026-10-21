r"""check.py — L205 (`data/hai/hai outfits.txt`, 13 unita', righe 805-984). **Lotto terminale del file.**

Porta `hai outfits.txt` a **65/65**: le cinque finestre (L201 8, L202 16, L203 9, L204 19, L205 13) sommano al file
intero. Il controllo di chiusura e' qui, **misurato sul database**, non dedotto.

**13 `DESCRIPTION`**, nessun `VALUE` (i nomi di questi equipaggiamenti stanno nelle unita' `VALUE` dei lotti
precedenti). **Zero segnaposto**, **1 tab** (unita' 13), **2 virgolette** (unita' 3, dentro il nome `"Basrem"`).

**Apici**: **1 inglese** (`species'`, unita' 11) contro **4 italiani** (unita' 7, 8, 9: elisione).

**Unita' 12 e 13 sono lo stesso oggetto** (Shield Beetle Pendant): la 13 e' indentata e descrive la teca.
**Punteggiatura del sorgente conservata**: i tre punti di unita' 10 e i due trattini di unita' 13.
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
ED = os.path.join(L10N, 'staging/editorial')
PATH = 'data/hai/hai outfits.txt'
WINDOWS = [('L201_20261019_204959', 8), ('L202_20261019_205624', 16), ('L203_20261019_210258', 9),
           ('L204_20261019_210851', 19), ('L205_20261019_211129', 13)]
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
EN_ALL = ' '.join(v['english'] for v in cov)
EN_T = sum(len(TAGS.findall(v['english'])) for v in cov)
IT_T = sum(len(TAGS.findall(v['italian'])) for v in cov)
EN_Q = sum(v['english'].count(QUOTE) for v in cov)
IT_Q = sum(v['italian'].count(QUOTE) for v in cov)
EN_A = sum(v['english'].count(APOS) for v in cov)
IT_A = sum(v['italian'].count(APOS) for v in cov)
KINDS = collections.Counter(u['kind'] for u in units)
NAMES = ('Deep Sky', 'Basrem', 'Benga', 'Biroo', 'Bondir', 'Bufaer', 'Pulse Rifle', 'Shield Beetle',
         'Nanachi', 'Korath', 'Unfettered Hai')
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 13/13", len(cov) == 13 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 13 DESCRIPTION (asserzione scritta)', KINDS == {'DESCRIPTION': 13}, dict(KINDS))
ck('ZERO VALUE, TEXT, DIALOG, UI_LABEL (asserzioni vuote scritte)',
   [u['idx'] for u in units if u['kind'] != 'DESCRIPTION'] == [])
ctx = [u['context'].replace('outfit:', '') for u in units]
ck('12 contesti distinti da 13 unita\': Shield Beetle Pendant ne ha due (righe 983 e 984)',
   len(set(ctx)) == 12 and (ctx[0], ctx[-1]) == ('"Bondir" Atomic Thruster', 'Shield Beetle Pendant')
   and (cov[-2]['context'], cov[-1]['context']) == ('outfit:Shield Beetle Pendant',) * 2,
   '%d · %s · %s' % (len(set(ctx)), ctx[0], ctx[-1]))
ck('righe 805 e 984 (prima e ultima del lotto e del file)',
   (cov[0]['line'], cov[-1]['line']) == (805, 984), (cov[0]['line'], cov[-1]['line']))
ck('ZERO segnaposto in entrambe le lingue (asserzione negativa scritta)',
   EN_T == 0 == IT_T and '<' not in IT_ALL and '<' not in EN_ALL)
ck("1 tab, nella stessa unita' (13) in entrambe le lingue",
   [v['idx'] for v in cov if v['english'].startswith(TAB)] == [13]
   and [v['idx'] for v in cov if v['italian'].startswith(TAB)] == [13])
ck("2 virgolette in entrambe le lingue, nella stessa unita' (3), dentro il nome \"Basrem\"",
   EN_Q == 2 == IT_Q
   and [v['idx'] for v in cov if QUOTE in v['english']] == [3]
   and [v['idx'] for v in cov if QUOTE in v['italian']] == [3], (EN_Q, IT_Q))
ck("apici: 1 inglese (species', unita' 11) e 4 italiani (unita' 7, 8, 9)",
   EN_A == 1 and IT_A == 4
   and [v['idx'] for v in cov if APOS in v['english']] == [11]
   and [v['idx'] for v in cov if APOS in v['italian']] == [7, 8, 9], (EN_A, IT_A))
ck('nessun caporale e nessun carattere tipografico',
   not [v['idx'] for v in cov if any(c in v['italian'] for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026')])
ck("punteggiatura del sorgente conservata: i tre punti di unita' 10 (a meta' frase) e i due trattini di unita' 13",
   by[10]['italian'].count('...') == 1 == by[10]['english'].count('...')
   and by[13]['italian'].count(' - ') == 2 == by[13]['english'].count(' - '),
   (by[10]['italian'].count('...'), by[10]['english'].count('...'), by[13]['italian'].count(' - ')))
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
ck('i nomi di prodotto, di azienda e di persona presenti nel testo inglese restano invariati',
   not [n for n in NAMES if n in EN_ALL and n not in IT_ALL],
   [n for n in NAMES if n in EN_ALL and n not in IT_ALL])
ck('keystone = «chiavi di volta» anche al plurale (unita\' 13), nessuna «pietra chiave»',
   'chiavi di volta quantistiche' in by[13]['italian'] and 'pietra chiave' not in IT_ALL)
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
lines, wrong = [], []
for w, n in WINDOWS:
    d = json.load(open(os.path.join(ED, w, 'translation.json'), encoding='utf-8'))['units']
    got = [u['line'] for u in d if u['path'] == PATH]
    if len(got) != n:
        wrong.append((w, n, len(got)))
    lines += got
dbl = [r[0] for r in db.execute('select line from units where path=? order by line', (PATH,))]
ck('FILE CHIUSO: 65/65 righe distinte, nessun buco, nessuna sovrapposizione',
   not wrong and sorted(lines) == dbl and len(set(lines)) == len(lines) == 65,
   (wrong, len(lines), len(set(lines)), len(dbl), [x for x in dbl if x not in set(lines)][:5]))
st = dict(db.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('le 13 unita sono PENDING (misurato)',
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
