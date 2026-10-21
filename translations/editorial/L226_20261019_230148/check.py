r"""check.py — L226 (`data/remnant/remnant outfits.txt`, 11 unita', righe 675-864). Quarto lotto del file.

**Zero virgolette**, in inglese e in italiano: e' la prima volta in molti lotti, e va **asserito** (`== 0`), non omesso. Un
controllo che tace su un numero zero non distingue «non ce ne sono» da «non le ho guardate».

**Zero unita' da copiare** (11 `DESCRIPTION` su 11): confronto **0 / 11**.

**3 tab** (unita' 1, 4, 6) dopo i 4 di L225 e i 9 di L224: la densita' si conta sul lotto.

**Nove contesti su undici unita'**: solo Salvage Scanner e Bellows-Class Afterburner hanno due unita'; le altre sette ne
hanno una. Non ci sono coppie da confrontare come nei lotti precedenti, e il controllo non ne inventa.
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
EN_A = [(v['idx'], v['english'].count(APOS)) for v in cov if APOS in v['english']]
IT_A = [(v['idx'], v['italian'].count(APOS)) for v in cov if APOS in v['italian']]
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 11/11", len(cov) == 11 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 11 DESCRIPTION, nient\'altro', KINDS == {'DESCRIPTION': 11}, dict(KINDS))
ck('ZERO VALUE, TEXT, DIALOG, MISSION_TEXT, LOGBOOK, NEWS, UI_LABEL (asserzioni vuote scritte)',
   [u['idx'] for u in units if u['kind'] != 'DESCRIPTION'] == [])
ck('9 contesti su 11 unita\': solo Salvage Scanner e Bellows-Class Afterburner hanno 2 unita\'',
   len(CTX) == 9 and CTX == {'outfit:Research Laboratory': 1, 'outfit:Quantum Key Stone': 1,
                             'outfit:Salvage Scanner': 2, 'outfit:Bellows-Class Afterburner': 2,
                             'outfit:Anvil-Class Engine': 1, 'outfit:Crucible-Class Thruster': 1,
                             'outfit:Forge-Class Thruster': 1, 'outfit:Smelter-Class Thruster': 1,
                             'outfit:Crucible-Class Steering': 1}, dict(CTX))
ck('righe 675 e 864 (prima e ultima del lotto)',
   (cov[0]['line'], cov[-1]['line']) == (675, 864), (cov[0]['line'], cov[-1]['line']))
ck('3 tab, nelle unita\' 1, 4 e 6 (dopo 4 e 9 nei lotti precedenti)',
   [v['idx'] for v in cov if TAB in v['english']] == [1, 4, 6]
   == [v['idx'] for v in cov if TAB in v['italian']]
   and sum(v['english'].count(TAB) for v in cov) == 3 == sum(v['italian'].count(TAB) for v in cov))
ck('ZERO virgolette in inglese e in italiano: asserzione esplicita su un numero zero',
   sum(v['english'].count(QUOTE) for v in cov) == 0 == sum(v['italian'].count(QUOTE) for v in cov))
ck('NESSUN segnaposto (asserzione negativa scritta)',
   sum(len(TAG.findall(v['english'])) for v in cov) == 0 == sum(len(TAG.findall(v['italian'])) for v in cov))
ck('0 unita\' identiche all\'inglese e 11 tradotte',
   sum(1 for v in cov if v['italian'] == v['english']) == 0
   and all(v['italian'] != v['english'] for v in cov))
ck('i tre punti dell\'unita\' 9 restano tre punti: 1 occorrenza, nessun carattere …',
   by[9]['italian'].count('...') == 1 and '\u2026' not in by[9]['italian']
   and by[9]['english'].count('...') == 1)
ck('terminologia: «ramscoop», «Point Defense Turrets», «scanner», «sterzata», «intercettore»',
   'ramscoop' in IT_ALL and 'Point Defense Turrets' in IT_ALL and 'scanner' in IT_ALL
   and 'sterzata' in IT_ALL and 'intercettore' in IT_ALL)
ck('nomi propri invariati: Remnant, Ember Waste, la Waste, Aventine, Bellows-Class Afterburner',
   IT_ALL.count('Remnant') >= 6 and 'Ember Waste' in IT_ALL and 'della Waste' in IT_ALL
   and 'Aventine' in IT_ALL and 'Bellows-Class Afterburner' in IT_ALL)
ck('nessun residuo inglese di struttura (the, of the, and, with, their)',
   not [w for w in (' the ', ' of the ', ' and ', ' with ', ' their ', ' while ', ' that they ')
        if w in IT_ALL.lower()],
   [w for w in (' the ', ' of the ', ' and ', ' with ', ' their ', ' while ', ' that they ') if w in IT_ALL.lower()])
ck("apici: 3 in inglese (2 ship's, 5 aren't, 10 ship's) e 8 in italiano su 8 unita' diverse",
   sum(n for _, n in EN_A) == 3 and sum(n for _, n in IT_A) == 8
   and EN_A == [(2, 1), (5, 1), (10, 1)]
   and IT_A == [(1, 1), (2, 1), (5, 1), (6, 1), (7, 1), (9, 1), (10, 1), (11, 1)], (EN_A, IT_A))
ck('registro: nessun «Lei» e nessun «mi scusi»', not re.search(r'\bLei\b|mi scusi', IT_ALL))
ck('nessun caporale e nessun carattere tipografico',
   not [v['idx'] for v in cov if any(c in v['italian'] for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026')])
rs = [v['ratio'] for v in cov]
ck('rapporto nel gate 0,55-1,90 (1,00 - 1,21)',
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
ck('36 unita tradotte prima della 675 (L223 12 + L224 13 + L225 11)',
   db.execute('select count(*) from units where path=? and line<675', (PATH,)).fetchone()[0] == 36)
ck('lotto + residuo = file: 36 + 11 + 10 = 57',
   36 + 11 + db.execute('select count(*) from units where path=? and line>864', (PATH,)).fetchone()[0] == 57)
ck('il residuo dopo la 864 contiene l\'ULTIMO VALUE del file (riga 948)',
   [r[0] for r in db.execute('select line from units where path=? and line>864 and kind="VALUE"',
                             (PATH,)).fetchall()] == [948])
st = dict(db.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('le 11 unita sono PENDING (misurato)',
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
