r"""check.py — L126 (`data/incipias/incipias first contact.txt`, 55 unita', righe 22-218)

Primo lotto del file: **48 `MISSION_TEXT`**, **4 `UI_LABEL`**, **3 `LOGBOOK`**, **6 contesti** (23 / 13 / 13 / 2 /
2 / 2), **37 unità con tab**, **65 virgolette**, **zero token**, **52 testi distinti**.

Controlli propri del lotto:

- **4 `UI_LABEL`** (`ut divitas`, `spec inci`, `both planets`, `new species`): **identiche al sorgente**, escluse da
  «tutte tradotte» e verificate in un controllo loro;
- **65 virgolette**, comprese le **3 dell'unità 23** (il sorgente lascia una virgoletta di chiusura in più);
- **due registri**: il Guardiano alto e arcaico, i Quarg cerimoniali — il controllo verifica che le forme
  caratteristiche ci siano e che non ci siano residui inglesi.
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


ck("unita' tradotte 55/55", len(cov) == 55 == len(units) and not missing, '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
kk = collections.Counter(u['kind'] for u in units)
ck('tipi: 48 MISSION_TEXT · 4 UI_LABEL · 3 LOGBOOK',
   dict(kk) == {'MISSION_TEXT': 48, 'UI_LABEL': 4, 'LOGBOOK': 3}, dict(kk))
LAB = [u['idx'] for u in units if u['kind'] == 'UI_LABEL']
ck('le 4 UI_LABEL (30, 32, 34, 39) sono identiche al sorgente',
   LAB == [30, 32, 34, 39]
   and [by[i]['italian'] for i in LAB] == ['ut divitas', 'spec inci', 'both planets', 'new species'],
   [(i, by[i]['italian']) for i in LAB])
ck('tutte le unita prosaiche sono tradotte',
   not [v['idx'] for v in cov if v['kind'] != 'UI_LABEL' and v['italian'].strip() == v['english'].strip()],
   [v['idx'] for v in cov if v['kind'] != 'UI_LABEL' and v['italian'].strip() == v['english'].strip()])
ck('i 3 LOGBOOK sono tradotti',
   not [v['idx'] for v in cov if v['kind'] == 'LOGBOOK' and v['italian'] == v['english']])
tabs = [v['idx'] for v in cov if v['english'].startswith('\t')]
ck('37 unita iniziano con tab, le stesse in traduzione',
   len(tabs) == 37 and tabs == [v['idx'] for v in cov if v['italian'].startswith('\t')], len(tabs))
ck('conteggio dei tab identico per unita',
   not [v['idx'] for v in cov if v['english'].count('\t') != v['italian'].count('\t')])
ck('65 virgolette in inglese e in italiano',
   sum(v['english'].count('"') for v in cov) == 65 == sum(v['italian'].count('"') for v in cov),
   (sum(v['english'].count('"') for v in cov), sum(v['italian'].count('"') for v in cov)))
ck('virgolette per unita: stesso numero',
   not [v['idx'] for v in cov if v['english'].count('"') != v['italian'].count('"')],
   [(v['idx'], v['english'].count('"'), v['italian'].count('"')) for v in cov
    if v['english'].count('"') != v['italian'].count('"')])
ck('l unita 23 ha 3 virgolette (una in piu del sorgente), le altre 2 o 4',
   by[23]['italian'].count('"') == 3
   and sorted({v['english'].count('"') for v in cov if '"' in v['english']}) == [2, 3, 4],
   (by[23]['italian'].count('"'), sorted({v['english'].count('"') for v in cov if '"' in v['english']})))
ck('ZERO token (asserito)', collections.Counter(t for v in cov for t in TAGS.findall(v['english'])) == {}
   == collections.Counter(t for v in cov for t in TAGS.findall(v['italian'])))
ck('ZERO quadre · ZERO backtick (asserito)',
   not [v['idx'] for v in cov if '[' in v['italian'] or ']' in v['italian'] or '`' in v['italian']])
seen = collections.Counter(u['context'] for u in units)
ck('6 contesti distinti, tutti mission:', len(seen) == 6 and all(c.startswith('mission:') for c in seen),
   len(seen))
ck('distribuzione 23 / 13 / 13 / 2 / 2 / 2',
   sorted(seen.values()) == [2, 2, 2, 13, 13, 23], sorted(seen.values()))
ck('prima e ultima unita: righe 22 e 218', (cov[0]['line'], cov[-1]['line']) == (22, 218),
   (cov[0]['line'], cov[-1]['line']))
ck('primo e ultimo contesto: Warning of the Guardian / The Derelict',
   (cov[0]['context'], cov[-1]['context'])
   == ('mission:Incipias: Warning of the Guardian', 'mission:Incipias: The Derelict'),
   (cov[0]['context'], cov[-1]['context']))
grd = collections.Counter(u['english'] for u in units)
ck('52 testi inglesi distinti per 55 unita', len(grd) == 52, len(grd))
ck('3 coppie ripetute, nessuna con due rese',
   collections.Counter(grd.values()) == {1: 49, 2: 3}
   and not [k for k in grd if len({by[u['idx']]['italian'] for u in units if u['english'] == k}) > 1],
   collections.Counter(grd.values()))
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
TERMS = ('fiori non nati', 'guardiano', 'quarg', 'iperguida', 'equipaggio', 'specie', 'vicolo cieco',
         'attrezzatura di riparazione', 'torretta', 'artigliere')
ck('terminologia presente: 10 termini chiave', all(t in LOW for t in TERMS),
   [t for t in TERMS if t not in LOW])
ck('registro alto del Guardiano (follia, giacciono, viaggiatore)',
   all(t in LOW for t in ('follia', 'giacciono', 'viaggiatore')))
ck('registro cerimoniale dei Quarg (peregrinare, vagabondaggi, autorizzato)',
   all(t in LOW for t in ('peregrinare', 'vagabondaggi', 'autorizzato')))
NOSCRUB = ' '.join(TAGS.sub('""', v['italian']) for v in cov if v['kind'] != 'UI_LABEL')
for s in ('Quarg', 'Hai', 'Incipias'):
    NOSCRUB = NOSCRUB.replace(s, '@@')
NOSCRUB = NOSCRUB.lower()
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' ship ', ' voice ')
ck('nessun residuo inglese fuori dai nomi propri e dai token',
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
ck('tutte le 55 unita sono PENDING nel database (misurato)',
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
