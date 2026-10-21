"""state.py — fotografia misurata del progetto e controllo di integrita'.

Uso:
    python staging/editorial/tools/state.py            # stato + integrita'
    python staging/editorial/tools/state.py --bless    # riscrive protected.sha256 (solo dopo una
                                                       # modifica voluta e documentata)

Esce 0 se tutti gli hash protetti coincidono, 1 se qualcosa e' cambiato, 2 su errore d'uso.
Sola lettura su `state.db`.
"""
import glob
import hashlib
import json
import os
import sqlite3
import subprocess
import sys

L10N = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
REPO = os.path.abspath(os.path.join(L10N, '..', 'endless-sky'))
MANIFEST = os.path.join(os.path.dirname(__file__), 'protected.sha256')

PROTECTED = [
    'state.db',
    'glossary.csv',
    'staging/inventory_fields.csv',
    'tools/l10n.py',
    'output/l10n-it/data/_ui/interfaces.txt',
    'output/l10n-it/data/_ui/tooltips.txt',
    'output/l10n-it/data/_ui/help.txt',
]


def sha(path):
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def main():
    if '--bless' in sys.argv:
        with open(MANIFEST, 'w', encoding='utf-8') as f:
            for p in PROTECTED:
                f.write('%s  %s\n' % (sha(os.path.join(L10N, p)), p))
        print('manifest scritto:', MANIFEST)
        return 0

    c = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
    q = lambda s, *a: c.execute(s, a).fetchone()
    st = dict(c.execute('select state, count(*) from units group by state').fetchall())
    print('== DATABASE (autorevole, sola lettura) ==')
    print('  APPROVED %s · PENDING %s · totale %s' % (
        st.get('APPROVED'), st.get('PENDING'), sum(st.values())))
    print('  ultimo evento APPROVED: %s' % q("select max(updated_at) from units where state='APPROVED'")[0])
    lab = q("select count(*) from units where state='PENDING' and kind='UI_LABEL'")[0]
    print('  PENDING con kind UI_LABEL (label, non traducibili): %s' % lab)

    print()
    print('== STAGING EDITORIALE (tradotto, NON nel database) ==')
    tot = [0, 0, 0]
    per_file = {}
    for f in sorted(glob.glob(os.path.join(L10N, 'staging/editorial/L*/translation.json'))):
        d = json.load(open(f))['units']
        if not d:
            continue
        e = sum(len(x['english'].split()) for x in d)
        i = sum(len(x['italian'].split()) for x in d)
        tot[0] += len(d); tot[1] += e; tot[2] += i
        pf = per_file.setdefault(d[0]['path'], [0, 0, 0, 0])
        pf[0] += len(d); pf[1] += e; pf[2] += i; pf[3] += 1
    for path, (n, e, i, lots) in sorted(per_file.items()):
        total = q('select count(*) from units where path=?', path)[0]
        print('  %-42s %5d/%5d unita (%5.1f%%) · %6d EN -> %6d IT · %d lotti'
              % (path, n, total, 100.0 * n / total, e, i, lots))
    print('  TOTALE staging: %d unita · %d EN · %d IT' % tuple(tot))
    print('  residuo traducibile: %d unita (PENDING %d - staging %d - label %d)' % (
        st['PENDING'] - tot[0] - lab, st['PENDING'], tot[0], lab))

    print()
    print('== INTEGRITA\' ==')
    bad = 0
    if os.path.exists(MANIFEST):
        for line in open(MANIFEST, encoding='utf-8'):
            want, p = line.split('  ', 1)
            p = p.strip()
            got = sha(os.path.join(L10N, p))
            okk = got.startswith(want[:16]) or got == want
            print('  %-44s %s' % (p, 'OK' if okk else 'CAMBIATO (%s -> %s)' % (want[:16], got[:16])))
            bad += 0 if okk else 1
    else:
        print('  manifest assente: esegui --bless una volta')
    head = subprocess.run(['git', '-C', REPO, 'rev-parse', '--short', 'HEAD'],
                          capture_output=True, text=True).stdout.strip()
    dirty = subprocess.run(['git', '-C', REPO, 'status', '--porcelain'],
                           capture_output=True, text=True).stdout.strip()
    print('  %-44s %s (modifiche: %s)' % ('endless-sky HEAD', head, 'nessuna' if not dirty else dirty[:40]))
    if head != 'b4aa3bac3' or dirty:
        bad += 1
    print()
    print('ESITO:', 'OK' if bad == 0 else 'FAIL (%d controlli)' % bad)
    return 0 if bad == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
