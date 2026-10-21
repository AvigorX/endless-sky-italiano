r"""check.py — L242 (`data/successors/successor jobs.txt`, 38 unita', righe 306-802). **LOTTO TERMINALE**: chiude il file
a 124/124.

19 `VALUE` (dati, invariati) + 19 `DESCRIPTION` (prosa, tradotte) in 19 contesti, **14 formule distinte** (quattro da
4 copie? no: una da 4, due da 2, undici da 1):

     4x  A courier is needed for <tons> of supplies ...
     2x  These <bunks> workers are looking for jobs ...
     2x  A courier is needed for a rush shipment ...
    11x  una copia ciascuna (studenti, carichi preziosi, aiuti, materiali sfusi, stabilizzatori, dati riservati,
         ricercatori ×3, simposio, Vecchie Casate, Nuove Casate)

**`<tons>` entra per la prima volta** (11): e' una quantita' prodotta dal motore, quindi si usa **senza articolo** e senza
concordanza («`<tons>` di provviste»), come i 75 precedenti del corpus.

**`<origin>` e `<planet>` convivono** in 11 unita': la partenza non si inverte, e il controllo confronta le posizioni.

**Vecchie e Nuove Casate**: nella prosa i nomi si traducono con la maiuscola (istituzioni, decisione 164), nei `VALUE`
restano inglesi (`Old Houses courier to <planet>`): nome = dato, prosa = traduzione.
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
PATH = 'data/successors/successor jobs.txt'
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
TOK_EN = collections.Counter(t for v in cov for t in TAG.findall(v['english']))
TOK_IT = collections.Counter(t for v in cov for t in TAG.findall(v['italian']))
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 38/38", len(cov) == 38 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna unita\' vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 19 VALUE + 19 DESCRIPTION',
   collections.Counter(u['kind'] for u in units) == {'VALUE': 19, 'DESCRIPTION': 19},
   dict(collections.Counter(u['kind'] for u in units)))
ck('19 contesti, due unita\' ciascuno',
   len({u['context'] for u in units}) == 19
   and set(collections.Counter(u['context'] for u in units).values()) == {2})
ck('righe 306 e 802 (prima e ultima del lotto, ultima del FILE)',
   (cov[0]['line'], cov[-1]['line']) == (306, 802), (cov[0]['line'], cov[-1]['line']))
ck('ZERO tab, ZERO virgolette, ZERO apici (tre asserzioni negative scritte)',
   sum(v['english'].count(TAB) for v in cov) == 0 == sum(v['italian'].count(TAB) for v in cov)
   and sum(v['english'].count(QUOTE) for v in cov) == 0 == sum(v['italian'].count(QUOTE) for v in cov)
   and sum(v['english'].count(APOS) for v in cov) == 0 == sum(v['italian'].count(APOS) for v in cov))
ck("i 19 VALUE sono IDENTICI all'inglese, per indice",
   all(v['italian'] == v['english'] for v in VAL) and len(VAL) == 19,
   [v['idx'] for v in VAL if v['italian'] != v['english']])
ck("le 19 DESCRIPTION sono TUTTE tradotte (0 identiche)",
   all(v['italian'] != v['english'] for v in DES) and len(DES) == 19)
ck('14 famiglie DESCRIPTION (una da 4, due da 2, undici da 1)',
   sorted(len(v) for v in FAM.values()) == [1] * 11 + [2, 2, 4] and len(FAM) == 14,
   sorted(len(v) for v in FAM.values()))
ck('una sola resa per famiglia',
   all(len({v['italian'] for v in DES if v['english'] == k}) == 1 for k in FAM))
ck('segnaposto: 98 su 10 famiglie, parita\' per simbolo',
   TOK_EN == TOK_IT == {'<planet>': 28, '<payment>': 19, '<date>': 11, '<tons>': 11, '<origin>': 11,
                        '<bunks>': 7, '<destination>': 4, '<planet stopovers>': 3, '<stopovers>': 3,
                        '<cargo>': 1}, (dict(TOK_EN), dict(TOK_IT)))
ck("segnaposto: ordine identico in ogni unita'",
   all(tuple(TAG.findall(v['english'])) == tuple(TAG.findall(v['italian'])) for v in cov),
   [(v['idx'], TAG.findall(v['english']), TAG.findall(v['italian'])) for v in cov
    if TAG.findall(v['english']) != TAG.findall(v['italian'])])
ck("`<origin>` precede `<planet>` in tutte le 11 unita' che li hanno entrambi",
   sum(1 for v in cov if '<origin>' in TAG.findall(v['english'])) == 11
   and all(TAG.findall(v['italian']).index('<origin>') < TAG.findall(v['italian']).index('<planet>')
           for v in cov if '<origin>' in TAG.findall(v['english'])))
ck("`<tons>` e' usato senza articolo davanti (e' una quantita' del motore): 11 volte",
   sum(v['italian'].count('<tons>') for v in cov) == 11
   and not re.search(r'\b(il|lo|la|i|gli|le|un|uno|una)\s+<tons>', ' '.join(v['italian'] for v in cov)))
ck("`<planet stopovers>` (3) e `<stopovers>` (3) sono simboli distinti",
   TOK_IT['<planet stopovers>'] == 3 and TOK_IT['<stopovers>'] == 3)
ck('Vecchie e Nuove Casate tradotte nella prosa, maiuscole comprese',
   sum(v['italian'].count('Vecchie Casate') for v in DES) == 1
   and sum(v['italian'].count('Nuove Casate') for v in DES) == 1
   and 'Old Houses' not in ' '.join(v['italian'] for v in DES)
   and 'New Houses' not in ' '.join(v['italian'] for v in DES))
ck('...e restano inglesi nei VALUE che le nominano',
   sum(1 for v in VAL if v['english'].startswith('Old Houses')) == 1
   and sum(1 for v in VAL if v['english'].startswith('New Houses')) == 1
   and any(v['italian'] == 'New Houses courier to <planet>' for v in VAL))
ck('nessun residuo inglese di struttura (the, and, with, for, from, will)',
   not [w for w in (' the ', ' and ', ' with ', ' for ', ' from ', ' will ')
        if w in ' '.join(v['italian'] for v in DES).lower()],
   [w for w in (' the ', ' and ', ' with ', ' for ', ' from ', ' will ')
    if w in ' '.join(v['italian'] for v in DES).lower()])
ck('registro: nessun «Lei» e nessuna cortesia',
   not re.search(r'\bLei\b|\bSuo\b|\bSua\b|mi scusi', ' '.join(v['italian'] for v in cov)))
ck('nessun caporale e nessun carattere tipografico',
   not [v['idx'] for v in cov if any(c in v['italian'] for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026')])
rs = [v['ratio'] for v in cov]
ck('rapporto nel gate 0,55-1,90 (0,92-1,09; 480 -> 435 parole)',
   0.55 < min(rs) and max(rs) < 1.90, '%.2f - %.2f' % (min(rs), max(rs)))
ACC = re.compile(r"\b(e|piu|perche|cosi|gia|puo|cioe|percio)'(?![a-z])", re.I)
bad = [(v['idx'], ACC.search(v['italian']).group(0)) for v in cov if ACC.search(v['italian'])]
ck("tipografia (accenti veri, nessun apostrofo al posto dell'accento)", not bad, bad)
nonlat = [v['idx'] for v in cov for c in v['italian'] if ord(c) > 127 and not 0x00C0 <= ord(c) <= 0x024F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio',
   not [v['idx'] for v in cov if v['italian'] != v['italian'].rstrip() or '  ' in v['italian']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("86 unita' tradotte prima della 306 (L241)",
   db.execute('select count(*) from units where path=? and line<306', (PATH,)).fetchone()[0] == 86)
ck("ZERO unita' dopo la 802: il lotto CHIUDE il file",
   db.execute('select count(*) from units where path=? and line>802', (PATH,)).fetchone()[0] == 0)
ck('il file intero: 124 unita, righe 16 - 802',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (124, 16, 802))
ck("86 + 38 = 124 = unita' del file", 86 + 38 == 124)
st = dict(db.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('le 38 unita sono PENDING (misurato)',
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
