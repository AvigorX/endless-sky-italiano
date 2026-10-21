r"""check.py — L232 (`data/korath/korath outfits.txt`, 10 unita', righe 809-908). Quinto e ULTIMO lotto del file.

**Primo lotto della campagna con sole `DESCRIPTION`**: **zero `VALUE`**, quindi il confronto non e' «N identiche / M
tradotte» ma **0 identiche / 10 tradotte**, e l'asserzione e' che *nessuna* unita' resti identica all'inglese.

**I tab risalgono a 4** (erano 0 in L231): 809, 862, 880, 908, uno per unita', sempre iniziale. Quinto conteggio
consecutivo diverso nello stesso file: 0 (L228) · 3 (L229) · 7 (L230) · 0 (L231) · **4 (L232)**.

**Le virgolette tornano a 2** dopo sei lotti a zero, e stanno **tutte e due** nell'unita' 10 (`"escape,"`): la virgola
sta **dentro** le virgolette e si riproduce, non si sposta.

**5 apici in inglese contro 3 in italiano**, per ragioni opposte: l'inglese contrae (`engineers'`, `system's`, `aren't`,
`user's`, `won't`), l'italiano elide (`all'inefficienza`, `l'influenza`, `l'abbandono`). Il controllo elenca le unita',
non solo il totale (decisione 202).

**Lessico fissato**: `steering` -> «sistema di sterzata», `thruster` -> «propulsore», `rifle` -> «fucile»,
`world-ship` -> «nave-mondo», `airlock` -> «camera di equilibrio», `microbot` e `nutrigel` invariati come nomi di
prodotto, `jump drive` -> «motore di salto» (forma dominante del corpus: 334 contro 13; L231 unita' 19 aveva scritto
«jump drive», divergenza dichiarata in `review.md`).
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
PATH = 'data/korath/korath outfits.txt'
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
KINDS = collections.Counter(u['kind'] for u in units)
CTX = collections.Counter(u['context'] for u in units)
EN_A = [(v['idx'], v['english'].count(APOS)) for v in cov if APOS in v['english']]
IT_A = [(v['idx'], v['italian'].count(APOS)) for v in cov if APOS in v['italian']]
EN_T = [(v['idx'], v['english'].count(TAB)) for v in cov if TAB in v['english']]
IT_T = [(v['idx'], v['italian'].count(TAB)) for v in cov if TAB in v['italian']]
EN_Q = [(v['idx'], v['english'].count(QUOTE)) for v in cov if QUOTE in v['english']]
IT_Q = [(v['idx'], v['italian'].count(QUOTE)) for v in cov if QUOTE in v['italian']]
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 10/10", len(cov) == 10 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 10 DESCRIPTION', KINDS == {'DESCRIPTION': 10}, dict(KINDS))
ck('ZERO VALUE, TEXT, DIALOG, MISSION_TEXT, LOGBOOK, NEWS, UI_LABEL (asserzioni vuote scritte)',
   [u['idx'] for u in units if u['kind'] != 'DESCRIPTION'] == [])
ck('7 contesti con i conteggi misurati (Gaktem, Nelmeb e Microbot hanno 2 unita\', gli altri 1)',
   len(CTX) == 7 and CTX == {'outfit:Nelmeb GP Hybrid Thruster': 1, 'outfit:Arkrof GP Hybrid Steering': 1,
                             'outfit:Farves GP Hybrid Steering': 1, 'outfit:Gaktem GP Hybrid Steering': 2,
                             'outfit:Nelmeb GP Hybrid Steering': 2, 'outfit:Thermal Repeater Rifle': 1,
                             'outfit:Microbot Defense Station': 2}, dict(CTX))
ck('righe 809 e 908 (prima e ultima del lotto, 908 e\' l\'ultima del FILE)',
   (cov[0]['line'], cov[-1]['line']) == (809, 908), (cov[0]['line'], cov[-1]['line']))
ck('4 tab nel lotto, uno per unita\' (809, 862, 880, 908), sempre iniziali, uguali in inglese e italiano',
   sum(n for _, n in EN_T) == 4 == sum(n for _, n in IT_T)
   and EN_T == [(1, 1), (5, 1), (7, 1), (10, 1)] and EN_T == IT_T,
   (EN_T, IT_T))
ck('2 virgolette, entrambe nell\'unita\' 10 (`"escape,"`), uguali in inglese e italiano',
   sum(n for _, n in EN_Q) == 2 == sum(n for _, n in IT_Q)
   and EN_Q == [(10, 2)] and EN_Q == IT_Q, (EN_Q, IT_Q))
ck('NESSUN segnaposto (asserzione negativa scritta)',
   sum(len(TAG.findall(v['english'])) for v in cov) == 0 == sum(len(TAG.findall(v['italian'])) for v in cov))
ck('0 unita\' IDENTICHE all\'inglese e 10 tradotte (primo lotto di sole DESCRIPTION)',
   sum(1 for v in cov if v['italian'] == v['english']) == 0
   and sum(1 for v in cov if v['italian'] != v['english']) == 10,
   sum(1 for v in cov if v['italian'] == v['english']))
ck('nomi di scena invariati: Quarg 3, Efreti 8, Korath 10 (stessi conteggi dell\'inglese)',
   IT_ALL.count('Quarg') == EN_ALL.count('Quarg') == 3
   and IT_ALL.count('Efreti') == EN_ALL.count('Efreti') == 8
   and IT_ALL.count('Korath') == EN_ALL.count('Korath') == 10
   and not re.search(r'Quarg[a-z]+|Efreti[a-z]+|Korath[a-z]+', IT_ALL),
   (IT_ALL.count('Quarg'), IT_ALL.count('Efreti'), IT_ALL.count('Korath')))
ck('termine del file: `Thermal Repeater` (nome) invariato, `rifle` -> «fucile» (2)',
   'Thermal Repeater' in IT_ALL and IT_ALL.count('fucile') == 2 and 'rifle' not in IT_ALL)
ck('la coppia thruster/steering resta distinta: «propulsori» e «sistema di sterzata» (3)',
   'propulsori' in IT_ALL and IT_ALL.count('sistema di sterzata') == 3
   and 'thruster' not in IT_ALL and 'steering' not in IT_ALL)
ck('terminologia tecnica: «gravitoplasma» 3, «propulsione gravitazionale» 2, «gravità quantistica» 1',
   IT_ALL.count('gravitoplasma') == 3 and IT_ALL.count('propulsione gravitazionale') == 2
   and IT_ALL.count('gravità quantistica') == 1)
ck('lessico di L231 ripreso: «tristemente inefficiente», «coppia torcente», «reattori a fusione», '
   '«produzione di calore»',
   'tristemente inefficiente' in IT_ALL and 'coppia torcente' in IT_ALL
   and 'reattori a fusione' in IT_ALL and 'produzione di calore' in IT_ALL)
ck('la scheda dei microbot: «nave-mondo», «camera di equilibrio», «microbot» 2, «nutrigel», «vasca»',
   'nave-mondo' in IT_ALL and 'camera di equilibrio' in IT_ALL and IT_ALL.count('microbot') == 2
   and 'nutrigel' in IT_ALL and 'vasca' in IT_ALL
   and 'World-Ships' not in IT_ALL and 'airlock' not in IT_ALL)
ck('lessico del fucile: «plasma surriscaldato» e «cannibalismo»/«tabù»/«multe salate»',
   'plasma surriscaldato' in IT_ALL and 'cannibalismo' in IT_ALL and 'tabù' in IT_ALL
   and 'multe salate' in IT_ALL)
ck('nessun residuo inglese di struttura (the, of the, and, with, their, while)',
   not [w for w in (' the ', ' of the ', ' and ', ' with ', ' their ', ' while ')
        if w in IT_ALL.lower()],
   [w for w in (' the ', ' of the ', ' and ', ' with ', ' their ', ' while ') if w in IT_ALL.lower()])
ck("apici: 5 in inglese (3:1, 5:1, 8:3) e 3 in italiano (1, 3, 6) — l'inglese contrae, l'italiano elide",
   sum(n for _, n in EN_A) == 5 and sum(n for _, n in IT_A) == 3
   and EN_A == [(3, 1), (5, 1), (8, 3)] and IT_A == [(1, 1), (3, 1), (6, 1)], (EN_A, IT_A))
ck('registro: nessun «Lei» e nessun «mi scusi»', not re.search(r'\bLei\b|mi scusi', IT_ALL))
ck('nessun caporale e nessun carattere tipografico',
   not [v['idx'] for v in cov if any(c in v['italian'] for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026')])
rs = [v['ratio'] for v in cov]
ck('rapporto nel gate 0,55-1,90 (1,04-1,25; 454 -> 508 parole)',
   0.55 < min(rs) and max(rs) < 1.90, '%.2f - %.2f' % (min(rs), max(rs)))
ACC = re.compile(r"\b(e|piu|perche|cosi|gia|puo|cioe|percio|fa)'", re.I)
bad = [(v['idx'], ACC.search(v['italian']).group(0)) for v in cov if ACC.search(v['italian'])]
ck("tipografia (accenti veri, nessun apostrofo al posto dell'accento)", not bad, bad)
nonlat = [v['idx'] for v in cov for c in v['italian'] if ord(c) > 127 and not 0x00C0 <= ord(c) <= 0x024F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio',
   not [v['idx'] for v in cov if v['italian'] != v['italian'].rstrip()
        or '  ' in v['italian'] or v['english'] != v['english'].rstrip()])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck('82 unita tradotte prima della 809 (L228-L231: 20+15+26+21)',
   db.execute('select count(*) from units where path=? and line<809', (PATH,)).fetchone()[0] == 82)
ck('ZERO unita dopo la 908: il lotto chiude il file',
   db.execute('select count(*) from units where path=? and line>908', (PATH,)).fetchone()[0] == 0)
ck('lotto + tradotte prima = file: 10 + 82 = 92',
   10 + db.execute('select count(*) from units where path=? and line<809', (PATH,)).fetchone()[0] == 92)
ck('il file intero: 92 unita, righe 16 - 908',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (92, 16, 908))
st = dict(db.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('le 10 unita sono PENDING (misurato)',
   db.execute('select count(*) from units where id in (%s) and state != "PENDING"'
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
