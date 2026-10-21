r"""verify.py — L290 (`data/avgi/avgi culture conversations.txt`, righe 24-106). **Primo lotto del file**.

Verifica da sola: riga grezza, campi del DB, il **segmento** (0 prima — il lotto **apre** il file — 8 qui, **38** dopo la 106),
i **sei contesti** con i due doppi **non adiacenti**, le **dieci virgolette**, il **segnaposto**, le **scene ripetute** (5/6 e
7/8) con inizio e chiusura identici, i **tre slogan** in maiuscolo, e che **nessun altro lotto** rivendichi le righe 24-106.

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
CTX = [('mission:Avgi Culture: Verticality', 24), ('mission:Avgi Culture: Free Fuel', 39),
       ('mission:Avgi Culture: Playfight', 52), ('mission:Avgi Culture: Cocoon', 66),
       ('mission:Avgi Culture: Zapchannel Ad', 82), ('mission:Avgi Culture: Zapchannel Ad', 86),
       ('mission:Avgi Culture: Dissonance Protest 1', 102), ('mission:Avgi Culture: Dissonance Protest 1', 106)]
SLOGANS = ['BASTA CON LE TASSE DELLA CONSONANCE', 'ABOLIAMO IL FEUDALESIMO MINERALE', 'SMETTETE DI MANDARCI A MORIRE']
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


def prefisso(a, b):
    i = 0
    while i < min(len(a), len(b)) and a[i] == b[i]:
        i += 1
    return a[:i]


ck('riga grezza identica al sorgente (8/8)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = [u['idx'] for u in su
       if db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
       != (u['english'], u['kind'], u['path'], u['context'])]
ck('english/kind/path/context identici al DB', not bad, bad)
ck('8 unita, righe distinte, tutte MISSION_TEXT, sei contesti',
   len(tu) == 8 and len({u['line'] for u in tu}) == 8 and {u['kind'] for u in tu} == {'MISSION_TEXT'}
   and [(u['context'], u['line']) for u in tu] == CTX)
ck('i due contesti doppi non sono adiacenti (82->86, 102->106)',
   at[86]['line'] - at[82]['line'] == 4 and at[106]['line'] - at[102]['line'] == 4)
ck("ZERO unita' prima della 24: il lotto APRE il file",
   db.execute('select count(*) from units where path=? and line<24', (PATH,)).fetchone()[0] == 0)
ck("38 unita' dopo la 106",
   db.execute('select count(*) from units where path=? and line>106', (PATH,)).fetchone()[0] == 38)
ck('confine: la 122 apre `Dissonance Graffiti 1`',
   db.execute('select line,context from units where path=? and line>106 order by line limit 1', (PATH,)).fetchone()
   == (122, 'mission:Avgi Culture: Dissonance Graffiti 1'))
ck('il file ha 46 unita, righe 24-270',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (46, 24, 270))
righe = set()
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH:
            righe.add(u['line'])
seg = {l for l in righe if 24 <= l <= 106}
ck('SEGMENTO: le 8 righe del lotto sono esattamente quelle 24-106',
   seg == {u['line'] for u in tu} and len(seg) == 8, (sorted(seg - {u['line'] for u in tu}), len(seg)))
overlap = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    if os.path.basename(os.path.dirname(f)) == os.path.basename(HERE):
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH and 24 <= u['line'] <= 106:
            overlap.append((os.path.basename(os.path.dirname(f)), u['line']))
ck('nessun altro lotto rivendica le righe 24-106', not overlap, overlap)
ck('copertura: 8 righe nel segmento, il totale del file e stampato e non supera 46',
   len(seg) == 8 and len(righe) <= 46, '%d/46 al momento' % len(righe))
ck('tutte le 8 unita sono tradotte',
   all(u['italian'] != u['english'] for u in tu))
ck('registro: la seconda persona e presente in almeno cinque unita',
   len([u for u in tu if re.search(r'\b(tu|tuo|tua|tuoi|tue|ti|te|sei|riesci|senti|puoi)\b', u['italian'])]) >= 5)
ck('scene ripetute: 5/6 condividono l inizio, 7/8 condividono inizio e chiusura',
   prefisso(at[82]['italian'], at[86]['italian']).startswith("Un'insegna elettronica economica, appiccica ")
   or prefisso(at[82]['italian'], at[86]['italian']).startswith("Un'insegna elettronica economica, appiccicata")
   and prefisso(at[102]['italian'], at[106]['italian']).startswith("Una fila di Avgi dall'aria arrabbiata marcia"))
ck('chiusura identica fra 102 e 106, e pari all inglese',
   at[102]['italian'].endswith('sulle loro bandiere e sui loro striscioni.')
   and at[106]['italian'].endswith('sulle loro bandiere e sui loro striscioni.')
   and at[102]['english'].endswith('on their flags and banners.')
   and at[106]['english'].endswith('on their flags and banners.'))
ck('tab zero; virgolette 10 in entrambe le lingue, per unita; segnaposto 1',
   sum(u['english'].count(TAB) for u in tu) == 0 == sum(u['italian'].count(TAB) for u in tu)
   and sum(u['english'].count(QUOTE) for u in tu) == 10 == sum(u['italian'].count(QUOTE) for u in tu)
   and all(u['english'].count(QUOTE) == u['italian'].count(QUOTE) for u in tu)
   and sum(u['english'].count('<ship>') for u in tu) == 1 == sum(u['italian'].count('<ship>') for u in tu))
ck('i tre slogan in maiuscolo fra virgolette',
   all(('"%s"' % s) in at[106]['italian'] for s in SLOGANS))
ck('asserzioni vuote: 0 alternative, 0 segnaposto oltre a `<ship>`',
   sum(len(ALT.findall(u['english'])) for u in tu) == 0 == sum(len(ALT.findall(u['italian'])) for u in tu)
   and sum(len(TAG.findall(u['english'])) for u in tu) == 1 == sum(len(TAG.findall(u['italian'])) for u in tu))
ck('apici: 9 in inglese, 9 in italiano',
   sum(u['english'].count(APOS) for u in tu) == 9 == sum(u['italian'].count(APOS) for u in tu),
   (sum(u['english'].count(APOS) for u in tu), sum(u['italian'].count(APOS) for u in tu)))
ck('nomi e parole inventate invariati (case-insensitive)',
   all(k.lower() in ''.join(u['italian'] for u in tu).lower()
       for k in ('Avgi', 'Consonance', 'Zapchannel Ray Energy', 'Incredulation', 'dee', 'magenta')))
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in tu for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90',
   all(0.55 < u['ratio'] < 1.90 for u in tu),
   [(u['idx'], u['ratio']) for u in tu if not 0.55 < u['ratio'] < 1.90])
ck('tutte le 8 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in tu))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('SEGMENTO: 0 prima (apre il file) · 8 qui · 38 dopo la 106 · 6 contesti · 2 doppi non adiacenti')
print('parole EN %d -> IT %d · ratio %.2f - %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(u['ratio'] for u in tu), max(u['ratio'] for u in tu)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L290 superato' if not fail else 'verify L290 fallito')
raise SystemExit(0 if not fail else 1)
