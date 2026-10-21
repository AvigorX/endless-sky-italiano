r"""check.py — L230 (`data/korath/korath outfits.txt`, 26 unita', righe 319-581). Terzo lotto del file.

**10 `VALUE` in una finestra sola**: massimo della campagna per un lotto misto. Confronto **10 identiche / 16 tradotte**.

**Due gruppi di testi ripetuti**:
- le unita' **1 e 4** dicono la stessa frase dei postbruciatori, che e' anche quella di **L229 unita' 10 e 13**: la resa deve
  essere la stessa **attraverso il confine del lotto**, e il controllo la confronta con `translation.json` di L229;
- le unita' **11, 14, 17, 20 e 23** sono **cinque copie** dello stesso paragrafo (il motore installato in parte nello spazio
  armi): una sola resa, ripetuta cinque volte.

**7 tab** (unita' 1, 4, 11, 14, 17, 20, 23) dopo i 3 di L229. **Zero virgolette**, quinto lotto consecutivo.
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
ED = os.path.join(L10N, 'staging/editorial')
PATH = 'data/korath/korath outfits.txt'
PREV = os.path.join(ED, 'L229_20261019_231932', 'translation.json')
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
VALS = [u['idx'] for u in units if u['kind'] == 'VALUE']
DESCS = [u['idx'] for u in units if u['kind'] == 'DESCRIPTION']
EN_A = [(v['idx'], v['english'].count(APOS)) for v in cov if APOS in v['english']]
IT_A = [(v['idx'], v['italian'].count(APOS)) for v in cov if APOS in v['italian']]
prev = {u['line']: u['italian'] for u in json.load(open(PREV, encoding='utf-8'))['units']}
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 26/26", len(cov) == 26 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 16 DESCRIPTION e 10 VALUE (massimo di VALUE in un lotto misto)',
   KINDS == {'DESCRIPTION': 16, 'VALUE': 10}, dict(KINDS))
ck('ZERO TEXT, DIALOG, MISSION_TEXT, LOGBOOK, NEWS, UI_LABEL (asserzioni vuote scritte)',
   [u['idx'] for u in units if u['kind'] not in ('DESCRIPTION', 'VALUE')] == [])
ck('11 contesti con i conteggi MISURATI (Reverser 3 a testa, Stellar Afterburner 3, Planetary e Comet Thruster 1)',
   len(CTX) == 11 and CTX == {'outfit:Afterburner (Planetary Class)': 1, 'outfit:Afterburner (Stellar Class)': 3,
                              'outfit:Engine (Meteor Class)': 2, 'outfit:Bow Drive (Meteor Class)': 2,
                              'outfit:Reverser (Asteroid Class)': 3, 'outfit:Reverser (Comet Class)': 3,
                              'outfit:Reverser (Lunar Class)': 3, 'outfit:Reverser (Planetary Class)': 3,
                              'outfit:Reverser (Stellar Class)': 3, 'outfit:Thruster (Asteroid Class)': 2,
                              'outfit:Thruster (Comet Class)': 1}, dict(CTX))
ck('righe 319 e 581 (prima e ultima del lotto)',
   (cov[0]['line'], cov[-1]['line']) == (319, 581), (cov[0]['line'], cov[-1]['line']))
ck('7 tab, nelle unita\' 1, 4, 11, 14, 17, 20, 23 (dopo i 3 di L229)',
   [v['idx'] for v in cov if TAB in v['english']] == [1, 4, 11, 14, 17, 20, 23]
   == [v['idx'] for v in cov if TAB in v['italian']]
   and sum(v['english'].count(TAB) for v in cov) == 7 == sum(v['italian'].count(TAB) for v in cov))
ck('ZERO virgolette in inglese e in italiano (quinto lotto consecutivo)',
   sum(v['english'].count(QUOTE) for v in cov) == 0 == sum(v['italian'].count(QUOTE) for v in cov))
ck('NESSUN segnaposto (asserzione negativa scritta)',
   sum(len(TAG.findall(v['english'])) for v in cov) == 0 == sum(len(TAG.findall(v['italian'])) for v in cov))
ck('10 unita\' IDENTICHE all\'inglese (tutti e soli i VALUE) e 16 tradotte (tutte e sole le DESCRIPTION)',
   sum(1 for v in cov if v['italian'] == v['english']) == 10
   and sorted(v['idx'] for v in cov if v['italian'] == v['english']) == VALS
   and sorted(v['idx'] for v in cov if v['italian'] != v['english']) == DESCS,
   (sorted(v['idx'] for v in cov if v['italian'] == v['english']), VALS))
ck('i 10 VALUE copiati alla lettera («Afterburners (Stellar Class)», «Reversers (Lunar Class)»…)',
   VALS == [2, 5, 7, 9, 12, 15, 18, 21, 24, 26]
   and by[2]['italian'] == 'Afterburners (Stellar Class)' and by[21]['italian'] == 'Reversers (Stellar Class)')
ck('COERENZA OLTRE IL LOTTO: le unita\' 1 e 4 dicono la stessa frase di L229 unita\' 10 (riga 300)',
   by[1]['italian'] == by[4]['italian'] and by[1]['english'] == by[4]['english']
   and by[1]['italian'] == prev[300],
   (by[1]['italian'][:60], prev[300][:60]))
ck('CINQUE copie identiche (unita\' 11, 14, 17, 20, 23) hanno una sola resa',
   len({by[i]['italian'] for i in (11, 14, 17, 20, 23)}) == 1
   and len({by[i]['english'] for i in (11, 14, 17, 20, 23)}) == 1
   and by[11]['italian'].strip().startswith('Questo motore Korath è stato modificato'))
ck('il recapito del nome è misto: «retropulsore Asteroid Class», «motori Meteor Class», «propulsore Korath»',
   'retropulsore Asteroid Class' in IT_ALL and 'motori Meteor Class' in IT_ALL
   and 'propulsore Korath' in IT_ALL and 'postbruciatori Korath' in IT_ALL)
ck('terminologia: «spazio armi», «spinta all\'indietro», «camere di reazione», «gli Esuli»',
   'spazio armi' in IT_ALL and "spinta all'indietro" in IT_ALL
   and 'camere di reazione' in IT_ALL and 'Esuli' in IT_ALL)
ck('nessun residuo inglese di struttura (the, of the, and, with, their)',
   not [w for w in (' the ', ' of the ', ' and ', ' with ', ' their ', ' while ', ' that they ')
        if w in IT_ALL.lower()],
   [w for w in (' the ', ' of the ', ' and ', ' with ', ' their ', ' while ', ' that they ') if w in IT_ALL.lower()])
ck("apici: 8 in inglese (le 7 unita' col tab piu' la 22 con you've) e 16 in italiano su 13 unita'",
   sum(n for _, n in EN_A) == 8 and sum(n for _, n in IT_A) == 16
   and EN_A == [(1, 1), (4, 1), (11, 1), (14, 1), (17, 1), (20, 1), (22, 1), (23, 1)]
   and IT_A == [(1, 2), (3, 1), (4, 2), (6, 2), (11, 1), (13, 1), (14, 1), (16, 1),
                (17, 1), (19, 1), (20, 1), (22, 1), (23, 1)], (EN_A, IT_A))
ck('registro: nessun «Lei» e nessun «mi scusi»', not re.search(r'\bLei\b|mi scusi', IT_ALL))
ck('nessun caporale e nessun carattere tipografico',
   not [v['idx'] for v in cov if any(c in v['italian'] for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026')])
rs = [v['ratio'] for v in cov]
ck('rapporto nel gate 0,55-1,90 (1,00 per i nomi, 1,04-1,25 per le DESCRIPTION)',
   0.55 < min(rs) and max(rs) < 1.90, '%.2f - %.2f' % (min(rs), max(rs)))
ACC = re.compile(r"\b(e|piu|perche|cosi|gia|puo|cioe|percio|fa)'", re.I)
bad = [(v['idx'], ACC.search(v['italian']).group(0)) for v in cov if ACC.search(v['italian'])]
ck('tipografia (accenti veri, nessun apostrofo al posto dell\'accento)', not bad, bad)
nonlat = [v['idx'] for v in cov for c in v['italian'] if ord(c) > 127 and not 0x00C0 <= ord(c) <= 0x024F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio (tab iniziali ammessi)',
   not [v['idx'] for v in cov if v['italian'] != v['italian'].rstrip()
        or '  ' in v['italian'].strip(TAB) or v['english'] != v['english'].rstrip()])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck('35 unita tradotte prima della 319 (L228 20 + L229 15)',
   db.execute('select count(*) from units where path=? and line<319', (PATH,)).fetchone()[0] == 35)
ck('lotto + residuo = file: 35 + 26 + 31 = 92',
   35 + 26 + db.execute('select count(*) from units where path=? and line>581', (PATH,)).fetchone()[0] == 92)
st = dict(db.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('le 26 unita sono PENDING (misurato)',
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
