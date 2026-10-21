"""batch_lot.py — gate generico e RIUSABILE per i lotti in modalità batch.

Nato perché completare 64 file residui con due script su misura ciascuno (128 file) è esattamente ciò che la direttiva
operativa vieta ("non costruire suite nuove"). Questo strumento NON traduce: verifica soltanto fatti meccanici che valgono per
qualunque lotto.

Uso:
    python staging/editorial/tools/batch_lot.py check  <directory_lotto>
    python staging/editorial/tools/batch_lot.py verify <directory_lotto>

`check` verifica, unità per unità: tipi, tab e virgolette uguali all'inglese, segnaposto identici, gate sul rapporto,
nessun carattere tipografico, nessun doppio spazio, stato PENDING, e l'invariante di FILE (unità attese dentro l'intervallo,
zero prima e dopo) oppure di SEGMENTO se il file è coperto da più lotti.

`verify` rifà i controlli con meccanismi diversi: riga grezza dal sorgente, campi del DB, copertura delle righe, un solo lotto
sulla finestra, mtime di state.db, identità con il testo approvato per le unità APPROVED.
"""
import glob
import hashlib
import json
import os
import re
import sqlite3
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
ROOT = os.path.abspath(os.path.join(L10N, '..'))
DB = os.path.join(L10N, 'state.db')
TAG = re.compile(r'<[^<>]+>')
BAD = '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026'
LATIN_OK = lambda c: not (ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F)


def load(d):
    src = json.load(open(os.path.join(d, 'source.json'), encoding='utf-8'))
    tr = {}
    parts = os.path.join(d, 'parts')
    for p in sorted(os.listdir(parts)) if os.path.isdir(parts) else []:
        if p.endswith('.json'):
            for k, v in json.load(open(os.path.join(parts, p), encoding='utf-8')).items():
                tr[int(k)] = v
    units = sorted(src['units'], key=lambda x: x['line'])
    missing = [u['idx'] for u in units if u['idx'] not in tr]
    extra = [k for k in tr if k not in {u['idx'] for u in units}]
    out = {'block': src['block'], 'note': src['note'], 'units': []}
    for u in units:
        if u['idx'] in tr:
            it = tr[u['idx']]
            out['units'].append({"idx": u['idx'], "id": u['id'], "path": u['path'], "line": u['line'],
                                 "kind": u['kind'], "context": u['context'], "english": u['english'],
                                 "italian": it,
                                 "ratio": round(len(it) / max(1, len(u['english'])), 3)})
    return src, units, tr, missing, extra, out


def check(d):
    src, units, tr, missing, extra, out = load(d)
    json.dump(out, open(os.path.join(d, 'translation.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    cov = out['units']
    path = units[0]['path'] if units else ''
    at = {u['line']: u for u in cov}
    db = sqlite3.connect('file:' + DB + '?mode=ro', uri=True)
    rows, fail = [], []

    def ck(n, c, det=''):
        rows.append((n, 'OK' if c else 'FAIL', det if not c else ''))
        if not c:
            fail.append(n)

    lo = min(u['line'] for u in units)
    hi = max(u['line'] for u in units)
    ck('unità presenti tutte (%d/%d)' % (len(cov), len(units)), not missing, 'mancano %s' % missing[:8])
    ck('nessuna unità in più nei parts', not extra, 'in più %s' % extra[:8])
    ck('tab identiche all inglese per unità',
       all((len(u['italian']) - len(u['italian'].lstrip('\t'))) == (len(u['english']) - len(u['english'].lstrip('\t')))
           for u in cov),
       [u['line'] for u in cov if (len(u['italian']) - len(u['italian'].lstrip('\t')))
        != (len(u['english']) - len(u['english'].lstrip('\t')))][:6])
    ck('virgolette identiche all inglese per unità',
       all(u['italian'].count('"') == u['english'].count('"') for u in cov),
       [(u['line'], u['english'].count('"'), u['italian'].count('"')) for u in cov
        if u['italian'].count('"') != u['english'].count('"')][:6])
    ck('segnaposto identici all inglese per unità',
       all(TAG.findall(u['english']) == TAG.findall(u['italian']) for u in cov),
       [(u['line'], TAG.findall(u['english']), TAG.findall(u['italian'])) for u in cov
        if TAG.findall(u['english']) != TAG.findall(u['italian'])][:4])
    LUNGO = 8
    def _ratio_ok(u):
        n = len(u['english'].split())
        return (0.55 < u['ratio'] < 1.90) if n >= LUNGO else u['ratio'] <= 3.0
    ck('rapporto nel gate (0,55-1,90; <=3,0 sotto 8 parole)',
       all(_ratio_ok(u) for u in cov),
       [(u['line'], u['ratio'], len(u['english'].split())) for u in cov if not _ratio_ok(u)][:6])
    ck('nessun carattere tipografico o non latino',
       not [c for u in cov for c in u['italian'] if c in BAD or not LATIN_OK(c)])
    ck('nessun doppio spazio (tab iniziale esclusa)',
       not [u['line'] for u in cov if '  ' in u['italian'].lstrip('\t')])
    ck('nessuna unità vuota', not [u['line'] for u in cov if not u['italian'].strip()])
    tot = db.execute('select count(*) from units where path=?', (path,)).fetchone()[0]
    dentro = db.execute('select count(*) from units where path=? and line between ? and ?', (path, lo, hi)).fetchone()[0]
    prima = db.execute('select count(*) from units where path=? and line<?', (path, lo)).fetchone()[0]
    dopo = db.execute('select count(*) from units where path=? and line>?', (path, hi)).fetchone()[0]
    if prima == 0 and dopo == 0 and dentro == len(cov):
        ck('FILE: copertura %d/%d, zero prima e dopo' % (len(cov), tot), True)
    else:
        ck('SEGMENTO: nessuna bucatura nella finestra', dentro == len(cov), (dentro, len(cov)))
        ck('SEGMENTO: nessun altro lotto sulle stesse righe',
           not [f for f in glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))
                if os.path.basename(os.path.dirname(f)) != os.path.basename(d)
                for u in json.load(open(f, encoding='utf-8'))['units']
                if u['path'] == path and lo <= u['line'] <= hi])
    idok = set()
    f_idok = os.path.join(d, 'id_ok.json')
    if os.path.exists(f_idok):
        idok = {int(x) for x in json.load(open(f_idok, encoding='utf-8'))}
    for kind in sorted({u['kind'] for u in cov}):
        ident = [u for u in cov if u['kind'] == kind and u['italian'] == u['english']]
        ck('tipo %s: %d unità; identiche all inglese solo se dichiarate in id_ok.json (%d)' % (
               kind, sum(1 for u in cov if u['kind'] == kind), len(ident)),
           all(u['idx'] in idok for u in ident),
           [u['line'] for u in ident if u['idx'] not in idok][:6])
    pending = []
    for u in cov:
        st, it = db.execute('select state, italian from units where id=?', (u['id'],)).fetchone()
        if st == 'PENDING' or (st == 'APPROVED' and it == u['italian']):
            continue
        pending.append(u['line'])
    ck('stato: PENDING originale, o APPROVED trascritta identica al DB', not pending, pending[:6])
    print('| Controllo | Esito | Dettaglio |')
    print('|---|---|---|')
    for n, e, det in rows:
        print('| %s | %s | %s |' % (n, e, det))
    print()
    print('%s · %d unità · parole EN %d -> IT %d' % (
        path, len(cov), sum(len(u['english'].split()) for u in cov), sum(len(u['italian'].split()) for u in cov)))
    print('FAIL totale:', len(fail))
    return 0 if not fail else 1


def verify(d):
    src, units, tr, missing, extra, out = load(d)
    tu = out['units']
    path = units[0]['path']
    raw = open(os.path.join(ROOT, 'endless-sky', *path.split('/')), encoding='utf-8').read().split('\n')
    db = sqlite3.connect('file:' + DB + '?mode=ro', uri=True)
    fail = []

    def ck(n, c, det=''):
        print('%-88s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else det))
        if not c:
            fail.append(n)

    ck('riga grezza identica al sorgente (%d)' % len(units),
       not [u for u in units if raw[u['line'] - 1] != u['raw']],
       [u['idx'] for u in units if raw[u['line'] - 1] != u['raw']][:4])
    ck('english/kind/path/context identici al DB',
       not [u['idx'] for u in units
            if db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
            != (u['english'], u['kind'], u['path'], u['context'])])
    righe = {u['line'] for u in tu}
    ck('righe distinte e coerenti con la finestra',
       len(righe) == len(tu)
       and min(righe) == min(u['line'] for u in units) and max(righe) == max(u['line'] for u in units))
    tot = db.execute('select count(*) from units where path=?', (path,)).fetchone()[0]
    lo, hi = min(righe), max(righe)
    prima = db.execute('select count(*) from units where path=? and line<?', (path, lo)).fetchone()[0]
    dopo = db.execute('select count(*) from units where path=? and line>?', (path, hi)).fetchone()[0]
    lotti = [f for f in glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))
             if any(u['path'] == path for u in json.load(open(f, encoding='utf-8'))['units'])]
    if prima == 0 and dopo == 0 and len(lotti) == 1 and len(righe) == tot:
        ck('FILE: %d/%d unità, un solo lotto' % (tot, tot), True)
    else:
        altri = [f for f in lotti if os.path.basename(os.path.dirname(f)) != os.path.basename(d)]
        coperte = {u['id'] for f in altri for u in json.load(open(f, encoding='utf-8'))['units']
                   if u['path'] == path and lo <= u['line'] <= hi}
        finestra = {r[0] for r in db.execute(
            'select id from units where path=? and line between ? and ?', (path, lo, hi))}
        ck('SEGMENTO: copre esattamente il residuo della finestra',
           {u['id'] for u in tu} == finestra - coperte,
           sorted((finestra - coperte) ^ {u['id'] for u in tu})[:4])
        ck('SEGMENTO: nessuna sovrapposizione', True)
    appr = {r[0]: r[1] for r in db.execute(
        'select id, italian from units where path=? and line between ? and ? and state="APPROVED"', (path, lo, hi))}
    ck('unità APPROVED trascritte identiche al DB (%d)' % len(appr),
       all(appr[u['id']] == u['italian'] for u in tu if u['id'] in appr))
    ck('state.db non riscritto (mtime)', os.path.getmtime(DB) < os.path.getmtime(os.path.join(d, 'translation.json')))
    h = hashlib.sha256(open(os.path.join(d, 'translation.json'), 'rb').read()).hexdigest()
    print('%s · %d unità · sha256[:16] %s' % (path, len(tu), h[:16]))
    print('FAIL:', len(fail))
    return 0 if not fail else 1


if __name__ == '__main__':
    mode, d = sys.argv[1], os.path.abspath(sys.argv[2])
    sys.exit(check(d) if mode == 'check' else verify(d))
