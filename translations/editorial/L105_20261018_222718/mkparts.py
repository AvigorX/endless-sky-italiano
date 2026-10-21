"""mkparts.py — L105: costruisce `parts/part01-04.json` (61 unita', righe 335-506).

**Ultimo segmento di `quarg missions.txt`: chiude il file a 178/178.**
Un solo contesto (`Ask Quarg About Coalition Late`) con **tre tipi**:
56 `MISSION_TEXT`, **4 `UI_LABEL`** (etichette di salto, unita' 29, 31, 36, 38 — **identiche**) e **1 `LOGBOOK`**
(unita' 58, la scheda di Gohl: prosa, tradotta per intero).

**Sette token**: `<origin>` (1), `<first>`+`<last>` (11, 43), `<start planet>`+`<start system>` (49).
**Una citazione aperta** (unita' 26). **Cinque ripetizioni**: 2/6, 3/7, 4/8, 17/20/24, 21/25.

La voce di Gohl: il Quarg anziano parla al **«tu»**, con frasi lunghe e interrotte; le pause sono nel testo
(«Si ferma», «chiude l'occhio») e la resa le conserva.
"""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'parts')

YES = '''(Sì.)'''
NOTNOW = '''(Non ora.)'''
NOINT = '''(No, non mi interessa.)'''
ADVANCED = '''"Anche ora siete più avanzati di loro, no? Com'è che avete perso migliaia di anni fa, quando erano più deboli?"'''
THATSALL = '''"È tutto. Grazie per aver parlato con me."'''

P1 = {
 1: '''Avete ottenuto il grado di Heliarch, il gruppo che ancora oggi resta ostile ai Quarg. Ciononostante vi è stato permesso di atterrare qui su <origin> - non sapete se perché i Quarg semplicemente non sanno che vi siete uniti agli Heliarch, o perché non se ne curano abbastanza da impedirvi di venire sui loro anelli. Volete chiedere ai Quarg la loro versione della storia, alla luce di ciò che avete appreso dagli Heliarch?''',
 2: YES,
 3: NOTNOW,
 4: NOINT,
 5: '''Vi siete uniti al Lunarium nello spazio della Coalizione, e avete persino fatto da messaggero per portare ai Quarg alcune informazioni sul Lunarium stesso, nella speranza che potessero offrire un aiuto. Volete chiedere ai Quarg la loro versione della storia, alla luce di ciò che avete appreso dal Lunarium e dalla vostra visita ai Quarg con Oobat?''',
 6: YES,
 7: NOTNOW,
 8: NOINT,
 9: '''Non sapete mai bene con chi parlare, quando si tratta dei Quarg, ma questa volta siete attirati da uno che si distingue facilmente. Lo giudicate un membro anziano della loro specie: le scaglie sottili gli coprono le dita, e le parti più ossute della testa sono diventate di una tonalità argentea brillante. A differenza di quasi tutti i Quarg che avete visto, indossa una veste bianca, di un pallido bianco sbiadito, con macchie di catene rosse (che in qualche modo tornano a essere tessuto con perfetta naturalezza) sempre più evidenti man mano che si sale, fino a culminare in un cappuccio cremisi e rigido che gli copre la testa. La cosa più sorprendente di tutte, per un Quarg, è però la grande cicatrice che occupa gran parte del lato sinistro del viso, coprendo del tutto il punto dove dovrebbe essere l'occhio sinistro.''',
 10: '''È del tutto immobile, con lo sguardo perduto fisso sul soffitto, finché non vi avvicinate. Non si accovaccia per mettersi alla vostra altezza. Non dice nulla: si limita a fissarvi con il suo unico occhio, di un oro brillante.''',
 11: '''"Salve, sono <first> <last>. Che cosa mi puoi dire della Coalizione?"''',
 12: '''"Salve. È vero che gli Heliarch vi hanno sconfitti e vi hanno rubato i mondi ad anello?"''',
 13: '''Continua a fissarvi per un po', senza nemmeno battere ciglio. Guarda verso una panca in una delle zone più tranquille dello spazioporto e vi fa cenno di seguirlo. Mentre vi sedete, notate che si ferma a metà respiro. Dopo qualche secondo passato a sistemarsi sul sedile, il Quarg finalmente parla.''',
 14: '''"Quelle tre specie nacquero in rapida successione, tutte molto vicine fra loro, rispetto a come le altre specie tendono a essere separate da lunghi periodi di tempo, e ancora più lunghi dalle distanze." La sua voce, pur conservando il ronzio profondo e vibrante che avete imparato ad aspettarvi dai Quarg, è rotta ogni due parole da qualcosa come uno scricchiolio o un cigolio, come se certe corde vocali si fossero infiammate, con un suono sgradevole, simile a un violoncello scordato, che si insinua fra le sue parole. "Così grandi sono i vuoti, che si potrebbe non venire mai a sapere di quelli che sono venuti prima. Ma non fu così per le tre. La prima di loro, i Saryd, erano per molti versi molto simili a noi Quarg nei nostri anni giovani, e forse fummo troppo indulgenti proprio per questo..." Si ferma, si porta una mano sopra la testa, poi l'altra, e chiude l'occhio come per un improvviso mal di testa. I vostri occhi vanno quasi istintivamente alle sue scaglie, aspettandosi che cambino come quelle degli altri Quarg che avete visto. Ma i loro colori restano immutati, gli stessi grigi pallidi e argentei. Passano alcuni secondi, e riporta le mani in grembo, aprendo l'occhio mentre continua. "I Kimek, traumatizzati dai miliardi caduti nelle loro carestie, cercarono aiuto per assicurarsi di non dover mai più affrontare una crisi simile, ed erano ansiosi di stabilire relazioni amichevoli con i Saryd. Gli Arach, in un certo senso, seguono lo sviluppo dell'umanità, anche se erano meno propensi a rendere pubblici i loro conflitti interni. Furono gli ultimi dei tre, e incontrando le altre due, più anziane, investirono pesantemente nella ricerca per mettersi al passo."''',
 15: '''Si ferma di nuovo, dando un'occhiata intorno allo spazioporto. Si fissa su di voi per un po', poi sulle navi che atterrano e partono. "Nel punto in cui i loro territori si intersecano, abbiamo costruito i nostri mondi ad anello. Settemila anni terrestri fa, le tre specie della Coalizione cercarono di impadronirsi di quegli anelli. Dopo secoli... no, un millennio di combattimenti, abbiamo lasciato quella parte della galassia."''',
}

P2 = {
 16: '''"Perché decisero di attaccare voi e i vostri anelli?"''',
 17: ADVANCED,
 18: '''"Qualunque ragione avessero, qualunque cosa li abbia spinti ad attaccarci, non riusciamo del tutto a comprenderla... No." Si ferma, senza sospirare né mostrare molta emozione, e le sue scaglie non danno ancora segno di cambiare. Guarda di nuovo il soffitto, poi di nuovo voi. "No. Siete stanchi di sentire sempre la stessa storia da noi Quarg, vero? Che le specie stolte e giovani fecero guerra senza una buona ragione." Si ferma ancora, soppesando le parole. "Quella guerra non fu il primo caso in cui perdemmo un nostro anello, ma nessuno di noi aveva mai desiderato che un anello andasse perduto. Con tre anelli laggiù, con lo spazio vitale per oltre tre trilioni di Quarg in costruzione, diventammo terribilmente... protettivi verso quella regione, per evitare che interferenze esterne ci creassero di nuovo problemi. I nostri rapporti con i Kimek e gli Arach erano ben lontani dal successo iniziale e dall'amicizia che avevamo con i Saryd, e quando una nave Arach mostrò per la prima volta segni di una tecnologia che riparava le sue piastre dello scafo in volo, un risultato che nemmeno i Saryd avevano ancora ottenuto, noi... saltammo alle conclusioni."''',
 19: '''"Siete 'saltati alle conclusioni'? Che cosa vuoi dire?"''',
 20: ADVANCED,
 21: THATSALL,
 22: '''Volge lentamente la testa verso di voi, con l'occhio che si fissa nel vostro. Passa un minuto scomodo, alla velocità di una lumaca, mentre sembrate lottare per sostenere lo sguardo del Quarg e al tempo stesso trovate difficile guardare altrove.''',
 23: '''"Eravamo andati lì per proteggere le tre specie. Per guidarle. Per osservarle. Abbiamo fallito nell'ultima cosa, perdendo di vista la saggezza e la ragione in favore del timore di passate vergogne. In questo la nostra guida si compromise, perché non si fidavano più di noi. Non fummo più visti come protettori, ma come coloro da cui dovevano proteggersi."''',
 24: ADVANCED,
 25: THATSALL,
 26: '''"Siamo davvero così terribilmente potenti, o la nostra forza è solo la conseguenza dell'essere anziani in una galassia disseminata delle morti premature di altre specie?" chiede. "No... perdonami, non ho risposto alla tua domanda. Noi... molti dei nostri giovani e dei nostri veterani giurarono di non permettere mai più che un anello andasse perduto. Non uccidiamo per diletto, ma per un Quarg difendere un anello è diventato naturale quanto per un umano difendere la propria famiglia.''',
 27: '''"A miliardi si levarono difensori, ignorando i nostri modi di pace, le usanze sociali che ci si aspettava seguissimo e... quelli che tu chiameresti 'ordini'. Dopo qualche secolo, quelli che tollerarono, o furono costretti a tollerare la richiesta di cessate il fuoco, furono evacuati dagli anelli, e poi fu solo questione di tempo prima che quelli di noi rimasti fossero travolti dalla Coalizione."''',
 28: '''Riprende a guardare il soffitto, restando così per un minuto circa.''',
 29: '''heliarch 2''',
 30: '''Poi si volta di nuovo verso di te. "Abbiamo naturalmente notato quel copricapo che gli Heliarch ti hanno dato. Sebbene ti sia ufficialmente unito ai loro ranghi, sei umano. Non sei legato a quella zona di spazio. Non c'è bisogno che tu obbedisca ai loro ordini. Non hai bisogno di tornarci mai più. Non c'è bisogno che tu e noi Quarg siamo nemici."''',
}

P3 = {
 31: '''heliarch ask''',
 32: '''"È una minaccia?"''',
 33: '''"E se invece volessi aiutare gli Heliarch?"''',
 34: '''"No. È un consiglio. Sebbene ti sia unito a loro, sei ancora il benvenuto sui nostri anelli, per il momento. Ma gli Heliarch sono un gruppo formato e legato dalla loro diffidenza e dal loro disgusto per la nostra specie. Se continuerai a seguire gli Heliarch, presto o tardi ti metteranno di certo contro di noi, e a quel punto non posso più garantirti che conserverai un passaggio sicuro nei nostri sistemi, o che ti sarà ancora concesso il permesso di atterrare sui nostri mondi."''',
 35: '''"Le tue ragioni sono tue, ma se ti sei lasciato catturare dalle tue stesse ossessioni, allora posso solo sperare che arriverai a vedere la ragione prima che anche tu vada perduto sulla loro strada."''',
 36: '''lunarium 2''',
 37: '''Poi si volta di nuovo verso di te e dice: "So che ci hai portato qualcuno dalla Coalizione, per una conversazione. Uno che appartiene a un gruppo che cerca di rovesciare gli Heliarch. Fa' attenzione, umano: potranno non essere tecnologicamente avanzati come noi Quarg, ma sono ancora molto forti, e legati al dovere come pochi altri. Tu e i tuoi alleati dovrete affrontare enormi difficoltà, se volete opporvi a loro."''',
 38: '''lunarium ask''',
 39: '''"I Quarg ci aiuteranno a combattere gli Heliarch?"''',
 40: '''"Qualche consiglio su come combatterli?"''',
 41: '''"Abbiamo accettato quella conversazione, quella tua 'intervista'. Oltre a questo, temo che non possiamo aiutare molto senza provocare una guerra. Non cerchiamo di incutere timore nei cuori di quelli della Coalizione, non l'abbiamo mai fatto. Sarebbe un peso per la tua causa se prendessimo parte ai combattimenti."''',
 42: '''"Non essere arrogante. Non sottovalutarli. Non dare la vittoria per scontata, per quanto possano sembrare alle strette, se non vuoi trovarti tu alle strette."''',
 43: '''Vi alzate e state per andarvene quando dice: "<first> <last>." Lo sguardo del Quarg vi trapassa, il suo occhio all'altezza del vostro. "Dov'è la tua casa?"''',
 44: '''"Vengo da New Boston, nella Dirt Belt."''',
 45: '''"Vengo da Midgard, nel Deep."''',
}

P4 = {
 46: '''"Vengo da Mainsail, nei Paradise Worlds."''',
 47: '''"Vengo da Greenwater, nello spazio Hai."''',
 48: '''"Sono nato sulla Terra."''',
 49: '''"Vengo da <start planet>, nel sistema di <start system>."''',
 50: '''"La mia nave è la mia casa."''',
 51: '''"Non ho davvero una casa."''',
 52: '''Accoglie la tua risposta con il più impercettibile dei cenni. "Rare furono le mie visite ai mondi rocciosi abitati dalle altre specie. Sono diversi dai nostri. Così diversi, così... completi." Il suo occhio guizza intorno, guarda ciò che vi circonda, gli altri Quarg qui, e infine le proprie mani e braccia. "Ma noi Quarg dobbiamo arrangiarci."''',
 53: '''Sebbene sia il più impercettibile dei movimenti, giurereste che il Quarg si scosti appena da te. "È forse naturale che una specie finisca per venerare il proprio mondo d'origine, come la culla che l'ha sostenuta finché non ha potuto reclamare le stelle." Poi si avvicina e sussurra: "Ma molti considerano ancora il luogo di nascita della propria specie nulla più che una reliquia di un'epoca passata."''',
 54: '''Le tue parole sembrano smuovere qualcosa in lui, che si porta una mano sulla cicatrice, abbassando lo sguardo. "Una sensazione struggente, non è vero?"''',
 55: '''Dopo averti fissato per qualche secondo, si fissa di nuovo sul soffitto. "Suppongo che altri come te possano immaginare che la nostra vita nei mondi ad anello sia simile alla tua su una nave o in una semplice stazione spaziale." Si ferma di nuovo, questa volta per quasi un minuto. "Considerate le circostanze, potrebbe essere una conclusione ragionevole da parte tua."''',
 56: '''Si volta di nuovo verso di te e chiede: "Hai altre domande per me, Capitano?"''',
 57: '''"Chi sei?"''',
 58: '''Nome completo: Gohl Salyi Memt-Wrik Laz. È un Quarg vecchio e strano, più aperto di quanto la sua specie tenda a essere nel rispondere a domande su argomenti piuttosto delicati.''',
 59: '''"Mi chiamo Gohl Salyi Memt-Wrik Laz. Un Quarg vecchio. Troppo vecchio per il mio bene."''',
 60: '''Lo ringraziate del tempo, e lo vedete alzarsi per andarsene. Appena si allontana dalla panca, notate una dozzina di Quarg pesantemente corazzati che cominciano a seguirlo, alcuni spuntati dai lati della panca, altri sembrati materializzarsi dalle pareti e dal pavimento stessi. Seguono Gohl in una formazione da macchina, e non vi rivolgono mai il minimo cenno.''',
 61: '''Quando vi voltate un'ultima volta verso di lui prima di rientrare nella nave, vedete il distinto riflesso dell'occhio di Gohl che vi guarda da lontano, prima che i Quarg corazzati lo seguano più a fondo nella stazione.''',
}

src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units']
eng = {u['idx']: u['english'] for u in src}
kind = {u['idx']: u['kind'] for u in src}
TAGS = re.compile(r'<[^<>]+>')
ALL = {}
for d in (P1, P2, P3, P4):
    ALL.update(d)
for idx, txt in ALL.items():
    assert not txt.startswith('\t'), idx
    assert txt.count('\t') == 0, idx
    assert txt.count('"') == eng[idx].count('"'), (idx, txt.count('"'), eng[idx].count('"'))
    assert TAGS.findall(txt) == TAGS.findall(eng[idx]), (idx, TAGS.findall(eng[idx]), TAGS.findall(txt))
    assert '[' not in txt and ']' not in txt, idx
    assert txt.strip(), idx
    if kind[idx] == 'UI_LABEL':
        # etichetta di salto: identica al sorgente
        assert txt == eng[idx], (idx, txt, eng[idx])
    if kind[idx] == 'MISSION_TEXT':
        # nessuna battuta lasciata in inglese (le opzioni sono tutte tradotte)
        assert txt.strip() != eng[idx].strip(), idx
assert sorted(P1) == list(range(1, 16)) and sorted(P2) == list(range(16, 31))
assert sorted(P3) == list(range(31, 46)) and sorted(P4) == list(range(46, 62))
assert [i for i in range(1, 62) if kind[i] == 'UI_LABEL'] == [29, 31, 36, 38]
assert [i for i in range(1, 62) if kind[i] == 'LOGBOOK'] == [58]
# il LOGBOOK e' prosa tradotta, non un'etichetta
assert eng[58] != P4[58] and len(P4[58]) > 120
# ripetizioni da costante unica
assert P1[2] is P1[6] is YES and P1[3] is P1[7] is NOTNOW and P1[4] is P1[8] is NOINT
assert P2[17] is P2[20] is P2[24] is ADVANCED and P2[21] is P2[25] is THATSALL
# l'unica citazione aperta
assert [i for i in range(1, 62) if eng[i].count('"') % 2] == [26]
assert not P2[26].rstrip().endswith('"')

os.makedirs(OUT, exist_ok=True)
for name, d in (('part01.json', P1), ('part02.json', P2), ('part03.json', P3), ('part04.json', P4)):
    with open(os.path.join(OUT, name), 'w', encoding='utf-8') as f:
        json.dump({str(k): v for k, v in sorted(d.items())}, f, ensure_ascii=False, indent=1)
print('scritte %d unita (15 + 15 + 15 + 16)' % len(ALL))
