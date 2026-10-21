r"""check.py — L231 (`data/korath/korath outfits.txt`, 21 unita', righe 596-808). Quarto lotto del file.

**8 `VALUE` e 13 `DESCRIPTION`**: confronto **8 identiche / 13 tradotte**, con il controllo che verifica *quali* unita' sono
identiche (tutti e soli i `VALUE`).

**Zero tab e zero virgolette**, in inglese e in italiano. I tab erano 7 in L230: il conteggio si misura sul lotto.

**Nuovi nomi di scena**: **Quarg** (la specie che guarda i Korath con disapprovazione) ed **Efreti** (gli ingegneri Korath
che sviluppano i propulsori ibridi). Restano invariati, come `Kor Efret`, `Mereti`, `Kor Sestor`.

**Il primo lotto della campagna con `ratio` massimo 1,37**: la frase dei Quarg che credono la nave in fin di vita si allunga
in italiano, e resta nel gate.
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
KINDS = collections.Counter(u['kind'] for u in units)
CTX = collections.Counter(u['context'] for u in units)
VALS = [u['idx'] for u in units if u['kind'] == 'VALUE']
DESCS = [u['idx'] for u in units if u['kind'] == 'DESCRIPTION']
EN_A = [(v['idx'], v['english'].count(APOS)) for v in cov if APOS in v['english']]
IT_A = [(v['idx'], v['italian'].count(APOS)) for v in cov if APOS in v['italian']]
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 21/21", len(cov) == 21 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 13 DESCRIPTION e 8 VALUE', KINDS == {'DESCRIPTION': 13, 'VALUE': 8}, dict(KINDS))
ck('ZERO TEXT, DIALOG, MISSION_TEXT, LOGBOOK, NEWS, UI_LABEL (asserzioni vuote scritte)',
   [u['idx'] for u in units if u['kind'] not in ('DESCRIPTION', 'VALUE')] == [])
ck('13 contesti con i conteggi misurati (Comet Thruster e i quattro GP ibridi hanno 1 unita\', gli altri 2)',
   len(CTX) == 13 and CTX == {'outfit:Thruster (Comet Class)': 1, 'outfit:Thruster (Lunar Class)': 2,
                              'outfit:Thruster (Planetary Class)': 2, 'outfit:Thruster (Stellar Class)': 2,
                              'outfit:Steering (Asteroid Class)': 2, 'outfit:Steering (Comet Class)': 2,
                              'outfit:Steering (Lunar Class)': 2, 'outfit:Steering (Planetary Class)': 2,
                              'outfit:Steering (Stellar Class)': 2, 'outfit:Arkrof GP Hybrid Thruster': 1,
                              'outfit:Farves GP Hybrid Thruster': 1, 'outfit:Gaktem GP Hybrid Thruster': 1,
                              'outfit:Nelmeb GP Hybrid Thruster': 1}, dict(CTX))
ck('righe 596 e 808 (prima e ultima del lotto)',
   (cov[0]['line'], cov[-1]['line']) == (596, 808), (cov[0]['line'], cov[-1]['line']))
ck('ZERO tab nel lotto (erano 7 in L230: il conteggio si misura, non si eredita)',
   sum(v['english'].count(TAB) for v in cov) == 0 == sum(v['italian'].count(TAB) for v in cov))
ck('ZERO virgolette in inglese e in italiano (sesto lotto consecutivo)',
   sum(v['english'].count(QUOTE) for v in cov) == 0 == sum(v['italian'].count(QUOTE) for v in cov))
ck('NESSUN segnaposto (asserzione negativa scritta)',
   sum(len(TAG.findall(v['english'])) for v in cov) == 0 == sum(len(TAG.findall(v['italian'])) for v in cov))
ck('8 unita\' IDENTICHE all\'inglese (tutti e soli i VALUE) e 13 tradotte (tutte e sole le DESCRIPTION)',
   sum(1 for v in cov if v['italian'] == v['english']) == 8
   and sorted(v['idx'] for v in cov if v['italian'] == v['english']) == VALS
   and sorted(v['idx'] for v in cov if v['italian'] != v['english']) == DESCS,
   (sorted(v['idx'] for v in cov if v['italian'] == v['english']), VALS))
ck('gli 8 VALUE copiati alla lettera («Thrusters (Lunar Class)», «Steerings (Stellar Class)»…)',
   VALS == [2, 4, 6, 8, 10, 12, 14, 16]
   and by[2]['italian'] == 'Thrusters (Lunar Class)' and by[16]['italian'] == 'Steerings (Stellar Class)')
ck('nomi di scena invariati: Quarg (5) ed Efreti (5), mai tradotti',
   IT_ALL.count('Quarg') == 5 and IT_ALL.count('Efreti') == 5,
   (IT_ALL.count('Quarg'), IT_ALL.count('Efreti')))
ck('la coppia thruster/steering è resa con due termini distinti: «propulsore» e «sistema di sterzata»',
   'propulsore' in IT_ALL and 'sistema di sterzata' in IT_ALL
   and by[9]['italian'].count('sterzata') >= 1 and by[3]['italian'].count('propulsione') >= 1)
ck('terminologia tecnica: «calore disperso», «propulsione gravitazionale», «gravitoplasma», «gravità quantistica»',
   'calore disperso' in IT_ALL and 'propulsione gravitazionale' in IT_ALL
   and 'gravitoplasma' in IT_ALL and 'gravità quantistica' in IT_ALL)
ck('nessun residuo inglese di struttura (the, of the, and, with, their)',
   not [w for w in (' the ', ' of the ', ' and ', ' with ', ' their ', ' while ', ' that they ')
        if w in IT_ALL.lower()],
   [w for w in (' the ', ' of the ', ' and ', ' with ', ' their ', ' while ', ' that they ') if w in IT_ALL.lower()])
ck("apici: 2 in inglese (1 thruster's, 20 Efreti's) e 6 in italiano su 5 unita'",
   sum(n for _, n in EN_A) == 2 and sum(n for _, n in IT_A) == 6
   and EN_A == [(1, 1), (20, 1)]
   and IT_A == [(3, 1), (7, 1), (15, 2), (18, 1), (21, 1)], (EN_A, IT_A))
ck('registro: nessun «Lei» e nessun «mi scusi»', not re.search(r'\bLei\b|mi scusi', IT_ALL))
ck('nessun caporale e nessun carattere tipografico',
   not [v['idx'] for v in cov if any(c in v['italian'] for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026')])
rs = [v['ratio'] for v in cov]
ck('rapporto nel gate 0,55-1,90 (1,00 per i nomi, 1,04-1,37 per le DESCRIPTION)',
   0.55 < min(rs) and max(rs) < 1.90, '%.2f - %.2f' % (min(rs), max(rs)))
ACC = re.compile(r"\b(e|piu|perche|cosi|gia|puo|cioe|percio|fa)'", re.I)
bad = [(v['idx'], ACC.search(v['italian']).group(0)) for v in cov if ACC.search(v['italian'])]
ck('tipografia (accenti veri, nessun apostrofo al posto dell\'accento)', not bad, bad)
nonlat = [v['idx'] for v in cov for c in v['italian'] if ord(c) > 127 and not 0x00C0 <= ord(c) <= 0x024F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio',
   not [v['idx'] for v in cov if v['italian'] != v['italian'].rstrip()
        or '  ' in v['italian'] or v['english'] != v['english'].rstrip()])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck('61 unita tradotte prima della 596 (L228-L230)',
   db.execute('select count(*) from units where path=? and line<596', (PATH,)).fetchone()[0] == 61)
ck('lotto + residuo = file: 61 + 21 + 10 = 92',
   61 + 21 + db.execute('select count(*) from units where path=? and line>808', (PATH,)).fetchone()[0] == 92)
ck("il residuo dopo la 808 e' di 10 unita', TUTTE DESCRIPTION e nessun VALUE: "
   "L232 chiudera' il file con 0 identiche / 10 tradotte",
   db.execute('select count(*) from units where path=? and line>808', (PATH,)).fetchone()[0] == 10
   and db.execute('select count(*) from units where path=? and line>808 and kind="VALUE"',
                  (PATH,)).fetchone()[0] == 0)
st = dict(db.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('le 21 unita sono PENDING (misurato)',
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
