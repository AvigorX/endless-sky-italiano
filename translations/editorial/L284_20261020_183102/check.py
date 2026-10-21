r"""check.py — L284 (`data/wanderer/wanderer missions.txt`, righe 93-136). **Terzo lotto del file**.

Due missioni (`The Plant 4` e `The Plant 5`), **18 alternative** e — **prima volta in questo file** — un'unita' **UI_LABEL**.
Il test verifica:

1. **il `UI_LABEL`** (riga 108, `next steps`) e' **copiato**: uguaglianza, non differenza;
2. **i due `VALUE`** sono copiati e **diversi fra loro** (`Return to <planet>` / `Plant to <planet>`: non e' il caso di L283);
3. **le 18 alternative**: numero, posizione (3, 6, 8, 14, 16, 18) e **la distribuzione delle opzioni**, che qui non e' tutta
   doppia: `[disheartened?]` ha **una sola opzione** (17 coppie + 1 singola);
4. **`<npc>` e' una nave, quindi femminile**: «la <npc>», «lasciato indietro la <npc>»;
5. **otto tab** (unita 4, 5, 6, 8, 14, 15, 16, 18) e **venti virgolette**, contate **per unita**;
6. **due contesti** con le righe dichiarate, **27 unita' prima** e **9 dopo**.
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
TABBED = [4, 5, 6, 8, 14, 15, 16, 18]
ALTED = [3, 6, 8, 14, 16, 18]
VALUES = [1, 10]
LABEL = 7
TOK = {'<planet>': 5, '<destination>': 2, '<origin>': 2, '<npc>': 2, '<first>': 1}
CTX = {('mission:Wanderers: Mereti: The Plant 4', 93, 112), ('mission:Wanderers: Mereti: The Plant 5', 115, 136)}
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


def opzioni(x):
    return [p.strip() for p in re.split(r'[,?]', x.strip('[]')) if p.strip()]


cl = lambda t: [len(opzioni(a)) for a in ALT.findall(t)]  # noqa: E731

ck('unita tradotte 18/18', len(cov) == 18 == len(units), '%d/%d' % (len(cov), len(units)))
ck('tipi: 11 MISSION_TEXT + 2 DESCRIPTION + 2 VALUE + 2 DIALOG + 1 UI_LABEL',
   collections.Counter(u['kind'] for u in units)
   == {'MISSION_TEXT': 11, 'DESCRIPTION': 2, 'VALUE': 2, 'DIALOG': 2, 'UI_LABEL': 1},
   dict(collections.Counter(u['kind'] for u in units)))
ck('due contesti, con le righe dichiarate (Plant 4: 93-112, Plant 5: 115-136)',
   {(c, min(u['line'] for u in cov if u['context'] == c), max(u['line'] for u in cov if u['context'] == c))
    for c in {u['context'] for u in cov}} == CTX,
   {(c, min(u['line'] for u in cov if u['context'] == c), max(u['line'] for u in cov if u['context'] == c))
    for c in {u['context'] for u in cov}})
ck('il UI_LABEL e COPIATO (`next steps`, riga 108)',
   by[LABEL]['kind'] == 'UI_LABEL' and by[LABEL]['italian'] == by[LABEL]['english'] == 'next steps'
   and by[LABEL]['line'] == 108)
ck('i due VALUE sono COPIATI e DIVERSI fra loro (`Return to <planet>` / `Plant to <planet>`)',
   [by[i]['italian'] for i in VALUES] == [by[i]['english'] for i in VALUES]
   == ['Return to <planet>', 'Plant to <planet>']
   and by[1]['italian'] != by[10]['italian'])
ck('le 15 unita di prosa sono TRADOTTE, nessuna copiata',
   all(by[i]['italian'] != by[i]['english'] for i in by if i not in VALUES + [LABEL]),
   [i for i in by if i not in VALUES + [LABEL] and by[i]['italian'] == by[i]['english']])
ck('TAB: otto per lingua, sulle unita 4, 5, 6, 8, 14, 15, 16, 18, come PRIMO carattere',
   sum(u['english'].count(TAB) for u in cov) == 8 == sum(u['italian'].count(TAB) for u in cov)
   and [u['idx'] for u in cov if TAB in u['english']] == TABBED == [u['idx'] for u in cov if TAB in u['italian']]
   and all(u['italian'].startswith(TAB) for u in cov if u['idx'] in TABBED))
ck('VIRGOLETTE: 20 in inglese e 20 in italiano, stesso numero per ogni unita',
   sum(u['english'].count(QUOTE) for u in cov) == 20 == sum(u['italian'].count(QUOTE) for u in cov)
   and all(u['english'].count(QUOTE) == u['italian'].count(QUOTE) for u in cov),
   [(u['idx'], u['english'].count(QUOTE), u['italian'].count(QUOTE)) for u in cov
    if u['english'].count(QUOTE) != u['italian'].count(QUOTE)])
ck('ALTERNATIVE: 18 per lingua, sulle stesse sei unita, nello stesso ordine',
   sum(len(ALT.findall(u['english'])) for u in cov) == 18 == sum(len(ALT.findall(u['italian'])) for u in cov)
   and [u['idx'] for u in cov if ALT.findall(u['english'])] == ALTED == [u['idx'] for u in cov if ALT.findall(u['italian'])]
   and [len(ALT.findall(by[i]['english'])) for i in ALTED] == [1, 1, 1, 6, 6, 3]
   == [len(ALT.findall(by[i]['italian'])) for i in ALTED])
ck('ALTERNATIVE: la DISTRIBUZIONE delle opzioni e identica — 17 coppie e UNA singola (`[scoraggiata?]`)',
   cl(by[3]['english']) + cl(by[6]['english']) + cl(by[8]['english']) + cl(by[14]['english'])
   + cl(by[16]['english']) + cl(by[18]['english'])
   == [2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
   == cl(by[3]['italian']) + cl(by[6]['italian']) + cl(by[8]['italian']) + cl(by[14]['italian'])
   + cl(by[16]['italian']) + cl(by[18]['italian']),
   (cl(by[14]['english']), cl(by[14]['italian'])))
ck('ALTERNATIVE: la singola ha UNA opzione e conserva il punto interrogativo',
   len(opzioni(ALT.findall(by[14]['english'])[3])) == 1 == len(opzioni(ALT.findall(by[14]['italian'])[3]))
   and ALT.findall(by[14]['italian'])[3].endswith('?]'))
ck('ALTERNATIVE: nessuna coppia resta in inglese',
   all(a != b for u in cov for a, b in zip(ALT.findall(u['english']), ALT.findall(u['italian']))),
   [(u['idx'], a, b) for u in cov for a, b in zip(ALT.findall(u['english']), ALT.findall(u['italian'])) if a == b])
ck('CONCORDANZA: nessuna coppia mescola un infinito e un aggettivo',
   not [(u['idx'], c) for u in cov for c in (opzioni(a) for a in ALT.findall(u['italian']))
        if len(c) == 2 and (c[0].endswith(('are', 'ere', 'ire', 'rre')))
        != (c[1].endswith(('are', 'ere', 'ire', 'rre')))]
   , [(u['idx'], c) for u in cov for c in (opzioni(a) for a in ALT.findall(u['italian']))
      if len(c) == 2 and (c[0].endswith(('are', 'ere', 'ire', 'rre')))
      != (c[1].endswith(('are', 'ere', 'ire', 'rre')))])
ck('SEGNAPOSTO: dodici token in cinque famiglie, identici',
   {t: sum(collections.Counter(TAG.findall(u['english']))[t] for u in cov) for t in TOK} == TOK
   == {t: sum(collections.Counter(TAG.findall(u['italian']))[t] for u in cov) for t in TOK},
   ({t: sum(collections.Counter(TAG.findall(u['english']))[t] for u in cov) for t in TOK},
    {t: sum(collections.Counter(TAG.findall(u['italian']))[t] for u in cov) for t in TOK}))
ck("`<npc>` trattata come NAVE, quindi FEMMINILE: «la <npc>» due volte",
   by[12]['italian'].count('la <npc>') == 1 and by[17]['italian'].count('la <npc>') == 1
   and 'il <npc>' not in by[12]['italian'] + by[17]['italian'],
   (by[12]['italian'][:40], by[17]['italian'][:40]))
ck('APICI: undici in inglese, quattordici in italiano',
   sum(u['english'].count(APOS) for u in cov) == 11 and sum(u['italian'].count(APOS) for u in cov) == 14,
   (sum(u['english'].count(APOS) for u in cov), sum(u['italian'].count(APOS) for u in cov)))
ck("`Va'ika` compare otto volte e resta invariato",
   sum(u['english'].count("Va'ika") for u in cov) == 8 == sum(u['italian'].count("Va'ika") for u in cov),
   (sum(u['english'].count("Va'ika") for u in cov), sum(u['italian'].count("Va'ika") for u in cov)))
ck('nomi propri invariati: `Vara Kehi\'ki`, `Solima Skarati`, `Strong Wind`',
   "Vara Kehi'ki" in by[8]['italian'] and 'Solima Skarati' in by[3]['italian'] and 'Strong Wind' in by[13]['italian'])
ck('lessico: steppa, piuma, piazzola, distaccamento, attecchire',
   'steppa' in by[3]['italian'] and 'piuma' in by[14]['italian'] and 'piazzola' in by[13]['italian']
   and 'distaccamento' in by[8]['italian'] and 'attecchiscano' in by[8]['italian'])
ck('nessun caporale, nessun carattere tipografico',
   not [u['idx'] for u in cov for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026' if c in u['italian']])
nonlat = [(u['idx'], c) for u in cov for c in u['italian'] if ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']],
   [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90 sulle 15 unita tradotte (0,90-1,27)',
   all(0.55 < by[i]['ratio'] < 1.90 for i in by if i not in VALUES + [LABEL]),
   [(i, by[i]['ratio']) for i in by if i not in VALUES + [LABEL] and not 0.55 < by[i]['ratio'] < 1.90])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("27 unita' prima della 93",
   db.execute('select count(*) from units where path=? and line<93', (PATH,)).fetchone()[0] == 27)
ck("9 unita' dopo la 136",
   db.execute('select count(*) from units where path=? and line>136', (PATH,)).fetchone()[0] == 9)
ck('il file ha 54 unita, righe 16-182',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (54, 16, 182))
ck('tutte le 18 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · 2 contesti · 8 tab · 20 virgolette · 18 alternative (17 coppie + 1 singola)' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
