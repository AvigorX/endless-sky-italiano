r"""check.py — L262 (`data/remnant/remnant jobs.txt`, righe 226-490). Secondo lotto del file.

**Il lotto piu' misto finora**: quattro tipi (9 `DIALOG`, 8 `VALUE`, 7 `DESCRIPTION`, **5 `MISSION_TEXT`**) e **nove
contesti**, verificati come coppie (prima unita', contesto) e non come numero.

Tre cose vanno asserite con cura:

1. **I 2 `DIALOG` iniziali ripetono stringhe gia' tradotte in L261** (`You have destroyed the Korath ship…`,
   `A Remnant military leader thanks you…`): il `check.py` rilegge il `translation.json` di L261 e pretende
   **l'identita' alla lettera**. E' l'unico controllo del lotto che dipende da un altro lotto, ed e' voluto: quella resa e'
   gia' stata approvata dal corpus.
2. **`Ember Waste` resta invariato** (13 occorrenze nel corpus non lo traducono): il controllo vieta qualunque resa italiana.
3. **`<cargo>` compare 8 volte e senza articolo davanti al segnaposto**, `<payment>` 13, `<planet>` 12, `<npc>` 8,
   `<destination>` 2: confronto per famiglia **e per ordine dentro ogni unita'**.
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
PREV = os.path.join(L10N, 'staging', 'editorial', 'L261_20261020_161448', 'translation.json')
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
BLOCCHI = [(1, 3), (4, 7), (8, 10), (11, 13), (14, 16), (17, 19), (20, 23), (24, 28), (29, 29)]
CTXS = ['mission:Remnant: Bounty 4', 'mission:Remnant: Bounty 5',
        'mission:Remnant: Logistics Civil Engineering', 'mission:Remnant: Logistics Industrial Delivery',
        'mission:Remnant: Logistics Outfitter Delivery', 'mission:Remnant: Logistics Salvage Delivery',
        'mission:Remnant: Rescue', 'mission:Remnant: Rescue 1B', 'mission:Remnant: Rescue 2']
TOK = {'<payment>': 13, '<planet>': 12, '<npc>': 8, '<cargo>': 8, '<destination>': 2}
GRUPPI = [[21, 25], [23, 28], [20, 24]]
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck('unita tradotte 29/29', len(cov) == 29 == len(units), '%d/%d' % (len(cov), len(units)))
ck('QUATTRO tipi: 9 DIALOG + 8 VALUE + 7 DESCRIPTION + 5 MISSION_TEXT',
   collections.Counter(u['kind'] for u in units)
   == {'DIALOG': 9, 'VALUE': 8, 'DESCRIPTION': 7, 'MISSION_TEXT': 5},
   dict(collections.Counter(u['kind'] for u in units)))
ck('NOVE contesti: primo e ultimo di ogni blocco come misurato',
   [(a, b, by[a]['context']) for a, b in BLOCCHI] == [(a, b, c) for (a, b), c in zip(BLOCCHI, CTXS)]
   and len(set(u['context'] for u in cov)) == 9,
   [(a, b, by[a]['context']) for a, b in BLOCCHI])
ck('righe 226-490, nessun buco interno',
   [u['line'] for u in cov] == sorted({u['line'] for u in cov})
   and cov[0]['line'] == 226 and cov[-1]['line'] == 490)
ck('gli 8 VALUE sono COPIATI, identici per indice',
   [u['idx'] for u in cov if u['kind'] == 'VALUE'] == [3, 8, 11, 14, 17, 20, 24, 29]
   and all(u['italian'] == u['english'] for u in cov if u['kind'] == 'VALUE'))
ck('le altre 21 unita sono TRADOTTE, nessuna copiata',
   all(u['italian'] != u['english'] for u in cov if u['kind'] != 'VALUE'),
   [u['idx'] for u in cov if u['kind'] != 'VALUE' and u['italian'] == u['english']])
ck("le unita 1 e 2 riprendono ALLA LETTERA le rese gia' approvate in L261",
   all(by[k]['italian'] == {u['english']: u['italian'] for u in
                            json.load(open(PREV, encoding='utf-8'))['units']}[by[k]['english']] for k in (1, 2)))
ck('ZERO tab e ZERO virgolette in entrambe le lingue (asserzioni negative)',
   sum(u['english'].count(TAB) + u['italian'].count(TAB) for u in cov) == 0
   and sum(u['english'].count(QUOTE) + u['italian'].count(QUOTE) for u in cov) == 0)
ck('APICI: 1 in inglese (unita 6, `You\'ve`), 8 in italiano su 7 unita',
   {u['idx']: u['english'].count(APOS) for u in cov if APOS in u['english']} == {6: 1}
   and {u['idx']: u['italian'].count(APOS) for u in cov if APOS in u['italian']}
   == {4: 1, 15: 1, 21: 1, 22: 1, 25: 1, 26: 1, 27: 2},
   ({u['idx']: u['english'].count(APOS) for u in cov if APOS in u['english']},
    {u['idx']: u['italian'].count(APOS) for u in cov if APOS in u['italian']}))
ck('SEGNAPOSTO: 43 in 5 famiglie, e ORDINE identico per unita',
   collections.Counter(t for u in cov for t in TAG.findall(u['english'])) == TOK
   == collections.Counter(t for u in cov for t in TAG.findall(u['italian']))
   and not [u['idx'] for u in cov if TAG.findall(u['english']) != TAG.findall(u['italian'])],
   ([u['idx'] for u in cov if TAG.findall(u['english']) != TAG.findall(u['italian'])],
    dict(collections.Counter(t for u in cov for t in TAG.findall(u['italian'])))))
ck('`<cargo>` non ha mai un articolo davanti (8 su 8); `<planet>` e `<destination>` restano famiglie distinte',
   not [u['idx'] for u in cov if '<cargo>' in u['italian']
        and re.search(r'\b(il|lo|la|i|gli|le|un|uno|una|del|della|dei)\s+<cargo>', u['italian'])]
   and sum(1 for u in cov if '<cargo>' in u['italian']) == 8
   and collections.Counter(t for u in cov for t in TAG.findall(u['english']))['<planet>'] == 12
   and collections.Counter(t for u in cov for t in TAG.findall(u['english']))['<destination>'] == 2,
   [u['idx'] for u in cov if '<cargo>' in u['italian']
    and re.search(r'\b(il|lo|la|i|gli|le|un|uno|una|del|della|dei)\s+<cargo>', u['italian'])])
ck('`Ember Waste` resta INVARIATO: il nome non viene tradotto (corpus: 13 occorrenze inglesi)',
   sum(u['english'].count('Ember Waste') for u in cov) == 3
   and sum(u['italian'].count('Ember Waste') for u in cov) == 3
   and not [u['idx'] for u in cov if re.search(r'[Bb]race|[Bb]raci', u['italian'])])
ck('i gruppi di stringhe identiche hanno UNA sola resa',
   all(len({by[i]['italian'] for i in g}) == 1 for g in GRUPPI)
   and all(len({by[i]['english'] for i in g}) == 1 for g in GRUPPI),
   [(g, len({by[i]['italian'] for i in g})) for g in GRUPPI])
ck('la prima MISSION_TEXT del file compare qui (5 unita, tutte tradotte)',
   [u['idx'] for u in cov if u['kind'] == 'MISSION_TEXT'] == [22, 23, 26, 27, 28]
   and all(u['italian'] != u['english'] for u in cov if u['kind'] == 'MISSION_TEXT'))
ck('lessico: emporio per outfitter, compenso logistico, assegnazione di risorse, avamposti',
   'empori' in by[18]['italian'] and "dell'emporio" in by[15]['italian']
   and 'compenso logistico' in by[9]['italian'] and 'assegnazione di risorse' in by[22]['italian']
   and 'avamposti' in by[4]['italian'])
ck('fazioni invariante: Remnant e Korath, nessun «Remnants»',
   'Remnant' in by[2]['italian'] and 'Remnant' in by[27]['italian'] and 'Korath' in by[4]['italian']
   and 'Remnants' not in ' '.join(u['italian'] for u in cov))
ck('nessun caporale, nessun carattere tipografico',
   not [u['idx'] for u in cov for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026' if c in u['italian']])
nonlat = [(u['idx'], c) for u in cov for c in u['italian'] if ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']],
   [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90 (0,95-1,34)',
   all(0.55 < u['ratio'] < 1.90 for u in cov),
   [(u['idx'], u['ratio']) for u in cov if not 0.55 < u['ratio'] < 1.90])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("25 unita' prima (L261), e la precedente e in `Bounty 4`",
   db.execute('select count(*) from units where path=? and line<226', (PATH,)).fetchone()[0] == 25
   and db.execute('select context from units where path=? and line<226 order by line desc limit 1', (PATH,)).fetchone()
   == (CTXS[0],))
ck("33 unita' dopo la 490",
   db.execute('select count(*) from units where path=? and line>490', (PATH,)).fetchone()[0] == 33)
ck('il file ha 87 unita, righe 19-741',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (87, 19, 741))
st = dict(db.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('tutte le 29 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · 9 contesti · 43 segnaposto in 5 famiglie' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
