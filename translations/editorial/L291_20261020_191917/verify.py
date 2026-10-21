r"""verify.py — L291 (`data/avgi/avgi culture conversations.txt`, righe 122-227). **Secondo lotto del file**.

Verifica da sola: riga grezza, campi del DB, il **segmento** (8 prima, 12 qui, **26** dopo la 227), gli **otto contesti**, le
**tre coppie consecutive** con tab sulla seconda meta', la coppia **non adiacente** del graffito, gli **otto atti dichiarati**
del tic linguistico Avgi, il **gioco di parole** lasciato in inglese, e che **nessun altro lotto** rivendichi le righe 122-227.

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
PATH = 'data/avgi/avgi culture conversations.txt'
CTX = [('mission:Avgi Culture: Dissonance Graffiti 1', 122), ('mission:Avgi Culture: Dissonance Graffiti 1', 126),
       ('mission:Avgi Culture: We Live In A Society', 140), ('mission:Avgi Culture: Realism', 154),
       ('mission:Avgi Culture: Doomed Korath', 168), ('mission:Avgi Culture: General Ripper', 182),
       ('mission:Avgi Culture: General Ripper', 183), ('mission:Avgi Culture: Criminal Mischief', 197),
       ('mission:Avgi Culture: Criminal Mischief', 198), ('mission:Avgi Culture: False Alarm', 212),
       ('mission:Avgi Culture: False Alarm', 213), ('mission:Avgi Culture: Fencing', 227)]
ATTI = ['Incredibile.', 'Apprezzamento.', 'Proclama.', 'Dichiarazione.', 'Attenzione!', 'Scherno!', 'Comando.',
        'Imbarazzo.']
NAMES = ['Avgi', 'Twilight Guard', 'Twilight Gourd', 'Aberrant', 'Mindaro', 'Korath']
src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
su = sorted(src['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
raw_lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
by = {u['idx']: u for u in tu}
at = {u['line']: u for u in tu}
fail = []


def ck(n, c, d=''):
    print('%-96s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente (12/12)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = [u['idx'] for u in su
       if db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
       != (u['english'], u['kind'], u['path'], u['context'])]
ck('english/kind/path/context identici al DB', not bad, bad)
ck('12 unita, righe distinte, tutte MISSION_TEXT, otto contesti con le righe',
   len(tu) == 12 and len({u['line'] for u in tu}) == 12 and {u['kind'] for u in tu} == {'MISSION_TEXT'}
   and [(u['context'], u['line']) for u in tu] == CTX)
ck("8 unita' prima della 122 e 26 dopo la 227",
   db.execute('select count(*) from units where path=? and line<122', (PATH,)).fetchone()[0] == 8
   and db.execute('select count(*) from units where path=? and line>227', (PATH,)).fetchone()[0] == 26)
ck('Fencing continua oltre il confine: la prima unita dopo la 227 e ancora `Fencing`',
   db.execute('select context from units where path=? and line>227 order by line limit 1', (PATH,)).fetchone()
   == ('mission:Avgi Culture: Fencing',))
ck('il file ha 46 unita, righe 24-270',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (46, 24, 270))
righe = set()
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH:
            righe.add(u['line'])
seg = {l for l in righe if 122 <= l <= 227}
ck('SEGMENTO: le 12 righe del lotto sono esattamente quelle 122-227',
   seg == {u['line'] for u in tu} and len(seg) == 12, (sorted(seg - {u['line'] for u in tu}), len(seg)))
overlap = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    if os.path.basename(os.path.dirname(f)) == os.path.basename(HERE):
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH and 122 <= u['line'] <= 227:
            overlap.append((os.path.basename(os.path.dirname(f)), u['line']))
ck('nessun altro lotto rivendica le righe 122-227', not overlap, overlap)
ck('copertura: 12 righe nel segmento, il totale del file e stampato e non supera 46',
   len(seg) == 12 and len(righe) <= 46, '%d/46 al momento' % len(righe))
ck('tutte le 12 unita sono tradotte', all(u['italian'] != u['english'] for u in tu))
ck('tre coppie consecutive con tab sulla seconda meta (183, 198, 213)',
   all(at[b]['line'] == at[a]['line'] + 1 and at[a]['context'] == at[b]['context'] for a, b in
       [(182, 183), (197, 198), (212, 213)])
   and all(at[l]['italian'].startswith(TAB) for l in (183, 198, 213))
   and not any(at[l]['italian'].startswith(TAB) for l in (182, 197, 212)))
ck('la coppia del graffito non e consecutiva (122 e 126)',
   at[126]['line'] - at[122]['line'] == 4 and at[122]['context'] == at[126]['context'])
ck('le due versioni del graffito hanno lo stesso lessico (case-insensitive)',
   all(f in at[122]['italian'].lower() and f in at[126]['italian'].lower()
       for f in ('simboli colorati e ricurvi', 'pugno di avgi con spazzole e mocci')))
ck('otto atti dichiarati, tutti presenti (tic linguistico degli Avgi)',
   [a for a in ATTI if a in ''.join(u['italian'] for u in tu)] == ATTI,
   [a for a in ATTI if a not in ''.join(u['italian'] for u in tu)])
ck('il gioco di parole resta in inglese, con i nomi invariati',
   'Twilight Guard? Più che altro Twilight Gourd.' in at[126]['italian'])
ck('tab 3; virgolette 16 per unita; segnaposto 3',
   sum(u['english'].count(TAB) for u in tu) == 3 == sum(u['italian'].count(TAB) for u in tu)
   and sum(u['english'].count(QUOTE) for u in tu) == 16 == sum(u['italian'].count(QUOTE) for u in tu)
   and all(u['english'].count(QUOTE) == u['italian'].count(QUOTE) for u in tu)
   and sum(u['english'].count('<planet>') for u in tu) == 3 == sum(u['italian'].count('<planet>') for u in tu))
ck('apici: 16 in inglese, 10 in italiano',
   sum(u['english'].count(APOS) for u in tu) == 16 and sum(u['italian'].count(APOS) for u in tu) == 10,
   (sum(u['english'].count(APOS) for u in tu), sum(u['italian'].count(APOS) for u in tu)))
ck('nomi e fazioni invariati',
   all(n in ''.join(u['italian'] for u in tu) for n in NAMES),
   [n for n in NAMES if n not in ''.join(u['italian'] for u in tu)])
ck('la ladra e femminile («ladra», «viva»)',
   'ladra' in at[197]['italian'] and 'mai viva' in at[198]['italian'])
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in tu for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90',
   all(0.55 < u['ratio'] < 1.90 for u in tu),
   [(u['idx'], u['ratio']) for u in tu if not 0.55 < u['ratio'] < 1.90])
ck('tutte le 12 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in tu))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('SEGMENTO: 8 prima · 12 qui · 26 dopo la 227 · 8 contesti · 3 coppie consecutive + 1 non adiacente')
print('parole EN %d -> IT %d · ratio %.2f - %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(u['ratio'] for u in tu), max(u['ratio'] for u in tu)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L291 superato' if not fail else 'verify L291 fallito')
raise SystemExit(0 if not fail else 1)
