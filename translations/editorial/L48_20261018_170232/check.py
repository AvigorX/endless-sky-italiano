r"""check.py — L48 (data/avgi/avgi side missions.txt, 180 unita', righe 26-499)

Deriva da check.py di L47. Differenze misurate sul `source.json` di questo lotto:

  - **linea Avgi, prima incursione**: nessun lotto precedente ha toccato questo file.
  - `NT` = **14 `UI_LABEL`** e **nessun riferimento di dato**: tutte le 14 righe `LOGBOOK` hanno il
    testo fra **backtick**, quindi `tools/l10n.py` estrae il **testo** (non la categoria). E' il primo
    lotto della serie in cui la lacuna dell'estrattore **non** si presenta: il `check.py` lo asserisce
    esplicitamente (`LOGBOOK` = 14 testi, 0 categorie).
  - **`LOGBOOK` 14**, di due forme: `log "Categoria" "Nome" \`testo\`` (11) e `log \`testo\`` (3).
  - **`CONVERSATION` 0, `DIALOG` 0, `VALUE` 0, `DESCRIPTION` 0**: asserzioni di assenza dichiarate.
    I tipi del segmento sono **solo tre**: 152 `MISSION_TEXT`, 14 `UI_LABEL`, 14 `LOGBOOK`.
  - **0 virgolette dispari, 0 quadre, 0 backtick**: assenze dichiarate (252 virgolette tutte in coppia).
  - **tab 145**: 145 unita' su 180 iniziano con tab; il costruttore antepone all'italiano i tab del
    sorgente (`ntab = len(en) - len(en.lstrip('\\\\t'))`); le parti si scrivono senza tab.
  - **10 token in 4 famiglie**: `<first>` 3, `<last>` 5, `<origin>` 1, `<ship>` 1.
  - `TOKEN_EXC` vuoto: nessuna eccezione ammessa.
  - **segmento interno**: il file ha 436 unita', 256 restano dopo la riga 499 (lotto L49).
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

# --- non traducibili: 14 label di salto, nessun riferimento di dato ---
NT_LABEL = set([28, 30, 37, 39, 46, 61, 63, 65, 67, 76, 94, 116, 118, 121])
NT_DATA = set()
NT = NT_LABEL | NT_DATA
NT_REASON = 'solo label di salto (goto): nessuna categoria di diario in questo lotto'

# --- righe di diario: tutte di testo (14) ---
LOG = set([84, 90, 99, 100, 101, 102, 103, 104, 105, 152, 153, 158, 176, 179])

# --- nodi di conversazione: nessuno (asserzione di assenza) ---
CONV = set()

# --- eccezioni sui token: nessuna (4 famiglie, tutte di dati) ---
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

ident = [(v['idx'], v['english'], v['italian']) for v in cov
         if v['idx'] in NT and v['italian'] != v['english']]
rows.append(('non traducibili lasciate identiche (%d attese)' % len([x for x in NT if lo <= x <= hi]),
             ident or 'ok', not ident))

# --- LOGBOOK: 14 righe, tutte di testo (nessuna categoria estratta) ---
log_sel = [x for x in LOG if lo <= x <= hi]
log_cov = [v for v in cov if v['idx'] in LOG]
log_missing = [i for i in log_sel if i not in {v['idx'] for v in log_cov}]
log_same = [v['idx'] for v in log_cov if v['italian'].strip() == v['english'].strip()]
rows.append(('righe log di testo tradotte (%d attese)' % len(log_sel),
             '%d/%d' % (len(log_cov), len(log_sel)), len(log_cov) == len(log_sel)))
rows.append(('righe log mancanti o lasciate in inglese',
             (log_missing or log_same) or 'ok', not log_missing and not log_same))
log_tab = [v['idx'] for v in log_cov if v['italian'].count('\t') != v['english'].count('\t')]
rows.append(('righe log con tab del sorgente', log_tab or 'ok', not log_tab))
raw_by_idx = {u['idx']: u['raw'] for u in units}
form_three = [i for i in LOG if re.match(r'\t+log "[^"]+" "[^"]+" `', raw_by_idx[i])]
form_one = [i for i in LOG if re.match(r'\t+log `', raw_by_idx[i])]
formed = set(form_three) | set(form_one)
_log_ok = formed == LOG and len(form_three) == 11 and len(form_one) == 3
rows.append(('forme di log: %d a tre argomenti, %d diretta' % (len(form_three), len(form_one)),
             'ok' if _log_ok else (sorted(form_three), sorted(form_one)), _log_ok))
# la lacuna dell'estrattore: qui NON si presenta, tutte le righe log hanno il testo nell'unita'
log_kinds = [u['idx'] for u in units if u['kind'] == 'LOGBOOK']
rows.append(('nessuna categoria estratta come unita (14 LOGBOOK = 14 testi)',
             'ok' if sorted(log_kinds) == sorted(LOG) else log_kinds,
             sorted(log_kinds) == sorted(LOG)))

# --- assenze dichiarate ---
conv = [v['idx'] for v in cov if v['kind'] == 'CONVERSATION']
rows.append(('nodi di conversazione (0 attesi: assenza dichiarata)', conv or 'ok', conv == []))
for kind in ('DIALOG', 'VALUE', 'DESCRIPTION'):
    k = [v['idx'] for v in cov if v['kind'] == kind]
    rows.append(('unita %s (0 attese: assenza dichiarata)' % kind, k or 'ok', k == []))

it = collections.Counter(v['italian'] for v in cov)
di = [(k[:45], c, [v['idx'] for v in cov if v['italian'] == k]) for k, c in it.items() if c > 1]
di = [d for d in di if not set(d[2]) <= DUP_OK]
rows.append(('duplicati italiano non spiegati dal sorgente', di or 'ok', not di))

tab = [(v['idx'], v['english'].count('\t'), v['italian'].count('\t'))
       for v in cov if v['english'].count('\t') != v['italian'].count('\t')]
rows.append(('tab per unita', tab or 'ok', not tab))
lead = [v['idx'] for v in cov if v['english'].startswith('\t') != v['italian'].startswith('\t')]
rows.append(('tab iniziale conservato', lead or 'ok', not lead))
quo = [(v['idx'], v['english'].count('"'), v['italian'].count('"'))
       for v in cov if v['english'].count('"') != v['italian'].count('"')]
rows.append(('virgolette per unita', quo or 'ok', not quo))
bra = [(v['idx'], v['english'].count('['), v['italian'].count('['),
        v['english'].count(']'), v['italian'].count(']'))
       for v in cov if v['english'].count('[') != v['italian'].count('[')
       or v['english'].count(']') != v['italian'].count(']')]
rows.append(('quadre [ ] per unita (0 attese: assenza dichiarata)', bra or 'ok', not bra))

tag = [v['idx'] for v in cov
       if collections.Counter(TAGS.findall(v['english'])) != collections.Counter(TAGS.findall(v['italian']))]
unexpected = sorted(set(tag) - TOKEN_EXC)
rows.append(('token <...> (eccezioni ammesse: %d)' % len([x for x in TOKEN_EXC if lo <= x <= hi]),
             unexpected or 'ok', not unexpected))

bt = [(v['idx'], v['english'].count('`'), v['italian'].count('`'))
      for v in cov if v['english'].count('`') != v['italian'].count('`')]
rows.append(('backtick per unita', bt or 'ok', not bt))
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
rows.append(('rapporto lunghezza',
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
TITLES = ('Avgi', 'Consonance', 'Electors', 'Assembly', 'Wisteria', 'Nikkio', 'Zapchannel',
          'Park Politics', 'Centralists', 'Technocrats', 'Financiers', 'Nationalists',
          'Ecologists', 'Freelancers', 'Captain')
TOKEN_RE = re.compile(r'<[^<>]+>')


def scrub(s):
    s = TOKEN_RE.sub(' ', s)
    for t in TITLES:
        s = s.replace(t, '')
    return s


res = [(v['idx'], sorted(set(m.group(0).lower() for m in ENG.finditer(scrub(v['italian'])))))
       for v in cov if v['idx'] not in NT and ENG.search(scrub(v['italian']))]
rows.append(('parole inglesi residue (istituzioni/navi escluse)', res or 'nessuna', not res))

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
print('parti caricate: %d · duplicati inglese: %d gruppi (%d unita)'
      % (len(parts), len(DUP_GROUPS), len(DUP_OK)))
print('unita mancanti nel lotto: %d' % len(missing))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
