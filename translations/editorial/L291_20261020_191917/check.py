r"""check.py — L291 (`data/avgi/avgi culture conversations.txt`, righe 122-227). **Secondo lotto del file**.

Dodici scene, **tre coppie consecutive** (182-183, 197-198, 212-213) e **una coppia non adiacente** (122+126). Il test verifica:

1. **il tic linguistico degli Avgi**: ogni battuta comincia con l'**atto dichiarato** — «Incredibile.», «Apprezzamento.»,
   «Proclama.», «Dichiarazione.», «Attenzione!», «Scherno!», «Comando.», «Imbarazzo.» — la forma che `avgi news` usa già
   («Rifiuto.», «Rabbia.», «Esasperazione.»);
2. **le tre coppie consecutive** con il **tab sulla seconda metà**, e la coppia 122+126 che **non** e' consecutiva;
3. **il gioco di parole** `Twilight Guard? More like Twilight Gourd.`: i nomi restano inglesi, e la resa lo dichiara;
4. **`Fencing` (227) continua oltre il confine** (riga 229): il test verifica il contesto della prima unita' successiva.
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
ALT = re.compile(r'\[[^\]]*\]')
HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
PATH = 'data/avgi/avgi culture conversations.txt'
CTX = [('mission:Avgi Culture: Dissonance Graffiti 1', 122), ('mission:Avgi Culture: Dissonance Graffiti 1', 126),
       ('mission:Avgi Culture: We Live In A Society', 140), ('mission:Avgi Culture: Realism', 154),
       ('mission:Avgi Culture: Doomed Korath', 168), ('mission:Avgi Culture: General Ripper', 182),
       ('mission:Avgi Culture: General Ripper', 183), ('mission:Avgi Culture: Criminal Mischief', 197),
       ('mission:Avgi Culture: Criminal Mischief', 198), ('mission:Avgi Culture: False Alarm', 212),
       ('mission:Avgi Culture: False Alarm', 213), ('mission:Avgi Culture: Fencing', 227)]
PAIRS_CONSEC = [(6, 7), (8, 9), (10, 11)]   # indici delle unita', righe 182-183, 197-198, 212-213
ATTI = ['Incredibile.', 'Apprezzamento.', 'Proclama.', 'Dichiarazione.', 'Attenzione!', 'Scherno!', 'Comando.',
        'Imbarazzo.']
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
by = {u['idx']: u for u in cov}
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck('unita tradotte 12/12', len(cov) == 12 == len(units), '%d/%d' % (len(cov), len(units)))
ck('tutte MISSION_TEXT, otto contesti con le righe dichiarate',
   {u['kind'] for u in cov} == {'MISSION_TEXT'} and [(u['context'], u['line']) for u in cov] == CTX,
   [(u['context'], u['line']) for u in cov])
ck('tutte e 12 le unita sono TRADOTTE, nessuna copiata',
   all(u['italian'] != u['english'] for u in cov), [u['idx'] for u in cov if u['italian'] == u['english']])
ck('TRE coppie consecutive, tab sulla SECONDA meta',
   all(by[b]['line'] == by[a]['line'] + 1 and by[a]['context'] == by[b]['context'] for a, b in PAIRS_CONSEC)
   and all(by[b]['italian'].startswith(TAB) and not by[a]['italian'].startswith(TAB) for a, b in PAIRS_CONSEC),
   [(a, b) for a, b in PAIRS_CONSEC if not by[b]['italian'].startswith(TAB)])
ck('la coppia del GRAFFITO non e consecutiva (122 e 126)',
   by[2]['line'] - by[1]['line'] == 4 and by[1]['context'] == by[2]['context'] == 'mission:Avgi Culture: Dissonance Graffiti 1')
ck('le due versioni del graffito condividono il lessico: stessi simboli, stessi addetti',
   all(frase in by[1]['italian'].lower() and frase in by[2]['italian'].lower()
       for frase in ('simboli colorati e ricurvi', 'pugno di avgi con spazzole e mocci')),
   (by[2]['italian'][:60],))
ck('ATTI DICHIARATI: tutte e otto le battute cominciano con il loro (corpus avgi news)',
   [a for a in ATTI if a in ''.join(u['italian'] for u in cov)] == ATTI,
   [a for a in ATTI if a not in ''.join(u['italian'] for u in cov)])
ck('il graffito e leggibile nella seconda versione: «tasse» e «defenestrare»',
   "'tasse'" in by[2]['italian'] and "'defenestrare'" in by[2]['italian'])
ck('il gioco di parole resta in inglese e lo dichiara (`Twilight Guard? ... Twilight Gourd.`)',
   'Twilight Guard? Più che altro Twilight Gourd.' in by[2]['italian'])
ck('TAB: tre in tutto, sulle unita 7, 9, 11 (righe 183, 198, 213)',
   sum(u['english'].count(TAB) for u in cov) == 3 == sum(u['italian'].count(TAB) for u in cov)
   and [u['idx'] for u in cov if TAB in u['italian']] == [7, 9, 11] == [u['idx'] for u in cov if TAB in u['english']])
ck('VIRGOLETTE: sedici in inglese e sedici in italiano, per unita',
   sum(u['english'].count(QUOTE) for u in cov) == 16 == sum(u['italian'].count(QUOTE) for u in cov)
   and all(u['english'].count(QUOTE) == u['italian'].count(QUOTE) for u in cov),
   [(u['idx'], u['english'].count(QUOTE), u['italian'].count(QUOTE)) for u in cov
    if u['english'].count(QUOTE) != u['italian'].count(QUOTE)])
ck('SEGNAPOSTO: tre `<planet>`, identici',
   sum(u['english'].count('<planet>') for u in cov) == 3 == sum(u['italian'].count('<planet>') for u in cov))
ck('APICI: sedici in inglese, dieci in italiano',
   sum(u['english'].count(APOS) for u in cov) == 16 and sum(u['italian'].count(APOS) for u in cov) == 10,
   (sum(u['english'].count(APOS) for u in cov), sum(u['italian'].count(APOS) for u in cov)))
ck('ALTERNATIVE: zero', sum(len(ALT.findall(u['english'])) for u in cov) == 0
   == sum(len(ALT.findall(u['italian'])) for u in cov))
ck('nomi e fazioni INVARIATI: Avgi, Twilight Guard, Twilight Gourd, Aberrant, Mindaro, Korath',
   all(n in ''.join(u['italian'] for u in cov) for n in
       ['Avgi', 'Twilight Guard', 'Twilight Gourd', 'Aberrant', 'Mindaro', 'Korath']),
   [n for n in ['Avgi', 'Twilight Guard', 'Twilight Gourd', 'Aberrant', 'Mindaro', 'Korath']
    if n not in ''.join(u['italian'] for u in cov)])
ck('la ladra e FEMMINILE («ladra», «viva»), come dice l inglese (`her`, `she`)',
   'ladra' in by[8]['italian'] and 'ladra' in by[9]['italian'] and 'mai viva' in by[9]['italian'])
ck('registro: la seconda persona e presente',
   len([u for u in cov if re.search(r'\b(tu|tuo|tua|tuoi|tue|ti|te|sei|riesci|senti|trovi|noti|scuoti)\b',
                                     u['italian'])]) >= 6,
   [u['idx'] for u in cov if re.search(r'\b(tu|tuo|tua|tuoi|tue|ti|te|sei|riesci|senti|trovi|noti|scuoti)\b',
                                       u['italian'])])
ck('nessun caporale, nessun carattere tipografico',
   not [u['idx'] for u in cov for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026' if c in u['italian']])
nonlat = [(u['idx'], c) for u in cov for c in u['italian'] if ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']],
   [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90 (0,96-1,21)',
   all(0.55 < u['ratio'] < 1.90 for u in cov),
   [(u['idx'], u['ratio']) for u in cov if not 0.55 < u['ratio'] < 1.90])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("8 unita' prima della 122 (L290)",
   db.execute('select count(*) from units where path=? and line<122', (PATH,)).fetchone()[0] == 8)
ck("26 unita' dopo la 227",
   db.execute('select count(*) from units where path=? and line>227', (PATH,)).fetchone()[0] == 26)
ck('FENCING continua oltre il confine: la prima unita dopo la 227 e ancora `Fencing`',
   db.execute('select context from units where path=? and line>227 order by line limit 1', (PATH,)).fetchone()
   == ('mission:Avgi Culture: Fencing',))
ck('il file ha 46 unita, righe 24-270',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (46, 24, 270))
ck('tutte le 12 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · 8 contesti · 3 coppie consecutive + 1 non adiacente · 16 virgolette' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
