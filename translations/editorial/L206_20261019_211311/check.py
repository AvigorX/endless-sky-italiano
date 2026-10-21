r"""check.py — L206 (`data/coalition/coalition news.txt`, 20 unita', righe 28-94). Primo lotto del file.

**Primo lotto di tipo `NEWS`** della campagna: venti voci di notiziario, tutte `NEWS`, quattro contesti
(`heliarch news` 1, `longcow rancher` 5, `kimek farmer` 4, `heliarch agent` 10).

**La decisione del lotto e' il registro.** I Saryd parlano con l'ordine delle parole invertito: e' una
caratterizzazione, non un refuso. Regola applicata: **narrazione in italiano naturale** (unita' 1 e 10),
**discorso Saryd con l'inversione riprodotta** (tutte le altre). Il marcatore si misura: le unita' citate
finiscono con un **verbo flesso** («un duro lavoro e'», «a tua disposizione sono», «impegnati siamo»), mentre la
narrazione no.

**40 virgolette** (2 per unita', 20 unita'), **5 apici inglesi / 9 italiani**, zero segnaposto, zero tab.
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
VERBS = ('dovresti', 'sono', 'devi', 'siamo', 'sto', 'torno', 'trovo', 'ho')
NAMES = ('Heliarch', 'longcow', 'Saryd', 'Kimek', 'Arach', 'Punisher', 'Stalker', 'magister')
NARRATION = [1, 10]
QUOTED = [i for i in sorted(by) if i not in NARRATION]
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


def tail(i):
    w = WORDS.findall(by[i]['italian'].rstrip('."!?'))
    return w[-1] if w else ''


ck("unita' tradotte 20/20", len(cov) == 20 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 20 NEWS (primo lotto di questo tipo nella campagna)', KINDS == {'NEWS': 20}, dict(KINDS))
ck('ZERO VALUE, TEXT, DIALOG, UI_LABEL (asserzioni vuote scritte)',
   [u['idx'] for u in units if u['kind'] != 'NEWS'] == [])
ck('4 contesti: heliarch news 1, longcow rancher 5, kimek farmer 4, heliarch agent 10',
   dict(CTX) == {'heliarch news': 1, 'longcow rancher': 5, 'kimek farmer': 4, 'heliarch agent': 10}, dict(CTX))
ck('righe 28 e 94 (prima e ultima del lotto)',
   (cov[0]['line'], cov[-1]['line']) == (28, 94), (cov[0]['line'], cov[-1]['line']))
ck('ZERO segnaposto e ZERO tab in entrambe le lingue (asserzioni vuote scritte)',
   EN_T == 0 == IT_T and '<' not in IT_ALL and '<' not in EN_ALL
   and [v['idx'] for v in cov if TAB in v['english'] or TAB in v['italian']] == [])
ck('40 virgolette in entrambe le lingue, 2 per unita\' in TUTTE le 20 unita\'',
   EN_Q == 40 == IT_Q and all(v['english'].count(QUOTE) == 2 == v['italian'].count(QUOTE) for v in cov),
   (EN_Q, IT_Q))
ck('virgolette iniziale e finale coerenti con il sorgente (citazione aperta e chiusa)',
   not [v['idx'] for v in cov
        if v['english'].startswith(QUOTE) != v['italian'].startswith(QUOTE)
        or v['english'].endswith(QUOTE) != v['italian'].endswith(QUOTE)])
ck("apici: 5 inglesi (unita' 9, 10, 18) e 9 italiani (unita' 1, 6, 7, 9, 10, 17)",
   EN_A == 5 and IT_A == 9
   and [v['idx'] for v in cov if APOS in v['english']] == [9, 10, 18]
   and [v['idx'] for v in cov if APOS in v['italian']] == [1, 6, 7, 9, 10, 17], (EN_A, IT_A))
ck('REGISTRO SARYD: 9 unita\' citate finiscono con un verbo flesso (inversione riprodotta)',
   [i for i in QUOTED if tail(i) in VERBS] == [3, 12, 13, 14, 15, 16, 17, 18, 20],
   [i for i in QUOTED if tail(i) in VERBS])
ck('REGISTRO SARYD: la narrazione (unita\' 1 e 10) NON finisce con un verbo',
   [i for i in NARRATION if tail(i) in VERBS] == [], [tail(1), tail(10)])
ck('i tre parlanti sono distinguibili: longcow rancher, kimek farmer, heliarch agent',
   CTX['longcow rancher'] == 5 and CTX['kimek farmer'] == 4 and CTX['heliarch agent'] == 10)
ck('nessun caporale e nessun carattere tipografico',
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
ck('i nomi di fazione, specie e prodotto restano invariati (Heliarch, Saryd, Kimek, Arach, Punisher...)',
   not [n for n in NAMES if n in EN_ALL and n not in IT_ALL],
   [n for n in NAMES if n in EN_ALL and n not in IT_ALL])
ck('«Coalition Games» tradotto in «Giochi della Coalizione»: nome comune di evento, non nome di prodotto',
   'Coalition Games' in EN_ALL and 'Giochi della Coalizione' in IT_ALL and 'Coalition Games' not in IT_ALL)
ck('«longcow» resta invariato al singolare e al plurale (nessun «longcowghi»)',
   'longcow' in IT_ALL and 'longcowgh' not in IT_ALL and IT_ALL.count('longcow') == EN_ALL.count('longcow'),
   (IT_ALL.count('longcow'), EN_ALL.count('longcow')))
c = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
st = dict(c.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('tutte le 20 unita sono PENDING (misurato)',
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
