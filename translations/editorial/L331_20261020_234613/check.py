r"""check.py — L331 (`data/human/power.txt`, 23–272). **TERMINALE, FILE INTERO.** 22 `DESCRIPTION`, 22 contesti, 0 tab, 0 virgolette."""
import collections
import glob
import json
import os
import sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
PATH = 'data/human/power.txt'
NOMI = ['LP036a', 'LP072a', 'LP144a', 'LP288a', 'LP576a', 'KP-6', 'nGVF-AA', 'nGVF-BB',
        'nGVF-CC', 'nGVF-DD', 'nGVF-EE', 'RT-I', 'S3', 'NT-200', 'Dwarf Core', 'Breeder Reactor',
        'Armageddon Core', 'Stack Core', 'Deep Sky', 'Korunak Photovoltaics', 'Free Worlds', 'Dreadnought']
src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
units = sorted(src['units'], key=lambda x: x['line'])
hits = {}
for p in sorted(f for f in os.listdir(os.path.join(HERE, 'parts')) if f.endswith('.json')):
    for k, v in json.load(open(os.path.join(HERE, 'parts', p), encoding='utf-8')).items():
        hits[int(k)] = v
out = {'block': src['block'], 'note': src['note'], 'units': []}
for u in units:
    it = hits[u['idx']]
    out['units'].append({"idx": u['idx'], "id": u['id'], "path": u['path'], "line": u['line'],
                         "kind": u['kind'], "context": u['context'], "english": u['english'],
                         "italian": it, "ratio": round(len(it) / max(1, len(u['english'])), 3)})
open(os.path.join(HERE, 'translation.json'), 'w', encoding='utf-8').write(
    json.dumps(out, ensure_ascii=False, indent=1))
cov = out['units']
at = {u['line']: u for u in cov}
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else 'FAIL'), c))


ck('22/22 unità tradotte', len(cov) == 22 == len(units))
ck('22 DESCRIPTION, 22 contesti (uno per unità)',
   collections.Counter(u['kind'] for u in cov) == {'DESCRIPTION': 22}
   and len({u['context'] for u in cov}) == 22
   and max(collections.Counter(u['context'] for u in cov).values()) == 1)
ck('nessuna tab, nessuna virgoletta, nessun segnaposto (asserzioni vuote)',
   not [u for u in cov if '\t' in u['italian'] or '"' in u['italian'] or '<' in u['italian']])
ck('`Supercapacitors` è nome comune in prosa: reso «supercondensatori»',
   'supercondensatori' in at[23]['italian'])
ck('i nomi degli equipaggiamenti sono invariati dove compaiono',
   all(n in u['italian'] for u in cov for n in NOMI if n in u['english']))
ck('la scala delle celle a combustibile: AA → EE in ordine crescente',
   'molto piccole o lente' in at[114]['italian'] and 'qualche cannone leggero' in at[126]['italian']
   and 'taglia media' in at[138]['italian'] and 'relativamente grande' in at[150]['italian']
   and 'più grande disponibile' in at[162]['italian'])
ck('la scala delle batterie: 036a → 576a con capacità crescente',
   'modello più elementare' in at[45]['italian'] and 'più del doppio' in at[45]['italian']
   and 'taglia media' in at[56]['italian'] and 'pacco batterie grande' in at[67]['italian']
   and 'tutta questa potenza' in at[78]['italian'])
ck('Deep Sky e Korunak Photovoltaics invariati, Dreadnought e Free Worlds invariati',
   'Deep Sky' in at[212]['italian'] and 'Korunak Photovoltaics' in at[101]['italian']
   and 'Free Worlds' in at[272]['italian'] and 'Dreadnought' in at[272]['italian'])
ck('Marina della Repubblica (Republic Navy) e non «Marina Repubblicana»',
   'Marina della Repubblica' in at[260]['italian'])
ck('nessuna unità identica all inglese', not [u for u in cov if u['italian'] == u['english']])
ck('nessun caporale, nessun carattere tipografico, nessun doppio spazio',
   not [c for u in cov for c in u['italian'] if c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026']
   and not [u['idx'] for u in cov if '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90', all(0.55 < u['ratio'] < 1.90 for u in cov),
   [(u['idx'], u['ratio']) for u in cov if not 0.55 < u['ratio'] < 1.90])
ck('FILE: 22 unità, righe 23–272, zero prima e dopo',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (22, 23, 272)
   and db.execute('select count(*) from units where path=? and (line<23 or line>272)', (PATH,)).fetchone()[0] == 0)
ck('FILE: copertura 22/22, un solo lotto',
   db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0] == 22
   and sum(1 for f in glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))
           if any(u['path'] == PATH for u in json.load(open(f, encoding='utf-8'))['units'])) == 1)
ck('tutte le 22 unità restano PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · 22 DESCRIPTION · 22 contesti · FILE 22/22' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
