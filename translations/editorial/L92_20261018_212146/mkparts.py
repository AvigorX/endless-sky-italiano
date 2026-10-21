"""mkparts.py — L92: costruisce `parts/part01.json`, `part02.json`, `part03.json`.

Ultimo segmento del file (righe 230-351). Le stringhe NON contengono tab iniziali: il tab lo antepone
`check.py`. Le virgolette sono quelle del sorgente **per unita'**: le unita' 13 e 21 hanno una sola
virgoletta (citazione lasciata aperta dal testo teatrale) e restano cosi'.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'parts')

P1 = {
 1: '''Vi conducono a una delle porte di trasporto più piccole dello spazioporto, dove un treno compatto serpeggia fuori dalla città e dentro una campagna straordinariamente intatta. Alla fine la guida vi fa scendere; la stazione domina una grande depressione costiera dove migliaia di altri Successori si sono radunati su panche semicircolari attorno a una vasca centrale posta sul bordo del mare. Alcune panche sono state rialzate a formare piccoli palchi riccamente adornati, dove presumibilmente i membri più facoltosi del pubblico possono godersi lo spettacolo in privato.''',
 2: '''Vi sedete e, dopo alcuni minuti, un Successore pronuncia una breve introduzione. Comincia ringraziando la Casata locale per aver finanziato l'evento, prosegue nominando e presentando ciascuno degli attori principali e si chiude con uno strano rituale in cui l'organizzatore dello spettacolo consegna a ogni attore un piccolo contrassegno decorativo. Gli attori li infilano su lunghi fili che portano con sé: diversi di loro hanno già fili molto adorni, che si avvolgono più volte attorno al corpo.''',
 3: '''"Myiara! Da quanto tempo non vediamo il tuo volto gentile fra noi! Torna, e concedici questa grazia", grida un attore dentro la vasca, la voce amplificata per il pubblico. Diversi altri gli roteano attorno, ognuno con una maschera dettagliata e colorata, e ognuno riecheggia "Myiara!" mentre il primo parla. Altri attori ancora entrano da aperture sul fondo della vasca, risalgono a nuoto fino alla superficie e schizzano in aria con eleganza acrobatica prima di atterrare sul coperchio trasparente della vasca.''',
 4: '''"I Miarani non rivedranno mai più la loro gente", dice uno, mentre abito e pelle cambiano insieme colore diventando di un blu intenso. "Perché nobili non siamo, né mai lo saremo..."''',
 5: '''(Fa' attenzione.)''',
 6: '''(Lascia che la mente vaghi.)''',
 7: '''(Vattene prima.)''',
 8: '''Restate fino al primo intervallo: un'attesa comunque scomodamente lunga, e per quanto possiate giudicare la storia è ancora lontanissima dalla conclusione. Lo spettacolo è decisamente alieno, con maschere, acrobazie e un momento sbalorditivo a metà del primo atto, quando uno dei personaggi evoca una tempesta per colpirne un altro. Enormi masse d'acqua, sospese in sfere trasparenti, venivano sollevate dietro il palco da una specie di meccanismo a repulsione.''',
 9: '''Il treno arriva in silenzio dopo solo qualche minuto di attesa e vi riporta allo spazioporto senza problemi.''',
 10: '''"Irja, va' e apri le tue braccia! Ascolta il richiamo anelante del nostro cuore, la sua voce, se le tue orecchie riescono a percepire i piccoli palpiti che una vita mortale produce..."''',
 11: '''Lo spettacolo si rivela straordinariamente lungo e immensamente complesso. La trama segue sia i Successori mortali, sul palco asciutto, sia gli dèi nell'acqua sotto di loro. Myiara Raaja era la creatura adottiva di uno degli dèi, eternamente giovane nel regno immortale, ma fuggì nel mondo dei mortali mentre gli dèi dormivano. Lì visse una vita lunga e piena, finché alla fine morì lasciando dietro di sé Myiara Sera, la propria unica creatura. Gli dèi, destatisi, lamentano la perdita e mandano il messaggero Irja a riprendere Myiara Raaja dal mondo di sopra; ma Irja, accecato dalla gioia, scambia la giovane Myiara Sera per Myiara Raaja. In un disperato sfoggio di astuzia, Myiara Sera riesce ad avvelenare Irja con una bevanda di sonno eterno, spalmandola su un mantello pregiato a cui il dio non sa resistere, convinto che sia un dono di ricongiungimento dalla creatura perduta da tanto tempo.''',
 12: '''Per conservare la propria libertà, Myiara Sera scende nel regno immortale e, in lacrime, avvelena uno per uno gli dèi allo stesso modo, lasciandoli infine come erano all'inizio: dormienti, avvolti nella lenta rotazione delle correnti sottomarine. Nell'epilogo Myiara Sera ha a sua volta due figli: uno resta per sempre con gli dèi, convincendoli a un sonno sempre più profondo e popolato di sogni; l'altro vive nel mondo dei mortali e dà origine a una famiglia di eroi, ognuno dei quali ha i propri spettacoli e altri prodotti culturali.''',
 13: '''"Questo resterà, incontaminato, insensato, nel sepolcro degli abissi. E tutte le moltitudini in lacrime, sopra e sotto, ne serberanno memoria e offriranno doni...''',
 14: '''La messa in scena è sorprendentemente aliena: ogni attore indossa una maschera complessa del proprio personaggio, che si muove insieme al volto sotto di essa. Le maschere dei personaggi mortali sono semplici, anche se espressive; quelle degli dèi sono enormi e drammatiche. Molte hanno lunghe appendici a nastro che non si posano mai nelle correnti della vasca e ruotano continuamente attorno alla testa degli attori.''',
 15: '''I personaggi passano dal regno mortale a quello immortale con salti acrobatici fra la vasca piena d'acqua e la sua superficie superiore quasi asciutta. Nei momenti che devono essere sottolineati, enormi schizzi d'acqua erompono da dietro il palco; in altri, lunghi filamenti del metallo guizzante dei Successori si sollevano tutt'intorno, formando foreste, onde marine e tempeste spaventose con le loro lunghezze lucenti.''',
 16: '''"Myiara giovane, anziana, ancora giovane, ognuna ci scuote dal riposo per farci sentire di nuovo l'amaro negli oceani del nostro sangue..."''',
 17: '''Quando finisce, siete completamente esausti per l'esperienza. Il treno arriva dopo solo pochi minuti di attesa e voi, stipati insieme a molti altri Successori, tornate verso lo spazioporto, arrivando infine a notte fonda.''',
}

P2 = {
 18: '''Lo spettacolo si rivela straordinariamente lungo e incomprensibilmente complesso. La trama sembra seguire sia i Successori mortali, sul palco asciutto, sia gli dèi nell'acqua sotto di loro. Un personaggio di nome Myiara era la beniamina degli dèi, e un altro, apparentemente scambiato per lei, intraprende il lungo lavoro di avvelenare uno per uno tutti gli dèi perché il suo segreto non venga scoperto. Alla fine ha dei figli: uno resta nel regno degli dèi, l'altro torna nel mondo dei vivi.''',
 19: '''La messa in scena è di per sé notevole: gli attori indossano maschere imponenti che si muovono insieme ai loro volti, esaltando le emozioni che intendono rappresentare. In certi momenti della storia enormi schizzi d'acqua erompono da dietro il palco, in altri lunghi filamenti di metallo vengono fatti salire in forme sospese, creando scene di tempesta e di foresta sopra la testa degli attori.''',
 20: '''Quando finisce, siete completamente esausti per l'esperienza. Il treno arriva dopo solo pochi minuti di attesa e voi, stipati insieme a molti altri Successori, tornate verso lo spazioporto, arrivando infine a notte fonda.''',
 21: '''Poco dopo che siete scesi dalla nave, notate due Successori che vi osservano dall'altra parte dello spazioporto; il più giovane tira più volte le braccia del più grande finché i due non si avvicinano a voi. Il più grande apre le braccia in segno di saluto. "Mio figlio voleva che te lo chiedessi, alieno: nei tuoi viaggi hai mai incontrato un Sosrue?''',
 22: '''"Un che?"''',
 23: '''"Forse, ma se l'avessi incontrato non lo saprei con quel nome."''',
 24: '''"Non ho tempo per questo."''',
 25: '''L'adulto assume quella che potrebbe essere una tonalità di rosso delusa, ma prende comunque con sé il figlio e vi lascia ai vostri affari.''',
 26: '''Il piccolo prorompe in un discorso concitato. "Attento al Sosrue, vestito di nero, con i suoi denti e i suoi artigli!" prima che il genitore lo interrompa.''',
 27: '''"Mi scuso", dice l'adulto. "È un mostro, da una poesia per bambini. Il preferito di questo piccolo. Allora racconta anche a me e a mio figlio: fra le distese più ampie delle stelle, hai mai incontrato una creatura dalle lunghe braccia, dall'orecchio fine e dai molti denti, che abita ogni genere di abisso stellare?" Mentre parla, la pelle gli si riga di sottili linee dorate che tremano a ogni sillaba.''',
 28: '''"No, ma ho incontrato alieni interessanti."''',
 29: '''"Una volta ho lottato con una, in fondo a una nebulosa."''',
 30: '''"È una storia terribilmente cupa per un bambino."''',
 31: '''Il piccolo ondeggia piano, gorgogliando una risata strana. "Non è vero", dice il genitore. "Perché mio figlio dovrebbe averne paura?"''',
 32: '''Detto questo, i due Successori scivolano di nuovo nello spazioporto, chiacchierando fra loro mentre si allontanano.''',
 33: '''Il piccolo si dimena piano come se ridesse, assumendo una tonalità di rosa pastello. "Quanto sei serio", dice il genitore. "Forse i tuoi compagni alieni hanno già visto tutti i Sosrue prima che arrivassi tu. Devono essere spiritosi, per essere scampati con la vita!"''',
 34: '''Detto questo, i due si allontanano di nuovo nello spazioporto, avendo chiaramente soddisfatto quel bisogno di divertimento che li aveva portati da voi.''',
}

P3 = {
 35: '''"Le tue ferite!" esclama il piccolo, "e così metà delle tue braccia sono state separate da te!" Si dimena felice, e il genitore prosegue, mentre le linee dorate di prima esplodono in chiazze di colore su tutto il suo corpo. "Devi essere stato spiritoso per scamparla. Senza dubbio il tuo nemico è ancora in agguato, ora che conosce la tua forza. Dovrai essere due volte più astuto, se mai vi incontrerete di nuovo!"''',
 36: '''Dopo quest'ultimo commento, il genitore apre di nuovo le braccia verso di voi e i due Successori scivolano via nello spazioporto, con il piccolo che mormora ancora versi della poesia.''',
 37: '''Anche se lo spazioporto qui è silenzioso e senza vita come sempre, quando scendete per un momento scorgete un oggetto strano e colorato che giace a poca distanza nel buio. A prima vista è difficile dire che cosa sia, ma guardando meglio sembra un piccolo modello in metallo di una navetta Kvelqde, dipinto con colori vivaci dall'aspetto oleoso. Dal retro spunta una minuscola elica, molto consumata.''',
 38: '''(Lascialo dov'è.)''',
 39: '''(Prendilo.)''',
 40: '''(Calpestalo.)''',
 41: '''Il giocattolo si rivela straordinariamente resistente: il vostro assalto non fa altro che graffiarne la vernice, mentre voi siete costretti a tornare zoppicando alla <ship> con un piede contuso.''',
 42: '''Tornate alla vostra nave, con un ultimo sguardo a quel puntino di colore improbabile contro le pareti scure e minacciose della stazione.''',
 43: '''Lasciate cadere il giocattolo poco dopo averlo raccolto, quando un bordo affilato dell'elica vi taglia la mano. Vi affrettate verso la vostra nave stringendovi la ferita che brucia.''',
 44: '''Uno schermo su una delle pareti mostra un messaggio commemorativo: l'immagine di una piccola creatura simile a una salamandra cullata fra le braccia di un Successore, con un testo sotto:''',
 45: '''"Mirja-Mirja, il più leale degli amici e il più gentile degli animali. Di questa materia sono fatti i sogni."''',
 46: '''Mentre vi guardate intorno nello spazioporto, una nave da guerra delle Alte Casate si avvicina per atterrare e prosegue verso un piccolo hangar di allestimento laterale, solo in parte visibile agli sguardi dei civili. Enormi bracci meccanici si abbassano dalla sommità dell'hangar, si calibrano prima sulla forma e sulla posizione del vascello, poi cominciano a scorrere sull'armatura della nave tanto da vicino che sembra quasi la tocchino. Il metallo guizza al passaggio dei bracci: protuberanze viscide dall'aspetto liquido si formano e si richiudono sulla loro scia, schizzando in sé stesse come gocce di pioggia nell'acqua, rugiadose e morbide. Quando l'increspatura si ferma, la trama dello scafo appare in qualche modo cambiata: un po' più ruvida, forse, o di una tonalità di grigio leggermente diversa. La nave decolla poco dopo.''',
}

src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units']
eng = {u['idx']: u['english'] for u in src}
for idx, txt in list(P1.items()) + list(P2.items()) + list(P3.items()):
    assert not txt.startswith('\t'), idx
    assert txt.count('\t') == 0, idx
    assert txt.count('"') == eng[idx].count('"'), (idx, txt.count('"'), eng[idx].count('"'))
    assert txt.strip(), idx
assert sorted(P1) == list(range(1, 18)), sorted(P1)
assert sorted(P2) == list(range(18, 35)), sorted(P2)
assert sorted(P3) == list(range(35, 47)), sorted(P3)

os.makedirs(OUT, exist_ok=True)
for name, d in (('part01.json', P1), ('part02.json', P2), ('part03.json', P3)):
    with open(os.path.join(OUT, name), 'w', encoding='utf-8') as f:
        json.dump({str(k): v for k, v in sorted(d.items())}, f, ensure_ascii=False, indent=1)
print('scritte %d unita (17 + 17 + 12)' % (len(P1) + len(P2) + len(P3)))
