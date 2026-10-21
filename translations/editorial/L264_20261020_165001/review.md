# review.md — L264 (`data/remnant/remnant jobs.txt`, righe 703–741) — LOTTO TERMINALE

Registro delle decisioni editoriali dell'**ultimo lotto** del file dei lavori Remnant: la chiusura del soccorso e un lavoro
nuovo, dove la differenza fra **disabilitare** e **distruggere** è il contenuto stesso della missione.

## 1. Le due missioni

| missione | unità | contenuto |
|---|---|---|
| `Rescue 5` | 1–2 | la nave dispersa rientra; il capitano ringrazia di persona, **prima** della notifica ufficiale |
| `Disable 1` | 3–9 | una **Dathnak A'awoj** danneggiata, bloccata vicino a **Postverta**, va resa inoffensiva **senza distruggerla** |

## 2. `disable` / `destroy`: il nodo della missione

| inglese | resa | dove |
|---|---|---|
| `we ask you to only disable it to avoid an atrocity` | «ti chiediamo **solo di disabilitarla**, per evitare un massacro» | scheda (4) |
| `It has a large civilian population` | «Ha **a bordo una grande popolazione civile**» | scheda (4) |
| `You have disabled the Dathnak A'awoj.` | «**Hai disabilitato** la Dathnak A'awoj.» | successo (5) |
| `…has not been disabled yet. Hunt it down and disable it` | «…**non è ancora stata disabilitata**. Dalle la caccia e **disabilitala**» | sollecito (6) |
| `You were unable to disable … without destroying it...` | «Non sei riuscito a **disabilitare** … senza **distruggerla**…» | **fallimento** (8) |
| `thanks you for disabling …` | «ti ringrazia per aver **disabilitato** …» | consegna (9) |

Il verbo della missione è **disabilitare**; **distruggere** appare solo nel ramo in cui il giocatore ha fatto la cosa
sbagliata. La scelta di resa — «disabilitare», non «neutralizzare» — tiene il gioco coerente con i pannelli
dell'interfaccia, dove `disabled` significa nave inoffensiva ma intatta.

La frase `It has a large civilian population` ha un antecedente ambiguo in inglese (la nave? il sistema?). Ho reso **«Ha a
bordo una grande popolazione civile»**, che è l'unica lettura compatibile con «per evitare un massacro»: se la popolazione
fosse nel sistema, disabilitare la nave non salverebbe nessuno.

## 3. Nomi e luoghi

| inglese | resa | nota |
|---|---|---|
| `Dathnak A'awoj` | **Dathnak A'awoj** | nome proprio: invariato, apice compreso, in tutte le 6 occorrenze |
| `Disable Damaged Dathnak A'awoj` | **copiato** | `VALUE` |
| `Postverta` | **Postverta** | sistema |
| `the Embers` | **le Braci** | nome rituale, maiuscolo |
| `a Remnant military prefect` | **un prefetto militare dei Remnant** | grado tradotto, fazione invariata |
| `a logistics adjustment of <payment>` | **un compenso logistico di `<payment>`** | formula già fissata in L262 |
| `a resource allocation of <payment>` | **un'assegnazione di risorse di `<payment>`** | idem |
| `aborting of this mission` | **abbandono della missione** | |
| `they will prioritize other teams` | **assegneranno queste missioni ad altre squadre** | |

## 4. La voce

`Rescue 5` chiude in **gratitudine** («Temendo di non rivedere mai più le Braci, il capitano… ti ringrazia di persona per
averla riportata a casa»), `Disable 1` è **burocratico e morale** («per evitare un massacro», «I Remnant non ne saranno
contenti...»). Il contrasto è nel testo e non va appianato: la seconda missione ha un **limite etico** che la prima non ha.

## 5. Struttura

| cosa | inglese | italiano |
|---|---|---|
| tab | **0** | **0** |
| virgolette | **0** | **0** |
| apici | **7** (6 dal nome, 1 da `You've`) | **8** (i 6 del nome + `un'assegnazione`, `c'è`) |
| segnaposto | 8 | 8, ordine per unità identico |

## 6. Il file chiuso

`data/remnant/remnant jobs.txt`: **87 unità** in quattro lotti (L261–L264), **87 righe distinte**, dalla 19 alla 741. Il
`verify.py` confronta le righe dei quattro `translation.json` con quelle del database: nessun buco, nessuna
sovrapposizione.

## 7. Cosa resta aperto (dichiarato)

- **Nessuna approvazione**: le 87 unità del file sono `PENDING`.
- **Nessun testo visto nel gioco**; **nessuna revisione umana**.
- **Anomalia `Ember Waste`**: «Distesa di Braci» 69 unità contro `Ember Waste` 16 su 85 — sanatoria da fare solo con
  autorizzazione globale sui lotti chiusi.
- **Il resto della campagna**: 2.479 unità su 93 file.
