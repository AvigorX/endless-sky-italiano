r"""check.py — L140 (`data/hai/unfettered 0 prologue.txt`, 25 unita', righe 22-81).

Controlli propri: **un solo contesto**; **23 unita' con tab**; **50 virgolette** con distribuzione per unita' e nessuna
dispari; **quattro frasi ripetute** rese identiche (le due scelte, la domanda sui «veri Hai», la battuta
sull'estinzione); il **motto degli Slegati** presente **cinque volte** e sempre identico; **zero token** e **zero
`VALUE`/`UI_LABEL`**.
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
MOTTO = "Eravamo padroni di cento mondi quando le scimmie umane non avevano ancora imparato a usare i pollici."
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 25/25", len(cov) == 25 == len(units) and not missing, '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 25 MISSION_TEXT', collections.Counter(u['kind'] for u in units) == {'MISSION_TEXT': 25},
   collections.Counter(u['kind'] for u in units))
ck('ZERO VALUE, ZERO UI_LABEL (due asserzioni vuote scritte)',
   [u['idx'] for u in units if u['kind'] in ('VALUE', 'UI_LABEL')] == [])
ck('ZERO token in questa finestra (asserzione vuota scritta)',
   collections.Counter(t for u in units for t in TAGS.findall(u['english'])) == {})
ck('tutte le unita di testo sono tradotte (25 su 25)',
   not [v['idx'] for v in cov if v['italian'].strip() == v['english'].strip()])
tabs = [v['idx'] for v in cov if v['english'].startswith('\t')]
ck('23 unita iniziano con tab, le stesse in traduzione',
   len(tabs) == 23 and tabs == [v['idx'] for v in cov if v['italian'].startswith('\t')], len(tabs))
ck('le due unita senza tab sono la 1 e la 8',
   [v['idx'] for v in cov if not v['english'].startswith('\t')] == [1, 8])
ck('spazi iniziali e finali identici al sorgente (25/25)',
   not [v['idx'] for v in cov
        if len(v['italian']) - len(v['italian'].rstrip()) != len(v['english']) - len(v['english'].rstrip())])
ck('50 virgolette in inglese e in italiano',
   sum(v['english'].count('"') for v in cov) == 50 == sum(v['italian'].count('"') for v in cov),
   (sum(v['english'].count('"') for v in cov), sum(v['italian'].count('"') for v in cov)))
ck('virgolette per unita: stesso numero in tutte',
   not [v['idx'] for v in cov if v['english'].count('"') != v['italian'].count('"')],
   [(v['idx'], v['english'].count('"'), v['italian'].count('"')) for v in cov
    if v['english'].count('"') != v['italian'].count('"')])
ck('distribuzione delle virgolette: 4 alle unita 4, 11, 19, 20, 22, 23',
   [v['idx'] for v in cov if v['italian'].count('"') == 4] == [4, 11, 19, 20, 22, 23],
   [v['idx'] for v in cov if v['italian'].count('"') == 4])
ck('nessuna unita dispari (asserito: lista vuota)',
   [v['idx'] for v in cov if v['english'].count('"') % 2] == [])
ck('1 contesto: First Contact: Unfettered, 25 unita',
   list(collections.Counter(v['context'] for v in cov).items()) == [('mission:First Contact: Unfettered', 25)])
ck('prima e ultima unita: righe 22 e 81', (cov[0]['line'], cov[-1]['line']) == (22, 81),
   (cov[0]['line'], cov[-1]['line']))
ck('21 testi distinti su 25 unita', len({v['english'] for v in cov}) == 21,
   len({v['english'] for v in cov}))
ck('le due scelte ripetute hanno la stessa resa (2-9 e 3-10)',
   by[2]['italian'].lstrip('	') == by[9]['italian'].lstrip('	') == '(Certo.)'
   and by[3]['italian'].lstrip('	') == by[10]['italian'].lstrip('	') == '(Non ora, è troppo rischioso.)')
ck('la domanda sui «veri Hai» ha la stessa resa (6 e 13)', by[6]['italian'] == by[13]['italian'],
   (by[6]['italian'], by[13]['italian']))
ck('la battuta sull\'estinzione ha la stessa resa (18 e 21)', by[18]['italian'] == by[21]['italian'])
ck('il motto degli Slegati compare 5 volte, sempre identico',
   ' '.join(v['italian'] for v in cov).count(MOTTO) == 5,
   ' '.join(v['italian'] for v in cov).count(MOTTO))
ck('ZERO quadre e zero backtick (asserito)',
   not [v['idx'] for v in cov if any(c in v['english'] + v['italian'] for c in '[]`')])
LOW = ' '.join(v['italian'] for v in cov).lower()
TERMS = ('scimmia', 'hai', 'slegati' if 'slegati' in LOW else 'veri hai', 'alterati' if 'alterati' in LOW else 'inalterati',
         'estinzione', 'conquistatori', 'banchina', 'scoiattoli', 'cento mondi', 'pollici')
ck('terminologia presente: 9 termini chiave', all(t in LOW for t in TERMS),
   [t for t in TERMS if t not in LOW])
ck('i nomi restano: Hai (mai tradotto)', 'hai' in LOW and 'hay' not in LOW)
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' you ', ' to the ')
LONG = ' '.join(TAGS.sub('""', v['italian']) for v in cov).lower()
for s in ('true hai', 'hai'):
    LONG = LONG.replace(s, '@@')
ck('nessun residuo inglese fuori dai nomi propri',
   not [w for w in ENGW if w in LONG], [w for w in ENGW if w in LONG])
CORT = re.findall(r'\bLei\b|(?<![.!?] )\b(?:Suo|Sua|Suoi|Sue)\b', ' '.join(v['italian'] for v in cov))
ck('nessuna forma di cortesia «Lei»', not CORT, CORT)
rs = [v['ratio'] for v in cov]
ck('rapporto nel gate', 0.55 < min(rs) and max(rs) < 1.90, '%.2f - %.2f' % (min(rs), max(rs)))
bad = [(v['idx'], n) for v in cov for p, n in ((r"\b(e|piu|perche|cosi|gia|puo|cioe|percio|fa)'", 'accento'),
       ('\u2026', 'ellissi'), ('\u2014', 'em dash'), ('\u2013', 'en dash'), ('\u2019', 'apostrofo curvo'),
       ('\u00ab', 'caporale'), ('\u00bb', 'caporale')) if re.search(p, v['italian'])]
ck('tipografia', not bad, bad)
nonlat = [v['idx'] for v in cov for c in v['italian'] if ord(c) > 127 and not 0x00C0 <= ord(c) <= 0x024F]
ck('caratteri non latini', not nonlat, nonlat)
c = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
st = dict(c.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('tutte le 25 unita sono PENDING nel database (misurato)',
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
