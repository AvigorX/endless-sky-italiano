r"""check.py — L276 (`data/korath/korath ships.txt`, righe 1375-1961). Quarto lotto del file.

**12 `DESCRIPTION`, nessun `VALUE`** su **dieci navi**: tre Efreti (sotto protezione Quarg) e sette Kor Sestor robotiche.
Quattro cose da verificare con cura:

1. **due unita' sono stringhe GIA' TRADOTTE** (droni e caccia senza iperguida, unita' 10 e 12): si riprendono **alla lettera**
   e il test le confronta con la resa **piu' frequente** di tutti i `translation.json`;
2. **due virgolette** all'unita' 1, attorno a `"navi-mondo"`: restano **dritte**;
3. **due tab** (unita' 10 e 12), primo carattere;
4. **due apici inglesi soli** (`Efreti's`) e **sette italiani**: mappe diverse.
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
BLOCCHI = [('ship:Echo-Galleon', 1375, 1375), ('ship:Arch-Carrack', 1439, 1439),
           ('ship:Charm-Shallop', 1498, 1498), ('ship:Kar Ik Vot 349', 1567, 1567),
           ('ship:Tek Far 71 - Lek', 1648, 1648), ('ship:Tek Far 78 - Osk', 1729, 1729),
           ('ship:Tek Far 109', 1818, 1818), ('ship:Met Par Tek 53', 1878, 1878),
           ('ship:Far Lek 14', 1918, 1919), ('ship:Far Osk 27', 1960, 1961)]
TABBED = [10, 12]
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


def corpus_rese(english):
    c = collections.Counter()
    for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
        for u in json.load(open(f, encoding='utf-8'))['units']:
            if u['english'] == english:
                c[u['italian']] += 1
    return c


ck('unita tradotte 12/12', len(cov) == 12 == len(units), '%d/%d' % (len(cov), len(units)))
ck('tipo: 12 DESCRIPTION, nessun VALUE',
   collections.Counter(u['kind'] for u in units) == {'DESCRIPTION': 12},
   dict(collections.Counter(u['kind'] for u in units)))
ck('dieci contesti, con le righe misurate',
   [(c, by[[u['idx'] for u in cov if u['context'] == c][0]]['line'],
     by[[u['idx'] for u in cov if u['context'] == c][-1]]['line']) for c, _, _ in BLOCCHI] == BLOCCHI,
   [(c, by[[u['idx'] for u in cov if u['context'] == c][0]]['line']) for c, _, _ in BLOCCHI])
ck('righe 1375-1961, nessun buco interno, ultima unita alla 1961',
   [u['line'] for u in cov] == sorted({u['line'] for u in cov})
   and cov[0]['line'] == 1375 and cov[-1]['line'] == 1961)
ck('tutte TRADOTTE, nessuna copiata',
   all(u['italian'] != u['english'] for u in cov), [u['idx'] for u in cov if u['italian'] == u['english']])
ck('TAB: due in inglese e due in italiano, alle unita 10 e 12, come PRIMO carattere',
   sum(u['english'].count(TAB) for u in cov) == 2 == sum(u['italian'].count(TAB) for u in cov)
   and [u['idx'] for u in cov if TAB in u['english']] == TABBED == [u['idx'] for u in cov if TAB in u['italian']]
   and all(u['italian'].startswith(TAB) for u in cov if u['idx'] in TABBED))
ck('VIRGOLETTE: due in inglese e due in italiano, all unita 1, DRITTE, attorno a "navi-mondo"',
   sum(u['english'].count(QUOTE) for u in cov) == 2 == sum(u['italian'].count(QUOTE) for u in cov)
   and [u['idx'] for u in cov if QUOTE in u['italian']] == [1]
   and '"navi-mondo"' in by[1]['italian'])
c10, c12 = corpus_rese(by[10]['english']), corpus_rese(by[12]['english'])
ck('unita 10 (droni): la resa e quella PIU FREQUENTE del corpus, ripresa alla lettera',
   by[10]['italian'] in c10 and c10[by[10]['italian']] == max(c10.values()), dict(c10))
ck('unita 12 (caccia): la resa e quella PIU FREQUENTE del corpus, ripresa alla lettera',
   by[12]['italian'] in c12 and c12[by[12]['italian']] == max(c12.values()), dict(c12))
ck('APICI in inglese: 2, entrambi `Efreti\'s` (unita 2 e 3)',
   {u['idx']: u['english'].count(APOS) for u in cov if APOS in u['english']} == {2: 1, 3: 1},
   {u['idx']: u['english'].count(APOS) for u in cov if APOS in u['english']})
ck('APICI in italiano: 7 su 6 unita, mappa dichiarata',
   {u['idx']: u['italian'].count(APOS) for u in cov if APOS in u['italian']}
   == {1: 1, 3: 1, 4: 1, 5: 1, 6: 1, 9: 2},
   {u['idx']: u['italian'].count(APOS) for u in cov if APOS in u['italian']})
ck("la formula di apertura di L275 e ripresa: «derivano da un telaio comune e antico»",
   by[1]['italian'].startswith('Le più grandi navi da produzione Korath derivano da un telaio comune e antico'))
ck('i nomi delle fazioni e delle navi restano dove l inglese li nomina',
   not [(u['idx'], n) for u in cov
        for n in ('Efreti', 'Quarg', 'Mereti', 'Kor Sestor', 'TF109', 'FS27')
        if n in u['english'] and n not in u['italian']],
   [(u['idx'], n) for u in cov for n in ('Efreti', 'Quarg', 'Mereti', 'Kor Sestor', 'TF109', 'FS27')
    if n in u['english'] and n not in u['italian']])
ck('lessico: mercantile, portatrice, incrociatore da battaglia, agganci d attracco, scafo ultradenso',
   'mercantile' in by[2]['italian'] and 'portatrice' in by[6]['italian']
   and 'incrociatori da battaglia' in by[4]['italian'] and "agganci d'attracco" in by[6]['italian']
   and 'scafo ultradenso' in by[9]['italian'])
ck('le tre navi Efreti sono descritte come PROTETTE dai Quarg, non come potenze militari',
   'protettori Quarg' in by[1]['italian'] and 'oltre i Quarg' in by[2]['italian']
   and 'ispirati ai Quarg' in by[3]['italian'])
ck('nessun residuo inglese delle parole chiave',
   not [u['idx'] for u in cov for w in ('freighter', 'carrier', 'battlecruiser', 'docking clamp', 'hull')
        if w in u['italian'].lower()],
   [(u['idx'], w) for u in cov for w in ('freighter', 'carrier', 'battlecruiser', 'docking clamp', 'hull')
    if w in u['italian'].lower()])
ck('nessun caporale, nessun carattere tipografico',
   not [u['idx'] for u in cov for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026' if c in u['italian']])
nonlat = [(u['idx'], c) for u in cov for c in u['italian'] if ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']],
   [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90 (0,92-1,16)',
   all(0.55 < u['ratio'] < 1.90 for u in cov),
   [(u['idx'], u['ratio']) for u in cov if not 0.55 < u['ratio'] < 1.90])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("31 unita' prima (L273 + L274 + L275)",
   db.execute('select count(*) from units where path=? and line<1375', (PATH,)).fetchone()[0] == 31)
ck("7 unita' dopo la 1961",
   db.execute('select count(*) from units where path=? and line>1961', (PATH,)).fetchone()[0] == 7)
ck('il file ha 50 unita, righe 95-2363',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (50, 95, 2363))
st = dict(db.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('tutte le 12 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · 10 contesti · 2 tab · 2 virgolette' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
