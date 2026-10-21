r"""check.py — L288 (`data/gegno/gegno ships.txt`, righe 725-1192). **Terzo lotto del file**.

Nove unita' su **sette contesti**: otto descrizioni e **un `VALUE`** (`Gneiss`, riga 983). Il contesto `ship:Gneiss` ha **tre**
unita' — una `VALUE` e due `DESCRIPTION` — e il test le distingue **per tipo**, non per contesto. Verifica anche la coppia
consecutiva 1061-1062 e il fatto che `Halite` (riga 1192) sia **la stessa nave** che aprono le righe 1193+.
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
PATH = 'data/gegno/gegno ships.txt'
NAMES = ['Rhyolite', 'Eclogite', 'Diorite', 'Hornfel', 'Gneiss', 'Granulite', 'Halite', 'Gegno', 'Vi', 'Scin',
         'Ballistic Cannons']
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
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck('unita tradotte 9/9', len(cov) == 9 == len(units), '%d/%d' % (len(cov), len(units)))
ck('tipi: 8 DESCRIPTION + 1 VALUE, e il VALUE e alla riga 983',
   collections.Counter(u['kind'] for u in cov) == {'DESCRIPTION': 8, 'VALUE': 1}
   and [u['line'] for u in cov if u['kind'] == 'VALUE'] == [983],
   dict(collections.Counter(u['kind'] for u in cov)))
ck('sette contesti, con le righe dichiarate',
   [(u['context'], u['line']) for u in cov]
   == [('ship:Rhyolite', 725), ('ship:Eclogite', 776), ('ship:Diorite', 832), ('ship:Hornfel', 917),
       ('ship:Gneiss', 983), ('ship:Gneiss', 1061), ('ship:Gneiss', 1062), ('ship:Granulite', 1149),
       ('ship:Halite', 1192)],
   [(u['context'], u['line']) for u in cov])
ck('il VALUE `Gneiss` e COPIATO, e il test lo distingue dalle due DESCRIPTION dello stesso contesto',
   by[5]['kind'] == 'VALUE' and by[5]['italian'] == by[5]['english'] == 'Gneiss'
   and by[6]['kind'] == by[7]['kind'] == 'DESCRIPTION'
   and by[6]['italian'] != by[6]['english'] and by[7]['italian'] != by[7]['english']
   and {by[5]['context'], by[6]['context'], by[7]['context']} == {'ship:Gneiss'})
ck('le 8 DESCRIPTION sono TRADOTTE, nessuna copiata',
   all(u['italian'] != u['english'] for u in cov if u['kind'] == 'DESCRIPTION'),
   [u['idx'] for u in cov if u['kind'] == 'DESCRIPTION' and u['italian'] == u['english']])
ck('coppia consecutiva 1061-1062 nello stesso contesto, e la seconda CONTINUA',
   by[7]['line'] == by[6]['line'] + 1 and by[7]['context'] == by[6]['context'] == 'ship:Gneiss'
   and by[7]['italian'].lstrip(TAB).startswith('Purtroppo')
   and not by[7]['italian'].lstrip(TAB).startswith('I Gneiss'),
   by[7]['italian'][:40])
ck('TAB: uno solo, sull unita 7 (seconda meta del Gneiss), come PRIMO carattere',
   sum(u['english'].count(TAB) for u in cov) == 1 == sum(u['italian'].count(TAB) for u in cov)
   and [u['idx'] for u in cov if TAB in u['english']] == [7] == [u['idx'] for u in cov if TAB in u['italian']]
   and by[7]['italian'].startswith(TAB) and not by[6]['italian'].startswith(TAB))
ck('VIRGOLETTE: zero in inglese e zero in italiano',
   sum(u['english'].count(QUOTE) for u in cov) == 0 == sum(u['italian'].count(QUOTE) for u in cov))
ck('SEGNAPOSTO e ALTERNATIVE: zero',
   sum(len(TAG.findall(u['english'])) for u in cov) == 0 == sum(len(TAG.findall(u['italian'])) for u in cov)
   and sum(len(ALT.findall(u['english'])) for u in cov) == 0 == sum(len(ALT.findall(u['italian'])) for u in cov))
ck('APICI: nove in inglese, nove in italiano',
   sum(u['english'].count(APOS) for u in cov) == 9 == sum(u['italian'].count(APOS) for u in cov),
   (sum(u['english'].count(APOS) for u in cov), sum(u['italian'].count(APOS) for u in cov)))
ck('nomi di modello e di fazione INVARIATI',
   all(n in ''.join(u['italian'] for u in cov) for n in NAMES),
   [n for n in NAMES if n not in ''.join(u['italian'] for u in cov)])
ck('`Hornfel` resta `Hornfel` anche al plurale inglese (`Hornfels`), e `Gneiss` e invariabile',
   by[4]['italian'].count('Hornfel') == 4 and by[6]['italian'].count('Gneiss') == 2
   and 'Hornfels' not in by[4]['italian'] and 'Gneisss' not in by[6]['italian'])
ck('`Halite` descritto come velivolo dei **Scin** (non dei Vi)',
   'Gegno Scin' in by[9]['italian'] and 'velivolo da combattimento' in by[9]['italian'])
ck('registro in terza persona: nessun «tu»/«tuo»',
   not [u['idx'] for u in cov if re.search(r'\b(tu|tuo|tua|tuoi|tue|ti|te)\b', u['italian'])],
   [u['idx'] for u in cov if re.search(r'\b(tu|tuo|tua|tuoi|tue|ti|te)\b', u['italian'])])
ck('lessico: corazzatura, bordate, cannoniera, rifornimenti, velivolo, scafo',
   'corazzatura' in by[6]['italian'] and 'bordate' in by[6]['italian'] and 'cannoniera' in by[2]['italian']
   and 'rifornimenti' in by[4]['italian'] and 'velivolo' in by[9]['italian'] and 'scafo' in by[9]['italian'])
ck('nessun caporale, nessun carattere tipografico',
   not [u['idx'] for u in cov for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026' if c in u['italian']])
nonlat = [(u['idx'], c) for u in cov for c in u['italian'] if ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']],
   [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90 sulle 8 DESCRIPTION (1,11-1,19), il VALUE a 1,00',
   all(0.55 < by[i]['ratio'] < 1.90 for i in by if by[i]['kind'] == 'DESCRIPTION')
   and by[5]['ratio'] == 1.0,
   [(i, by[i]['ratio']) for i in by if by[i]['kind'] == 'DESCRIPTION' and not 0.55 < by[i]['ratio'] < 1.90])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("16 unita' prima della 725",
   db.execute('select count(*) from units where path=? and line<725', (PATH,)).fetchone()[0] == 16)
ck("12 unita' dopo la 1192",
   db.execute('select count(*) from units where path=? and line>1192', (PATH,)).fetchone()[0] == 12)
ck('`Halite` prosegue oltre il confine: la prima unita dopo la 1192 e ancora `ship:Halite`',
   db.execute('select context from units where path=? and line>1192 order by line limit 1', (PATH,)).fetchone()
   == ('ship:Halite',))
ck('il file ha 37 unita, righe 53-1616',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (37, 53, 1616))
ck('tutte le 9 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · 7 contesti · 8 DESCRIPTION + 1 VALUE · 1 tab · 0 virgolette' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
