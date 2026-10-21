r"""verify.py — L284 (`data/wanderer/wanderer missions.txt`, righe 93-136). **Terzo lotto del file**.

Verifica da sola: riga grezza, campi del DB, il **segmento** (27 prima, 18 qui, **9** dopo la 136), i **due contesti**, il
**`UI_LABEL` copiato**, i due `VALUE` copiati e diversi, le **18 alternative** con la loro distribuzione (17 coppie + **una
singola**), `<npc>` femminile, **otto tab**, **venti virgolette**, e che **nessun altro lotto** rivendichi le righe 93-136.

Indipendente da `check.py`: rilegge `source.json`, il `translation.json`, il database, il file del gioco e **tutti** i
`translation.json` dello staging.
"""
import collections
import glob
import hashlib
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
ROOT = os.path.abspath(os.path.join(L10N, '..'))
PATH = 'data/wanderer/wanderer missions.txt'
TOK = {'<planet>': 5, '<destination>': 2, '<origin>': 2, '<npc>': 2, '<first>': 1}
VALUES = (1, 10)
LABEL = 7
DIST = [2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
su = sorted(src['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
raw_lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
by = {u['idx']: u for u in tu}
fail = []


def ck(n, c, d=''):
    print('%-96s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


def opz(x):
    return [p.strip() for p in re.split(r'[,?]', x.strip('[]')) if p.strip()]


ck('riga grezza identica al sorgente (18/18)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = [u['idx'] for u in su
       if db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
       != (u['english'], u['kind'], u['path'], u['context'])]
ck('english/kind/path/context identici al DB', not bad, bad)
ck('18 unita, righe distinte, 11 MISSION_TEXT + 2 DESCRIPTION + 2 VALUE + 2 DIALOG + 1 UI_LABEL',
   len(tu) == 18 and len({u['line'] for u in tu}) == 18
   and collections.Counter(u['kind'] for u in tu)
   == {'MISSION_TEXT': 11, 'DESCRIPTION': 2, 'VALUE': 2, 'DIALOG': 2, 'UI_LABEL': 1},
   (len(tu), collections.Counter(u['kind'] for u in tu)))
ck('due contesti: `The Plant 4` (93-112) e `The Plant 5` (115-136)',
   {(c, min(u['line'] for u in tu if u['context'] == c), max(u['line'] for u in tu if u['context'] == c))
    for c in {u['context'] for u in tu}}
   == {('mission:Wanderers: Mereti: The Plant 4', 93, 112), ('mission:Wanderers: Mereti: The Plant 5', 115, 136)})
ck("27 unita' prima della 93 e 9 dopo la 136",
   db.execute('select count(*) from units where path=? and line<93', (PATH,)).fetchone()[0] == 27
   and db.execute('select count(*) from units where path=? and line>136', (PATH,)).fetchone()[0] == 9)
ck('confine dopo: la prima unita dopo la 136 apre l epilogo (riga 169)',
   db.execute('select line,context from units where path=? and line>136 order by line limit 1', (PATH,)).fetchone()
   == (169, 'mission:Wanderers: Mereti: The Plant Epilogue'))
ck('il file ha 54 unita, righe 16-182',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (54, 16, 182))
righe = set()
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH:
            righe.add(u['line'])
seg = {l for l in righe if 93 <= l <= 136}
ck('SEGMENTO: le 18 righe del lotto sono esattamente quelle 93-136',
   seg == {u['line'] for u in tu} and len(seg) == 18, (sorted(seg - {u['line'] for u in tu}), len(seg)))
overlap = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    if os.path.basename(os.path.dirname(f)) == os.path.basename(HERE):
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH and 93 <= u['line'] <= 136:
            overlap.append((os.path.basename(os.path.dirname(f)), u['line']))
ck('nessun altro lotto rivendica le righe 93-136', not overlap, overlap)
ck('copertura: il lotto copre 18 righe del segmento e la copertura del file non PUO calare sotto 45',
   len(seg) == 18 and 45 <= len(righe) <= 54, '%d/54 (stampata, non asserita)' % len(righe))
ck('il UI_LABEL e copiato; i due VALUE copiati e diversi; le 15 di prosa tradotte',
   by[LABEL]['italian'] == by[LABEL]['english'] == 'next steps'
   and all(by[i]['italian'] == by[i]['english'] for i in VALUES)
   and by[1]['italian'] != by[10]['italian']
   and all(u['italian'] != u['english'] for u in tu
           if u['kind'] not in ('VALUE', 'UI_LABEL')))
ck('TAB: otto, unita 4, 5, 6, 8, 14, 15, 16, 18, primo carattere in entrambe le lingue',
   sum(u['english'].count(TAB) for u in tu) == 8 == sum(u['italian'].count(TAB) for u in tu)
   and [u['idx'] for u in tu if TAB in u['italian']] == [4, 5, 6, 8, 14, 15, 16, 18]
   and all(u['italian'].startswith(TAB) for u in tu if TAB in u['italian']))
ck('virgolette: 20 in tutto e lo stesso numero per ogni unita',
   sum(u['english'].count(QUOTE) for u in tu) == 20 == sum(u['italian'].count(QUOTE) for u in tu)
   and all(u['english'].count(QUOTE) == u['italian'].count(QUOTE) for u in tu))
ck('alternative: 18 per lingua e la stessa distribuzione di opzioni (17 coppie + 1 singola)',
   [len(opz(a)) for u in sorted(tu, key=lambda x: x['idx']) for a in ALT.findall(u['italian'])] == DIST
   == [len(opz(a)) for u in sorted(tu, key=lambda x: x['idx']) for a in ALT.findall(u['english'])],
   [len(opz(a)) for u in sorted(tu, key=lambda x: x['idx']) for a in ALT.findall(u['italian'])])
ck('alternative: la singola e in unita 14 ed e `[scoraggiata?]` con UNA opzione',
   ALT.findall(by[14]['italian']) == ['[costretti, obbligati]', '[concepite, progettate]', '[servire, adempiere]',
                                      '[scoraggiata?]', '[desideri, progetti]', '[guarire, curare]']
   and len(opz('[scoraggiata?]')) == 1)
ck('alternative: nessuna coppia resta in inglese',
   all(a != b for u in tu for a, b in zip(ALT.findall(u['english']), ALT.findall(u['italian']))),
   [(u['idx'], a) for u in tu for a, b in zip(ALT.findall(u['english']), ALT.findall(u['italian'])) if a == b])
ck('segnaposto per famiglia: dodici token, cinque famiglie, identici',
   {t: sum(collections.Counter(TAG.findall(u['english']))[t] for u in tu) for t in TOK} == TOK
   == {t: sum(collections.Counter(TAG.findall(u['italian']))[t] for u in tu) for t in TOK})
ck("`<npc>` femminile: «la <npc>» in unita 12 e 17",
   by[12]['italian'].count('la <npc>') == 1 and by[17]['italian'].count('la <npc>') == 1
   and 'il <npc>' not in by[12]['italian'] + by[17]['italian'])
ck('apici: 11 in inglese, 14 in italiano',
   sum(u['english'].count(APOS) for u in tu) == 11 and sum(u['italian'].count(APOS) for u in tu) == 14,
   (sum(u['english'].count(APOS) for u in tu), sum(u['italian'].count(APOS) for u in tu)))
ck("`Va'ika` otto volte in entrambe le lingue, `Vara Kehi'ki` e `Strong Wind` invariati",
   sum(u['english'].count("Va'ika") for u in tu) == 8 == sum(u['italian'].count("Va'ika") for u in tu)
   and "Vara Kehi'ki" in by[8]['italian'] and 'Strong Wind' in by[13]['italian'])
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in tu for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90 per le 15 unita tradotte',
   all(0.55 < u['ratio'] < 1.90 for u in tu if u['kind'] not in ('VALUE', 'UI_LABEL')),
   [(u['idx'], u['ratio']) for u in tu if u['kind'] not in ('VALUE', 'UI_LABEL') and not 0.55 < u['ratio'] < 1.90])
ck('tutte le 18 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in tu))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('SEGMENTO: 27 prima · 18 qui · 9 dopo · 2 contesti · file 45/54 (83,3%)')
print('parole EN %d -> IT %d · ratio %.2f - %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(u['ratio'] for u in tu if u['kind'] not in ('VALUE', 'UI_LABEL')),
    max(u['ratio'] for u in tu if u['kind'] not in ('VALUE', 'UI_LABEL'))))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L284 superato' if not fail else 'verify L284 fallito')
raise SystemExit(0 if not fail else 1)
