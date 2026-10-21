"""next_section.py — propone il confine del prossimo lotto, a fine contesto.

Uso:
    python staging/editorial/tools/next_section.py "<path>" <riga_inizio> [parole_min] [parole_max]

Il confine cade sempre fra due contesti (pianeta o missione), mai dentro un testo: accumula parole
unita' per unita' e si ferma al primo cambio di contesto che porta il totale in [parole_min, parole_max].
Stampa anche i tipi presenti, i token e le righe che producono piu' unita' (indizio di `log` o `phrase`).

Sola lettura su `state.db`.
"""
import collections
import os
import re
import sqlite3
import sys

L10N = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    path, start = sys.argv[1], int(sys.argv[2])
    lo = int(sys.argv[3]) if len(sys.argv) > 3 else 4200
    hi = int(sys.argv[4]) if len(sys.argv) > 4 else 5000

    c = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
    rows = c.execute('select line, context, kind, english from units where path=? and line>=? '
                     'order by line', (path, start)).fetchall()
    if not rows:
        print('ERRORE: nessuna unita\' dopo la riga %d in %s' % (start, path))
        return 2

    order, agg = [], collections.OrderedDict()
    for line, ctx, kind, eng in rows:
        if ctx not in agg:
            agg[ctx] = [0, 0, [], collections.Counter()]
            order.append(ctx)
        agg[ctx][0] += len(eng.split())
        agg[ctx][1] += 1
        agg[ctx][2].append(line)
        agg[ctx][3][kind] += 1

    first_line = agg[order[0]][2][0]
    words = units = 0
    for i, ctx in enumerate(order):
        w, n, lines, kinds = agg[ctx]
        words += w
        units += n
        if words >= lo and i:
            upto = lines[-1]
            toks = collections.Counter()
            seen = collections.Counter()
            kinds_all = collections.Counter()
            for line, cc, kk, eng in rows:
                if line <= upto:
                    toks.update(re.findall(r'<[^>]{1,30}>', eng))
                    seen[line] += 1
                    kinds_all[kk] += 1
            print('LOTTO PROPOSTO')
            print('  path      %s' % path)
            print('  righe     %d - %d' % (first_line, upto))
            print('  unita\'    %d' % units)
            print('  parole    %d' % words)
            print('  contesti  %d (da %s a %s)' % (i + 1, order[0], ctx))
            print('  tipi      %s' % dict(kinds_all))
            print('  token     %s' % dict(toks))
            print('  righe con piu\' unita: %s' % [l for l, n2 in seen.items() if n2 > 1])
            nxt = [l for l, cc, kk, eng in rows if l > lines[-1]]
            nxt_ctx = [cc for l, cc, kk, eng in rows if l > lines[-1]]
            if nxt:
                print('  dopo: riga %d apre %s' % (nxt[0], nxt_ctx[0]))
            else:
                print('  dopo: file esaurito (questo e\' l\'ultimo lotto del file)')
            if words > hi:
                print('  ATTENZIONE: sopra la soglia di %d parole, valuta di chiudere un contesto prima' % hi)
            return 0
    print('ERRORE: il file finisce prima di raggiungere %d parole (residuo %d)' % (lo, words))
    return 1


if __name__ == '__main__':
    sys.exit(main())
