"""check.py — L45 (data/successors/successor 2 ghosts.txt, 680 unita', righe 37-2167, fine file)

Deriva da check.py di L44. Differenze misurate sul `source.json` di questo lotto:

  - `NT` = **26 `UI_LABEL`** (label di salto) **piu' 8 riferimenti di dato**:
      * 195, 305, 357, 418 — `log "Categoria" "Nome" "testo"` con il **testo fra virgolette** invece che
        fra backtick: `tools/l10n.py` estrae come unita' la **categoria** (`People`, `Factions`), non il
        testo. La categoria e' un riferimento di dato del diario: resta identica.
      * 355, 467, 513, 552 — `government `...``: nomi di governo usati come riferimento, non prosa.
    Totale `NT` = 34, elencati uno per uno.
  - **`LOGBOOK` 23**, di cui **19 di testo** (le altre 4 sono le categorie qui sopra): controllo positivo
    su 19 righe, nessuna identica all'inglese.
  - **`CONVERSATION` 16** (135-138, 256-267): **prima volta nella serie**. Sono nodi di conversazione con
    il testo fra backtick (`english` senza backtick, con i tab interni). Controllo dedicato: 16 attese,
    nessuna identica all'inglese.
  - **11 unita' con quadre** (651, 652, 653, 655, 657, 664, 666, 667, 668, 669, 670): sono i marcatori
    `[...]` dei frammenti redatti. Il controllo e' per unita' (conteggio di `[` e `]` invariato), non
    un'asserzione di assenza come in L44.
  - **tab 526**: il costruttore antepone all'italiano i tab iniziali del sorgente
    (`ntab = len(en) - len(en.lstrip('\\\\t'))`); le parti si scrivono senza tab.
  - Tipi del lotto: 559 `MISSION_TEXT`, 26 `UI_LABEL`, 23 `LOGBOOK`, 21 `DESCRIPTION`, 20 `VALUE`,
    16 `CONVERSATION`, 15 `DIALOG`. Nessun `TEXT`.
  - **15 unita' con virgolette dispari**: 15, 95, 159, 163, 479, 524, 525, 611, 612, 651, 652, 657,
    666, 667, 669.
  - `TOKEN_EXC` vuoto: 102 token in 14 famiglie, tutte di dati.
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

# --- non traducibili: 26 label di salto + 8 riferimenti di dato ---
NT_LABEL = set([12, 51, 56, 99, 186, 206, 208, 218, 221, 349, 434, 473, 533, 536, 574, 578, 616, 627,
                632, 636, 639, 641, 643, 654, 656, 658])
NT_DATA = set([195, 305, 357, 418, 355, 467, 513, 552])
NT = NT_LABEL | NT_DATA
NT_REASON = 'label di salto (goto) e riferimenti di dato (categoria di diario, nome di governo)'

# --- righe di diario di testo (le 4 categorie sono in NT_DATA) ---
LOG = set([1, 7, 25, 59, 125, 151, 231, 252, 255, 282, 304, 356, 554, 586,
           651, 652, 653, 655, 657])

# --- nodi di conversazione ---
CONV = set([135, 136, 137, 138, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267])
# opzioni di dialogo che in italiano restano identiche per forza: (No.) e' (No.)
CONV_SAME = set([137])

# --- eccezioni sui token: nessuna (14 famiglie, tutte di dati) ---
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

# il costruttore aggiunge i tab iniziali del sorgente: le parti si scrivono senza tab
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

# --- LOGBOOK di testo: controllo positivo (19 attese) ---
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

# --- CONVERSATION: controllo dedicato (16 attese) ---
conv_sel = [x for x in CONV if lo <= x <= hi]
conv_cov = [v for v in cov if v['idx'] in CONV]
rows.append(('nodi di conversazione tradotti (%d attese)' % len(conv_sel),
             '%d/%d' % (len(conv_cov), len(conv_sel)), len(conv_cov) == len(conv_sel)))
conv_same = [v['idx'] for v in conv_cov
             if v['italian'].strip() == v['english'].strip() and v['idx'] not in CONV_SAME]
rows.append(('nodi di conversazione lasciati in inglese', conv_same or 'ok', not conv_same))

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
# quadre: marcatori [...] dei frammenti redatti. Il numero di [ e ] deve restare identico per unita'.
bra = [(v['idx'], v['english'].count('['), v['italian'].count('['),
        v['english'].count(']'), v['italian'].count(']'))
       for v in cov if v['english'].count('[') != v['italian'].count('[')
       or v['english'].count(']') != v['italian'].count(']')]
rows.append(('quadre [ ] per unita', bra or 'ok', not bra))

tag = [v['idx'] for v in cov
       if collections.Counter(TAGS.findall(v['english'])) != collections.Counter(TAGS.findall(v['italian']))]
diff_tok = set(tag)
unexpected = sorted(diff_tok - TOKEN_EXC)
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
          'Tiliia', 'Kijran', 'Kijran-Khora', 'Qasa-Sija-Iri', 'Osolaa-Val-Mavra', 'Kasii-Sola',
          'Avasaa-Novaa', 'Geminus', 'Martini', 'Predecessors', 'Predecessori', 'Quarg', 'House',
          'Houses', 'High Houses', 'New Houses', 'Captain', 'archivist')
TOKEN_RE = re.compile(r'<[^<>]+>')


def scrub(s):
    s = TOKEN_RE.sub(' ', s)   # un token <...> non e' prosa: la parita' dei token e' un altro controllo
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
