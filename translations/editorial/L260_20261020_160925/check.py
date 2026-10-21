r"""check.py — L260 (`data/human/post-war reactions.txt`, righe 253-264). **LOTTO TERMINALE**: chiude il file.

Chiude `post-war reactions.txt` a **87/87** (quattordicesimo file completo) con **7 unita'**: il pezzo finale della
sottotrama di Gus — l'arrivo all'officina, il fratello **Calvin**, il saluto, la presa al collo «con estrema attenzione» e la
liberazione.

**Invariante di FILE** (non di segmento): `22 + 23 + 20 + 15 + 7 = 87` unita', **87 righe distinte**, la **264** come ultima
riga, **0** dopo.

Due unita' di **narrazione** (4 e 7) non hanno virgolette; le altre cinque sono dialogo. I tab sono su **tutte e 7**.
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
PATH = 'data/human/post-war reactions.txt'
CTX = 'mission:War Reactions: Syndicate Orphan'
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
QUOTES = {1: 2, 2: 2, 3: 2, 4: 0, 5: 4, 6: 6, 7: 0}
NARRATION = [4, 7]
APOS_EN = {2: 3, 3: 2, 5: 3, 6: 3}
APOS_IT = {1: 1, 4: 2, 5: 2, 6: 1}
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck('unita tradotte 7/7', len(cov) == 7 == len(units), '%d/%d' % (len(cov), len(units)))
ck('tipo: 7 MISSION_TEXT', collections.Counter(u['kind'] for u in units) == {'MISSION_TEXT': 7},
   dict(collections.Counter(u['kind'] for u in units)))
ck('contesto unico: mission:War Reactions: Syndicate Orphan',
   {u['context'] for u in cov} == {CTX}, sorted({u['context'] for u in cov}))
ck('righe 253-264, la 264 e l\'ultima del lotto',
   [u['line'] for u in cov] == sorted({u['line'] for u in cov})
   and cov[0]['line'] == 253 and cov[-1]['line'] == 264)
ck('tutte TRADOTTE, nessuna copiata', not [u for u in cov if u['italian'] == u['english']],
   [u['idx'] for u in cov if u['italian'] == u['english']])
ck('TAB: 7 in inglese, 7 in italiano, su TUTTE le unita, come primo carattere',
   sum(u['english'].count(TAB) for u in cov) == 7 == sum(u['italian'].count(TAB) for u in cov)
   and all(u['italian'].startswith(TAB) for u in cov))
ck('VIRGOLETTE: 16 in inglese, 16 in italiano, mappa per unita identica',
   {u['idx']: u['english'].count(QUOTE) for u in cov} == QUOTES
   == {u['idx']: u['italian'].count(QUOTE) for u in cov},
   ({u['idx']: u['english'].count(QUOTE) for u in cov},
    {u['idx']: u['italian'].count(QUOTE) for u in cov}))
ck('le due unita di NARRAZIONE (4 e 7) non hanno virgolette in nessuna delle due lingue',
   all(by[i]['english'].count(QUOTE) == 0 == by[i]['italian'].count(QUOTE) for i in NARRATION)
   and [u['idx'] for u in cov if QUOTE not in u['italian']] == NARRATION,
   [u['idx'] for u in cov if QUOTE not in u['italian']])
ck('APICI: 11 in inglese (4 unita), 6 in italiano (4 unita), mappe dichiarate',
   {u['idx']: u['english'].count(APOS) for u in cov if APOS in u['english']} == APOS_EN
   and {u['idx']: u['italian'].count(APOS) for u in cov if APOS in u['italian']} == APOS_IT,
   ({u['idx']: u['english'].count(APOS) for u in cov if APOS in u['english']},
    {u['idx']: u['italian'].count(APOS) for u in cov if APOS in u['italian']}))
ck('ZERO segnaposto in inglese e in italiano (asserzione negativa)',
   not [t for u in cov for t in TAG.findall(u['english']) + TAG.findall(u['italian'])])
ck('i nomi restano: Gus, Calvin; «Sindacato» per Syndicate, «Marina» per Navy',
   'Calvin' in by[6]['italian'] and 'Gus' in by[5]['italian'] and 'Gus' in by[4]['italian']
   and 'Sindacato' in by[2]['italian'] and 'Marina' in by[3]['italian']
   and 'Syndicate' not in ' '.join(u['italian'] for u in cov))
ck('lessico della scena: presa al collo, distretto dell\'infanzia, spazioporto, officina',
   'presa al collo' in by[5]['italian'] and "distretto dell'infanzia" in by[5]['italian']
   and 'spazioporto' in by[5]['italian'] and 'officina' in by[4]['italian'])
ck('nessun caporale, nessun carattere tipografico',
   not [u['idx'] for u in cov for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026' if c in u['italian']])
nonlat = [(u['idx'], c) for u in cov for c in u['italian'] if ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']],
   [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90 (0,91-1,37)',
   all(0.55 < u['ratio'] < 1.90 for u in cov),
   [(u['idx'], u['ratio']) for u in cov if not 0.55 < u['ratio'] < 1.90])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("80 unita' prima (L256-L259), e l'ultima prima della 253 e nello stesso contesto",
   db.execute('select count(*) from units where path=? and line<253', (PATH,)).fetchone()[0] == 80
   and db.execute('select context from units where path=? and line<253 order by line desc limit 1', (PATH,)).fetchone()
   == (CTX,))
ck("ZERO unita' dopo la 264: il lotto CHIUDE il file",
   db.execute('select count(*) from units where path=? and line>264', (PATH,)).fetchone()[0] == 0)
ck("la 264 e' la riga massima del file, che ha 87 unita' fra la 40 e la 264",
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (87, 40, 264))
righe, lotti = set(), []
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    us = [u for u in json.load(open(f, encoding='utf-8'))['units'] if u['path'] == PATH]
    if us:
        lotti.append((os.path.basename(os.path.dirname(f)), len(us)))
        righe |= {u['line'] for u in us}
ck('INVARIANTE DI FILE: 22 + 23 + 20 + 15 + 7 = 87 unita in 5 lotti',
   [n for _, n in lotti] == [22, 23, 20, 15, 7] and sum(n for _, n in lotti) == 87 == len(righe),
   (lotti, len(righe)))
ck('le 87 righe dei lotti sono esattamente quelle del database (nessun buco)',
   righe == {l for l, in db.execute('select line from units where path=?', (PATH,))})
st = dict(db.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('tutte le 7 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d' % (sum(len(v['english'].split()) for v in cov),
                                sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
