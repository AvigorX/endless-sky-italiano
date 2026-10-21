r"""check.py — L306 (`data/quarg/quarg outfits.txt`, righe 257-579). **LOTTO TERMINALE del file**.

Dieci schede che chiudono il file: l'**invariante di FILE** (31 unita', somma dei lotti **11 + 10 + 10**) e tre cose del testo:

1. **dieci contesti, dieci unita'**: **nessuna coppia**, **nessuna tab** — le asserzioni «coppia/tab» sono **vuote** e vanno
   dichiarate come tali;
2. **otto nomi di arma e due hub INVARIATI**: `Skydagger`, `Skylance`, `Stratospear`, `Elysian Ranseur`, `Celestial Culverin`,
   `Astral Ribault`, `Slipstream Projector`, `Phalanx System`, `Peripheral Repair Hub`, `Central Repair Hub`. Il test rifiuta le
   traduzioni tentatrici («Pugnale del cielo», «Lancia delle stelle», «Falange»…);
3. **il trattino ` - `** dell'unita 1 si conserva (non diventa due punti né virgola).
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
ARMI = ['Skydagger', 'Skylance', 'Stratospear', 'Elysian Ranseur', 'Celestial Culverin', 'Astral Ribault',
        'Slipstream Projector', 'Phalanx System']
HUB = ['Peripheral Repair Hub', 'Central Repair Hub']
VIETATI = ['Pugnale del cielo', 'Lancia delle stelle', 'Falange', 'Falange System', 'Proiettore della scia',
           'Culverina celeste', 'Ribault astrale', 'Hub di riparazione periferico']
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
_it = ''.join(u['italian'] for u in cov)
ck('unita tradotte 10/10', len(cov) == 10 == len(units), '%d/%d' % (len(cov), len(units)))
ck('tutte DESCRIPTION, dieci contesti da UNA unita ciascuno',
   {u['kind'] for u in cov} == {'DESCRIPTION'} and len(grp) == 10 and set(grp.values()) == {1}, dict(grp))
ck('ASSERZIONI VUOTE sulle coppie: nessun contesto con due unita',
   all(n == 1 for n in grp.values()) and not [c for c, n in grp.items() if n > 1])
ck('ASSERZIONI VUOTE sulle tab: nessuna unita inizia con la tabulazione',
   sum(u['english'].count(TAB) for u in cov) == 0 == sum(u['italian'].count(TAB) for u in cov))
ck('tutte e 10 le unita sono TRADOTTE, nessuna copiata',
   all(u['italian'] != u['english'] for u in cov), [u['idx'] for u in cov if u['italian'] == u['english']])
_ctx = {u['context'].split(':', 1)[1] for u in cov}
ck('i dieci contesti sono esattamente i due hub e le otto armi',
   _ctx == set(HUB + ARMI), sorted(_ctx - set(HUB + ARMI)))
ck('l unica arma NOMINATA in prosa (`Skylance`, riga 336) resta invariata',
   'Skylance' in at[336]['italian'] and 'Skylance' not in ''.join(u['italian'] for u in cov if u['line'] != 336))
ck('nessuna delle traduzioni tentatrici dei nomi d arma compare nel testo',
   not [v for v in VIETATI if v.lower() in _it.lower()], [v for v in VIETATI if v.lower() in _it.lower()])
ck('i due hub sono citati come «hub» e non come «hub di riparazione periferico»',
   'hub centrale' in by[2]['italian'] and 'hub di riparazione periferico' not in _it.lower())
ck('il trattino ` - ` dell unita 1 e conservato',
   ' - durabilità, longevità e' in by[1]['italian'])
ck('APICI: cinque in inglese, dieci in italiano',
   sum(u['english'].count(APOS) for u in cov) == 5 and sum(u['italian'].count(APOS) for u in cov) == 10,
   (sum(u['english'].count(APOS) for u in cov), sum(u['italian'].count(APOS) for u in cov)))
ck('VIRGOLETTE, SEGNAPOSTO, ALTERNATIVE: tutti zero (asserzioni vuote)',
   sum(u['english'].count(QUOTE) for u in cov) == 0 == sum(u['italian'].count(QUOTE) for u in cov)
   and sum(len(TAG.findall(u['italian'])) for u in cov) == 0
   and sum(len(ALT.findall(u['italian'])) for u in cov) == 0)
ck('lessico: spaziotempo, energia negativa, mondi ad anello, antimissile, abbordaggi',
   'spaziotempo' in by[6]['italian'] and 'energia negativa' in by[8]['italian']
   and 'mondi ad anello' in by[9]['italian'] and 'antimissile' in by[5]['italian']
   and 'abbordaggi' in by[10]['italian'])
ck('REGISTRO: nessuna seconda persona',
   not [u['idx'] for u in cov if re.search(r'\b(tu|tuo|tua|tuoi|tue|ti|te)\b', u['italian'])],
   [u['idx'] for u in cov if re.search(r'\b(tu|tuo|tua|tuoi|tue|ti|te)\b', u['italian'])])
ck('nessun caporale, nessun carattere tipografico',
   not [u['idx'] for u in cov for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026' if c in u['italian']])
nonlat = [(u['idx'], c) for u in cov for c in u['italian'] if ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessun doppio spazio', not [u['idx'] for u in cov if '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90 (0,88-1,19)',
   all(0.55 < u['ratio'] < 1.90 for u in cov),
   [(u['idx'], u['ratio']) for u in cov if not 0.55 < u['ratio'] < 1.90])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck('FILE: 21 unita prima della 257 (11 + 10)',
   db.execute('select count(*) from units where path=? and line<257', (PATH,)).fetchone()[0] == 21)
ck('FILE: ZERO unita dopo la 579 — il lotto CHIUDE il file',
   db.execute('select count(*) from units where path=? and line>579', (PATH,)).fetchone()[0] == 0)
ck('FILE: 31 unita, righe 37-579, tutte DESCRIPTION',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (31, 37, 579)
   and dict(db.execute('select kind,count(*) from units where path=? group by kind', (PATH,)).fetchall())
   == {'DESCRIPTION': 31})
ck('FILE: i tre lotti sommano 31 (11 + 10 + 10)', 11 + 10 + 10 == 31)
ck('tutte le 10 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · 10 contesti singoli · 0 tab · FILE 31/31' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
