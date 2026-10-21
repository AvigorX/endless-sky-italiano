r"""check.py — L236 (`data/avgi/avgi news.txt`, 23 unita', righe 301-344). Quarto lotto del file.

**Si torna alla citazione intera** (2 virgolette per unita', 46 in tutto) dopo il lotto di composizione L235, ma con tre
trapole proprie:

1. **tre coppie di inglese identico dentro la finestra** — 10/20 (`Have you seen my homework, question?`), 12/22 e 13/23
   (`Annoyance. The quality of education out here just isn't the same as back on …`). La resa **deve** essere identica
   dentro la coppia, e il controllo confronta le stringhe, non solo i conteggi;
2. **una coppia quasi identica che deve restare distinta** — 11 e 21 dicono la stessa cosa ma finiscono con
   `…, amusement.` / `…, dejection.` -> `…, divertimento.` / `…, scoramento.`. E' l'unico punto del file in cui
   l'**etichetta sta in coda**, minuscola, dentro la citazione;
3. **quattro unita' senza etichetta in testa** (10, 11, 20, 21): sono domande e battute. La lista ha `None` in quelle
   posizioni e il controllo la confronta **con** i `None`.

**18 apici in inglese e 14 in italiano**, ma non sono la stessa cosa: in inglese ci sono le contrazioni (`I'm`, `can't`,
`isn't`, `don't`) **e** le virgolette semplici `'practical'`, `'useful'`; in italiano le elisioni (`l'ora`,
`dell'istruzione`, `all'ultimo`…) **e** le stesse virgolette semplici. Il confronto e' per unita' (decisione 202).
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
DUP_PAIRS = [(10, 20), (12, 22), (13, 23)]
NEAR_PAIR = (11, 21)
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


ck("unita' tradotte 23/23", len(cov) == 23 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 23 NEWS', KINDS == {'NEWS': 23}, dict(KINDS))
ck('ZERO VALUE, TEXT, DIALOG, MISSION_TEXT, LOGBOOK, DESCRIPTION, UI_LABEL (asserzioni vuote scritte)',
   [u['idx'] for u in units if u['kind'] != 'NEWS'] == [])
ck('2 contesti con i conteggi misurati (student happy 13, student frustrated 10)',
   len(CTX) == 2 and CTX == {'news:avgi student happy': 13, 'news:avgi student frustrated': 10}, dict(CTX))
ck('righe 301 e 344 (prima e ultima del lotto)',
   (cov[0]['line'], cov[-1]['line']) == (301, 344), (cov[0]['line'], cov[-1]['line']))
ck('ZERO tab in inglese e in italiano (asserzione negativa scritta)',
   sum(v['english'].count(TAB) for v in cov) == 0 == sum(v['italian'].count(TAB) for v in cov))
ck('46 virgolette, 2 per unita\', in tutte e 23 le unita\'',
   sum(v['english'].count(QUOTE) for v in cov) == 46 == sum(v['italian'].count(QUOTE) for v in cov)
   and [v['idx'] for v in cov if v['italian'].count(QUOTE) == 2] == list(range(1, 24)),
   [v['idx'] for v in cov if v['italian'].count(QUOTE) != 2])
ck('ogni unita\' e\' una citazione intera: comincia e finisce con le virgolette',
   not [v['idx'] for v in cov if not (v['italian'].startswith('"') and v['italian'].endswith('"'))])
ck('NESSUN segnaposto (asserzione negativa scritta)',
   sum(len(TAG.findall(v['english'])) for v in cov) == 0 == sum(len(TAG.findall(v['italian'])) for v in cov))
ck('0 unita\' IDENTICHE all\'inglese e 23 tradotte',
   sum(1 for v in cov if v['italian'] == v['english']) == 0
   and sum(1 for v in cov if v['italian'] != v['english']) == 23)
ck('19 etichette in testa e 4 None (unita\' 10, 11, 20, 21: domande e battute)',
   IT_LAB == ['Felicità', 'Felicità', 'Felicità', 'Felicità', 'Felicità', 'Felicità', 'Entusiasmo', 'Gratitudine',
              'Gioia', None, None, 'Fastidio', 'Fastidio', 'Frustrazione', 'Abbattimento', 'Rabbia', 'Rabbia',
              'Preoccupazione', 'Preoccupazione', None, None, 'Fastidio', 'Fastidio'], IT_LAB)
ck('le etichette inglesi confermano la stessa forma (19 + 4 None nelle stesse posizioni)',
   EN_LAB == ['Happiness', 'Happiness', 'Happiness', 'Happiness', 'Happiness', 'Happiness', 'Enthusiasm', 'Gratitude',
              'Joy', None, None, 'Annoyance', 'Annoyance', 'Frustration', 'Depression', 'Anger', 'Anger', 'Worry',
              'Worry', None, None, 'Annoyance', 'Annoyance'], EN_LAB)
ck('le sei unita\' 1-6 differiscono solo per la disciplina, e la formula e\' identica in tutte e sei',
   len({v['italian'].replace('fisica', 'X').replace('economia', 'X').replace('ingegneria', 'X')
        .replace('nanotecnologia', 'X').replace('genetica', 'X').replace('aerodinamica', 'X')
        for v in cov[:6]}) == 1)
ck('le tre coppie di inglese identico hanno la STESSA resa italiana (10/20, 12/22, 13/23)',
   all(by[a]['english'] == by[b]['english'] and by[a]['italian'] == by[b]['italian'] for a, b in DUP_PAIRS)
   and collections.Counter(by[i]['english'] for i in (10, 20, 12, 22, 13, 23)).most_common(1)[0][1] == 2,
   [(a, b, by[a]['italian'] == by[b]['italian']) for a, b in DUP_PAIRS])
ck('la coppia quasi identica 11/21 resta DISTINTA: stesso testo tranne l\'etichetta in coda',
   by[11]['italian'] != by[21]['italian']
   and by[11]['italian'].rsplit(' ', 1)[0] == by[21]['italian'].rsplit(' ', 1)[0]
   and by[11]['italian'].endswith(', divertimento."') and by[21]['italian'].endswith(', scoramento."'),
   (by[11]['italian'][-30:], by[21]['italian'][-30:]))
ck('le due etichette in coda sono minuscole, come nell\'inglese (`amusement.` / `dejection.`)',
   ', divertimento."' in IT_ALL and ', scoramento."' in IT_ALL
   and ', Amusement."' not in IT_ALL and ', Dejection."' not in IT_ALL)
ck('la domanda Avgi conserva il dispositivo «, domanda?» (2 volte, come l\'inglese «, question?»)',
   IT_ALL.count(', domanda?') == 2 == EN_ALL.count(', question?'))
ck('le virgolette semplici dentro la citazione sono riprodotte: \'pratiche\' e \'utile\'',
   "'pratiche'" in IT_ALL and "'utile'" in IT_ALL
   and "'practical'" in EN_ALL and "'useful'" in EN_ALL)
ck('nomi invariati: Aviskir 2, Livloua 2, Aberrant 2; tradotti: Assemblea, Guerra, xenologia',
   IT_ALL.count('Aviskir') == 2 == EN_ALL.count('Aviskir') and IT_ALL.count('Livloua') == 2 == EN_ALL.count('Livloua')
   and IT_ALL.count('Aberrant') == 2 == EN_ALL.count('Aberrant')
   and IT_ALL.count('Assemblea') == 1 and IT_ALL.count('Guerra') == 1 and IT_ALL.count('xenologia') == 1)
ck('lessico universitario: «laurea magistrale» 7, «accademia», «esami intermedi», «cantieri»',
   IT_ALL.count('laurea magistrale') == 7 and 'accademia' in IT_ALL
   and 'esami intermedi' in IT_ALL and 'cantieri' in IT_ALL)
ck('nessun residuo inglese di struttura (the, of the, and, with, their, while)',
   not [w for w in (' the ', ' of the ', ' and ', ' with ', ' their ', ' while ')
        if w in IT_ALL.lower()],
   [w for w in (' the ', ' of the ', ' and ', ' with ', ' their ', ' while ') if w in IT_ALL.lower()])
ck("apici: 18 in inglese su 15 unita' e 14 in italiano su 10 unita' (contrazioni + virgolette semplici)",
   sum(n for _, n in EN_A) == 18 and sum(n for _, n in IT_A) == 14
   and EN_A == [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (12, 1), (13, 1), (14, 2), (17, 3),
                (18, 1), (19, 1), (22, 1), (23, 1)]
   and IT_A == [(7, 2), (8, 1), (12, 1), (13, 1), (14, 3), (15, 1), (17, 2), (19, 1), (22, 1), (23, 1)],
   (EN_A, IT_A))
ck('registro: nessun «Lei» e nessun «mi scusi»', not re.search(r'\bLei\b|mi scusi', IT_ALL))
ck('nessun caporale e nessun carattere tipografico',
   not [v['idx'] for v in cov if any(c in v['italian'] for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026')])
ck('i tre punti restano tre punti (unita\' 14), mai l\'ellissi tipografica',
   by[14]['italian'].endswith('...\"') and '\u2026' not in IT_ALL)
rs = [v['ratio'] for v in cov]
ck('rapporto nel gate 0,55-1,90 (0,88-1,58; 348 -> 320 parole)',
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
ck("57 unita' tradotte prima della 301 (L233 22 + L234 20 + L235 15)",
   db.execute('select count(*) from units where path=? and line<301', (PATH,)).fetchone()[0] == 57)
ck("35 unita' dopo la 344 (115 - 57 - 23): il lotto NON chiude il file",
   db.execute('select count(*) from units where path=? and line>344', (PATH,)).fetchone()[0] == 35)
ck('lotto + prima + dopo = file: 23 + 57 + 35 = 115',
   23 + db.execute('select count(*) from units where path=? and line<301', (PATH,)).fetchone()[0]
   + db.execute('select count(*) from units where path=? and line>344', (PATH,)).fetchone()[0] == 115)
ck('il file intero: 115 unita, righe 32 - 507',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (115, 32, 507))
st = dict(db.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('le 23 unita sono PENDING (misurato)',
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
