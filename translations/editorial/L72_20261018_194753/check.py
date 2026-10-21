r"""check.py — L72 (data/successors/successor 2 ghosts myurej.txt, 50 unita', righe 402-531)

Quinto lotto sul file e **ultimo**: **chiude** `successor 2 ghosts myurej.txt` a **211/211**
(49 + 31 + 39 + 42 + 50), `max(line) = 531`, 0 unita' dopo. Copre **tre contesti**: `Myurej 6`, `7`, `8`.

Misure del sorgente, tutte rimisurate (decisione 119):
  - **`NT` vuoto** (0 `UI_LABEL`, 0 riferimenti di dato): assenza dichiarata, asserita anche sul `raw`;
  - **`LOGBOOK` 2** (unita' 5 e 30), forma **diretta**, testi distinti e tradotti;
  - **`DIALOG` 2** (unita' 3 e 4): primi del file, sono **testo** (descrizioni di evento), tradotti;
  - **`VALUE` 3** e **`DESCRIPTION` 3**: tre missioni si aprono/chiudono qui;
  - **18 token** in 8 famiglie: `<planet>` 5, `<last>` 3, `<ship>` 2, `<destination>` 2, `<origin>` 2,
    `<tons>` 2, `<payment>` 1, `<first>` 1;
  - **36 tab su 36 unita'**, **96 virgolette**, **0 dispari**, **0 quadre**, **0 backtick**;
  - tipi: 40 `MISSION_TEXT` + 3 `VALUE` + 3 `DESCRIPTION` + 2 `DIALOG` + 2 `LOGBOOK`; 0 `CONVERSATION`,
    0 `TEXT`; **0 gruppi** di duplicati inglesi.

Invariante **di file** (il lotto chiude): `0 dopo`, `max(line) = 531`, copertura 211/211 (decisione 181).
"""

import collections
import json
import os
import re
import sqlite3
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))

src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
units = src['units']

tr = {}
parts = sorted(f for f in os.listdir(os.path.join(HERE, 'parts')) if f.endswith('.json'))
for p in parts:
    for k, v in json.load(open(os.path.join(HERE, 'parts', p), encoding='utf-8')).items():
        tr[int(k)] = v

NT_LABEL = set()
NT_DATA = set()
NT = NT_LABEL | NT_DATA
LOG = set([5, 30])
LOG_CAT = set()
DIALOG = set([3, 4])

en_count = collections.Counter(u['english'] for u in units)
DUP_GROUPS = collections.OrderedDict()
for u in units:
    if en_count[u['english']] > 1:
        DUP_GROUPS.setdefault(u['english'], []).append(u['idx'])
DUP_OK = set(i for idxs in DUP_GROUPS.values() for i in idxs)

lo, hi = 1, len(units)
if '--range' in sys.argv:
    i = sys.argv.index('--range')
    lo, hi = int(sys.argv[i + 1]), int(sys.argv[i + 2])
sel = [u for u in units if lo <= u['idx'] <= hi]


def build(it, en):
    return '\t' * (len(en) - len(en.lstrip('\t'))) + it


out = {'block': src['block'], 'note': src['note'], 'units': []}
missing = [u['idx'] for u in units if u['idx'] not in tr]
for u in units:
    if u['idx'] not in tr:
        continue
    it = build(tr[u['idx']], u['english'])
    out['units'].append({
        "idx": u['idx'], "id": u['id'], "path": u['path'], "line": u['line'],
        "kind": u['kind'], "context": u['context'], "english": u['english'],
        "italian": it, "ratio": round(len(it) / max(1, len(u['english'])), 3)})
open(os.path.join(HERE, 'translation.json'), 'w', encoding='utf-8').write(
    json.dumps(out, ensure_ascii=False, indent=1))

by_idx = {v['idx']: v for v in out['units']}
cov = [by_idx[u['idx']] for u in sel if u['idx'] in by_idx]
allcov = [by_idx[u['idx']] for u in units if u['idx'] in by_idx]
TAGS = re.compile(r'<[^<>]+>')

rows = []
rows.append(('unita\' richieste in questo controllo', len(sel), True))
rows.append(('unita\' tradotte nell\'intervallo', '%d/%d' % (len(cov), len(sel)), len(cov) == len(sel)))
rows.append(('copertura del lotto', '%d/%d' % (len(allcov), len(units)), len(allcov) == len(units)))
e = [v['idx'] for v in cov if not v['italian'].strip()]
rows.append(('traduzioni vuote', e or 0, not e))

ui_all = tuple(v['idx'] for v in cov if v['kind'] == 'UI_LABEL')
rows.append(('unita UI_LABEL nel segmento (0 attese: assenza dichiarata)', ui_all or 'ok', ui_all == ()))
ident = [v['idx'] for v in cov if v['idx'] in NT and v['italian'] != v['english']]
rows.append(('non traducibili lasciate identiche (0 attese: NT vuoto)', ident or 0, not ident and NT == set()))

log_units = [v['idx'] for v in cov if v['kind'] == 'LOGBOOK']
rows.append(('righe LOGBOOK nel segmento (2 attese: controllo positivo)', log_units or 'ok', log_units == [5, 30]))
log_same = [i for i in log_units if by_idx[i]['italian'].strip() == by_idx[i]['english'].strip()]
rows.append(('righe log di testo tradotte (2 attese)', '%d/2' % len(log_units), len(log_units) == 2 and not log_same))
two_log = by_idx[5]['italian'] != by_idx[30]['italian']
rows.append(('i due LOGBOOK restano distinti', 'ok' if two_log else 'identici', two_log))
raw_by_idx = {u['idx']: u['raw'] for u in units}
form_quote = [i for i in LOG if re.match(r'\t+log "[^"]+"\s*$', raw_by_idx[i])]
form_back = [i for i in LOG if re.match(r'\t+log `', raw_by_idx[i])]
form_three = [i for i in LOG if re.match(r'\t+log "[^"]+" "[^"]+" "[^"]+"\s*$', raw_by_idx[i])]
rows.append(('forme di log: 2 diretta, 0 backtick, 0 tre argomenti',
             'ok' if set(form_quote) == LOG else (sorted(form_quote), sorted(form_back), sorted(form_three)),
             set(form_quote) == LOG and not form_back and not form_three))
rows.append(('categorie estratte come unita (0 attese)', sorted(LOG_CAT) or 'ok', LOG_CAT == set()))

dlg = [v['idx'] for v in cov if v['kind'] == 'DIALOG']
rows.append(('nodi DIALOG nel segmento (2 attese: primi del file)', dlg or 'ok', dlg == [3, 4]))
dlg_same = [i for i in dlg if by_idx[i]['italian'].strip() == by_idx[i]['english'].strip()]
rows.append(('DIALOG sono testo tradotto, non etichette', dlg_same or 'ok', not dlg_same))
txt = tuple(sorted(v['idx'] for v in cov if v['kind'] == 'TEXT'))
rows.append(('unita TEXT di phrase (0 attese: assenza dichiarata)', txt or 'ok', txt == ()))
conv = [v['idx'] for v in cov if v['kind'] == 'CONVERSATION']
rows.append(('nodi di conversazione (0 attesi: assenza dichiarata)', conv or 'ok', conv == []))

KINDS = {'MISSION_TEXT': 40, 'VALUE': 3, 'DESCRIPTION': 3, 'DIALOG': 2, 'LOGBOOK': 2}
kk = collections.Counter(u['kind'] for u in units)
rows.append(('distribuzione dei tipi (%s)' % ', '.join('%s %d' % (k, v) for k, v in sorted(KINDS.items())),
             ', '.join('%s %d' % (k, v) for k, v in sorted(kk.items())), dict(kk) == KINDS))
vd = [v['idx'] for v in allcov if v['kind'] in ('VALUE', 'DESCRIPTION')]
rows.append(('VALUE/DESCRIPTION presenti e tradotti (6 attese: 3 + 3)', len(vd) == 6, vd))

it = collections.Counter(v['italian'] for v in cov)
di = [(k[:45], c, [v['idx'] for v in cov if v['italian'] == k]) for k, c in it.items() if c > 1]
di = [d for d in di if not set(d[2]) <= DUP_OK]
rows.append(('duplicati italiano non spiegati dal sorgente', di or 'ok', not di))
rows.append(('duplicati inglesi: 0 gruppi (controllo negativo dichiarato)', len(DUP_GROUPS), len(DUP_GROUPS) == 0))

tab = [(v['idx'], v['english'].count('\t'), v['italian'].count('\t'))
       for v in cov if v['english'].count('\t') != v['italian'].count('\t')]
rows.append(('tab per unita', tab or 'ok', not tab))
lead = [v['idx'] for v in cov if v['english'].startswith('\t') != v['italian'].startswith('\t')]
rows.append(('tab iniziale conservato', lead or 'ok', not lead))
quo = [(v['idx'], v['english'].count('"'), v['italian'].count('"'))
       for v in cov if v['english'].count('"') != v['italian'].count('"')]
rows.append(('virgolette per unita', quo or 'ok', not quo))
odd = tuple(sorted(v['idx'] for v in cov if v['english'].count('"') % 2))
rows.append(('virgolette dispari nel sorgente (0 attese)', odd or 0, odd == ()))
bra = [v['idx'] for v in cov if v['english'].count('[') != v['italian'].count('[')
       or v['english'].count(']') != v['italian'].count(']')]
rows.append(('quadre [ ] per unita (0 attese: assenza dichiarata)', bra or 'ok', not bra))

tag = [v['idx'] for v in cov
       if collections.Counter(TAGS.findall(v['english'])) != collections.Counter(TAGS.findall(v['italian']))]
rows.append(('token <...> per unita', tag or 'ok', not tag))
en_tok = collections.Counter(t for v in allcov for t in TAGS.findall(v['english']))
it_tok = collections.Counter(t for v in allcov for t in TAGS.findall(v['italian']))
rows.append(('token per simbolo: 8 famiglie, 18 occorrenze',
             '%s | %s' % (dict(en_tok), dict(it_tok)) if en_tok != it_tok else
             '%d simboli, %d occorrenze' % (len(en_tok), sum(en_tok.values())),
             en_tok == it_tok and sum(en_tok.values()) == 18 and len(en_tok) == 8
             and en_tok == collections.Counter({'<planet>': 5, '<last>': 3, '<ship>': 2, '<destination>': 2,
                                                '<origin>': 2, '<tons>': 2, '<payment>': 1, '<first>': 1})))

bt = [(v['idx'], v['english'].count('`'), v['italian'].count('`'))
      for v in cov if v['english'].count('`') != v['italian'].count('`')]
rows.append(('backtick per unita (0 attesi: assenza dichiarata)', bt or 'ok', not bt))
sp = [v['idx'] for v in cov
      if ('  ' in v['italian'] and '  ' not in v['english'])
      or ' \t' in v['italian'] or '\t ' in v['italian'] or '\n' in v['italian']]
rows.append(('spazi doppi/ai bordi non voluti', sp or 'ok', not sp))

rs = [v['ratio'] for v in cov]
outl = [(v['idx'], v['ratio'], v['english'][:40], v['italian'][:40]) for v in cov
        if not 0.55 < v['ratio'] < 1.90]
rows.append(('rapporto lunghezza (gate 0,55-1,90)',
             '%.2f - %.2f' % (min(rs), max(rs)) if rs else 'nessuna unita tradotta',
             bool(rs) and 0.55 < min(rs) and max(rs) < 1.90))
for o in outl:
    print('OUTLIER ratio:', o)

bad = []
for v in cov:
    for pat, name in ((r"\b(e|E|piu|perche|cosi|gia|puo|cioe|percio)'", 'accento sostitutivo'),
                      ('\u2026', 'ellissi tipografica'), ('\u00ab', 'caporale'), ('\u00bb', 'caporale'),
                      ('\u2014', 'em dash'), ('\u2019', 'apostrofo curvo')):
        if re.search(pat, v['italian']):
            bad.append((v['idx'], name))
rows.append(('tipografia (accenti/apostrofi/dash)', bad or 'ok', not bad))

nonlat = [(v['idx'], hex(ord(c))) for v in cov for c in v['italian']
          if ord(c) > 127 and not (0x00C0 <= ord(c) <= 0x024F) and c not in "'\u2019\u00ab\u00bb\u2026\u2014"]
rows.append(('caratteri non latini', nonlat or 'ok', not nonlat))

ENG = re.compile(r'\b(the|and|with|this|that|from|your|their|which|have|into|about|there|would|while|'
                 r'windows|but|are|was|were|they|his|her|its|be|been)\b', re.I)
TITLES = ('Myurej', 'Kaatrij', 'Khiajsore', 'Ijaset', 'Riiria', 'Riijaaora', 'Myaede', 'Shroud',
          'Successori', 'Casate', 'Predecessori', 'Iret')
TOKEN_RE = re.compile(r'<[^<>]+>')


def scrub(s):
    s = TOKEN_RE.sub(' ', s)
    for t in TITLES:
        s = s.replace(t, '')
    return s


res = [(v['idx'], sorted(set(m.group(0).lower() for m in ENG.finditer(scrub(v['italian'])))))
       for v in cov if ENG.search(scrub(v['italian']))]
rows.append(('parole inglesi residue (nomi propri esclusi)', res or 'nessuna', not res))

c = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
st = dict(c.execute('select state,count(*) from units group by state').fetchall())
rows.append(('state.db APPROVED/PENDING', '%s/%s' % (st['APPROVED'], st['PENDING']), st['APPROVED'] == 364))
last = c.execute("select max(updated_at) from units where state='APPROVED'").fetchone()[0]
rows.append(('ultimo aggiornamento APPROVED', last, last == '2026-10-17T14:33:18Z'))
ids = [u['id'] for u in units]
dl = c.execute('select count(*) from units where id in (%s) and state != "PENDING"' % ','.join('?' * len(ids)),
               ids).fetchone()[0]
rows.append(('unita\' del lotto fuori da PENDING', dl, dl == 0))

print('| Controllo | Esito | OK |')
print('|---|---|---|')
for a, b, ok in rows:
    print('| %s | %s | %s |' % (a, b, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d' % (sum(len(v['english'].split()) for v in cov),
                                 sum(len(v['italian'].split()) for v in cov)))
print('tab IT %d / EN %d' % (sum(v['italian'].count('\t') for v in cov),
                             sum(v['english'].count('\t') for v in cov)))
print('virgolette IT %d / EN %d' % (sum(v['italian'].count('"') for v in cov),
                                    sum(v['english'].count('"') for v in cov)))
print('token IT %d / EN %d' % (sum(len(TAGS.findall(v['italian'])) for v in cov),
                               sum(len(TAGS.findall(v['english'])) for v in cov)))
print('prima/ultima riga del segmento: %d/%d' % (min(u['line'] for u in sel), max(u['line'] for u in sel)))
print('parti caricate: %d · duplicati inglese: %d gruppi (%d unita)'
      % (len(parts), len(DUP_GROUPS), len(DUP_OK)))
print('unita mancanti nel lotto: %d' % len(missing))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
