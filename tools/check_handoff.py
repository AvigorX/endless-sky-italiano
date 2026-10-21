"""check_handoff.py — verifica che i numeri dichiarati dall'handoff corrente siano quelli reali.

Uso:
    python staging/editorial/tools/check_handoff.py [file.md]

Senza argomenti prende il file `HANDOFF_*.md` piu' recente (per nome) nella radice del workspace.

Ogni misura dichiarata nel documento viene **estratta dal documento** e confrontata con il workspace:
unita' e parole dello staging, copertura per file, numero di lotti, stato del database, residui, tabella del
prossimo lotto (righe, unita', parole, contesti, tab/virgolette, confine), hash dei file protetti e dei
lotti, stato del repository originale. Esce 0 se tutto combacia, 1 se qualcosa e' cambiato.

Nota di manutenzione (2026-10-17, chiusura L19): la versione precedente confrontava con valori **cablati**
per la transizione L18 -> L19 (per esempio la stringa '501/ 4253 unita'' e il blocco fisso righe
1811-2375). Alla chiusura di L19 quel documento non descrive piu' il workspace — correttamente — ma lo
strumento falliva su 8 controlli su 29 anche con un handoff giusto, perche' verificava il lotto *precedente*
invece del prossimo. Ora i valori attesi si leggono dal documento; **se un numero non c'e' nel documento il
controllo fallisce**, cosi' non si puo' "passare" omettendo i dati.

Nota di manutenzione (2026-10-17, L21): la tabella del prossimo lotto puo' descrivere un file diverso da
`human missions.txt`; si legge la cella `File` e le query usano quel percorso. Senza la cella il
comportamento resta quello di prima (`human missions.txt`). Serve per i lotti che attraversano piu' file.

Nota di manutenzione (2026-10-17, chiusura L20): la cella `Confine dopo` accetta anche la forma
`fine file`. Serve per l'ultimo segmento di un file: li' non esiste un'unita' successiva, e la
versione precedente falliva sempre (`nxt is None`) pur con un handoff corretto. Il controllo ora
verifica che **non** ci siano unita' dopo la riga finale dichiarata.
"""
import glob
import hashlib
import json
import os
import re
import sqlite3
import subprocess
import sys

L10N = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
REPO = os.path.abspath(os.path.join(L10N, '..', 'endless-sky'))

if len(sys.argv) > 1:
    DOC = sys.argv[1]
else:
    cands = sorted(glob.glob(os.path.join(L10N, 'HANDOFF_*.md')))
    DOC = cands[-1] if cands else os.path.join(L10N, 'HANDOFF.md')

doc = open(DOC, encoding='utf-8').read()
c = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
q = lambda s, *a: c.execute(s, a).fetchone()

print('documento:', os.path.basename(DOC))
print()

ok = []


def ck(name, cond, detail=''):
    ok.append((name, bool(cond), detail))


def grab(pattern, flags=0):
    """Primo gruppo (o tupla di gruppi) del documento; None se il pattern non c'e'."""
    m = re.search(pattern, doc, flags)
    if not m:
        return None
    return m.group(1) if m.lastindex == 1 else m.groups()


def num(s):
    return int(s.replace('.', '').replace(',', ''))


# --- misure reali ---
lots = {}
per_file = {}
for f in sorted(glob.glob(os.path.join(L10N, 'staging/editorial/L*/translation.json'))):
    d = json.load(open(f, encoding='utf-8'))['units']
    if not d:
        continue
    lots[os.path.basename(os.path.dirname(f))] = (
        len(d), sum(len(x['english'].split()) for x in d), sum(len(x['italian'].split()) for x in d))
    pf = per_file.setdefault(d[0]['path'], [0, 0, 0])
    pf[0] += len(d)
    pf[1] += sum(len(x['english'].split()) for x in d)
    pf[2] += sum(len(x['italian'].split()) for x in d)

n_lots = len(lots)
U = sum(v[0] for v in lots.values())
E = sum(v[1] for v in lots.values())
I = sum(v[2] for v in lots.values())

MIS = 'data/human/human missions.txt'
PLA = 'data/map planets.txt'
st = dict(c.execute('select state, count(*) from units group by state').fetchall())
lab = q("select count(*) from units where state='PENDING' and kind='UI_LABEL'")[0]
tot_mis = q('select count(*) from units where path=?', MIS)[0]
tot_pla = q('select count(*) from units where path=?', PLA)[0]

# --- totale dello staging ---
g = grab(r'TOTALE staging: ([\d.]+) unità · ([\d.]+) EN · ([\d.]+) IT')
ck('totale unita\' in staging', g is not None and tuple(map(num, g)) == (U, E, I), (g, (U, E, I)))
ck('parole EN/IT in staging', g is not None and (num(g[1]), num(g[2])) == (E, I), (g, (E, I)))

# --- copertura per file (righe in stile state.py) ---
for path, tot_units in ((MIS, tot_mis), (PLA, tot_pla)):
    g = grab(r'%s\s+(\d+)/ (\d+) unità \(\s*([\d.]+)%%\)' % re.escape(path))
    got = per_file.get(path, [0, 0, 0])
    pct = 100.0 * got[0] / tot_units if tot_units else 0.0
    ck('copertura %s' % os.path.basename(path),
       g is not None and int(g[0]) == got[0] and int(g[1]) == tot_units and abs(float(g[2]) - pct) < 0.05,
       (g, (got[0], tot_units, round(pct, 1))))

ck('conteggio lotti', grab(r'(\d+) directory') == str(n_lots), (grab(r'(\d+) directory'), n_lots))
ck('DB APPROVED/PENDING',
   grab(r'APPROVED (\d+) · PENDING (\d+)') == (str(st['APPROVED']), str(st['PENDING'])),
   (grab(r'APPROVED (\d+) · PENDING (\d+)'), (st['APPROVED'], st['PENDING'])))
ck('label non traducibili', grab(r'non traducibili\): (\d+)') == str(lab),
   (grab(r'non traducibili\): (\d+)'), lab))
ck('residuo traducibile', grab(r'residuo traducibile: ([\d.]+)') == str(st['PENDING'] - U - lab),
   (grab(r'residuo traducibile: ([\d.]+)'), st['PENDING'] - U - lab))

# --- residuo del file in lavorazione, ancorato alla riga dichiarata ---
g = grab(r'([\d.]+) unità / ([\d.]+) parole\*\* dopo la riga (\d+)')
if g:
    rest_mis = q('select count(*), sum(length(english)-length(replace(english," ",""))+1) '
                 'from units where path=? and line>?', MIS, int(g[2]))
    rest_mis = (rest_mis[0], rest_mis[1] or 0)   # file completo: sum() su zero righe vale NULL
    ck('residuo missions dopo la riga %s' % g[2],
       (num(g[0]), num(g[1])) == (rest_mis[0], rest_mis[1]), (g[:2], rest_mis))
else:
    ck('residuo missions', False, 'riga "N unità / M parole dopo la riga X" non trovata')

# --- tabella del prossimo lotto (parsing per riga: niente regex sulle barre) ---
def table_value(label):
    """Valore della cella di una riga `| Etichetta | Valore |` della tabella del prossimo lotto."""
    for line in doc.splitlines():
        cells = [x.strip() for x in line.strip().strip('|').split('|')]
        if len(cells) == 2 and cells[0] == label:
            return cells[1]
    return None

def bold(text):
    """Toglie i marcatori **...** dalla cella (il valore puo' contenere altro testo dopo)."""
    return text.replace('**', '') if text else text

file_cell = bold(table_value('File'))
PATH_NEXT = MIS
if file_cell:
    mfile = re.search(r'(data/[A-Za-z0-9_./ \-]+\.txt)', file_cell)
    if mfile:
        PATH_NEXT = mfile.group(1).strip()

righe = bold(table_value('Righe'))
unita = bold(table_value('Unità'))
parole = bold(table_value('Parole'))
contesti = bold(table_value('Contesti'))
tabq = bold(table_value('Tab / virgolette'))
confine = bold(table_value('Confine dopo'))

if all((righe, unita, parole, contesti, tabq, confine)):
    a, b = [int(x) for x in righe.replace('–', '-').split('-')]
    rows = c.execute('select line, context, kind, english from units where path=? and line between ? and ? '
                     'order by line', (PATH_NEXT, a, b)).fetchall()
    ctxs = []
    for line, ctx, kind, eng in rows:
        if ctx not in ctxs:
            ctxs.append(ctx)
    words = sum(len(e.split()) for _l, _c, _k, e in rows)
    tab = sum(1 for _l, _c, _k, e in rows if e.startswith('	'))
    quo = sum(e.count('"') for _l, _c, _k, e in rows)

    def bare(x):
        return x.split(':', 1)[1] if ':' in x else x

    n_ctx = num(contesti.split()[0])
    first = contesti.split('`')[1] if '`' in contesti else None
    last = contesti.split('`')[-2] if contesti.count('`') >= 4 else None
    tq = tabq.split(' / ')

    ck('prossimo lotto: righe %d-%d' % (a, b), len(rows) > 0, len(rows))
    ck("prossimo lotto: unita'", num(unita) == len(rows), (unita, len(rows)))
    ck('prossimo lotto: parole', num(parole) == words, (parole, words))
    ck('prossimo lotto: contesti',
       n_ctx == len(ctxs) and bare(ctxs[0]) == first and bare(ctxs[-1]) == last,
       ((n_ctx, first, last), (len(ctxs), ctxs[0] if ctxs else None, ctxs[-1] if ctxs else None)))
    ck('prossimo lotto: tab/virgolette',
       len(tq) == 2 and (num(tq[0]), num(tq[1])) == (tab, quo), (tabq, (tab, quo)))
    nxt = q('select line, context from units where path=? and line>? order by line limit 1', PATH_NEXT, b)
    m = re.search(r'riga (\d+) apre `([^`]+)`', confine or '')
    if confine and confine.strip().lower().startswith('fine file'):
        # caso terminale: il lotto finisce con l'ultima unita' del file, quindi non esiste
        # un'unita' successiva da confrontare. Il confine e' valido solo se dopo `b` non c'e' nulla.
        ck('prossimo lotto: confine dopo (fine file)', nxt is None, (confine, nxt, b))
    else:
        ck('prossimo lotto: confine dopo',
           m is not None and nxt is not None and (nxt[0], nxt[1]) == (int(m.group(1)), m.group(2)),
           (confine, nxt))
else:
    ck('prossimo lotto: tabella completa', False,
       'mancano Righe/Unità/Parole/Contesti/Tab/Confine nella sezione del prossimo lotto')

# --- hash dei file protetti, presi dal manifest e cercati nel documento ---
MANIFEST = os.path.join(L10N, 'staging/editorial/tools/protected.sha256')
REQUIRED = ('state.db', 'glossary.csv', 'staging/inventory_fields.csv', 'tools/l10n.py')
if os.path.exists(MANIFEST):
    for line in open(MANIFEST, encoding='utf-8'):
        want, path = line.split('  ', 1)
        path = path.strip()
        got = hashlib.sha256(open(os.path.join(L10N, path), 'rb').read()).hexdigest()
        if path not in REQUIRED and got[:16] not in doc:
            continue  # i tre output _ui non sono citati per hash: li copre state.py
        ck('hash %s nel doc' % path.split('/')[-1],
           got.startswith(want[:16]) and got[:16] in doc, (got[:16], want[:16]))
else:
    ck('manifest protetto presente', False, MANIFEST)

# --- hash dei lotti citati nel documento ---
for lab_, h in re.findall(r'`(L[0-9a-z]+) ([0-9a-f]{16})`', doc):
    dirs = [d for d in lots if d == lab_ or d.startswith(lab_ + '_')]
    if not dirs:
        ck('hash %s nel doc' % lab_, False, 'lotto non trovato in staging')
        continue
    f = os.path.join(L10N, 'staging/editorial', dirs[0], 'translation.json')
    got = hashlib.sha256(open(f, 'rb').read()).hexdigest()[:16]
    ck('hash %s nel doc' % lab_, got == h, (got, h))

# --- repository originale ---
head = subprocess.run(['git', '-C', REPO, 'rev-parse', '--short', 'HEAD'],
                      capture_output=True, text=True).stdout.strip()
dirty = subprocess.run(['git', '-C', REPO, 'status', '--porcelain'],
                       capture_output=True, text=True).stdout.strip()
ck('endless-sky b4aa3bac3 pulito (documento e realta\')',
   head == 'b4aa3bac3' and not dirty and 'b4aa3bac3' in doc, (head, dirty[:40]))
ck('strumenti citati esistono', all(os.path.exists(os.path.join(L10N, 'staging/editorial/tools', t))
                                    for t in ('state.py', 'export_section.py', 'next_section.py',
                                              'protected.sha256')))

for n, cond, d in ok:
    print('%-48s %s %s' % (n, 'OK' if cond else 'FAIL', '' if cond else d))
print()
bad = sum(1 for _, cond, _ in ok if not cond)
print('FAIL:', bad, '/', len(ok), '—', 'HANDOFF coerente col workspace' if bad == 0 else 'HANDOFF da rigenerare')
sys.exit(0 if bad == 0 else 1)
