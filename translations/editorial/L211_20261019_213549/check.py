r"""check.py — L211 (`data/coalition/coalition news.txt`, 16 unita', righe 401-496). **Lotto terminale del file.**

Porta `coalition news.txt` a **112/112**. Le sei finestre (L206 20, L207 17, L208 19, L209 21, L210 19, L211 16) sommano
al file intero, e il controllo di chiusura e' qui, misurato sul database.

**Struttura insolita**: le unita' **6** e **11** sono **una sola virgoletta doppia** ciascuna — una citazione che si apre
alla riga 458 e si chiude alla 465, con quattro paragrafi in mezzo (7-10) che **non** portano virgolette. Va riprodotta
esattamente: 1 virgoletta in 6, zero in 7-10, 1 in 11. E' il primo caso della campagna di citazione spezzata su piu'
unita'.

**Registro**: 13 unita' su 16 chiudono con un verbo. Le eccezioni sono le due unita' strutturali (6 e 11, senza testo) e
l'unita' 9, che chiude con «gioia» come il sorgente chiude con *joy*.
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
PATH = 'data/coalition/coalition news.txt'
WINDOWS = [('L206_20261019_211311', 20), ('L207_20261019_211444', 17), ('L208_20261019_212349', 19),
           ('L209_20261019_212543', 21), ('L210_20261019_213332', 19), ('L211_20261019_213549', 16)]
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
WORDS = re.compile(r"[A-Za-z\u00C0-\u024F']+")
IT_ALL = ' '.join(v['italian'] for v in cov)
EN_ALL = ' '.join(v['english'] for v in cov)
EN_T = sum(len(TAGS.findall(v['english'])) for v in cov)
IT_T = sum(len(TAGS.findall(v['italian'])) for v in cov)
EN_Q = sum(v['english'].count(QUOTE) for v in cov)
IT_Q = sum(v['italian'].count(QUOTE) for v in cov)
EN_A = sum(v['english'].count(APOS) for v in cov)
IT_A = sum(v['italian'].count(APOS) for v in cov)
KINDS = collections.Counter(u['kind'] for u in units)
CTX = collections.Counter(u['context'].replace('news:', '') for u in units)
SPLIT = [6, 11]
VERB_FINAL = [1, 2, 3, 4, 5, 7, 8, 10, 12, 13, 14, 15, 16]
NAMES = ('Anna Fangvin', 'Beyond the Hyperdrive', 'Kimek', 'Arach', 'Saryd')
VEND = ('sono', 'facciano', 'faccio', 'fatto', 'stato', 'sei', 'puoi', 'fanno', 'è', 'possiamo', "l'ho")
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


def tail(i):
    w = WORDS.findall(by[i]['italian'].rstrip('."!?'))
    return w[-1] if w else ''


ck("unita' tradotte 16/16", len(cov) == 16 == len(units), '%d/%d' % (len(cov), len(units)))
ck("tutte le unita' tranne le due strutturali (6, 11) hanno testo non vuoto",
   not [v['idx'] for v in cov if v['idx'] not in SPLIT and not v['italian'].strip()])
ck('tipi: 16 NEWS', KINDS == {'NEWS': 16}, dict(KINDS))
ck('ZERO VALUE, TEXT, DIALOG, UI_LABEL (asserzioni vuote scritte)',
   [u['idx'] for u in units if u['kind'] != 'NEWS'] == [])
ck('4 contesti: games planet heliarch 1, games planet people 4, fangvin 6, lunarium 5',
   len(CTX) == 4 and sorted(CTX.values()) == [1, 4, 5, 6], dict(CTX))
ck('righe 401 e 496 (prima e ultima del lotto e del file)',
   (cov[0]['line'], cov[-1]['line']) == (401, 496), (cov[0]['line'], cov[-1]['line']))
ck('ZERO segnaposto e ZERO tab in entrambe le lingue (asserzioni vuote scritte)',
   EN_T == 0 == IT_T and '<' not in IT_ALL and '<' not in EN_ALL
   and [v['idx'] for v in cov if TAB in v['english'] or TAB in v['italian']] == [])
ck('22 virgolette con la STESSA distribuzione per unita\' (2,2,2,2,2,1,0,0,0,0,1,2,2,2,2,2)',
   EN_Q == 22 == IT_Q
   and [v['english'].count(QUOTE) for v in cov] == [2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2]
   and [v['italian'].count(QUOTE) for v in cov] == [2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2],
   (EN_Q, IT_Q))
ck('CITAZIONE SPEZZATA: le unita\' 6 e 11 sono esattamente una virgoletta, nei due sensi',
   all(by[i]['english'] == QUOTE and by[i]['italian'] == QUOTE for i in SPLIT))
ck('CITAZIONE SPEZZATA: le unita\' 7-10 non portano virgolette e restano testo nudo',
   all(by[i]['english'].count(QUOTE) == 0 == by[i]['italian'].count(QUOTE) for i in (7, 8, 9, 10)))
ck("apici: 6 inglesi (unita' 7, 10, 12, 14) e 14 italiani (unita' 1, 2, 7, 8, 9, 10, 13, 14, 16)",
   EN_A == 6 and IT_A == 14
   and [v['idx'] for v in cov if APOS in v['english']] == [7, 10, 12, 14]
   and [v['idx'] for v in cov if APOS in v['italian']] == [1, 2, 7, 8, 9, 10, 13, 14, 16], (EN_A, IT_A))
ck("il titolo 'Beyond the Hyperdrive' resta in inglese e con gli apici singoli, due volte",
   IT_ALL.count("'Beyond the Hyperdrive'") == 2 == EN_ALL.count("'Beyond the Hyperdrive'"))
ck('REGISTRO SARYD: 13 unita\' su 16 chiudono con un verbo flesso',
   [i for i in sorted(by) if tail(i) in VEND] == VERB_FINAL,
   [i for i in sorted(by) if tail(i) in VEND])
ck("le tre eccezioni: le due unita' strutturali 6 e 11 (senza testo) e l'unita' 9, che chiude con «gioia» come «joy»",
   [i for i in sorted(by) if tail(i) not in VEND] == [6, 9, 11]
   and by[9]['italian'].rstrip(QUOTE + '.!?').endswith('gioia')
   and by[9]['english'].rstrip(QUOTE + '.!?').endswith('joy'))
ck('nessun caporale e nessun carattere tipografico',
   not [v['idx'] for v in cov if any(c in v['italian'] for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026')])
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' you ', ' to the ', ' will be ',
        ' is ', ' are ', ' from the ', ' its ', ' it is ', ' such as ', ' rather than ', ' for a ', ' that ')
# il titolo inglese del libro e il nome proprio sono testi da conservare: si tolgono prima del controllo
IT_SCAN = IT_ALL.replace('Beyond the Hyperdrive', '').replace('Anna Fangvin', '')
ck("nessun residuo inglese (titolo del libro e nome proprio esclusi, perche' vanno conservati)",
   not [w for w in ENGW if w in IT_SCAN.lower()], [w for w in ENGW if w in IT_SCAN.lower()])
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
ck('i nomi restano invariati (Anna Fangvin, Beyond the Hyperdrive, Kimek, Arach, Saryd)',
   not [n for n in NAMES if n in EN_ALL and n not in IT_ALL],
   [n for n in NAMES if n in EN_ALL and n not in IT_ALL])
ck('«Arach Houses» -> «Case Arach» (istituzione), come «our Houses» -> «le nostre Case» in L209',
   'Arach Houses' in EN_ALL and 'Case Arach' in IT_ALL and 'Houses' not in IT_ALL)
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
lines, wrong = [], []
for w, n in WINDOWS:
    d = json.load(open(os.path.join(ED, w, 'translation.json'), encoding='utf-8'))['units']
    got = [u['line'] for u in d if u['path'] == PATH]
    if len(got) != n:
        wrong.append((w, n, len(got)))
    lines += got
dbl = [r[0] for r in db.execute('select line from units where path=? order by line', (PATH,))]
ck('FILE CHIUSO: 112/112 righe distinte, tutte quelle del DB, nessun buco',
   not wrong and sorted(lines) == dbl and len(set(lines)) == len(lines) == 112,
   (wrong, len(lines), len(set(lines)), len(dbl)))
st = dict(db.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('le 16 unita sono PENDING (misurato)',
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
