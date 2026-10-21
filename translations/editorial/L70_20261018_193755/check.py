r"""check.py — L70 (data/successors/successor 2 ghosts myurej.txt, 39 unita', righe 198-307)

Terzo lotto sul file (dopo L68 e L69). Un solo contesto: `Successors: Ghosts Myurej 4`.
Il file **prosegue** (riga 311 apre `Myurej 5`): invariante di **segmento**, non di file.

Misure del sorgente, tutte rimisurate (decisione 119):
  - **`NT` 3**, e non per il motivo di L68:
      * unita' 30 = `label "not met solitude enforcers"` (bersaglio di salto) -> resta identica;
      * unita' **7 e 10** = `government \`People's Houses (Hostile)\``: sono **riferimenti di dato**
        (nome di governo) che il parser classifica `MISSION_TEXT`. Tradurli romperebbe la logica della
        missione: restano identici ed elencati uno per uno, e il controllo `raw` lo documenta;
  - **`LOGBOOK` 3** (unita' 8, 35, 37): tutte e tre forma **diretta** (`log "testo"`), nessuna categoria
    emersa come unita' -> `LOG_CAT` vuoto;
  - **`VALUE` 1** e **`DESCRIPTION` 1** (unita' 1-2), con due `LOGBOOK` alternativi (accettato / rifiutato);
  - **5 token** in 4 famiglie: `<ship>` 2, `<destination>` 1, `<origin>` 1, `<planet>` 1;
  - **28 tab su 28 unita'** (tutte le 28 tradotte con tab iniziale), **64 virgolette**, **0 dispari**,
    **0 quadre**, **0 backtick**;
  - tipi: 33 `MISSION_TEXT` + 1 `VALUE` + 1 `DESCRIPTION` + 3 `LOGBOOK` + 1 `UI_LABEL`; 0 `DIALOG`.
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

# --- non traducibili: 1 label + 2 riferimenti di dato, elencati uno per uno (decisione 151) ---
NT_LABEL = set([30])
NT_DATA = set([7, 10])
NT = NT_LABEL | NT_DATA
NT_REASON = '1 label di salto + 2 riferimenti di dato (`government`): restano identici'

LOG = set([8, 35, 37])
LOG_CAT = set()
LOG_TEXT = LOG - LOG_CAT
DIALOG = set()
TEXT = set()
CONV = set()
TOKEN_EXC = set()

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
    ntab = len(en) - len(en.lstrip('\t'))
    return '\t' * ntab + it


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
ui_sel = tuple(sorted(x for x in NT_LABEL if lo <= x <= hi))
rows.append(('unita UI_LABEL nel segmento (1 attesa)',
             '%s/%s' % (ui_all, ui_sel) if ui_all != ui_sel else ui_all, ui_all == ui_sel))
ident = [(v['idx'], v['english'], v['italian']) for v in cov
         if v['idx'] in NT and v['italian'] != v['english']]
rows.append(('non traducibili lasciate identiche (3 attese: 30 label, 7 e 10 `government`)',
             ident or 'ok', not ident))
rows.append(('i due riferimenti `government` sono le unita 7 e 10',
             tuple(sorted(i for i in NT_DATA if lo <= i <= hi)) == (7, 10),
             sorted(NT_DATA)))

log_units = [v['idx'] for v in cov if v['kind'] == 'LOGBOOK']
log_sel = [x for x in LOG if lo <= x <= hi]
rows.append(('righe LOGBOOK nel segmento (%d attese: controllo positivo)' % len(log_sel),
             log_units or 'ok', log_units == log_sel))
log_cov = [v for v in cov if v['idx'] in LOG_TEXT]
log_same = [v['idx'] for v in log_cov if v['italian'].strip() == v['english'].strip()]
rows.append(('righe log di testo tradotte (%d attese)' % len(log_sel),
             '%d/%d' % (len(log_cov), len(log_sel)), len(log_cov) == len(log_sel)))
rows.append(('righe log lasciate in inglese', log_same or 'ok', not log_same))
log_tab = [v['idx'] for v in log_cov if v['italian'].count('\t') != v['english'].count('\t')]
rows.append(('righe log con tab del sorgente', log_tab or 'ok', not log_tab))
raw_by_idx = {u['idx']: u['raw'] for u in units}
form_three = [i for i in LOG if re.match(r'\t+log "[^"]+" "[^"]+" "[^"]+"\s*$', raw_by_idx[i])]
form_three_bt = [i for i in LOG if re.match(r'\t+log "[^"]+" "[^"]+" `', raw_by_idx[i])]
form_back = [i for i in LOG if re.match(r'\t+log `', raw_by_idx[i])]
form_quote = [i for i in LOG if re.match(r'\t+log "[^"]+"\s*$', raw_by_idx[i])]
formed = set(form_three) | set(form_three_bt) | set(form_back) | set(form_quote)
rows.append(('forme di log: %d tre argomenti, %d tre con backtick, %d backtick, %d diretta'
             % (len(form_three), len(form_three_bt), len(form_back), len(form_quote)),
             'ok' if formed == LOG and set(form_quote) == LOG else
             (sorted(form_three), sorted(form_three_bt), sorted(form_back), sorted(form_quote)),
             formed == LOG and set(form_quote) == LOG))
rows.append(('categorie estratte come unita (0 attese: nessuna categoria in questo lotto)',
             sorted(LOG_CAT) or 'ok', LOG_CAT == set()))

dlg = [v['idx'] for v in cov if v['kind'] == 'DIALOG']
rows.append(('nodi dialog (0 attesi: assenza dichiarata)', dlg or 'ok', dlg == []))
txt = tuple(sorted(v['idx'] for v in cov if v['kind'] == 'TEXT'))
rows.append(('unita TEXT di phrase (0 attese: assenza dichiarata)', txt or 'ok', txt == ()))
conv = [v['idx'] for v in cov if v['kind'] == 'CONVERSATION']
rows.append(('nodi di conversazione (0 attesi: assenza dichiarata)', conv or 'ok', conv == []))

KINDS = {'MISSION_TEXT': 33, 'VALUE': 1, 'DESCRIPTION': 1, 'LOGBOOK': 3, 'UI_LABEL': 1}
kk = collections.Counter(u['kind'] for u in units)
rows.append(('distribuzione dei tipi nel segmento (%s)' % ', '.join('%s %d' % (k, v) for k, v in sorted(KINDS.items())),
             ', '.join('%s %d' % (k, v) for k, v in sorted(kk.items())), dict(kk) == KINDS))
vd = [v['idx'] for v in allcov if v['kind'] in ('VALUE', 'DESCRIPTION')]
rows.append(('VALUE/DESCRIPTION presenti e tradotti (2 attese)', vd or 'ok', len(vd) == 2))
two_alt = by_idx[35]['italian'] != by_idx[37]['italian']
rows.append(('due LOGBOOK alternativi (accettato 35 / rifiutato 37) presenti e distinti',
             'ok' if two_alt else 'identici', two_alt))

it = collections.Counter(v['italian'] for v in cov)
di = [(k[:45], c, [v['idx'] for v in cov if v['italian'] == k]) for k, c in it.items() if c > 1]
di = [d for d in di if not set(d[2]) <= DUP_OK]
rows.append(('duplicati italiano non spiegati dal sorgente', di or 'ok', not di))
rows.append(('duplicati inglesi spiegati dal sorgente (1 gruppo: 7/10, riferimento di governo)',
             '%d gruppi / %d unita' % (len(DUP_GROUPS), len(DUP_OK)),
             len(DUP_GROUPS) == 1 and DUP_OK == {7, 10}))

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
bra = [(v['idx'], v['english'].count('['), v['italian'].count('['),
        v['english'].count(']'), v['italian'].count(']'))
       for v in cov if v['english'].count('[') != v['italian'].count('[')
       or v['english'].count(']') != v['italian'].count(']')]
rows.append(('quadre [ ] per unita (0 attese: assenza dichiarata)', bra or 'ok', not bra))

tag = [v['idx'] for v in cov
       if collections.Counter(TAGS.findall(v['english'])) != collections.Counter(TAGS.findall(v['italian']))]
unexpected = sorted(set(tag) - TOKEN_EXC)
rows.append(('token <...> per unita (eccezioni ammesse: %d)' % len([x for x in TOKEN_EXC if lo <= x <= hi]),
             unexpected or 'ok', not unexpected))
en_tok = collections.Counter(t for v in allcov for t in TAGS.findall(v['english']))
it_tok = collections.Counter(t for v in allcov for t in TAGS.findall(v['italian']))
rows.append(('token per simbolo: 4 famiglie, 5 occorrenze',
             '%s | %s' % (dict(en_tok), dict(it_tok)) if en_tok != it_tok else
             '%d simboli, %d occorrenze' % (len(en_tok), sum(en_tok.values())),
             en_tok == it_tok and sum(en_tok.values()) == 5 and len(en_tok) == 4
             and en_tok == collections.Counter({'<ship>': 2, '<destination>': 1,
                                                '<origin>': 1, '<planet>': 1})))

bt = [(v['idx'], v['english'].count('`'), v['italian'].count('`'))
      for v in cov if v['english'].count('`') != v['italian'].count('`')]
rows.append(('backtick per unita (0 attesi: assenza dichiarata)', bt or 'ok', not bt))
sig = [(v['idx'], v['english'][:1] == ' ', v['italian'][:1] == ' ', v['english'][-1:] in (' ', '\t'),
        v['italian'][-1:] in (' ', '\t')) for v in cov
       if (v['english'][:1] == ' ') != (v['italian'][:1] == ' ')
       or (v['english'][-1:] in (' ', '\t')) != (v['italian'][-1:] in (' ', '\t'))]
rows.append(('spazio iniziale/finale come il sorgente', sig or 'ok', not sig))
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
if outl:
    for o in outl:
        print('OUTLIER ratio:', o)

bad = []
for v in cov:
    s = v['italian']
    for pat, name in ((r"\b(e|E|piu|perche|cosi|gia|puo|cioe|percio)'", 'accento sostitutivo'),
                      ('\u2026', 'ellissi tipografica'), ('\u00ab', 'caporale'), ('\u00bb', 'caporale'),
                      ('\u2014', 'em dash'), ('\u2019', 'apostrofo curvo')):
        if re.search(pat, s):
            bad.append((v['idx'], name))
rows.append(('tipografia (accenti/apostrofi/dash)', bad or 'ok', not bad))

nonlat = [(v['idx'], hex(ord(c))) for v in cov for c in v['italian']
          if ord(c) > 127 and not (0x00C0 <= ord(c) <= 0x024F) and c not in "'\u2019\u00ab\u00bb\u2026\u2014"]
rows.append(('caratteri non latini', nonlat or 'ok', not nonlat))

ENG = re.compile(r'\b(the|and|with|this|that|from|your|their|which|have|into|about|there|would|while|'
                 r'windows|but|are|was|were|they|his|her|its|be|been)\b', re.I)
TITLES = ('Myurej', 'Kaatrij', 'Chydiyi', 'Sioeora', 'Aqrabe', 'Riiria', 'Raaqa-Kvelq-Ryuit',
          'Shroud', 'Successori', 'Casate', 'Predecessori')
TOKEN_RE = re.compile(r'<[^<>]+>')


def scrub(s):
    s = TOKEN_RE.sub(' ', s)
    for t in TITLES:
        s = s.replace(t, '')
    return s


res = [(v['idx'], sorted(set(m.group(0).lower() for m in ENG.finditer(scrub(v['italian'])))))
       for v in cov if v['idx'] not in NT and ENG.search(scrub(v['italian']))]
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
