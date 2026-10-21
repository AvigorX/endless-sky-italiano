r"""check.py — L297 (`data/coalition/coalition outfits.txt`, righe 26-187). **PRIMO lotto del file**.

Quindici schede di equipaggiamento della Coalizione in **dodici contesti**, con **tre coppie** in cui la seconda unita' del
contesto **inizia con una tabulazione** (righe 55, 70, 85): la tab e' **struttura del gioco** e va conservata come primo
carattere.

Il test verifica:

1. **le tre coppie con tab**: ogni unita' che inizia con `\t` ha un'altra unita' **dello stesso contesto** nella riga
   precedente, e **solo** quelle tre iniziano con la tab;
2. **le nove unita' singole**: i contesti con una sola unita' sono **nove** (dodici contesti in tutto);
3. **la citazione interna**: l'unita' 14 nomina `Large Shield Module`, il modulo descritto dall'unita' 13 — il nome va
   lasciato **invariato**;
4. **zero seconda persona**: schede tecniche in terza persona.
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
PATH = 'data/coalition/coalition outfits.txt'
PAIRS = {54: 55, 69: 70, 84: 85}
SINGOLE = [26, 40, 99, 112, 125, 141, 156, 172, 187]
NAMES = ['Heliarch', 'Kimek', 'Quarg', 'Arach', 'Coalizione', 'Large Shield Module']
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


ck('unita tradotte 15/15', len(cov) == 15 == len(units), '%d/%d' % (len(cov), len(units)))
ck('tutte DESCRIPTION, dodici contesti, nove con una sola unita',
   {u['kind'] for u in cov} == {'DESCRIPTION'}
   and len({u['context'] for u in cov}) == 12
   and sum(1 for c, n in collections.Counter(u['context'] for u in cov).items() if n == 1) == 9,
   (len({u['context'] for u in cov}), collections.Counter(u['context'] for u in cov).most_common(3)))
ck('tutte e 15 le unita sono TRADOTTE, nessuna copiata',
   all(u['italian'] != u['english'] for u in cov), [u['idx'] for u in cov if u['italian'] == u['english']])
tabbed = [u for u in cov if u['english'].startswith(TAB)]
ck('TAB: esattamente tre unita la iniziano, alle righe 55, 70, 85',
   sorted(u['line'] for u in tabbed) == [55, 70, 85], [u['line'] for u in tabbed])
ck('TAB conservata come PRIMO carattere in tutte e tre',
   all(u['italian'].startswith(TAB) for u in tabbed)
   and sum(u['italian'].count(TAB) for u in cov) == 3)
ck('COPPIE: ogni unita con tab ha il compagno dello STESSO contesto alla riga precedente',
   all(by[i]['context'] == by[i - 1]['context'] and by[i]['line'] - 1 == by[i - 1]['line']
       for i in range(1, 16) if by[i]['line'] in [55, 70, 85]),
   [(by[i]['line'], by[i - 1]['line']) for i in range(1, 16) if by[i]['line'] in [55, 70, 85]])
ck('le nove unita singole sono quelle dichiarate',
   [u['line'] for u in cov if collections.Counter(x['context'] for x in cov)[u['context']] == 1] == SINGOLE,
   [u['line'] for u in cov if collections.Counter(x['context'] for x in cov)[u['context']] == 1])
ck('VIRGOLETTE, SEGNAPOSTO, ALTERNATIVE: tutti zero (asserzioni vuote)',
   sum(u['english'].count(QUOTE) for u in cov) == 0 == sum(u['italian'].count(QUOTE) for u in cov)
   and sum(len(TAG.findall(u['italian'])) for u in cov) == 0
   and sum(len(ALT.findall(u['italian'])) for u in cov) == 0)
ck('APICI: uno in inglese (unit 1), nove in italiano',
   sum(u['english'].count(APOS) for u in cov) == 1 and sum(u['italian'].count(APOS) for u in cov) == 9,
   (sum(u['english'].count(APOS) for u in cov), sum(u['italian'].count(APOS) for u in cov)))
ck('nomi di fazione e dei moduli INVARIATI; `Coalition` reso «Coalizione»',
   all(n in ''.join(u['italian'] for u in cov) for n in NAMES)
   and 'Coalition' not in ''.join(u['italian'] for u in cov),
   [n for n in NAMES if n not in ''.join(u['italian'] for u in cov)])
ck('citazione interna: l unita 14 nomina il modulo dell unita 13 (`outfit:Large Shield Module`)',
   by[13]['context'] == 'outfit:Large Shield Module'
   and 'Large Shield Module' in by[14]['italian']
   and 'Large Shield Module' not in by[13]['italian'])
ck('REGISTRO: nessuna seconda persona in tutto il lotto',
   not [u['idx'] for u in cov if re.search(r'\b(tu|tuo|tua|tuoi|tue|ti|te)\b', u['italian'])],
   [u['idx'] for u in cov if re.search(r'\b(tu|tuo|tua|tuoi|tue|ti|te)\b', u['italian'])])
ck('lessico del corpus: marina mercantile, pannelli solari, torri della fame, cella a combustibile',
   'marina mercantile' in by[1]['italian'] and 'pannelli solari' in by[11]['italian']
   and 'torri della fame' in by[7]['italian'] and 'cella a combustibile' in by[8]['italian'])
ck('impianto tecnico: generatori di scudi, emettitori, corazzatura, moduli di riparazione',
   'generatori di scudi' in by[13]['italian'] and 'emettitori' in by[14]['italian']
   and 'corazzatura' in by[15]['italian'] and 'moduli di riparazione' in by[15]['italian'])
ck('nessun caporale, nessun carattere tipografico',
   not [u['idx'] for u in cov for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026' if c in u['italian']])
nonlat = [(u['idx'], c) for u in cov for c in u['italian'] if ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in cov if u['italian'].rstrip(TAB) != u['italian'].rstrip(TAB).rstrip() or '  ' in u['italian']],
   [u['idx'] for u in cov if '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90 (0,996-1,35)',
   all(0.55 < u['ratio'] < 1.90 for u in cov),
   [(u['idx'], u['ratio']) for u in cov if not 0.55 < u['ratio'] < 1.90])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("ZERO unita' prima della 26: il lotto APRE il file",
   db.execute('select count(*) from units where path=? and line<26', (PATH,)).fetchone()[0] == 0)
ck("34 unita' dopo la 187, la prima apre `Large Repair Module` alla 202",
   db.execute('select count(*) from units where path=? and line>187', (PATH,)).fetchone()[0] == 34
   and db.execute('select line,context from units where path=? and line>187 order by line limit 1', (PATH,)).fetchone()
   == (202, 'outfit:Large Repair Module'))
ck('il file ha 49 unita, righe 26-533',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (49, 26, 533))
ck('tutte le 15 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · 12 contesti · 3 coppie con tab · file 15/49' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
