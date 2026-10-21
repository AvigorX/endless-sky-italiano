r"""check.py — L225 (`data/remnant/remnant outfits.txt`, 11 unita', righe 581-674). Terzo lotto del file.

**Ancora zero unita' da copiare**: 11 `DESCRIPTION` su 11. Confronto **0 identiche / 11 tradotte**, scritto come
asserzione.

**I tab scendono a 4** (unita' 2, 4, 6, 10) dopo i 9 di L224: la densita' non si eredita, si conta.

**Le virgolette sono le "branchie"** dell'unita' 8 — *their "gills," which are effectively built-in ramscoops* — e sono le
sole 2 del lotto, in entrambe le lingue, nella stessa unita'.

**Famiglia lessicale da tenere coerente**: `ion` compare in tre forme — *ionization* («ionizzazione»), *ion dissipation*
(«dissipazione ionica») e *ion resistance* («resistenza ionica»); *ion storm* → «tempesta ionica» e *ion storms* al plurale
in due unita'.
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
ck('7 contesti con le dimensioni misurate (Millennium/Epoch/Aeon Cell 2 a testa, NDR-114 Android 2, gli altri 1)',
   CTX == {'outfit:Millennium Cell': 2, 'outfit:Epoch Cell': 2, 'outfit:Aeon Cell': 2,
           'outfit:Thermoelectric Cooler': 1, 'outfit:Emergency Ramscoop': 1,
           'outfit:NDR-114 Android': 2, 'outfit:Research Laboratory': 1}, dict(CTX))
ck('righe 581 e 674 (prima e ultima del lotto)',
   (cov[0]['line'], cov[-1]['line']) == (581, 674), (cov[0]['line'], cov[-1]['line']))
ck('4 tab, nelle unita\' 2, 4, 6, 10 (non 9 come in L224: la densita\' si conta)',
   [v['idx'] for v in cov if TAB in v['english']] == [2, 4, 6, 10]
   == [v['idx'] for v in cov if TAB in v['italian']]
   and sum(v['english'].count(TAB) for v in cov) == 4 == sum(v['italian'].count(TAB) for v in cov))
ck('2 virgolette, entrambe nell\'unita\' 8 (le "branchie"), come in inglese',
   sum(v['english'].count(QUOTE) for v in cov) == 2 == sum(v['italian'].count(QUOTE) for v in cov)
   and [v['idx'] for v in cov if QUOTE in v['english']] == [8]
   and [v['idx'] for v in cov if QUOTE in v['italian']] == [8]
   and '"branchie"' in by[8]['italian'])
ck('NESSUN segnaposto (asserzione negativa scritta)',
   sum(len(TAG.findall(v['english'])) for v in cov) == 0 == sum(len(TAG.findall(v['italian'])) for v in cov))
ck('0 unita\' identiche all\'inglese e 11 tradotte',
   sum(1 for v in cov if v['italian'] == v['english']) == 0
   and all(v['italian'] != v['english'] for v in cov))
ck("la famiglia di «ion» e' resa in modo coerente: ionizzazione (1), dissipazione ionica, resistenza ionica, "
   "tempeste ioniche (1); poi il testo dice «dalla tempesta», senza ripetere l'aggettivo",
   'ionizzazione' in IT_ALL and 'dissipazione ionica' in IT_ALL
   and 'resistenza ionica' in IT_ALL and 'tempeste ioniche' in IT_ALL
   and IT_ALL.count('ionica') == 2 and 'dalla tempesta' in by[6]['italian'],
   (IT_ALL.count('ionizzazione'), IT_ALL.count('ionica'), IT_ALL.count('ioniche')))
ck('«generatore radiotermico», «radioisotopi», «calore disperso», «termoelettrica a radioisotopi»',
   'generatore radiotermico' in IT_ALL and 'radioisotopi' in IT_ALL
   and 'calore disperso' in IT_ALL and 'termoelettrica a radioisotopi' in IT_ALL)
ck('nomi propri e nomi di equipaggiamento invariati: Remnant, Ember Waste, Viminal, Millennium Cell, NDR-114 Android, ramscoop',
   IT_ALL.count('Remnant') >= 8 and 'Ember Waste' in IT_ALL and 'Viminal' in IT_ALL
   and 'Millennium Cell' in IT_ALL and 'NDR-114 Android' not in IT_ALL and 'ramscoop' in IT_ALL)
ck('nessun residuo inglese di struttura (the, of the, and, with, their)',
   not [w for w in (' the ', ' of the ', ' and ', ' with ', ' their ', ' while ', ' that they ')
        if w in IT_ALL.lower()],
   [w for w in (' the ', ' of the ', ' and ', ' with ', ' their ', ' while ', ' that they ') if w in IT_ALL.lower()])
ck("apici: 3 in inglese (3 generator's, 7 ship's, 11 isn't) e 15 in italiano in 9 unita'",
   sum(n for _, n in EN_A) == 3 and sum(n for _, n in IT_A) == 15
   and EN_A == [(3, 1), (7, 1), (11, 1)]
   and IT_A == [(3, 1), (4, 2), (5, 2), (6, 1), (7, 1), (8, 2), (9, 1), (10, 2), (11, 3)], (EN_A, IT_A))
ck('registro: nessun «Lei» e nessun «mi scusi»', not re.search(r'\bLei\b|mi scusi', IT_ALL))
ck('nessun caporale e nessun carattere tipografico',
   not [v['idx'] for v in cov if any(c in v['italian'] for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026')])
rs = [v['ratio'] for v in cov]
ck('rapporto nel gate 0,55-1,90 (1,04 - 1,15, molto stretto)',
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
ck('25 unita tradotte prima della 581 (L223 12 + L224 13)',
   db.execute('select count(*) from units where path=? and line<581', (PATH,)).fetchone()[0] == 25)
ck('lotto + residuo = file: 25 + 11 + 21 = 57',
   25 + 11 + db.execute('select count(*) from units where path=? and line>674', (PATH,)).fetchone()[0] == 57)
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
