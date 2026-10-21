r"""check.py — L300 (`data/coalition/coalition outfits.txt`, righe 516-533). **LOTTO TERMINALE del file**.

Cinque schede che chiudono il file: verifica l'**invariante di FILE** (49 unita', somma dei lotti 15 + 15 + 14 + 5) e tre cose
del testo:

1. **le due coppie con tab** (517 e 533), e **una sola** scheda singola (`Heliarch License`, 524);
2. **la seconda persona NARRATIVA**: la riga 532 dice «gifted to **you**» — un libro regalato al giocatore, **non** un'istruzione
   di montaggio come in L299. E' l'**unica** del lotto e va elencata come tale;
3. **i nomi degli atti di legge** sono **titoli inventati**: si rendono in italiano descrittivo («Nona Rettifica su Commercio e
   Traffico»), mentre `Beyond the Hyperdrive` e `Anna Fangvin` restano **invariati**.
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
PATH = 'data/coalition/coalition outfits.txt'
PAIRS = [(516, 517), (532, 533)]
SINGOLA = 524
TABBED = [517, 533]
TU = [4]
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


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


grp = collections.Counter(u['context'] for u in cov)
ck('unita tradotte 5/5', len(cov) == 5 == len(units), '%d/%d' % (len(cov), len(units)))
ck('tutte DESCRIPTION, tre contesti: due coppie e una singola',
   {u['kind'] for u in cov} == {'DESCRIPTION'} and len(grp) == 3 and sorted(grp.values()) == [1, 2, 2], dict(grp))
ck('COPPIE 516/517 e 532/533, stesso contesto, tab sulla seconda',
   [(a, b) for a, b in PAIRS if at[b]['context'] == at[a]['context'] and at[b]['english'].startswith(TAB)] == PAIRS)
ck('la singola e `Heliarch License` alla 524',
   524 in at and at[524]['context'] == 'outfit:Heliarch License' and grp['outfit:Heliarch License'] == 1)
ck('TAB: esattamente due unita la portano (517, 533), primo carattere in italiano',
   sorted(u['line'] for u in cov if u['english'].startswith(TAB)) == TABBED
   and all(at[l]['italian'].startswith(TAB) for l in TABBED)
   and sum(u['italian'].count(TAB) for u in cov) == 2)
ck('tutte e 5 le unita sono TRADOTTE, nessuna copiata',
   all(u['italian'] != u['english'] for u in cov), [u['idx'] for u in cov if u['italian'] == u['english']])
ck('VIRGOLETTE, SEGNAPOSTO, ALTERNATIVE: tutti zero (asserzioni vuote)',
   sum(u['english'].count(QUOTE) for u in cov) == 0 == sum(u['italian'].count(QUOTE) for u in cov)
   and sum(len(TAG.findall(u['italian'])) for u in cov) == 0
   and sum(len(ALT.findall(u['italian'])) for u in cov) == 0)
ck('APICI: due in inglese (unita 3), cinque in italiano',
   sum(u['english'].count(APOS) for u in cov) == 2 and sum(u['italian'].count(APOS) for u in cov) == 5,
   (sum(u['english'].count(APOS) for u in cov), sum(u['italian'].count(APOS) for u in cov)))
ck('SECONDA PERSONA NARRATIVA: solo l unita 4 («un libro che ti ha regalato»)',
   [u['idx'] for u in cov if re.search(r'\b(tu|tuo|tua|tuoi|tue|ti|te)\b', u['italian'])] == TU,
   [u['idx'] for u in cov if re.search(r'\b(tu|tuo|tua|tuoi|tue|ti|te)\b', u['italian'])])
ck('il nome dell autrice resta invariato e il titolo non viene inventato in prosa',
   'Anna Fangvin' in by[4]['italian']
   and 'Beyond the Hyperdrive' not in ''.join(u['italian'] for u in cov)
   and 'Hyperdrive' not in ''.join(u['italian'] for u in cov))
ck('gli atti di legge sono resi in italiano descrittivo, non lasciati in inglese',
   'Guerra d\'Indipendenza' in by[2]['italian']
   and 'Nona Rettifica su Commercio e Traffico' in by[2]['italian']
   and 'Legge sui Beni e sulle Tariffe Civili' in by[2]['italian']
   and 'Rectification' not in ''.join(u['italian'] for u in cov)
   and 'Civil Goods' not in ''.join(u['italian'] for u in cov))
ck('lessico del corpus: motore di salto, ipervie',
   'motore di salto' in by[5]['italian'] and 'ipervie' in by[5]['italian'])
ck('nessun caporale, nessun carattere tipografico',
   not [u['idx'] for u in cov for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026' if c in u['italian']])
nonlat = [(u['idx'], c) for u in cov for c in u['italian'] if ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessun doppio spazio (la tab iniziale non conta)',
   not [u['idx'] for u in cov if '  ' in u['italian'].lstrip(TAB)])
ck('rapporto nel gate 0,55-1,90 (0,93-1,28)',
   all(0.55 < u['ratio'] < 1.90 for u in cov),
   [(u['idx'], u['ratio']) for u in cov if not 0.55 < u['ratio'] < 1.90])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck('FILE: 44 unita prima della 516 (15 + 15 + 14)',
   db.execute('select count(*) from units where path=? and line<516', (PATH,)).fetchone()[0] == 44)
ck('FILE: ZERO unita dopo la 533 — il lotto CHIUDE il file',
   db.execute('select count(*) from units where path=? and line>533', (PATH,)).fetchone()[0] == 0)
ck('FILE: 49 unita, righe 26-533, tutte DESCRIPTION',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (49, 26, 533)
   and dict(db.execute('select kind,count(*) from units where path=? group by kind', (PATH,)).fetchall())
   == {'DESCRIPTION': 49})
ck('FILE: i quattro lotti sommano 49 (15 + 15 + 14 + 5)',
   15 + 15 + 14 + 5 == 49)
ck('tutte le 5 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · 3 contesti · 2 tab · FILE 49/49' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
