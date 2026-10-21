r"""check.py — L279 (`data/human/kestrel.txt`, righe 56-164). Secondo lotto del file.

**33 `MISSION_TEXT`** del colloquio tecnico: il giocatore distrugge (o disabilita) il prototipo, Atinoda chiede **cosa
cambiare**, e poi la **sceneggiata del nome**, che e' il cuore comico della missione. Quattro cose da verificare con cura:

1. **94 virgolette** su 33 battute: il test le conta **per unita'** (una sola dimenticata lascerebbe il totale a 93 e
   passerebbe un controllo aggregato);
2. **32 tab**: l'unica unita' NON rientrata e' la 4 (la narrazione dell'incontro dopo l'atterraggio);
3. **il nome scelto**: le battute propongono `Wraith`, `Grey Goose`, `Dire Wolf`, `Kestrel`, `Reaper`, e `Kestrel` torna
   **quattro volte** — il test verifica i conteggi, non solo la presenza;
4. **`'Kestrel'` fra apici semplici** all'unita' 33: sono **due** apici, e restano.
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
TOK = {'<waypoints>': 1, '<first>': 1, '<last>': 1}
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck('unita tradotte 33/33', len(cov) == 33 == len(units), '%d/%d' % (len(cov), len(units)))
ck('tipo: 33 MISSION_TEXT, nessun VALUE',
   collections.Counter(u['kind'] for u in units) == {'MISSION_TEXT': 33},
   dict(collections.Counter(u['kind'] for u in units)))
ck('un solo contesto, `mission:Kestrel Testing`, righe 56-164',
   {u['context'] for u in cov} == {'mission:Kestrel Testing'}
   and cov[0]['line'] == 56 and cov[-1]['line'] == 164)
ck('righe 56-164, nessun buco interno',
   [u['line'] for u in cov] == sorted({u['line'] for u in cov}))
ck('tutte TRADOTTE, nessuna copiata',
   all(u['italian'] != u['english'] for u in cov), [u['idx'] for u in cov if u['italian'] == u['english']])
ck('TAB: 32 in inglese e 32 in italiano; l unica unita senza rientro e la 4 (narrazione)',
   sum(u['english'].count(TAB) for u in cov) == 32 == sum(u['italian'].count(TAB) for u in cov)
   and [u['idx'] for u in cov if TAB not in u['italian']] == [4]
   and by[4]['italian'].startswith('Atinoda ti raggiunge'))
ck('VIRGOLETTE: 94 in inglese e 94 in italiano, con lo STESSO numero per ogni unita',
   sum(u['english'].count(QUOTE) for u in cov) == 94 == sum(u['italian'].count(QUOTE) for u in cov)
   and all(u['english'].count(QUOTE) == u['italian'].count(QUOTE) for u in cov),
   [(u['idx'], u['english'].count(QUOTE), u['italian'].count(QUOTE)) for u in cov
    if u['english'].count(QUOTE) != u['italian'].count(QUOTE)])
ck('SEGNAPOSTO per famiglia: 3 token, tre famiglie, identici in inglese e italiano',
   {t: sum(collections.Counter(TAG.findall(u['english']))[t] for u in cov) for t in TOK} == TOK
   == {t: sum(collections.Counter(TAG.findall(u['italian']))[t] for u in cov) for t in TOK})
ck('APICI in inglese: 16 su 11 unita (unita 33 con sei)',
   sum(u['english'].count(APOS) for u in cov) == 16
   and {u['idx']: u['english'].count(APOS) for u in cov if APOS in u['english']}
   == {2: 1, 3: 1, 6: 1, 13: 1, 14: 1, 15: 1, 16: 1, 24: 1, 27: 1, 30: 1, 33: 6},
   {u['idx']: u['english'].count(APOS) for u in cov if APOS in u['english']})
ck('APICI in italiano: 10 su 8 unita, mappa dichiarata',
   {u['idx']: u['italian'].count(APOS) for u in cov if APOS in u['italian']}
   == {6: 1, 7: 1, 8: 1, 15: 1, 24: 2, 27: 1, 30: 1, 33: 2},
   {u['idx']: u['italian'].count(APOS) for u in cov if APOS in u['italian']})
ck("il nome `Kestrel` torna QUATTRO volte fra le proposte e vince",
   sum(1 for u in cov if u['italian'] == '\t"La Kestrel."') == 4
   and sum(1 for u in cov if u['italian'] == '\t"La Grey Goose."') == 2
   and sum(1 for u in cov if u['italian'] == '\t"Il Wraith."') == 2)
ck('gli altri nomi proposti restano invariati: Wraith, Grey Goose, Dire Wolf, Reaper',
   all(n in ' '.join(u['italian'] for u in cov) for n in ('Wraith', 'Grey Goose', 'Dire Wolf', 'Reaper')))
ck('le navi Tarazed gia\' esistenti sono nomi di uccelli e restano invariati: Falcon, Osprey, Hawk',
   'Falcon' in by[27]['italian'] and 'Osprey' in by[27]['italian'] and 'Hawk' in by[27]['italian']
   and 'sono uccelli' in by[27]['italian'])
ck("`'Kestrel'` fra apici semplici all'unita 33: due apici, conservati",
   "'Kestrel'" in by[33]['italian'] and by[33]['italian'].count(APOS) == 2)
ck('la regola del collaudo: disabilitare senza distruggere, o si perde il pagamento',
   'disabilitala senza distruggerla' in by[3]['italian']
   and 'perderai il pagamento' in by[3]['italian'])
ck('lessico: produrre in serie, ritocchi, capacità per le armi, matrice degli scudi, baie di caccia',
   'produrre questa nave in serie' in by[7]['italian'] and 'ritocco' in by[7]['italian']
   and 'capacità per le armi' in by[13]['italian'] and 'matrice degli scudi' in by[15]['italian']
   and 'baie di caccia' in by[12]['italian'])
ck('il pagamento finale: due milioni di crediti',
   'due milioni di crediti' in by[33]['italian'])
ck('nessun caporale, nessun carattere tipografico',
   not [u['idx'] for u in cov for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026' if c in u['italian']])
nonlat = [(u['idx'], c) for u in cov for c in u['italian'] if ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']],
   [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90 (0,71-1,14)',
   all(0.55 < u['ratio'] < 1.90 for u in cov),
   [(u['idx'], u['ratio']) for u in cov if not 0.55 < u['ratio'] < 1.90])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("16 unita' prima (L278)",
   db.execute('select count(*) from units where path=? and line<56', (PATH,)).fetchone()[0] == 16)
ck("2 unita' dopo la 164",
   db.execute('select count(*) from units where path=? and line>164', (PATH,)).fetchone()[0] == 2)
ck('il file ha 51 unita, righe 15-402',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (51, 15, 402))
st = dict(db.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('tutte le 33 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · 1 contesto · 32 tab · 94 virgolette' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
