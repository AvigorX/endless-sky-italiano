r"""check.py — L285 (`data/wanderer/wanderer missions.txt`, righe 169-182). **LOTTO TERMINALE del file**.

L'**epilogo** della serie della pianta: il giocatore torna anni dopo e trova il campo di fiori blu. Il test verifica il file
**per intero**, non un segmento:

1. **invariante di FILE**: **54 unita**, **somma dei tre lotti 27 + 18 + 9 = 54**, **righe distinte**, **ultima riga 182**,
   **zero unita' dopo**;
2. **le due scelte del giocatore** fra parentesi tonde (`(Take a closer look.)` / `(Not right now.)`): struttura, **punto
   finale dentro** la parentesi, e ordine conservati;
3. **`sitrasanir` invariato** (nome del fiore, 3 occorrenze) e il traduttore che **non lo traduce**;
4. **le 6 alternative**, tutte coppie, con `[presenti? vivi?]` separata da `?` come il sorgente;
5. **otto tab** (unita 2-9: la 1 e' l'unica non rientrata) e **otto virgolette**, contate **per unita'**.
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
PAR = re.compile(r'\([^()]*\)')
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
TABBED = [2, 3, 4, 5, 6, 7, 8, 9]
TOK = {'<planet>': 1, '<first>': 1, '<last>': 1}
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


def opzioni(x):
    return [p.strip() for p in re.split(r'[,?]', x.strip('[]')) if p.strip()]


ck('unita tradotte 9/9', len(cov) == 9 == len(units), '%d/%d' % (len(cov), len(units)))
ck('tutte MISSION_TEXT, un solo contesto `The Plant Epilogue`, righe 169-182',
   {u['kind'] for u in units} == {'MISSION_TEXT'}
   and {u['context'] for u in units} == {'mission:Wanderers: Mereti: The Plant Epilogue'}
   and cov[0]['line'] == 169 and cov[-1]['line'] == 182)
ID_OK = [6]  # `"Sitrasanir?"`: nome proprio fra virgolette, identico per necessita'
ck('le 8 unita di prosa sono TRADOTTE; la sola identica e l ID_OK (nome proprio)',
   all(u['italian'] != u['english'] for u in cov if u['idx'] not in ID_OK)
   and all(by[i]['italian'] == by[i]['english'] for i in ID_OK),
   [u['idx'] for u in cov if u['idx'] not in ID_OK and u['italian'] == u['english']])
ck('TAB: otto, sulle unita 2-9, come PRIMO carattere; la 1 NON e rientrata',
   sum(u['english'].count(TAB) for u in cov) == 8 == sum(u['italian'].count(TAB) for u in cov)
   and [u['idx'] for u in cov if TAB in u['english']] == TABBED == [u['idx'] for u in cov if TAB in u['italian']]
   and all(u['italian'].startswith(TAB) for u in cov if u['idx'] in TABBED)
   and not by[1]['italian'].startswith(TAB))
ck('VIRGOLETTE: otto in inglese e otto in italiano, stesso numero per ogni unita',
   sum(u['english'].count(QUOTE) for u in cov) == 8 == sum(u['italian'].count(QUOTE) for u in cov)
   and all(u['english'].count(QUOTE) == u['italian'].count(QUOTE) for u in cov),
   [(u['idx'], u['english'].count(QUOTE), u['italian'].count(QUOTE)) for u in cov
    if u['english'].count(QUOTE) != u['italian'].count(QUOTE)])
ck('SCELTE del giocatore: due parentesi tonde, unita 2 e 3, punto finale DENTRO',
   [u['idx'] for u in cov if PAR.findall(u['english'])] == [2, 3] == [u['idx'] for u in cov if PAR.findall(u['italian'])]
   and PAR.findall(by[2]['english']) == ['(Take a closer look.)']
   and PAR.findall(by[3]['english']) == ['(Not right now.)']
   and PAR.findall(by[2]['italian'])[0].endswith('.)')
   and PAR.findall(by[3]['italian'])[0].endswith('.)'),
   (PAR.findall(by[2]['italian']), PAR.findall(by[3]['italian'])))
ck('SCELTE: la prima invita a guardare, la seconda rinvia',
   'vicino' in by[2]['italian'] and by[2]['italian'] != by[3]['italian'])
ck('ALTERNATIVE: sei per lingua, tutte coppie, stesse posizioni',
   sum(len(ALT.findall(u['english'])) for u in cov) == 6 == sum(len(ALT.findall(u['italian'])) for u in cov)
   and [u['idx'] for u in cov if ALT.findall(u['italian'])] == [5, 8] == [u['idx'] for u in cov if ALT.findall(u['english'])]
   and all(len(opzioni(a)) == 2 for u in cov for a in ALT.findall(u['italian'])),
   [(u['idx'], a) for u in cov for a in ALT.findall(u['italian']) if len(opzioni(a)) != 2])
ck('ALTERNATIVE: `[present? alive?]` separata da `?` e tradotta `[presenti? vivi?]`',
   '[present? alive?]' in by[8]['english'] and '[presenti? vivi?]' in by[8]['italian'])
ck('ALTERNATIVE: nessuna copiata alla lettera',
   all(a != b for u in cov for a, b in zip(ALT.findall(u['english']), ALT.findall(u['italian']))))
ck('`sitrasanir` invariato tre volte (due minuscole + la domanda), e il traduttore rinuncia alla parola',
   sum(u['italian'].lower().count('sitrasanir') for u in cov) == 3
   == sum(u['english'].lower().count('sitrasanir') for u in cov)
   and 'Sitrasanir?' in by[6]['italian']
   and 'non prova nemmeno a rendere' in by[5]['italian'])
ck('SEGNAPOSTO: tre token in tre famiglie, identici',
   {t: sum(collections.Counter(TAG.findall(u['english']))[t] for u in cov) for t in TOK} == TOK
   == {t: sum(collections.Counter(TAG.findall(u['italian']))[t] for u in cov) for t in TOK},
   ({t: sum(collections.Counter(TAG.findall(u['english']))[t] for u in cov) for t in TOK},
    {t: sum(collections.Counter(TAG.findall(u['italian']))[t] for u in cov) for t in TOK}))
ck('APICI: due in inglese, uno in italiano',
   sum(u['english'].count(APOS) for u in cov) == 2 and sum(u['italian'].count(APOS) for u in cov) == 1,
   (sum(u['english'].count(APOS) for u in cov), sum(u['italian'].count(APOS) for u in cov)))
ck('lessico: campo di fiori, petali blu, valle, sommosso, tonalita',
   'campo di fiori' in by[4]['italian'] and 'blu intenso' in by[4]['italian']
   and 'valle' in by[1]['italian'] and 'sommessa' in by[5]['italian'] and 'tonalità blu' in by[9]['italian'])
ck('nessun caporale, nessun carattere tipografico',
   not [u['idx'] for u in cov for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026' if c in u['italian']])
nonlat = [(u['idx'], c) for u in cov for c in u['italian'] if ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']],
   [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90 su tutte e nove (0,65-1,09)',
   all(0.55 < u['ratio'] < 1.90 for u in cov),
   [(u['idx'], u['ratio']) for u in cov if not 0.55 < u['ratio'] < 1.90])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck('FILE: 45 unita prima della 169 (L282-L284, somma 13+14+18)',
   db.execute('select count(*) from units where path=? and line<169', (PATH,)).fetchone()[0] == 45)
ck('FILE: ZERO unita dopo la 182 — il lotto CHIUDE il file',
   db.execute('select count(*) from units where path=? and line>182', (PATH,)).fetchone()[0] == 0)
ck('FILE: 54 unita totali, righe 16-182',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (54, 16, 182))
ck('FILE: i tre lotti sommano 54 (13 + 14 + 18 + 9)',
   13 + 14 + 18 + 9 == 54 and db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0] == 54)
ck('tutte le 9 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · 1 contesto · 8 tab · 8 virgolette · 6 alternative · FILE 54/54' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
