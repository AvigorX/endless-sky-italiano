r"""check.py — L47 (data/successors/successor 1 prologue.txt, 124 unita', righe 680-1024, fine file)

Deriva da check.py di L46. Differenze misurate sul `source.json` di questo lotto:

  - **fine file**: il segmento chiude il file (345 unita' totali = 221 di L46 + 124 di L47).
  - `NT` = **8 `UI_LABEL`** (label di salto) **piu' 1 riferimento di dato**: 54 e' un
    `log "People" "Saajret, of Somber Sejra" "testo"` con il **testo fra virgolette**:
    `tools/l10n.py` estrae come unita' la **categoria** (`People`), non il testo.
    Totale `NT` = 9, elencati uno per uno.
  - **`LOGBOOK` 4** = **3 di testo** (59, 67, 68) + **1 categoria** (54). Due forme convivono:
    `log "testo"` (59, 67) e `log "Categoria" "Nome" \`testo\`` (68, unita' = testo fra backtick).
  - **`CONVERSATION` 0**: asserzione di assenza dichiarata (il file ne ha altrove, il segmento no).
  - **2 virgolette dispari** (46, 63): battute aperte nel sorgente, riprodotte aperte; confronto come
    **insieme di idx**.
  - **1 unita' con quadre** (21): `HOUSE KAATRIJ [REQUESTS, REQUIRES] AUDIENCE OF HUMAN CAPTAIN`,
    annuncio in maiuscolo con parentesi quadre. Conteggio di `[` e `]` invariato per unita'.
  - **tab 102 caratteri su 100 unita'**: 98 unita' con 1 tab iniziale, 2 con 2 tab. Il costruttore
    antepone all'italiano i tab del sorgente (`ntab = len(en) - len(en.lstrip('\\\\t'))`); le parti si
    scrivono senza tab.
  - Tipi del lotto: 108 `MISSION_TEXT`, 8 `UI_LABEL`, 4 `LOGBOOK`, 2 `VALUE`, 2 `DESCRIPTION`.
    Nessun `DIALOG`, nessun `TEXT`, nessun `CONVERSATION`.
  - **24 token in 9 famiglie**: `<ship>` 7, `<origin>` 3, `<destination>` 2, `<coalition ally>` 2,
    `<first>` 2, `<last>` 3, `<system>` 1, `<successor patron>` 3, `<successor opponent>` 1.
  - `TOKEN_EXC` vuoto: nessuna eccezione ammessa.
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

# --- non traducibili: 8 label di salto + 1 riferimento di dato ---
NT_LABEL = set([6, 12, 18, 20, 79, 81, 85, 112])
NT_DATA = set([54])
NT = NT_LABEL | NT_DATA
NT_REASON = 'label di salto (goto) e riferimenti di dato (categoria di diario)'

# --- righe di diario di testo (la categoria e' in NT_DATA) ---
LOG = set([59, 67, 68])

# --- nodi di conversazione: nessuno in questo segmento (asserzione di assenza) ---
CONV = set()

# --- eccezioni sui token: nessuna (9 famiglie, tutte di dati) ---
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

# --- LOGBOOK di testo: controllo positivo (3 attese) ---
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
form1 = [i for i in LOG if re.match(r'\t+log "[^"]+"\s*$', raw_by_idx[i])]
form3 = [i for i in LOG if re.match(r'\t+log "[^"]+" "[^"]+" `', raw_by_idx[i])]
formed = set(form1) | set(form3)
_log_ok = formed == LOG and sorted(form1) == [59, 67] and sorted(form3) == [68]
rows.append(('forme di log: %d diretta, %d a tre argomenti' % (len(form1), len(form3)),
             'ok' if _log_ok else (sorted(form1), sorted(form3)), _log_ok))

# --- CONVERSATION: asserzione di assenza dichiarata ---
conv = [v['idx'] for v in cov if v['kind'] == 'CONVERSATION']
rows.append(('nodi di conversazione (0 attesi: assenza dichiarata)', conv or 'ok', conv == []))

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
rows.append(('quadre [ ] per unita', bra or 'ok', not bra))

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
TITLES = ('Successors', 'Successor', 'Myiara', 'Myiaran', 'Chydiyi', 'Myurej', 'Kaatrij', 'Seineq',
          'Sioeora', 'Somber Sejra', 'Saajret', 'Sijra', 'Rijatet', 'Kampa', 'Resja', 'Queru', 'Hasur',
          'Tiliia', 'Kijran', 'Kijra', 'Kiitaa', 'Khora', 'Kijran-Riitaa', 'Kijran-Khora',
          'Qasa-Sija-Iri', 'Osolaa-Val-Mavra', 'Kasii-Sola', 'Avasaa-Novaa', 'Raaqa-Uur-Kaav',
          'Jaasii', 'Vejret', 'Ijridanii', 'Sejra', 'Geminus', 'Martini', 'Predecessors',
          'Predecessori', 'Quarg', 'Houses', 'House', 'High Houses', 'Old and New', 'Coalition',
          'Hai', 'Shakespeare', 'Captain', 'archivist', 'Tempest')
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
