r"""check.py — L210 (`data/coalition/coalition news.txt`, 19 unita', righe 309-400). Quinto lotto del file.

**19 `NEWS`**, tutte citazioni (38 virgolette, 2 per unita'). Cinque contesti: vendor 2, civilian expeditions past 5,
heliarch expeditions past 5, coalition games people 6, coalition games planet heliarch 1.

**Il lotto entra nei Giochi della Coalizione** (`Coalition Games` → «Giochi della Coalizione», scelta di L206) e chiude
il filone della spedizione dell'ispettrice **Sedlitaris**, promossa *arbiter*.

**Termini nuovi e dichiarati**: `arbiter` resta prestito latino (come `magister` e `consul`); `consuls` al plurale
diventa «consoli»; `tribune` diventa «tribuno»; `hedgelion` resta invariato.

**Registro**: 18 unita' su 19 chiudono con un verbo flesso. L'unica eccezione e' l'unita' 1, che chiude con «acquisto»
esattamente come il sorgente chiude con *purchase*.
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
VERB_FINAL = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
NAMES = ('hedgelion', 'Arachi', 'Heliarch', 'Saryd', 'Sedlitaris', 'arbiter')
VEND = ('ho', 'essere', 'è', 'chiedo', 'fatto', 'stati', 'aspettavano', 'hanno', 'abbiamo',
        'sta', 'ero', 'riuscito', 'farò')
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
ck('5 contesti con forma 1, 2, 5, 5, 6 (games planet 1, vendor 2, due spedizioni da 5, games people 6)',
   len(CTX) == 5 and sorted(CTX.values()) == [1, 2, 5, 5, 6], dict(CTX))
ck('righe 309 e 400 (prima e ultima del lotto)',
   (cov[0]['line'], cov[-1]['line']) == (309, 400), (cov[0]['line'], cov[-1]['line']))
ck('ZERO segnaposto e ZERO tab in entrambe le lingue (asserzioni vuote scritte)',
   EN_T == 0 == IT_T and '<' not in IT_ALL and '<' not in EN_ALL
   and [v['idx'] for v in cov if TAB in v['english'] or TAB in v['italian']] == [])
ck('38 virgolette, 2 per unita\' in tutte e 19, e tutte citano (aperte e chiuse)',
   EN_Q == 38 == IT_Q and all(v['english'].count(QUOTE) == 2 == v['italian'].count(QUOTE) for v in cov)
   and all(v['italian'].startswith(QUOTE) and v['italian'].endswith(QUOTE) for v in cov), (EN_Q, IT_Q))
ck("apici: 4 inglesi (unita' 9, 10, 11) e 24 italiani (elisione diffusa: dall'esterno, quell'ispettrice, l'uno...)",
   EN_A == 4 and IT_A == 24
   and [v['idx'] for v in cov if APOS in v['english']] == [9, 10, 11]
   and [v['idx'] for v in cov if APOS in v['italian']] == [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 18, 19],
   (EN_A, IT_A))
ck("le virgolette singole di 'spedizione' (unita' 9) sono conservate, due per lato",
   "'spedizione'" in by[9]['italian'] and "'expedition,'" in by[9]['english']
   and by[9]['italian'].count(APOS) == 2 == by[9]['english'].count(APOS))
ck('REGISTRO SARYD: 18 unita\' su 19 chiudono con un verbo flesso',
   [i for i in sorted(by) if tail(i) in VEND] == VERB_FINAL,
   [i for i in sorted(by) if tail(i) in VEND])
ck("l'unica eccezione e' l'unita' 1, che chiude con «acquisto» come il sorgente chiude con «purchase»",
   [i for i in sorted(by) if tail(i) not in VEND] == [1]
   and by[1]['italian'].rstrip(QUOTE + '.').endswith('acquisto')
   and by[1]['english'].rstrip(QUOTE + '.').endswith('purchase'))
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
ck('i nomi restano invariati (hedgelion, Arachi, Heliarch, Saryd, Sedlitaris, arbiter)',
   not [n for n in NAMES if n in EN_ALL and n not in IT_ALL],
   [n for n in NAMES if n in EN_ALL and n not in IT_ALL])
ck('«Coalition Games» resta tradotto: «Giochi della Coalizione», stesso numero di occorrenze',
   EN_ALL.count('Coalition Games') == IT_ALL.count('Giochi della Coalizione') > 0
   and 'Coalition Games' not in IT_ALL,
   (EN_ALL.count('Coalition Games'), IT_ALL.count('Giochi della Coalizione')))
ck('«consuls» -> «consoli» e «tribune» -> «tribuno» (titoli comuni, non nomi propri)',
   'consoli' in IT_ALL and 'tribuno' in IT_ALL and 'consuls' not in IT_ALL and 'tribune' not in IT_ALL)
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
