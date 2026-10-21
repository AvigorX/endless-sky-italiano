r"""check.py — L78 (data/successors/successor side missions.txt, 53 unita', righe 221-325)

Secondo lotto sul file, **un contesto intero**: `Ghosts Stargazing` -> `mission:Successors: Stargazing 1`.

Misure del sorgente, rimisurate (decisione 119):
  - **`UI_LABEL` 2** (unita' 47 `fah soom`, 50 `novel name`): entrambe restano **identiche** (in `NT`);
  - **0 `LOGBOOK`**, **0 `DIALOG`**, **0 `CONVERSATION`**, **0 `TEXT`**: assenze dichiarate;
  - **`VALUE` 1** (1) e **`DESCRIPTION` 1** (2);
  - **0 virgolette dispari** (86, tutte pari): assenza dichiarata (in L77 erano 2);
  - **5 gruppi di duplicati inglesi** (13/20, 15/22, 16/23, 39/41, 45/49): le due varianti dello stesso
    dialogo, e le due opzioni identiche — resa identica **voluta**;
  - **13 token** in 7 famiglie: `<ship>` 4, `<home system>` 4, e 1 ciascuno per `<planet stopovers>`,
    `<destination>`, `<date>`, `<origin>`, `<payment>`;
  - **46 tab** su **46 unita'**, 0 quadre, 0 backtick;
  - tipi: 49 `MISSION_TEXT` + 1 `VALUE` + 1 `DESCRIPTION` + 2 `UI_LABEL`.
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

NT = set([47, 50])

en_count = collections.Counter(u['english'] for u in units)
DUP_GROUPS = collections.OrderedDict()
for u in units:
    if en_count[u['english']] > 1:
        DUP_GROUPS.setdefault(u['english'], []).append(u['idx'])
DUP_OK = set(i for idxs in DUP_GROUPS.values() for i in idxs)
WANT_DUP = {frozenset([13, 20]), frozenset([15, 22]), frozenset([16, 23]),
            frozenset([39, 41]), frozenset([45, 49])}

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
rows.append(('traduzioni vuote', [v['idx'] for v in cov if not v['italian'].strip()] or 0,
             all(v['italian'].strip() for v in cov)))

ui = tuple(v['idx'] for v in cov if v['kind'] == 'UI_LABEL')
rows.append(('unita UI_LABEL nel segmento (2 attese: 47, 50)', ui or 'ok', ui == (47, 50)))
bad_ui = [i for i in NT if by_idx[i]['italian'] != by_idx[i]['english']]
rows.append(('label `fah soom` e `novel name` identiche', bad_ui or 'ok', not bad_ui))

for k in ('LOGBOOK', 'DIALOG', 'CONVERSATION', 'TEXT'):
    got = tuple(sorted(v['idx'] for v in cov if v['kind'] == k))
    rows.append(('%s nel segmento (0 attesi: assenza dichiarata)' % k, got or 0, got == ()))

KINDS = {'MISSION_TEXT': 49, 'VALUE': 1, 'DESCRIPTION': 1, 'UI_LABEL': 2}
kk = collections.Counter(u['kind'] for u in units)
rows.append(('distribuzione dei tipi (%s)' % ', '.join('%s %d' % (k, v) for k, v in sorted(KINDS.items())),
             ', '.join('%s %d' % (k, v) for k, v in sorted(kk.items())), dict(kk) == KINDS))
vd = sorted(v['idx'] for v in allcov if v['kind'] in ('VALUE', 'DESCRIPTION'))
rows.append(('VALUE/DESCRIPTION presenti e tradotti (2 attese: 1, 2)', vd == [1, 2], vd))

it = collections.Counter(v['italian'] for v in cov)
di = [(k[:45], c, [v['idx'] for v in cov if v['italian'] == k]) for k, c in it.items() if c > 1]
di = [d for d in di if not set(d[2]) <= DUP_OK]
rows.append(('duplicati italiano non spiegati dal sorgente', di or 'ok', not di))
got = set(frozenset(v) for v in DUP_GROUPS.values())
rows.append(('duplicati inglesi: 5 gruppi (13/20, 15/22, 16/23, 39/41, 45/49)',
             '%d gruppi' % len(got), got == WANT_DUP))
rows.append(('i cinque gruppi hanno resa identica',
             sum(1 for g in DUP_GROUPS.values() if len(set(by_idx[i]['italian'] for i in g)) == 1),
             all(len(set(by_idx[i]['italian'] for i in g)) == 1 for g in DUP_GROUPS.values())))

tab = [(v['idx'], v['english'].count('\t'), v['italian'].count('\t'))
       for v in cov if v['english'].count('\t') != v['italian'].count('\t')]
rows.append(('tab per unita', tab or 'ok', not tab))
lead = [v['idx'] for v in cov if v['english'].startswith('\t') != v['italian'].startswith('\t')]
rows.append(('tab iniziale conservato (46 unita con tab)', lead or 'ok', not lead))
quo = [(v['idx'], v['english'].count('"'), v['italian'].count('"'))
       for v in cov if v['english'].count('"') != v['italian'].count('"')]
rows.append(('virgolette per unita', quo or 'ok', not quo))
odd = tuple(sorted(v['idx'] for v in cov if v['english'].count('"') % 2))
rows.append(('virgolette dispari nel sorgente (0 attese: assenza dichiarata)', odd or 0, odd == ()))
bra = [v['idx'] for v in cov if v['english'].count('[') != v['italian'].count('[')
       or v['english'].count(']') != v['italian'].count(']')]
rows.append(('quadre [ ] per unita (0 attese)', bra or 'ok', not bra))

tag = [v['idx'] for v in cov
       if collections.Counter(TAGS.findall(v['english'])) != collections.Counter(TAGS.findall(v['italian']))]
rows.append(('token <...> per unita', tag or 'ok', not tag))
en_tok = collections.Counter(t for v in allcov for t in TAGS.findall(v['english']))
it_tok = collections.Counter(t for v in allcov for t in TAGS.findall(v['italian']))
want = collections.Counter({'<ship>': 4, '<home system>': 4, '<planet stopovers>': 1,
                            '<destination>': 1, '<date>': 1, '<origin>': 1, '<payment>': 1})
rows.append(('token per simbolo: 7 famiglie, 13 occorrenze',
             '%d simboli, %d occorrenze' % (len(en_tok), sum(en_tok.values())),
             en_tok == it_tok == want))

bt = [(v['idx'], v['english'].count('`'), v['italian'].count('`'))
      for v in cov if v['english'].count('`') != v['italian'].count('`')]
rows.append(('backtick nel tradotto (0 attesi)', bt or 'ok', not bt))
sp = [v['idx'] for v in cov
      if ('  ' in v['italian'] and '  ' not in v['english'])
      or ' \t' in v['italian'] or '\t ' in v['italian'] or '\n' in v['italian']]
rows.append(('spazi doppi/ai bordi non voluti', sp or 'ok', not sp))

rs = [v['ratio'] for v in cov]
for v in cov:
    if not 0.55 < v['ratio'] < 1.90:
        print('OUTLIER ratio:', v['idx'], v['ratio'], v['english'][:50], '|', v['italian'][:50])
rows.append(('rapporto lunghezza (gate 0,55-1,90)',
             '%.2f - %.2f' % (min(rs), max(rs)) if rs else 'nessuna',
             bool(rs) and 0.55 < min(rs) and max(rs) < 1.90))

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
                 r'but|are|was|were|they|his|her|its|be|been|thou|thee|thy|of)\b', re.I)
TITLES = ('Myurej', 'Aqrabe', 'Tiliia', 'Sola', 'Remnant', 'Hai', 'Successori', 'Predecessori', 'Casate',
          'Kaatrij', 'Vujlet', 'Kasii', 'Tangles', 'Quarg', 'Sieasej', 'Sioeora', 'Kaatiora', 'Nnesa',
          'Jaasora', 'Maspa', 'Mavra', 'Khosa', 'Kella', 'Saaqa', 'Viirja', 'Sol')
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
print('parti caricate: %d · duplicati inglese: %d gruppi (%d unita)' % (len(parts), len(DUP_GROUPS), len(DUP_OK)))
print('unita mancanti nel lotto: %d' % len(missing))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
