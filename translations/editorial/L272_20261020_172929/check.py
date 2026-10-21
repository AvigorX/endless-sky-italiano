r"""check.py — L272 (`data/dialog phrases.txt`, righe 102-172). **LOTTO TERMINALE: chiude il file.**

**25 `TEXT`** in **18 contesti `phrase:`**: taglie (singole e con flotta), flotte pirata, missioni di contrabbando concluse o
abortite, missioni essenziali dei **Free Worlds** fallite o rifiutate, e il blocco **tributo pacifista** (otto frasi).
Quattro cose da verificare con cura:

1. **lotto terminale**: oltre all'invariante di segmento ci vuole quella di **FILE** — 54 unita', righe distinte, ultima riga
   la **172**, **0 dopo**, somma dei due lotti = 54;
2. **il tributo pacifista ha OTTO unita'** (165-172), non tre come diceva il contratto L272: vince il workspace, e il
   documento e' stato corretto;
3. **sei famiglie di segnaposto**, con `<bunks>` nuovo (`<bunks> schiavi`: il numero di cuccette occupate);
4. **sette apici inglesi** e **quattro italiani**: elencati per unita'.
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
HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
PATH = 'data/dialog phrases.txt'
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
BLOCCHI = [('phrase:generic hunted bounty eliminated dialog', 102, 102),
           ('phrase:generic bounty hunting payment dialog', 105, 105),
           ('phrase:generic bounty hunting on visit', 108, 108),
           ('phrase:generic bounty hunting boarding on visit', 111, 111),
           ('phrase:generic hunted bounty fleet eliminated and payment dialog', 115, 115),
           ('phrase:generic hunted bounty fleet eliminated dialog', 119, 119),
           ('phrase:generic fleet bounty hunting payment dialog', 122, 122),
           ('phrase:generic fleet bounty hunting on visit', 125, 125),
           ('phrase:generic pirate fleet battle on visit', 129, 129),
           ('phrase:generic completed pirate cargo mission', 133, 133),
           ('phrase:generic completed highly illegal pirate cargo mission', 137, 137),
           ('phrase:generic aborted pirate passenger mission', 141, 141),
           ('phrase:generic aborted pirate cargo mission', 145, 145),
           ('phrase:generic completed pirate slave mission', 149, 149),
           ('phrase:generic aborted pirate slave mission', 153, 153),
           ('phrase:free worlds failed', 157, 157),
           ('phrase:free worlds declined', 161, 161),
           ('phrase:tribute pacifist undefined', 165, 172)]
PACIFISTI = list(range(18, 26))
TOK = {'<npc>': 8, '<destination>': 4, '<planet>': 8, '<payment>': 6, '<commodity>': 3, '<bunks>': 1}
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck('unita tradotte 25/25', len(cov) == 25 == len(units), '%d/%d' % (len(cov), len(units)))
ck('tipo: 25 TEXT, ne VALUE ne DESCRIPTION',
   collections.Counter(u['kind'] for u in units) == {'TEXT': 25},
   dict(collections.Counter(u['kind'] for u in units)))
ck('diciotto contesti, con le righe misurate (il pacifista ne occupa otto: 165-172)',
   [(c, by[[u['idx'] for u in cov if u['context'] == c][0]]['line'],
     by[[u['idx'] for u in cov if u['context'] == c][-1]]['line']) for c, _, _ in BLOCCHI] == BLOCCHI,
   [(c, by[[u['idx'] for u in cov if u['context'] == c][0]]['line']) for c, _, _ in BLOCCHI])
ck('righe 102-172, nessun buco interno, ultima unita del lotto alla 172',
   [u['line'] for u in cov] == sorted({u['line'] for u in cov})
   and cov[0]['line'] == 102 and cov[-1]['line'] == 172)
ck('tutte TRADOTTE, nessuna copiata',
   all(u['italian'] != u['english'] for u in cov), [u['idx'] for u in cov if u['italian'] == u['english']])
ck('SEGNAPOSTO per famiglia: 30 token, sei famiglie, identici in inglese e italiano',
   {t: sum(collections.Counter(TAG.findall(u['english']))[t] for u in cov) for t in TOK} == TOK
   == {t: sum(collections.Counter(TAG.findall(u['italian']))[t] for u in cov) for t in TOK})
ck('nessun segnaposto inventato o perso per unita',
   all(collections.Counter(TAG.findall(u['english'])) == collections.Counter(TAG.findall(u['italian'])) for u in cov),
   [u['idx'] for u in cov
    if collections.Counter(TAG.findall(u['english'])) != collections.Counter(TAG.findall(u['italian']))])
ck('ZERO tab, ZERO virgolette (due asserzioni negative)',
   sum(u['english'].count(TAB) + u['italian'].count(TAB) for u in cov) == 0
   and sum(u['english'].count(QUOTE) + u['italian'].count(QUOTE) for u in cov) == 0)
ck('APICI in inglese: 7 (unita 3, 4, 8, 9, 12, 13, 15)',
   {u['idx']: u['english'].count(APOS) for u in cov if APOS in u['english']}
   == {3: 1, 4: 1, 8: 1, 9: 1, 12: 1, 13: 1, 15: 1},
   {u['idx']: u['english'].count(APOS) for u in cov if APOS in u['english']})
ck('APICI in italiano: 4 (unita 14, 16, 17, 22)',
   {u['idx']: u['italian'].count(APOS) for u in cov if APOS in u['italian']}
   == {14: 1, 16: 1, 17: 1, 22: 1},
   {u['idx']: u['italian'].count(APOS) for u in cov if APOS in u['italian']})
ck('`<npc>` e una NAVE: femminile («e stata eliminata», unita 1, 5, 6; «la sua flotta», 5-8)',
   sum(1 for u in cov if 'è stata eliminata' in u['italian']) == 1
   and sorted(u['idx'] for u in cov if 'sono state eliminate' in u['italian']) == [5, 6]
   and 'sono ancora state eliminate' in by[8]['italian']
   and sum(1 for u in cov if 'la sua flotta' in u['italian']) == 4)
ck('`<bunks>` e un NUMERO di cuccette: «<bunks> schiavi», senza articolo davanti al segnaposto',
   '<bunks> schiavi' in by[14]['italian'] and by[14]['italian'].count('<bunks>') == 1)
ck('il pacifista: otto frasi, nessuna traccia di tributo pagato',
   len({by[i]['italian'] for i in PACIFISTI}) == 8
   and 'tributo' in by[23]['italian'] and 'credito' in by[23]['italian']
   and sum(1 for i in PACIFISTI if 'tributo' in by[i]['italian']) == 1)
ck('contrabbando: merce altamente illegale, schiavi, e il registro non edulcorato',
   'schiavi' in by[14]['italian'] and 'schiavi' in by[15]['italian']
   and 'città principale' in by[11]['italian'] and 'spazioporto' in by[10]['italian'])
ck('Free Worlds invariato, «istantanea» e «salvataggio automatico» per revert/autosave',
   by[16]['italian'].count('Free Worlds') == 1 and 'Free Worlds' in by[17]['italian']
   and 'salvataggio automatico' in by[16]['italian'] and 'istantanea' in by[16]['italian'])
ck('nessun residuo inglese delle parole chiave',
   not [u['idx'] for u in cov for w in ('bounty', 'fleet', 'pirates', 'tribute', 'slaves', 'boarding')
        if w in u['italian'].lower()],
   [(u['idx'], w) for u in cov for w in ('bounty', 'fleet', 'pirates', 'tribute', 'slaves', 'boarding')
    if w in u['italian'].lower()])
ck('nessun caporale, nessun carattere tipografico',
   not [u['idx'] for u in cov for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026' if c in u['italian']])
nonlat = [(u['idx'], c) for u in cov for c in u['italian'] if ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']],
   [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90 (0,92-1,31)',
   all(0.55 < u['ratio'] < 1.90 for u in cov),
   [(u['idx'], u['ratio']) for u in cov if not 0.55 < u['ratio'] < 1.90])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("29 unita' prima (L271)",
   db.execute('select count(*) from units where path=? and line<102', (PATH,)).fetchone()[0] == 29)
ck("ZERO unita' dopo la 172: il lotto CHIUDE il file",
   db.execute('select count(*) from units where path=? and line>172', (PATH,)).fetchone()[0] == 0)
ck('INVARIANTE DI FILE: 54 unita, righe 16-172, ultima alla 172',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (54, 16, 172))
somma, righe = 0, set()
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    us = [u for u in json.load(open(f, encoding='utf-8'))['units'] if u['path'] == PATH]
    if us:
        somma += len(us)
        righe |= {u['line'] for u in us}
ck('INVARIANTE DI FILE: somma dei due lotti = 54, righe distinte = 54, nessuna riga fuori',
   somma == 54 and len(righe) == 54 and min(righe) == 16 and max(righe) == 172,
   (somma, len(righe), min(righe) if righe else None, max(righe) if righe else None))
st = dict(db.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('tutte le 25 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · 18 contesti · 30 segnaposto in 6 famiglie' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
