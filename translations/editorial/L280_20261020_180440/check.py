r"""check.py — L280 (`data/human/kestrel.txt`, righe 252-402). **LOTTO TERMINALE: chiude il file.**

**Due unita'**: il **messaggio di disponibilita'** (`MISSION_TEXT`, con un discorso citato) e la **scheda della nave**
(`DESCRIPTION`), che **ripete il motivo della visione** gia' raccontato in L279. Quattro cose da verificare:

1. **lotto terminale**: oltre al segmento ci vuole l'**invariante di FILE** — 51 unita', righe distinte, ultima riga la
   **402**, **0 dopo**, somma dei tre lotti = 51;
2. **due virgolette**, entrambe nel messaggio: restano **dritte** e sono **due** anche in italiano;
3. **un segnaposto** (`<last>`) e **due apici inglesi** — quelli si misurano, non si presumono;
4. **coerenza con L279**: la `DESCRIPTION` racconta la stessa visione della capanna del sudore, e deve usare le stesse forme
   («capanna del sudore», «trance», «visioni»).
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
HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
PREV = os.path.join(L10N, 'staging', 'editorial', 'L278_20261020_175557', 'translation.json')
PATH = 'data/human/kestrel.txt'
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
prev = {u['idx']: u for u in json.load(open(PREV, encoding='utf-8'))['units']}
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck('unita tradotte 2/2', len(cov) == 2 == len(units), '%d/%d' % (len(cov), len(units)))
ck('tipi: 1 MISSION_TEXT + 1 DESCRIPTION',
   collections.Counter(u['kind'] for u in units) == {'MISSION_TEXT': 1, 'DESCRIPTION': 1},
   dict(collections.Counter(u['kind'] for u in units)))
ck('due contesti: `mission:Kestrel Available` (252) e `ship:Kestrel` (402)',
   [(u['context'], u['line']) for u in cov]
   == [('mission:Kestrel Available', 252), ('ship:Kestrel', 402)],
   [(u['context'], u['line']) for u in cov])
ck('tutte TRADOTTE, nessuna copiata',
   all(u['italian'] != u['english'] for u in cov), [u['idx'] for u in cov if u['italian'] == u['english']])
ck('ZERO tab (asserzione negativa)',
   sum(u['english'].count(TAB) + u['italian'].count(TAB) for u in cov) == 0)
ck('VIRGOLETTE: due in inglese e due in italiano, all unita 1, dritte',
   sum(u['english'].count(QUOTE) for u in cov) == 2 == sum(u['italian'].count(QUOTE) for u in cov)
   and [u['idx'] for u in cov if QUOTE in u['italian']] == [1]
   and '"Capitano <last>,' in by[1]['italian'])
ck('SEGNAPOSTO: `<last>` una volta, identico in inglese e italiano',
   collections.Counter(TAG.findall(by[1]['english'])) == {'<last>': 1}
   == collections.Counter(TAG.findall(by[1]['italian'])))
ck("APICI: due in inglese (unita 1 `We've`, unita 2 `Tarazed's`), UNO in italiano (`un'astronave`)",
   sum(u['english'].count(APOS) for u in cov) == 2 and sum(u['italian'].count(APOS) for u in cov) == 1
   and {u['idx']: u['italian'].count(APOS) for u in cov if APOS in u['italian']} == {2: 1},
   (sum(u['english'].count(APOS) for u in cov), sum(u['italian'].count(APOS) for u in cov),
    {u['idx']: u['italian'].count(APOS) for u in cov if APOS in u['italian']}))
ck('il messaggio annuncia la vendita su Wayfarer e ringrazia',
   'in vendita qui su Wayfarer' in by[1]['italian'] and 'Grazie ancora' in by[1]['italian']
   and 'tutti i tuoi commenti' in by[1]['italian'])
ck('la DESCRIPTION racconta la visione con le forme di L279: capanna del sudore, trance, visioni',
   'capanna del sudore' in by[2]['italian'] and 'trance' in by[2]['italian']
   and 'vide le visioni' in by[2]['italian'])
ck('coerenza cross-lot: la stessa espressione di L278 (la scena della visione) e ripresa alla lettera',
   'capanna del sudore' in prev[6]['italian'] and 'trance' in prev[6]['italian']
   and 'capanna del sudore' in by[2]['italian'])
ck('i nomi propri restano: Kestrel, Tarazed, Wayfarer, Charles Atinoda',
   all(n in ' '.join(u['italian'] for u in cov) for n in ('Kestrel', 'Tarazed', 'Wayfarer', 'Charles Atinoda')))
ck('nessun caporale, nessun carattere tipografico',
   not [u['idx'] for u in cov for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026' if c in u['italian']])
nonlat = [(u['idx'], c) for u in cov for c in u['italian'] if ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']],
   [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90',
   all(0.55 < u['ratio'] < 1.90 for u in cov),
   [(u['idx'], u['ratio']) for u in cov if not 0.55 < u['ratio'] < 1.90])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("49 unita' prima (L278 + L279)",
   db.execute('select count(*) from units where path=? and line<252', (PATH,)).fetchone()[0] == 49)
ck("ZERO unita' dopo la 402: il lotto CHIUDE il file",
   db.execute('select count(*) from units where path=? and line>402', (PATH,)).fetchone()[0] == 0)
ck('INVARIANTE DI FILE: 51 unita, righe 15-402, ultima alla 402',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (51, 15, 402))
somma, righe = 0, set()
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    us = [u for u in json.load(open(f, encoding='utf-8'))['units'] if u['path'] == PATH]
    if us:
        somma += len(us)
        righe |= {u['line'] for u in us}
ck('INVARIANTE DI FILE: somma dei tre lotti = 51, righe distinte = 51, nessuna riga fuori',
   somma == 51 and len(righe) == 51 and min(righe) == 15 and max(righe) == 402,
   (somma, len(righe)))
st = dict(db.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('tutte e 2 le unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · 2 contesti · 2 virgolette' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
