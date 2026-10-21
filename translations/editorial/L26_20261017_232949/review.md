# L26 — data/coalition/coalition missions.txt, righe 2913–3868

Revisione del lotto chiuso. Tutti i numeri sono misurati (`check.py`, `verify.py`, `translation.json`,
`state.db`); se un numero qui non torna con il workspace, vince il workspace.

## 1. Che cosa contiene il lotto

**406 unità** (righe 2913–3868, **ultimo segmento** del file), **10.765 parole EN → 10.151 IT**
(rapporto complessivo **0,943**). **19 contesti**, **5 parti**. Con questo lotto
`coalition missions.txt` è **completo**: 1.580/1.580 unità su due lotti (L25 1.174 + L26 406).

| tipo | unità | note |
|---|---|---|
| `MISSION_TEXT` | 321 | testo di missione, dialoghi, rami |
| `UI_LABEL` | 27 | **non traducibili**: bersagli di `goto` |
| `CONVERSATION` | 23 | **testo visibile** dentro un blocco `conversation` |
| `VALUE` | 13 | nomi di missione |
| `DESCRIPTION` | 13 | descrizioni nel pannello |
| `LOGBOOK` | 6 | voci di registro |
| `DIALOG` | 3 | righe all'atterraggio |

## 2. La trappola che questo lotto ha smentito

L'handoff di L25 annunciava: «dentro i blocchi `conversation` ci sono `label` di condizione da mettere
in `NT`». **La ricognizione ha detto il contrario**: le 23 unità `CONVERSATION` sono il **testo visibile**
del blocco (delimitato da backtick nel `raw`, delimitatore già rimosso in `english`), e vanno tradotte
come prosa. Le `label` di salto sono esattamente le 27 `UI_LABEL`.

Conseguenze misurate:
- `NT` = 27, nient'altro;
- `verify.py` asserisce che **nessuna** `CONVERSATION` sia finita in `NT` e che **tutte e 23** siano
  state tradotte (`italian != english`): è il controllo che avrebbe colto l'errore opposto.

L'handoff è stato corretto nello stesso turno in cui la ricognizione è stata fatta, non lasciato
invecchiare.

## 3. La voce della Coalizione, applicata

Gli Arachi, i Kimek e i Saryd di questo lotto parlano con **ordine rovesciato** (complemento → soggetto
esplicito → verbo in fondo), un solo verbo finale per proposizione.

> «Lavorare per la Casa Idriss, noi lo facciamo» (4) · «Arrivare lì, la sonda presto dovrebbe» (18)
> «Collezionisti di letteratura, noi siamo» (116) · «Molto grati siamo, per questo libro» (233)
> «Al sedicesimo piano, la Priyepichia Publishing è» (294) · «Seguirmi dovete» (299)

Restano in **italiano normale**: il narratore, i `LOGBOOK`, le `DESCRIPTION`, i `DIALOG`, **Anna**
(umana), il **pirata** del deposito di rottami, il **contadino** del mercato e i **consoli** quando
parlano in registro amministrativo. È il contrasto che rende leggibile il testo.

## 4. Terminologia

Voci nuove: `Flopug`, `Kachachee`, `Ikiyachee`, `Akacharra`, `Temporo`, `Anna Fangvin`,
`Oltre l'Iperguida` (`Beyond the Hyperdrive`), `Priyepichia Publishing`, `Ki Patek Ka`, `Humanika`,
`Heliarchia` (`Heliarchy`, distinta dagli Heliarchs), `Anello dell'Amicizia` (`Ring of Friendship`),
`Rete Mondiale` (`Worlds Wide Web`), `iperrete` (`hypernet`), `chip dati` / `scheda dati`,
`casa editrice`, `deposito di rottami`, `Outskirts Gauger` (nome commerciale, invariato),
`Quicksilver`, `Wardragon`, `Punisher`, `Starcross`.

Invariati: `Casa Idriss`, `Darkstone`, `Han`, `Zug`, `Saros`, `Sheragi`, `Hai`, `Unfettered`
(e le altre voci già fissate in L24/L25).

## 5. Duplicati e virgolette

- **7 gruppi di inglese identico, 15 unità**: righe strutturali (risposte alternative con lo stesso
  esito, `(Say nothing.)` ricorrente, `Visit Anna` in due missioni, `(Accompagna Anna…)`).
- **9 unità con virgolette dispari**, tutte riprodotte esattamente:

| unità | virgolette | forma nel sorgente |
|---|---|---|
| 116, 118, 172, 186, 346, 401 | 3 | battuta aperta e non chiusa |
| 252, 309, 311 | 1 | solo virgoletta di apertura |

Il caso **309 / 313** è il più istruttivo: stesso testo, ma 309 ha **una** virgoletta e 313 **due**.
Dare a entrambe una sola virgoletta produce due FAIL insieme — conteggio virgolette *e* duplicato
italiano non giustificato. La differenza del sorgente è l'unica cosa che li distingue, e va riprodotta.

## 6. Correzioni reali

| unità | difetto | correzione |
|---|---|---|
| 34 | tab iniziale assente nel sorgente, presente in italiano | tab rimosso (tab 68/68) |
| 172 | a-capo dentro la stringa JSON: il file non veniva scritto | riscritta come stringa singola |
| 309 / 313 | virgolette 108/109 e duplicato italiano | 309 con 1 virgoletta, 313 con 2 |

Nessun controllo è stato allentato.

## 7. Esito misurato

```
check.py (intero lotto)   FAIL totale: 0
  tab 308/308 · virgolette 593/593 · token 69/69 · backtick 0/0
  rapporto 0,69-1,86 · caratteri non latini: nessuno · trattini lunghi: nessuno
verify.py                 28 controlli · FAIL: 0 · exit 0
translation.json          sha256[:16] 889ca7d8935e9ac0
```

`verify.py` ricontrolla in modo indipendente: riga grezza contro il file, `english/kind/path` contro
`state.db`, stato `PENDING`, nessuna `APPROVED`, id e ordine, collocazione 406 unità righe 2913–3868,
**1.174 unità prima e 0 dopo**, copertura del file **1580/1580** da due lotti senza sovrapposizioni,
27 NT, 23 `CONVERSATION` tradotte e nessuna in `NT`, token, tab/virgolette/backtick, italiano non vuoto,
divieto di trattini lunghi, rapporto, ricostruzione da parti.

## 8. Che cosa non è stato fatto

- **Nessuna approvazione nel database**: le 406 unità sono `PENDING`. Lo staging **non** è approvazione.
- **Nessun rendering nel gioco**: nessuna stringa è mai stata vista a schermo.
- **Nessuna revisione umana terza**: questo documento è scritto da chi ha tradotto.
- **Il libro nel libro**: `Oltre l'Iperguida` è un romanzo inventato, e la traduzione delle sue
  descrizioni (395–402) è una resa, non un adattamento editoriale. Se il libro venisse pubblicato
  davvero nel gioco, servirebbe una revisione dedicata.
