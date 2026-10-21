#!/usr/bin/env python3
"""apply_translations.py — applica le traduzioni in staging a una COPIA del gioco.

`tools/l10n.py` dichiara nel docstring «The game repository is only read. Integration
writes into ./output/», ma non contiene il comando che fa l'integrazione. Questo tool è
quel passo, separato e verificabile:

  * legge tutti i `staging/editorial/L*/translation.json` (dedup per `id`, conflitti = errore);
  * scrive **solo** nella copia indicata con `--dest` (mai nel repository originale);
  * sostituisce `english` con `italian` DENTRO la riga grezza, una sola volta;
  * le unità con `italian == english` (nomi propri, `VALUE`) sono saltate: nessuna sostituzione,
    nessun rischio (è il caso di `People` dentro `People's`);
  * se `english` non compare esattamente una volta nella riga, l'unità è un ERRORE, non un
    silenzio: si stampa e si esce 1 senza scrivere il file.

Uso:
    python apply_translations.py --l10n <repo l10n> --dest <copia del gioco> [--dry-run]

Esce 0 se tutte le unità sono applicate o saltate, 1 se c'è un errore.
"""
from __future__ import annotations

import argparse
import collections
import glob
import json
import os
import sys


def load_units(l10n: str) -> tuple[dict, list]:
    units: dict[str, dict] = {}
    conflicts = []
    # L* = lotti censiti in state.db · N* = estrazioni integrative (news/hail) non presenti
    # nel DB, create da review/extract_news_units.py per non toccare l'inventario protetto.
    lotti = sorted(glob.glob(os.path.join(l10n, 'staging', 'editorial', 'L*', 'translation.json')))
    lotti += sorted(glob.glob(os.path.join(l10n, 'staging', 'editorial', 'N*', 'translation.json')))
    for f in lotti:
        for x in json.load(open(f, encoding='utf-8'))['units']:
            old = units.get(x['id'])
            if old is not None:
                if old['italian'] != x['italian'] or old['line'] != x['line']:
                    conflicts.append((x['id'], os.path.basename(os.path.dirname(f))))
                continue
            units[x['id']] = {'id': x['id'], 'path': x['path'], 'line': x['line'],
                              'english': x['english'], 'italian': x['italian'],
                              'kind': x.get('kind', '')}
    return units, conflicts


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--l10n', required=True)
    ap.add_argument('--dest', required=True, help='copia del gioco da modificare (NON il repo)')
    ap.add_argument('--dry-run', action='store_true')
    a = ap.parse_args()

    units, conflicts = load_units(a.l10n)
    if conflicts:
        print('ERRORE: %d id con traduzioni diverse fra lotti:' % len(conflicts), conflicts[:5])
        return 1
    by_path = collections.defaultdict(list)
    for u in units.values():
        by_path[u['path']].append(u)

    applied = noop = 0
    errors = []
    per_file = []
    for path, us in sorted(by_path.items()):
        full = os.path.join(a.dest, *path.split('/'))
        if not os.path.exists(full):
            errors.append((path, 0, 'file assente'))
            continue
        with open(full, encoding='utf-8', newline='') as fh:
            lines = fh.read().splitlines(keepends=True)
        n_before = len(lines)
        n_applied = 0
        for u in sorted(us, key=lambda x: x['line']):
            i = u['line'] - 1
            if i >= len(lines):
                errors.append((path, u['line'], 'riga oltre il file'))
                continue
            raw = lines[i]
            if u['italian'] == u['english']:
                noop += 1
                continue
            n = raw.count(u['english'])
            if n != 1:
                errors.append((path, u['line'], 'english presente %d volte' % n))
                continue
            # il newline finale resta: `english` non lo contiene, `replace` tocca solo il testo
            lines[i] = raw.replace(u['english'], u['italian'], 1)
            applied += 1
            n_applied += 1
        if len(lines) != n_before:
            errors.append((path, 0, 'numero di righe cambiato'))
            continue
        if not a.dry_run and n_applied:
            with open(full, 'w', encoding='utf-8', newline='') as fh:
                fh.writelines(lines)
        per_file.append((n_applied, len(us), path))

    per_file.sort(reverse=True)
    print('unitá nel workspace : %d su %d file' % (len(units), len(by_path)))
    print('applicate           : %d' % applied)
    print('saltate (identiche) : %d' % noop)
    print('errori              : %d' % len(errors))
    for e in errors[:10]:
        print('  ERRORE', e)
    print()
    print('%6s %6s  %s' % ('appl.', 'unità', 'file'))
    for na, nu, p in per_file[:12]:
        print('%6d %6d  %s' % (na, nu, p))
    print('%6d %6d  (%d file totali)' % (applied, len(units), len(per_file)))
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())
