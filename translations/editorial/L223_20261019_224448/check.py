r"""check.py — L223 (`data/remnant/remnant outfits.txt`, 12 unita', righe 48-297). **Primo lotto del file.**

**Il rovesciamento**: in `successor ships.txt` erano 100 `TEXT` di nomi su 146; qui sono **11 `DESCRIPTION` su 12** e un solo
`VALUE` da copiare. La parte delicata e' la traduzione, non la copia, e le unita' sono lunghe (12 unita' = 463 parole).

**I nomi degli equipaggiamenti restano in inglese anche nella prosa** (`Inhibitor Cannon`, `Inhibitor Turret`, `Thrasher
Cannon`, `Point Defense Turret`, `EMP Torpedo Storage Bay`): sono gli stessi nomi che il giocatore vede nel negozio di
equipaggiamenti. Si traducono invece le parole comuni — *cannon* quando e' «cannone», *turret* quando e' «torretta»,
*torpedo* quando e' «siluro» — e il controllo verifica che le forme inglesi **non** compaiano come nomi comuni.

**Nomi propri invariati**: `Remnant`, `Ember Waste`, `Aventine`, `Alphas`.
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
PATH = 'data/remnant/remnant outfits.txt'
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


ck("unita' tradotte 12/12", len(cov) == 12 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 11 DESCRIPTION, 1 VALUE (asserzione scritta)', KINDS == {'DESCRIPTION': 11, 'VALUE': 1}, dict(KINDS))
ck('ZERO TEXT, DIALOG, MISSION_TEXT, LOGBOOK, NEWS, UI_LABEL (asserzioni vuote scritte)',
   [u['idx'] for u in units if u['kind'] not in ('DESCRIPTION', 'VALUE')] == [])
ck('8 contesti, uno per equipaggiamento (non per unita\')',
   len(CTX) == 8 and CTX == {'outfit:Inhibitor Cannon': 2, 'outfit:Inhibitor Turret': 2,
                             'outfit:Thrasher Cannon': 1, 'outfit:Thrasher Turret': 1,
                             'outfit:Point Defense Turret': 1, 'outfit:EMP Torpedo': 2,
                             'outfit:EMP Torpedo Storage Bay': 2, 'outfit:EMP Torpedo Bay': 1},
   dict(CTX))
ck('righe 48 e 297 (prima e ultima del lotto)',
   (cov[0]['line'], cov[-1]['line']) == (48, 297), (cov[0]['line'], cov[-1]['line']))
ck('PRIMO LOTTO DEL FILE: 0 unita prima della 48', not [u for u in units if u['line'] < 48])
ck('3 tab, unita\' 2, 4 e 11 (tutte DESCRIPTION), identici nelle due lingue',
   [v['idx'] for v in cov if TAB in v['english']] == [2, 4, 11]
   == [v['idx'] for v in cov if TAB in v['italian']]
   and all(by[i]['italian'].startswith(TAB) and not by[i]['italian'].startswith(TAB + TAB) for i in (2, 4, 11)))
ck('2 virgolette, entrambe nell\'unita\' 1 (la battuta della capitana), e in nessun\'altra',
   sum(v['english'].count(QUOTE) for v in cov) == 2 == sum(v['italian'].count(QUOTE) for v in cov)
   and [v['idx'] for v in cov if QUOTE in v['italian']] == [1]
   and 'Non torneremo a casa finché non ci impadroniremo di quell\'arma.' in by[1]['italian'])
ck('NESSUN segnaposto (asserzione negativa scritta)',
   sum(len(TAG.findall(v['english'])) for v in cov) == 0
   == sum(len(TAG.findall(v['italian'])) for v in cov))
ck('1 VALUE identico all\'inglese e 11 DESCRIPTION tradotte: qui si traduce quasi tutto',
   VALS == [8] and by[8]['italian'] == by[8]['english'] == 'EMP Torpedoes'
   and all(by[i]['italian'] != by[i]['english'] for i in DESCS))
ck('le 11 DESCRIPTION sono tutte distinte', len({by[i]['italian'] for i in DESCS}) == 11)
ck('i nomi degli equipaggiamenti restano in inglese nella prosa',
   'Inhibitor Cannon' in IT_ALL and 'Inhibitor Turrets' in IT_ALL
   and 'Thrasher Cannon' in IT_ALL and 'Thrasher Cannons' in IT_ALL
   and 'EMP Torpedo Storage Bay' in IT_ALL)
ck('le parole comuni sono tradotte: «cannone/cannoni», «torretta/torrette», «siluro/siluri» presenti; '
   'nessun «cannon»/«turret»/«torpedo» nudo fuori dai nomi',
   re.search(r'\bcannon[ei]\b', IT_ALL) is not None
   and re.search(r'\btorrett[ae]\b', IT_ALL) is not None
   and re.search(r'\bsilur[oi]\b', IT_ALL) is not None
   and not re.search(r'\b(cannons?|turrets?|torpedoes?)\b',
                     IT_ALL.replace('Inhibitor Cannon', '').replace('Thrasher Cannons', '')
                     .replace('Thrasher Cannon', '').replace('EMP Torpedo', '')
                     .replace('Inhibitor Turrets', '')),
   (re.findall(r'\bcannon[ei]\b', IT_ALL)[:3], re.findall(r'\btorrett[ae]\b', IT_ALL)[:3],
    re.findall(r'\bsilur[oi]\b', IT_ALL)[:3]))
ck('nomi propri invariati: Remnant, Ember Waste, Aventine, Alphas',
   IT_ALL.count('Remnant') >= 8 and 'Ember Waste' in IT_ALL and 'Aventine' in IT_ALL and 'Alphas' in IT_ALL)
ck('nessun residuo inglese di struttura (the, of the, and, with, their)',
   not [w for w in (' the ', ' of the ', ' and ', ' with ', ' their ', ' while ', ' that they ')
        if w in IT_ALL.lower()],
   [w for w in (' the ', ' of the ', ' and ', ' with ', ' their ', ' while ', ' that they ') if w in IT_ALL.lower()])
ck("apici: 4 in inglese (1 x2 scout's/aren't, 3 ship's, 9 ship's) e 16 in italiano in 6 unita'",
   sum(n for _, n in EN_A) == 4 and sum(n for _, n in IT_A) == 16
   and EN_A == [(1, 2), (3, 1), (9, 1)]
   and IT_A == [(1, 4), (2, 5), (4, 2), (5, 2), (6, 2), (10, 1)], (EN_A, IT_A))
ck('registro: nessun «Lei» e nessun «mi scusi»', not re.search(r'\bLei\b|mi scusi', IT_ALL))
ck('nessun caporale e nessun carattere tipografico',
   not [v['idx'] for v in cov if any(c in v['italian'] for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026')])
rs = [v['ratio'] for v in cov]
ck('rapporto nel gate 0,55-1,90 (0,99 - 1,15: l\'italiano e\' leggermente piu\' corto, 458 parole contro 463)',
   0.55 < min(rs) and max(rs) < 1.90, '%.2f - %.2f' % (min(rs), max(rs)))
ACC = re.compile(r"\b(e|piu|perche|cosi|gia|puo|cioe|percio|fa)'", re.I)
bad = [(v['idx'], ACC.search(v['italian']).group(0)) for v in cov if ACC.search(v['italian'])]
ck('tipografia (accenti veri, nessun apostrofo al posto dell\'accento)', not bad, bad)
nonlat = [v['idx'] for v in cov for c in v['italian'] if ord(c) > 127 and not 0x00C0 <= ord(c) <= 0x024F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio (tab iniziali delle 2, 4, 11 ammessi)',
   not [v['idx'] for v in cov if v['italian'] != v['italian'].rstrip()
        or '  ' in v['italian'].strip(TAB) or v['english'] != v['english'].rstrip()])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck('il file ha 57 unita', db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0] == 57)
ck('lotto + residuo = file: 12 + 45 = 57',
   12 + db.execute('select count(*) from units where path=? and line>297', (PATH,)).fetchone()[0] == 57)
ck('il file e\' quasi tutto prosa: 55 DESCRIPTION e 2 VALUE',
   db.execute('select kind,count(*) from units where path=? group by kind',
              (PATH,)).fetchall() == [('DESCRIPTION', 55), ('VALUE', 2)])
st = dict(db.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('le 12 unita sono PENDING (misurato)',
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
