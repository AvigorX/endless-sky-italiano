# STATO — L180 · `human outfits.txt` (raffreddamento e generatori di scudi)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L180_20261019_190943` |
| Righe / unità | **15–146** / **12** — file al **12/63 (19,0%)** |
| Tipi | **11 `DESCRIPTION`** · **1 `VALUE`** |
| `UI_LABEL` · token · tab · virgolette | **0** · **0** · **0** · **0** — quattro asserzioni vuote scritte |
| Contesti | **11** (dieci con 1 unità, `Cooling Ducts` con 2) · **12 testi distinti** |
| Parole | **467 EN → 478 IT** (1,024) · rapporto **1,01–1,27**, media **1,10** |
| Apici | **1** in inglese (idx 3, `ship's`) · nessun possessivo in italiano |
| sha256 | `263300dbfc862221…` |
| Esiti | `check.py` **24** (`FAIL 0`) · `verify.py` **20**, exit **0** |

## Cosa contiene

| blocco | unità | righe | contenuto |
|---|---|---|---|
| raffreddamento | 1-5 | 15-57 | `Cooling Ducts`, acqua, azoto liquido, elio liquido («il massimo») |
| generatori di scudi | 6-10 | 70-132 | `D14-RN` → `D94-YV`, dal caccia al `D94-YV` «il più potente dello spazio umano» |
| rigeneratori | 11-12 | 132-146 | `S-270` (meno efficienti, più calore) e `S-970` (fabbisogno energetico alto) |

## Le due scale del lotto

**Potenza**: standard → «leggermente più potente» → «combattimenti frequenti» → «così potente che» → «il più potente
disponibile nello spazio umano».

**Costo**: i due rigeneratori dicono cose diverse — l'`S-270` rende gli scudi **meno efficienti** e sottrae energia anche a
scudi fermi; l'`S-970` ha **fabbisogno energetico alto** e produce calore per **ritorno**. Verificati separatamente.

## Verifica

```bash
cd staging/editorial/L180_20261019_190943
python check.py     # FAIL totale: 0 (24 controlli)
python verify.py    # exit 0 (20 controlli)
```

**Non verificato**: nessun equipaggiamento visto a schermo; i testi non sono stati caricati nel gioco.
