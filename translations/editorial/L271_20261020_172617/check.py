r"""check.py — L271 (`data/dialog phrases.txt`, righe 16-98). **Primo lotto del file**.

**29 `TEXT`** di frasi **generiche** delle missioni, in **20 contesti `phrase:`**. Tre cose da verificare con cura:

1. **le unita' 3-11 non sono frasi, sono FRAMMENTI** del `phrase "generic pirate attack payment dialog"`: si compongono per
   concatenazione **senza separatore** in sei blocchi alternativi (governo / ringraziamento o spazio / pagamento / modo /
   articolo / predone). Il controllo **compone tutte le 12 combinazioni** e verifica che nessuna abbia doppi spazi, spazio
   prima del punto o segnaposto persi;
2. **il blocco ` ` (riga 24) non e' nel database**: l'estrattore salta le stringhe di solo spazio bianco, quindi quel
   frammento **non e traducibile** e resta uno spazio. E' una **lacuna dichiarata dell'estrattore**, non un errore del
   lotto. La resa italiana e' costruita per funzionare **anche** con quello spazio;
3. **dieci famiglie di segnaposto**: i conteggi per famiglia devono essere **identici** fra inglese e italiano.
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
BLOCCHI = [('phrase:generic arrived-without-npc dialog', 16, 16),
           ('phrase:generic safe escort completion dialog', 19, 19),
           ('phrase:generic pirate attack payment dialog', 23, 37),
           ('phrase:generic cargo delivery payment', 41, 41),
           ('phrase:generic cargo on visit', 44, 44),
           ('phrase:generic passenger dropoff payment', 48, 49),
           ('phrase:generic passenger on visit', 52, 52),
           ('phrase:generic cargo and passenger on visit', 56, 56),
           ('phrase:generic mineral delivery payment', 60, 60),
           ('phrase:generic mineral on visit', 64, 64),
           ('phrase:generic missing stopover or cargo and passengers', 68, 68),
           ('phrase:generic missing stopover or passengers', 71, 71),
           ('phrase:generic missing stopover or cargo', 74, 74),
           ('phrase:generic missing stopover or escort', 77, 77),
           ('phrase:generic missing waypoint or cargo and passengers', 80, 80),
           ('phrase:generic missing waypoint or passengers', 83, 83),
           ('phrase:generic missing waypoint or cargo', 86, 86),
           ('phrase:generic stopover on visit', 90, 90),
           ('phrase:generic waypoint on visit', 93, 93),
           ('phrase:generic hunted bounty eliminated and payment dialog', 98, 98)]
FRAMMENTI = list(range(3, 12))
TOK = {'<planet>': 17, '<npc>': 4, '<payment>': 7, '<commodity>': 1, '<passengers>': 2,
       '<amount>': 2, '<mineral>': 2, '<origin>': 1, '<stopovers>': 5, '<waypoints>': 4}
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


def tok(u, k):
    return collections.Counter(TAG.findall(u[k]))


def composto():
    """Compone il phrase dei pirati come fa il gioco: blocchi concatenati SENZA separatore."""
    w1, w2, w3, w4, w5, w6 = by[3]['italian'], [' ', by[4]['italian']], by[5]['italian'], \
        [by[6]['italian'], by[7]['italian']], by[8]['italian'], [by[9]['italian'], by[10]['italian'], by[11]['italian']]
    return [w1 + a + w3 + b + w5 + c for a in w2 for b in w4 for c in w6]


ck('unita tradotte 29/29', len(cov) == 29 == len(units), '%d/%d' % (len(cov), len(units)))
ck('tipo: 29 TEXT, ne VALUE ne DESCRIPTION',
   collections.Counter(u['kind'] for u in units) == {'TEXT': 29},
   dict(collections.Counter(u['kind'] for u in units)))
ck('venti contesti `phrase:`, con le righe misurate',
   [(c, by[[u['idx'] for u in cov if u['context'] == c][0]]['line'],
     by[[u['idx'] for u in cov if u['context'] == c][-1]]['line']) for c, _, _ in BLOCCHI] == BLOCCHI,
   [(c, by[[u['idx'] for u in cov if u['context'] == c][0]]['line']) for c, _, _ in BLOCCHI])
ck('righe 16-98, nessun buco interno',
   [u['line'] for u in cov] == sorted({u['line'] for u in cov})
   and cov[0]['line'] == 16 and cov[-1]['line'] == 98)
ck('tutte TRADOTTE, nessuna copiata',
   all(u['italian'] != u['english'] for u in cov), [u['idx'] for u in cov if u['italian'] == u['english']])
ck('SEGNAPOSTO per famiglia: identici in inglese e in italiano (dieci famiglie, 45 token)',
   {t: sum(tok(u, 'english')[t] for u in cov) for t in TOK} == TOK
   == {t: sum(tok(u, 'italian')[t] for u in cov) for t in TOK},
   ({t: sum(tok(u, 'english')[t] for u in cov) for t in TOK},
    {t: sum(tok(u, 'italian')[t] for u in cov) for t in TOK}))
ck('nessun segnaposto INVENTATO e nessuno perso per unita',
   all(tok(by[i], 'english') == tok(by[i], 'italian') for i in by),
   [(i, dict(tok(by[i], 'english')), dict(tok(by[i], 'italian'))) for i in by
    if tok(by[i], 'english') != tok(by[i], 'italian')])
ck('FRAMMENTI del phrase dei pirati: 9 unita, 3-11, nello stesso contesto',
   [u['idx'] for u in cov if u['idx'] in FRAMMENTI] == FRAMMENTI
   and {u['context'] for u in cov if u['idx'] in FRAMMENTI} == {'phrase:generic pirate attack payment dialog'})
ck('COMPOSIZIONE: 12 combinazioni, nessun doppio spazio, nessuno spazio prima del punto, segnaposto intatti',
   len(composto()) == 12
   and not [s for s in composto() if '  ' in s or ' .' in s or ' ,' in s
            or not s.endswith('.') or s.count('<payment>') != 1 or s.count('<planet>') != 1
            or not s.startswith('Il governo di <planet>')],
   [s for s in composto() if '  ' in s or ' .' in s or s.count('<payment>') != 1])
ck('COMPOSIZIONE: tutte e 12 cominciano con la maiuscola e finiscono con il punto',
   all(s[0].isupper() and s.endswith('.') for s in composto()))
ck('il blocco ringraziamento porta lo spazio finale che serve alla concatenazione (spazio strutturale)',
   by[4]['italian'].endswith(' ') and by[4]['italian'].startswith(' ')
   and ' ti ringrazia sentitamente e ' == by[4]['italian'])
ck('i tre sostantivi finali vogliono tutti l articolo `i`',
   [by[i]['italian'] for i in (9, 10, 11)] == ['pirati.', 'predoni.', 'razziatori.']
   and by[8]['italian'] == 'i ')
ck('nessun tab, nessuna virgoletta (due asserzioni negative)',
   sum(u['english'].count(TAB) + u['italian'].count(TAB) for u in cov) == 0
   and sum(u['english'].count(QUOTE) + u['italian'].count(QUOTE) for u in cov) == 0)
ck('APICI: 17 in inglese su 10 unita, ZERO in italiano',
   sum(u['english'].count(APOS) for u in cov) == 17
   and {u['idx']: u['english'].count(APOS) for u in cov if APOS in u['english']}
   == {19: 1, 20: 2, 21: 2, 22: 2, 23: 2, 24: 2, 25: 2, 26: 2, 27: 1, 28: 1}
   and sum(u['italian'].count(APOS) for u in cov) == 0,
   (sum(u['english'].count(APOS) for u in cov), sum(u['italian'].count(APOS) for u in cov)))
ck('registro del giocatore: «Hai raggiunto» 13 volte, «Meglio ripartire» 6, «incassi il pagamento» 4',
   sum(1 for u in cov if u['italian'].startswith('Hai raggiunto')) == 13
   and sum(1 for u in cov if 'Meglio ripartire' in u['italian']) == 6
   and sum(1 for u in cov if 'incassi il pagamento di <payment>' in u['italian']) == 4,
   (sum(1 for u in cov if u['italian'].startswith('Hai raggiunto')),
    sum(1 for u in cov if 'Meglio ripartire' in u['italian']),
    sum(1 for u in cov if 'incassi il pagamento di <payment>' in u['italian'])))
ck('`<npc>` e una NAVE: femminile dove il testo lo richiede (unita 29 «e stata eliminata»)',
   'è stata eliminata' in by[29]['italian'])
ck('terminologia: tappa, punto di passaggio, stiva, scorte, tonnellate, carico',
   'scorte' in by[13]['italian'] and 'stiva' in by[19]['italian']
   and 'tonnellate' in by[18]['italian'] and 'carico' in by[12]['italian'])
ck('nessun caporale, nessun carattere tipografico',
   not [u['idx'] for u in cov for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026' if c in u['italian']])
nonlat = [(u['idx'], c) for u in cov for c in u['italian'] if ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessun doppio spazio; gli spazi finali esistono SOLO nei frammenti 4, 6, 7, 8 (strutturali)',
   not [u['idx'] for u in cov if '  ' in u['italian']]
   and sorted(u['idx'] for u in cov if u['italian'] != u['italian'].rstrip()) == [4, 6, 7, 8],
   [u['idx'] for u in cov if '  ' in u['italian'] or u['italian'] != u['italian'].rstrip()])
ck('rapporto nel gate 0,55-1,90 per le 20 unita che sono FRASI (i 9 frammenti sono esclusi e dichiarati)',
   all(0.55 < u['ratio'] < 1.90 for u in cov if u['idx'] not in FRAMMENTI),
   [(u['idx'], u['ratio']) for u in cov if u['idx'] not in FRAMMENTI and not 0.55 < u['ratio'] < 1.90])
ck('i frammenti fuori gate sono esattamente 4 (2,417) e 8 (0,50); gli altri sette stanno nel gate',
   [u['idx'] for u in cov if u['idx'] in FRAMMENTI and not 0.55 < u['ratio'] < 1.90] == [4, 8]
   and (by[4]['ratio'], by[8]['ratio']) == (2.417, 0.5))
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("ZERO unita' prima della 16: il lotto APRE il file",
   db.execute('select count(*) from units where path=? and line<16', (PATH,)).fetchone()[0] == 0)
ck("25 unita' dopo la 98", db.execute('select count(*) from units where path=? and line>98', (PATH,)).fetchone()[0] == 25)
ck('il file ha 54 unita, righe 16-172',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (54, 16, 172),
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone())
st = dict(db.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('tutte le 29 unita sono PENDING',
   all(db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] == 'PENDING' for u in cov))
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d · 20 contesti · 45 segnaposto in 10 famiglie' % (
    sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
