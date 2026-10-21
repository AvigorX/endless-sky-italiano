r"""check.py — L304 (`data/quarg/quarg outfits.txt`, righe 37-137). **PRIMO lotto del file**.

Undici schede di equipaggiamento Quarg in **sei contesti**: **cinque coppie** (seconda unita' con `\t`) e la **prima meta'**
della sesta (`Large Graviton Steering`, 137, che si chiude alla 138 fuori dal lotto).

Il test verifica:

1. **la ripetizione QUATTRO volte identica** del secondo paragrafo (55, 78, 96, 120): «Hanno anche strane capacita' che sembrano
   violare le leggi della fisica…». La resa deve essere **una sola**, e il test la confronta con `set()`;
2. **la VARIANTE della riga 38**: dice `These engines` e `Ships equipped with them` invece di `They` / `Ships with these
   engines`, e va **conservata diversa** — non uniformata alle altre quattro;
3. **il confine alla 137**: e' la **prima** unita' della coppia `Large Graviton Steering`, che si chiude alla **138**, fuori dal
   segmento.
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
PATH = 'data/quarg/quarg outfits.txt'
COPPIE = [(37, 38), (54, 55), (77, 78), (95, 96), (119, 120)]
TABBED = [38, 55, 78, 96, 120]
QUATTRO = [4, 6, 8, 10]
NAMES = ['Quarg', 'umanità']
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
ck('unita tradotte 11/11', len(cov) == 11 == len(units), '%d/%d' % (len(cov), len(units)))
ck('tutte DESCRIPTION, sei contesti: cinque doppi + una prima meta',
   {u['kind'] for u in cov} == {'DESCRIPTION'} and len(grp) == 6 and sorted(grp.values()) == [1, 2, 2, 2, 2, 2], dict(grp))
ck('le cinque coppie sono quelle dichiarate, con tab sulla seconda',
   all(at[b]['context'] == at[a]['context'] and at[b]['english'].startswith(TAB) and b - a <= 1 for a, b in COPPIE))
ck('la sesta coppia e `Large Graviton Steering`: la 137 e la PRIMA meta',
   at[137]['context'] == 'outfit:Large Graviton Steering' and not at[137]['english'].startswith(TAB))
ck('TAB: esattamente cinque unita la portano, alle righe dichiarate',
   sorted(u['line'] for u in cov if u['english'].startswith(TAB)) == TABBED
   and all(at[l]['italian'].startswith(TAB) for l in TABBED)
   and sum(u['italian'].count(TAB) for u in cov) == 5)
ck('RIPETIZIONE: le quattro unita 4, 6, 8, 10 identiche in inglese E in italiano',
   len({by[i]['english'] for i in QUATTRO}) == 1 and len({by[i]['italian'] for i in QUATTRO}) == 1,
   len({by[i]['italian'] for i in QUATTRO}))
ck('VARIANTE 38: diversa dalle quattro E costruita con `These engines` / `Ships equipped with them`',
   by[2]['italian'] != by[4]['italian']
   and 'Questi motori' in by[2]['italian'] and 'ne sono dotate' in by[2]['italian']
   and 'Questi motori' not in by[4]['italian'])
ck('tutte e 11 le unita sono TRADOTTE, nessuna copiata',
   all(u['italian'] != u['english'] for u in cov), [u['idx'] for u in cov if u['italian'] == u['english']])
ck('VIRGOLETTE, SEGNAPOSTO, ALTERNATIVE: tutti zero (asserzioni vuote)',
   sum(u['english'].count(QUOTE) for u in cov) == 0 == sum(u['italian'].count(QUOTE) for u in cov)
   and sum(len(TAG.findall(u['italian'])) for u in cov) == 0
   and sum(len(ALT.findall(u['italian'])) for u in cov) == 0)
ck('APICI: uno in inglese (riga 54, `ship\'s`), undici in italiano',
   sum(u['english'].count(APOS) for u in cov) == 1 and sum(u['italian'].count(APOS) for u in cov) == 11,
   (sum(u['english'].count(APOS) for u in cov), sum(u['italian'].count(APOS) for u in cov)))
ck('nomi e lessico: `Quarg` invariato, «umanità» reso',
   'Quarg' in ''.join(u['italian'] for u in cov) and 'umanità' in by[2]['italian'])
ck('terminologia: propulsori, motori di governo, centro di massa, giroscopio, onde gravitazionali',
   'propulsori Quarg' in by[1]['italian'] and 'motori di governo' in by[3]['italian']
   and 'centro di massa' in by[3]['italian'] and 'giroscopio' in by[7]['italian']
   and 'onde gravitazionali' in by[5]['italian'])
ck('REGISTRO: nessuna seconda persona',
   not [u['idx'] for u in cov if re.search(r'\b(tu|tuo|tua|tuoi|tue|ti|te)\b', u['italian'])],
   [u['idx'] for u in cov if re.search(r'\b(tu|tuo|tua|tuoi|tue|ti|te)\b', u['italian'])])
ck('nessun caporale, nessun carattere tipografico',
   not [u['idx'] for u in cov for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026' if c in u['italian']])
nonlat = [(u['idx'], c) for u in cov for c in u['italian'] if ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessun doppio spazio (la tab iniziale non conta)',
   not [u['idx'] for u in cov if '  ' in u['italian'].lstrip(TAB)])
ck('rapporto nel gate 0,55-1,90 (0,99-1,16)',
   all(0.55 < u['ratio'] < 1.90 for u in cov),
   [(u['idx'], u['ratio']) for u in cov if not 0.55 < u['ratio'] < 1.90])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("ZERO unita' prima della 37: il lotto APRE il file",
   db.execute('select count(*) from units where path=? and line<37', (PATH,)).fetchone()[0] == 0)
ck("20 unita' dopo la 137; la prima e la SECONDA meta di `Large Graviton Steering` alla 138",
   db.execute('select count(*) from units where path=? and line>137', (PATH,)).fetchone()[0] == 20
   and db.execute('select line,context from units where path=? and line>137 order by line limit 1', (PATH,)).fetchone()
   == (138, 'outfit:Large Graviton Steering'))
ck('il file ha 31 unita, righe 37-579, tutte DESCRIPTION',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (31, 37, 579)
   and dict(db.execute('select kind,count(*) from units where path=? group by kind', (PATH,)).fetchall())
   == {'DESCRIPTION': 31})
ck('tutte le 11 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · 6 contesti · 4 identiche + 1 variante · 5 tab · file 11/31' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
