r"""check.py — L327 (`data/_ui/help.txt`, righe 15-69). **PRIMO DI TRE LOTTI — NON TERMINALE.**

**CHE COSA E' DIVERSO DAGLI ALTRI LOTTI.** Le ventotto unita' di questa finestra **non sono da tradurre**: sono gia' **`APPROVED`** nel
database, con il testo italiano **nella colonna `italian`**. Il lotto e' quindi di **revisione e trascrizione**: prende il testo
**approvato** come autorita', lo porta in staging e lo verifica **strutturalmente**.

Una prima traduzione indipendente divergeva dal testo approvato in **25 unita' su 28** («ipoteche» contro «mutui», «disabilitata»
contro «neutralizzata», «lavori» contro «incarichi»): il testo approvato **vince**, e il test lo rende falsificabile confrontando
**unita' per unita'**.

Il test difende:

1. **l'identita' col testo approvato**, 28/28 — e' il controllo centrale;
2. **i 5 segnaposto in 14 occorrenze**, identici al sorgente inglese **riga per riga**;
3. **le 12 virgolette** su quattro righe, con le etichette **tradotte** (`"Gestisci piloti"`, `"Entra nella nave"`, `"Preferenze"`,
   `"Manuale"`): il testo approvato le traduce, e questo **contraddice** l'ipotesi «le etichette restano inglesi»;
4. **la numerazione `lost 1` … `lost 7`** dei contesti;
5. **l'invariante di SEGMENTO**: 28 unita' proprie, righe distinte, nessun altro lotto sulle stesse righe. **Non** si contano i lotti del
   file: L328 e L329 devono poter arrivare senza far diventare RED questo test.
"""
import collections
import glob
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
PATH = 'data/_ui/help.txt'
RIGHE = (15, 69)
TAG_ATTESI = {'<Initiate hyperspace jump>': 5, '<Show main menu>': 4, '<View star map>': 3,
              '<Select next ship>': 1, '<Talk to selected ship>': 1}
LOST = {'help:lost 1': 2, 'help:lost 2': 1, 'help:lost 3': 2, 'help:lost 4': 2,
        'help:lost 5': 2, 'help:lost 6': 1, 'help:lost 7': 2}
VIRG = {19: 2, 20: 2, 24: 4, 45: 4}
ETICHETTE = ['"100k"', '"1m"', '"Gestisci piloti"', '"Entra nella nave"', '"Preferenze"', '"Manuale"']
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
at = {u['line']: u for u in cov}
rows = []
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else 'FAIL'), c))


ck('unita trascritte 28/28', len(cov) == 28 == len(units), '%d/%d' % (len(cov), len(units)))
ck('CENTRALE: il testo di staging e IDENTICO al testo APPROVATO, 28/28',
   all(db.execute('select italian from units where id=?', (u['id'],)).fetchone()[0] == u['italian'] for u in cov),
   [u['line'] for u in cov
    if db.execute('select italian from units where id=?', (u['id'],)).fetchone()[0] != u['italian']])
ck('le 28 unita sono APPROVED nel database (questo lotto NON le approva: le trascrive)',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'APPROVED' for u in cov),
   [(u['line'], db.execute('select state from units where id=?', (u['id'],)).fetchone()[0]) for u in cov][:4])
ck('tutte e 28 sono HELP (tipo nuovo: prosa di aiuto all interfaccia)',
   collections.Counter(u['kind'] for u in cov) == {'HELP': 28})
ck('14 contesti: due terzine, dieci coppie, due singoli',
   len({u['context'] for u in cov}) == 14
   and sorted(collections.Counter(u['context'] for u in cov).values(), reverse=True) == [3, 3] + [2] * 10 + [1, 1],
   sorted(collections.Counter(u['context'] for u in cov).values(), reverse=True))
ck('le sette sezioni lost hanno 2,1,2,2,2,1,2 unita e la numerazione NON si traduce',
   {c: n for c, n in collections.Counter(u['context'] for u in cov).items() if c.startswith('help:lost')} == LOST)
ck('i 5 segnaposto sono identici al sorgente, riga per riga, in 14 occorrenze',
   all(TAG.findall(at[u['line']]['english']) == TAG.findall(u['italian']) for u in cov)
   and collections.Counter(t for u in cov for t in TAG.findall(u['italian'])) == TAG_ATTESI,
   collections.Counter(t for u in cov for t in TAG.findall(u['italian'])))
ck('nessun segnaposto tradotto (niente <Mostra…> o <Vai a…>)',
   not [t for u in cov for t in TAG.findall(u['italian']) if re.search(r'[àèéìòù]', t)])
ck('le 12 virgolette sono su quattro righe e le etichette sono TRADOTTE',
   {u['line']: u['italian'].count(QUOTE) for u in cov if u['italian'].count(QUOTE)} == VIRG
   and sum(u['italian'].count(QUOTE) for u in cov) == 12
   and all(e in ''.join(u['italian'] for u in cov) for e in ETICHETTE),
   [e for e in ETICHETTE if e not in ''.join(u['italian'] for u in cov)])
ck('il testo approvato usa «neutralizzata» e «incarichi» (non «disabilitata», non «lavori»)',
   'neutralizzata' in at[27]['italian'] and 'incarichi' in at[36]['italian']
   and 'disabilitata' not in at[27]['italian'])
ck('la scala comica dei lost: la 6 cita il Tao, la 7 si chiude in sospensione',
   'Il Tao che può essere detto non è il vero Tao' in at[60]['italian']
   and 'davvero, davvero scarso' in at[57]['italian']
   and at[65]['italian'].endswith('tace...'))
ck('i numeri restano numeri: 100 crediti al giorno, K/M/B/T, 100.000 crediti',
   '100 crediti al giorno' in at[32]['italian']
   and 'K, M, B e T' in at[19]['italian'] and '100.000 crediti' in at[19]['italian'])
ck('ALTERNATIVE: nessuna (asserzione vuota)', sum(len(ALT.findall(u['italian'])) for u in cov) == 0)
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in cov for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessun doppio spazio, nessuna tab (il file non ne ha)',
   not [u['idx'] for u in cov if '  ' in u['italian']] and not [u['idx'] for u in cov if TAB in u['italian']])
ck('rapporto nel gate 0,55-1,90',
   all(0.55 < u['ratio'] < 1.90 for u in cov),
   [(u['idx'], u['ratio']) for u in cov if not 0.55 < u['ratio'] < 1.90])
ck('SEGMENTO: le 28 unita sono tutte dentro la finestra 15-69',
   all(RIGHE[0] <= u['line'] <= RIGHE[1] for u in cov)
   and min(u['line'] for u in cov) == 15 and max(u['line'] for u in cov) == 69)
ck('SEGMENTO: 28 righe distinte, nessuna riga ripetuta',
   len({u['line'] for u in cov}) == 28)
ck('SEGMENTO: nessun ALTRO lotto usa queste righe',
   not [f for f in glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))
        if os.path.basename(os.path.dirname(f)) != os.path.basename(HERE)
        for u in json.load(open(f, encoding='utf-8'))['units']
        if u['path'] == PATH and RIGHE[0] <= u['line'] <= RIGHE[1]])
ck('SEGMENTO: il confine dopo e la riga 72 (help:map advanced), NON inclusa',
   db.execute('select line, context from units where path=? and line>? order by line limit 1',
              (PATH, RIGHE[1])).fetchone() == (72, 'help:map advanced'))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · 28 HELP in 14 contesti · 14 segnaposto in 5 forme · SEGMENTO 15-69' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
