r"""check.py — L246 (`data/hai/hai ships.txt`, 37 unita', righe 1517-1860). **LOTTO TERMINALE**: chiude il file.

**Invariante di FILE**: dopo questo lotto `hai ships.txt` deve avere **157 unita' distinte su 157**, `29 + 45 + 46 + 37`,
la riga **1860** come ultima e **0** unita' dopo.

**Due tab**, uno per volta: unita' 1 (secondo paragrafo dell'Emperor Beetle) e unita' 24 (la nota sui caccia). Entrambi
conservati come **primo carattere** in inglese e in italiano.

**66 virgolette**: 2 per i 32 nomi + 2 intorno a `"Giftbringer,"` nella scheda della Solifuge. Confronto **per unita'**.

**La nota sui caccia non e' inventata**: la stringa inglese compare in **8 lotti precedenti**, e la resa corretta e' quella
**dominante** (6 su 8). Il `check.py` la confronta con la forma piu' frequente del corpus, non con la mia memoria.
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
PATH = 'data/hai/hai ships.txt'
FNOTE_EN = TAB + 'Fighters do not come equipped with a hyperdrive. You cannot carry a fighter unless you have a ship in your fleet with a fighter bay.'
DNOTE_EN = TAB + 'Drones do not come equipped with a hyperdrive. You cannot carry a drone unless you have a ship in your fleet with a drone bay.'
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
KINDS = collections.Counter(u['kind'] for u in units)
DATA = [v for v in cov if v['kind'] in ('VALUE', 'TEXT')]
DES = [v for v in cov if v['kind'] == 'DESCRIPTION']
TAB_UNITS = [(v['idx'], v['english'].count(TAB), v['italian'].count(TAB)) for v in cov
             if TAB in v['english'] or TAB in v['italian']]
Q_EN = [(v['idx'], v['english'].count(QUOTE)) for v in cov if QUOTE in v['english']]
Q_IT = [(v['idx'], v['italian'].count(QUOTE)) for v in cov if QUOTE in v['italian']]
A_EN = [(v['idx'], v['english'].count(APOS)) for v in cov if APOS in v['english']]
A_IT = [(v['idx'], v['italian'].count(APOS)) for v in cov if APOS in v['italian']]
ctx = collections.Counter(u['context'] for u in units)
prosa = ' '.join(v['italian'] for v in DES)
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


def corpus(english):
    """Tutte le rese gia' presenti nel corpus per questa stringa inglese, con l'occorrenza."""
    c = collections.Counter()
    for f in glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json')):
        if os.path.basename(os.path.dirname(f)) == os.path.basename(HERE):
            continue
        for u in json.load(open(f, encoding='utf-8'))['units']:
            if u['english'] == english:
                c[u['italian']] += 1
    return c


ck("unita' tradotte 37/37", len(cov) == 37 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna unita\' vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 32 TEXT + 5 DESCRIPTION e NESSUN VALUE',
   dict(KINDS) == {'TEXT': 32, 'DESCRIPTION': 5} and 'VALUE' not in KINDS, dict(KINDS))
ck('4 contesti: Emperor Beetle 1, Solifuge 19, Violin Spider 6, Water Bug 11',
   dict(ctx) == {'ship:Emperor Beetle': 1, 'ship:Solifuge': 19, 'ship:Violin Spider': 6,
                 'ship:Water Bug': 11}, dict(ctx))
ck('righe 1517 e 1860 (prima e ultima del lotto)',
   (cov[0]['line'], cov[-1]['line']) == (1517, 1860), (cov[0]['line'], cov[-1]['line']))
ck("i DUE tab stanno all'inizio delle unita' 1 e 24, in inglese e in italiano",
   TAB_UNITS == [(1, 1, 1), (24, 1, 1)] and cov[0]['italian'][0] == TAB and cov[23]['italian'][0] == TAB,
   TAB_UNITS)
ck('i due paragrafi col tab sono tradotti, non copiati',
   cov[0]['italian'] != cov[0]['english'] and cov[23]['italian'] != cov[23]['english']
   and 'More than just a ship' not in cov[0]['italian'] and 'Fighters do not' not in cov[23]['italian'])
ck("i 32 TEXT sono IDENTICI all'inglese, per indice",
   all(v['italian'] == v['english'] for v in DATA) and len(DATA) == 32,
   [v['idx'] for v in DATA if v['italian'] != v['english']])
ck("le 5 DESCRIPTION sono TUTTE tradotte (0 identiche)",
   all(v['italian'] != v['english'] for v in DES) and len(DES) == 5)
ck('66 virgolette: 2 per unita\' su 33 unita\' (32 nomi + il "Giftbringer")',
   Q_EN == Q_IT and len(Q_IT) == 33 and set(n for _, n in Q_IT) == {2}
   and sum(n for _, n in Q_IT) == 66, (len(Q_EN), len(Q_IT)))
ck('il nome fra virgolette e\' `"Giftbringer"`, tradotto il resto e non il nome',
   '"Giftbringer"' in prosa and 'Giftbringer' not in ' '.join(
       v['italian'] for v in DES if v['idx'] != 5))
ck("apici: 2 in inglese (unita' 1 e 5, possessivi) e 5 in italiano (unita' 1 e 30, elisioni)",
   A_EN == [(1, 1), (5, 1)] and A_IT == [(1, 2), (30, 3)], (A_EN, A_IT))
ck("nessun possessivo inglese sopravvive ('s o s' finali)",
   not [v['idx'] for v in cov if "'s " in v['italian'] or "s' " in v['italian']])
# --- coerenza cross-lot: la nota si riproduce, non si reinventa ---
cf = corpus(FNOTE_EN)
ck("la nota sui caccia e' la resa DOMINANTE del corpus (%d lotti la contengono, %d forme)"
   % (sum(cf.values()), len(cf)),
   len(cf) >= 2 and cf.most_common(1)[0][0] == cov[23]['italian'],
   (cf.most_common(2), cov[23]['italian']))
cd = corpus(DNOTE_EN)
ck('la nota sui droni (L244) coincide con la resa dominante del corpus',
   len(cd) >= 1 and len(cd.most_common(1)[0][0]) > 0 and cd.most_common(1)[0][0].strip().startswith('I droni non sono dotati di iperguida'),
   cd.most_common(2))
# Conteggio misurato **per nome**. Gli zeri sono fatti, non sviste: la scheda della Solifuge parla del «Giftbringer»
# degli Alphas e quella della Violin Spider dice «the Hai fighter», quindi nessuna delle due nomina la nave.
ATTESI = {'Emperor Beetle': 1, 'Shield Beetle': 1, 'Solifuge': 0, 'Violin Spider': 0, 'Water Bug': 1,
          'Aphid': 1, 'Alphas': 1, 'Giftbringer': 1}
misurati = {n: sum(1 for v in DES if n in v['english']) for n in ATTESI}
persi = [(v['idx'], n) for v in DES for n in ATTESI if n in v['english'] and n not in v['italian']]
ck('ogni nome proprio che l\'inglese nomina resta in italiano (%d unita\'-nome, 0 perse)'
   % sum(ATTESI.values()), misurati == ATTESI and not persi, (misurati, persi))
ck('lessico: «Slegati», «porta-caccia», «motori di salto», «baia di caccia», «mercante/mercantile»',
   all(t in prosa for t in ('Slegati', 'porta-caccia', 'motori di salto', 'baia di caccia', 'mercantile')))
ck("`Unfettered` non compare mai in italiano (resa «Slegati»)",
   'Unfettered' not in ' '.join(v['italian'] for v in cov))
ck('nessuna virgoletta fuori dalle 33 unita\' attese e nessun tab fuori dalle 2',
   sum(v['italian'].count(QUOTE) for v in cov) == 66 and sum(v['italian'].count(TAB) for v in cov) == 2)
ck("NESSUN segnaposto (asserzione negativa scritta)",
   sum(len(TAG.findall(v['english'])) for v in cov) == 0 == sum(len(TAG.findall(v['italian'])) for v in cov))
ck('nessun residuo inglese di struttura (the, and, with, that, from)',
   not [w for w in (' the ', ' and ', ' with ', ' that ', ' from ') if w in prosa.lower()],
   [w for w in (' the ', ' and ', ' with ', ' that ', ' from ') if w in prosa.lower()])
ck('registro: nessun «Lei» e nessuna cortesia',
   not re.search(r'\bLei\b|\bSuo\b|\bSua\b|mi scusi', ' '.join(v['italian'] for v in cov)))
ck('nessun caporale e nessun carattere tipografico',
   not [v['idx'] for v in cov if any(c in v['italian'] for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026')])
rs = [v['ratio'] for v in cov]
ck('rapporto nel gate 0,55-1,90 (0,99-1,23; 327 -> 324 parole)',
   0.55 < min(rs) and max(rs) < 1.90, '%.2f - %.2f' % (min(rs), max(rs)))
ACC = re.compile(r"\b(e|piu|perche|cosi|gia|puo|cioe|percio)'(?![a-z])", re.I)
bad = [(v['idx'], ACC.search(v['italian']).group(0)) for v in cov if ACC.search(v['italian'])]
ck("tipografia (accenti veri, nessun apostrofo al posto dell'accento)", not bad, bad)
nonlat = [v['idx'] for v in cov for c in v['italian'] if ord(c) > 127 and not 0x00C0 <= ord(c) <= 0x024F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio',
   not [v['idx'] for v in cov if v['italian'] != v['italian'].rstrip() or '  ' in v['italian']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ck("120 unita' prima della 1517 (L243 29 + L244 45 + L245 46)",
   db.execute('select count(*) from units where path=? and line<1517', (PATH,)).fetchone()[0] == 120)
ck("ZERO unita' dopo la 1860: il lotto CHIUDE il file",
   db.execute('select count(*) from units where path=? and line>1860', (PATH,)).fetchone()[0] == 0)
ck('il file intero: 157 unita, righe 15 - 1860',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (157, 15, 1860))
righe_lotti, n_lotti = set(), []
for _f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    _us = [u for u in json.load(open(_f, encoding='utf-8'))['units'] if u['path'] == PATH]
    if _us:
        n_lotti.append(len(_us))
        righe_lotti |= {u['line'] for u in _us}
ck('INVARIANTE DI FILE: 4 lotti (29 + 45 + 46 + 37) coprono 157 righe distinte su 157',
   29 + 45 + 46 + 37 == 157 and sum(n_lotti) == 157 == len(righe_lotti) and len(n_lotti) == 4,
   (n_lotti, len(righe_lotti)))
st = dict(db.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('le 37 unita sono PENDING (misurato)',
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
