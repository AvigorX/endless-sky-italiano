r"""check.py — L207 (`data/coalition/coalition news.txt`, 17 unita', righe 95-176). Secondo lotto del file.

**Tutte e 17 le unita' sono discorso citato** (2 virgolette ciascuna, 34 in totale) e **tutte sono Saryd** o membri
della Coalizione che ne imitano il parlato: heliarch agent, heliarch candidate, arach tourist, kimek tourist,
saryd tourist, coalition researcher. Il registro del lotto e' quindi **interamente invertito**, con la stessa regola
di L206.

**14 unita' su 17 finiscono con un verbo flesso.** Le tre che non lo fanno (12, 13, 16) **non lo fanno nemmeno nel
sorgente**: la loro ultima frase e' in ordine normale («If only the locals had a more civil sense of attire.»,
«...in the distinct architecture of some buildings here.», «...so much easier to get a hold of complex chemicals...»).
Il controllo lo verifica invece di pretendere l'inversione ovunque.

**Nomi**: `Aulori`, `Ring of Wisdom`, `Saryd Traveler`, `Arachi`, `longcow` restano invariati. `consul` resta
prestito latino per non confonderlo con «console»; `arcology` diventa «arcologia».
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
VERB_FINAL = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 14, 15, 17]
NOT_VERB_FINAL = [12, 13, 16]
NAMES = ('Aulori', 'Ring of Wisdom', 'Saryd Traveler', 'Arachi', 'longcow', 'Saryd', 'Heliarch', 'Kimek')
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


def tail(i):
    w = WORDS.findall(by[i]['italian'].rstrip('."!?'))
    return w[-1] if w else ''


ck("unita' tradotte 17/17", len(cov) == 17 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 17 NEWS', KINDS == {'NEWS': 17}, dict(KINDS))
ck('ZERO VALUE, TEXT, DIALOG, UI_LABEL (asserzioni vuote scritte)',
   [u['idx'] for u in units if u['kind'] != 'NEWS'] == [])
ck('6 contesti: agent 1, candidate 3, arach tourist 3, kimek tourist 3, saryd tourist 3, researcher 4',
   dict(CTX) == {'heliarch agent': 1, 'heliarch candidate': 3, 'arach tourist': 3, 'kimek tourist': 3,
                 'saryd tourist': 3, 'coalition researcher': 4}, dict(CTX))
ck('righe 95 e 176 (prima e ultima del lotto)',
   (cov[0]['line'], cov[-1]['line']) == (95, 176), (cov[0]['line'], cov[-1]['line']))
ck('ZERO segnaposto e ZERO tab in entrambe le lingue (asserzioni vuote scritte)',
   EN_T == 0 == IT_T and '<' not in IT_ALL and '<' not in EN_ALL
   and [v['idx'] for v in cov if TAB in v['english'] or TAB in v['italian']] == [])
ck('TUTTE le 17 unita\' sono citate: 34 virgolette, 2 per unita\'',
   EN_Q == 34 == IT_Q and all(v['english'].count(QUOTE) == 2 == v['italian'].count(QUOTE) for v in cov),
   (EN_Q, IT_Q))
ck('virgolette iniziale e finale coerenti con il sorgente',
   not [v['idx'] for v in cov
        if v['english'].startswith(QUOTE) != v['italian'].startswith(QUOTE)
        or v['english'].endswith(QUOTE) != v['italian'].endswith(QUOTE)])
ck("apici: 4 inglesi (unita' 4, 7, 11, 17) e 4 italiani (unita' 7, 10, 12, 13)",
   EN_A == 4 == IT_A
   and [v['idx'] for v in cov if APOS in v['english']] == [4, 7, 11, 17]
   and [v['idx'] for v in cov if APOS in v['italian']] == [7, 10, 12, 13], (EN_A, IT_A))
ck('REGISTRO SARYD: 14 unita\' su 17 finiscono con un verbo flesso',
   [i for i in sorted(by) if tail(i) in ('facciamo', 'sono', 'hanno', 'essere', 'ha', 'riesce', 'avuto',
                                        'riesco', 'ho', 'è')] == VERB_FINAL,
   [i for i in sorted(by) if tail(i) in ('facciamo', 'sono', 'hanno', 'essere', 'ha', 'riesce', 'avuto',
                                         'riesco', 'ho', 'è')])
ck('le tre unita\' che non finiscono con un verbo non lo fanno nemmeno nel sorgente',
   [tail(i) for i in NOT_VERB_FINAL] == ['civile', 'qui', 'complesse'])
ck('nessuna cortesia «Lei»: l\'unita\' 14 usa «ti dispiacerebbe»',
   'ti dispiacerebbe' in by[14]['italian'] and 'Scusi' not in IT_ALL)
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
ck('i nomi restano invariati (Aulori, Ring of Wisdom, Saryd Traveler, Arachi, longcow...)',
   not [n for n in NAMES if n in EN_ALL and n not in IT_ALL],
   [n for n in NAMES if n in EN_ALL and n not in IT_ALL])
ck('«arcology» tradotto in «arcologia»; «consul» resta prestito (non «console»)',
   'arcologia' in IT_ALL and 'consul Aulori' in IT_ALL and 'console Aulori' not in IT_ALL)
c = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
st = dict(c.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('tutte le 17 unita sono PENDING (misurato)',
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
