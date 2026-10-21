r"""check.py — L240 (`data/avgi/avgi jobs.txt`, 40 unita', righe 684-1156). **LOTTO TERMINALE**: chiude il file a 102/102.

20 `VALUE` (dati, invariati) + 20 `DESCRIPTION` (prosa, tradotte) in 20 contesti, **8 formule distinte**:

     6x  Bring <cargo> from <origin> to the <destination> to support the construction of the <destination> ...
     3x  Take these <bunks> doctors ...
     3x  Deliver <cargo> to <destination> by <date> ... pirates ...
     3x  Take these <bunks> Twilight Guards ... shore leave ...
     2x  Bring <cargo> storage media ... update <planet>'s local network ...
     1x  These <bunks> Twilight Guardsmen need transportation ...
     1x  These <bunks> Twilight Guard officers ...
     1x  These <bunks> Twilight Guard flag officers ...

**Due segnaposto nuovi rispetto a L239**: `<origin>` (6) e il `the` **dentro** un `VALUE` (`Construction materials to
the <planet>`), che resta **identico** perche' e' un dato.

**`<planet>'s`**: gli **unici due apostrofi** del lotto sono il possessivo inglese delle righe 988 e 1009. In italiano il
possessivo non esiste («la rete locale di <planet>») e gli apostrofi scendono a **zero**: la differenza e' dichiarata e
asserita, non nascosta nel totale.
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
PATH = 'data/avgi/avgi jobs.txt'
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
VAL = [v for v in cov if v['kind'] == 'VALUE']
DES = [v for v in cov if v['kind'] == 'DESCRIPTION']
FAM = collections.defaultdict(list)
for v in DES:
    FAM[v['english']].append(v['idx'])
FAM_V = collections.defaultdict(list)
for v in VAL:
    FAM_V[v['english']].append(v['idx'])
TOK_EN = collections.Counter(t for v in cov for t in TAG.findall(v['english']))
TOK_IT = collections.Counter(t for v in cov for t in TAG.findall(v['italian']))
PROSA = ' '.join(v['italian'] for v in DES)
EN_A = [(v['idx'], v['english'].count(APOS)) for v in cov if APOS in v['english']]
IT_A = [(v['idx'], v['italian'].count(APOS)) for v in cov if APOS in v['italian']]
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 40/40", len(cov) == 40 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna unita\' vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 20 VALUE + 20 DESCRIPTION', collections.Counter(u['kind'] for u in units) ==
   {'VALUE': 20, 'DESCRIPTION': 20}, dict(collections.Counter(u['kind'] for u in units)))
ck('20 contesti, due unita\' ciascuno',
   len({u['context'] for u in units}) == 20 and set(collections.Counter(u['context'] for u in units).values()) == {2})
ck('righe 684 e 1156 (prima e ultima del lotto, ultima del FILE)',
   (cov[0]['line'], cov[-1]['line']) == (684, 1156), (cov[0]['line'], cov[-1]['line']))
ck('ZERO tab e ZERO virgolette in inglese e in italiano (due asserzioni negative scritte)',
   sum(v['english'].count(TAB) for v in cov) == 0 == sum(v['italian'].count(TAB) for v in cov)
   and sum(v['english'].count(QUOTE) for v in cov) == 0 == sum(v['italian'].count(QUOTE) for v in cov))
ck("i 20 VALUE sono IDENTICI all'inglese, per indice (il `the` compreso: e' un dato)",
   all(v['italian'] == v['english'] for v in VAL) and len(VAL) == 20,
   [v['idx'] for v in VAL if v['italian'] != v['english']])
ck("il `the` dentro i VALUE e' conservato in 6 unita'",
   sum(1 for v in VAL if ' to the <planet>' in v['italian']) == 6)
ck('le 20 DESCRIPTION sono TUTTE tradotte (0 identiche)', all(v['italian'] != v['english'] for v in DES))
ck('8 famiglie DESCRIPTION con gli indici attesi',
   sorted((len(v), tuple(v)) for v in FAM.values()) ==
   sorted([(3, (2, 4, 6)), (6, (8, 10, 12, 14, 16, 18)), (3, (20, 22, 24)), (2, (26, 28)),
           (1, (30,)), (1, (32,)), (1, (34,)), (3, (36, 38, 40))]),
   sorted((len(v), tuple(v)) for v in FAM.values()))
ck('una sola resa per famiglia',
   all(len({v['italian'] for v in DES if v['english'] == k}) == 1 for k in FAM))
ck('9 famiglie VALUE, tutte invariate',
   sorted((len(v), tuple(v)) for v in FAM_V.values()) ==
   sorted([(3, (1, 3, 5)), (3, (7, 9, 11)), (3, (13, 15, 17)), (3, (19, 21, 23)),
           (2, (25, 27)), (1, (29,)), (1, (31,)), (1, (33,)), (3, (35, 37, 39))]),
   sorted((len(v), tuple(v)) for v in FAM_V.values()))
ck('segnaposto: 99 su 7 simboli, parita\' per simbolo',
   TOK_EN == TOK_IT == {'<destination>': 26, '<planet>': 22, '<payment>': 20, '<cargo>': 11,
                        '<bunks>': 9, '<origin>': 6, '<date>': 5}, (dict(TOK_EN), dict(TOK_IT)))
ck("segnaposto: ordine identico in ogni unita'",
   all(tuple(TAG.findall(v['english'])) == tuple(TAG.findall(v['italian'])) for v in cov),
   [(v['idx'], TAG.findall(v['english']), TAG.findall(v['italian'])) for v in cov
    if TAG.findall(v['english']) != TAG.findall(v['italian'])])
ck("`<origin>` non si scambia con `<destination>`: dove ci sono entrambi, la partenza viene prima",
   not [v['idx'] for v in cov
        if '<origin>' in TAG.findall(v['english'])
        and TAG.findall(v['italian']).index('<origin>') >= TAG.findall(v['italian']).index('<destination>')])
ck("nessuna unita' con segnaposto solo in una lingua",
   [v['idx'] for v in cov if bool(TAG.findall(v['english'])) != bool(TAG.findall(v['italian']))] == [])
ck("apici: 2 in inglese (il possessivo `<planet>'s` delle righe 988 e 1009) e 0 in italiano",
   sum(n for _, n in EN_A) == 2 and [i for i, _ in EN_A] == [26, 28] and IT_A == [],
   (EN_A, IT_A))
ck("i quattro gradi dei Twilight Guard: nome della fazione invariato, grado in italiano",
   'membri della Twilight Guard' in PROSA and 'ufficiali della Twilight Guard' in PROSA
   and 'ufficiali superiori della Twilight Guard' in PROSA and 'Guardie' in PROSA
   and 'Guardsmen' not in PROSA and 'flag officers' not in PROSA)
ck('nessun residuo inglese di struttura (the, and, with, for, these, from, need)',
   not [w for w in (' the ', ' and ', ' with ', ' for ', ' these ', ' from ', ' need ')
        if w in PROSA.lower()],
   [w for w in (' the ', ' and ', ' with ', ' for ', ' these ', ' from ', ' need ')
    if w in PROSA.lower()])
ck('registro: nessun «Lei» e nessuna cortesia',
   not re.search(r'\bLei\b|\bSuo\b|\bSua\b|mi scusi', ' '.join(v['italian'] for v in cov)))
ck('nessun caporale e nessun carattere tipografico',
   not [v['idx'] for v in cov if any(c in v['italian'] for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026')])
rs = [v['ratio'] for v in cov]
ck('rapporto nel gate 0,55-1,90 (0,90-1,14; 470 -> 476 parole)',
   0.55 < min(rs) and max(rs) < 1.90, '%.2f - %.2f' % (min(rs), max(rs)))
ACC = re.compile(r"\b(e|piu|perche|cosi|gia|puo|cioe|percio)'(?![a-z])", re.I)
bad = [(v['idx'], ACC.search(v['italian']).group(0)) for v in cov if ACC.search(v['italian'])]
ck("tipografia (accenti veri, nessun apostrofo al posto dell'accento)", not bad, bad)
nonlat = [v['idx'] for v in cov for c in v['italian'] if ord(c) > 127 and not 0x00C0 <= ord(c) <= 0x024F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio',
   not [v['idx'] for v in cov if v['italian'] != v['italian'].rstrip() or '  ' in v['italian']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("62 unita' tradotte prima della 684 (L239)",
   db.execute('select count(*) from units where path=? and line<684', (PATH,)).fetchone()[0] == 62)
ck("ZERO unita' dopo la 1156: il lotto CHIUDE il file",
   db.execute('select count(*) from units where path=? and line>1156', (PATH,)).fetchone()[0] == 0)
ck('il file intero: 102 unita, righe 20 - 1156',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (102, 20, 1156))
ck('62 + 40 = 102 = unita\' del file', 62 + 40 == 102)
st = dict(db.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('le 40 unita sono PENDING (misurato)',
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
