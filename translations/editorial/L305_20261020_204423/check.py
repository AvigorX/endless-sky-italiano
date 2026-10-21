r"""check.py — L305 (`data/quarg/quarg outfits.txt`, righe 138-243). **Secondo lotto del file**.

Dieci schede in **otto contesti**: la **seconda meta'** di `Large Graviton Steering` (138), **due coppie** (`Singularity Core`
180/181, `Quasar Core` 195/196) e **sei schede singole**, fra cui i **tre generatori di scudi** `Aspis` / `Ancile` / `Aegis`.

Il test verifica:

1. **la continuita' 137/138**: la 137 (L304) e' la **prima** meta' di `Large Graviton Steering`, la 138 la **seconda**, con la tab;
2. **il ritornello**: la 138 deve avere la **stessa resa** delle quattro unita' identiche di L304 (55, 78, 96, 120) — si **riapre**
   il `translation.json` precedente;
3. **i nomi greci dei tre scudi** e i nomi dei nuclei restano **invariati**.
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
PREV = os.path.join(L10N, 'staging', 'editorial', 'L304_20261020_203826', 'translation.json')
PATH = 'data/quarg/quarg outfits.txt'
COPPIE = [(180, 181), (195, 196)]
TABBED = [138, 181, 196]
SCUDI = [213, 228, 243]
NAMES = ['Quarg', 'Aspis', 'Ancile', 'Aegis', 'Singularity Core', 'Quasar Core', 'Antimatter Core',
         'Quantum Vacuum Battery']
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
prev = {u['line']: u for u in json.load(open(PREV, encoding='utf-8'))['units']}
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


grp = collections.Counter(u['context'] for u in cov)
ck('unita tradotte 10/10', len(cov) == 10 == len(units), '%d/%d' % (len(cov), len(units)))
ck('tutte DESCRIPTION, otto contesti: 2 coppie + 1 seconda meta + 7 singole',
   {u['kind'] for u in cov} == {'DESCRIPTION'} and len(grp) == 8
   and sorted(grp.values()) == [1] * 6 + [2, 2], dict(grp))
ck('CONTINUITA: la 137 (L304) e la prima meta di `Large Graviton Steering`, la 138 la seconda',
   prev[137]['context'] == 'outfit:Large Graviton Steering' and at[138]['context'] == 'outfit:Large Graviton Steering'
   and not prev[137]['english'].startswith(TAB) and at[138]['english'].startswith(TAB)
   and at[138]['italian'].startswith(TAB))
ck('RITORNELLO: la 138 ha la stessa resa delle quattro identiche di L304 (55, 78, 96, 120)',
   at[138]['italian'] == prev[55]['italian'] == prev[78]['italian'] == prev[96]['italian'] == prev[120]['italian'])
ck('COPPIE `Singularity Core` 180/181 e `Quasar Core` 195/196, tab sulla seconda',
   all(at[b]['context'] == at[a]['context'] and at[b]['english'].startswith(TAB) for a, b in COPPIE))
ck('i secondi paragrafi delle due coppie sono DIVERSI (generatori diversi)',
   at[181]['italian'] != at[196]['italian'])
ck('TAB: esattamente tre unita la portano, alle righe dichiarate',
   sorted(u['line'] for u in cov if u['english'].startswith(TAB)) == TABBED
   and sum(u['italian'].count(TAB) for u in cov) == 3)
ck('i tre generatori di scudi sono schede singole, con i nomi greci',
   [u['line'] for u in cov if 'Shield Generator' in u['context']] == SCUDI)
ck('tutte e 10 le unita sono TRADOTTE, nessuna copiata',
   all(u['italian'] != u['english'] for u in cov), [u['idx'] for u in cov if u['italian'] == u['english']])
ck('VIRGOLETTE, SEGNAPOSTO, ALTERNATIVE: tutti zero (asserzioni vuote)',
   sum(u['english'].count(QUOTE) for u in cov) == 0 == sum(u['italian'].count(QUOTE) for u in cov)
   and sum(len(TAG.findall(u['italian'])) for u in cov) == 0
   and sum(len(ALT.findall(u['italian'])) for u in cov) == 0)
ck('APICI: due in inglese (195, 243), sei in italiano',
   sum(u['english'].count(APOS) for u in cov) == 2 and sum(u['italian'].count(APOS) for u in cov) == 6,
   (sum(u['english'].count(APOS) for u in cov), sum(u['italian'].count(APOS) for u in cov)))
_it = ''.join(u['italian'] for u in cov)
ck('nomi nel testo INVARIATI e nessuna italianizzazione dei nomi greci',
   all(n in _it for n in ['Quarg', 'Singularity Core', 'Quasar Core', 'Antimatter Core'])
   and not [x for x in ['Aspide', 'Egida', 'Ancile italianizzato', 'Batteria a vuoto quantistico'] if x in _it],
   [n for n in ['Quarg', 'Singularity Core', 'Quasar Core', 'Antimatter Core'] if n not in _it])
ck('lessico: buco nero, orizzonte degli eventi, radiazione di Hawking, disco di accrescimento',
   'buco nero' in by[4]['italian'] and 'orizzonte degli eventi' in by[6]['italian']
   and 'radiazione di Hawking' in by[4]['italian'] and 'disco di accrescimento' in by[6]['italian'])
ck('lessico: vuoto quantistico, antimateria, calore di scarto',
   'vuoto quantistico' in by[2]['italian'] and 'antimateria' in by[3]['italian']
   and 'calore di scarto' in by[3]['italian'])
ck('REGISTRO: nessuna seconda persona',
   not [u['idx'] for u in cov if re.search(r'\b(tu|tuo|tua|tuoi|tue|ti|te)\b', u['italian'])],
   [u['idx'] for u in cov if re.search(r'\b(tu|tuo|tua|tuoi|tue|ti|te)\b', u['italian'])])
ck('nessun caporale, nessun carattere tipografico',
   not [u['idx'] for u in cov for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026' if c in u['italian']])
nonlat = [(u['idx'], c) for u in cov for c in u['italian'] if ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessun doppio spazio (la tab iniziale non conta)',
   not [u['idx'] for u in cov if '  ' in u['italian'].lstrip(TAB)])
ck('rapporto nel gate 0,55-1,90 (0,99-1,24)',
   all(0.55 < u['ratio'] < 1.90 for u in cov),
   [(u['idx'], u['ratio']) for u in cov if not 0.55 < u['ratio'] < 1.90])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("11 unita' prima della 138 (L304)",
   db.execute('select count(*) from units where path=? and line<138', (PATH,)).fetchone()[0] == 11)
ck("10 unita' dopo la 243; la prima e `Peripheral Repair Hub` alla 257",
   db.execute('select count(*) from units where path=? and line>243', (PATH,)).fetchone()[0] == 10
   and db.execute('select line,context from units where path=? and line>243 order by line limit 1', (PATH,)).fetchone()
   == (257, 'outfit:Peripheral Repair Hub'))
ck('il file ha 31 unita, righe 37-579',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (31, 37, 579))
ck('tutte le 10 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · 8 contesti · 2 coppie · 3 tab · file 21/31' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
