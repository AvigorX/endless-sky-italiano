#!/usr/bin/env python3
"""verify_integration.py — verifica indipendente della copia tradotta contro `git HEAD`.

Non si fida dell'applicazione: rilegge i file modificati e li confronta con il contenuto
del repository originale preso da `git show HEAD:<path>`. Per ogni file toccato:

  * stesso numero di righe;
  * ogni riga diversa deve corrispondere a un'unita' tradotta di quel file, e differire
    dall'originale SOLO per la sostituzione `english` -> `italian`;
  * nessuna riga non prevista puo' cambiare.

Esce 0 se tutto torna, 1 altrimenti.
"""
from __future__ import annotations

import collections
import glob
import json
import os
import subprocess
import sys

L10N = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
REPO = os.path.abspath(os.path.join(L10N, '..', 'endless-sky'))
# Directory dei dati tradotti da verificare. Default = la prima build; si puo'
# puntare altrove con `--dest <percorso>` per verificare una build isolata.
DEST = os.path.abspath(os.path.join(L10N, '..', 'endless-sky-it', 'src'))
if '--dest' in sys.argv:
    DEST = os.path.abspath(sys.argv[sys.argv.index('--dest') + 1])

units = {}
lotti = sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json')))
lotti += sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'N*', 'translation.json')))
for f in lotti:
    for x in json.load(open(f, encoding='utf-8'))['units']:
        units[x['id']] = x

by_path = collections.defaultdict(lambda: collections.defaultdict(list))
for u in units.values():
    # una riga puo' contenere PIU' unita' (caso misurato: human missions.txt riga 555)
    by_path[u['path']][u['line']].append(u)

fail = []
tot_changed = tot_expected = 0
for path, per_line in sorted(by_path.items()):
    orig = subprocess.run(['git', '-C', REPO, 'show', 'HEAD:' + path.replace('\\', '/')],
                          capture_output=True, check=True).stdout.decode('utf-8')
    # `git show` restituisce LF, la copia estratta e' CRLF come un checkout Windows (core.autocrlf=true):
    # il confronto e' sul contenuto, e i fine riga si normalizzano da entrambi i lati.
    new = open(os.path.join(DEST, *path.split('/')), encoding='utf-8', newline=None).read()
    if orig.count('\n') != new.count('\n'):
        fail.append((path, 'numero di righe %d -> %d' % (orig.count('\n'), new.count('\n'))))
        continue
    o, n = orig.split('\n'), new.split('\n')
    expected = sum(1 for us in per_line.values() if any(u['italian'] != u['english'] for u in us))
    changed = 0
    for i, (a, b) in enumerate(zip(o, n)):
        if a == b:
            continue
        changed += 1
        us = per_line.get(i + 1)
        if us is None:
            fail.append((path, 'riga %d cambiata ma non e\' nel lotto' % (i + 1)))
            continue
        # si applicano TUTTE le sostituzioni della riga, in ordine
        s = a
        for u in us:
            if u['italian'] != u['english']:
                s = s.replace(u['english'], u['italian'], 1)
        if s != b:
            fail.append((path, 'riga %d non e\' una sostituzione esatta' % (i + 1)))
    if changed != expected:
        fail.append((path, 'righe cambiate %d invece di %d' % (changed, expected)))
    tot_changed += changed
    tot_expected += expected

print('file confrontati      : %d' % len(by_path))
print('righe cambiate        : %d (attese %d)' % (tot_changed, tot_expected))
print('unita\' nel workspace  : %d · tradotte %d · identiche %d' % (
    len(units), sum(1 for u in units.values() if u['italian'] != u['english']),
    sum(1 for u in units.values() if u['italian'] == u['english'])))
multi = sum(1 for p in by_path.values() for us in p.values() if len(us) > 1)
print("righe con piu' unita' : %d (spiegano la differenza righe/unita')" % multi)
print('FAIL                  : %d' % len(fail))
for f in fail[:10]:
    print('  ', f)
print()
print('ESITO:', 'OK' if not fail else 'FALLITO')
sys.exit(0 if not fail else 1)
