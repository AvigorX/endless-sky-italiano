r"""check.py — L235 (`data/avgi/avgi news.txt`, 15 unita', righe 197-280). Terzo lotto del file.

**Lotto di composizione, non di prosa.** Le due notizie di questa finestra non sono frasi: sono **pezzi** che il gioco
concatena con `Phrase::Get()` (`source/Phrase.cpp`: `result += ...`, **nessun separatore aggiunto**).

- `avgi safety advisory`: **6 prefissi** (`"Caution. ` … `"Vigilance. `, con la **virgoletta aperta** e **uno spazio
  finale**) × **7 messaggi** (senza virgoletta aperta e con il **punto e la virgoletta chiusa** in coda) = **42 testi**.
- `avgi missing advisory`: il database contiene **solo due unita'** — la virgoletta aperta (riga 230) e il punto finale
  (riga 280) — mentre il `message` del sorgente ha **tredici** blocchi `word` (misurati sul file). Le parole interne (`Convoy`, `reported
  lost`, `the Demilude system`…) **non sono inventariate**: e' la lacuna dell'estrattore, dichiarata nel `review.md`
  §5 e verificata dal `verify.py`, non riparabile da un lotto (`tools/l10n.py` e `state.db` sono protetti).

**Le due unita' di punteggiatura sono identiche per necessita'** (`"` e `.`): stanno in `ID_OK` con un controllo
dedicato, e «tutte tradotte» le esclude per indice, non per deroga generale (decisione 55).

**Lo spazio finale e' struttura**: i sei prefissi finiscono con **uno** spazio, in inglese e in italiano. Il controllo
generale «nessuno spazio finale» e' **rovesciato** per queste unita' — ed e' scritto come eccezione nominata, non
allentato (L129 docet).
"""
import collections
import json
import os
import re
import sqlite3

TAB = chr(9)
QUOTE = chr(34)
TAG = re.compile(r'<[^<>]+>')
HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
PATH = 'data/avgi/avgi news.txt'
PREFIX = list(range(1, 7))
MSG = list(range(7, 14))
ID_OK = [14, 15]
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
IT_ALL = ' '.join(v['italian'] for v in cov)
EN_ALL = ' '.join(v['english'] for v in cov)
KINDS = collections.Counter(u['kind'] for u in units)
CTX = collections.Counter(u['context'] for u in units)
# composizione: 6 prefissi x 7 messaggi, in entrambe le lingue
EN_COMP = [by[p]['english'] + by[m]['english'] for p in PREFIX for m in MSG]
IT_COMP = [by[p]['italian'] + by[m]['italian'] for p in PREFIX for m in MSG]


def composed_ok(s):
    return (s.startswith('"') and s.endswith('"') and s.count('"') == 2
            and '  ' not in s and '. ' in s and len(s) > 20)


rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 15/15", len(cov) == 15 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 15 NEWS', KINDS == {'NEWS': 15}, dict(KINDS))
ck('ZERO VALUE, TEXT, DIALOG, MISSION_TEXT, LOGBOOK, DESCRIPTION, UI_LABEL (asserzioni vuote scritte)',
   [u['idx'] for u in units if u['kind'] != 'NEWS'] == [])
ck('2 contesti con i conteggi misurati (safety advisory 13, missing advisory 2)',
   len(CTX) == 2 and CTX == {'news:avgi safety advisory': 13, 'news:avgi missing advisory': 2}, dict(CTX))
ck('righe 197 e 280 (prima e ultima del lotto)',
   (cov[0]['line'], cov[-1]['line']) == (197, 280), (cov[0]['line'], cov[-1]['line']))
ck('ZERO tab in inglese e in italiano (asserzione negativa scritta)',
   sum(v['english'].count(TAB) for v in cov) == 0 == sum(v['italian'].count(TAB) for v in cov))
ck('14 virgolette: una per prefisso (6), una per messaggio (7), una per la virgoletta aperta (14)',
   sum(v['english'].count(QUOTE) for v in cov) == 14 == sum(v['italian'].count(QUOTE) for v in cov)
   and [v['idx'] for v in cov if v['italian'].count(QUOTE)] == list(range(1, 15))
   and by[15]['italian'].count(QUOTE) == 0,
   [(v['idx'], v['italian'].count(QUOTE)) for v in cov])
ck('i 6 prefissi: virgoletta APERTA, etichetta, punto, UNO spazio finale (struttura, non stile)',
   all(by[i]['italian'].startswith('"') and by[i]['italian'].endswith('. ')
       and by[i]['italian'].count('"') == 1 and by[i]['italian'].count(' ') == 1 for i in PREFIX)
   and [by[i]['italian'] for i in PREFIX]
   == ['"Cautela. ', '"Avvertenza. ', '"Avviso. ', '"Diligenza. ', '"Allarme. ', '"Vigilanza. '],
   [by[i]['italian'] for i in PREFIX])
ck('i 7 messaggi: nessuna virgoletta aperta, punto e virgoletta CHIUSA in coda',
   all(not by[i]['italian'].startswith('"') and by[i]['italian'].endswith('."')
       and by[i]['italian'].count('"') == 1 for i in MSG))
ck('lo spazio finale e\' identico in inglese e in italiano, unita\' per unita\' (i soli 6 prefissi)',
   [i for i in sorted(by) if by[i]['english'].endswith(' ')] == PREFIX
   == [i for i in sorted(by) if by[i]['italian'].endswith(' ')])
ck('COMPOSIZIONE: 42 combinazioni (6 prefissi x 7 messaggi) valide in inglese e in italiano',
   len(EN_COMP) == len(IT_COMP) == 42
   and all(composed_ok(s) for s in EN_COMP) and all(composed_ok(s) for s in IT_COMP),
   [s for s in IT_COMP if not composed_ok(s)][:3])
ck('nessuna combinazione italiana perde il punto dell\'etichetta ne\' produce doppio spazio',
   not [s for s in IT_COMP if '. ' not in s or '  ' in s])
ck('le due unita\' di punteggiatura sono IDENTICHE per necessita\' e dichiarate (`"` e `.`)',
   sorted(v['idx'] for v in cov if v['italian'] == v['english']) == ID_OK
   and by[14]['italian'] == '"' and by[15]['italian'] == '.',
   sorted(v['idx'] for v in cov if v['italian'] == v['english']))
ck('13 unita\' tradotte (tutte tranne le due di punteggiatura)',
   [v['idx'] for v in cov if v['italian'] != v['english']] == list(range(1, 14)))
ck('NESSUN segnaposto (asserzione negativa scritta)',
   sum(len(TAG.findall(v['english'])) for v in cov) == 0 == sum(len(TAG.findall(v['italian'])) for v in cov))
ck('nome invariato: `Tangled Shroud` 5 volte nei messaggi (misurato), `Arche` 1',
   IT_ALL.count('Tangled Shroud') == 5 == EN_ALL.count('Tangled Shroud') and IT_ALL.count('Arche') == 1,
   (IT_ALL.count('Tangled Shroud'), EN_ALL.count('Tangled Shroud')))
ck('lessico del bollettino: «sciame», «convoglio» 2, «flotta» 2, «cordone difensivo», «avvistamento» '
   '(minuscolo: due parole aprono frase con la maiuscola)',
   IT_ALL.lower().count('sciame') == 1 and IT_ALL.lower().count('convoglio') == 2
   and IT_ALL.lower().count('flotta') == 2 and 'cordone difensivo' in IT_ALL
   and IT_ALL.lower().count('avvistamento') == 1,
   {w: IT_ALL.lower().count(w) for w in ('sciame', 'convoglio', 'flotta', 'avvistamento')})
ck('nessun residuo inglese di struttura (the, of the, and, with, their, while)',
   not [w for w in (' the ', ' of the ', ' and ', ' with ', ' their ', ' while ')
        if w in IT_ALL.lower()],
   [w for w in (' the ', ' of the ', ' and ', ' with ', ' their ', ' while ') if w in IT_ALL.lower()])
ck('registro: nessun «Lei» e nessun «mi scusi»', not re.search(r'\bLei\b|mi scusi', IT_ALL))
ck('nessun caporale e nessun carattere tipografico',
   not [v['idx'] for v in cov if any(c in v['italian'] for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026')])
rs = [v['ratio'] for v in cov]
ck('rapporto nel gate 0,55-1,90 (0,69-1,30; 72 -> 68 parole)',
   0.55 < min(rs) and max(rs) < 1.90, '%.2f - %.2f' % (min(rs), max(rs)))
ACC = re.compile(r"\b(e|piu|perche|cosi|gia|puo|cioe|percio|fa)'", re.I)
bad = [(v['idx'], ACC.search(v['italian']).group(0)) for v in cov if ACC.search(v['italian'])]
ck("tipografia (accenti veri, nessun apostrofo al posto dell'accento)", not bad, bad)
nonlat = [v['idx'] for v in cov for c in v['italian'] if ord(c) > 127 and not 0x00C0 <= ord(c) <= 0x024F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessun doppio spazio e nessuno spazio iniziale',
   not [v['idx'] for v in cov if '  ' in v['italian'] or v['italian'] != v['italian'].lstrip()])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("42 unita' tradotte prima della 197 (L233 22 + L234 20)",
   db.execute('select count(*) from units where path=? and line<197', (PATH,)).fetchone()[0] == 42)
ck("58 unita' dopo la 280 (115 - 42 - 15): il lotto NON chiude il file",
   db.execute('select count(*) from units where path=? and line>280', (PATH,)).fetchone()[0] == 58)
ck('lotto + prima + dopo = file: 15 + 42 + 58 = 115',
   15 + db.execute('select count(*) from units where path=? and line<197', (PATH,)).fetchone()[0]
   + db.execute('select count(*) from units where path=? and line>280', (PATH,)).fetchone()[0] == 115)
ck("LACUNA dell'inventario: ZERO unita' fra la 231 e la 279, dove il sorgente ha i blocchi `word` del "
   "`missing advisory` (asserzione misurata, non omessa)",
   db.execute('select count(*) from units where path=? and line between 231 and 279', (PATH,)).fetchone()[0] == 0)
ck('il file intero: 115 unita, righe 32 - 507',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (115, 32, 507))
st = dict(db.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('le 15 unita sono PENDING (misurato)',
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
