r"""check.py — L275 (`data/korath/korath ships.txt`, righe 606-1311). Terzo lotto del file.

**9 `DESCRIPTION` + 5 `VALUE`** su **sette navi Korath**: cinque «A'awoj» da produzione e i due grandi abitati nomadi
(`Kasichara` e `Korsmanath A'awoj`). Quattro cose da verificare con cura:

1. **cinque `VALUE`** sono nomi di variante (`Karek`, `Sapira`, `Dathnak`, `Spera`, `Ikfar` + `A'awoj`): si **copiano**,
   e il test distingue «identico» per quegli indici e «tradotto» per le nove `DESCRIPTION`;
2. **due virgolette**, entrambe all’unita’ 11, attorno a `"navi-mondo"`: restano **dritte** e restano **due**;
3. **due tab** (unita’ 12 e 14), primo carattere;
4. **nove apici inglesi** (tutti nei nomi `A'awoj`) e **sedici italiani**: mappe diverse, entrambe dichiarate.
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
HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
PATH = 'data/korath/korath ships.txt'
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
BLOCCHI = [("ship:Lor'kas Ik 577", 606, 679), ("ship:Ra'gru Ik 618", 683, 765),
           ("ship:Kas'lor Ik 582", 769, 839), ("ship:Lor'nag Ik 590", 843, 916),
           ("ship:Ra'at Ik 621", 920, 1005), ("ship:Kasichara A'awoj", 1073, 1074),
           ("ship:Korsmanath A'awoj", 1310, 1311)]
VALORI = [1, 3, 5, 7, 9]
DESC = [2, 4, 6, 8, 10, 11, 12, 13, 14]
TABBED = [12, 14]
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck('unita tradotte 14/14', len(cov) == 14 == len(units), '%d/%d' % (len(cov), len(units)))
ck('tipi: 9 DESCRIPTION + 5 VALUE',
   collections.Counter(u['kind'] for u in units) == {'DESCRIPTION': 9, 'VALUE': 5},
   dict(collections.Counter(u['kind'] for u in units)))
ck('sette contesti, con le righe misurate',
   [(c, by[[u['idx'] for u in cov if u['context'] == c][0]]['line'],
     by[[u['idx'] for u in cov if u['context'] == c][-1]]['line']) for c, _, _ in BLOCCHI] == BLOCCHI,
   [(c, by[[u['idx'] for u in cov if u['context'] == c][0]]['line']) for c, _, _ in BLOCCHI])
ck('righe 606-1311, nessun buco interno, ultima unita alla 1311',
   [u['line'] for u in cov] == sorted({u['line'] for u in cov})
   and cov[0]['line'] == 606 and cov[-1]['line'] == 1311)
ck('i CINQUE VALUE sono COPIATI (nomi di variante)',
   all(by[i]['kind'] == 'VALUE' and by[i]['italian'] == by[i]['english'] for i in VALORI)
   and [by[i]['italian'] for i in VALORI]
   == ["Karek A'awoj", "Sapira A'awoj", "Dathnak A'awoj", "Spera A'awoj", "Ikfar A'awoj"],
   [by[i]['italian'] for i in VALORI])
ck('le NOVE DESCRIPTION sono TRADOTTE, nessuna copiata',
   all(by[i]['italian'] != by[i]['english'] for i in DESC),
   [i for i in DESC if by[i]['italian'] == by[i]['english']])
ck('TAB: due in inglese e due in italiano, alle unita 12 e 14, come PRIMO carattere',
   sum(u['english'].count(TAB) for u in cov) == 2 == sum(u['italian'].count(TAB) for u in cov)
   and [u['idx'] for u in cov if TAB in u['english']] == TABBED == [u['idx'] for u in cov if TAB in u['italian']]
   and all(u['italian'].startswith(TAB) for u in cov if u['idx'] in TABBED))
ck('VIRGOLETTE: due in inglese e due in italiano, all unita 11, DRITTE, attorno a "navi-mondo"',
   sum(u['english'].count(QUOTE) for u in cov) == 2 == sum(u['italian'].count(QUOTE) for u in cov)
   and [u['idx'] for u in cov if QUOTE in u['italian']] == [11]
   and '"navi-mondo"' in by[11]['italian'],
   (sum(u['italian'].count(QUOTE) for u in cov), by[11]['italian'][:60]))
ck('APICI in inglese: 9, tutti nei nomi `A\'awoj`',
   {u['idx']: u['english'].count(APOS) for u in cov if APOS in u['english']}
   == {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 7: 1, 9: 1, 13: 1, 14: 1},
   {u['idx']: u['english'].count(APOS) for u in cov if APOS in u['english']})
ck('APICI in italiano: 16 su 13 unita, mappa dichiarata',
   {u['idx']: u['italian'].count(APOS) for u in cov if APOS in u['italian']}
   == {1: 1, 2: 1, 3: 1, 4: 2, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 11: 1, 12: 1, 13: 2, 14: 2},
   {u['idx']: u['italian'].count(APOS) for u in cov if APOS in u['italian']})
ck('i nomi Korath restano dove l inglese li nomina',
   not [(u['idx'], n) for u in cov
        for n in ("Lor'kas Ik 577", "Ra'gru Ik 618", "Kas'lor Ik 582", "Lor'nag Ik 590", "Ra'at Ik 621",
                  'Efreti', 'Mereti', 'Sestor', 'Korsmanathi', 'Anatruskor', 'Deka Dathnak')
        if n in u['english'] and n not in u['italian']],
   [(u['idx'], n) for u in cov
    for n in ("Lor'kas Ik 577", "Ra'gru Ik 618", "Kas'lor Ik 582", "Lor'nag Ik 590", "Ra'at Ik 621",
              'Efreti', 'Mereti', 'Sestor', 'Korsmanathi', 'Anatruskor', 'Deka Dathnak')
    if n in u['english'] and n not in u['italian']])
ck('`Korsmanath A\'awoj` ripete la forma usata in L273 (senza articolo nel nome)',
   by[13]['italian'].startswith("I Korsmanath A'awoj") and "Korsmanath A'awoj" in by[14]['italian'])
ck('la formula comune e IDENTICA nelle cinque navi da produzione',
   len({by[i]['italian'].split('.')[0] for i in (2, 4, 6, 8, 10)}) == 1,
   [by[i]['italian'].split('.')[0] for i in (2, 4, 6, 8, 10)])
ck('lessico: navi da produzione, telaio, motore di salto, portatrici, gruppo d abbordaggio, hangar',
   'navi da produzione' in by[2]['italian'] and 'telaio comune e antico' in by[2]['italian']
   and 'motore di salto' in by[8]['italian'] and 'portatrici' in by[10]['italian']
   and "gruppi d'abbordaggio" in by[8]['italian'] and 'hangar' in by[10]['italian'])
ck('le due grandi navi: navi-città, navarchi, abitati nomadi, città volanti',
   'navi-città' in by[12]['italian'] and 'navarchi' in by[14]['italian']
   and 'abitati nomadi' in by[13]['italian'] and 'città volanti' in by[13]['italian'])
ck('nessun residuo inglese delle parole chiave (`hangar` e `navarchi` sono parole italiane)',
   not [u['idx'] for u in cov for w in ('chassis', 'jump drive', 'world-ship', 'city ship', 'production vessel')
        if w in u['italian'].lower()]
   and 'hangar' in by[10]['italian'] and 'navarchi' in by[14]['italian'],
   [(u['idx'], w) for u in cov for w in ('chassis', 'jump drive', 'world-ship', 'city ship', 'production vessel')
    if w in u['italian'].lower()])
ck('nessun caporale, nessun carattere tipografico',
   not [u['idx'] for u in cov for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026' if c in u['italian']])
nonlat = [(u['idx'], c) for u in cov for c in u['italian'] if ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']],
   [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90 per le nove DESCRIPTION (1,06-1,17)',
   all(0.55 < by[i]['ratio'] < 1.90 for i in DESC),
   [(i, by[i]['ratio']) for i in DESC if not 0.55 < by[i]['ratio'] < 1.90])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("17 unita' prima (L273 + L274)",
   db.execute('select count(*) from units where path=? and line<606', (PATH,)).fetchone()[0] == 17)
ck("19 unita' dopo la 1311",
   db.execute('select count(*) from units where path=? and line>1311', (PATH,)).fetchone()[0] == 19)
ck('il file ha 50 unita, righe 95-2363',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (50, 95, 2363))
st = dict(db.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('tutte le 14 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · 7 contesti · 2 tab · 2 virgolette' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
