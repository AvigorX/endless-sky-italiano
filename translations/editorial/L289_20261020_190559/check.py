r"""check.py — L289 (`data/gegno/gegno ships.txt`, righe 1193-1616). **LOTTO TERMINALE del file**.

Dodici descrizioni, **otto contesti**, **quattro coppie consecutive** e **cinque tab**. Il lotto chiude il file: verifica
l'**invariante di FILE** e due cose che nessun altro lotto di questa serie aveva:

1. **l'unita' 2 e un'istruzione di gioco in seconda persona** (`You cannot carry a fighter unless…`): e' l'**unica** unita' con
   «tu», e va dichiarata — il registro tecnico delle altre undici resta impersonale;
2. **il `Halite` continua la scheda di L288** (riga 1192): la riga 1193 non riapre la descrizione.
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
ALT = re.compile(r'\[[^\]]*\]')
HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
PATH = 'data/gegno/gegno ships.txt'
NAMES = ['Halite', 'Mica', 'Coesite', 'Tridymite', 'Felsic', 'Feldspar', 'Epidote', 'Kyanite', 'Gegno', 'Scin', 'Vi',
         'Shale', 'Slate', 'Schist']
PAIRS = [(1, 2), (7, 8), (9, 10), (11, 12)]
TABBED = [1, 2, 8, 10, 12]  # righe 1193, 1194, 1481, 1548, 1616
HINT = 2  # unica unita' in seconda persona: istruzione di gioco
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


ck('unita tradotte 12/12', len(cov) == 12 == len(units), '%d/%d' % (len(cov), len(units)))
ck('tutte DESCRIPTION, otto contesti con le righe dichiarate',
   {u['kind'] for u in cov} == {'DESCRIPTION'}
   and [(u['context'], u['line']) for u in cov]
   == [('ship:Halite', 1193), ('ship:Halite', 1194), ('ship:Mica', 1234), ('ship:Coesite', 1288),
       ('ship:Tridymite', 1342), ('ship:Felsic', 1395), ('ship:Feldspar', 1480), ('ship:Feldspar', 1481),
       ('ship:Epidote', 1547), ('ship:Epidote', 1548), ('ship:Kyanite', 1615), ('ship:Kyanite', 1616)],
   [(u['context'], u['line']) for u in cov])
ck('tutte e 12 le unita sono TRADOTTE, nessuna copiata',
   all(u['italian'] != u['english'] for u in cov), [u['idx'] for u in cov if u['italian'] == u['english']])
ck('QUATTRO coppie consecutive, ognuna nello stesso contesto',
   all(by[b]['line'] == by[a]['line'] + 1 and by[a]['context'] == by[b]['context'] for a, b in PAIRS),
   [(a, b) for a, b in PAIRS if by[b]['line'] != by[a]['line'] + 1 or by[a]['context'] != by[b]['context']])
ck('le seconde meta CONTINUANO (nessuna riapre con il soggetto)',
   by[2]['italian'].lstrip(TAB).startswith('I velivoli')
   and by[8]['italian'].lstrip(TAB).startswith('Capaci')
   and by[10]['italian'].lstrip(TAB).startswith('Come le altre navi')
   and by[12]['italian'].lstrip(TAB).startswith('Il sistema di scanner'),
   [by[i]['italian'][:30] for i in (2, 8, 10, 12)])
ck('il Halite CONTINUA la scheda di L288 (riga 1192) senza riaprirla',
   by[1]['italian'].lstrip(TAB).startswith('Capaci')
   and not by[1]['italian'].lstrip(TAB).startswith('Gli Halite'),
   by[1]['italian'][:50])
prev = sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L288_*', 'translation.json')))
p1192 = [u for u in json.load(open(prev[-1], encoding='utf-8'))['units']
         if u['path'] == PATH and u['line'] == 1192] if prev else []
ck('L288 ha la riga 1192 del Halite e la chiude con «nuovi sviluppi.»',
   len(p1192) == 1 and p1192[0]['context'] == 'ship:Halite' and p1192[0]['italian'].endswith('nuovi sviluppi.'),
   p1192[0]['italian'][-40:] if p1192 else 'L288 assente')
ck('TAB: cinque, sulle unita 1, 2, 8, 10, 12, come PRIMO carattere',
   sum(u['english'].count(TAB) for u in cov) == 5 == sum(u['italian'].count(TAB) for u in cov)
   and [u['idx'] for u in cov if TAB in u['english']] == TABBED == [u['idx'] for u in cov if TAB in u['italian']]
   and all(by[i]['italian'].startswith(TAB) for i in TABBED))
ck('VIRGOLETTE, SEGNAPOSTO, ALTERNATIVE: tutti zero in entrambe le lingue',
   sum(u['english'].count(QUOTE) for u in cov) == 0 == sum(u['italian'].count(QUOTE) for u in cov)
   and sum(len(TAG.findall(u['english'])) for u in cov) == 0 == sum(len(TAG.findall(u['italian'])) for u in cov)
   and sum(len(ALT.findall(u['english'])) for u in cov) == 0 == sum(len(ALT.findall(u['italian'])) for u in cov))
ck('APICI: quattro in inglese, cinque in italiano',
   sum(u['english'].count(APOS) for u in cov) == 4 and sum(u['italian'].count(APOS) for u in cov) == 5,
   (sum(u['english'].count(APOS) for u in cov), sum(u['italian'].count(APOS) for u in cov)))
ck('REGISTRO: solo l unita 2 (istruzione di gioco) usa la seconda persona',
   [u['idx'] for u in cov if re.search(r'\b(tu|tuo|tua|tuoi|tue|ti|te|puoi)\b', u['italian'])] == [HINT]
   and 'Non puoi trasportare' in by[HINT]['italian'],
   [u['idx'] for u in cov if re.search(r'\b(tu|tuo|tua|tuoi|tue|ti|te|puoi)\b', u['italian'])])
ck('l istruzione di gioco usa «baia di caccia» (forma maggioritaria del corpus)',
   'baia di caccia' in by[HINT]['italian'] and 'baia per caccia' not in by[HINT]['italian'])
ck('nomi di modello e di fazione INVARIATI',
   all(n in ''.join(u['italian'] for u in cov) for n in NAMES),
   [n for n in NAMES if n not in ''.join(u['italian'] for u in cov)])
ck('nessun plurale inglese riprodotto: niente `Halites`, `Coesites`, `Kyanites`, `Feldspars`',
   not [p for p in ('Halites', 'Coesites', 'Kyanites', 'Feldspars', 'Epidotes', 'Tridymites', 'Felsics', 'Micas')
        if p in ''.join(u['italian'] for u in cov)],
   [p for p in ('Halites', 'Coesites', 'Kyanites', 'Feldspars', 'Epidotes', 'Tridymites', 'Felsics', 'Micas')
    if p in ''.join(u['italian'] for u in cov)])
ck('lessico: portaerei, torretta, scanner, banco di prova, stiva, scafo',
   'portaerei' in by[1]['italian'] and 'torrette' in by[4]['italian'] and 'scanner' in by[5]['italian']
   and 'banco di prova' in by[7]['italian'] and 'stive' in by[9]['italian'] and 'scafo' in by[11]['italian'])
ck('nessun caporale, nessun carattere tipografico',
   not [u['idx'] for u in cov for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026' if c in u['italian']])
nonlat = [(u['idx'], c) for u in cov for c in u['italian'] if ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']],
   [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90 (1,06-1,27)',
   all(0.55 < u['ratio'] < 1.90 for u in cov),
   [(u['idx'], u['ratio']) for u in cov if not 0.55 < u['ratio'] < 1.90])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck('FILE: 25 unita prima della 1193 (7 + 9 + 9)',
   db.execute('select count(*) from units where path=? and line<1193', (PATH,)).fetchone()[0] == 25)
ck('FILE: ZERO unita dopo la 1616 — il lotto CHIUDE il file',
   db.execute('select count(*) from units where path=? and line>1616', (PATH,)).fetchone()[0] == 0)
ck('FILE: 37 unita, righe 53-1616, 36 DESCRIPTION + 1 VALUE',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (37, 53, 1616)
   and dict(db.execute('select kind,count(*) from units where path=? group by kind', (PATH,)).fetchall())
   == {'DESCRIPTION': 36, 'VALUE': 1})
ck('FILE: i quattro lotti sommano 37 (7 + 9 + 9 + 12)',
   7 + 9 + 9 + 12 == 37
   and db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0] == 37)
ck('tutte le 12 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · 8 contesti · 4 coppie · 5 tab · FILE 37/37' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
