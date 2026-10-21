r"""check.py — L224 (`data/remnant/remnant outfits.txt`, 13 unita', righe 298-565). Secondo lotto del file.

**Primato del lotto**: **zero unita' da copiare** — 13 `DESCRIPTION` su 13, nessun `VALUE` e nessun `TEXT`. Il confronto
«identiche / tradotte» vale quindi **0 / 13**, e va scritto: un controllo che si aspetta «qualche unita' identica» qui
sarebbe sbagliato.

**Tre unita' ripetono la stessa frase**: 1, 5 e 8 dicono tutte *Ammunition for this weapon can be restocked at any
outfitter.* Tre equipaggiamenti diversi, la stessa riga di servizio: la resa deve essere **identica nelle tre**.

**Una frase torna da L223**: *Electromagnetic pulse weapons were [originally] developed by the Remnant during the early days
of their colony…* era gia' stata resa nell'unita' 12 del lotto precedente; qui c'e' `originally` in piu', e la resa lo
registra («furono sviluppate originariamente»).
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
AMMO = ('\tLe munizioni per quest\'arma possono essere rifornite presso qualsiasi negozio di equipaggiamenti.')
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 13/13", len(cov) == 13 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 13 DESCRIPTION, nient\'altro (primato: zero unita\' da copiare)',
   KINDS == {'DESCRIPTION': 13}, dict(KINDS))
ck('ZERO VALUE, TEXT, DIALOG, MISSION_TEXT, LOGBOOK, NEWS, UI_LABEL (asserzioni vuote scritte)',
   [u['idx'] for u in units if u['kind'] != 'DESCRIPTION'] == [])
ck('5 contesti con le dimensioni misurate: Teciimach Bay 4, Teciimach Pod 3, Ember Tear 3, Crystal Capacitor 2, EMP Torpedo Bay 1',
   CTX == {'outfit:EMP Torpedo Bay': 1, 'outfit:Teciimach Bay': 4, 'outfit:Teciimach Pod': 3,
           'outfit:Ember Tear': 3, 'outfit:Crystal Capacitor': 2}, dict(CTX))
ck('righe 298 e 565 (prima e ultima del lotto)',
   (cov[0]['line'], cov[-1]['line']) == (298, 565), (cov[0]['line'], cov[-1]['line']))
ck('9 tab, nelle unita\' 1, 3, 4, 5, 7, 8, 10, 11, 13 — la densita\' piu\' alta della campagna',
   [v['idx'] for v in cov if TAB in v['english']] == [1, 3, 4, 5, 7, 8, 10, 11, 13]
   == [v['idx'] for v in cov if TAB in v['italian']]
   and sum(v['english'].count(TAB) for v in cov) == 9 == sum(v['italian'].count(TAB) for v in cov)
   and all(by[i]['italian'].startswith(TAB) for i in (1, 3, 4, 5, 7, 8, 10, 11, 13)))
ck('2 virgolette, entrambe nell\'unita\' 3 (il nome "Teciimach"), come in inglese',
   sum(v['english'].count(QUOTE) for v in cov) == 2 == sum(v['italian'].count(QUOTE) for v in cov)
   and [v['idx'] for v in cov if QUOTE in v['italian']] == [3]
   and 'il "Teciimach", contiene' in by[3]['italian'])
ck('NESSUN segnaposto (asserzione negativa scritta)',
   sum(len(TAG.findall(v['english'])) for v in cov) == 0 == sum(len(TAG.findall(v['italian'])) for v in cov))
ck('0 unita\' identiche all\'inglese e 13 tradotte: tutti i testi sono stati scritti',
   sum(1 for v in cov if v['italian'] == v['english']) == 0
   and all(v['italian'] != v['english'] for v in cov))
ck('le tre righe di servizio (unita\' 1, 5, 8) hanno la STESSA resa, carattere per carattere',
   by[1]['italian'] == by[5]['italian'] == by[8]['italian'] == AMMO)
ck('«munizioni» una volta per unita\' di servizio, tre in tutto',
   IT_ALL.count('Le munizioni per quest\'arma') == 3)
ck("coerenza con L223/12: la frase sugli impulsi elettromagnetici torna, con «originariamente» per il nuovo "
   "`originally` del sorgente",
   by[2]['italian'].startswith('Le armi a impulso elettromagnetico furono sviluppate originariamente dai Remnant')
   and 'originally' in by[2]['english']
   and 'furono sviluppate dai Remnant' not in by[2]['italian'])
ck('terminologia: «negozio di equipaggiamenti», «punti d\'attacco», «ioni»/«ionizzazione», «navi capitali»',
   'negozio di equipaggiamenti' in IT_ALL and "punti d'attacco" in IT_ALL
   and 'ionizzare' in IT_ALL and 'ionizzazione' in IT_ALL and 'navi capitali' in IT_ALL)
ck('nomi propri e nomi di equipaggiamento invariati: Remnant, Ember Waste, Viminal, Alphas, Teciimach, EMP Torpedo Bay',
   IT_ALL.count('Remnant') >= 6 and 'Ember Waste' in IT_ALL and 'Viminal' in IT_ALL
   and 'Alphas' in IT_ALL and 'Teciimach' in IT_ALL and 'EMP Torpedo Bay' in IT_ALL)
ck('nessun residuo inglese di struttura (the, of the, and, with, their)',
   not [w for w in (' the ', ' of the ', ' and ', ' with ', ' their ', ' while ', ' that they ')
        if w in IT_ALL.lower()],
   [w for w in (' the ', ' of the ', ' and ', ' with ', ' their ', ' while ', ' that they ') if w in IT_ALL.lower()])
ck("apici: 3 in inglese (3 torpedoes', 10 x2 'both') e 16 in italiano in 8 unita'",
   sum(n for _, n in EN_A) == 3 and sum(n for _, n in IT_A) == 16
   and EN_A == [(3, 1), (10, 2)]
   and IT_A == [(1, 1), (3, 3), (5, 1), (6, 1), (8, 1), (9, 3), (10, 5), (11, 1)], (EN_A, IT_A))
ck('la citazione \'both.\' e\' resa fra apici singoli, come il sorgente',
   "'entrambe le cose'" in by[10]['italian'])
ck('registro: nessun «Lei» e nessun «mi scusi»', not re.search(r'\bLei\b|mi scusi', IT_ALL))
ck('nessun caporale e nessun carattere tipografico (il trattino del sorgente resta semplice)',
   not [v['idx'] for v in cov if any(c in v['italian'] for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026')])
rs = [v['ratio'] for v in cov]
ck('rapporto nel gate 0,55-1,90 (le tre righe di servizio stanno a 1,58 per «negozio di equipaggiamenti»; max 1,58)',
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
ck('12 unita tradotte prima della 298 (L223)',
   db.execute('select count(*) from units where path=? and line<298', (PATH,)).fetchone()[0] == 12)
ck('lotto + residuo = file: 12 + 13 + 32 = 57',
   12 + 13 + db.execute('select count(*) from units where path=? and line>565', (PATH,)).fetchone()[0] == 57)
st = dict(db.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('le 13 unita sono PENDING (misurato)',
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
