r"""check.py — L290 (`data/avgi/avgi culture conversations.txt`, righe 24-106). **Primo lotto del file**.

Otto scene di vita Avgi. Tre cose contano piu' delle altre:

1. **il registro torna al «tu»** (le schede tecniche di L286-L289 erano impersonali): qui il controllo va **invertito**;
2. **le scene sono ripetute in due versioni** — l'insegna (unita' 5 e 6) e la protesta (7 e 8) — e le parti condivise devono
   essere **identiche** nelle due rese, altrimenti lo stesso testo appare diverso in due momenti del gioco;
3. **due contesti hanno due unita' NON adiacenti** (82+86, 102+106): non sono coppie consecutive.
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
CTX = [('mission:Avgi Culture: Verticality', 24), ('mission:Avgi Culture: Free Fuel', 39),
       ('mission:Avgi Culture: Playfight', 52), ('mission:Avgi Culture: Cocoon', 66),
       ('mission:Avgi Culture: Zapchannel Ad', 82), ('mission:Avgi Culture: Zapchannel Ad', 86),
       ('mission:Avgi Culture: Dissonance Protest 1', 102), ('mission:Avgi Culture: Dissonance Protest 1', 106)]
KEEP = ['Avgi', 'Consonance', 'Zapchannel Ray Energy', 'Incredulation', 'dee', 'magenta']
SLOGANS = ['BASTA CON LE TASSE DELLA CONSONANCE', 'ABOLIAMO IL FEUDALESIMO MINERALE', 'SMETTETE DI MANDARCI A MORIRE']
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


def prefisso(a, b):
    i = 0
    while i < min(len(a), len(b)) and a[i] == b[i]:
        i += 1
    return a[:i]


def suffisso(a, b):
    i = 0
    while i < min(len(a), len(b)) and a[-1 - i] == b[-1 - i]:
        i += 1
    return a[-i:] if i else ''


ck('unita tradotte 8/8', len(cov) == 8 == len(units), '%d/%d' % (len(cov), len(units)))
ck('tutte MISSION_TEXT, sei contesti con le righe dichiarate',
   {u['kind'] for u in cov} == {'MISSION_TEXT'}
   and [(u['context'], u['line']) for u in cov] == CTX, [(u['context'], u['line']) for u in cov])
ck('tutte e 8 le unita sono TRADOTTE, nessuna copiata',
   all(u['italian'] != u['english'] for u in cov), [u['idx'] for u in cov if u['italian'] == u['english']])
ck('i due contesti doppi NON sono coppie consecutive (82->86 e 102->106)',
   by[6]['line'] - by[5]['line'] == 4 and by[8]['line'] - by[7]['line'] == 4
   and by[5]['context'] == by[6]['context'] == 'mission:Avgi Culture: Zapchannel Ad'
   and by[7]['context'] == by[8]['context'] == 'mission:Avgi Culture: Dissonance Protest 1')
ck('REGISTRO: la seconda persona e tornata (contrario delle schede tecniche)',
   len([u for u in cov if re.search(r'\b(tu|tuo|tua|tuoi|tue|ti|te|sei|riesci|senti|puoi)\b', u['italian'])]) >= 5,
   [u['idx'] for u in cov if re.search(r'\b(tu|tuo|tua|tuoi|tue|ti|te|sei|riesci|senti|puoi)\b', u['italian'])])
ck('COERENZA 5/6: lo stesso inizio di scena, parola per parola',
   prefisso(by[5]['italian'], by[6]['italian']).startswith("Un'insegna elettronica economica, appiccicata alla parete")
   and prefisso(by[5]['english'], by[6]['english']).startswith('A cheap electronic sign, haphazardly stuck to a wall'))
CHIUSA_IT = 'sulle loro bandiere e sui loro striscioni.'
CHIUSA_EN = 'on their flags and banners.'
ck('COERENZA 7/8: stesso inizio E stessa chiusura, parola per parola',
   prefisso(by[7]['italian'], by[8]['italian']).startswith("Una fila di Avgi dall'aria arrabbiata marcia")
   and by[7]['italian'].endswith(CHIUSA_IT) and by[8]['italian'].endswith(CHIUSA_IT)
   and by[7]['english'].endswith(CHIUSA_EN) and by[8]['english'].endswith(CHIUSA_EN)
   and by[7]['italian'][-len(CHIUSA_IT) - 40:] == by[8]['italian'][-len(CHIUSA_IT) - 40:],
   (by[7]['italian'][-60:], by[8]['italian'][-60:]))
ck('TAB: zero in inglese e zero in italiano (asserzione vuota)',
   sum(u['english'].count(TAB) for u in cov) == 0 == sum(u['italian'].count(TAB) for u in cov))
ck('VIRGOLETTE: dieci in inglese e dieci in italiano, per unita',
   sum(u['english'].count(QUOTE) for u in cov) == 10 == sum(u['italian'].count(QUOTE) for u in cov)
   and all(u['english'].count(QUOTE) == u['italian'].count(QUOTE) for u in cov),
   [(u['idx'], u['english'].count(QUOTE), u['italian'].count(QUOTE)) for u in cov
    if u['english'].count(QUOTE) != u['italian'].count(QUOTE)])
ck('i tre SLOGAN sono in maiuscolo e fra virgolette',
   all(('"%s"' % s) in by[8]['italian'] for s in SLOGANS),
   [s for s in SLOGANS if ('"%s"' % s) not in by[8]['italian']])
ck('SEGNAPOSTO: un solo `<ship>`, identico',
   sum(u['english'].count('<ship>') for u in cov) == 1 == sum(u['italian'].count('<ship>') for u in cov)
   and '<ship>' in by[2]['italian'])
ck('ALTERNATIVE: zero parentesi quadre', sum(len(ALT.findall(u['english'])) for u in cov) == 0
   == sum(len(ALT.findall(u['italian'])) for u in cov))
ck('APICI: nove in inglese, nove in italiano',
   sum(u['english'].count(APOS) for u in cov) == 9 == sum(u['italian'].count(APOS) for u in cov),
   (sum(u['english'].count(APOS) for u in cov), sum(u['italian'].count(APOS) for u in cov)))
tutto = ''.join(u['italian'] for u in cov).lower()
ck('nomi e parole inventate INVARIATI (Avgi, Consonance, Zapchannel Ray Energy, Incredulation, dee, magenta)',
   all(k.lower() in tutto for k in KEEP),
   [k for k in KEEP if k.lower() not in tutto])
ck('`Consonance` femminile: nello slogan e `DELLA CONSONANCE`, come nel corpus (avgi news: «la Consonance»)',
   'DELLA CONSONANCE' in by[8]['italian'] and 'DEL CONSONANCE' not in by[8]['italian'])
ck('lessico: spazioporto, montacarichi, bozzolo, tonneau, striscioni, nastri',
   'spazioporto' in by[1]['italian'] and 'montacarichi' in by[1]['italian'] and 'bozzolo' in by[4]['italian']
   and 'tonneau' in by[3]['italian'] and 'striscioni' in by[7]['italian'] and 'nastri' in by[7]['italian'])
ck('nessun caporale, nessun carattere tipografico',
   not [u['idx'] for u in cov for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026' if c in u['italian']])
nonlat = [(u['idx'], c) for u in cov for c in u['italian'] if ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']],
   [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90 (1,06-1,17)',
   all(0.55 < u['ratio'] < 1.90 for u in cov),
   [(u['idx'], u['ratio']) for u in cov if not 0.55 < u['ratio'] < 1.90])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("ZERO unita' prima della 24: il lotto APRE il file",
   db.execute('select count(*) from units where path=? and line<24', (PATH,)).fetchone()[0] == 0)
ck("38 unita' dopo la 106",
   db.execute('select count(*) from units where path=? and line>106', (PATH,)).fetchone()[0] == 38)
ck('il file ha 46 unita, righe 24-270, 44 MISSION_TEXT + 2 LOGBOOK',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (46, 24, 270)
   and dict(db.execute('select kind,count(*) from units where path=? group by kind', (PATH,)).fetchall())
   == {'MISSION_TEXT': 44, 'LOGBOOK': 2})
ck('tutte le 8 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · 6 contesti · 10 virgolette · 3 slogan · 1 segnaposto' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
