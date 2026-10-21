r"""check.py — L263 (`data/remnant/remnant jobs.txt`, righe 491-682). Terzo lotto del file.

Sei missioni di soccorso (`Rescue 2` … `Rescue 5`), **13 `MISSION_TEXT`**, 6 `DESCRIPTION`, 5 `VALUE`.
Cose da verificare, in ordine di rischio:

1. **quattro stringhe sono ereditate da L262** e si pretendono identiche, rileggendo il suo `translation.json`;
2. **`<npc>` e' una nave**: 17 occorrenze, tutte al femminile (`la <npc>`, «scomparsa», «distrutta», «dispersa»,
   «Trovala», «aiutala»), e nessuna forma maschile;
3. **un solo tab** (unita' 21, primo carattere) e **due virgolette** (unita' 20, la frase delle Braci);
4. **zero apici in inglese**, 12 in italiano, elencati.
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
PREV = os.path.join(L10N, 'staging', 'editorial', 'L262_20261020_162037', 'translation.json')
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
CTXS = ['mission:Remnant: Rescue 2', 'mission:Remnant: Rescue 2B', 'mission:Remnant: Rescue 3',
        'mission:Remnant: Rescue 3B', 'mission:Remnant: Rescue 4', 'mission:Remnant: Rescue 5']
BLOCCHI = [(1, 3), (4, 8), (9, 12), (13, 17), (18, 22), (23, 24)]
TOK = {'<npc>': 17, '<destination>': 6, '<payment>': 5}
INHERITED = [3, 6, 7, 8, 12, 15, 16, 17]
APOS_IT = {1: 1, 2: 1, 5: 1, 6: 1, 7: 2, 10: 1, 11: 1, 14: 1, 15: 1, 16: 2, 21: 1}
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck('unita tradotte 24/24', len(cov) == 24 == len(units), '%d/%d' % (len(cov), len(units)))
ck('tipi: 13 MISSION_TEXT + 6 DESCRIPTION + 5 VALUE',
   collections.Counter(u['kind'] for u in units) == {'MISSION_TEXT': 13, 'DESCRIPTION': 6, 'VALUE': 5},
   dict(collections.Counter(u['kind'] for u in units)))
ck('sei contesti: primo e ultimo di ogni blocco come misurato',
   [(a, b, by[a]['context']) for a, b in BLOCCHI] == [(a, b, c) for (a, b), c in zip(BLOCCHI, CTXS)]
   and len(set(u['context'] for u in cov)) == 6,
   [(a, b, by[a]['context']) for a, b in BLOCCHI])
ck('righe 491-682, nessun buco interno',
   [u['line'] for u in cov] == sorted({u['line'] for u in cov})
   and cov[0]['line'] == 491 and cov[-1]['line'] == 682)
ck('i 5 VALUE sono COPIATI, identici per indice',
   [u['idx'] for u in cov if u['kind'] == 'VALUE'] == [4, 9, 13, 18, 23]
   and all(u['italian'] == u['english'] for u in cov if u['kind'] == 'VALUE'))
ck('le altre 19 unita sono TRADOTTE, nessuna copiata',
   all(u['italian'] != u['english'] for u in cov if u['kind'] != 'VALUE'),
   [u['idx'] for u in cov if u['kind'] != 'VALUE' and u['italian'] == u['english']])
ck("le 8 unita ereditate da L262 sono IDENTICHE alla lettera (riletto il suo translation.json)",
   all(by[k]['italian'] == {u['english']: u['italian'] for u in
                            json.load(open(PREV, encoding='utf-8'))['units']}[by[k]['english']]
       for k in INHERITED),
   [k for k in INHERITED
    if by[k]['italian'] != {u['english']: u['italian'] for u in
                            json.load(open(PREV, encoding='utf-8'))['units']}[by[k]['english']]])
ck('TAB: uno solo, unita 21, primo carattere; nessun altro tab in italiano',
   sum(u['italian'].count(TAB) for u in cov) == 1
   and [u['idx'] for u in cov if TAB in u['italian']] == [21]
   and by[21]['italian'].startswith(TAB)
   and sum(u['english'].count(TAB) for u in cov) == 1)
ck('VIRGOLETTE: 2 in inglese e 2 in italiano, entrambe nell unita 20',
   sum(u['english'].count(QUOTE) for u in cov) == 2 == sum(u['italian'].count(QUOTE) for u in cov)
   and [u['idx'] for u in cov if QUOTE in u['italian']] == [20]
   and by[20]['italian'].rstrip().endswith('"'))
ck('APICI: ZERO in inglese (asserzione negativa); 13 in italiano su 11 unita, mappa dichiarata',
   sum(u['english'].count(APOS) for u in cov) == 0
   and {u['idx']: u['italian'].count(APOS) for u in cov if APOS in u['italian']} == APOS_IT,
   {u['idx']: u['italian'].count(APOS) for u in cov if APOS in u['italian']})
ck('SEGNAPOSTO: 28 in 3 famiglie, e ORDINE identico per unita',
   collections.Counter(t for u in cov for t in TAG.findall(u['english'])) == TOK
   == collections.Counter(t for u in cov for t in TAG.findall(u['italian']))
   and not [u['idx'] for u in cov if TAG.findall(u['english']) != TAG.findall(u['italian'])],
   [u['idx'] for u in cov if TAG.findall(u['english']) != TAG.findall(u['italian'])])
ck('`<npc>` e una NAVE: 17 occorrenze, sempre «la <npc>», mai «il <npc>»',
   sum(u['italian'].count('<npc>') for u in cov) == 17
   and all('<npc>' not in m.group(0) for m in re.finditer(r'\b(?:il|lo|un|uno|del|dello)\s+<npc>',
                                                          ' '.join(u['italian'] for u in cov)))
   and 'la <npc>' in ' '.join(u['italian'] for u in cov)
   and 'della <npc>' in by[11]['italian'])
ck('concordanza al femminile: scomparsa, distrutta, dispersa, andata perduta, Trovala, aiutala',
   'è scomparsa' in by[1]['italian'] and 'è stata distrutta' in by[6]['italian']
   and 'risulta ancora dispersa' in by[3]['italian'] and 'è andata perduta' in by[7]['italian']
   and 'Trovala' in by[1]['italian'] and 'aiutala' in by[1]['italian']
   and not re.search(r'\b(?:scomparso|distrutto|disperso|perduto)\b',
                     ' '.join(u['italian'] for u in cov)))
ck('luoghi: «Cimitero» per Graveyard, `Terminus` e `Ember Waste` invariati',
   'Cimitero' in by[19]['italian'] and 'Cimitero' in by[20]['italian']
   and [u['idx'] for u in cov if 'Graveyard' in u['italian']] == [18]
   and all(u['kind'] == 'VALUE' for u in cov if 'Graveyard' in u['italian'])
   and 'Terminus' in by[23]['italian'] and 'Terminus' in by[24]['italian']
   and sum(u['italian'].count('Ember Waste') for u in cov) == 4
   and sum(u['english'].count('Ember Waste') for u in cov) == 4)
ck('lessico: assegnazione di risorse, recupero tecnologico, rifornimento, Braci',
   'assegnazione di risorse' in by[2]['italian'] and 'recupero tecnologico' in by[1]['italian']
   and 'missione di rifornimento' in by[10]['italian'] and 'Braci' in by[20]['italian'])
ck('nessun caporale, nessun carattere tipografico',
   not [u['idx'] for u in cov for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026' if c in u['italian']])
nonlat = [(u['idx'], c) for u in cov for c in u['italian'] if ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']],
   [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90',
   all(0.55 < u['ratio'] < 1.90 for u in cov),
   [(u['idx'], u['ratio']) for u in cov if not 0.55 < u['ratio'] < 1.90])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("54 unita' prima (L261 + L262), 9 dopo la 682",
   db.execute('select count(*) from units where path=? and line<491', (PATH,)).fetchone()[0] == 54
   and db.execute('select count(*) from units where path=? and line>682', (PATH,)).fetchone()[0] == 9)
ck('il file ha 87 unita, righe 19-741',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (87, 19, 741))
st = dict(db.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('tutte le 24 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · 6 contesti · 28 segnaposto in 3 famiglie' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
