r"""check.py — L200 (`data/hai/hai jobs.txt`, 23 unita', righe 1753-2067). **QUINTO E ULTIMO LOTTO: CHIUDE IL FILE.**

Una sola famiglia numerata, `Superstitious Hai [1]…[12]`: **11 `VALUE`** identici (`Superstitious Hai to <planet>`)
e **12 `DESCRIPTION`**, nessun `DIALOG`, nessun `TEXT`. **Zero tab, zero virgolette, zero apici**: tre asserzioni
vuote scritte comunque. **57 segnaposto su 5 simboli**.

**Struttura da verificare come relazione**: le `DESCRIPTION` `[1]…[6]` portano in coda la frase sul keystone
(«Ha/Hanno chiesto che sulla propria nave sia installata una chiave di volta Hai autentica.»), le `[7]…[12]` sono
**le stesse senza quella frase**. Il controllo toglie la frase dalle prime e le confronta con le seconde, una per una.

**Terminologia**: `keystone` → **chiave di volta** (la resa usata nel lavoro che introduce l'oggetto, `Fetching
keystones` → «Recuperare le chiavi di volta»). In staging convive con «pietra chiave»: la scelta e' dichiarata e il
controllo pretende che in questo lotto ci sia **una sola** delle due.
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
NON_VALUE = ' '.join(v['italian'] for v in cov if v['kind'] != 'VALUE')
IT_ALL = ' '.join(v['italian'] for v in cov)
EN_Q = sum(v['english'].count(QUOTE) for v in cov)
IT_Q = sum(v['italian'].count(QUOTE) for v in cov)
EN_A = sum(v['english'].count(APOS) for v in cov)
IT_A = sum(v['italian'].count(APOS) for v in cov)
KINDS = collections.Counter(u['kind'] for u in units)
S1 = ' Ha chiesto che sulla propria nave sia installata una chiave di volta Hai autentica.'
S2 = ' Hanno chiesto che sulla propria nave sia installata una chiave di volta Hai autentica.'
PAIRS = [(1, 13), (3, 15), (5, 17), (7, 19), (9, 21), (11, 23)]
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


def strip_key(s):
    return s.replace(S1, '').replace(S2, '')


ck("unita' tradotte 23/23", len(cov) == 23 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 11 VALUE, 12 DESCRIPTION, ZERO DIALOG (asserzione scritta)',
   KINDS == {'VALUE': 11, 'DESCRIPTION': 12}, dict(KINDS))
ck('ZERO UI_LABEL, ZERO tab, ZERO TEXT (asserzioni vuote scritte)',
   [u['idx'] for u in units if u['kind'] == 'UI_LABEL'] == []
   and [u['idx'] for u in units if u['kind'] == 'TEXT'] == []
   and [u['idx'] for u in units if u['english'].startswith(TAB)] == []
   and [v['idx'] for v in cov if v['italian'].startswith(TAB)] == [])
ctx = [u['context'].replace('mission:', '') for u in units]
ck('12 contesti: la famiglia numerata Superstitious Hai [1]…[12], in ordine di prima occorrenza',
   len(set(ctx)) == 12
   and list(dict.fromkeys(ctx)) == ['Superstitious Hai [%d]' % i for i in range(1, 13)],
   list(dict.fromkeys(ctx)))
ck('righe 1753 e 2067 (prima e ultima del lotto)',
   (cov[0]['line'], cov[-1]['line']) == (1753, 2067), (cov[0]['line'], cov[-1]['line']))
EN_T = collections.Counter(t for u in units for t in TAGS.findall(u['english']))
IT_T = collections.Counter(t for v in cov for t in TAGS.findall(v['italian']))
ck('57 segnaposto su 5 simboli (payment 12, destination 12, date 12, planet 11, bunks 10)',
   sum(EN_T.values()) == 57 and EN_T == {'<payment>': 12, '<destination>': 12, '<date>': 12,
                                         '<planet>': 11, '<bunks>': 10} and EN_T == IT_T,
   (sum(EN_T.values()), dict(EN_T)))
bad_tags = [(v['idx'], sorted(TAGS.findall(v['english'])), sorted(TAGS.findall(v['italian'])))
            for v in cov
            if collections.Counter(TAGS.findall(v['english'])) != collections.Counter(TAGS.findall(v['italian']))]
ck('nessuna unita\' perde, duplica o sposta un segnaposto', not bad_tags, bad_tags)
ck('11 VALUE, tutti identici all\'inglese',
   [v['idx'] for v in cov if v['kind'] == 'VALUE'] == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]
   and all(v['italian'] == v['english'] == 'Superstitious Hai to <planet>'
           for v in cov if v['kind'] == 'VALUE'))
ck('12 DESCRIPTION tradotte (nessuna lasciata in inglese)',
   [v['idx'] for v in cov if v['kind'] == 'DESCRIPTION'] == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
   and all(v['italian'] != v['english'] for v in cov if v['kind'] == 'DESCRIPTION'))
ck('zero virgolette e zero apici in entrambe le lingue (asserzioni vuote scritte)',
   EN_Q == 0 == IT_Q and EN_A == 0 == IT_A, (EN_Q, IT_Q, EN_A, IT_A))
ck('nessun caporale e nessun carattere tipografico',
   not [v['idx'] for v in cov if any(c in v['italian'] for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026')])
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' you ', ' to the ', ' will be ',
        ' is ', ' are ', ' from the ', ' its ', ' it is ', ' such as ', ' rather than ', ' for a ')
ck('nessun residuo inglese fuori dai VALUE (che restano inglesi per convenzione)',
   not [w for w in ENGW if w in NON_VALUE.lower()], [w for w in ENGW if w in NON_VALUE.lower()])
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
ck('le sei coppie con/senza keystone: la seconda e\' la prima meno la frase finale (1-13, 3-15, 5-17, 7-19, 9-21, 11-23)',
   all(strip_key(by[a]['italian']) == by[b]['italian'] for a, b in PAIRS),
   [(a, b, strip_key(by[a]['italian']) == by[b]['italian']) for a, b in PAIRS])
ck("le sei unita' [1]…[6] portano la frase sul keystone; le [7]…[12] NO (asserzione incrociata)",
   all(S1 in by[i]['italian'] or S2 in by[i]['italian'] for i in (1, 3, 5, 7, 9, 11))
   and not any(S1 in by[i]['italian'] or S2 in by[i]['italian'] for i in (13, 15, 17, 19, 21, 23)))
ck('accordo del verbo: «Ha chiesto» per matriarca e anziano, «Hanno chiesto» per famiglie e gruppi',
   S1 in by[1]['italian'] and S1 in by[5]['italian']
   and all(S2 in by[i]['italian'] for i in (3, 7, 9, 11)))
ck('termine unico del lotto: «chiave di volta» 18 volte (2 nelle unita\' con frase, 1 nelle altre), mai «pietra chiave»',
   IT_ALL.count('chiave di volta') == 18 and 'pietra chiave' not in IT_ALL,
   (IT_ALL.count('chiave di volta'), IT_ALL.count('pietra chiave')))
ck('i sei soggetti sono distinti: sei prefissi diversi prima di «pagherà»',
   len({by[i]['italian'].split(' pagherà ')[0] for i in (1, 3, 5, 7, 9, 11)}) == 6,
   sorted({by[i]['italian'].split(' pagherà ')[0] for i in (1, 3, 5, 7, 9, 11)}))
ck('«casa di riposo» compare solo nelle unita\' dell\'anziano (5, 17)',
   'casa di riposo' in by[5]['italian'] and 'casa di riposo' in by[17]['italian']
   and not any('casa di riposo' in v['italian'] for v in cov if v['idx'] not in (5, 17)))
c = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
st = dict(c.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('tutte le 23 unita sono PENDING (misurato)',
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
