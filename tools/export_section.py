"""export_section.py — esporta una sezione di unita' da `state.db` in source.json.

Uso:
    python staging/editorial/tools/export_section.py <dir> <path> <line_from> <line_to> [note]

- <path> e' il percorso del file DENTRO il repository, es. "data/human/human missions.txt"
- crea <dir>/ e <dir>/parts/, scrive <dir>/source.json (mai sovrascrive: se esiste, esce 2)
- stampa la ricognizione: tipi, tab, virgolette, backtick, token, righe con piu' unita'

Non scrive su `state.db` (aperto in sola lettura) e non tocca il repository originale.
"""
import collections
import hashlib
import json
import os
import re
import sqlite3
import sys

L10N = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
REPO = os.path.abspath(os.path.join(L10N, '..', 'endless-sky'))


def main():
    if len(sys.argv) < 5:
        print(__doc__)
        return 2
    d, path = sys.argv[1], sys.argv[2]
    lf, lt = int(sys.argv[3]), int(sys.argv[4])
    note = sys.argv[5] if len(sys.argv) > 5 else ''

    src_file = os.path.join(REPO, *path.split('/'))
    if not os.path.exists(src_file):
        print('ERRORE: file inesistente ->', src_file)
        return 2
    src = [l.rstrip('\n') for l in open(src_file, encoding='utf-8')]

    c = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
    rows = c.execute('select id, line, kind, context, english from units where path=? '
                     'and line between ? and ? order by line', (path, lf, lt)).fetchall()
    if not rows:
        print('ERRORE: nessuna unita\' fra le righe %d e %d di %s' % (lf, lt, path))
        return 2

    units = []
    for i, (uid, line, kind, ctx, eng) in enumerate(rows, 1):
        raw = src[line - 1]
        delim = 'backtick' if '`' in raw else ('quote' if '"' in raw else 'none')
        units.append({'idx': i, 'id': uid, 'path': path, 'line': line, 'kind': kind,
                      'context': ctx, 'english': eng, 'delimiter': delim,
                      'leading_tab': eng.startswith('\t'), 'raw': raw,
                      'english_hash': hashlib.sha256(eng.encode()).hexdigest()[:16]})

    doc = {'block': {'path': path, 'line_from': lf, 'line_to': lt, 'units': len(units)},
           'note': note, 'units': units}

    os.makedirs(os.path.join(d, 'parts'), exist_ok=True)
    out = os.path.join(d, 'source.json')
    if os.path.exists(out):
        print('ERRORE: %s esiste gia\': nessuna sovrascrittura.' % out)
        return 2
    open(out, 'w', encoding='utf-8').write(json.dumps(doc, ensure_ascii=False, indent=1))

    tok = collections.Counter()
    for u in units:
        tok.update(re.findall(r'<[^>]{1,30}>', u['english']))
    multi = collections.OrderedDict()
    for u in units:
        multi.setdefault(u['line'], []).append(u['idx'])
    print('DIR', d)
    print('path %s · righe %d-%d · %d unita · %d parole' % (
        path, lf, lt, len(units), sum(len(u['english'].split()) for u in units)))
    print('tipi', dict(collections.Counter(u['kind'] for u in units)))
    print('tab %d · virgolette %d · backtick %d' % (
        sum(1 for u in units if u['english'].startswith('\t')),
        sum(u['english'].count('"') for u in units),
        sum(u['english'].count('`') for u in units)))
    print('token', dict(tok))
    dup = [(k, v) for k, v in multi.items() if len(v) > 1]
    print('righe con piu\' unita:', dup or 'nessuna')
    print('primo', units[0]['context'], 'riga', units[0]['line'],
          '| ultimo', units[-1]['context'], 'riga', units[-1]['line'])
    return 0


if __name__ == '__main__':
    sys.exit(main())
