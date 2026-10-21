r"""check.py — L219 (`data/successors/successor ships.txt`, 25 unita', righe 386-629). Secondo lotto del file.

**19 unita' su 25 restano identiche all'inglese** (16 `TEXT` = nomi di equipaggiamento, 3 `VALUE` = nomi di specie) e si
traducono le **6 `DESCRIPTION`**. Il rapporto 19/6 e' la regola del file, non una dimenticanza: il controllo lo asserisce
e verifica che le unita' tradotte siano **esattamente** le `DESCRIPTION`.

**Due coppie di `DESCRIPTION` condividono frasi**, e le rese devono restare identiche:
- unita' **7 e 9** aprono con la stessa frase («Questa navetta minuscola e' la nave piu' piccola in servizio…»);
- unita' **24 e 25** condividono «non e' ne' elegante ne' veloce» e «una disposizione delle armi abbastanza flessibile da
  permetterle di reagire all'occorrenza».

Se una delle due cambia, la scheda della stessa nave racconta due cose diverse.
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
PATH = 'data/successors/successor ships.txt'
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
KINDS = collections.Counter(u['kind'] for u in units)
CTX = collections.Counter(u['context'] for u in units)
TEXTS = [u['idx'] for u in units if u['kind'] == 'TEXT']
VALS = [u['idx'] for u in units if u['kind'] == 'VALUE']
DESCS = [u['idx'] for u in units if u['kind'] == 'DESCRIPTION']
EN_A = [(v['idx'], v['english'].count(APOS)) for v in cov if APOS in v['english']]
IT_A = [(v['idx'], v['italian'].count(APOS)) for v in cov if APOS in v['italian']]
SAME_OPEN = 'Questa navetta minuscola è la nave più piccola in servizio nello spazio dei Successori, e'
SHARED_24 = 'una disposizione delle armi abbastanza flessibile da permetterle di reagire all\'occorrenza'
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 25/25", len(cov) == 25 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 16 TEXT, 6 DESCRIPTION, 3 VALUE (asserzione scritta)',
   KINDS == {'TEXT': 16, 'DESCRIPTION': 6, 'VALUE': 3}, dict(KINDS))
ck('ZERO DIALOG, MISSION_TEXT, LOGBOOK, NEWS, UI_LABEL (asserzioni vuote scritte)',
   [u['idx'] for u in units if u['kind'] not in ('TEXT', 'DESCRIPTION', 'VALUE')] == [])
ck('3 contesti con le dimensioni misurate: Kvelqde 9, Myaede 9, Kvelqde-Khora 7',
   CTX == {'ship:Kvelqde': 9, 'ship:Kvelqde-Khora': 7, 'ship:Myaede': 9}, dict(CTX))
ck('righe 386 e 629 (prima e ultima del lotto)',
   (cov[0]['line'], cov[-1]['line']) == (386, 629), (cov[0]['line'], cov[-1]['line']))
ck('1 tab, solo nell\'unita\' 8 (la nota sui Predecessori), identico nelle due lingue',
   [v['idx'] for v in cov if TAB in v['english']] == [8] == [v['idx'] for v in cov if TAB in v['italian']]
   and by[8]['italian'].startswith(TAB) and not by[8]['italian'].startswith(TAB + TAB))
ck('32 virgolette: esattamente 2 per ognuna delle 16 TEXT, zero altrove',
   sum(v['english'].count(QUOTE) for v in cov) == 32 == sum(v['italian'].count(QUOTE) for v in cov)
   and [v['idx'] for v in cov if QUOTE in v['english']] == TEXTS
   and all(v['english'].count(QUOTE) == 2 == v['italian'].count(QUOTE) for v in cov if v['kind'] == 'TEXT'),
   (sum(v['english'].count(QUOTE) for v in cov), sum(v['italian'].count(QUOTE) for v in cov)))
ck('NESSUN segnaposto (asserzione negativa scritta)',
   sum(len(TAG.findall(v['english'])) for v in cov) == 0
   == sum(len(TAG.findall(v['italian'])) for v in cov))
ck('19 unita\' IDENTICHE all\'inglese (16 TEXT + 3 VALUE) e 6 tradotte: sono esattamente le DESCRIPTION',
   sum(1 for v in cov if v['italian'] == v['english']) == 19
   and sorted(v['idx'] for v in cov if v['italian'] != v['english']) == DESCS)
ck('i 16 TEXT e i 3 VALUE copiati alla lettera, virgolette comprese',
   len(TEXTS) == 16 and len(VALS) == 3 == len([i for i in VALS if by[i]['italian'] == by[i]['english']])
   and all(by[i]['italian'] == by[i]['english'] for i in TEXTS))
ck('le 6 DESCRIPTION sono tutte tradotte e tutte distinte',
   len(DESCS) == 6 and all(by[i]['italian'] != by[i]['english'] for i in DESCS)
   and len({by[i]['italian'] for i in DESCS}) == 6)
ck('COERENZA 7/9: le due schede della Kvelqde aprono con la stessa frase',
   by[7]['italian'].startswith(SAME_OPEN) and by[9]['italian'].startswith(SAME_OPEN),
   (by[7]['italian'][:60], by[9]['italian'][:60]))
ck('COERENZA 24/25: «non è né elegante né veloce» e la formula delle armi identiche nelle due schede',
   'non è né elegante né veloce' in by[24]['italian'] and 'non è né elegante né veloce' in by[25]['italian']
   and SHARED_24 in by[24]['italian'] and SHARED_24 in by[25]['italian'])
ck('terminologia: «Alte Case», «Case del Popolo», «Successori», «Predecessori»; «High Houses» assente',
   'Alte Case' in IT_ALL and 'Case del Popolo' in IT_ALL and 'Successori' in IT_ALL
   and 'Predecessori' in IT_ALL and 'High Houses' not in IT_ALL and 'People\'s' not in IT_ALL)
ck("apici: 3 in inglese (16 People's, 24 grandparent's, 25 you've) e 10 in italiano in 5 unita' "
   "(8 x5, 9 x2, 16, 24, 25): totale e distribuzione non coincidono, ed e' atteso",
   sum(n for _, n in EN_A) == 3 and sum(n for _, n in IT_A) == 10
   and EN_A == [(16, 1), (24, 1), (25, 1)] and IT_A == [(8, 5), (9, 2), (16, 1), (24, 1), (25, 1)],
   (EN_A, IT_A))
ck('registro: nessun «Lei» e nessun «mi scusi»',
   not re.search(r'\bLei\b|mi scusi', IT_ALL))
ck('nessun caporale e nessun carattere tipografico (le virgolette dritte dei nomi sono ammesse)',
   not [v['idx'] for v in cov if any(c in v['italian'] for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026')])
DESC_TXT = ' '.join(by[i]['italian'] for i in DESCS)
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' you ', ' to the ', ' will be ',
        ' is ', ' are ', ' from the ', ' its ', ' it is ', ' such as ', ' rather than ', ' for a ', ' that ',
        ' have ', ' they ', ' their ')
ck('nessun residuo inglese nelle DESCRIPTION', not [w for w in ENGW if w in DESC_TXT.lower()],
   [w for w in ENGW if w in DESC_TXT.lower()])
rs = [v['ratio'] for v in cov]
ck('rapporto nel gate 0,55-1,90 (nomi 1,00; DESCRIPTION 1,05-1,16)',
   0.55 < min(rs) and max(rs) < 1.90, '%.2f - %.2f' % (min(rs), max(rs)))
ACC = re.compile(r"\b(e|piu|perche|cosi|gia|puo|cioe|percio|fa)'", re.I)
bad = [(v['idx'], ACC.search(v['italian']).group(0)) for v in cov if ACC.search(v['italian'])]
ck('tipografia (accenti veri, nessun apostrofo al posto dell\'accento)', not bad, bad)
nonlat = [v['idx'] for v in cov for c in v['italian'] if ord(c) > 127 and not 0x00C0 <= ord(c) <= 0x024F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio (il tab iniziale dell\'unita\' 8 e\' ammesso)',
   not [v['idx'] for v in cov if v['italian'] != v['italian'].rstrip()
        or '  ' in v['italian'].strip(TAB) or v['english'] != v['english'].rstrip()])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck('45 unita tradotte prima della 386 (L218)',
   db.execute('select count(*) from units where path=? and line<386', (PATH,)).fetchone()[0] == 45)
ck('lotto + residuo = file: 45 + 25 + 76 = 146',
   45 + 25 + db.execute('select count(*) from units where path=? and line>629', (PATH,)).fetchone()[0] == 146)
st = dict(db.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('le 25 unita sono PENDING (misurato)',
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
