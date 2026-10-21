"""check.py — L24 (data/remnant/remnant 1 introduction.txt, 1250 unita')

Deriva da check.py di L23. Novita' di L24:
  - `NT` = 43 unita', tutte `UI_LABEL`: la ricognizione del `source.json` mostra che ognuna e'
    una riga `label "..."` con indietro un `goto`, quindi un nome di nodo e non testo.
    Non ci sono `label` dentro blocchi `conversation` (verificato: 0 occorrenze nel `raw`).
  - `TOKEN_EXC` vuoto: nessun pronome-token nel sorgente (verificato unita' per unita').
  - `TITLES`: come L23; i nomi che restano in inglese si aggiungono qui man mano, mai allentando
    la regex.
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

# --- non traducibili: `label` dentro un blocco conversation (bersaglio di goto) ---
NT = {59, 249, 318, 385, 395, 427, 500, 542,
      870, 930, 932, 937, 944, 950, 958, 961, 963, 1014,
      1016, 1025, 1028, 1053, 1065, 1073, 1080, 1085, 1087, 1093,
      1103, 1117, 1126, 1138, 1152, 1156, 1162, 1175, 1192, 1201,
      1206, 1210, 1218, 1228, 1231}
NT_REASON = '43 label di salto (goto) dentro conversation: restano identiche'

# --- eccezioni sui token: pronomi inglesi resi con costruzione italiana ---
TOKEN_EXC = set()
PRON = re.compile(r"<(?:they've|they're|they are|they|their|them)>")

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

out = {'block': src['block'], 'note': src['note'], 'units': []}
missing = [u['idx'] for u in units if u['idx'] not in tr]
for u in units:
    if u['idx'] not in tr:
        continue
    it = tr[u['idx']]
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

tag = [v['idx'] for v in cov
       if collections.Counter(TAGS.findall(v['english'])) != collections.Counter(TAGS.findall(v['italian']))]
diff_tok = set(tag)
unexpected = sorted(diff_tok - TOKEN_EXC)
rows.append(('token <...> (eccezioni pronomi ammesse: %d)' % len([x for x in TOKEN_EXC if lo <= x <= hi]),
             unexpected or 'ok', not unexpected))
# le unita' in TOKEN_EXC devono contenere davvero un pronome e perdere solo quello
bad_exc = []
for v in cov:
    if v['idx'] not in TOKEN_EXC:
        continue
    en = collections.Counter(TAGS.findall(v['english']))
    itk = collections.Counter(TAGS.findall(v['italian']))
    lost = en - itk
    gained = itk - en
    if not PRON.search(v['english']) or lost != collections.Counter(PRON.findall(v['english'])) or gained:
        bad_exc.append((v['idx'], dict(lost), dict(gained)))
rows.append(('eccezioni token coerenti (solo pronomi persi)', bad_exc or 'ok', not bad_exc))

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
TITLES = ('Dirt Belt', 'Far North', 'Deep', 'Core', 'Rim', 'Earth Day', 'Bactrian',
          'There Might Be Riots', 'Songs for the End of Civilization', 'Trouble on the Tarmac')
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
