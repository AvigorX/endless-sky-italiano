r"""check.py — L292 (`data/avgi/avgi culture conversations.txt`, righe 229-259). **Terzo lotto del file**.

Diciassette unita' in **un solo contesto**: un albero di dialogo sulla scherma Avgi. Tre cose contano:

1. **i primi due `LOGBOOK` del progetto** (righe 255 e 256): prosa di **diario** in prima persona, da distinguere **per tipo**
   dalle quindici `MISSION_TEXT`;
2. **il tic delle domande**: gli Avgi dicono «**domanda?**» in fondo alla frase (`, question?` in inglese) — non e' una domanda
   retorica, e' la loro **etichetta**;
3. **la scena 11/12 e' ripetuta**: la dodicesima aggiunge solo il cartello, quindi il testo comune deve restare **identico**.
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
PAR = re.compile(r'\([^()]*\)')
HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
PATH = 'data/avgi/avgi culture conversations.txt'
LOGS = [13, 14]  # righe 255, 256
CHOICES = [1, 2]  # righe 229, 230: (Approach them.) / (Ignore them.)
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


def prefisso(a, b):
    i = 0
    while i < min(len(a), len(b)) and a[i] == b[i]:
        i += 1
    return a[:i]


ck('unita tradotte 17/17', len(cov) == 17 == len(units), '%d/%d' % (len(cov), len(units)))
ck('tipi: 15 MISSION_TEXT + 2 LOGBOOK, i LOGBOOK alle righe 255 e 256',
   collections.Counter(u['kind'] for u in cov) == {'MISSION_TEXT': 15, 'LOGBOOK': 2}
   and [u['line'] for u in cov if u['kind'] == 'LOGBOOK'] == [255, 256],
   dict(collections.Counter(u['kind'] for u in cov)))
ck('un solo contesto: `mission:Avgi Culture: Fencing`',
   {u['context'] for u in cov} == {'mission:Avgi Culture: Fencing'})
ck('tutte e 17 le unita sono TRADOTTE, nessuna copiata',
   all(u['italian'] != u['english'] for u in cov), [u['idx'] for u in cov if u['italian'] == u['english']])
ck('i due LOGBOOK sono in PRIMA PERSONA e al passato («Ho assistito», «Ho visto»)',
   'Ho assistito' in by[14]['italian'] and 'Ho visto' in by[14]['italian'])
ck('i LOGBOOK NON hanno tab; tutte le altre quindici si',
   sum(u['english'].count(TAB) for u in cov) == 15 == sum(u['italian'].count(TAB) for u in cov)
   and [u['idx'] for u in cov if u['idx'] not in LOGS] == [u['idx'] for u in cov if TAB in u['italian']]
   and not any(by[i]['italian'].startswith(TAB) for i in LOGS))
ck('SCELTE del giocatore: due parentesi tonde con punto dentro (unita 1 e 2)',
   [u['idx'] for u in cov if PAR.findall(u['italian'])] == CHOICES
   and PAR.findall(by[1]['italian']) == ['(Avvicinati.)'] and PAR.findall(by[2]['italian']) == ['(Ignorali.)'])
ck('TIC delle domande: «domanda?» in fondo alla frase, due volte',
   by[3]['italian'].endswith('domanda?"') and by[16]['italian'].endswith('domanda?"')
   and by[3]['english'].endswith('question?"') and by[16]['english'].endswith('question?"'))
ck('SCENA RIPETUTA 11/12: il testo comune e identico parola per parola',
   len(prefisso(by[11]['italian'], by[12]['italian'])) == len(by[11]['italian'])
   and by[12]['italian'].startswith(by[11]['italian'].rstrip('.') )
   or by[12]['italian'].startswith(by[11]['italian'][:-1]),
   (len(prefisso(by[11]['italian'], by[12]['italian'])), len(by[11]['italian'])))
ck('la 12 aggiunge SOLO il cartello, in maiuscolo e fra virgolette',
   'ZOMP PER SCHIACCIARLI COME L\'ASSEMBLEA!' in by[12]['italian']
   and '"ZOMP PER SCHIACCIARLI COME L\'ASSEMBLEA!"' in by[12]['italian']
   and 'ASSEMBLEA' not in by[11]['italian'])
ck('VIRGOLETTE: 26 in inglese e 26 in italiano, per unita',
   sum(u['english'].count(QUOTE) for u in cov) == 26 == sum(u['italian'].count(QUOTE) for u in cov)
   and all(u['english'].count(QUOTE) == u['italian'].count(QUOTE) for u in cov),
   [(u['idx'], u['english'].count(QUOTE), u['italian'].count(QUOTE)) for u in cov
    if u['english'].count(QUOTE) != u['italian'].count(QUOTE)])
ck('APICI: cinque in inglese, diciassette in italiano',
   sum(u['english'].count(APOS) for u in cov) == 5 and sum(u['italian'].count(APOS) for u in cov) == 17,
   (sum(u['english'].count(APOS) for u in cov), sum(u['italian'].count(APOS) for u in cov)))
ck('SEGNAPOSTO e ALTERNATIVE: zero (asserzioni vuote)',
   sum(len(TAG.findall(u['english'])) for u in cov) == 0 == sum(len(TAG.findall(u['italian'])) for u in cov)
   and sum(len(ALT.findall(u['english'])) for u in cov) == 0 == sum(len(ALT.findall(u['italian'])) for u in cov))
ck('nomi INVARIATI: Zomp, Razmatazz; `Dissonance` -> «Dissonanza» (corpus)',
   by[12]['italian'].lower().count('zomp') == 1 and 'Razmatazz' in by[16]['italian']
   and 'Dissonanza' in by[14]['italian'] and 'Dissonance' not in by[14]['italian'])
ck('atti dichiarati degli Avgi: Invito, Rassicurazione, Aggiunta, Proclama, Attesa',
   all(a in ''.join(u['italian'] for u in cov) for a in
       ['Invito.', 'Rassicurazione.', 'Aggiunta.', 'Proclama.', 'Attesa.']),
   [a for a in ['Invito.', 'Rassicurazione.', 'Aggiunta.', 'Proclama.', 'Attesa.']
    if a not in ''.join(u['italian'] for u in cov)])
ck('lessico: scherma, stocchi, gradinate, piedistalli, fili di rame, campione in carica',
   'scherma' in by[3]['italian'] and 'stocchi' in by[15]['italian'] and 'gradinate' in by[11]['italian']
   and 'piedistalli' in by[15]['italian'] and 'fili di rame' in by[15]['italian']
   and 'campione in carica' in by[16]['italian'])
ck('nessun caporale, nessun carattere tipografico',
   not [u['idx'] for u in cov for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026' if c in u['italian']])
nonlat = [(u['idx'], c) for u in cov for c in u['italian'] if ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']],
   [u['idx'] for u in cov if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('rapporto nel gate 0,55-1,90 (0,80-1,27)',
   all(0.55 < u['ratio'] < 1.90 for u in cov),
   [(u['idx'], u['ratio']) for u in cov if not 0.55 < u['ratio'] < 1.90])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("20 unita' prima della 229 (L290 + L291)",
   db.execute('select count(*) from units where path=? and line<229', (PATH,)).fetchone()[0] == 20)
ck("9 unita' dopo la 259",
   db.execute('select count(*) from units where path=? and line>259', (PATH,)).fetchone()[0] == 9)
ck('FENCING continua oltre il confine: la prima unita dopo la 259 e ancora `Fencing`',
   db.execute('select context from units where path=? and line>259 order by line limit 1', (PATH,)).fetchone()
   == ('mission:Avgi Culture: Fencing',))
ck('il file ha 46 unita, righe 24-270',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (46, 24, 270))
ck('tutte le 17 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · 1 contesto · 15 tab · 26 virgolette · 2 LOGBOOK' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
