r"""check.py — L283 (`data/wanderer/wanderer missions.txt`, righe 42-88). **Secondo lotto del file**.

Tre missioni della serie della pianta (`The Plant 1` -> `2` -> `3`) e **18 alternative fra parentesi quadre**, il numero piu'
alto finora. Il test verifica:

1. **le 18 alternative**: numero, posizione (unita 1, 6, 7, 10, 11, 14) e **due opzioni ciascuna**, dividendole su `[,?]`;
2. **la concordanza**: in ogni coppia le opzioni hanno la **stessa classe grammaticale** (verbo con verbo, sostantivo con
   sostantivo), cosi' che ogni combinazione resti corretta;
3. **i due `VALUE`** sono copiati **e identici fra loro** (`A Home for the Plant`, missione 2 e 3);
4. **sette tab** (unita 1, 6-11) e **diciotto virgolette**, contate **per unita**;
5. **tre contesti** in 47 righe, con le righe che il contratto dichiara.
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
PATH = 'data/wanderer/wanderer missions.txt'
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
TABBED = [1, 6, 7, 8, 9, 10, 11]
ALTED = [1, 6, 7, 10, 11, 14]
VALUES = [3, 12]
TOK = {'<origin>': 1, '<planet>': 2, '<system>': 1}
CTX = {('mission:Wanderers: Mereti: The Plant 1', 42, 45),
       ('mission:Wanderers: Mereti: The Plant 2', 56, 74),
       ('mission:Wanderers: Mereti: The Plant 3', 79, 88)}
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


def opzioni(x):
    return [p.strip() for p in re.split(r'[,?]', x.strip('[]')) if p.strip()]


def coppie(t):
    return [opzioni(a) for a in ALT.findall(t)]


ck('unita tradotte 14/14', len(cov) == 14 == len(units), '%d/%d' % (len(cov), len(units)))
ck('tipi: 9 MISSION_TEXT + 2 DESCRIPTION + 2 VALUE + 1 DIALOG',
   collections.Counter(u['kind'] for u in units) == {'MISSION_TEXT': 9, 'DESCRIPTION': 2, 'VALUE': 2, 'DIALOG': 1},
   dict(collections.Counter(u['kind'] for u in units)))
ck('tre contesti, con le righe dichiarate (42-45, 56-74, 79-88)',
   {(u['context'], u['line'], u['line']) for u in cov} and
   {(u['context'], min(x['line'] for x in cov if x['context'] == u['context']),
     max(x['line'] for x in cov if x['context'] == u['context'])) for u in cov} == CTX,
   {(u['context'], min(x['line'] for x in cov if x['context'] == u['context']),
     max(x['line'] for x in cov if x['context'] == u['context'])) for u in cov})
ck('i due VALUE sono COPIATI e identici (`A Home for the Plant`)',
   all(by[i]['kind'] == 'VALUE' and by[i]['italian'] == by[i]['english'] == 'A Home for the Plant' for i in VALUES))
ck('le 12 unita non-VALUE sono TRADOTTE, nessuna copiata',
   all(by[i]['italian'] != by[i]['english'] for i in by if i not in VALUES),
   [i for i in by if i not in VALUES and by[i]['italian'] == by[i]['english']])
ck('le due DESCRIPTION sono identiche fra loro, come nel sorgente',
   by[4]['english'] == by[13]['english'] and by[4]['italian'] == by[13]['italian'])
ck('TAB: sette per lingua, sulle unita 1 e 6-11, come PRIMO carattere',
   sum(u['english'].count(TAB) for u in cov) == 7 == sum(u['italian'].count(TAB) for u in cov)
   and [u['idx'] for u in cov if TAB in u['english']] == TABBED == [u['idx'] for u in cov if TAB in u['italian']]
   and all(u['italian'].startswith(TAB) for u in cov if u['idx'] in TABBED))
ck('VIRGOLETTE: 18 in inglese e 18 in italiano, stesso numero per ogni unita',
   sum(u['english'].count(QUOTE) for u in cov) == 18 == sum(u['italian'].count(QUOTE) for u in cov)
   and all(u['english'].count(QUOTE) == u['italian'].count(QUOTE) for u in cov),
   [(u['idx'], u['english'].count(QUOTE), u['italian'].count(QUOTE)) for u in cov
    if u['english'].count(QUOTE) != u['italian'].count(QUOTE)])
ck('ALTERNATIVE: 18 per lingua, sulle stesse sei unita, nello stesso ordine',
   sum(len(ALT.findall(u['english'])) for u in cov) == 18 == sum(len(ALT.findall(u['italian'])) for u in cov)
   and [u['idx'] for u in cov if ALT.findall(u['english'])] == ALTED == [u['idx'] for u in cov if ALT.findall(u['italian'])]
   and [len(ALT.findall(by[i]['english'])) for i in ALTED] == [1, 2, 6, 2, 4, 3]
   == [len(ALT.findall(by[i]['italian'])) for i in ALTED])
ck('ALTERNATIVE: ogni coppia ha due opzioni, in inglese e in italiano',
   all(len(c) == 2 for u in cov for c in coppie(u['english']))
   and all(len(c) == 2 for u in cov for c in coppie(u['italian'])),
   [(u['idx'], c) for u in cov for c in coppie(u['italian']) if len(c) != 2])
ck('ALTERNATIVE: due opzioni per coppia in entrambe le lingue, confrontate coppia per coppia',
   all(by[i]['english'].count('[') == by[i]['italian'].count('[') for i in by))
ck('ALTERNATIVE: le opzioni NON sono identiche all inglese (sono tradotte)',
   all(a != b for u in cov for a, b in zip(ALT.findall(u['english']), ALT.findall(u['italian']))),
   [(u['idx'], a, b) for u in cov for a, b in zip(ALT.findall(u['english']), ALT.findall(u['italian'])) if a == b])
ck('CONCORDANZA: le opzioni di ogni coppia hanno la stessa forma (nessun misto verbo/sostantivo)',
   not [(u['idx'], c) for u in cov for c in coppie(u['italian'])
        if (c[0].endswith(('are', 'ere', 'ire', 'iamo', 'ano', 'uto', 'ato', 'ito', 'ato')))
        != (c[1].endswith(('are', 'ere', 'ire', 'iamo', 'ano', 'uto', 'ato', 'ito')))],
   [(u['idx'], c) for u in cov for c in coppie(u['italian'])
    if (c[0].endswith(('are', 'ere', 'ire', 'iamo', 'ano', 'uto', 'ato', 'ito')))
    != (c[1].endswith(('are', 'ere', 'ire', 'iamo', 'ano', 'uto', 'ato', 'ito')))])
ck('SEGNAPOSTO: quattro token in tre famiglie, identici',
   {t: sum(collections.Counter(TAG.findall(u['english']))[t] for u in cov) for t in TOK} == TOK
   == {t: sum(collections.Counter(TAG.findall(u['italian']))[t] for u in cov) for t in TOK},
   ({t: sum(collections.Counter(TAG.findall(u['english']))[t] for u in cov) for t in TOK},
    {t: sum(collections.Counter(TAG.findall(u['italian']))[t] for u in cov) for t in TOK}))
ck('APICI: nove in inglese, quindici in italiano (nomi Va\'ika piu\' elisioni)',
   sum(u['english'].count(APOS) for u in cov) == 9 and sum(u['italian'].count(APOS) for u in cov) == 15,
   (sum(u['english'].count(APOS) for u in cov), sum(u['italian'].count(APOS) for u in cov)))
ck("il nome `Va'ika` compare lo stesso numero di volte (9) e resta invariato",
   sum(u['english'].count("Va'ika") for u in cov) == 9 == sum(u['italian'].count("Va'ika") for u in cov),
   (sum(u['english'].count("Va'ika") for u in cov), sum(u['italian'].count("Va'ika") for u in cov)))
ck("`Sopi Lefarkata` e `Keti` invariati; `xenobotany` -> «xenobotanica»",
   'Sopi Lefarkata' in by[7]['italian'] and 'Sopi Lefarkata' in by[14]['italian']
   and 'Keti' in by[5]['italian'] and 'xenobotanica' in by[5]['italian'])
ck('`Unfettered` nella prosa diventa «Slegati»',
   'Slegati' in by[8]['italian'] and 'Unfettered' not in by[8]['italian'])
ck('lessico: steppe, ala, dimora, stiva, spazioporto',
   'steppe' in by[14]['italian'] and "un'ala" in by[14]['italian']
   and 'dimora' in by[4]['italian'] and 'stiva' in by[1]['italian'] and 'spazioporto' in by[1]['italian'])
ck('nessun caporale, nessun carattere tipografico',
   not [u['idx'] for u in cov for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026' if c in u['italian']])
nonlat = [(u['idx'], c) for u in cov for c in u['italian'] if ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']],
   [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90 sulle 12 unita tradotte (0,90-1,07)',
   all(0.55 < by[i]['ratio'] < 1.90 for i in by if i not in VALUES),
   [(i, by[i]['ratio']) for i in by if i not in VALUES and not 0.55 < by[i]['ratio'] < 1.90])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("13 unita' PRIMA della 42 (il file e' aperto da L282)",
   db.execute('select count(*) from units where path=? and line<42', (PATH,)).fetchone()[0] == 13)
ck("27 unita' dopo la 88",
   db.execute('select count(*) from units where path=? and line>88', (PATH,)).fetchone()[0] == 27)
ck('il file ha 54 unita, righe 16-182',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (54, 16, 182))
ck('tutte le 14 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · 3 contesti · 7 tab · 18 virgolette · 18 alternative' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
