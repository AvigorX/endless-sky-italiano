r"""check.py — L115 (data/_ui/tooltips.txt, 104 unita', righe 1312-1566)

**104 `TUTORIAL_TIP`**, tutte **`PENDING`** (misurato e asserito in `mkparts.py`).

**Tre registri nello stesso lotto**: avvisi del cantiere (1-11), etichette di comando con la loro
descrizione (12-58) e descrizioni di opzione, molte con le varianti in elenco (59-104).

**La forma dei contesti cambia di nuovo**: **72 contesti per 104 unità** — 56 singole, 7 coppie, 5 terne,
2 quaterne, una da cinque (`Text alignment`) e una da sei (`Show status overlays`). Il controllo di L114
(«110 contesti, max 1») qui sarebbe rosso su un lotto corretto; qui è il `Counter` esatto a valere.

**82 virgolette** in 38 unità (37 con due, **una con otto**): i testi fra virgolette sono **chiavi e valori
di impostazione** del gioco (`Preferences::Has("Escorts expend ammo")`), quindi restano **identici
all'inglese** — unica eccezione dichiarata l'unità 10, che cita l'etichetta `surge` già resa «picco» da L113
nello stesso pannello. **8 token** `<shift>`, una sola famiglia. Zero tab, zero quadre, zero backtick.
Una ripetizione identica: `- "fast": just uses the ship's sprite.` (89 e 92), resa identica.
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
CTX = [u['context'] for u in units]
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
QUOTED = re.compile(r'"([^"]*)"')
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 104/104", len(cov) == 104 == len(units) and not missing, '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
kk = collections.Counter(u['kind'] for u in units)
ck('tipo unico: 104 TUTORIAL_TIP', dict(kk) == {'TUTORIAL_TIP': 104}, dict(kk))
for k in ('VALUE', 'DESCRIPTION', 'MISSION_TEXT', 'TEXT', 'DIALOG', 'LOGBOOK', 'UI_LABEL', 'CONVERSATION'):
    ck('%s assente' % k, not [u for u in cov if u['kind'] == k])
ck('nessuna unita identica al sorgente',
   not [v['idx'] for v in cov if v['italian'].strip() == v['english'].strip()])
ck('ZERO tab, nel sorgente e in traduzione',
   not [u['idx'] for u in units if '\t' in u['english']]
   and not [v['idx'] for v in cov if '\t' in v['italian']])
a = sum(v['english'].count('"') for v in cov)
b = sum(v['italian'].count('"') for v in cov)
ck('virgolette: %d = %d (82)' % (a, b), a == b == 82, (a, b))
ck('virgolette per unita', not [v for v in cov if v['english'].count('"') != v['italian'].count('"')],
   [(v['idx'], v['english'].count('"'), v['italian'].count('"'))
    for v in cov if v['english'].count('"') != v['italian'].count('"')])
ck('38 unita citano: 37 con due, la 35 con otto',
   sum(1 for v in cov if v['italian'].count('"')) == 38
   and [v['idx'] for v in cov if v['italian'].count('"') == 8] == [35],
   [v['idx'] for v in cov if v['italian'].count('"') == 8])
QEXC = {10: (['picco'], ['surge'])}
badq = [(v['idx'], QUOTED.findall(v['italian']), QUOTED.findall(v['english'])) for v in cov
        if v['idx'] not in QEXC and QUOTED.findall(v['italian']) != QUOTED.findall(v['english'])]
ck('le citazioni sono chiavi/valori identici all\'inglese (eccezione dichiarata: 10)',
   not badq and (QUOTED.findall(by[10]['italian']), QUOTED.findall(by[10]['english'])) == QEXC[10], badq)
ck('ZERO token estranei: solo <shift>',
   collections.Counter(t for v in cov for t in TAGS.findall(v['english']))
   == collections.Counter(t for v in cov for t in TAGS.findall(v['italian']))
   == {'<shift>': 8},
   collections.Counter(t for v in cov for t in TAGS.findall(v['italian'])))
ck('token per unita (8 unita con un <shift> ciascuna)',
   [v['idx'] for v in cov if '<shift>' in v['italian']]
   == [v['idx'] for v in cov if '<shift>' in v['english']]
   and sum(1 for v in cov if '<shift>' in v['italian']) == 8,
   [v['idx'] for v in cov if '<shift>' in v['italian']])
ck('ZERO quadre (asserito vuoto)', not [v['idx'] for v in cov if '[' in v['italian'] or ']' in v['italian']])
ck('ZERO backtick', not [v['idx'] for v in cov if '`' in v['italian']])
# --- contesti: 72 per 104 unita' ----------------------------------------------------------
seen = collections.Counter(CTX)
ck('72 contesti distinti, tutti tip:', len(seen) == 72 and all(c.startswith('tip:') for c in seen), len(seen))
ck('distribuzione dei contesti 56/7/5/2/1/1',
   collections.Counter(seen.values()) == {1: 56, 2: 7, 3: 5, 4: 2, 5: 1, 6: 1},
   collections.Counter(seen.values()))
ck('i sedici contesti ripetuti sono quelli attesi',
   sorted(k for k, v in seen.items() if v > 1) == [
       'tip:Board selected ship', 'tip:Camera acceleration', 'tip:Cloaked ship outlines',
       'tip:Deploy / recall fighters', 'tip:Fleet: Gather around me', 'tip:Initiate hyperspace jump',
       'tip:Parallax background', 'tip:Reverse', 'tip:Select nearest hostile ship', 'tip:Select next ship',
       'tip:Ship outlines in HUD', 'tip:Ship outlines in shops', 'tip:Show status overlays',
       'tip:Talk to selected ship', 'tip:Text alignment', 'tip:Texture filtering'],
   sorted(k for k, v in seen.items() if v > 1))
ck('massimo sei unita nello stesso contesto (Show status overlays)',
   max(seen.values()) == 6 and seen['tip:Show status overlays'] == 6, seen.most_common(2))
ck('prima e ultima unita: righe 1312 e 1566', (cov[0]['line'], cov[-1]['line']) == (1312, 1566),
   (cov[0]['line'], cov[-1]['line']))
ck('primo e ultimo contesto: battery only? / Show status overlays',
   (cov[0]['context'], cov[-1]['context']) == ('tip:battery only?', 'tip:Show status overlays'),
   (cov[0]['context'], cov[-1]['context']))
# --- ripetizioni: una coppia --------------------------------------------------------------
grd = {}
for u in units:
    grd.setdefault(u['english'], []).append(u['idx'])
pairs = sorted(v for v in grd.values() if len(v) > 1)
ck('una sola coppia di ripetizioni (89/92)', pairs == [[89, 92]], pairs)
ck('la coppia ha la stessa resa italiana', by[89]['italian'] == by[92]['italian'])
it_grp = {}
for v in cov:
    it_grp.setdefault(v['italian'], []).append(v)
ck('nessun duplicato italiano non spiegato dal sorgente',
   not [g for g in it_grp.values() if len(g) > 1 and len({v['english'] for v in g}) > 1],
   [[v['idx'] for v in g] for g in it_grp.values() if len(g) > 1 and len({v['english'] for v in g}) > 1])
ck('registro approvato: nessun «voi»',
   not [v['idx'] for v in cov if re.search(r'\b(avete|potete|potrete|siete|vostro|vostra|vostri|vostre)\b',
                                           v['italian'])])
LOW = ' '.join(v['italian'] for v in cov).lower()
TERMS = ('ammiraglia', 'propulsori', 'virata', 'scudi', 'scafo', 'flotta', 'scorte', 'caccia', 'detrito',
         'carburante', 'energia', 'occultamento', 'impostazione', 'pannello', 'zoom', 'postbruciatore')
ck('terminologia presente: 16 termini chiave', all(t in LOW for t in TERMS),
   [t for t in TERMS if t not in LOW])
NOSCRUB = ' '.join(QUOTED.sub('""', v['italian']) for v in cov).lower()
ENGWORDS = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' ship ', ' game ')
ck('nessun residuo inglese fuori dalle citazioni',
   not [w for w in ENGWORDS if w in NOSCRUB], [w for w in ENGWORDS if w in NOSCRUB])
rs = [v['ratio'] for v in cov]
for v in cov:
    if not 0.55 < v['ratio'] < 1.90:
        print('OUTLIER', v['idx'], v['ratio'], v['english'][:40], '|', v['italian'][:40])
ck('rapporto nel gate', 0.55 < min(rs) and max(rs) < 1.90, '%.2f - %.2f' % (min(rs), max(rs)))
bad = [(v['idx'], n) for v in cov for p, n in ((r"\b(e|piu|perche|cosi|gia|puo|cioe|percio|fa)'", 'accento'),
       ('\u2026', 'ellissi'), ('\u2014', 'em dash'), ('\u2019', 'apostrofo curvo'), ('\u00ab', 'caporale'),
       ('\u00bb', 'caporale')) if re.search(p, v['italian'])]
ck('tipografia', not bad, bad)
nonlat = [v['idx'] for v in cov for c in v['italian'] if ord(c) > 127 and not 0x00C0 <= ord(c) <= 0x024F]
ck('caratteri non latini', not nonlat, nonlat)
c = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
st = dict(c.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('tutte le 104 unita sono PENDING nel database (misurato)',
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
