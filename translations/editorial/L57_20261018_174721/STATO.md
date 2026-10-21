# STATO — L57 · `data/gegno/gegno I corroboration.txt`

**Lotto chiuso. Il file è chiuso: 298/298.**

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L57_20261018_174721` |
| File | `data/gegno/gegno I corroboration.txt` |
| Unità | **127** (righe **943–1287**; la finestra di export 905–1287 contiene righe senza unità) |
| Parti | **4** — 23 · 47 · 34 · 23 |
| Contesti | **3** — `Gegno Intervention` 1–23 (23), `Acquiescence` 24–104 (81), `Gegno Asteroid Mining Prologue` 105–127 (23) |
| Tipi | 101 `MISSION_TEXT` · 17 `UI_LABEL` · 3 `DIALOG` · 3 `VALUE` · 3 `DESCRIPTION` |
| Parole | 4.974 EN → 4.514 IT (**0,908**) |
| Rapporto per unità | **0,57 – 1,47** (gate 0,55–1,90) |
| `UI_LABEL` (`NT`) | **17** — 16, 18, 20, 38, 44, 60, 79, 81, 86, 91, 93, 97, 101, 112, 116, 119, 121 |
| `DIALOG` | **3** — 22, 23, 125 (22 e 23 identiche nel sorgente) |
| `LOGBOOK` / `CONVERSATION` / `TEXT` | **0 / 0 / 0** (assenze dichiarate) |
| Tab · virgolette | **94** · **60** (0 dispari, 0 quadre, 0 backtick) |
| Token `<…>` | **13** in 6 famiglie (`<destination>` 4, `<ship>` 3, `<first>` 2, `<last>` 2, `<origin>` 1, `<payment>` 1) |
| Duplicati inglesi | **4 gruppi / 8 unità** |
| sha256 `translation.json` | `c3f3b8a9de69cfe1…` |
| `check.py` | **33 controlli**, `FAIL totale: 0` |
| `verify.py` | **41 controlli**, exit **0** |

## Dove siamo nel file

L57 **chiude** `gegno I corroboration.txt`:

| Lotto | Unità | Righe |
|---|---|---|
| L56 | 171 | 29–904 |
| L57 | 127 | 943–1287 |
| **Totale** | **298/298** | |

`0` unità dopo la 1287, `max(line) = 1287`. L'invariante «di file» qui è legittimo (decisione 181) ed è
asserito **insieme**: chiusura, `max(line)` e copertura 298/298 sui due lotti.

## Cosa è stato deciso qui

1. **`DIALOG` 22/23 ripetono 170/171 di L56.** Stessa scena, stessi due esiti. La resa è **la stessa
   stringa**, e `verify.py` la confronta con il testo letterale: se un domani cambia in un lotto e non
   nell'altro, il controllo diventa rosso.
2. **`<payment>` compare per la prima volta nella linea Gegno** (unità 126): «ti paga una somma di
   `<payment>` per il lavoro». Il token resta invariato e la frase regge sia con un numero sia con una
   descrizione.
3. **Il discorso del trio Gegno** (unità 72–75) è una scena assembleare: il narratore descrive, non
   interpreta. «You feel as if you are standing among them as part of the gathering» è reso senza
   aggiungere un giudizio sul giocatore.
4. **Le due «armi-asta»** (unità 99 e 103) usano la stessa scena di chiusura: il Gegno solleva l'asta,
   la capovolge, il cratere compare accanto alla nave. La resa è identica dove il testo è identico.
5. **Le righe in lingua Gegno** restano identiche: `"Eyuu udyom Gegno tyysis…"`, `"Gegno Dueyu Eitch
   echre…"`, `"Eyuu idu keiou ghynem uf, 'Dueyu.'"`. Non sono testo traducibile.
6. **`Dueyu Earth?`** (unità 89) resta in inglese **con** `Dueyu`: è il giocatore che tenta di ripetere un
   nome alieno appena sentito, e il tentativo fa parte della scena.

## Verifica

```bash
cd staging/editorial/L57_20261018_174721
python check.py                 # FAIL totale: 0   (33 controlli)
python verify.py                # exit 0           (41 controlli)
```

Il primo esito di `verify.py` è stato **rosso di proposito**: asseriva `righe 905–1287` e la prima unità
sta sulla **943**. Corretto il numero, non il controllo. Questo è il tipo di errore che il documento deve
riportare: la finestra di export non coincide con la prima unità.

## Prossimo passo

Il file è chiuso. Il prossimo lotto (**L58**) apre un nuovo file: si parte da `next_section.py` sul
prossimo file non coperto, non da questo.
