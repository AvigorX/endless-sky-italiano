r"""check.py — L234 (`data/avgi/avgi news.txt`, 20 unita', righe 115-180). Secondo lotto del file.

**20 `NEWS`**, tre contesti nuovi: `merchant` (10), `politician` (6), `military` (4). Nessun `VALUE`, nessun `UI_LABEL`,
nessun riferimento di dato, **zero tab**, **zero segnaposto**.

**19 unita' su 20 hanno l'etichetta di modalita'**; la **17** (riga 177) non ce l'ha ed e' una **domanda Avgi** nella
forma esplicita che finisce con `, question?` -> «, domanda?» (L48: «Tu umano, domanda?»). Un controllo che
pretendesse venti etichette sarebbe rosso su un lotto corretto: la lista ha un `None` in posizione 17 e il controllo la
confronta **con** quel `None`.

**Apici: 6 in inglese, 12 in italiano** — il contrario di L233: qui l'italiano elide piu' di quanto l'inglese contragga
(`l'avrebbero`, `L'unica`, `dall'Incursione`, `c'è`, `dell'Incursione`, `c'erano`, `all'Assemblea`, `l'economia`,
`all'altezza`, `l'altro`). Il confronto e' per unita' (decisione 202).

**`the Guard` -> «la Guardia»**: la questione lasciata aperta in L233 e' chiusa qui sulla forma dominante del corpus
(28 occorrenze di «la Guardia»).
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


ck("unita' tradotte 20/20", len(cov) == 20 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 20 NEWS', KINDS == {'NEWS': 20}, dict(KINDS))
ck('ZERO VALUE, TEXT, DIALOG, MISSION_TEXT, LOGBOOK, DESCRIPTION, UI_LABEL (asserzioni vuote scritte)',
   [u['idx'] for u in units if u['kind'] != 'NEWS'] == [])
ck('3 contesti con i conteggi misurati (merchant 10, politician 6, military 4)',
   len(CTX) == 3 and CTX == {'news:avgi merchant': 10, 'news:avgi politician': 6,
                             'news:avgi military': 4}, dict(CTX))
ck('righe 115 e 180 (prima e ultima del lotto)',
   (cov[0]['line'], cov[-1]['line']) == (115, 180), (cov[0]['line'], cov[-1]['line']))
ck('ZERO tab in inglese e in italiano (asserzione negativa scritta)',
   sum(v['english'].count(TAB) for v in cov) == 0 == sum(v['italian'].count(TAB) for v in cov))
ck('40 virgolette, 2 per unita\', in tutte e 20 le unita\' (citazione intera)',
   sum(v['english'].count(QUOTE) for v in cov) == 40 == sum(v['italian'].count(QUOTE) for v in cov)
   and [v['idx'] for v in cov if v['italian'].count(QUOTE) == 2] == list(range(1, 21)),
   [v['idx'] for v in cov if v['italian'].count(QUOTE) != 2])
ck('nessuna citazione spezzata: ogni unita\' comincia e finisce con le virgolette',
   not [v['idx'] for v in cov if not (v['italian'].startswith('"') and v['italian'].endswith('"'))])
ck('NESSUN segnaposto (asserzione negativa scritta)',
   sum(len(TAG.findall(v['english'])) for v in cov) == 0 == sum(len(TAG.findall(v['italian'])) for v in cov))
ck('0 unita\' IDENTICHE all\'inglese e 20 tradotte',
   sum(1 for v in cov if v['italian'] == v['english']) == 0
   and sum(1 for v in cov if v['italian'] != v['english']) == 20)
ck('19 etichette di modalita\' tradotte, con un None in posizione 17 (unita\' senza etichetta, misurata)',
   IT_LAB == ['Scoramento', 'Sollievo', 'Segretezza', 'Sfida', 'Dubbio', 'Ironia', 'Interesse', 'Orgoglio',
              'Soddisfazione', 'Tristezza', 'Esasperazione', 'Orgoglio', 'Derisione', 'Umorismo', 'Riserva',
              'Rassicurazione', None, 'Riflessione', 'Determinazione', 'Orgoglio'], IT_LAB)
ck('le etichette inglesi confermano la stessa forma: 19 etichette e un None in posizione 17',
   EN_LAB == ['Dejection', 'Relief', 'Secrecy', 'Defiance', 'Doubt', 'Irony', 'Intrigue', 'Pride', 'Satisfaction',
              'Sadness', 'Exasperation', 'Pride', 'Mocking', 'Humor', 'Reservation', 'Assurance', None, 'Pensive',
              'Resolve', 'Pride'], EN_LAB)
ck('l\'unita\' senza etichetta e\' la domanda Avgi: finisce con «, domanda?» (dispositivo di L48, riprodotto)',
   by[17]['italian'].endswith(', domanda?"') and by[17]['english'].endswith(', question?"')
   and IT_ALL.count('domanda?') == 1)
ck('nomi invariati: Consonance 2, Avgi 3, Tangled Shroud 2, Shroud 3, Stilacrest 1, skyhook 1',
   IT_ALL.count('Consonance') == 2 and IT_ALL.count('Avgi') == 3
   and IT_ALL.count('Tangled Shroud') == 2 and IT_ALL.count('Shroud') == 3
   and IT_ALL.count('Stilacrest') == 1 and IT_ALL.count('skyhook') == 1,
   (IT_ALL.count('Consonance'), IT_ALL.count('Avgi'), IT_ALL.count('Shroud')))
ck('`Aberrations` e `Aberrant` resi con lo stesso nome della fazione: «Aberrant» 7 (5 + 2 forme plurali)',
   IT_ALL.count('Aberrant') == 7 and 'Aberration' not in IT_ALL and 'Aberrazione' not in IT_ALL,
   IT_ALL.count('Aberrant'))
ck('istituzioni e lessico politico: Assemblea 2, Incursione 2, Guardia 1, «entità politiche» 2',
   IT_ALL.count('Assemblea') == 2 and IT_ALL.count('Incursione') == 2
   and IT_ALL.count('Guardia') == 1 and IT_ALL.count('entità politiche') == 2)
ck('lessico economico del lotto: «economia di guerra», «austerità», «quote»',
   'economia di guerra' in IT_ALL and 'austerità' in IT_ALL and 'quote' in IT_ALL)
ck('lessico militare ed editoriale: «fogli di memoria», «paggetto», «nave corriere»',
   'fogli di memoria' in IT_ALL and 'paggetto' in IT_ALL and 'nave corriere' in IT_ALL)
ck('nessun residuo inglese di struttura (the, of the, and, with, their, while)',
   not [w for w in (' the ', ' of the ', ' and ', ' with ', ' their ', ' while ')
        if w in IT_ALL.lower()],
   [w for w in (' the ', ' of the ', ' and ', ' with ', ' their ', ' while ') if w in IT_ALL.lower()])
ck("apici: 6 in inglese (5, 6, 9, 10, 11, 16) e 12 in italiano (5, 6, 9, 11x2, 12x2, 13, 15, 18, 19, 20)",
   sum(n for _, n in EN_A) == 6 and sum(n for _, n in IT_A) == 12
   and EN_A == [(5, 1), (6, 1), (9, 1), (10, 1), (11, 1), (16, 1)]
   and IT_A == [(5, 1), (6, 1), (9, 1), (11, 2), (12, 2), (13, 1), (15, 1), (18, 1), (19, 1), (20, 1)],
   (EN_A, IT_A))
ck('registro: nessun «Lei» e nessun «mi scusi»', not re.search(r'\bLei\b|mi scusi', IT_ALL))
ck('nessun caporale e nessun carattere tipografico',
   not [v['idx'] for v in cov if any(c in v['italian'] for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026')])
rs = [v['ratio'] for v in cov]
ck('rapporto nel gate 0,55-1,90 (0,90-1,28; 439 -> 433 parole)',
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
ck('22 unita\' tradotte prima della 115 (L233: righe 32-91)',
   db.execute('select count(*) from units where path=? and line<115', (PATH,)).fetchone()[0] == 22)
ck("73 unita' dopo la 180 (115 - 22 - 20): il lotto NON chiude il file",
   db.execute('select count(*) from units where path=? and line>180', (PATH,)).fetchone()[0] == 73)
ck('lotto + prima + dopo = file: 20 + 22 + 73 = 115',
   20 + db.execute('select count(*) from units where path=? and line<115', (PATH,)).fetchone()[0]
   + db.execute('select count(*) from units where path=? and line>180', (PATH,)).fetchone()[0] == 115)
ck('il file intero: 115 unita, righe 32 - 507',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (115, 32, 507))
st = dict(db.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('le 20 unita sono PENDING (misurato)',
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
