r"""verify.py — L292 (`data/avgi/avgi culture conversations.txt`, righe 229-259). **Terzo lotto del file**.

Verifica da sola: riga grezza, campi del DB, il **segmento** (20 prima, 17 qui, **9** dopo la 259), il **contesto unico**,
i **due `LOGBOOK`** distinti per tipo, le **due scelte** fra parentesi, il **tic delle domande** («domanda?»), la **scena
ripetuta** (la 251 deve **iniziare** con il testo della 248), i **15 tab**, le **26 virgolette**, e che **nessun altro lotto**
rivendichi le righe 229-259.

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
PAR = re.compile(r'\([^()]*\)')
HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
ROOT = os.path.abspath(os.path.join(L10N, '..'))
PATH = 'data/avgi/avgi culture conversations.txt'
LINES = [229, 230, 232, 234, 235, 237, 239, 240, 242, 243, 248, 251, 255, 256, 257, 258, 259]
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


ck('riga grezza identica al sorgente (17/17)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = [u['idx'] for u in su
       if db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
       != (u['english'], u['kind'], u['path'], u['context'])]
ck('english/kind/path/context identici al DB', not bad, bad)
ck('17 unita, righe tutte quelle dichiarate, 15 MISSION_TEXT + 2 LOGBOOK',
   len(tu) == 17 and sorted(u['line'] for u in tu) == LINES
   and collections.Counter(u['kind'] for u in tu) == {'MISSION_TEXT': 15, 'LOGBOOK': 2},
   (sorted({u['line'] for u in tu}), collections.Counter(u['kind'] for u in tu)))
ck('contesto unico: `mission:Avgi Culture: Fencing`', {u['context'] for u in tu} == {'mission:Avgi Culture: Fencing'})
ck("20 unita' prima della 229 e 9 dopo la 259",
   db.execute('select count(*) from units where path=? and line<229', (PATH,)).fetchone()[0] == 20
   and db.execute('select count(*) from units where path=? and line>259', (PATH,)).fetchone()[0] == 9)
ck('Fencing continua oltre il confine: la prima unita dopo la 259 e ancora `Fencing`',
   db.execute('select context from units where path=? and line>259 order by line limit 1', (PATH,)).fetchone()
   == ('mission:Avgi Culture: Fencing',))
ck('il file ha 46 unita, righe 24-270',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (46, 24, 270))
righe = set()
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH:
            righe.add(u['line'])
seg = {l for l in righe if 229 <= l <= 259}
ck('SEGMENTO: le 17 righe del lotto sono esattamente quelle 229-259',
   seg == set(LINES) and len(seg) == 17, (sorted(seg - set(LINES)), len(seg)))
overlap = []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    if os.path.basename(os.path.dirname(f)) == os.path.basename(HERE):
        continue
    for u in json.load(open(f, encoding='utf-8'))['units']:
        if u['path'] == PATH and 229 <= u['line'] <= 259:
            overlap.append((os.path.basename(os.path.dirname(f)), u['line']))
ck('nessun altro lotto rivendica le righe 229-259', not overlap, overlap)
ck('copertura: 17 righe nel segmento, il totale del file e stampato e non supera 46',
   len(seg) == 17 and len(righe) <= 46, '%d/46 al momento' % len(righe))
ck('tutte e 17 le unita sono tradotte',
   all(u['italian'] != u['english'] for u in tu))
ck('i due LOGBOOK sono in prima persona («Ho assistito», «Ho visto») e senza tab',
   'Ho assistito' in at[256]['italian'] and 'Ho visto' in at[256]['italian']
   and not at[255]['italian'].startswith(TAB) and not at[256]['italian'].startswith(TAB))
ck('le quindici MISSION_TEXT hanno tutte il tab iniziale',
   sum(1 for l in LINES if at[l]['italian'].startswith(TAB)) == 15
   and all(at[l]['italian'].startswith(TAB) for l in LINES if at[l]['kind'] == 'MISSION_TEXT'))
ck('scelte del giocatore: `(Avvicinati.)` e `(Ignorali.)`', 
   PAR.findall(at[229]['italian']) == ['(Avvicinati.)'] and PAR.findall(at[230]['italian']) == ['(Ignorali.)'])
ck('tic delle domande: due frasi finiscono con «domanda?"»',
   at[232]['italian'].endswith('domanda?"') and at[258]['italian'].endswith('domanda?"'))
ck('scena ripetuta: il testo della 251 INIZIA con quello della 248',
   at[251]['italian'].startswith(at[248]['italian']) and len(at[251]['italian']) > len(at[248]['italian']))
ck('la 251 aggiunge il cartello in maiuscolo, assente nella 248',
   "ZOMP PER SCHIACCIARLI COME L'ASSEMBLEA!" in at[251]['italian']
   and 'ASSEMBLEA' not in at[248]['italian'])
ck('tab 15; virgolette 26 per unita; zero segnaposto e zero alternative',
   sum(u['english'].count(TAB) for u in tu) == 15 == sum(u['italian'].count(TAB) for u in tu)
   and sum(u['english'].count(QUOTE) for u in tu) == 26 == sum(u['italian'].count(QUOTE) for u in tu)
   and all(u['english'].count(QUOTE) == u['italian'].count(QUOTE) for u in tu)
   and sum(len(TAG.findall(u['english'])) for u in tu) == 0 == sum(len(TAG.findall(u['italian'])) for u in tu)
   and sum(len(ALT.findall(u['italian'])) for u in tu) == 0)
ck('apici: 5 in inglese, 17 in italiano',
   sum(u['english'].count(APOS) for u in tu) == 5 and sum(u['italian'].count(APOS) for u in tu) == 17,
   (sum(u['english'].count(APOS) for u in tu), sum(u['italian'].count(APOS) for u in tu)))
ck('nomi invariati: Zomp, Razmatazz; Dissonance -> «Dissonanza»',
   'Zomp' in at[255]['italian'] and 'Razmatazz' in at[258]['italian']
   and 'Dissonanza' in at[256]['italian'] and 'Dissonance' not in at[256]['italian'])
ck('atti dichiarati presenti: Invito, Rassicurazione, Aggiunta, Proclama, Attesa',
   all(a in ''.join(u['italian'] for u in tu)
       for a in ('Invito.', 'Rassicurazione.', 'Aggiunta.', 'Proclama.', 'Attesa.')))
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in tu for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90',
   all(0.55 < u['ratio'] < 1.90 for u in tu),
   [(u['idx'], u['ratio']) for u in tu if not 0.55 < u['ratio'] < 1.90])
ck('tutte le 17 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in tu))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('SEGMENTO: 20 prima · 17 qui · 9 dopo la 259 · contesto unico · 2 LOGBOOK')
print('parole EN %d -> IT %d · ratio %.2f - %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(u['ratio'] for u in tu), max(u['ratio'] for u in tu)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L292 superato' if not fail else 'verify L292 fallito')
raise SystemExit(0 if not fail else 1)
