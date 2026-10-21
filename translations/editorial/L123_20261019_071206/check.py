r"""check.py — L123 (`data/human/ships.txt`, 54 unita', righe 78-2044)

Primo lotto di un file di **navi**: **48 `DESCRIPTION`**, **6 `VALUE`**, **33 contesti** (18 da una sola unità),
**14 unità con tab**, **16 virgolette**, **zero token**.

Controlli propri del lotto:

- **i 6 `VALUE` sono nomi di nave al plurale** (`Argosies`, `Auxiliaries` ×3, `Finches`, `Furies`), **identici** al
  sorgente (decisione 259), elencati esplicitamente;
- **un contesto per nave**: 33 contesti per 54 unità, 18 da una sola; nessuna ripetizione strutturale;
- **la nota sui caccia** («Fighters do not come equipped with a hyperdrive…») compare **cinque volte** e ha **una
  sola resa**; il nome `Auxiliaries` tre volte.
"""
import collections
import json
import os
import re
import sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
units = sorted(src['units'], key=lambda x: x['line'])
tr = {}
parts = sorted(f for f in os.listdir(os.path.join(HERE, 'parts')) if f.endswith('.json'))
for p in parts:
    for k, v in json.load(open(os.path.join(HERE, 'parts', p), encoding='utf-8')).items():
        tr[int(k)] = v
out = {'block': src['block'], 'note': src['note'], 'units': []}
missing = [u['idx'] for u in units if u['idx'] not in tr]
for u in units:
    if u['idx'] not in tr:
        continue
    it = tr[u['idx']]
    out['units'].append({"idx": u['idx'], "id": u['id'], "path": u['path'], "line": u['line'],
                         "kind": u['kind'], "context": u['context'], "english": u['english'],
                         "italian": it, "ratio": round(len(it) / max(1, len(u['english'])), 3)})
open(os.path.join(HERE, 'translation.json'), 'w', encoding='utf-8').write(
    json.dumps(out, ensure_ascii=False, indent=1))
cov = out['units']
by = {v['idx']: v for v in cov}
TAGS = re.compile(r'<[^<>]+>')
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 54/54", len(cov) == 54 == len(units) and not missing, '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
kk = collections.Counter(u['kind'] for u in units)
ck('tipi: 48 DESCRIPTION · 6 VALUE', dict(kk) == {'DESCRIPTION': 48, 'VALUE': 6}, dict(kk))
VAL = [u['idx'] for u in units if u['kind'] == 'VALUE']
ck('i 6 VALUE sono identici al sorgente (nomi di nave al plurale)',
   VAL == [2, 6, 9, 10, 45, 53] and all(by[i]['italian'] == by[i]['english'] for i in VAL)
   and {by[i]['english'] for i in VAL} == {'Argosies', 'Auxiliaries', 'Finches', 'Furies'},
   [i for i in VAL if by[i]['italian'] != by[i]['english']])
ck('tutte le unita non-VALUE sono tradotte',
   not [v['idx'] for v in cov if v['kind'] != 'VALUE' and v['italian'].strip() == v['english'].strip()])
tabs = [v['idx'] for v in cov if v['english'].startswith('\t')]
ck('14 unita iniziano con tab, le stesse in traduzione',
   len(tabs) == 14 and tabs == [v['idx'] for v in cov if v['italian'].startswith('\t')], len(tabs))
ck('conteggio dei tab identico per unita',
   not [v['idx'] for v in cov if v['english'].count('\t') != v['italian'].count('\t')])
ck('16 virgolette in inglese e in italiano',
   sum(v['english'].count('"') for v in cov) == 16 == sum(v['italian'].count('"') for v in cov),
   (sum(v['english'].count('"') for v in cov), sum(v['italian'].count('"') for v in cov)))
ck('virgolette per unita: stesso numero',
   not [v['idx'] for v in cov if v['english'].count('"') != v['italian'].count('"')])
ck('le virgolette stanno nelle unita 13, 21, 27, 36 e 42',
   [v['idx'] for v in cov if '"' in v['english']] == [13, 21, 27, 36, 42],
   [v['idx'] for v in cov if '"' in v['english']])
ck('ZERO token (asserito)', collections.Counter(t for v in cov for t in TAGS.findall(v['english'])) == {}
   == collections.Counter(t for v in cov for t in TAGS.findall(v['italian'])))
ck('ZERO quadre · ZERO backtick (asserito)',
   not [v['idx'] for v in cov if '[' in v['italian'] or ']' in v['italian'] or '`' in v['italian']])
seen = collections.Counter(u['context'] for u in units)
ck('33 contesti distinti, tutti ship:', len(seen) == 33 and all(c.startswith('ship:') for c in seen),
   len(seen))
ck('distribuzione 18x1 / 11x2 / 3x3 / 1x5',
   collections.Counter(seen.values()) == {1: 18, 2: 11, 3: 3, 5: 1}, collections.Counter(seen.values()))
ck('prima e ultima unita: righe 78 e 2044', (cov[0]['line'], cov[-1]['line']) == (78, 2044),
   (cov[0]['line'], cov[-1]['line']))
ck('primo e ultimo contesto: Aerie / Fury',
   (cov[0]['context'], cov[-1]['context']) == ('ship:Aerie', 'ship:Fury'),
   (cov[0]['context'], cov[-1]['context']))
grd = collections.Counter(u['english'] for u in units)
ck('48 testi inglesi distinti per 54 unita', len(grd) == 48, len(grd))
ck('nessun gruppo con due rese diverse',
   not [k for k in grd if len({by[u['idx']]['italian'] for u in units if u['english'] == k}) > 1])
ck('la nota sui caccia compare 5 volte con una sola resa',
   sum(1 for u in units if u['english'].strip().startswith('Fighters do not come')) == 5
   and len({by[u['idx']]['italian'] for u in units
            if u['english'].strip().startswith('Fighters do not come')}) == 1)
it_grp = {}
for v in cov:
    it_grp.setdefault(v['italian'], []).append(v)
ck('nessun duplicato italiano non spiegato dal sorgente',
   not [g for g in it_grp.values() if len(g) > 1 and len({v['english'] for v in g}) > 1],
   [[v['idx'] for v in g] for g in it_grp.values() if len(g) > 1 and len({v['english'] for v in g}) > 1])
ck('registro approvato: nessun «voi»',
   not [v['idx'] for v in cov if re.search(r'\b(avete|potete|potrete|siete|vostro|vostra|vostri|vostre)\b',
                                           v['italian'])])
LOW = ' '.join(v['italian'] for v in cov).lower()
TERMS = ('baia di caccia', 'portatrice', 'nave da guerra', 'scafo', 'carico', 'manovrabile', 'intercettore',
         'iperguida', 'torretta', 'equipaggio')
ck('terminologia presente: 10 termini chiave', all(t in LOW for t in TERMS),
   [t for t in TERMS if t not in LOW])
# i nomi di nave restano inglesi: si neutralizzano prima della scansione dei residui
SHIPS = ('Lionheart Aerie', 'Argosy', 'Arrow', 'Auxiliary', 'Bactrian', 'Barb', 'Bastion', 'Behemoth', 'Berserker',
         'Blackbird', 'Bounder', 'Boxwing', 'Hauler', 'Bulk Freighter', 'Bulwark', 'Carrier', 'Falcon', 'Clipper',
         'Combat Drone', 'Container Transport', 'Corvette', 'Cruiser', 'Cutthroat', 'Dagger', 'Dreadnought',
         'Dropship', 'Enforcer', 'Finch', 'Firebird', 'Flivver', 'Freighter', 'Frigate', 'Fury', 'Hawk',
         'Leviathan', 'Protector', 'Sparrow', 'Barb', 'Bastion')
NOSCRUB = ' '.join(v['italian'] for v in cov)
for s in sorted(SHIPS, key=len, reverse=True):
    NOSCRUB = NOSCRUB.replace(s, '@@')
NOSCRUB = NOSCRUB.lower()
# «cargo» è un prestito entrato nell'italiano (modulo cargo, cassa cargo): non è un residuo
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' ship ', ' fighter ')
ck('nessun residuo inglese fuori dai nomi di nave e dai token',
   not [w for w in ENGW if w in NOSCRUB], [w for w in ENGW if w in NOSCRUB])
rs = [v['ratio'] for v in cov]
ck('rapporto nel gate', 0.55 < min(rs) and max(rs) < 1.90, '%.2f - %.2f' % (min(rs), max(rs)))
bad = [(v['idx'], n) for v in cov for p, n in ((r"\b(e|piu|perche|cosi|gia|puo|cioe|percio|fa)'", 'accento'),
       ('\u2026', 'ellissi'), ('\u2014', 'em dash'), ('\u2019', 'apostrofo curvo'), ('\u00ab', 'caporale'),
       ('\u00bb', 'caporale')) if re.search(p, v['italian'])]
ck('tipografia', not bad, bad)
nonlat = [v['idx'] for v in cov for c in v['italian'] if ord(c) > 127 and not 0x00C0 <= ord(c) <= 0x024F]
ck('caratteri non latini', not nonlat, nonlat)
c = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
st = dict(c.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('tutte le 54 unita sono PENDING nel database (misurato)',
   c.execute('select count(*) from units where id in (%s) and state != "PENDING"'
             % ','.join('?' * len(units)), [u['id'] for u in units]).fetchone()[0] == 0)
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d' % (sum(len(v['english'].split()) for v in cov),
                                 sum(len(v['italian'].split()) for v in cov)))
print('righe %d/%d · parti %d · mancanti %d' % (min(u['line'] for u in units), max(u['line'] for u in units),
      len(parts), len(missing)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
