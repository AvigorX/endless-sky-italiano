r"""check.py — L233 (`data/avgi/avgi news.txt`, 22 unita', righe 32-91). Primo lotto del file.

**Tutte e 22 le unita' sono `NEWS`**: nessun `VALUE`, nessun `UI_LABEL`, nessun riferimento di dato. E' il lotto piu'
omogeneo della campagna recente, e il rischio non e' la forma ma il **registro**: ogni notizia Avgi comincia con
l'**etichetta di modalita'** (`Dejection.`, `Rejection.`, `Guilt.`…) e l'etichetta va riprodotta come etichetta.

**Ogni unita' e' una citazione intera**: due virgolette, aperte e chiuse dentro l'unita' (44 in tutto). Il contrario di
`coalition news.txt`, dove la citazione si spezzava su piu' unita': qui il criterio e' `2 == count('"')` per unita'.

**Zero tab** (nessun `MISSION_TEXT`, nessun separatore di paragrafo) e **zero segnaposto**: due asserzioni negative
scritte, non omesse.

**12 apici inglesi contro 5 italiani**: l'inglese contrae (`I've`, `wouldn't`, `We'd`, `can't`, `aren't`, `We're`,
`it's`, `don't`, `I'll`), l'italiano elide (`All'inizio`, `l'assedio`, `l'Assemblea`, `d'origine`, `Com'è`). Il
controllo confronta le coppie `(unita', conteggio)`, non i totali (decisione 202).
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
LABEL = re.compile(r'^"([A-Za-zÀ-ÿ]+)\. ')
HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
PATH = 'data/avgi/avgi news.txt'
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
EN_A = [(v['idx'], v['english'].count(APOS)) for v in cov if APOS in v['english']]
IT_A = [(v['idx'], v['italian'].count(APOS)) for v in cov if APOS in v['italian']]
IT_LAB = [LABEL.match(v['italian']).group(1) if LABEL.match(v['italian']) else None for v in cov]
EN_LAB = [LABEL.match(v['english']).group(1) if LABEL.match(v['english']) else None for v in cov]
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 22/22", len(cov) == 22 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 22 NEWS', KINDS == {'NEWS': 22}, dict(KINDS))
ck('ZERO VALUE, TEXT, DIALOG, MISSION_TEXT, LOGBOOK, DESCRIPTION, UI_LABEL (asserzioni vuote scritte)',
   [u['idx'] for u in units if u['kind'] != 'NEWS'] == [])
ck("3 contesti con i conteggi misurati (civilian 11, merchant 5, hatchling 6)",
   len(CTX) == 3 and CTX == {'news:avgi siege civilian': 11, 'news:avgi siege merchant': 5,
                             'news:avgi siege hatchling': 6}, dict(CTX))
ck('righe 32 e 91 (prima e ultima del lotto; la 32 e\' la prima unita\' del file)',
   (cov[0]['line'], cov[-1]['line']) == (32, 91), (cov[0]['line'], cov[-1]['line']))
ck('ZERO tab in inglese e in italiano (asserzione negativa scritta)',
   sum(v['english'].count(TAB) for v in cov) == 0 == sum(v['italian'].count(TAB) for v in cov))
ck('44 virgolette, 2 per unita\', in tutte e 22 le unita\' (citazione intera, non spezzata)',
   sum(v['english'].count(QUOTE) for v in cov) == 44 == sum(v['italian'].count(QUOTE) for v in cov)
   and [v['idx'] for v in cov if v['italian'].count(QUOTE) == 2] == list(range(1, 23)),
   [v['idx'] for v in cov if v['italian'].count(QUOTE) != 2])
ck('nessuna citazione spezzata: ogni unita\' comincia e finisce con le virgolette',
   not [v['idx'] for v in cov if not (v['italian'].startswith('"') and v['italian'].endswith('"'))])
ck('NESSUN segnaposto (asserzione negativa scritta)',
   sum(len(TAG.findall(v['english'])) for v in cov) == 0 == sum(len(TAG.findall(v['italian'])) for v in cov))
ck('0 unita\' IDENTICHE all\'inglese e 22 tradotte',
   sum(1 for v in cov if v['italian'] == v['english']) == 0
   and sum(1 for v in cov if v['italian'] != v['english']) == 22)
ck('le 22 etichette di modalita\' ci sono tutte e sono tradotte (nessuna resta inglese)',
   IT_LAB == ['Scoramento', 'Rifiuto', 'Ricordo', 'Ricordo', 'Colpa', 'Preoccupazione', 'Dolore', 'Rabbia',
              'Curiosità', 'Soddisfazione', 'Ottimismo', 'Sollievo', 'Frustrazione', 'Placazione', 'Esasperazione',
              'Frustrazione', 'Meraviglia', 'Confusione', 'Tristezza', 'Offesa', 'Perdita', 'Disperazione'], IT_LAB)
ck('le etichette inglesi sono 22 e distinte dove l\'inglese distingue (Remembrance e Frustration due volte)',
   EN_LAB == ['Dejection', 'Rejection', 'Remembrance', 'Remembrance', 'Guilt', 'Worry', 'Sorrow', 'Anger',
              'Curiosity', 'Satisfaction', 'Optimism', 'Relief', 'Frustration', 'Appeasing', 'Exasperation',
              'Frustration', 'Wonder', 'Confusion', 'Sadness', 'Hurt', 'Loss', 'Despair'], EN_LAB)
ck('nomi invariati: Consonance 3, Avgi 3, Tangled Shroud 2, Shroud 4, skyhook 1, Anax 1, Nisos 1',
   IT_ALL.count('Consonance') == 3 and IT_ALL.count('Avgi') == 3
   and IT_ALL.count('Tangled Shroud') == 2 and IT_ALL.count('Shroud') == 4
   and IT_ALL.count('skyhook') == 1 and IT_ALL.count('Anax') == 1 and IT_ALL.count('Nisos') == 1,
   (IT_ALL.count('Consonance'), IT_ALL.count('Avgi'), IT_ALL.count('Tangled Shroud')))
ck('`Aberrations` e `Aberration` resi con lo stesso nome della fazione: «Aberrant» 7 (5 + 2 forme inglesi)',
   IT_ALL.count('Aberrant') == 7 and 'Aberration' not in IT_ALL and 'Aberrazione' not in IT_ALL,
   IT_ALL.count('Aberrant'))
ck('istituzioni e nomi comuni tradotti: Assemblea, Nucleo, habitat cilindrici (2), Cilindro Nisos',
   IT_ALL.count('Assemblea') == 1 and IT_ALL.count('Nucleo') == 1
   and IT_ALL.count('habitat cilindrici') == 2 and 'Cilindro Nisos' in IT_ALL)
ck('lessico tecnico del lotto: «batterie laser terra-orbita», «missili nucleari superficie-orbita»',
   'batterie laser terra-orbita' in IT_ALL and 'missili nucleari superficie-orbita' in IT_ALL)
ck('lessico civile: «forzare un blocco», «di contrabbando», «quota di evacuazione», «a occhio nudo»',
   'forzare un blocco' in IT_ALL and 'di contrabbando' in IT_ALL
   and 'quota di evacuazione' in IT_ALL and 'a occhio nudo' in IT_ALL)
ck('il numero resta in lettere: «Dodici milioni», non «12 milioni»',
   'Dodici milioni' in IT_ALL and '12 milioni' not in IT_ALL)
ck('nessun residuo inglese di struttura (the, of the, and, with, their, while)',
   not [w for w in (' the ', ' of the ', ' and ', ' with ', ' their ', ' while ')
        if w in IT_ALL.lower()],
   [w for w in (' the ', ' of the ', ' and ', ' with ', ' their ', ' while ') if w in IT_ALL.lower()])
ck("apici: 12 in inglese su 9 unita' e 5 in italiano su 5 unita' (contrazione contro elisione)",
   sum(n for _, n in EN_A) == 12 and sum(n for _, n in IT_A) == 5
   and EN_A == [(9, 1), (12, 1), (13, 1), (14, 1), (15, 2), (16, 2), (17, 1), (18, 1), (19, 2)]
   and IT_A == [(3, 1), (11, 1), (14, 1), (16, 1), (18, 1)], (EN_A, IT_A))
ck('registro: nessun «Lei» e nessun «mi scusi»', not re.search(r'\bLei\b|mi scusi', IT_ALL))
ck('nessun caporale e nessun carattere tipografico',
   not [v['idx'] for v in cov if any(c in v['italian'] for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026')])
rs = [v['ratio'] for v in cov]
ck('rapporto nel gate 0,55-1,90 (0,93-1,25; 447 -> 441 parole)',
   0.55 < min(rs) and max(rs) < 1.90, '%.2f - %.2f' % (min(rs), max(rs)))
ACC = re.compile(r"\b(e|piu|perche|cosi|gia|puo|cioe|percio|fa)'", re.I)
bad = [(v['idx'], ACC.search(v['italian']).group(0)) for v in cov if ACC.search(v['italian'])]
ck("tipografia (accenti veri, nessun apostrofo al posto dell'accento)", not bad, bad)
nonlat = [v['idx'] for v in cov for c in v['italian'] if ord(c) > 127 and not 0x00C0 <= ord(c) <= 0x024F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio',
   not [v['idx'] for v in cov if v['italian'] != v['italian'].rstrip()
        or '  ' in v['italian'] or v['english'] != v['english'].rstrip()])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck('la 32 e\' la PRIMA unita\' del file: zero unita\' prima',
   db.execute('select count(*) from units where path=? and line<32', (PATH,)).fetchone()[0] == 0)
ck("93 unita' dopo la 91 (115 - 22): il lotto NON chiude il file",
   db.execute('select count(*) from units where path=? and line>91', (PATH,)).fetchone()[0] == 93)
ck('lotto + residuo = file: 22 + 93 = 115',
   22 + db.execute('select count(*) from units where path=? and line>91', (PATH,)).fetchone()[0] == 115)
ck('il file intero: 115 unita, righe 32 - 507',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (115, 32, 507))
st = dict(db.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('le 22 unita sono PENDING (misurato)',
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
