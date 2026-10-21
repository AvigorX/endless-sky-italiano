r"""check.py — L237 (`data/avgi/avgi news.txt`, 14 unita', righe 369-399). Quinto lotto del file.

**Fisici (8 unita', 369-376) e astronomi (6, 394-399)**: quattordici citazioni intere, 2 virgolette ciascuna, zero tab,
zero segnaposto. Il testo e' tecnico e ogni unita' porta l'etichetta di modalita' in testa.

**Un refuso del sorgente, dichiarato e non replicato**: le unita' 370 e 371 hanno l'etichetta `Frustation.` (senza la
prima `r`) invece di `Frustration.`. In italiano la parola e' **«Frustrazione»** in tutte e tre le unita' (370, 371, 397):
il refuso inglese non si trasporta. Il `check.py` pero' cita l'etichetta inglese **come sta nel sorgente** (`Frustation`
due volte, `Frustration` una), cosi' un cambio futuro del testo diventa rosso.

**`Twilight Nebula`**: il sorgente scrive il nome con la maiuscola in 394 e 396 e con la minuscola in 395
(`the Twilight nebula`). La resa usa **sempre la maiuscola** — e' il nome dell'oggetto, non una descrizione — e la
divergenza e' dichiarata: IT 3, EN 2.

**Otto apici in una sola unita'** (398): `'Nord'`, `'Ovest'`, `'senso di rotazione'`, `'verso il bordo'`. Le ultime due
sono la resa di `'spinward'` e `'rimward'`, gergo galattico tradotto e dichiarato in `review.md`.
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


ck("unita' tradotte 14/14", len(cov) == 14 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 14 NEWS', KINDS == {'NEWS': 14}, dict(KINDS))
ck('ZERO VALUE, TEXT, DIALOG, MISSION_TEXT, LOGBOOK, DESCRIPTION, UI_LABEL (asserzioni vuote scritte)',
   [u['idx'] for u in units if u['kind'] != 'NEWS'] == [])
ck('2 contesti con i conteggi misurati (physicist 8, astronomer 6)',
   len(CTX) == 2 and CTX == {'news:avgi physicist': 8, 'news:avgi astronomer': 6}, dict(CTX))
ck('righe 369 e 399 (prima e ultima del lotto)',
   (cov[0]['line'], cov[-1]['line']) == (369, 399), (cov[0]['line'], cov[-1]['line']))
ck('ZERO tab in inglese e in italiano (asserzione negativa scritta)',
   sum(v['english'].count(TAB) for v in cov) == 0 == sum(v['italian'].count(TAB) for v in cov))
ck('28 virgolette, 2 per unita\', in tutte e 14 le unita\'',
   sum(v['english'].count(QUOTE) for v in cov) == 28 == sum(v['italian'].count(QUOTE) for v in cov)
   and [v['idx'] for v in cov if v['italian'].count(QUOTE) == 2] == list(range(1, 15)),
   [v['idx'] for v in cov if v['italian'].count(QUOTE) != 2])
ck('ogni unita\' e\' una citazione intera: comincia e finisce con le virgolette',
   not [v['idx'] for v in cov if not (v['italian'].startswith('"') and v['italian'].endswith('"'))])
ck('NESSUN segnaposto (asserzione negativa scritta)',
   sum(len(TAG.findall(v['english'])) for v in cov) == 0 == sum(len(TAG.findall(v['italian'])) for v in cov))
ck('0 unita\' IDENTICHE all\'inglese e 14 tradotte',
   sum(1 for v in cov if v['italian'] == v['english']) == 0
   and sum(1 for v in cov if v['italian'] != v['english']) == 14)
ck('etichette: tutte e 14 tradotte, con «Frustrazione» tre volte',
   IT_LAB == ['Gratitudine', 'Frustrazione', 'Frustrazione', 'Orgoglio', 'Divertimento', 'Curiosità', 'Informazione',
              'Stupore', 'Istruttivo', 'Curioso', 'Insegnamento', 'Frustrazione', 'Fastidio', 'Curiosità'], IT_LAB)
ck('REFUSO del sorgente: `Frustation` due volte e `Frustration` una, citate come stanno',
   EN_LAB == ['Gratitude', 'Frustation', 'Frustation', 'Pride', 'Amusement', 'Curiosity', 'Information', 'Amazement',
              'Instructive', 'Inquisitive', 'Tutelage', 'Frustration', 'Annoyance', 'Curiosity']
   and EN_LAB.count('Frustation') == 2 and EN_LAB.count('Frustration') == 1, EN_LAB)
ck('il refuso NON si trasporta: in italiano «Frustrazione» 3 volte, «Frustation» mai',
   IT_ALL.count('Frustrazione') == 3 and 'Frustation' not in IT_ALL)
ck('`Twilight Nebula` sempre con la maiuscola (IT 3, EN 2: il sorgente scrive `nebula` minuscolo in una unita\')',
   IT_ALL.count('Twilight Nebula') == 3 and EN_ALL.count('Twilight Nebula') == 2
   and 'Twilight nebula' in EN_ALL and 'Twilight nebula' not in IT_ALL,
   (IT_ALL.count('Twilight Nebula'), EN_ALL.count('Twilight Nebula')))
ck('terminologia tecnica: «iperpropulsore» 2, `wormhole` invariato 1, «vie stellari», «stelle di neutroni»',
   IT_ALL.count('iperpropulsore') == 2 and IT_ALL.count('wormhole') == 1
   and 'vie stellari' in IT_ALL and 'stelle di neutroni' in IT_ALL
   and 'hyperdrive' not in IT_ALL)
ck('astronomia: «nebulosa a riflessione», «nube molecolare», «equilibrio idrostatico», «vivaio stellare»',
   'nebulosa a riflessione' in IT_ALL and 'nube molecolare' in IT_ALL
   and 'equilibrio idrostatico' in IT_ALL and 'vivaio stellare' in IT_ALL)
ck('tecnica: «vortici di scia», «diamante di memoria», «resistenza aerodinamica», «giunzione per celle solari»',
   'vortici di scia' in IT_ALL and 'diamante di memoria' in IT_ALL
   and 'resistenza aerodinamica' in IT_ALL and 'giunzione per celle solari' in IT_ALL)
ck('il gergo galattico e\' stato tradotto (dichiarato in review.md): «senso di rotazione» e «verso il bordo»',
   "'senso di rotazione'" in IT_ALL and "'verso il bordo'" in IT_ALL
   and 'spinward' not in IT_ALL and 'rimward' not in IT_ALL)
ck('`Stream` invariato (1) e i punti cardinali tradotti: «Nord», «Ovest»',
   IT_ALL.count('Stream') == 1 == EN_ALL.count('Stream') and "'Nord'" in IT_ALL and "'Ovest'" in IT_ALL)
ck('nessun gruppo di inglese identico dentro il lotto (0 gruppi: 14 stringhe tutte diverse)',
   {k: v for k, v in collections.Counter(v['english'] for v in cov).items() if v > 1} == {})
ck('nessuna cifra in inglese e nessuna in italiano (i numeri del lotto sono tutti in lettere)',
   [v['idx'] for v in cov if re.search(r'\d', v['english'])] == []
   and [v['idx'] for v in cov if re.search(r'\d', v['italian'])] == [])
ck('nessun residuo inglese di struttura (the, of the, and, with, their, while)',
   not [w for w in (' the ', ' of the ', ' and ', ' with ', ' their ', ' while ')
        if w in IT_ALL.lower()],
   [w for w in (' the ', ' of the ', ' and ', ' with ', ' their ', ' while ') if w in IT_ALL.lower()])
ck("apici: 11 in inglese su 4 unita' (6, 7, 12, 13) e 14 in italiano su 6 unita', con 8 in una sola",
   sum(n for _, n in EN_A) == 11 and sum(n for _, n in IT_A) == 14
   and EN_A == [(6, 1), (7, 1), (12, 1), (13, 8)]
   and IT_A == [(3, 1), (5, 1), (6, 2), (10, 1), (13, 8), (14, 1)], (EN_A, IT_A))
ck('registro: nessun «Lei» e nessun «mi scusi»', not re.search(r'\bLei\b|mi scusi', IT_ALL))
ck('nessun caporale e nessun carattere tipografico',
   not [v['idx'] for v in cov if any(c in v['italian'] for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026')])
rs = [v['ratio'] for v in cov]
ck('rapporto nel gate 0,55-1,90 (0,94-1,21; 356 -> 354 parole)',
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
ck("80 unita' tradotte prima della 369 (L233-L236)",
   db.execute('select count(*) from units where path=? and line<369', (PATH,)).fetchone()[0] == 80)
ck("21 unita' dopo la 399 (115 - 80 - 14): il lotto NON chiude il file",
   db.execute('select count(*) from units where path=? and line>399', (PATH,)).fetchone()[0] == 21)
ck('lotto + prima + dopo = file: 14 + 80 + 21 = 115',
   14 + db.execute('select count(*) from units where path=? and line<369', (PATH,)).fetchone()[0]
   + db.execute('select count(*) from units where path=? and line>399', (PATH,)).fetchone()[0] == 115)
ck('il file intero: 115 unita, righe 32 - 507',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (115, 32, 507))
st = dict(db.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('le 14 unita sono PENDING (misurato)',
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
