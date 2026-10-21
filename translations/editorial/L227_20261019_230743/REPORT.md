# REPORT — L227 · `remnant outfits.txt` (quinto e ultimo lotto) — **file chiuso 57/57**

## 1. Contenuto

Dieci unità che chiudono il file. I due sistemi di sterzata pesanti — **Forge-Class** (avido di energia, spia di una
tecnologia dei motori più avanzata di quella umana) e **Smelter-Class** (di origine incerta, propria o aliena). Il **Tuning
Rifle** e il **Void Rifle**, l'arma che paralizza il sistema nervoso e attraversa i muri. Le **Void Sprite Parts**: un metro
cubo di parti, «un evento terribile e un'occasione spaventosa», con il secondo paragrafo che spiega perché ora valgono poco.
La **Remnant License**, che oltre a identificare il portatore suona musica classica, e la **Remnant Capital License**, che
con un ronzio chiama le pattuglie.

## 2. Difficoltà

1. **Lotto terminale: invariante di file, non confine.** `12 + 13 + 11 + 11 + 10 = 57`, senza `UI_LABEL` da scorporare — a
   differenza di `deep jobs.txt`, dove la riga 683 restava fuori. Il `verify.py` verifica che le cinque finestre coprano
   **esattamente** le righe del database.
2. **Torna un'unità da copiare, dopo tre lotti a zero.** Il `VALUE` della riga 948 riporta il confronto a **1 / 9**. Non è
   un'incoerenza: il file ha 55 `DESCRIPTION` + 2 `VALUE`, e i due nomi cadono in due finestre diverse. Il controllo
   asserisce **entrambe** le direzioni — che l'unica identica sia il `VALUE` e che tutte le nove `DESCRIPTION` siano
   tradotte — perché un «1» senza specificazione potrebbe nascondere una descrizione lasciata in inglese.
3. **Zero virgolette per il secondo lotto consecutivo.** Il numero si misura: dopo lotti con decine di virgolette, due zeri
   di fila sono un fatto da asserire, non da presumere.
4. **L'ultima unità è una licenza.** `Remnant Capital License` non descrive un'arma: descrive un dispositivo di soccorso.
   Il registro è più narrativo, e la resa lo segue («Sebbene all'apparenza innocuo, questo dispositivo mostra la brillante
   semplicità dell'ingegneria dei Remnant»).
5. **`Archon`** resta invariato: è un'autorità, non una carica traducibile.
6. **`a terrible occurrence and a dreadful opportunity`** → «un evento terribile e un'occasione spaventosa»: due aggettivi
   inglesi distinti, due italiani distinti.
7. **L'italiano è più corto** (376 contro 382 parole, media 0,99): è il secondo lotto della campagna in cui il totale scende,
   e qui dipende dalla concisione delle formule («un metro cubo di parti» per *a cubic meter of void sprite parts*).

## 3. Numeri osservati

```
unita' 10 · {'DESCRIPTION': 9, 'VALUE': 1} · tutte PENDING
2 tab (unita' 5, 8) · ZERO virgolette in EN e IT · 3 apici EN / 7 IT · 0 segnaposto
7 contesti · righe 884/979 · 47 prima (L223-L226) · 0 dopo (fine file)
1 unita' identica all'inglese (il VALUE), 9 tradotte
parole 382 -> 376 · rapporto 0.84 - 1.10 (media 0.99)
FAIL totale: 0 (24 controlli) · verify exit 0 (20 controlli) · sha256[:16] ba3673a78c7a0d5e
FILE CHIUSO: 12 + 13 + 11 + 11 + 10 = 57/57, nessun UI_LABEL nel file
```

## 4. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | `parts/part01.json`, `translation.json`, `check.py`, `verify.py`, i tre documenti |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (24), `verify.py` exit **0** (20) con invariante di file |

## 5. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 10 unità `PENDING`, nessuna scrittura su `state.db`.
- **Nessun equipaggiamento visto nel gioco**: nessuna delle dieci schede è stata osservata in partita.
- **Il file è completo in staging, non nel gioco**: `remnant outfits.txt` è tradotto in tutte le 57 unità e nessuna è
  approvata.
