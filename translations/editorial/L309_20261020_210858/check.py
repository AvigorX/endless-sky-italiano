r"""check.py — L309 (`data/avgi/avgi weapons.txt`, righe 716-969). **LOTTO TERMINALE del file**.

Tredici unita' che chiudono il file: l'**invariante di FILE** (46 unita', somma dei lotti **12 + 21 + 13**) e quattro cose del
testo:

1. **tre tipi**: **10 `DESCRIPTION`** da tradurre, **2 `TEXT`** e **1 `VALUE`** da **copiare**;
2. **due terzine** (`"Orchid" Nuclear Missile` 801/802/803, `"Ophrys" Nuclear Torpedo` 949/950/951) e **due coppie**
   (`"Nettle" KKV` 716/717, `Ophrys Stockpile` 968/969);
3. **la frase «ammunition for» in TRE varianti** (717, 803, 951): stessa struttura, **arma diversa** e **contenitore diverso** —
   non e' la nota munizioni di L307/L308, che qui **non compare**;
4. **la seconda persona compare in TRE unita'** (2, 7, 10: «non **puoi** comprare ne' usare»), e sono **avvisi di gioco**.
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
PATH = 'data/avgi/avgi weapons.txt'
TERZINE = {"outfit:\"Orchid\" Nuclear Missile": [801, 802, 803],
           "outfit:\"Ophrys\" Nuclear Torpedo": [949, 950, 951]}
COPPIE = [(716, 717), (968, 969)]
TABBED = [717, 802, 803, 950, 951, 969]
TEXT_IDX = [4, 11]
VALUE_IDX = [3]
AMMO3 = [2, 7, 10]
TU = [2, 7, 10]
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
kinds = collections.Counter(u['kind'] for u in cov)
ck('unita tradotte 13/13', len(cov) == 13 == len(units), '%d/%d' % (len(cov), len(units)))
ck('tre tipi: 10 DESCRIPTION + 2 TEXT + 1 VALUE',
   kinds == {'DESCRIPTION': 10, 'TEXT': 2, 'VALUE': 1}, dict(kinds))
ck('sei contesti', len(grp) == 6, dict(grp))
ck('TERZINE `Orchid` 801/802/803 e `Ophrys` 949/950/951, tab sulla 2a e 3a',
   all([u['line'] for u in cov if u['context'] == c and u['kind'] == 'DESCRIPTION'] == ls
       for c, ls in TERZINE.items())
   and all(at[l]['english'].startswith(TAB) and at[l]['italian'].startswith(TAB)
           for ls in TERZINE.values() for l in ls[1:])
   and all(not at[ls[0]]['english'].startswith(TAB) for ls in TERZINE.values()))
ck('COPPIE `Nettle KKV` 716/717 e `Ophrys Stockpile` 968/969, tab sulla seconda',
   all(at[b]['context'] == at[a]['context'] and at[b]['english'].startswith(TAB) for a, b in COPPIE))
ck('TAB: esattamente sei unita la portano, alle righe dichiarate',
   sorted(u['line'] for u in cov if u['english'].startswith(TAB)) == TABBED
   and sum(u['italian'].count(TAB) for u in cov) == 6)
ck('TEXT copiati VERBATIM (2) e VALUE copiato (1)',
   all(by[i]['italian'] == by[i]['english'] for i in TEXT_IDX + VALUE_IDX),
   {i: (by[i]['english'], by[i]['italian']) for i in TEXT_IDX + VALUE_IDX if by[i]['italian'] != by[i]['english']})
ck('le 4 virgolette sono 2 COPPIE, una per unita TEXT',
   sum(u['italian'].count(QUOTE) for u in cov) == 4
   and all(by[i]['italian'].count(QUOTE) == 2 for i in TEXT_IDX))
ck('la TEXT della 788 ha contesto `(root)` (la radice del file)',
   by[4]['context'] == '(root)')
ck('«ammunition for» in TRE varianti: arma e contenitore diversi, struttura uguale',
   all('è munizione per il' in by[i]['italian'] or 'è munizione per l\'' in by[i]['italian'] for i in AMMO3)
   and 'Vertical Launch Array' in by[2]['italian']
   and 'External Launch Tube' in by[7]['italian']
   and 'External Launch Rail' in by[10]['italian'])
ck('la NOTA MUNIZIONI di L307/L308 NON compare in questo lotto',
   'si possono rifornire in qualsiasi emporio' not in ''.join(u['italian'] for u in cov))
ck('SECONDA PERSONA solo negli avvisi di gioco (unita 2, 7, 10)',
   [u['idx'] for u in cov if re.search(r'\b(tu|tuo|tua|tuoi|tue|ti|te|puoi)\b', u['italian'])] == TU,
   [u['idx'] for u in cov if re.search(r'\b(tu|tuo|tua|tuoi|tue|ti|te|puoi)\b', u['italian'])])
ck('le 10 DESCRIPTION sono tutte TRADOTTE',
   all(u['italian'] != u['english'] for u in cov if u['kind'] == 'DESCRIPTION'))
ck('SEGNAPOSTO e ALTERNATIVE: zero (asserzioni vuote)',
   sum(len(TAG.findall(u['italian'])) for u in cov) == 0
   and sum(len(ALT.findall(u['italian'])) for u in cov) == 0)
ck('APICI: tre in inglese (801, 802, 949), diciassette in italiano',
   sum(u['english'].count(APOS) for u in cov) == 3 and sum(u['italian'].count(APOS) for u in cov) == 17,
   (sum(u['english'].count(APOS) for u in cov), sum(u['italian'].count(APOS) for u in cov)))
ck('nomi invariati: Nettle, Orchid, Ophrys, Nettle Flecks, contenitori',
   all(n in ''.join(u['italian'] for u in cov) for n in
       ['Nettle', 'Orchid', 'Ophrys', 'Vertical Launch Array', 'External Launch Tube',
        'External Launch Rail', 'Ophrys Stockpile']),
   [n for n in ['Nettle', 'Orchid', 'Ophrys', 'Vertical Launch Array', 'External Launch Tube',
                'External Launch Rail', 'Ophrys Stockpile'] if n not in ''.join(u['italian'] for u in cov)])
ck('lessico: barre di tungsteno, ottazacubano, corazzatura ablativa, nave da guerra capitale',
   'barre di tungsteno' in by[1]['italian'] and 'ottazacubano' in by[1]['italian']
   and 'corazzatura ablativa' in by[8]['italian'] and 'nave da guerra capitale' in by[8]['italian'])
ck('nessun caporale, nessun carattere tipografico',
   not [u['idx'] for u in cov for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026' if c in u['italian']])
nonlat = [(u['idx'], c) for u in cov for c in u['italian'] if ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessun doppio spazio (la tab iniziale non conta)',
   not [u['idx'] for u in cov if '  ' in u['italian'].lstrip(TAB)])
ck('rapporto nel gate 0,55-1,90 (0,97-1,30)',
   all(0.55 < u['ratio'] < 1.90 for u in cov),
   [(u['idx'], u['ratio']) for u in cov if not 0.55 < u['ratio'] < 1.90])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck('FILE: 33 unita prima della 716 (12 + 21)',
   db.execute('select count(*) from units where path=? and line<716', (PATH,)).fetchone()[0] == 33)
ck('FILE: ZERO unita dopo la 969 — il lotto CHIUDE il file',
   db.execute('select count(*) from units where path=? and line>969', (PATH,)).fetchone()[0] == 0)
ck('FILE: 46 unita, righe 25-969, 35 DESCRIPTION + 7 TEXT + 4 VALUE',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (46, 25, 969)
   and dict(db.execute('select kind,count(*) from units where path=? group by kind', (PATH,)).fetchall())
   == {'DESCRIPTION': 35, 'TEXT': 7, 'VALUE': 4})
ck('FILE: i tre lotti sommano 46 (12 + 21 + 13)', 12 + 21 + 13 == 46)
ck('tutte le 13 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · 10 DESCRIPTION + 2 TEXT + 1 VALUE · 6 tab · FILE 46/46' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
