r"""check.py — L320 (`data/wanderer/wanderer outfits.txt`, righe 40-450). **Primo lotto** del file.

Diciotto `DESCRIPTION` in **17 contesti** — quattro famiglie:

| famiglia | righe |
|---|---|
| **raggi** | `Sunbeam` 40, `Sunbeam Turret` 82, `Dual Sunbeam Turret` 114, `Moonbeam` 145, `Moonbeam Turret` 195 |
| **missili** | `Anti-Missile` 219, `Thunderhead Launcher` 270-271, `Thunderhead Missile` 283, `Thunderhead Storage Array` 320 |
| **reattori** | `Small/Large Biochemical Cell` 346/361, `Red/Yellow/White/Blue Sun Reactor` 376/391/406/421 |
| **scudi** | `Bright Cloud Shielding` 436, `Dark Storm Shielding` 450 |

Il test difende: la **sola tab** (271, la nota dei rifornimenti **di nuovo**), i **due apici** per unita', la **scala dei reattori**
(`Red` -> `Blue`), lo **scambio** dichiarato in entrambi gli scudi (più ricarica, più consumo), e la progressione dei **raggi**
(un `Sunbeam` per torretta, due nel `Dual`).
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
PATH = 'data/wanderer/wanderer outfits.txt'
NOTA_EN = TAB + 'Ammunition for this weapon can be restocked at any outfitter.'
NOMI = ['Sunbeam', 'Moonbeam', 'Thunderhead', 'Biochemical Cell', 'Red Sun', 'Yellow Sun', 'White Sun',
        'Blue Sun', 'Bright Cloud Shielding', 'Dark Storm Shielding', 'Wanderer', 'Hai Slegati', 'Strong Wind']
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
    rows.append((n, d if d else ('OK' if c else 'FAIL'), c))


ck('unita tradotte 18/18', len(cov) == 18 == len(units), '%d/%d' % (len(cov), len(units)))
ck('tutte e 18 sono DESCRIPTION',
   collections.Counter(u['kind'] for u in cov) == {'DESCRIPTION': 18})
ck('17 contesti: solo il Thunderhead Launcher e doppio',
   len({u['context'] for u in cov}) == 17
   and [c for c, n in collections.Counter(u['context'] for u in cov).items() if n == 2]
   == ['outfit:Thunderhead Launcher'])
ck('una SOLA tab, riga 271, come primo carattere',
   [u['line'] for u in cov if u['italian'].startswith(TAB)] == [271]
   and at[271]['english'] == NOTA_EN)
ck('la nota dei rifornimenti usa la resa di maggioranza (quella di L318/L319)',
   at[271]['italian'] == NOTA_EN.replace(
       'Ammunition for this weapon can be restocked at any outfitter.',
       "Le munizioni per quest'arma possono essere rifornite presso qualsiasi emporio."))
ck('i due apici inglesi sono alle righe 436 e 450',
   [u['line'] for u in cov if u['english'].count(APOS)] == [436, 450],
   {u['line']: u['english'].count(APOS) for u in cov if u['english'].count(APOS)})
ck('nomi INVARIATI dove compaiono (raggi, missili, celle, reattori, scudi)',
   all(n in u['italian'] for u in cov for n in NOMI if n in u['english']),
   [(u['line'], n) for u in cov for n in NOMI if n in u['english'] and n not in u['italian']])
ck('`Unfettered Hai` -> «Hai Slegati» (corpus: 241 contro 65)',
   'Hai Slegati' in at[82]['italian'] and 'Hai Slegati' in at[219]['italian']
   and 'Unfettered' not in ''.join(u['italian'] for u in cov))
ck('i raggi: un Sunbeam per torretta, due nel Dual, e il Moonbeam contro la corazzatura',
   'ne porta uno solo' in at[82]['italian'] and 'una coppia di Sunbeam' in at[114]['italian']
   and 'corazzatura dello scafo' in at[145]['italian'])
ck('il Moonbeam in torretta fa il 50% di danni in più',
   '50%' in at[195]['italian'] and 'non in torretta' in at[195]['italian'])
ck('il Thunderhead: cinque submunizioni indipendenti, quaranta per lanciatore',
   'cinque submunizioni' in at[270]['italian'] and '40' in at[283]['italian'])
ck('la scala dei reattori: Red «piccolo», Yellow «compatto», White «grande», Blue «sempre più grandi»',
   'piccolo reattore' in at[376]['italian'] and 'reattore nucleare compatto' in at[391]['italian']
   and 'grande reattore nucleare' in at[406]['italian']
   and 'nuclei di reattore sempre più grandi' in at[421]['italian'])
ck('le celle biochimiche: microrganismi progettati e coltura che produce carica',
   'microrganismi' in at[346]['italian'] and 'coltura' in at[361]['italian']
   and 'carica elettrica' in at[361]['italian'])
ck('lo scambio in ENTRAMBI gli scudi: più ricarica, più consumo',
   'consuma anche più energia' in at[436]['italian']
   and 'assorbe anche molta più energia' in at[450]['italian'])
ck('VIRGOLETTE: zero · SEGNAPOSTO: nessuno · ALTERNATIVE: nessuna (asserzioni vuote)',
   sum(u['italian'].count(QUOTE) for u in cov) == 0
   and not TAG.findall(''.join(u['italian'] for u in cov))
   and sum(len(ALT.findall(u['italian'])) for u in cov) == 0)
ck('nessun caporale, nessun carattere tipografico, nessun non latino',
   not [c for u in cov for c in u['italian']
        if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026' or (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)])
ck('nessun doppio spazio (la tab iniziale non conta)',
   not [u['idx'] for u in cov if '  ' in u['italian'].lstrip(TAB)])
ck('rapporto nel gate 0,55-1,90',
   all(0.55 < u['ratio'] < 1.90 for u in cov),
   [(u['idx'], u['ratio']) for u in cov if not 0.55 < u['ratio'] < 1.90])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("SEGMENTO: zero unita' prima della 40 — il lotto APRE il file",
   db.execute('select count(*) from units where path=? and line<40', (PATH,)).fetchone()[0] == 0)
ck("SEGMENTO: 13 unita' dopo la 450 (la prossima alla 463)",
   db.execute('select count(*) from units where path=? and line>450', (PATH,)).fetchone()[0] == 13
   and db.execute('select min(line) from units where path=? and line>450', (PATH,)).fetchone()[0] == 463)
ck('FILE: 18 unita qui su 31 del file',
   db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0] == 31)
ck('tutte le 18 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · 18 DESCRIPTION in 17 contesti · 1 tab · 0 virgolette' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
