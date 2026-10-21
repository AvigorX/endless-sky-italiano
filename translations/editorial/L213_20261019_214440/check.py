r"""check.py — L213 (`data/human/deep jobs.txt`, 22 unita', righe 333-453). Secondo lotto del file.

**Primo lotto con `DIALOG`** (7 unità) accanto a 3 `DESCRIPTION` e 12 `TEXT`. I `DIALOG` sono prosa parlata di missione:
italiano naturale, **senza** l'inversione Saryd (non sono voci della Coalizione).

**Secondo blocco di frammenti** `phrase:secure package pickup` (unità 14-22): «Come da istruzioni, tu» + «ritiri il pacco
da un banco bagagli sorvegliato» + «in una zona tranquilla dello spazioporto.» + «È una cassa grande…». Quattro gruppi di
alternative, tutti da comporre: il controllo verifica la **maiuscola iniziale** e le alternative una per una.

**24 segnaposto** su 7 simboli (`<planet>` 7, `<payment>` 7, `<npc>` 4, `<stopovers>` 3, `<bunks>` 1, `<origin>` 1,
`<destination>` 1), confrontati **per unità**.

**Coerenza cross-lot**: «la struttura su <stopovers>» riprende l'unità 45 di L212, e «Il pagamento è <payment>» è la resa
fissata in L198.
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
src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
units = sorted(src['units'], key=lambda x: x['line'])
tr = {}
parts = sorted(f for f in os.listdir(os.path.join(HERE, 'parts')) if f.endswith('.json'))
for p in parts:
    for k, v in json.load(open(os.path.join(HERE, 'parts', p), encoding='utf-8')).items():
        tr[int(k)] = v
out = {'block': src['block'], 'note': src['note'], 'units': []}
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
IT_ALL = ' '.join(v['italian'] for v in cov)
EN_ALL = ' '.join(v['english'] for v in cov)
EN_T = sum(len(TAG.findall(v['english'])) for v in cov)
IT_T = sum(len(TAG.findall(v['italian'])) for v in cov)
EN_Q = sum(v['english'].count(QUOTE) for v in cov)
IT_Q = sum(v['italian'].count(QUOTE) for v in cov)
EN_A = sum(v['english'].count(APOS) for v in cov)
IT_A = sum(v['italian'].count(APOS) for v in cov)
KINDS = collections.Counter(u['kind'] for u in units)
CTX = collections.Counter(u['context'] for u in units)
PHRASE = [u['idx'] for u in units if u['context'].startswith('phrase:')]
DIALOG = [u['idx'] for u in units if u['kind'] == 'DIALOG']
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 22/22", len(cov) == 22 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 12 TEXT, 7 DIALOG, 3 DESCRIPTION (asserzione scritta)',
   KINDS == {'TEXT': 12, 'DIALOG': 7, 'DESCRIPTION': 3}, dict(KINDS))
ck('ZERO VALUE, LOGBOOK, MISSION_TEXT, UI_LABEL (asserzioni vuote scritte)',
   [u['idx'] for u in units if u['kind'] not in ('TEXT', 'DIALOG', 'DESCRIPTION')] == [])
ck('6 contesti, dal primo mission:Transport scientists a phrase:secure package pickup',
   len(CTX) == 6 and list(CTX)[0] == 'mission:Transport scientists'
   and list(CTX)[-1] == 'phrase:secure package pickup', '%d · %s' % (len(CTX), list(CTX)[-1]))
ck('righe 333 e 453 (prima e ultima del lotto)',
   (cov[0]['line'], cov[-1]['line']) == (333, 453), (cov[0]['line'], cov[-1]['line']))
ck('ZERO tab e ZERO virgolette in entrambe le lingue (asserzioni vuote scritte)',
   EN_Q == 0 == IT_Q and TAB not in ''.join(v['english'] + v['italian'] for v in cov), (EN_Q, IT_Q))
ck('24 segnaposto su 7 simboli, identici per unita\'',
   EN_T == 24 == IT_T
   and not [v['idx'] for v in cov
            if collections.Counter(TAG.findall(v['english'])) != collections.Counter(TAG.findall(v['italian']))],
   (EN_T, IT_T))
ck('la distribuzione dei simboli e\' quella misurata all\'export',
   collections.Counter(t for v in cov for t in TAG.findall(v['english']))
   == {'<planet>': 7, '<payment>': 7, '<npc>': 4, '<stopovers>': 3, '<bunks>': 1, '<origin>': 1,
       '<destination>': 1},
   collections.Counter(t for v in cov for t in TAG.findall(v['english'])))
ck('<npc> resta identico anche quando apre la frase o prende l\'articolo',
   by[6]['italian'].startswith("L'equipaggio della nave scientifica <npc>")
   and by[7]['italian'].startswith('La <npc>')
   and by[8]['italian'].count('<npc>') == 1)
ck("apici: 3 inglesi (unita' 1, 4, 8) e 9 italiani (unita' 1, 4, 6, 7, 10, 11)",
   EN_A == 3 and IT_A == 9
   and [v['idx'] for v in cov if APOS in v['english']] == [1, 4, 8]
   and [v['idx'] for v in cov if APOS in v['italian']] == [1, 4, 6, 7, 10, 11], (EN_A, IT_A))
ck('COMPOSIZIONE: i 12 frammenti `phrase:` conservano maiuscola o minuscola iniziale',
   not [v['idx'] for v in cov if v['idx'] in PHRASE
        and v['english'][0].isupper() != v['italian'][0].isupper()],
   [(v['idx'], v['english'][0], v['italian'][0]) for v in cov if v['idx'] in PHRASE
    and v['english'][0].isupper() != v['italian'][0].isupper()])
ck("i due frammenti d'apertura e le alternative sono resi come in L212",
   [by[i]['italian'] for i in (14, 15)] == ['Come da istruzioni, tu', 'Tu']
   and by[16]['italian'] != by[17]['italian'] and by[18]['italian'] != by[19]['italian']
   and len({by[i]['italian'] for i in (20, 21, 22)}) == 3)
ck('DIALOG: prosa parlata, nessuna inversione Saryd (nessuna chiusura con verbo in coda obbligatoria)',
   len(DIALOG) == 7 and 'Coalizione' not in ' '.join(by[i]['italian'] for i in DIALOG)
   and not [i for i in DIALOG if any(w in by[i]['italian'] for w in ('dall\'esterno', 'Heliarch', 'Saryd'))])
ck('coerenza con L212: «la struttura su <stopovers>» e «Il pagamento è <payment>»',
   'nella struttura su <stopovers>' in by[3]['italian']
   and by[13]['italian'].endswith('Il pagamento è <payment>.'))
ck('«science vessel» -> «nave scientifica», «escort» -> «scorta» (lessico fissato)',
   'nave scientifica <npc>' in by[6]['italian'] and 'una scorta' in by[6]['italian'])
ck('nessun caporale e nessun carattere tipografico',
   not [v['idx'] for v in cov if any(c in v['italian'] for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026')])
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' you ', ' to the ', ' will be ',
        ' is ', ' are ', ' from the ', ' its ', ' it is ', ' such as ', ' rather than ', ' for a ', ' that ')
ck('nessun residuo inglese', not [w for w in ENGW if w in IT_ALL.lower()],
   [w for w in ENGW if w in IT_ALL.lower()])
CORT = re.findall(r'\bLei\b|(?<![.!?] )\b(?:Suo|Sua|Suoi|Sue)\b', IT_ALL)
ck('nessuna forma di cortesia «Lei» (registro unico «tu»)', not CORT, CORT)
rs = [v['ratio'] for v in cov]
ck('rapporto nel gate 0,55-1,90', 0.55 < min(rs) and max(rs) < 1.90, '%.2f - %.2f' % (min(rs), max(rs)))
ACC = re.compile(r"\b(e|piu|perche|cosi|gia|puo|cioe|percio|fa)'", re.I)
bad = [(v['idx'], ACC.search(v['italian']).group(0)) for v in cov if ACC.search(v['italian'])]
ck('tipografia (accenti veri, nessun apostrofo al posto dell\'accento)', not bad, bad)
nonlat = [v['idx'] for v in cov for c in v['italian'] if ord(c) > 127 and not 0x00C0 <= ord(c) <= 0x024F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio',
   not [v['idx'] for v in cov if v['italian'] != v['italian'].rstrip()
        or '  ' in v['italian'] or v['english'] != v['english'].rstrip()])
c = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
st = dict(c.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('tutte le 22 unita sono PENDING (misurato)',
   c.execute('select count(*) from units where id in (%s) and state != "PENDING"'
             % ','.join('?' * len(units)), [u['id'] for u in units]).fetchone()[0] == 0)
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d' % (sum(len(v['english'].split()) for v in cov),
                                sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
