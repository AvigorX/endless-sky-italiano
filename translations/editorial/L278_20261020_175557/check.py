r"""check.py — L278 (`data/human/kestrel.txt`, righe 15-54). **Primo lotto del file**.

**16 unita'** in **un solo contesto** (`mission:Kestrel Testing`): la missione in cui **Charles Atinoda**, progettista capo
della Tarazed Corporation, chiede al giocatore di collaudare la **Kestrel**. Quattro cose da verificare con cura:

1. **42 virgolette**, due per battuta: il test le conta **per unita'** (2 in inglese => 2 in italiano, e **dritte**);
2. **13 tab**, su tutte le battute tranne la prima (unita' 3): primo carattere, conservati;
3. **cinque segnaposto** (`<waypoints>` 1, `<first>` 2, `<last>` 2), con i conteggi per famiglia;
4. **un `VALUE`** (`Warship Testing`) si **copia**; la `DESCRIPTION` e le 14 `MISSION_TEXT` si traducono.
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
TABBED = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
TOK = {'<waypoints>': 1, '<first>': 2, '<last>': 2}
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck('unita tradotte 16/16', len(cov) == 16 == len(units), '%d/%d' % (len(cov), len(units)))
ck('tipi: 14 MISSION_TEXT + 1 DESCRIPTION + 1 VALUE',
   collections.Counter(u['kind'] for u in units) == {'MISSION_TEXT': 14, 'DESCRIPTION': 1, 'VALUE': 1},
   dict(collections.Counter(u['kind'] for u in units)))
ck('un solo contesto, `mission:Kestrel Testing`, righe 15-54',
   {u['context'] for u in cov} == {'mission:Kestrel Testing'} and len(cov) == 16
   and cov[0]['line'] == 15 and cov[-1]['line'] == 54)
ck('righe 15-54, nessun buco interno',
   [u['line'] for u in cov] == sorted({u['line'] for u in cov}))
ck('il VALUE e COPIATO (`Warship Testing`)',
   by[1]['kind'] == 'VALUE' and by[1]['italian'] == by[1]['english'] == 'Warship Testing')
ck('le 15 unita di prosa sono TRADOTTE, nessuna copiata',
   all(u['italian'] != u['english'] for u in cov if u['idx'] != 1),
   [u['idx'] for u in cov if u['idx'] != 1 and u['italian'] == u['english']])
ck('TAB: tredici in inglese e tredici in italiano, sulle stesse unita, come PRIMO carattere',
   sum(u['english'].count(TAB) for u in cov) == 13 == sum(u['italian'].count(TAB) for u in cov)
   and [u['idx'] for u in cov if TAB in u['english']] == TABBED == [u['idx'] for u in cov if TAB in u['italian']]
   and all(u['italian'].startswith(TAB) for u in cov if u['idx'] in TABBED))
ck('VIRGOLETTE: 42 in inglese e 42 in italiano, con lo STESSO numero per ogni unita',
   sum(u['english'].count(QUOTE) for u in cov) == 42 == sum(u['italian'].count(QUOTE) for u in cov)
   and all(u['english'].count(QUOTE) == u['italian'].count(QUOTE) for u in cov),
   [(u['idx'], u['english'].count(QUOTE), u['italian'].count(QUOTE)) for u in cov
    if u['english'].count(QUOTE) != u['italian'].count(QUOTE)])
ck('SEGNAPOSTO per famiglia: 5 token, tre famiglie, identici in inglese e italiano',
   {t: sum(collections.Counter(TAG.findall(u['english']))[t] for u in cov) for t in TOK} == TOK
   == {t: sum(collections.Counter(TAG.findall(u['italian']))[t] for u in cov) for t in TOK})
ck('APICI in inglese: 4 (unita 3, 5, 6, 16)',
   {u['idx']: u['english'].count(APOS) for u in cov if APOS in u['english']} == {3: 1, 5: 1, 6: 1, 16: 1},
   {u['idx']: u['english'].count(APOS) for u in cov if APOS in u['english']})
ck('APICI in italiano: 9 su 7 unita, mappa dichiarata',
   {u['idx']: u['italian'].count(APOS) for u in cov if APOS in u['italian']}
   == {2: 1, 6: 3, 8: 1, 9: 1, 10: 1, 11: 1, 16: 1},
   {u['idx']: u['italian'].count(APOS) for u in cov if APOS in u['italian']})
ck('la DESCRIPTION dice DISABILITARE, non distruggere (o si perde il pagamento)',
   'disabilitare' in by[2]['italian'] and 'Non distruggere' in by[2]['italian']
   and 'perderai il pagamento' in by[2]['italian'])
ck('nomi propri invariati: Tarazed Corporation, Wayfarer, Charles Atinoda, Welsh Corgi',
   all(n in ' '.join(u['italian'] for u in cov)
       for n in ('Tarazed Corporation', 'Wayfarer', 'Charles Atinoda', 'Welsh Corgi')))
ck('registro unico «tu»: nessuna forma di cortesia (`Lei`, `Senta`, `desidera`)',
   not [u['idx'] for u in cov if re.search(r'\b(Lei|Senta|desidera|sarebbe disposto)\b', u['italian'])],
   [u['idx'] for u in cov if re.search(r'\b(Lei|Senta|desidera)\b', u['italian'])])
ck('le due battute quasi identiche (unita 9 e 10) restano DISTINTE',
   by[9]['italian'] != by[10]['italian']
   and by[9]['italian'].startswith('\tIgnora la tua domanda.')
   and by[10]['italian'].startswith('\t"Ma poi'))
ck('lessico: collaudo, prototipo, linea di produzione, liberatorie, capanna del sudore',
   'collaudare' in by[3]['italian'] and 'prototipo' in by[2]['italian']
   and 'linea di produzione' in by[14]['italian'] and 'Liberatorie' in by[16]['italian']
   and 'capanna del sudore' in by[6]['italian'])
ck('nessun caporale, nessun carattere tipografico',
   not [u['idx'] for u in cov for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026' if c in u['italian']])
nonlat = [(u['idx'], c) for u in cov for c in u['italian'] if ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']],
   [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90 (0,86-1,13)',
   all(0.55 < u['ratio'] < 1.90 for u in cov if u['idx'] != 1),
   [(u['idx'], u['ratio']) for u in cov if u['idx'] != 1 and not 0.55 < u['ratio'] < 1.90])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("ZERO unita' prima della 15: il lotto APRE il file",
   db.execute('select count(*) from units where path=? and line<15', (PATH,)).fetchone()[0] == 0)
ck("35 unita' dopo la 54",
   db.execute('select count(*) from units where path=? and line>54', (PATH,)).fetchone()[0] == 35)
ck('il file ha 51 unita, righe 15-402',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (51, 15, 402),
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone())
st = dict(db.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('tutte le 16 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · 1 contesto · 13 tab · 42 virgolette' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
