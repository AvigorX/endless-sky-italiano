# HANDOFF — fase post-traduzione (revisione) · 2026-10-21

Contratto di ripresa. Da leggere all'inizio della prossima sessione, prima di toccare qualsiasi cosa.

## Stato in una riga

Revisione eseguita e misurata: **491 correzioni** su 78 lotti, **0 errori reali di accento**, integrità
`parts`↔`translation.json` riparata, integrazione verificata in dry-run (exit 0). **Build non eseguita**,
**UI non tradotta**, **`state.db` non scritto** (sha e mtime invariati).

## Numeri di riferimento (da rimisurare, non da fidarsi)

```
staging        32 924 unità · 167 file · 403 lotti · 0 senza resa
parole         979 975 EN → 937 108 IT
DB             32 560 PENDING + 364 APPROVED = 32 924
protetti       7/7 integri
repo gioco     b4aa3bac3 · 0 righe di diff
gate           395 verdi · 6 falliti per difetto del controllo · 1 saltato (archivio)
apply_transl.  --dry-run → 30 882 applicate · 2 042 identiche · 0 errori · exit 0
```

## Comandi che ricostruiscono la baseline (in quest'ordine)

```bash
cd ~/PROGETTI/G-DEV/GAME-SOURCE-LAB/endless-sky-l10n

python review/check_protected.py                 # deve dare 7/7, exit 0
python review/build_corpus.py                     # 32 924 unità, 0 senza resa
python review/gate.py --consistency               # translation.json ≡ parts, 0 incoerenti
python review/apply_fixes.py --dry-run --file review/fixes_R04.jsonl   # atteso: tutte "già applicate"
```

`review/gate.py <lotto…>` riesegue `check`+`verify` sui lotti indicati; **salta** i lotti senza `parts/`
(archivio storico) per non azzerarne il `translation.json`.

## Cosa è cambiato in questa fase

| batch | contenuto | unità |
|---|---|---:|
| R01 | nomi di missione in inglese | 24 |
| R02 | nomi di incarico in inglese (157 stringhe) | 412 |
| R03 | `disable` → `neutralizzare` | 34 |
| R04 | `job board` → `bacheca degli incarichi` | 35 |
| integrità | allineamento `parts` → `translation.json` | 4 356 |
| dichiarazioni | `id_ok.json` per unità identiche per necessità | 1 388 |

Ogni modifica è reversibile: `review/applied.jsonl` (old/new per unità), `review/integrity_repair.jsonl`
(idem per la riparazione), backup dei `parts` in `review/backups/<timestamp>/`.

## Blocchi aperti (in ordine di urgenza)

1. **Lacuna dell'estrattore** — 2 065 righe / 29 128 parole di testo (news e hail di 6 file) non sono
   nell'inventario. Causa e diff pronto in `review/PROPOSTA_ESTRATTORE.md`. **Serve un'autorizzazione
   esplicita**: la modifica impone di rigenerare l'inventario e quindi `state.db` (protetto). Finché non è
   autorizzata, la copertura va dichiarata come «per ID, non sul testo».
2. **DB non allineato** — le 32 560 unità `PENDING` non sono nel DB: `tools/package.py` confezionerebbe
   364 unità. Prima della build serve una fase autorizzata che scriva le traduzioni in `state.db`
   (meccanismo esistente: `tools/l10n.py import`, oppure una scrittura dichiarata e verificata).
3. **Compilazione** — `BUILD_RECON.md` §6: registry `vcpkg` disallineata dal commit della CI; MSVC fallisce
   per difetti upstream. Il patch font non è mai stato compilato. Nessun tentativo fatto.

## Difetti del gate noti e **non** corretti (decisi, non dimenticati)

| controllo | problema | effetto |
|---|---|---|
| `segnaposto identici` | confronta **liste**, non multinsiemi | 4 lotti falliscono per riordino legittimo |
| `segnaposto identici` | pretende i pronomi `<they>`, `<their>`… | 1 lotto fallisce: in italiano sono impliciti |
| `verify: righe distinte` | presume una unità per riga | 1 lotto fallisce: una riga ha 3 unità |

Correggerli significa toccare `batch_lot.py`, condiviso da 402 lotti: proposta rimandata, da fare con la
stessa procedura usata in passato (difetto misurato → correzione → probe di falsificabilità → riesecuzione).
Non “aggiustare” le traduzioni per farli passare.

## Log e artefatti superati (non leggere come stato attuale)

| file | perché è superato |
|---|---|
| `review/gate_riparati.log` | `66 lotti · falliti: 45`: corsa avviata **prima** delle dichiarazioni `id_ok.json`, completata a fine sessione. La stessa lista, rieseguita nello stato finale, dà **65 verdi / 1 fallito** (`L42`, riordino segnaposto) |
| `review/gate_full.log` | concatenazione dei 4 chunk: valida, ma la sintesi sta in `REPORT_REVISIONE_20261021.md` §6 |
| `review/backups/<ts>/` | copie pre-modifica dei `parts`: servono solo per la reversione |

## Registro degli errori commessi in questa fase (da non ripetere)

| errore | conseguenza | stato |
|---|---|---|
| esecuzione del `check` sul lotto archivio `L19_20261017_201342` (senza `parts/`) | il suo `translation.json` (1 636 unità, formato vecchio, ID non mappabili) è azzerato | documentato; impatto sul pipeline nullo; **non** ricostruito per non fabbricare dati; `gate.py` ora lo salta |
| `.strip()` nel primo `build_corpus.py` | cancellava i tab di paragrafo: 19 475 finte “divergenze” | corretto prima di ogni scrittura; nessun danno |
| gate globale in serie | timeout a 180 s | eseguito in 4 processi paralleli; una falsa failure transitoria (`L62`), poi verde |

## Prossimo passo raccomandato

Fase **UI** solo dopo una build di verifica riuscita, come da mandato. Prima: decidere sui blocchi 1 e 2.
Se il mandato successivo è «build», il primo atto è una fase autorizzata di scrittura in `state.db` — senza
la quale il pacchetto contiene 364 unità su 32 924.
