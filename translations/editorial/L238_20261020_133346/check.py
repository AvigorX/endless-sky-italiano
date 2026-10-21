r"""check.py — L238 (`data/avgi/avgi news.txt`, 21 unita', righe 418-507). **LOTTO TERMINALE**: chiude il file a 115/115.

Quattro mestieri in un lotto solo: **ingegneri** (418-424, 7), **artisti** (452-454, 3), **artisti dello spettacolo**
(478-480, 3) e **medici** (500-507, 8). La finestra e' **discontinua** (425-451, 455-477, 481-499 non producono unita'):
non e' un buco di copertura.

**Cinque etichette nuove**, decise una volta e dichiarate in `review.md`: `Appreciation` -> «Apprezzamento» (3),
`Fascination` -> «Fascinazione» (2), `Consideration` -> «Considerazione» (2), `Recollection` -> «Rievocazione» (2,
distinta da `Remembrance` -> «Ricordo»), `Advisement` -> «Avviso» (cioe' la resa gia' nel corpus, non «Avvertenza»,
che e' `Warning`).

**Una etichetta a meta' frase** (454): `art is a waste, emphasis.` — l'Avgi dichiara la modalita' **dopo** una virgola e
in minuscolo. Non e' un refuso: e' lo stesso dispositivo di L236 (etichetta in coda), portato dentro il periodo. La resa
lo riproduce: «… uno spreco, enfasi.».

**`Twilight Guard` invariato** (30 occorrenze nello staging, decisione 16) e i **membri** tradotti («le Guardie»): il
nome e' un dato, la prosa no.
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
for p in sorted(f for f in os.listdir(os.path.join(HERE, 'parts')) if f.endswith('.json')):
    for k, v in json.load(open(os.path.join(HERE, 'parts', p), encoding='utf-8')).items():
        tr[int(k)] = v
out = {'block': src['block'], 'note': src['note'], 'units': []}
for u in units:
    if u['idx'] in tr:
        it = tr[u['idx']]
        out['units'].append({"idx": u['idx'], "id": u['id'], "path": u['path'], "line": u['line'],
                             "kind": u['kind'], "context": u['context'], "english": u['english'],
                             "italian": it, "ratio": round(len(it) / max(1, len(u['english'])), 3)})
open(os.path.join(HERE, 'translation.json'), 'w', encoding='utf-8').write(
    json.dumps(out, ensure_ascii=False, indent=1))
cov = out['units']
IT_ALL = ' '.join(v['italian'] for v in cov)
EN_ALL = ' '.join(v['english'] for v in cov)
KINDS = collections.Counter(u['kind'] for u in units)
CTX = collections.Counter(u['context'] for u in units)
EN_LAB = [LABEL.match(v['english']).group(1) if LABEL.match(v['english']) else None for v in cov]
IT_LAB = [LABEL.match(v['italian']).group(1) if LABEL.match(v['italian']) else None for v in cov]
EN_A = [(v['idx'], v['english'].count(APOS)) for v in cov if APOS in v['english']]
IT_A = [(v['idx'], v['italian'].count(APOS)) for v in cov if APOS in v['italian']]
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 21/21", len(cov) == 21 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 21 NEWS', KINDS == {'NEWS': 21}, dict(KINDS))
ck('ZERO VALUE, TEXT, DIALOG, MISSION_TEXT, LOGBOOK, DESCRIPTION, UI_LABEL (asserzioni vuote scritte)',
   [u['idx'] for u in units if u['kind'] != 'NEWS'] == [])
ck('4 contesti: engineer 7, artist 3, performer 3, doctor 8',
   CTX == {'news:avgi engineer': 7, 'news:avgi artist': 3,
           'news:avgi performer': 3, 'news:avgi doctor': 8}, dict(CTX))
ck('righe 418 e 507 (prima e ultima del lotto, ultima del FILE)',
   (cov[0]['line'], cov[-1]['line']) == (418, 507), (cov[0]['line'], cov[-1]['line']))
ck('la finestra e\' discontinua: nessuna unita\' fra 425-451, 455-477, 481-499',
   not [v['idx'] for v in cov if 425 <= v['line'] <= 451 or 455 <= v['line'] <= 477 or 481 <= v['line'] <= 499],
   [(v['idx'], v['line']) for v in cov])
ck('ZERO tab in inglese e in italiano (asserzione negativa scritta)',
   sum(v['english'].count(TAB) for v in cov) == 0 == sum(v['italian'].count(TAB) for v in cov))
ck("42 virgolette, 2 per unita', in tutte e 21",
   sum(v['english'].count(QUOTE) for v in cov) == 42 == sum(v['italian'].count(QUOTE) for v in cov)
   and [v['idx'] for v in cov if v['italian'].count(QUOTE) == 2] == list(range(1, 22)),
   [v['idx'] for v in cov if v['italian'].count(QUOTE) != 2])
ck("ogni unita' comincia e finisce con le virgolette",
   not [v['idx'] for v in cov if not (v['italian'].startswith('"') and v['italian'].endswith('"'))])
ck('NESSUN segnaposto (asserzione negativa scritta)',
   sum(len(TAG.findall(v['english'])) for v in cov) == 0 == sum(len(TAG.findall(v['italian'])) for v in cov))
ck("0 unita' identiche all'inglese e 21 tradotte",
   sum(1 for v in cov if v['italian'] == v['english']) == 0
   and sum(1 for v in cov if v['italian'] != v['english']) == 21)
ck('etichette in testa: 20 su 21, con l\'unita\' 10 SENZA etichetta (il None fa parte del confronto)',
   IT_LAB[:9] + IT_LAB[10:] == ['Fascinazione', 'Curiosità', 'Divertimento', 'Apprezzamento', 'Avviso',
                                'Apprezzamento', 'Fastidio', 'Orgoglio', 'Frustrazione',
                                'Orgoglio', 'Orgoglio', 'Soddisfazione', 'Apprezzamento', 'Divertimento',
                                'Fascinazione', 'Interesse', 'Considerazione', 'Considerazione',
                                'Rievocazione', 'Rievocazione']
   and EN_LAB[9] is None and IT_LAB[9] is None, (IT_LAB, EN_LAB))
ck('l\'etichetta a meta\' frase (unita\' 10, `emphasis`): «, enfasi.» dopo la virgola, in minuscolo',
   ', enfasi.' in cov[9]['italian'] and ', emphasis.' in cov[9]['english']
   and cov[9]['italian'].count('enfasi') == 1)
ck('5 etichette nuove, tutte con la resa decisa una volta: Apprezzamento 3, Fascinazione 2, Considerazione 2, Rievocazione 2, Avviso 1',
   IT_ALL.count('Apprezzamento') == 3 and IT_ALL.count('Fascinazione') == 2
   and IT_ALL.count('Considerazione') == 2 and IT_ALL.count('Rievocazione') == 2
   and IT_ALL.count('Avviso') == 1)
ck('`Recollection` NON diventa «Ricordo» (che e\' `Remembrance`, 2 precedenti): resa distinta',
   'Rievocazione' in IT_ALL and 'Ricordo' not in IT_ALL)
ck('`Advisement` NON diventa «Avvertenza» (che e\' `Warning`): resa dal corpus, «Avviso»',
   'Avviso' in IT_ALL and 'Avvertenza' not in IT_ALL)
ck('`Twilight Guard` invariato (30 precedenti) e i MEMBRI tradotti: «le Guardie»',
   'Twilight Guard' in IT_ALL and 'Guardie' in IT_ALL and 'Guards' not in IT_ALL)
ck('tecnica: «torcia a fusione», «navi a torcia», «nave mercantile a torcia»',
   'torcia a fusione' in IT_ALL and 'navi a torcia' in IT_ALL
   and 'nave mercantile a torcia' in IT_ALL and 'torchship' not in IT_ALL)
ck('biologia Avgi: «cervelli a forma di goccia», «quarzo opaco», «matrice cristallina», «mediciti»',
   'cervelli a forma di goccia' in IT_ALL and 'quarzo opaco' in IT_ALL
   and 'matrice cristallina' in IT_ALL and 'mediciti' in IT_ALL)
ck('industria: «acciaio-nichel», «habitat cilindrici», «manifattura su asteroide», «officina meccanica»',
   'acciaio-nichel' in IT_ALL and 'habitat cilindrici' in IT_ALL
   and 'manifattura su asteroide' in IT_ALL and "officina meccanica" in IT_ALL)
ck('misure e medicina: «sessant\'anni», «nanomedicina», «malattia da radiazioni», «danni da radiazioni»',
   "sessant'anni" in IT_ALL and 'nanomedicina' in IT_ALL
   and 'malattia da radiazioni' in IT_ALL and 'danni da radiazioni' in IT_ALL)
ck('nessun residuo inglese di struttura (the, of the, and, with, their, while, from)',
   not [w for w in (' the ', ' of the ', ' and ', ' with ', ' their ', ' while ', ' from ')
        if w in IT_ALL.lower()],
   [w for w in (' the ', ' of the ', ' and ', ' with ', ' their ', ' while ', ' from ')
    if w in IT_ALL.lower()])
ck("apici: 15 in inglese su 10 unita' e 20 in italiano su 11, con 4 in una sola (unita' 11)",
   sum(n for _, n in EN_A) == 15 and sum(n for _, n in IT_A) == 20
   and EN_A == [(1, 1), (4, 1), (5, 2), (7, 2), (9, 1), (10, 3), (11, 1), (12, 2), (19, 1), (21, 1)]
   and max(n for _, n in IT_A) == 4 and [i for i, n in IT_A if n == 4] == [11], (EN_A, IT_A))
ck('registro: nessun «Lei» e nessuna cortesia',
   not re.search(r'\bLei\b|\bSuo\b|\bSua\b|mi scusi|prego, si accomodi', IT_ALL))
ck('nessun caporale e nessun carattere tipografico',
   not [v['idx'] for v in cov if any(c in v['italian'] for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026')])
rs = [v['ratio'] for v in cov]
ck('rapporto nel gate 0,55-1,90 (0,95-1,23; 502 -> 508 parole)',
   0.55 < min(rs) and max(rs) < 1.90, '%.2f - %.2f' % (min(rs), max(rs)))
# solo le parole che in italiano portano un ACCENTO, mai un apostrofo: `un'opera` e `l'arte` sono elisioni corrette
ACC = re.compile(r"\b(e|piu|perche|cosi|gia|puo|cioe|percio|poiche|affinche)'(?![a-z])", re.I)
bad = [(v['idx'], ACC.search(v['italian']).group(0)) for v in cov if ACC.search(v['italian'])]
ck("tipografia (accenti veri, nessun apostrofo al posto dell'accento)", not bad, bad)
nonlat = [v['idx'] for v in cov for c in v['italian'] if ord(c) > 127 and not 0x00C0 <= ord(c) <= 0x024F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio',
   not [v['idx'] for v in cov if v['italian'] != v['italian'].rstrip() or '  ' in v['italian']])
ck('i tre puntini dell\'unita\' 501 sono tre punti semplici, non l\'ellissi tipografica',
   cov[14]['line'] == 501 and cov[14]['italian'].endswith('..."') and '\u2026' not in cov[14]['italian'],
   (cov[14]['line'], cov[14]['italian'][-14:]))
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck('94 unita\' tradotte prima della 418 (L233-L237)',
   db.execute('select count(*) from units where path=? and line<418', (PATH,)).fetchone()[0] == 94)
ck('ZERO unita\' dopo la 507: il lotto CHIUDE il file',
   db.execute('select count(*) from units where path=? and line>507', (PATH,)).fetchone()[0] == 0)
ck('il file intero: 115 unita, righe 32 - 507',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (115, 32, 507))
ck('94 + 21 = 115 = unita\' del file', 94 + 21 == 115)
st = dict(db.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('le 21 unita sono PENDING (misurato)',
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
