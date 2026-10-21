r"""check.py — L328 (`data/_ui/help.txt`, righe 72–116). **SECONDO DI TRE LOTTI — NON TERMINALE.**

Le venticinque unità sono **tutte `APPROVED`** nel database: il lotto **trascrive** il testo approvato (colonna `italian`) e lo
**verifica strutturalmente**. Non c'è traduzione nuova.

Il test difende:

1. **l'identità col testo approvato**, 25/25 — il controllo centrale;
2. **lo stato `APPROVED`** per tutte e 25, e il fatto che il lotto **non approva nulla** di suo;
3. **`<View player info>`**, 1 occorrenza, **identico** (un comando da tastiera non si traduce);
4. **le 10 virgolette**, concentrate nelle etichette del pannello («Save Order», «Park», «Park Local», «Park All» → «Salva ordine»,
   «Parcheggia», «Parcheggia le locali», «Parcheggia tutte»): il testo approvato **traduce** le etichette;
5. **la terminologia approvata**: «fornitore» per `outfitter`, «cantiere» per `shipyard`, «scorte» per `escorts`, «ammiraglia» per
   `flagship`, «pannello dati pilota» per `player info panel`;
6. **l'invariante di SEGMENTO**: 25 unità proprie nella finestra, righe distinte, nessun altro lotto sulle stesse righe, confine alla
   **119**. **Non** si contano i lotti del file (L329 deve poter arrivare).
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
RIGHE = (72, 116)
VIRG = {93: 2, 105: 2, 106: 6}
LOST_NON = 5
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


ck('unita trascritte 25/25', len(cov) == 25 == len(units), '%d/%d' % (len(cov), len(units)))
ck('CENTRALE: il testo di staging e IDENTICO al testo APPROVATO, 25/25',
   all(db.execute('select italian from units where id=?', (u['id'],)).fetchone()[0] == u['italian'] for u in cov),
   [u['line'] for u in cov
    if db.execute('select italian from units where id=?', (u['id'],)).fetchone()[0] != u['italian']])
ck('le 25 unita sono APPROVED nel database',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'APPROVED' for u in cov))
ck('tutte e 25 sono HELP',
   collections.Counter(u['kind'] for u in cov) == {'HELP': 25})
ck('11 contesti: ports, shops, map advanced e poteri con nomi propri',
   len({u['context'] for u in cov}) == 11
   and collections.Counter(u['context'] for u in cov)['help:map advanced ports'] == 3
   and collections.Counter(u['context'] for u in cov)['help:map advanced shops'] == 3
   and collections.Counter(u['context'] for u in cov)['help:multiple ship controls'] == 4,
   collections.Counter(u['context'] for u in cov))
ck('il segnaposto <View player info> e identico e in UNA sola occorrenza',
   collections.Counter(t for u in cov for t in TAG.findall(u['italian'])) == {'<View player info>': 1}
   and TAG.findall(at[102]['english']) == TAG.findall(at[102]['italian']) == ['<View player info>'])
ck('le 10 virgolette sono su tre righe (93, 105, 106)',
   {u['line']: u['italian'].count(QUOTE) for u in cov if u['italian'].count(QUOTE)} == VIRG
   and sum(u['italian'].count(QUOTE) for u in cov) == 10,
   {u['line']: u['italian'].count(QUOTE) for u in cov if u['italian'].count(QUOTE)})
ck('le etichette del pannello sono TRADOTTE: «Salva ordine», «Parcheggia le locali», «Parcheggia tutte»',
   '"Salva ordine"' in at[105]['italian'] and '"Parcheggia le locali"' in at[106]['italian']
   and '"Parcheggia tutte"' in at[106]['italian'] and '"Parcheggia"' in at[106]['italian'])
ck('la terminologia approvata: fornitore, cantiere, scorte, ammiraglia, pannello dati pilota',
   all(t in ' '.join(u['italian'] for u in cov) for t in
       ('fornitore', 'cantiere', 'scorte', 'ammiraglia', 'pannello dati pilota')))
ck('il testo NON usa «emporio» (divergenza dichiarata col resto del corpus)',
   not any('emporio' in u['italian'].lower() for u in cov))
ck('i tasti restano lettere latine: Shift+clic, Control+clic, F, T',
   'Shift+clic' in at[72]['italian'] and 'Control+clic' in at[72]['italian']
   and 'premere F' in at[83]['italian'] and 'premendo T' in at[86]['italian'])
ck('il pilota automatico atterra a fine rotta (riga 77)',
   'pilota automatico' in at[77]['italian'] and 'alla fine della rotta' in at[77]['italian'])
ck('ALTERNATIVE: nessuna (asserzione vuota)', sum(len(ALT.findall(u['italian'])) for u in cov) == 0)
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in cov for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessun doppio spazio, nessuna tab',
   not [u['idx'] for u in cov if '  ' in u['italian']] and not [u['idx'] for u in cov if TAB in u['italian']])
ck('rapporto nel gate 0,55-1,90',
   all(0.55 < u['ratio'] < 1.90 for u in cov),
   [(u['idx'], u['ratio']) for u in cov if not 0.55 < u['ratio'] < 1.90])
ck('SEGMENTO: 25 unita dentro 72-116, prima 72, ultima 116, 25 righe distinte',
   all(RIGHE[0] <= u['line'] <= RIGHE[1] for u in cov)
   and min(u['line'] for u in cov) == 72 and max(u['line'] for u in cov) == 116
   and len({u['line'] for u in cov}) == 25)
ck('SEGMENTO: nessun ALTRO lotto usa queste righe',
   not [f for f in glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))
        if os.path.basename(os.path.dirname(f)) != os.path.basename(HERE)
        for u in json.load(open(f, encoding='utf-8'))['units']
        if u['path'] == PATH and RIGHE[0] <= u['line'] <= RIGHE[1]])
ck('SEGMENTO: il confine dopo e la riga 119 (help:fleet asteroid mining), NON inclusa',
   db.execute('select line, context from units where path=? and line>? order by line limit 1',
              (PATH, RIGHE[1])).fetchone() == (119, 'help:fleet asteroid mining'))
ck('SEGMENTO: il lotto precedente (L327) finisce alla 69 e non si sovrappone',
   db.execute('select count(*) from units where path=? and line between 15 and 69', (PATH,)).fetchone()[0] == 28
   and min(u['line'] for u in cov) == 72)
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · 25 HELP in 11 contesti · 1 segnaposto · SEGMENTO 72-116' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
