r"""check.py — L208 (`data/coalition/coalition news.txt`, 19 unita', righe 177-246). Terzo lotto del file.

**19 `NEWS`**, cinque contesti: researcher (3), researcher yottrite (3), ringworld worker (6), spaceport worker (3),
merchant (4). **38 virgolette** (2 per unita'), **zero tab**, **zero segnaposto**.

**Registro Saryd**: 17 unita' su 19 finiscono con un verbo flesso. Le **due** che non lo fanno sono **esattamente** le
due di narrazione (1 e 12), dove il notiziario descrive la scena invece di citare: e' il marcatore piu' pulito dei tre
lotti della Coalizione, perche' coincide con la distinzione narrazione/discorso.

**Nomi**: `yottrite`, `House Ablomab`, `House Plumtab`, `Runabout`, `Hulk`, `Spindle`, `Saryd`, `Kimek`, `Heliarch`
restano invariati. `Coalition` invece si traduce: «Coalizione».
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
VERB_FINAL = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19]
NARRATION = [1, 12]
NAMES = ('yottrite', 'House Ablomab', 'House Plumtab', 'Runabout', 'Hulk', 'Spindle',
         'Saryd', 'Kimek', 'Heliarch')
VEND = ('era', 'ora', 'essere', 'domando', 'è', 'stato', 'potrei', 'saranno', 'sento', 'sei',
        'aggiungendo', 'cerchiamo', 'potremmo', 'fanno', 'fatto', 'preso', 'dovuto', 'pensato', 'passato',
        'dispiace')
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


def tail(i):
    w = WORDS.findall(by[i]['italian'].rstrip('."!?'))
    return w[-1] if w else ''


ck("unita' tradotte 19/19", len(cov) == 19 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 19 NEWS', KINDS == {'NEWS': 19}, dict(KINDS))
ck('ZERO VALUE, TEXT, DIALOG, UI_LABEL (asserzioni vuote scritte)',
   [u['idx'] for u in units if u['kind'] != 'NEWS'] == [])
ck('5 contesti: researcher 3, yottrite 3, ringworld worker 6, spaceport worker 3, merchant 4',
   dict(CTX) == {'coalition researcher': 3, 'coalition researcher yottrite': 3,
                 'coalition ringworld worker': 6, 'coalition spaceport worker': 3,
                 'coalition merchant': 4}, dict(CTX))
ck('righe 177 e 246 (prima e ultima del lotto)',
   (cov[0]['line'], cov[-1]['line']) == (177, 246), (cov[0]['line'], cov[-1]['line']))
ck('ZERO segnaposto e ZERO tab in entrambe le lingue (asserzioni vuote scritte)',
   EN_T == 0 == IT_T and '<' not in IT_ALL and '<' not in EN_ALL
   and [v['idx'] for v in cov if TAB in v['english'] or TAB in v['italian']] == [])
ck('38 virgolette, 2 per unita\' in tutte e 19',
   EN_Q == 38 == IT_Q and all(v['english'].count(QUOTE) == 2 == v['italian'].count(QUOTE) for v in cov),
   (EN_Q, IT_Q))
ck('virgolette iniziale/finale coerenti (le unita\' 1 e 12 hanno testo prima o dopo la citazione)',
   not [v['idx'] for v in cov
        if v['english'].startswith(QUOTE) != v['italian'].startswith(QUOTE)
        or v['english'].endswith(QUOTE) != v['italian'].endswith(QUOTE)])
ck("apici: 5 inglesi (unita' 9, 16, 17, 19) e 12 italiani (unita' 2, 4, 5, 6, 10, 13, 16, 17, 19)",
   EN_A == 5 and IT_A == 12
   and [v['idx'] for v in cov if APOS in v['english']] == [9, 16, 17, 19]
   and [v['idx'] for v in cov if APOS in v['italian']] == [2, 4, 5, 6, 10, 13, 16, 17, 19], (EN_A, IT_A))
ck("le due virgolette singole di 'trasporto' (unita' 19) sono conservate",
   "'trasporto'" in by[19]['italian'] and "'transport'" in by[19]['english'])
ck('REGISTRO SARYD: 17 unita\' su 19 chiudono con un verbo flesso',
   [i for i in sorted(by) if tail(i) in VEND] == VERB_FINAL,
   [i for i in sorted(by) if tail(i) in VEND])
ck('le due unita\' che NON chiudono con un verbo sono esattamente le due di narrazione (1 e 12)',
   [i for i in sorted(by) if tail(i) not in VEND] == NARRATION,
   [i for i in sorted(by) if tail(i) not in VEND])
ck('le due unita\' di narrazione mescolano racconto e citazione, come nel sorgente',
   by[1]['english'].count(QUOTE) == 2 and not by[1]['english'].startswith(QUOTE)
   and by[12]['english'].count(QUOTE) == 2 and not by[12]['english'].endswith(QUOTE))
ck('nessun caporale e nessun carattere tipografico',
   not [v['idx'] for v in cov if any(c in v['italian'] for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026')])
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' you ', ' to the ', ' will be ',
        ' is ', ' are ', ' from the ', ' its ', ' it is ', ' such as ', ' rather than ', ' for a ', ' that ')
ck('nessun residuo inglese', not [w for w in ENGW if w in IT_ALL.lower()],
   [w for w in ENGW if w in IT_ALL.lower()])
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
ck('i nomi restano invariati (yottrite, House Ablomab/Plumtab, Runabout, Hulk, Spindle...)',
   not [n for n in NAMES if n in EN_ALL and n not in IT_ALL],
   [n for n in NAMES if n in EN_ALL and n not in IT_ALL])
ck('«Coalition» si traduce: «Coalizione» (nome comune di istituzione, non nome proprio)',
   'Coalition' in EN_ALL and 'Coalizione' in IT_ALL and 'Coalition' not in IT_ALL)
c = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
st = dict(c.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('tutte le 19 unita sono PENDING (misurato)',
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
