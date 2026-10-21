r"""check.py — L229 (`data/korath/korath outfits.txt`, 15 unita', righe 208-318). Secondo lotto del file.

**File misto**: 11 `DESCRIPTION` + 4 `VALUE`, confronto **4 identiche / 11 tradotte**.

**I tre tab tornano** (unita' 7, 10, 13) dopo lo **zero** di L228: «zero tab» era una proprieta' del lotto, non del file.

**Tre unita' quasi identiche.** La 10 e la 13 dicono la stessa cosa parola per parola; la 7 e' la stessa frase con un `may`
in piu' (*that **may** nearly melt* contro *that nearly melts*). La resa lo registra: «che **può quasi fondere**» nella 7,
«che **quasi fonde**» nella 10 e nella 13. Il controllo verifica che la 10 e la 13 siano **identiche** e che la 7 sia la
stessa frase **modificata esattamente in quel punto**.

**Le virgolette restano zero** — quarto lotto consecutivo, asserito.
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
PATH = 'data/korath/korath outfits.txt'
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
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 15/15", len(cov) == 15 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 11 DESCRIPTION e 4 VALUE (file misto)',
   KINDS == {'DESCRIPTION': 11, 'VALUE': 4}, dict(KINDS))
ck('ZERO TEXT, DIALOG, MISSION_TEXT, LOGBOOK, NEWS, UI_LABEL (asserzioni vuote scritte)',
   [u['idx'] for u in units if u['kind'] not in ('DESCRIPTION', 'VALUE')] == [])
ck("8 contesti: Asteroid, Comet e Lunar hanno 3 unita' (VALUE + 2 DESCRIPTION), Planetary 2 "
   "(la seconda scheda e' oltre il confine, riga 319)",
   len(CTX) == 8 and CTX == {'outfit:Fuel Processor': 1, 'outfit:Command Center': 1,
                             'outfit:Reasoning Node': 1, 'outfit:Control Transceiver': 1,
                             'outfit:Afterburner (Asteroid Class)': 3, 'outfit:Afterburner (Comet Class)': 3,
                             'outfit:Afterburner (Lunar Class)': 3, 'outfit:Afterburner (Planetary Class)': 2},
   dict(CTX))
ck('righe 208 e 318 (prima e ultima del lotto)',
   (cov[0]['line'], cov[-1]['line']) == (208, 318), (cov[0]['line'], cov[-1]['line']))
ck('3 tab, nelle unita\' 7, 10 e 13: tornano dopo lo ZERO di L228',
   [v['idx'] for v in cov if TAB in v['english']] == [7, 10, 13]
   == [v['idx'] for v in cov if TAB in v['italian']]
   and sum(v['english'].count(TAB) for v in cov) == 3 == sum(v['italian'].count(TAB) for v in cov))
ck('ZERO virgolette in inglese e in italiano (quarto lotto consecutivo)',
   sum(v['english'].count(QUOTE) for v in cov) == 0 == sum(v['italian'].count(QUOTE) for v in cov))
ck('NESSUN segnaposto (asserzione negativa scritta)',
   sum(len(TAG.findall(v['english'])) for v in cov) == 0 == sum(len(TAG.findall(v['italian'])) for v in cov))
ck('4 unita\' IDENTICHE all\'inglese (tutti e soli i VALUE) e 11 tradotte (tutte e sole le DESCRIPTION)',
   sum(1 for v in cov if v['italian'] == v['english']) == 4
   and sorted(v['idx'] for v in cov if v['italian'] == v['english']) == VALS
   and sorted(v['idx'] for v in cov if v['italian'] != v['english']) == DESCS,
   (sorted(v['idx'] for v in cov if v['italian'] == v['english']), VALS))
ck('i 4 VALUE sono copiati alla lettera («Afterburners (Asteroid Class)»…)',
   VALS == [5, 8, 11, 14] and by[5]['italian'] == 'Afterburners (Asteroid Class)'
   and by[14]['italian'] == 'Afterburners (Planetary Class)')
ck('la 10 e la 13 sono IDENTICHE, in inglese e in italiano',
   by[10]['english'] == by[13]['english'] and by[10]['italian'] == by[13]['italian'])
ck('la 7 e\' la stessa frase con un `may` in piu\': nella resa, «può quasi fondere» contro «quasi fonde»',
   by[7]['italian'] == by[10]['italian'].replace('che quasi fonde', 'che può quasi fondere')
   and 'may nearly melt' in by[7]['english'] and 'may nearly melt' not in by[10]['english'])
ck('i nomi restano inglesi nella prosa (Fuel Processor, Command Center), le parole comuni si traducono',
   'Fuel Processor' in IT_ALL and 'Command Center' in IT_ALL
   and 'postbruciatore' in IT_ALL and 'cuccette' in IT_ALL)
ck('terminologia: «Guerra Civile Korath», «gli Hai», «Kor Efret», «automata Mereti», «Kor Sestor»',
   'Guerra Civile Korath' in IT_ALL and 'Hai' in IT_ALL and 'Kor Efret' in IT_ALL
   and 'automata Mereti' in IT_ALL and 'Kor Sestor' in IT_ALL)
ck('nessun residuo inglese di struttura (the, of the, and, with, their)',
   not [w for w in (' the ', ' of the ', ' and ', ' with ', ' their ', ' while ', ' that they ')
        if w in IT_ALL.lower()],
   [w for w in (' the ', ' of the ', ' and ', ' with ', ' their ', ' while ', ' that they ') if w in IT_ALL.lower()])
ck("apici: 4 in inglese (2 ship's, 7 thruster's, 10 thruster's, 13 thruster's) e 12 in italiano in 8 unita'",
   sum(n for _, n in EN_A) == 4 and sum(n for _, n in IT_A) == 12
   and EN_A == [(2, 1), (7, 1), (10, 1), (13, 1)]
   and IT_A == [(2, 1), (3, 1), (6, 2), (7, 2), (10, 2), (12, 1), (13, 2), (15, 1)], (EN_A, IT_A))
ck('registro: nessun «Lei» e nessun «mi scusi»', not re.search(r'\bLei\b|mi scusi', IT_ALL))
ck('nessun caporale e nessun carattere tipografico',
   not [v['idx'] for v in cov if any(c in v['italian'] for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026')])
rs = [v['ratio'] for v in cov]
ck('rapporto nel gate 0,55-1,90 (1,00 per i nomi, 1,04-1,21 per le DESCRIPTION)',
   0.55 < min(rs) and max(rs) < 1.90, '%.2f - %.2f' % (min(rs), max(rs)))
ACC = re.compile(r"\b(e|piu|perche|cosi|gia|puo|cioe|percio|fa)'", re.I)
bad = [(v['idx'], ACC.search(v['italian']).group(0)) for v in cov if ACC.search(v['italian'])]
ck('tipografia (accenti veri, nessun apostrofo al posto dell\'accento)', not bad, bad)
nonlat = [v['idx'] for v in cov for c in v['italian'] if ord(c) > 127 and not 0x00C0 <= ord(c) <= 0x024F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio (tab iniziali delle 7, 10, 13 ammessi)',
   not [v['idx'] for v in cov if v['italian'] != v['italian'].rstrip()
        or '  ' in v['italian'].strip(TAB) or v['english'] != v['english'].rstrip()])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck('20 unita tradotte prima della 208 (L228)',
   db.execute('select count(*) from units where path=? and line<208', (PATH,)).fetchone()[0] == 20)
ck('lotto + residuo = file: 20 + 15 + 57 = 92',
   20 + 15 + db.execute('select count(*) from units where path=? and line>318', (PATH,)).fetchone()[0] == 92)
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
