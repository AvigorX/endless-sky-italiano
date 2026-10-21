# REVIEW — L66 · `data/human/culture conversations.txt`

Revisione del lotto dopo la chiusura dei controlli.

## 1. Coerenza con L58–L65

- Stesso narratore in seconda persona e stesso presente. Le quattro scenette sono **autonome**: ognuna
  comincia e finisce senza dipendere dalle altre, e la traduzione non le cuce insieme.
- Il lessico delle istituzioni resta quello dei lotti precedenti: «Repubblica», «Mondi del Paradiso»,
  «Sindacato», «Coalizione degli Amanti dei Libri» (formazione nuova, ma coerente con la nominalizzazione
  usata altrove).

## 2. Nodi traduttivi aperti (dichiarati)

- **«Mammoth Mastiff»** → «Mastino Mammut»: la bestia è un incrocio inventato; il nome resta ibrido come
  nell'originale.
- **«Mainsail Seadog»** → «Cane di Mare di Mainsail»: il toponimo resta in inglese, la razza è tradotta
  perché descrittiva.
- **«skiff»** (17): «skiff», invariato: è un tipo di imbarcazione con nome proprio inglese.
- **«the Bloom»** → «la Fioritura»: malattia inventata; il nome resta floreale e sinistro insieme.
- **«'nades»** (29): «granate». È un'abbreviazione da bancarella, e in italiano la forma breve
  corrispondente è naturale.
- **«Delvan shipworms»**, **«teredini»**: qui il termine compare solo in forma indiretta («questa parte del
  Sol», il gas nervino); la resa piena arriva in L67, dove va tenuta identica.

## 3. Virgolette dispari

Unità **10** e **34**: due battute aperte e non chiuse (una domanda del locale di Mainsail, una frase del
vecchio di Bloodsea). Riprodotte; `verify.py` confronta l'insieme `(10, 34)`. **Non sono consecutive**,
quindi un controllo «a coppie» le avrebbe perse: serve l'insieme.

## 4. Duplicati

1 gruppo (2 unità). Sono ripetizioni reali del sorgente (due scelte identiche in punti diversi
dell'albero); resa identica per necessità, verificata.

## 5. Cosa NON è stato fatto

- **Nessuna scrittura su `state.db`**: le 45 unità restano `PENDING`.
- **Nessun caricamento nel gioco**: verifica sui file.
- **Nessuna verifica di runtime** delle scelte (4/5/6, 11/12/13/14, 20/21, 31/32/33, 38/39/40/41).

## 6. Rischi residui

- **«Teredini» deve restare identico in L67**, dove la stessa parola ricorre con la variante «teredine di
  Delve» e con la battuta legale del tecnico. Se cambia in uno dei due lotti, il file diventa incoerente
  pur restando verde ai controlli.
- **Il mercato nero di Bloodsea** è descritto con merci illegali e violenza implicita: la traduzione non
  edulcora e non esagera; il registro resta quello di un bazar pericoloso.
- **Il file è al 90,6%**: resta un solo lotto (35 unità) prima della chiusura.

## 7. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — 2 parti, `translation.json`, `check.py`, `verify.py`, documenti |
| ESEGUITO | sì — entrambi gli script lanciati, output letto |
| VERIFICATO | sì — `check.py` `FAIL totale: 0` (33 controlli), `verify.py` exit 0 (36 controlli) |
