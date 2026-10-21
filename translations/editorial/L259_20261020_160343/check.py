r"""check.py — L259 (`data/human/post-war reactions.txt`, righe 222-250). Quarto lotto del file.

Un solo contesto (`War Reactions: Syndicate Orphan`) e **tutti e 15 i tab presenti**. Il lotto ha due forme delicate:

- **la 2 ha CINQUE virgolette**: l'ultima citazione (`"Solo i più svegli di noi possono farlo…`) si apre e **non si chiude**
  nel sorgente — terzo caso del file dopo L257 u12 e L258 u5: si **riproduce**;
- **le unita' 7 e 8 sono quasi identiche**: cambia solo una battuta (`You're Captain <first> <last>!` contro `You led the
  attack!`) e il resto del testo e' parola per parola lo stesso. Il test verifica **la differenza in inglese e in italiano**
  e **l'identita' della coda**, cosi' non si puo' «unificare» per distrazione.

`<first>` e `<last>` compaiono **due volte ciascuno** (unita' 4 e 7), invariati e senza concordanza.
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
QUOTES = {1: 4, 2: 5, 3: 4, 4: 2, 5: 2, 6: 2, 7: 6, 8: 6, 9: 2, 10: 2, 11: 2, 12: 2, 13: 2, 14: 2, 15: 2}
APOS_EN = {1: 2, 2: 3, 3: 2, 4: 1, 7: 2, 8: 1, 11: 1, 12: 3, 13: 2, 15: 2}
APOS_IT = {1: 1, 2: 1, 3: 1, 7: 4, 8: 5, 9: 1, 10: 1, 12: 3}
TOK = {'<first>': 2, '<last>': 2}
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck('unita tradotte 15/15', len(cov) == 15 == len(units), '%d/%d' % (len(cov), len(units)))
ck('tipo: 15 MISSION_TEXT', collections.Counter(u['kind'] for u in units) == {'MISSION_TEXT': 15},
   dict(collections.Counter(u['kind'] for u in units)))
ck('contesto unico: mission:War Reactions: Syndicate Orphan',
   {u['context'] for u in cov} == {CTX}, sorted({u['context'] for u in cov}))
ck('righe 222-250, nessun buco interno',
   [u['line'] for u in cov] == sorted({u['line'] for u in cov})
   and cov[0]['line'] == 222 and cov[-1]['line'] == 250)
ck('tutte TRADOTTE, nessuna copiata', not [u for u in cov if u['italian'] == u['english']],
   [u['idx'] for u in cov if u['italian'] == u['english']])
ck('TAB: 15 in inglese, 15 in italiano, su TUTTE le unita, come primo carattere',
   sum(u['english'].count(TAB) for u in cov) == 15 == sum(u['italian'].count(TAB) for u in cov)
   and all(TAB in u['english'] and TAB in u['italian'] for u in cov)
   and all(u['italian'].startswith(TAB) for u in cov))
ck('VIRGOLETTE: 45 in inglese, 45 in italiano, mappa per unita identica',
   {u['idx']: u['english'].count(QUOTE) for u in cov if QUOTE in u['english']} == QUOTES
   == {u['idx']: u['italian'].count(QUOTE) for u in cov if QUOTE in u['italian']},
   ({u['idx']: u['english'].count(QUOTE) for u in cov if QUOTE in u['english']},
    {u['idx']: u['italian'].count(QUOTE) for u in cov if QUOTE in u['italian']}))
ck('la 2 ha CINQUE virgolette in entrambe le lingue: citazione aperta e non chiusa, riprodotta',
   by[2]['english'].count(QUOTE) == 5 == by[2]['italian'].count(QUOTE)
   and by[2]['english'].rstrip().endswith('machines.') and by[2]['italian'].rstrip().endswith('cucire.'),
   (by[2]['english'][-24:], by[2]['italian'][-24:]))
ck('APICI: 19 in inglese (10 unita), 17 in italiano (8 unita), mappe dichiarate',
   {u['idx']: u['english'].count(APOS) for u in cov if APOS in u['english']} == APOS_EN
   and {u['idx']: u['italian'].count(APOS) for u in cov if APOS in u['italian']} == APOS_IT,
   ({u['idx']: u['english'].count(APOS) for u in cov if APOS in u['english']},
    {u['idx']: u['italian'].count(APOS) for u in cov if APOS in u['italian']}))
ck('SEGNAPOSTI: <first> 2, <last> 2, con ordine identico per unita',
   collections.Counter(t for u in cov for t in TAG.findall(u['english'])) == TOK
   == collections.Counter(t for u in cov for t in TAG.findall(u['italian']))
   and not [u['idx'] for u in cov if TAG.findall(u['english']) != TAG.findall(u['italian'])],
   [u['idx'] for u in cov if TAG.findall(u['english']) != TAG.findall(u['italian'])])
ck('i segnaposto stanno nelle unita 4 e 7, non altrove',
   [u['idx'] for u in cov if TAG.search(u['english'])] == [4, 7],
   [u['idx'] for u in cov if TAG.search(u['english'])])
ck('7 e 8 sono quasi identiche: differisce solo la battuta, non il resto',
   'Sei il capitano <first> <last>!' in by[7]['italian']
   and "Hai guidato tu l'attacco!" in by[8]['italian']
   and 'Sei il capitano' not in by[8]['italian'] and "l'attacco" not in by[7]['italian']
   and by[7]['italian'][:60] == by[8]['italian'][:60]
   and by[7]['italian'][-60:] == by[8]['italian'][-60:]
   and by[7]['italian'].endswith('Ti tende la mano e tu la stringi.')
   and by[8]['italian'].endswith('Ti tende la mano e tu la stringi.'),
   (by[7]['italian'][:60], by[8]['italian'][:60]))
ck('lessico: Servizio di Sicurezza Ausiliario, Dispositivo per l\'Infanzia, navi da guerra',
   'Servizio di Sicurezza Ausiliario' in by[1]['italian']
   and "Dispositivo per l'Infanzia del Sindacato" in by[7]['italian']
   and 'navi da guerra' in by[9]['italian'] and 'tablet' in by[8]['italian'])
ck('nessun nome proprio tradotto: Pug, Maker, Syndicate->Sindacato',
   'Pug' in by[3]['italian'] and 'Maker' in by[3]['italian']
   and 'Syndicate' not in ' '.join(u['italian'] for u in cov)
   and 'Sindacato' in by[1]['italian'])
ck('nessun caporale, nessun carattere tipografico',
   not [u['idx'] for u in cov for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026' if c in u['italian']])
nonlat = [(u['idx'], c) for u in cov for c in u['italian'] if ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']],
   [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90 (0,92-1,53)',
   all(0.55 < u['ratio'] < 1.90 for u in cov),
   [(u['idx'], u['ratio']) for u in cov if not 0.55 < u['ratio'] < 1.90])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("65 unita' prima (L256 + L257 + L258), quindi la 222 prosegue Syndicate Orphan",
   db.execute('select count(*) from units where path=? and line<222', (PATH,)).fetchone()[0] == 65
   and db.execute('select context from units where path=? and line<222 order by line desc limit 1', (PATH,)).fetchone()
   == (CTX,))
ck("7 unita' dopo la 250",
   db.execute('select count(*) from units where path=? and line>250', (PATH,)).fetchone()[0] == 7)
ck('il file ha 87 unita, righe 40-264',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (87, 40, 264))
st = dict(db.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('tutte le 15 unita sono PENDING',
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
