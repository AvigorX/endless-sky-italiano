# REPORT — L220 · `successor ships.txt` (terzo lotto)

## 1. Contenuto

Quattro navi dei Successori: la **Nnaatej**, vascello specialistico che porta i passeggeri dall'oceano profondo allo
spazio profondo e ritorno, con scafo stabile alla pressione e resistenza alla corrosione; la **Nnesaarau**, trasporto di
lusso recentissimo e poco popolare, apprezzato da alcuni piloti come nave da corsa o corriere veloce; l'**Ojde**, il cargo
più grande impiegato dai Successori, con **due schede**; e l'apertura della scheda **Seiitej**.

## 2. Difficoltà

1. **La coppia 23/25.** Le due descrizioni dell'Ojde sono lo stesso testo: 374 caratteri contro 372, e la differenza sono
   **solo le due virgolette** attorno al nome nella 23. Ho tradotto una volta e ricavato l'altra togliendo le virgolette,
   verificando in entrambe le lingue che `t[23].replace('"','') == t[25]`. Se avessi riformulato la seconda «per farla
   suonare meglio», la stessa nave avrebbe avuto due schede discordanti e nessun controllo sul totale l'avrebbe visto.
2. **Le 34 virgolette.** Non sono 2 × 17: sono 2 × 16 `TEXT` = 32, più **2 dentro una `DESCRIPTION`**. Il contratto lo
   annunciava come «da misurare», e la misura ha confermato la riga 863. Un controllo «2 per ogni `TEXT`, zero altrove»
   sarebbe caduto su un testo corretto.
3. **L'articolo davanti a un nome fra virgolette.** In italiano `l'"Ojde"` (elisione fuori dalle virgolette) tiene il nome
   citato senza spezzare la grammatica; per la 25, senza virgolette, `l'Ojde`. La differenza di due caratteri fra le due
   versioni si conserva **anche in italiano**.
4. **`House Chydiyi` → «Casa Chydiyi»**: le Case dei Successori si traducono, il nome proprio no.
5. **`Bulk Freighter` e `Behemoth`** sono nomi di navi umane: restano inglesi, e il controllo li conta due volte ciascuno.
6. **`restrictive internals`** → «interni poco flessibili»: nel gergo del gioco `internals` sono gli spazi di
   equipaggiamento, non gli arredi.
7. **`slowing effects`** → «effetti di rallentamento»: è un effetto di gioco, non una figura retorica.

## 3. L'errore mio, e la correzione strutturale

Alla prima stesura ho **trascritto a mano** i nomi delle `TEXT` invece di leggerli, e **11 unità su 20** erano sbagliate:
avevo messo `"Ojet" Bimodal Coilgun` dove il sorgente dice `6-"Ruuv" Betavoltaic Cell`, `"Ej" Shield Cortex` dove dice
`1-"Uurau" Betavoltaic Cell`, e così via. Nessuna era inventata di sana pianta — erano nomi veri del file, presi dalle unità
sbagliate — ma il risultato era falso lo stesso.

Il confronto automatico le ha segnalate **tutte e 11**. La correzione non è stata testuale ma **strutturale**: `parts/part01.json`
ora si **genera dal sorgente**, copiando `english` per ogni unità `TEXT` e `VALUE`, e prendendo dalle mie traduzioni solo le
6 `DESCRIPTION`. I nomi non si trascrivono più: si copiano con il codice, e il `check.py` verifica le 20 unità
**carattere per carattere**.

## 4. Numeri osservati

```
unita' 26 · {'TEXT': 16, 'DESCRIPTION': 6, 'VALUE': 4} · tutte PENDING
1 tab (unita' 24) · 34 virgolette (32 TEXT + 2 nella 23) · 2 apici EN / 12 IT · 0 segnaposto
4 contesti: Nnesaarau 9, Ojde 9, Nnaatej 7, Seiitej 1
righe 634/873 · 70 prima (L218+L219) · 50 dopo · confine riga 904 TEXT (NON VALUE)
20 unita' identiche all'inglese, 6 tradotte (le DESCRIPTION); coppia 23/25 verificata
parole 440 -> 487 · rapporto 1.00 - 1.16 (media 1.02)
FAIL totale: 0 (28 controlli) · verify exit 0 (18 controlli) · sha256[:16] 3373e098d9af319f
```

## 5. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | `parts/part01.json` generato dal sorgente, `translation.json`, `check.py`, `verify.py`, i tre documenti |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (28), `verify.py` exit **0** (18) |

## 6. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 26 unità `PENDING`, nessuna scrittura su `state.db`.
- **Nessuna nave vista nel gioco**, nessuna schermata di allestimento aperta.
- Restano **50 unità** nel file, **26** dopo la riga 1137: L222 lo chiuderà.
