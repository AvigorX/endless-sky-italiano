r"""check.py — L241 (`data/successors/successor jobs.txt`, 86 unita', righe 16-280). Primo lotto del file.

**Il lotto della COMPOSIZIONE**: 76 `TEXT` di cui **66 sono frammenti** che il gioco concatena (`Phrase::Get()` fa
`result += …` senza separatore), 5 `VALUE` (dati, invariati) e 5 `DESCRIPTION` (prosa). Le frasi intere non sono scritte da
nessuna parte: esistono solo quando il motore sceglie un'opzione per ogni gruppo.

Quattro blocchi di frammenti, con i gruppi misurati sul sorgente:

    successor data               8-20    1x · 3x · 4x · 1x · 2x · 2x        =   48 frasi
    high houses delivery        21-34    1x · 4x · 2x · 2x · 1x · 3x · 1x  =   48 frasi
    predecessor researchers out 35-56    1x · 3x · 1x · 4x · 2x · 9x · 3x  =  648 frasi
    successor researchers out   57-74    1x · 3x · 1x · 4x · 2x · 5x · 3x  =  360 frasi

**Il quarto gruppo dei due blocchi «researchers» ha un'opzione VUOTA nel sorgente** (``): l'inventario ne conserva tre,
perche' la stringa vuota non e' un'unita'. La lacuna e' dichiarata, non riparabile da un lotto.

**Quattro frammenti hanno uno spazio in meno dell'inglese** (43, 44, 65, 66: `begin `/`start ` -> «iniziano a»/
«prendono a»). Non e' una svista: l'oggetto che segue comincia **con uno spazio** (` catalogare …`), e l'inglese produce
«begin  cataloging» con **due** spazi. In italiano il verbo non porta lo spazio finale, e la frase composta ne ha **uno
solo**. La cosa si verifica componendo, non guardando le singole unita'.
"""
import collections
import itertools
import json
import os
import re
import sqlite3

TAB = chr(9)
QUOTE = chr(34)
TAG = re.compile(r'<[^<>]+>')
HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
PATH = 'data/successors/successor jobs.txt'
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
by = {v['idx']: v for v in cov}
VAL = [v for v in cov if v['kind'] == 'VALUE']
PROSA = [v for v in cov if v['kind'] != 'VALUE']
TOK_EN = collections.Counter(t for v in cov for t in TAG.findall(v['english']))
TOK_IT = collections.Counter(t for v in cov for t in TAG.findall(v['italian']))

# struttura dei gruppi, misurata sul sorgente (l'opzione vuota e' indicata con None)
BLOCCHI = {
 'successor data': [[8], [9, 10, 11], [12, 13, 14, 15], [16], [17, 18], [19, 20]],
 'high houses delivery': [[21], [22, 23, 24, 25], [26, 27], [28, 29], [30], [31, 32, 33], [34]],
 'predecessor researchers out': [[35], [36, 37, 38], [39], [40, 41, 42, None], [43, 44],
                                 [45, 46, 47, 48, 49, 50, 51, 52, 53], [54, 55, 56]],
 'successor researchers out': [[57], [58, 59, 60], [61], [62, 63, 64, None], [65, 66],
                               [67, 68, 69, 70, 71], [72, 73, 74]],
}
CAMPIONE = {'<payment>': '1.000 crediti', '<commodity>': 'ferro', '<planet stopovers>': 'Korell e Vail',
            '<stopovers>': 'Korell', '<planet>': 'Korell', '<destination>': 'Korell', '<date>': '12 marzo',
            '<bunks>': '4'}


def resa(txt):
    for k, v in CAMPIONE.items():
        txt = txt.replace(k, v)
    return txt


def frasi(blocco, chiave):
    """Compone tutte le combinazioni; per l'opzione vuota il frammento e' la stringa vuota."""
    campi = []
    for gruppo in BLOCCHI[blocco]:
        opzioni = []
        for i in gruppo:
            opzioni.append('' if i is None else by[i][chiave])
        campi.append(opzioni)
    return [''.join(c) for c in itertools.product(*campi)]


rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 86/86", len(cov) == 86 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna unita\' vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 76 TEXT + 5 VALUE + 5 DESCRIPTION',
   collections.Counter(u['kind'] for u in units) == {'TEXT': 76, 'VALUE': 5, 'DESCRIPTION': 5},
   dict(collections.Counter(u['kind'] for u in units)))
ck('18 contesti', len({u['context'] for u in units}) == 18, len({u['context'] for u in units}))
ck('righe 16 e 280 (prima e ultima del lotto)',
   (cov[0]['line'], cov[-1]['line']) == (16, 280), (cov[0]['line'], cov[-1]['line']))
ck('ZERO tab e ZERO virgolette in inglese e in italiano (due asserzioni negative scritte)',
   sum(v['english'].count(TAB) for v in cov) == 0 == sum(v['italian'].count(TAB) for v in cov)
   and sum(v['english'].count(QUOTE) for v in cov) == 0 == sum(v['italian'].count(QUOTE) for v in cov))
ck("i 5 VALUE sono IDENTICI all'inglese, per indice",
   all(v['italian'] == v['english'] for v in VAL) and len(VAL) == 5,
   [v['idx'] for v in VAL if v['italian'] != v['english']])
ck('le 81 TEXT+DESCRIPTION sono TUTTE tradotte (0 identiche)',
   all(v['italian'] != v['english'] for v in PROSA) and len(PROSA) == 81,
   [v['idx'] for v in PROSA if v['italian'] == v['english']])
ck("segnaposto: 45 su 8 famiglie, parita' per simbolo",
   TOK_EN == TOK_IT == {'<payment>': 15, '<planet>': 7, '<bunks>': 5, '<destination>': 5,
                        '<date>': 5, '<planet stopovers>': 3, '<stopovers>': 3, '<commodity>': 2},
   (dict(TOK_EN), dict(TOK_IT)))
ck("`<planet stopovers>` e' un simbolo INTERO, distinto da `<stopovers>`: 3 + 3, non 6",
   TOK_IT['<planet stopovers>'] == 3 and TOK_IT['<stopovers>'] == 3
   and TOK_IT['<planet stopovers>'] + TOK_IT['<stopovers>'] == 6)
ck("segnaposto: ordine identico in ogni unita'",
   all(tuple(TAG.findall(v['english'])) == tuple(TAG.findall(v['italian'])) for v in cov),
   [(v['idx'], TAG.findall(v['english']), TAG.findall(v['italian'])) for v in cov
    if TAG.findall(v['english']) != TAG.findall(v['italian'])])
ck('stesso inglese => stessa resa, nei 21 gruppi di duplicati',
   all(len({v['italian'] for v in cov if v['english'] == k}) == 1
       for k, n in collections.Counter(v['english'] for v in cov).items() if n > 1)
   and len([1 for k, n in collections.Counter(v['english'] for v in cov).items() if n > 1]) == 21)
ck('spazi: 82 unita\' hanno gli stessi spazi dell\'inglese',
   [v['idx'] for v in cov if (len(v['english']) - len(v['english'].strip(' ')))
    != (len(v['italian']) - len(v['italian'].strip(' ')))] == [43, 44, 65, 66],
   [v['idx'] for v in cov if (len(v['english']) - len(v['english'].strip(' ')))
    != (len(v['italian']) - len(v['italian'].strip(' ')))])
ck('i 4 frammenti con uno spazio in meno sono i verbi: inglese con spazio finale, italiano senza',
   all(by[i]['english'].endswith(' ') and not by[i]['italian'].endswith(' ') for i in (43, 44, 65, 66)))
ck('...e l\'oggetto che li segue comincia con uno spazio (uno solo, non due)',
   all(by[i]['italian'].startswith(' ') for i in list(range(45, 54)) + list(range(67, 72))))
# --- composizione: 48 + 48 + 648 + 360 = 1104 frasi per lingua ---
tot = {k: 0 for k in ('en', 'it')}
difetti = []
for blocco in BLOCCHI:
    for chiave in ('english', 'italian'):
        for s in frasi(blocco, chiave):
            tot['en' if chiave == 'english' else 'it'] += 1
            if chiave != 'italian':
                continue
            t = resa(s)
            if '  ' in t:
                difetti.append(('doppio spazio', blocco, t[:70]))
            elif re.search(r'\s[.,;:!]', t):
                difetti.append(('spazio prima della punteggiatura', blocco, t[-70:]))
            elif not t[:1].isupper():
                difetti.append(('iniziale minuscola', blocco, t[:70]))
            elif not t.endswith('.'):
                difetti.append(('non finisce con un punto', blocco, t[-70:]))
            elif '<' in t:
                difetti.append(('segnaposto non risolto', blocco, t[-70:]))
ck('composizione: 1104 frasi in inglese e 1104 in italiano (stessa struttura di gruppi)',
   tot == {'en': 1104, 'it': 1104}, tot)
ck('composizione: nessuna delle 1104 frasi italiane ha doppi spazi, spazi prima della punteggiatura, '
   'iniziale minuscola, punto mancante o segnaposto irrisolto', not difetti, difetti[:3])
NOMI = {'ricercatori', 'scienziati', 'studiosi', 'sperimentatori', 'carico', 'lotto',
        'pagamento', 'banche', 'dati', 'partita'}
AMMESSI = {('i', 'ricercatori'), ('gli', 'scienziati'), ('gli', 'studiosi'), ('gli', 'sperimentatori'),
           ('il', 'carico'), ('il', 'lotto'), ('il', 'pagamento'), ('le', 'banche'), ('i', 'dati')}
accoppi = []
for blocco in BLOCCHI:
    for s_ in frasi(blocco, 'italian'):
        for m in re.finditer(r'\b(il|lo|la|i|gli|le)\s+(?:tuo\s+|tua\s+)?(\w+)', resa(s_)):
            if m.group(2) in NOMI and (m.group(1), m.group(2)) not in AMMESSI:
                accoppi.append((m.group(0), blocco))
ck("accordo articolo+nome: «il tuo partita» e «i scienziati» sarebbero qui, e non ci sono",
   not accoppi, accoppi[:3])
ck('composizione: la frase da 6 copie dei materiali tiene insieme i cinque gruppi',
   resa(''.join([by[35]['italian'], by[36]['italian'], by[39]['italian'], by[40]['italian'],
                 by[44]['italian'], by[45]['italian'], by[54]['italian']]))
   == 'Tu consegni i ricercatori a Korell e Vail, dove subito prendono a catalogare alcune formazioni rocciose vicine. '
      'Dopo qualche ora, sono pronti a tornare a casa.',
   resa(''.join([by[35]['italian'], by[36]['italian'], by[39]['italian'], by[40]['italian'],
                 by[44]['italian'], by[45]['italian'], by[54]['italian']])))
ck('composizione: con l\'opzione vuota del quarto gruppo la frase resta corretta',
   resa(''.join([by[35]['italian'], by[36]['italian'], by[39]['italian'], '', by[43]['italian'],
                 by[45]['italian'], by[54]['italian']]))
   .startswith('Tu consegni i ricercatori a Korell e Vail, dove iniziano a catalogare'))
ck('il quarto gruppo dei due blocchi «researchers» ha 3 opzioni nell\'inventario e 4 nel sorgente',
   [len(g) for g in BLOCCHI['predecessor researchers out']][3] == 4
   and len([i for i in BLOCCHI['predecessor researchers out'][3] if i is not None]) == 3
   and len([i for i in BLOCCHI['successor researchers out'][3] if i is not None]) == 3)
rs = [v['ratio'] for v in cov]
ck('rapporto nel gate 0,55-1,90 (0,67-1,70; 428 -> 445 parole)',
   0.55 < min(rs) and max(rs) < 1.90, '%.2f - %.2f' % (min(rs), max(rs)))
ck('nessun caporale e nessun carattere tipografico',
   not [v['idx'] for v in cov if any(c in v['italian'] for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026')])
ACC = re.compile(r"\b(e|piu|perche|cosi|gia|puo|cioe|percio)'(?![a-z])", re.I)
bad = [(v['idx'], ACC.search(v['italian']).group(0)) for v in cov if ACC.search(v['italian'])]
ck("tipografia (accenti veri, nessun apostrofo al posto dell'accento)", not bad, bad)
nonlat = [v['idx'] for v in cov for c in v['italian'] if ord(c) > 127 and not 0x00C0 <= ord(c) <= 0x024F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessun doppio spazio dentro le singole unita\' (la composizione e\' controllata a parte)',
   not [v['idx'] for v in cov if '  ' in v['italian']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("ZERO unita' prima della riga 16: il lotto APRE il file",
   db.execute('select count(*) from units where path=? and line<16', (PATH,)).fetchone()[0] == 0)
ck("38 unita' dopo la 280 (124 - 86): il lotto NON chiude il file",
   db.execute('select count(*) from units where path=? and line>280', (PATH,)).fetchone()[0] == 38)
ck('confine misurato: riga 306, VALUE di mission:Successors: Students In',
   db.execute('select line,kind,context from units where path=? and line>280 order by line limit 1', (PATH,)).fetchone()
   == (306, 'VALUE', 'mission:Successors: Students In'),
   db.execute('select line,kind,context from units where path=? and line>280 order by line limit 1', (PATH,)).fetchone())
ck('il file intero: 124 unita, righe 16 - 802',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (124, 16, 802))
ck('86 + 38 = 124', 86 + 38 == 124)
st = dict(db.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('le 86 unita sono PENDING (misurato)',
   db.execute('select count(*) from units where id in (%s) and state != "PENDING"'
              % ','.join('?' * len(units)), [u['id'] for u in units]).fetchone()[0] == 0)
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d' % (sum(len(v['english'].split()) for v in cov),
                                sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
