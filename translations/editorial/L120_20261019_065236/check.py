r"""check.py — L120 (`data/human/campaign events.txt`, 52 unita', righe 28-242)

Primo lotto del file **più pesante che resta** (150 unità, 6.961 parole). Forma propria:

- **41 unità su 52 iniziano con tab**: qui il tab è la norma, e il controllo conta **unità** e **occorrenze per
  unità**;
- **58 virgolette** che sono **dialogo** (si traducono) e si verificano **per unità**;
- **nessun `VALUE`**: il controllo «i `VALUE` sono identici al sorgente» è un'**asserzione vuota** (`0 = 0`),
  dichiarata — non omessa;
- **45 testi distinti** per 52 unità: sette coppie ripetono l'inglese e la resa ripete;
- **3 contesti** molto sbilanciati (6 / 9 / **37** unità), che non si «ribilanciano».
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
out = {'block': src['block'], 'note': src['note'], 'units': []}
missing = [u['idx'] for u in units if u['idx'] not in tr]
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
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 52/52", len(cov) == 52 == len(units) and not missing, '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
kk = collections.Counter(u['kind'] for u in units)
ck('tipi: 41 MISSION_TEXT · 9 DESCRIPTION · 2 LOGBOOK',
   dict(kk) == {'MISSION_TEXT': 41, 'DESCRIPTION': 9, 'LOGBOOK': 2}, dict(kk))
ck('ZERO VALUE nel file (asserzione vuota, dichiarata)',
   not [u['idx'] for u in units if u['kind'] == 'VALUE'])
ck('tutte le unita sono tradotte',
   not [v['idx'] for v in cov if v['italian'].strip() == v['english'].strip()])
ck('i 2 LOGBOOK sono tradotti',
   not [v['idx'] for v in cov if v['kind'] == 'LOGBOOK' and v['italian'] == v['english']])
# --- tab: 41 unita' -----------------------------------------------------------------------
te = [v['idx'] for v in cov if v['english'].startswith('\t')]
ti = [v['idx'] for v in cov if v['italian'].startswith('\t')]
ck('41 unita iniziano con tab, le stesse in inglese e in italiano', len(te) == 41 and te == ti,
   (len(te), len(ti)))
ck('occorrenze di tab identiche per unita (nessun tab doppio)',
   not [v['idx'] for v in cov if v['english'].count('\t') != v['italian'].count('\t')])
ck('le 11 unita senza tab sono le prime dei blocchi e le descrizioni',
   [v['idx'] for v in cov if not v['english'].startswith('\t')] == [1, 2, 3, 7, 8, 9, 10, 12, 13, 16, 17],
   [v['idx'] for v in cov if not v['english'].startswith('\t')])
# --- virgolette: 58, dialogo --------------------------------------------------------------
ck('58 virgolette in inglese e in italiano',
   sum(v['english'].count('"') for v in cov) == 58 == sum(v['italian'].count('"') for v in cov),
   (sum(v['english'].count('"') for v in cov), sum(v['italian'].count('"') for v in cov)))
ck('virgolette per unita: stesso numero',
   not [v['idx'] for v in cov if v['english'].count('"') != v['italian'].count('"')],
   [(v['idx'], v['english'].count('"'), v['italian'].count('"')) for v in cov
    if v['english'].count('"') != v['italian'].count('"')])
ck('ZERO quadre · ZERO backtick',
   not [v['idx'] for v in cov if '[' in v['italian'] or ']' in v['italian'] or '`' in v['italian']])
TOK = {'<ship>': 4, '<planet>': 1}
ck('5 token nelle due famiglie attese',
   collections.Counter(t for v in cov for t in TAGS.findall(v['english'])) == TOK
   == collections.Counter(t for v in cov for t in TAGS.findall(v['italian'])),
   collections.Counter(t for v in cov for t in TAGS.findall(v['italian'])))
ck('token per unita: stessi simboli e stesso ordine',
   not [v['idx'] for v in cov if TAGS.findall(v['italian']) != TAGS.findall(v['english'])])
# --- contesti -----------------------------------------------------------------------------
seen = collections.Counter(u['context'] for u in units)
ck('3 contesti distinti: remembrance day, war begins, event: war begins',
   list(seen) == ['mission:remembrance day', 'event:war begins', 'mission:event: war begins'], list(seen))
ck('distribuzione 6 / 9 / 37 unita (non si ribilancia)',
   sorted(seen.values()) == [6, 9, 37] and seen['mission:event: war begins'] == 37, dict(seen))
ck('prima e ultima unita: righe 28 e 242', (cov[0]['line'], cov[-1]['line']) == (28, 242),
   (cov[0]['line'], cov[-1]['line']))
ck('primo e ultimo contesto: remembrance day / event: war begins',
   (cov[0]['context'], cov[-1]['context']) == ('mission:remembrance day', 'mission:event: war begins'),
   (cov[0]['context'], cov[-1]['context']))
# --- ripetizioni: 45 testi distinti -------------------------------------------------------
grd = collections.Counter(u['english'] for u in units)
ck('45 testi inglesi distinti per 52 unita', len(grd) == 45, len(grd))
ck('7 coppie di testi ripetuti (le risposte del giocatore e un paragrafo di cronaca)',
   collections.Counter(grd.values()) == {1: 38, 2: 7}, collections.Counter(grd.values()))
ck('nessun gruppo con due rese diverse',
   not [k for k in grd if len({by[u['idx']]['italian'] for u in units if u['english'] == k}) > 1])
it_grp = {}
for v in cov:
    it_grp.setdefault(v['italian'], []).append(v)
ck('nessun duplicato italiano non spiegato dal sorgente',
   not [g for g in it_grp.values() if len(g) > 1 and len({v['english'] for v in g}) > 1],
   [[v['idx'] for v in g] for g in it_grp.values() if len(g) > 1 and len({v['english'] for v in g}) > 1])
# --- registro e terminologia --------------------------------------------------------------
ck('registro approvato: nessun «voi»',
   not [v['idx'] for v in cov if re.search(r'\b(avete|potete|potrete|siete|vostro|vostra|vostri|vostre)\b',
                                           v['italian'])])
ck('nessuna forma di cortesia «lei» nel dialogo (un registro solo)',
   not [v['idx'] for v in cov if re.search(r'\b(Pensi quello|la sua nave|la farò|Senta, capitano)\b',
                                           v['italian'])])
LOW = ' '.join(v['italian'] for v in cov).lower()
TERMS = ('giorno del ricordo', 'mondi liberi', 'arsenale', 'borsa galattica', 'parlamento', 'ultimatum',
         'stato di emergenza', 'legge marziale', 'navi portatrici', 'terroristi', 'guerra civile')
ck('terminologia presente: 11 termini chiave', all(t in LOW for t in TERMS),
   [t for t in TERMS if t not in LOW])
NOSCRUB = ' '.join(TAGS.sub('""', v['italian']) for v in cov).lower()
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' ship ', ' war zone')
ck('nessun residuo inglese fuori dai nomi propri e dai token',
   not [w for w in ENGW if w in NOSCRUB], [w for w in ENGW if w in NOSCRUB])
rs = [v['ratio'] for v in cov]
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
ck('tutte le 52 unita sono PENDING nel database (misurato)',
   c.execute('select count(*) from units where id in (%s) and state != "PENDING"'
             % ','.join('?' * len(units)), [u['id'] for u in units]).fetchone()[0] == 0)
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d' % (sum(len(v['english'].split()) for v in cov),
                                 sum(len(v['italian'].split()) for v in cov)))
print('righe %d/%d · parti %d · mancanti %d' % (min(u['line'] for u in units), max(u['line'] for u in units),
      len(parts), len(missing)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
