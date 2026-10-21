r"""check.py — L261 (`data/remnant/remnant jobs.txt`, righe 19-209). Primo lotto del file: **lavori dei Remnant**.

**Lotto misto**: 7 `VALUE` (i nomi dei lavori) si **copiano** — l'asserzione è l'**identita' per indice**, non la
«prosa tradotta»; 7 `DESCRIPTION` e 11 `DIALOG` si **traducono**.

**Sette contesti** in 25 unita': `Remnant: Bounty`, `… Bounty 2`, `Broken Jump Drive job`, `Expanded Horizons Astral job`,
`… late`, `… Bounty 3`, `… Bounty 4`. Il controllo verifica la **sequenza** dei blocchi, non solo il numero di contesti.

**29 segnaposto** in 6 famiglie: `<payment>` 10, `<planet>` 8, `<waypoints>` 4, `<npc>` 3, **`<npc model>` 2** (simbolo
distinto da `<npc>`), `<destination>` 2. Confrontati per famiglia **e per ordine dentro ogni unita'**.

**Gruppi di stringhe identiche** (una sola resa per inglese): `3/7/22`, `8/23`, `13/17`, `14/18`, `15/19`, `12/16`.
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
PATH = 'data/remnant/remnant jobs.txt'
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
CTXS = ['mission:Remnant: Bounty', 'mission:Remnant: Bounty 2', 'mission:Remnant: Broken Jump Drive job',
        'mission:Remnant: Expanded Horizons Astral job', 'mission:Remnant: Expanded Horizons Astral job late',
        'mission:Remnant: Bounty 3', 'mission:Remnant: Bounty 4']
BLOCCHI = [(1, 4), (5, 8), (9, 11), (12, 15), (16, 19), (20, 23), (24, 25)]
GRUPPI = [[3, 7, 22], [8, 23], [12, 16], [13, 17], [14, 18], [15, 19]]
TOK = {'<payment>': 10, '<planet>': 8, '<waypoints>': 4, '<npc>': 3, '<npc model>': 2, '<destination>': 2}
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck('unita tradotte 25/25', len(cov) == 25 == len(units), '%d/%d' % (len(cov), len(units)))
ck('tipi: 11 DIALOG + 7 DESCRIPTION + 7 VALUE',
   collections.Counter(u['kind'] for u in units) == {'DIALOG': 11, 'DESCRIPTION': 7, 'VALUE': 7},
   dict(collections.Counter(u['kind'] for u in units)))
ck('SETTE contesti, nella sequenza misurata (Bounty, 2, Jump Drive, Astral, late, 3, 4)',
   [(a, b, by[a]['context']) for a, b in BLOCCHI] == [(a, b, c) for (a, b), c in zip(BLOCCHI, CTXS)]
   and len(set(u['context'] for u in cov)) == 7,
   [(a, b, by[a]['context']) for a, b in BLOCCHI])
ck('righe 19-209, nessun buco interno',
   [u['line'] for u in cov] == sorted({u['line'] for u in cov})
   and cov[0]['line'] == 19 and cov[-1]['line'] == 209)
ck('i 7 VALUE sono COPIATI, identici per indice (sono dati, non prosa)',
   [u['idx'] for u in cov if u['kind'] == 'VALUE'] == [1, 5, 9, 12, 16, 20, 24]
   and all(u['italian'] == u['english'] for u in cov if u['kind'] == 'VALUE'))
ck('i 18 DESCRIPTION+DIALOG sono TRADOTTI, nessuno copiato',
   all(u['italian'] != u['english'] for u in cov if u['kind'] != 'VALUE'),
   [u['idx'] for u in cov if u['kind'] != 'VALUE' and u['italian'] == u['english']])
ck('ZERO tab e ZERO virgolette in entrambe le lingue (asserzioni negative)',
   sum(u['english'].count(TAB) + u['italian'].count(TAB) for u in cov) == 0
   and sum(u['english'].count(QUOTE) + u['italian'].count(QUOTE) for u in cov) == 0)
ck('APICI: 2 in inglese (20, 24: il nome `Rano\'erek`), 4 in italiano (15, 19, 20, 24)',
   {u['idx']: u['english'].count(APOS) for u in cov if APOS in u['english']} == {20: 1, 24: 1}
   and {u['idx']: u['italian'].count(APOS) for u in cov if APOS in u['italian']} == {15: 1, 19: 1, 20: 1, 24: 1},
   ({u['idx']: u['english'].count(APOS) for u in cov if APOS in u['english']},
    {u['idx']: u['italian'].count(APOS) for u in cov if APOS in u['italian']}))
ck('SEGNAPOSTO: 29 in 6 famiglie, e ORDINE identico per unita',
   collections.Counter(t for u in cov for t in TAG.findall(u['english'])) == TOK
   == collections.Counter(t for u in cov for t in TAG.findall(u['italian']))
   and not [u['idx'] for u in cov if TAG.findall(u['english']) != TAG.findall(u['italian'])],
   ([u['idx'] for u in cov if TAG.findall(u['english']) != TAG.findall(u['italian'])],
    dict(collections.Counter(t for u in cov for t in TAG.findall(u['italian'])))))
ck('`<npc model>` e `<npc>` sono famiglie DISTINTE (2 e 3), non lo stesso simbolo',
   collections.Counter(t for u in cov for t in TAG.findall(u['english']))['<npc model>'] == 2
   and collections.Counter(t for u in cov for t in TAG.findall(u['english']))['<npc>'] == 3)
ck('i gruppi di stringhe identiche hanno UNA sola resa',
   all(len({by[i]['italian'] for i in g}) == 1 for g in GRUPPI)
   and all(len({by[i]['english'] for i in g}) == 1 for g in GRUPPI),
   [(g, len({by[i]['italian'] for i in g})) for g in GRUPPI])
ck('le due spedizioni (13/17 e 15/19) sono identiche anche fra loro, come in inglese',
   by[13]['italian'] == by[17]['italian'] and by[15]['italian'] == by[19]['italian']
   and by[12]['italian'] == by[16]['italian'])
ck('lessico: Laboratorio di Ricerca, cristalli di dati, motore di salto, indennità logistica',
   'Laboratorio di Ricerca' in by[13]['italian'] and 'cristalli di dati' in by[15]['italian']
   and 'motore di salto' in by[10]['italian'] and 'indennità logistica' in by[15]['italian'])
ck('fazioni e nomi: Remnant e Korath invariati, nessun «Remnants»',
   'Remnant' in by[2]['italian'] and 'Korath' in by[2]['italian']
   and 'Remnants' not in ' '.join(u['italian'] for u in cov))
ck('nessun caporale, nessun carattere tipografico',
   not [u['idx'] for u in cov for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026' if c in u['italian']])
nonlat = [(u['idx'], c) for u in cov for c in u['italian'] if ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']],
   [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90 (0,90-1,26)',
   all(0.55 < u['ratio'] < 1.90 for u in cov),
   [(u['idx'], u['ratio']) for u in cov if not 0.55 < u['ratio'] < 1.90])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("ZERO unita' prima della 19: il lotto APRE il file",
   db.execute('select count(*) from units where path=? and line<19', (PATH,)).fetchone()[0] == 0)
ck("62 unita' dopo la 209",
   db.execute('select count(*) from units where path=? and line>209', (PATH,)).fetchone()[0] == 62)
ck('il file ha 87 unita, righe 19-741',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (87, 19, 741))
st = dict(db.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('tutte le 25 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · 7 contesti · 29 segnaposto' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
