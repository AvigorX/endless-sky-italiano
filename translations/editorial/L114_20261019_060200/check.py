r"""check.py — L114 (data/_ui/tooltips.txt, 110 unita', righe 976-1309)

**110 `TUTORIAL_TIP`**, tutte **`PENDING`** (misurato e asserito in `mkparts.py`).

**Novita' strutturale rispetto a L113**: i contesti tornano **uno per unita'** (110 su 110), quindi il
controllo «87 contesti con nove doppi» qui sarebbe rosso su un lotto corretto.

**Quattro coppie di ripetizioni legittime**: le armi hanno due misure dello stesso effetto, `/ second` e
`/ shot`, e l'inglese e' **identico** nelle due voci (17=64 scrambling, 18=65 slowing, 19=66 disruption,
36=83 firing scramble). Le rese devono essere **identiche** e la ripetizione si **dichiara**: qui il
criterio «zero ripetizioni» di L111-L113 e' rovesciato.

**12 virgolette** in cinque unita' (19, 38, 52, 66, 85): citazioni interne (`"leak through"`, `"direct"`,
`"leading"`), da riprodurre per unita'. **Zero tab**, **zero token**, **zero quadre**.
"""
import collections
import json
import os
import re
import sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
units = sorted(src['units'], key=lambda x: x['line'])
tr = {}
parts = sorted(f for f in os.listdir(os.path.join(HERE, 'parts')) if f.endswith('.json'))
for p in parts:
    for k, v in json.load(open(os.path.join(HERE, 'parts', p), encoding='utf-8')).items():
        tr[int(k)] = v
CTX = []
for u in units:
    CTX.append(u['context'])
out = {'block': src['block'], 'note': src['note'], 'units': []}
missing = []
for u in units:
    if u['idx'] not in tr:
        missing.append(u['idx'])
        continue
    it = tr[u['idx']]
    out['units'].append({"idx": u['idx'], "id": u['id'], "path": u['path'], "line": u['line'],
                         "kind": u['kind'], "context": u['context'], "english": u['english'],
                         "italian": it, "ratio": round(len(it) / max(1, len(u['english'])), 3)})
open(os.path.join(HERE, 'translation.json'), 'w', encoding='utf-8').write(json.dumps(out, ensure_ascii=False, indent=1))
cov = out['units']
by = {v['idx']: v for v in cov}
TAGS = re.compile(r'<[^<>]+>')
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 110/110", len(cov) == 110 == len(units) and not missing, '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
kk = collections.Counter(u['kind'] for u in units)
ck('tipo unico: 110 TUTORIAL_TIP', dict(kk) == {'TUTORIAL_TIP': 110}, dict(kk))
for k in ('VALUE', 'DESCRIPTION', 'MISSION_TEXT', 'TEXT', 'DIALOG', 'LOGBOOK', 'UI_LABEL', 'CONVERSATION'):
    ck('%s assente' % k, not [u for u in cov if u['kind'] == k])
ck('nessuna unita identica al sorgente',
   not [v['idx'] for v in cov if v['italian'].strip() == v['english'].strip()])
ck('ZERO tab, nel sorgente e in traduzione',
   not [u['idx'] for u in units if '\t' in u['english']]
   and not [v['idx'] for v in cov if '\t' in v['italian']])
a = sum(v['english'].count('"') for v in cov)
b = sum(v['italian'].count('"') for v in cov)
ck('virgolette: %d = %d (12)' % (a, b), a == b == 12, (a, b))
ck('virgolette per unita', not [v for v in cov if v['english'].count('"') != v['italian'].count('"')],
   [(v['idx'], v['english'].count('"'), v['italian'].count('"'))
    for v in cov if v['english'].count('"') != v['italian'].count('"')])
ck('le cinque unita citano: 19, 38, 52(x4), 66, 85',
   [v['idx'] for v in cov if v['italian'].count('"')] == [19, 38, 52, 66, 85]
   and by[52]['italian'].count('"') == 4, [v['idx'] for v in cov if v['italian'].count('"')])
ck('ZERO token (asserito vuoto)',
   not [t for v in cov for t in TAGS.findall(v['english'])]
   and not [t for v in cov for t in TAGS.findall(v['italian'])])
ck('ZERO quadre (asserito vuoto)', not [v['idx'] for v in cov if '[' in v['italian'] or ']' in v['italian']])
ck('ZERO backtick', not [v['idx'] for v in cov if '`' in v['italian']])
# --- contesti: 110, uno per unita' --------------------------------------------------------
seen = collections.Counter(CTX)
ck('110 contesti distinti, tutti tip:', len(seen) == 110 == len(units) and all(c.startswith('tip:') for c in seen),
   len(seen))
ck('nessun contesto doppio (la forma di L113 qui sarebbe un errore)', max(seen.values()) == 1,
   {k: v for k, v in seen.items() if v > 1})
ck('prima e ultima unita: righe 976 e 1309', (cov[0]['line'], cov[-1]['line']) == (976, 1309),
   (cov[0]['line'], cov[-1]['line']))
ck('primo e ultimo contesto: Engines: / reverse only?',
   (cov[0]['context'], cov[-1]['context']) == ('tip:Engines:', 'tip:reverse only?'),
   (cov[0]['context'], cov[-1]['context']))
# --- ripetizioni legittime: quattro coppie, rese identiche --------------------------------
grd = {}
for u in units:
    grd.setdefault(u['english'], []).append(u['idx'])
pairs = sorted(v for v in grd.values() if len(v) > 1)
ck('quattro coppie di ripetizioni, nessun gruppo da tre', pairs == [[17, 64], [18, 65], [19, 66], [36, 83]], pairs)
ck('ogni coppia ha la stessa resa italiana',
   all(by[p[0]]['italian'] == by[p[1]]['italian'] for p in pairs),
   [(p, by[p[0]]['italian'][:40]) for p in pairs if by[p[0]]['italian'] != by[p[1]]['italian']])
it_grp = {}
for v in cov:
    it_grp.setdefault(v['italian'], []).append(v)
ck('nessun duplicato italiano non spiegato dal sorgente',
   not [g for g in it_grp.values() if len(g) > 1 and len({v['english'] for v in g}) > 1],
   [[v['idx'] for v in g] for g in it_grp.values() if len(g) > 1 and len({v['english'] for v in g}) > 1])
# --- unita' di misura: / second -> al secondo, / shot -> per colpo ------------------------
sec = [v['idx'] for v in cov if 'per second' in v['english'] and 'al secondo' not in v['italian']]
shot = [v['idx'] for v in cov if 'per shot' in v['english'] and 'per colpo' not in v['italian']]
ck('ogni «per second» inglese reso con «al secondo»', not sec, sec)
ck('ogni «per shot» inglese reso con «per colpo»', not shot, shot)
ck('registro approvato: nessun «voi»',
   not [v['idx'] for v in cov if re.search(r'\b(avete|potete|potrete|siete|vostro|vostra|vostri|vostre)\b',
                                           v['italian'])])
LOW = ' '.join(v['italian'] for v in cov).lower()
TERMS = ('scudi', 'scafo', 'energia', 'calore', 'carburante', 'virata', 'torretta', 'equipaggiament',
         'propulsor', 'postbruciatore', 'al secondo', 'per colpo', 'bersaglio', 'colpo')
ck('terminologia presente: 14 termini chiave', all(t in LOW for t in TERMS),
   [t for t in TERMS if t not in LOW])
ck('nessun residuo inglese comune',
   not [w for w in (' the ', ' of the ', ' per second when', 'damage ', 'hull ', 'shield ', 'outfit ',
                    ' your ', ' this ')
        if w in LOW],
   [w for w in (' the ', ' of the ', ' per second when', 'damage ', 'hull ', 'shield ', 'outfit ',
                ' your ', ' this ') if w in LOW])
rs = [v['ratio'] for v in cov]
for v in cov:
    if not 0.55 < v['ratio'] < 1.90:
        print('OUTLIER', v['idx'], v['ratio'], v['english'][:40], '|', v['italian'][:40])
ck('rapporto nel gate', 0.55 < min(rs) and max(rs) < 1.90, '%.2f - %.2f' % (min(rs), max(rs)))
bad = [(v['idx'], n) for v in cov for p, n in ((r"\b(e|piu|perche|cosi|gia|puo|cioe|percio)'", 'accento'),
       ('\u2026', 'ellissi'), ('\u2014', 'em dash'), ('\u2019', 'apostrofo curvo'), ('\u00ab', 'caporale'),
       ('\u00bb', 'caporale')) if re.search(p, v['italian'])]
ck('tipografia', not bad, bad)
nonlat = [v['idx'] for v in cov for c in v['italian'] if ord(c) > 127 and not 0x00C0 <= ord(c) <= 0x024F]
ck('caratteri non latini', not nonlat, nonlat)
c = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
st = dict(c.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('tutte le 110 unita sono PENDING nel database (misurato)',
   c.execute('select count(*) from units where id in (%s) and state != "PENDING"'
             % ','.join('?' * len(units)), [u['id'] for u in units]).fetchone()[0] == 0)
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, b2, ok in rows:
    print('| %s | %s | %s |' % (n, b2, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d' % (sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('righe %d/%d · parti %d · mancanti %d' % (min(u['line'] for u in units), max(u['line'] for u in units),
      len(parts), len(missing)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
