r"""check.py — L293 (`data/avgi/avgi culture conversations.txt`, righe 260-270). **LOTTO TERMINALE del file**.

Nove unita' che chiudono il duello e il file: verifica l'**invariante di FILE** e tre cose del testo:

1. **gli atti dichiarati** degli Avgi continuano («Stupore.», «Riposo.», «Sconcerto.», «Isteria.», «Adorazione!»), con
   «Adorazione!» al **punto esclamativo** come nel sorgente;
2. **la scommessa** (`I'm up 10 to 1`): numeri e senso conservati — «dieci a uno»;
3. **tutte e nove le unita' sono rientrate** (9 tab su 9), cosa che finora era capitata solo in parte.
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
ALT = re.compile(r'\[[^\]]*\]')
HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
PATH = 'data/avgi/avgi culture conversations.txt'
LINES = [260, 261, 262, 263, 264, 265, 266, 267, 270]
ATTI = ['Stupore.', 'Riposo.', 'Sconcerto.', 'Isteria.', 'Adorazione!']
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
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck('unita tradotte 9/9', len(cov) == 9 == len(units), '%d/%d' % (len(cov), len(units)))
ck('tutte MISSION_TEXT, righe tutte quelle dichiarate (260-267 e 270)',
   {u['kind'] for u in cov} == {'MISSION_TEXT'} and [u['line'] for u in cov] == LINES,
   [u['line'] for u in cov])
ck('un solo contesto: `mission:Avgi Culture: Fencing`',
   {u['context'] for u in cov} == {'mission:Avgi Culture: Fencing'})
ck('tutte e 9 le unita sono TRADOTTE, nessuna copiata',
   all(u['italian'] != u['english'] for u in cov), [u['idx'] for u in cov if u['italian'] == u['english']])
ck('TAB: nove su nove, come PRIMO carattere',
   sum(u['english'].count(TAB) for u in cov) == 9 == sum(u['italian'].count(TAB) for u in cov)
   and all(u['italian'].startswith(TAB) for u in cov))
ck('ATTI dichiarati: Stupore, Riposo, Sconcerto, Isteria, Adorazione!',
   [a for a in ATTI if a in ''.join(u['italian'] for u in cov)] == ATTI,
   [a for a in ATTI if a not in ''.join(u['italian'] for u in cov)])
ck('«Adorazione!» con il punto ESCLAMATIVO, come nel sorgente',
   '"Adorazione! Ti amo, Zomp!"' in by[6]['italian'] and 'Adoration!' in by[6]['english'])
ck('la SCOMMESSA: «dieci a uno», e il numero resta',
   'dieci a uno' in by[5]['italian'] and '10 to 1' in by[5]['english'])
ck('VIRGOLETTE: dieci in inglese e dieci in italiano, per unita',
   sum(u['english'].count(QUOTE) for u in cov) == 10 == sum(u['italian'].count(QUOTE) for u in cov)
   and all(u['english'].count(QUOTE) == u['italian'].count(QUOTE) for u in cov),
   [(u['idx'], u['english'].count(QUOTE), u['italian'].count(QUOTE)) for u in cov
    if u['english'].count(QUOTE) != u['italian'].count(QUOTE)])
ck('APICI: cinque in inglese, quattordici in italiano',
   sum(u['english'].count(APOS) for u in cov) == 5 and sum(u['italian'].count(APOS) for u in cov) == 14,
   (sum(u['english'].count(APOS) for u in cov), sum(u['italian'].count(APOS) for u in cov)))
ck('SEGNAPOSTO e ALTERNATIVE: zero (asserzioni vuote)',
   sum(len(TAG.findall(u['english'])) for u in cov) == 0 == sum(len(TAG.findall(u['italian'])) for u in cov)
   and sum(len(ALT.findall(u['english'])) for u in cov) == 0 == sum(len(ALT.findall(u['italian'])) for u in cov))
ck('nomi INVARIATI: Zomp, e `campione in carica` coerente con L292',
   by[4]['italian'].count('Zomp') == 1 and by[6]['italian'].count('Zomp') == 1
   and 'campione in carica' in by[4]['italian'])
ck('lessico: annunciatore, lame, portata, ala ripiegata, applausi tonanti, carte rosa',
   "dell'annunciatore" in by[1]['italian'] and 'lame' in by[1]['italian']
   and 'portata' in by[1]['italian'] and 'ala ripiegata' in by[1]['italian']
   and 'applausi tonanti' in by[3]['italian'] and 'carte rosa' in by[5]['italian'])
ck('nessun caporale, nessun carattere tipografico',
   not [u['idx'] for u in cov for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026' if c in u['italian']])
nonlat = [(u['idx'], c) for u in cov for c in u['italian'] if ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']],
   [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90 (0,95-1,31)',
   all(0.55 < u['ratio'] < 1.90 for u in cov),
   [(u['idx'], u['ratio']) for u in cov if not 0.55 < u['ratio'] < 1.90])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck('FILE: 37 unita prima della 260 (8 + 12 + 17)',
   db.execute('select count(*) from units where path=? and line<260', (PATH,)).fetchone()[0] == 37)
ck('FILE: ZERO unita dopo la 270 — il lotto CHIUDE il file',
   db.execute('select count(*) from units where path=? and line>270', (PATH,)).fetchone()[0] == 0)
ck('FILE: 46 unita, righe 24-270, 44 MISSION_TEXT + 2 LOGBOOK',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (46, 24, 270)
   and dict(db.execute('select kind,count(*) from units where path=? group by kind', (PATH,)).fetchall())
   == {'MISSION_TEXT': 44, 'LOGBOOK': 2})
ck('FILE: i quattro lotti sommano 46 (8 + 12 + 17 + 9)',
   8 + 12 + 17 + 9 == 46
   and db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0] == 46)
ck('tutte le 9 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · 1 contesto · 9 tab · 10 virgolette · FILE 46/46' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
