# STATO — L261 (`data/remnant/remnant jobs.txt`, righe 19–209)

**Stato: CHIUSO.** Primo lotto del file dei lavori Remnant: **25 unità** — **7 `VALUE`** (copiati), **7 `DESCRIPTION`** e
**11 `DIALOG`** (tradotti) — su **7 contesti**. Il file è aperto a **25/87 (28,7%)**.

| voce | valore |
|---|---|
| directory | `staging/editorial/L261_20261020_161448/` |
| file | `data/remnant/remnant jobs.txt` (87 unità · 1.462 parole · righe 19–741) |
| righe | 19–209 |
| unità | **25** — 11 `DIALOG` + 7 `DESCRIPTION` + 7 `VALUE` |
| parole | **404 EN → 419 IT** |
| rapporto | **0,90 – 1,26** |
| contesti | **7** — `Bounty`, `Bounty 2`, `Broken Jump Drive job`, `Expanded Horizons Astral job`, `… late`, `Bounty 3`, `Bounty 4` |
| tab / virgolette | **0 / 0** in entrambe le lingue (asserzioni negative) |
| apici | **2 EN** (`Rano'erek`, unità 20 e 24) / **4 IT** (15, 19, 20, 24) |
| segnaposto | **29** in **6** famiglie — `<payment>` 10, `<planet>` 8, `<waypoints>` 4, `<npc>` 3, **`<npc model>` 2**, `<destination>` 2 |
| `check.py` | **23 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **20 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di segmento**: 0 prima (il lotto **apre** il file) · 25 qui · **62 dopo** la 209 |
| `sha256[:16]` | **`14b2dd524975c4fe`** |

## Comandi

```bash
python staging/editorial/L261_20261020_161448/check.py     # FAIL totale: 0 (23 controlli)
python staging/editorial/L261_20261020_161448/verify.py    # FAIL: 0 (20 controlli, 25/87)
```

## Le tre decisioni del lotto

1. **I `VALUE` si copiano.** `Crippled <npc model> Bounty`, `Broken Jump Drive Delivery`,
   `Research Expedition to <waypoints>` restano inglesi: sono i **nomi dei lavori**, non prosa. L'asserzione è l'**identità
   per indice**, non «prosa tradotta» — e vale anche per `Damaged Rano'erek Bounty`, che conserva il nome proprio.
2. **`<npc model>` e `<npc>` sono simboli distinti** (2 e 3): il primo è il **modello** della nave, il secondo la **nave**
   specifica. Il `verify.py` verifica le due famiglie separate, non un totale di 5.
3. **`Hunt it down`** → **«Dalle la caccia»**: la nave è femminile, e il corpus usa già `dare la caccia a <npc>`;
   l'accordo del clitico è stato scelto invece del più comodo «Dagli».

## Gruppi di stringhe identiche (una sola resa)

| gruppo | unità | inglese | resa |
|---|---|---|---|
| 3 | 3, 7, 22 | `You have destroyed the Korath ship. …` | «Hai distrutto la nave Korath. Ora puoi tornare su `<planet>` per riscuotere il pagamento.» |
| 2 | 8, 23 | `…the Korath ship <npc>, …` | «…per aver dato la caccia alla nave Korath `<npc>`…» |
| 2 | 12, 16 | `Research Expedition to <waypoints>` | copiato |
| 2 | 13, 17 | `Travel to <waypoints> …` | «Raggiungi `<waypoints>` con un Laboratorio di Ricerca…» |
| 2 | 14, 18 | `Your scientist unpacks…` | «Il tuo scienziato scarica il laboratorio…» |
| 2 | 15, 19 | `When you land…` | «Quando atterri, un ricercatore recupera…» |

## Lessico fissato

`Laboratorio di Ricerca` (nome dell'equipaggiamento, forma del corpus) · `cristalli di dati` · `motore di salto` ·
`indennità logistica` · `pagamento concordato` · `comandante militare dei Remnant` · `Ember Waste` → **(fuori da questo
lotto, riga 239: sarà L262)** · `Remnant` e `Korath` invariati.

## Limiti dichiarati

Nessuna approvazione (25 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. Restano **62 unità**.
