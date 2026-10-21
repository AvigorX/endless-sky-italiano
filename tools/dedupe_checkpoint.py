"""Deduplica i checkpoint: rimuove paragrafi e righe di tabella identici e CONSECUTIVI.

Nasce da un difetto del generatore: quando il testo nuovo **contiene** quello vecchio (`a` -> `a + b`), la
guardia di idempotenza non scattava e la patch, rieseguita, ha triplicato i blocchi. Qui si ripulisce in modo
deterministico e si conserva la prima occorrenza.
"""
import io
import re
import sys


def dedupe(text):
    paras = text.split('\n\n')
    out, removed = [], 0
    for p in paras:
        if out and p.strip() and p == out[-1]:
            removed += 1
            continue
        out.append(p)
    text = '\n\n'.join(out)
    lines = text.split('\n')
    keep, removed_rows = [], 0
    for l in lines:
        if keep and l.startswith('|') and l == keep[-1]:
            removed_rows += 1
            continue
        keep.append(l)
    return '\n'.join(keep), removed, removed_rows


for path in sys.argv[1:]:
    s = io.open(path, encoding='utf-8', newline='').read()
    crlf = s.count('\r\n')
    t = s.replace('\r\n', '\n')
    t2, np_, nr = dedupe(t)
    assert t2.count('\n\n\n') == 0, path
    io.open(path, 'w', encoding='utf-8', newline='').write(t2.replace('\n', '\r\n'))
    print('%-42s paragrafi rimossi %d · righe tabella rimosse %d · CRLF %d -> %d'
          % (path, np_, nr, crlf, t2.count('\n')))
