r"""check.py — L203 (`data/hai/hai outfits.txt`, 9 unita', righe 508-600). Terzo lotto del file.

**9 `DESCRIPTION`**, nessun `VALUE`, `DIALOG` o `TEXT`. **Zero segnaposto**, **1 tab** (unita' 8), **zero virgolette**.
**Apici**: **1 inglese** (`Tracker's`, unita' 2) contro **4 italiani** (elisione: `l'aggancio`, `L'Octopus`,
`nell'iperspazio`, `l'origine`).

**Lessico di glossario, verificato alla lettera**: `generatori di scudi`, `matrice dello scudo` (due volte),
`chiave di volta` per keystone (la scelta di L200), `disturbatore` per jammer.

**Nomi di prodotto invariati**: `Chameleon Anti-Missile`, `Bullfrog`, `Cuttlefish Jammer`, `Octopus Jammer`,
`Diamond`, `Williwaw Cooling`, `Hai-home`.
"""
import collections
import json
import os
import re
import sqlite3

TAB = chr(9)
QUOTE = chr(34)
APOS = chr(39)
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
TAGS = re.compile(r'<[^<>]+>')
IT_ALL = ' '.join(v['italian'] for v in cov)
EN_ALL = ' '.join(v['english'] for v in cov)
EN_T = sum(len(TAGS.findall(v['english'])) for v in cov)
IT_T = sum(len(TAGS.findall(v['italian'])) for v in cov)
EN_Q = sum(v['english'].count(QUOTE) for v in cov)
IT_Q = sum(v['italian'].count(QUOTE) for v in cov)
EN_A = sum(v['english'].count(APOS) for v in cov)
IT_A = sum(v['italian'].count(APOS) for v in cov)
KINDS = collections.Counter(u['kind'] for u in units)
NAMES = ('Chameleon Anti-Missile', 'Bullfrog', 'Cuttlefish Jammer', 'Octopus Jammer', 'Diamond',
         'Williwaw Cooling', 'Hai-home')
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 9/9", len(cov) == 9 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 9 DESCRIPTION (asserzione scritta)', KINDS == {'DESCRIPTION': 9}, dict(KINDS))
ck('ZERO VALUE, TEXT, DIALOG, UI_LABEL (asserzioni vuote scritte)',
   [u['idx'] for u in units if u['kind'] != 'DESCRIPTION'] == [])
ctx = [u['context'].replace('outfit:', '') for u in units]
ck('8 contesti distinti, da Chameleon Anti-Missile a Value Detector',
   len(set(ctx)) == 8 and (ctx[0], ctx[-1]) == ('Chameleon Anti-Missile', 'Value Detector'),
   '%d · %s · %s' % (len(set(ctx)), ctx[0], ctx[-1]))
ck('righe 508 e 600 (prima e ultima del lotto)',
   (cov[0]['line'], cov[-1]['line']) == (508, 600), (cov[0]['line'], cov[-1]['line']))
ck('ZERO segnaposto in inglese e in italiano (asserzione negativa scritta)',
   EN_T == 0 == IT_T and '<' not in IT_ALL and '<' not in EN_ALL)
ck('1 tab, nella stessa unita\' (8) in entrambe le lingue',
   [v['idx'] for v in cov if v['english'].startswith(TAB)] == [8]
   and [v['idx'] for v in cov if v['italian'].startswith(TAB)] == [8])
ck('zero virgolette in entrambe le lingue (asserzione vuota scritta)', EN_Q == 0 == IT_Q, (EN_Q, IT_Q))
ck("apici: 1 inglese (Tracker's, unita' 2) e 4 italiani (elisione: unita' 2, 3, 7, 8)",
   EN_A == 1 and IT_A == 4
   and [v['idx'] for v in cov if APOS in v['english']] == [2]
   and [v['idx'] for v in cov if APOS in v['italian']] == [2, 3, 7, 8], (EN_A, IT_A))
ck('nessun caporale e nessun carattere tipografico',
   not [v['idx'] for v in cov if any(c in v['italian'] for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026')])
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' you ', ' to the ', ' will be ',
        ' is ', ' are ', ' from the ', ' its ', ' it is ', ' such as ', ' rather than ', ' for a ', ' that ')
ck('nessun residuo inglese', not [w for w in ENGW if w in IT_ALL.lower()],
   [w for w in ENGW if w in IT_ALL.lower()])
CORT = re.findall(r'\bLei\b|(?<![.!?] )\b(?:Suo|Sua|Suoi|Sue)\b', IT_ALL)
ck('nessuna forma di cortesia «Lei»', not CORT, CORT)
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
ck('i nomi di prodotto presenti nel testo inglese restano invariati',
   not [n for n in NAMES if n in EN_ALL and n not in IT_ALL],
   [n for n in NAMES if n in EN_ALL and n not in IT_ALL])
ck('glossario: «generatori di scudi» (unita\' 4) e «matrice dello scudo» (unita\' 4 e 5)',
   'generatori di scudi' in by[4]['italian']
   and 'matrice dello scudo' in by[4]['italian'] and 'matrice dello scudo' in by[5]['italian'])
ck('keystone = «chiave di volta», due occorrenze, nessuna «pietra chiave»',
   by[8]['italian'].count('chiave di volta') == 2 and 'pietra chiave' not in IT_ALL)
ck('jammer = «disturbatore» (glossario): unita\' 2 e 3',
   'disturbatore' in by[2]['italian'] and 'Jammer' in by[2]['italian'] and 'Jammer' in by[3]['italian'])
ck('nessuna nave «grande» tradotta con «grosse»: «navi grandi» (unita\' 2)',
   'navi grandi' in by[2]['italian'])
c = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
st = dict(c.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('tutte le 9 unita sono PENDING (misurato)',
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
