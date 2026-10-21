r"""check.py — L308 (`data/avgi/avgi weapons.txt`, righe 264-703). **Secondo lotto del file**.

**Ventuno unita' di TRE tipi**: **13 `DESCRIPTION`** da tradurre, **5 `TEXT`** e **3 `VALUE`** da **copiare verbatim**.

Il test verifica:

1. **i cinque `TEXT`** sono **nomi di munizione fra virgolette** (`"Ophrys" Nuclear Torpedo`, `"Orchid" Nuclear Missile`,
   `"Nettle" KKV` ×3) e sono **copiati identici**; i **tre `VALUE`** (`Vertical Launch Array (9/18/36)`) idem;
2. **le 10 virgolette** sono **5 coppie**, una per unita' `TEXT`;
3. **la nota munizioni** torna **tre volte** (615, 659, 703) ed e' **identica** alle due di L307 (69, 108) — il testo riapre il
   `translation.json` precedente;
4. **il paragrafo VLS** torna **tre volte identico** (614, 658, 702) con `set()`;
5. **tre terzine** con due tab consecutive e **una coppia** (`Blue Optical Laser` 264/265);
6. **la 265 e' la sorella della 203** di L307: stessa frase, `Blue Laser` invece di `Green Laser`.
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
PREV = os.path.join(L10N, 'staging', 'editorial', 'L307_20261020_205626', 'translation.json')
PATH = 'data/avgi/avgi weapons.txt'
TERZINE = {'outfit:Tiny VLS': [613, 614, 615], 'outfit:Small VLS': [657, 658, 659],
           'outfit:Medium VLS': [701, 702, 703]}
COPPIA = (264, 265)
TABBED = [265, 614, 615, 658, 659, 702, 703]
VLS = [10, 15, 20]
AMMO = [11, 16, 21]
TEXT_IDX = [3, 5, 8, 13, 18]
VALUE_IDX = [7, 12, 17]
NOTA = '\tLe munizioni di quest\'arma si possono rifornire in qualsiasi emporio.'
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
kinds = collections.Counter(u['kind'] for u in cov)
ck('unita tradotte 21/21', len(cov) == 21 == len(units), '%d/%d' % (len(cov), len(units)))
ck('tre tipi: 13 DESCRIPTION + 5 TEXT + 3 VALUE',
   kinds == {'DESCRIPTION': 13, 'TEXT': 5, 'VALUE': 3}, dict(kinds))
ck('sei contesti: 3 VLS da cinque unita + 1 coppia + 2 doppi',
   len(grp) == 6 and sorted(grp.values()) == [2, 2, 2, 5, 5, 5], dict(grp))
ck('TEXT copiati VERBATIM (nomi di munizione fra virgolette)',
   all(by[i]['italian'] == by[i]['english'] for i in TEXT_IDX),
   {i: (by[i]['english'], by[i]['italian']) for i in TEXT_IDX if by[i]['italian'] != by[i]['english']})
ck('VALUE copiati VERBATIM (`Vertical Launch Array (N)`)',
   all(by[i]['italian'] == by[i]['english'] for i in VALUE_IDX),
   {i: (by[i]['english'], by[i]['italian']) for i in VALUE_IDX if by[i]['italian'] != by[i]['english']})
ck('le 10 virgolette sono 5 COPPIE, una per unita TEXT',
   sum(u['italian'].count(QUOTE) for u in cov) == 10
   and all(by[i]['italian'].count(QUOTE) == 2 for i in TEXT_IDX),
   [(i, by[i]['italian'].count(QUOTE)) for i in TEXT_IDX])
ck('TERZINE VLS: tre gruppi, tab sulla 2a e 3a unita',
   all([u['line'] for u in cov if u['context'] == c and u['kind'] == 'DESCRIPTION'] == ls
       for c, ls in TERZINE.items())
   and all(at[l]['english'].startswith(TAB) and at[l]['italian'].startswith(TAB)
           for ls in TERZINE.values() for l in ls[1:]))
ck('COPPIA `Blue Optical Laser` 264/265, tab sulla seconda',
   at[265]['context'] == at[264]['context'] and at[265]['english'].startswith(TAB)
   and not at[264]['english'].startswith(TAB))
ck('TAB: esattamente sette unita la portano, alle righe dichiarate',
   sorted(u['line'] for u in cov if u['english'].startswith(TAB)) == TABBED
   and sum(u['italian'].count(TAB) for u in cov) == 7)
ck('PARAGRAFO VLS identico nelle tre colonne (614, 658, 702)',
   len({by[i]['italian'] for i in VLS}) == 1 and len({by[i]['english'] for i in VLS}) == 1)
ck('NOTA MUNIZIONI: tre qui identiche fra loro e alle due di L307 (69, 108)',
   len({by[i]['italian'] for i in AMMO}) == 1 and by[AMMO[0]]['italian'] == NOTA
   and prev[69]['italian'] == NOTA and prev[108]['italian'] == NOTA,
   by[AMMO[0]]['italian'][:40])
ck('la 265 e la sorella della 203 di L307: stessa frase, `un solo Blue Laser` vs `tre Green Laser`',
   at[265]['italian'].replace('un solo Blue Laser', 'X') == prev[203]['italian'].replace('tre Green Laser', 'X')
   and 'un solo Blue Laser' in at[265]['italian'],
   at[265]['italian'][-60:])
ck('le 13 DESCRIPTION sono tutte TRADOTTE',
   all(u['italian'] != u['english'] for u in cov if u['kind'] == 'DESCRIPTION'))
ck('SEGNAPOSTO e ALTERNATIVE: zero (asserzioni vuote)',
   sum(len(TAG.findall(u['italian'])) for u in cov) == 0
   and sum(len(ALT.findall(u['italian'])) for u in cov) == 0)
ck('APICI: tre in inglese (264, 613 x2), nove in italiano',
   sum(u['english'].count(APOS) for u in cov) == 3 and sum(u['italian'].count(APOS) for u in cov) == 9,
   (sum(u['english'].count(APOS) for u in cov), sum(u['italian'].count(APOS) for u in cov)))
ck('nomi invariati: Avgi, munizioni, VLS, laser ottici',
   all(n in ''.join(u['italian'] for u in cov) for n in
       ['Avgi', 'Ophrys', 'Orchid', 'Nettle', 'Vertical Launch Array', 'Blue Laser', 'Optical Lasing Generator']),
   [n for n in ['Avgi', 'Ophrys', 'Orchid', 'Nettle', 'Vertical Launch Array', 'Blue Laser',
                'Optical Lasing Generator'] if n not in ''.join(u['italian'] for u in cov)])
ck('lessico: pilone, catapulta elettromagnetica, celle di lancio, alloggiamento per torrette',
   'pilone' in by[4]['italian'] and 'catapulta elettromagnetica' in by[4]['italian']
   and 'celle di lancio' in by[9]['italian'] and 'alloggiamento per torrette' in by[9]['italian'])
ck('REGISTRO: nessuna seconda persona (le TEXT/VALUE non sono prosa)',
   not [u['idx'] for u in cov if u['kind'] == 'DESCRIPTION'
        and re.search(r'\b(tu|tuo|tua|tuoi|tue|ti|te)\b', u['italian'])])
ck('nessun caporale, nessun carattere tipografico',
   not [u['idx'] for u in cov for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026' if c in u['italian']])
nonlat = [(u['idx'], c) for u in cov for c in u['italian'] if ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessun doppio spazio (la tab iniziale non conta)',
   not [u['idx'] for u in cov if '  ' in u['italian'].lstrip(TAB)])
ck('rapporto nel gate 0,55-1,90 (0,97-1,29)',
   all(0.55 < u['ratio'] < 1.90 for u in cov),
   [(u['idx'], u['ratio']) for u in cov if not 0.55 < u['ratio'] < 1.90])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("12 unita' prima della 264 (L307)",
   db.execute('select count(*) from units where path=? and line<264', (PATH,)).fetchone()[0] == 12)
ck("13 unita' dopo la 703; la prima apre `Nettle KKV` alla 716",
   db.execute('select count(*) from units where path=? and line>703', (PATH,)).fetchone()[0] == 13
   and db.execute('select line,context from units where path=? and line>703 order by line limit 1', (PATH,)).fetchone()
   == (716, 'outfit:"Nettle" KKV'))
ck('il file ha 46 unita (35 DESCRIPTION + 7 TEXT + 4 VALUE), righe 25-969',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (46, 25, 969)
   and dict(db.execute('select kind,count(*) from units where path=? group by kind', (PATH,)).fetchall())
   == {'DESCRIPTION': 35, 'TEXT': 7, 'VALUE': 4})
ck('tutte le 21 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · 13 DESCRIPTION + 5 TEXT + 3 VALUE · 7 tab · 10 virgolette · file 33/46' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
