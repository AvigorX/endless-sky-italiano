r"""check.py — L68 (data/successors/successor 2 ghosts myurej.txt, 49 unita', righe 16-113)

Primo lotto su questo file (nuovo della linea Successors, dopo `successor 2 ghosts.txt` di L45 e
`successor 1 prologue.txt` di L46-L47). Un solo contesto: `Successors: Ghosts Myurej 1`.
Il file prosegue: riga 118 apre `mission:Successors: Ghosts Myurej 2` -> invariante di **segmento**,
non di file (0 unita' dopo la 113 NON e' richiesto).

Misure del sorgente (tutte rimisurate, non ereditate: decisione 119):
  - **`UI_LABEL` 1** (unita' 20, `label "follow up"`): resta identica;
  - **`LOGBOOK` 2**, di forma diversa:
      * unita' 23 (riga 67) = `log "People" "Riiria" "testo..."` -> l'estrattore ha preso la
        **CATEGORIA** (`People`), non il testo: e' la lacuna nota del cofanetto a tre argomenti fra
        virgolette (L45 195/305/357/418, L46 62, L47 54). La categoria resta **identica** (in `NT`):
        tradurla creerebbe una categoria doppia nel diario del giocatore, perche' le altre categorie
        dello stesso file non sono inventariate. Il **testo** di quella voce (descrizione di Riiria)
        e' **fuori inventario**: dichiarato in `review.md`, non riparabile qui.
      * unita' 24 (riga 68) = `log "testo..."` forma diretta -> si traduce;
  - **`VALUE` 1** (nome missione, riga 16) e **`DESCRIPTION` 1** (riga 17): controllo positivo;
  - **13 -> 10 token** in 5 famiglie (`<first>` 3, `<last>` 3, `<ship>` 2, `<destination>` 1,
    `<planet>` 1): il handoff L68 dichiarava 13, la sua stessa tabella ne somma 10 e il sorgente ne
    conta 10. Vince il workspace;
  - **42 tab** (42 unita' con tab iniziale), **90 virgolette**, **0 dispari**, **0 quadre**,
    **0 backtick**;
  - **2 gruppi di duplicati inglesi** (15/21 e 16/22: le stesse due battute di scelta ripetute nei
    due rami), resa italiana identica legittima.
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

# --- non traducibili: identiche e elencate una per una (decisione 151) ---
NT_LABEL = set([20])      # label di salto (goto): `follow up`
NT_DATA = set([23])       # categoria di diario (`People`) emersa da un log a tre argomenti
NT = NT_LABEL | NT_DATA
NT_REASON = '1 label di salto + 1 categoria di diario (`People`): restano identiche'

LOG = set([23, 24])
LOG_CAT = set([23])       # categoria: resta identica
LOG_TEXT = LOG - LOG_CAT  # testo: si traduce
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
rows.append(('unita UI_LABEL nel segmento (%d attese)' % len(ui_sel),
             '%s/%s' % (ui_all, ui_sel) if ui_all != ui_sel else ui_all, ui_all == ui_sel))
ident = [(v['idx'], v['english'], v['italian']) for v in cov
         if v['idx'] in NT and v['italian'] != v['english']]
rows.append(('non traducibili lasciate identiche (%d attese)' % len([x for x in NT if lo <= x <= hi]),
             ident or 'ok', not ident))

log_sel = [x for x in LOG if lo <= x <= hi]
rows.append(('righe LOGBOOK nel segmento (%d attese: controllo positivo)' % len(log_sel),
             len([v for v in cov if v['kind'] == 'LOGBOOK']) or 'ok',
             len([v for v in cov if v['kind'] == 'LOGBOOK']) == len(log_sel)))
log_cov = [v for v in cov if v['idx'] in LOG_TEXT]
log_missing = [i for i in sorted(LOG_TEXT) if lo <= i <= hi and i not in {v['idx'] for v in log_cov}]
log_same = [v['idx'] for v in log_cov if v['italian'].strip() == v['english'].strip()]
rows.append(('righe log di testo tradotte (%d attese)' % len([x for x in LOG_TEXT if lo <= x <= hi]),
             '%d/%d' % (len(log_cov), len([x for x in LOG_TEXT if lo <= x <= hi])),
             len(log_cov) == len([x for x in LOG_TEXT if lo <= x <= hi])))
rows.append(('righe log mancanti o lasciate in inglese',
             (log_missing or log_same) or 'ok', not log_missing and not log_same))
log_tab = [v['idx'] for v in log_cov if v['italian'].count('\t') != v['english'].count('\t')]
rows.append(('righe log con tab del sorgente', log_tab or 'ok', not log_tab))
cat_cov = [v for v in cov if v['idx'] in LOG_CAT]
cat_bad = [v['idx'] for v in cat_cov if v['italian'] != v['english']]
rows.append(('categorie di diario lasciate identiche (%d attese: `People`)'
             % len([x for x in LOG_CAT if lo <= x <= hi]), cat_bad or 'ok', not cat_bad))
raw_by_idx = {u['idx']: u['raw'] for u in units}
form_three = [i for i in LOG if re.match(r'\t+log "[^"]+" "[^"]+" "[^"]+"\s*$', raw_by_idx[i])]
form_backtick = [i for i in LOG if re.match(r'\t+log "[^"]+" "[^"]+" `', raw_by_idx[i])]
form_back = [i for i in LOG if re.match(r'\t+log `', raw_by_idx[i])]
form_quote = [i for i in LOG if re.match(r'\t+log "[^"]+"\s*$', raw_by_idx[i])]
formed = set(form_three) | set(form_backtick) | set(form_back) | set(form_quote)
rows.append(('forme di log: %d tre argomenti fra virgolette, %d tre con backtick, %d backtick, %d diretta'
             % (len(form_three), len(form_backtick), len(form_back), len(form_quote)),
             'ok' if formed == LOG else (sorted(form_three), sorted(form_backtick),
                                         sorted(form_back), sorted(form_quote)),
             formed == LOG))
log_kinds = [u['idx'] for u in units if u['kind'] == 'LOGBOOK']
rows.append(('categorie estratte come unita (1 attesa: unita 23 `People`, resta identica)',
             'ok' if sorted(log_kinds) == sorted(LOG) else log_kinds,
             sorted(log_kinds) == sorted(LOG)))

# --- DIALOG / TEXT / CONVERSATION: assenze dichiarate ---
dlg = [v['idx'] for v in cov if v['kind'] == 'DIALOG']
rows.append(('nodi dialog (0 attesi: assenza dichiarata)', dlg or 'ok', dlg == []))
txt = tuple(sorted(v['idx'] for v in cov if v['kind'] == 'TEXT'))
rows.append(('unita TEXT di phrase (0 attese: assenza dichiarata)', txt or 'ok', txt == ()))
conv = [v['idx'] for v in cov if v['kind'] == 'CONVERSATION']
rows.append(('nodi di conversazione (0 attesi: assenza dichiarata)', conv or 'ok', conv == []))

# --- tipi del segmento: controllo positivo sulla distribuzione misurata ---
KINDS = {'MISSION_TEXT': 44, 'VALUE': 1, 'DESCRIPTION': 1, 'UI_LABEL': 1, 'LOGBOOK': 2}
kk = collections.Counter(u['kind'] for u in units)
rows.append(('distribuzione dei tipi nel segmento (%s)' % ', '.join('%s %d' % (k, v) for k, v in sorted(KINDS.items())),
             ', '.join('%s %d' % (k, v) for k, v in sorted(kk.items())), dict(kk) == KINDS))
vd = [v['idx'] for v in allcov if v['kind'] in ('VALUE', 'DESCRIPTION')]
rows.append(('VALUE/DESCRIPTION presenti e tradotti (2 attese)', vd or 'ok', len(vd) == 2))

it = collections.Counter(v['italian'] for v in cov)
di = [(k[:45], c, [v['idx'] for v in cov if v['italian'] == k]) for k, c in it.items() if c > 1]
di = [d for d in di if not set(d[2]) <= DUP_OK]
rows.append(('duplicati italiano non spiegati dal sorgente', di or 'ok', not di))
rows.append(('duplicati inglesi spiegati dal sorgente (2 gruppi: 15/21, 16/22)',
             '%d gruppi / %d unita' % (len(DUP_GROUPS), len(DUP_OK)),
             len(DUP_GROUPS) == 2 and DUP_OK == {15, 16, 21, 22}))

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
rows.append(('token per simbolo: 5 famiglie, 10 occorrenze',
             '%s | %s' % (dict(en_tok), dict(it_tok)) if en_tok != it_tok else
             '%d simboli, %d occorrenze' % (len(en_tok), sum(en_tok.values())),
             en_tok == it_tok and sum(en_tok.values()) == 10 and len(en_tok) == 5))

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
TITLES = ('Myurej', 'Kaatrij', 'Chydiyi', 'Sioeora', 'Riijaaora', 'Riiria', 'Kasii-Tuur-Saqru',
          'Vade-Osolaa-Kaska', 'Kvelqden', 'Myaede', 'Successori', 'Casa', 'Casate')
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
