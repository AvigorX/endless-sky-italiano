"""mkparts.py — L96: costruisce `parts/part01-03.json` (22 unita' tradotte, righe 192-234).

Quarto lotto di `coalition culture conversations.txt`; **chiude il contesto `Kimek`**.
Le unita' **3 (`defend ww`), 10 (`attack w`), 15 (`attack wr`), 17 (`attack r`), 22 (`attack rr`) sono
`UI_LABEL` di salto**: NON entrano nelle parti, le scrive `check.py` dal sorgente e le asserisce identiche.

Le unita' **14 e 21** hanno lo stesso inglese (il paragrafo dell'assalto) e la stessa resa: sono scritte da
un'unica costante.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'parts')

RAM = '''Cominciate a spingere insieme agli altri: i Saryd si uniscono dal basso, i Kimek e gli Arach salgono strisciando per spingere sulla parte alta del cancello. Si danno il cambio quando qualcuno si stanca, così c'è sempre chi spinge, anche se i loro tentativi non sono dei più efficaci. Dopo un po' sentite uno schiocco e il cancello comincia finalmente a cedere di poco, come se qualcosa che lo sbarrava si fosse spezzato. Quando arrivano gli ultimi della forza principale, portando l'ariete, tutti si fanno da parte perché comincino a batterlo contro il cancello. Il cancello trema a ogni colpo e via via cede sempre di più, ma nemmeno la squadra dell'ariete riesce a sfondare in tempo: il fischietto che segna l'inizio dell'evento risuona di nuovo. Evidentemente significa che il tempo è scaduto e che i difensori hanno vinto.'''
ANOTHER = '''(Prova a trovare un altro modo per entrare.)'''

P1 = {
 1: '''(Vai con gli altri a controllare il cancello posteriore.)''',
 2: '''Arrivati al cancello posteriore, voi e i Kimek restate in silenzio e tendete l'orecchio a chiunque si avvicini da quel lato del forte. In effetti, sentite le zampe Kimek frusciare nell'erba mentre gli attaccanti aggirano il forte. Per fortuna non molti sono venuti a questo cancello, così, con il vostro aiuto, i compagni Kimek non fanno molta fatica a tenerlo chiuso. Il gruppo al cancello principale non è altrettanto fortunato, però, e dopo un breve minuto il fischietto risuona di nuovo. Il vostro gruppo torna nel cortile e trova il cancello sfondato: gli attaccanti con le fasce blu hanno vinto.''',
 4: '''All'inizio tenere il cancello non è troppo difficile, ma dopo qualche minuto comincia a essere martellato da una specie di ariete, e in poco tempo il gruppo là non riesce più a tenerlo chiuso. Nello stesso tempo sentite un trambusto da dietro la baracca e, andando a controllare con gli altri, arrivate a vedere il cancello piccolo aperto. Con gli attaccanti entrati da entrambi i cancelli, il fischietto risuona di nuovo, segnando la fine della battaglia e la vittoria dell'altra parte.''',
 5: '''Vi conduce all'accampamento vicino, dove molti Kimek, Arach e perfino qualche Saryd si sono radunati per l'evento. Quasi tutti aspettano con impazienza dentro una delle tende, o guardano verso il forte; tutti portano lunghe strisce di stoffa blu sopra i vestiti. Quando nota voi due, un'altra organizzatrice Kimek, con addosso quello che sembra un farsetto imbottito, viene a salutarvi. Saluta il collega, che vi presenta e le dice che avete scelto di unirvi agli attaccanti, poi lascia l'accampamento per accogliere una famiglia venuta ad assistere all'evento.''',
 6: '''"Onorate di avervi a combattere al nostro fianco, la nostra compagnia è", esordisce la Kimek corazzata. "Informati sul nostro obiettivo, immagino che siate. Entrare nel forte, dobbiamo, prima che il tempo scada. Dieci minuti, abbiamo, una volta iniziata, la battaglia è." Vi dice di seguirla fino alla "tenda da guerra", un po' più grande delle altre intorno. Lì vi consegna un lungo pezzo di stoffa blu e vi spiega che va indossato, così che gli altri capiscano a quale squadra appartenete. Mentre ve lo avvolgete attorno al collo come una sciarpa e vi guardate intorno nella tenda principale, vedete che qui è custodito un tronco tozzo rinforzato con pezzi di metallo, che la Kimek dice servirà da ariete per forzare i cancelli. Vi fa poi seguire fino al bordo dell'accampamento per mostrarvi i confini di questo "gruppo", segnati da chiazze di vegetazione che indicano i limiti del gioco. "Inoltre, scoraggiare chiunque dal provarci, le spine dovrebbero, ma contro le regole, è, arrampicarsi sulle mura del forte, quindi..." Si interrompe, guardandovi come se solo ora si rendesse conto che per voi una cosa del genere è impossibile. "Scusate, per abitudine, l'ho detto. Partecipare a questo evento, non molti di voi legati al suolo lo fanno; pochi Saryd qui ho incontrato. Ancor meno umani, come potete immaginare."''',
 7: '''Quando ha finito, vi dice che siete liberi di girare per l'accampamento mentre aspettate che la "battaglia" cominci. Passano alcuni minuti prima che risuoni un fischietto acuto, e la Kimek a capo dell'accampamento annuncia a tutti che è arrivato il momento. Guida la carica su per il pendio, con quasi tutti quelli dell'accampamento dietro di lei. Altri si dividono in gruppi più piccoli e salgono lungo gli alberi che separano i gruppi, cercando di avvicinarsi al forte dai lati.''',
 8: '''(Carica con il gruppo principale.)''',
 9: '''(Prendi la strada più lunga, di lato.)''',
}

P2 = {
 11: '''Seguite l'esempio della Kimek e cominciate a correre dritto su per il pendio, verso il forte. Avvicinandovi, però, vedete i difensori, con le strisce di stoffa verde invece che blu, versare secchi di quello che sembra acqua. Quando il liquido scende lungo il pendio incontro ai vostri passi, però, perdete subito l'equilibrio e i piedi scivolano via da sotto, e scivolate per un breve tratto giù per il pendio. Vi rialzate, ma per quanto proviate non trovate un appoggio stabile nell'erba bagnata, e dovete mettere i piedi sui pochi ciuffi cresciuti troppo alti perché il liquido li coprisse. Anche con tutte le loro zampe, i Kimek e i Saryd non se la cavano meglio e si trovano in difficoltà simili, perdendo l'equilibrio ancora e ancora. Solo gli Arach riescono ad avanzare, scavando nella terra sotto l'erba con metà delle zampe a ogni passo. Piano ma con sicurezza aiutano voi e gli altri a salire, e alla fine raggiungete il cancello, per scoprire che i gruppi arrivati dai lati stanno già lavorando per sfondarlo. Vedete anche che cosa intendeva la Kimek parlando di "spine": ciuffi di barbe rossastre e insidiose, lunghe quasi quanto un braccio, coprono i tronchi che formano le mura.''',
 12: ANOTHER,
 13: '''(Aiuta gli altri a sfondare il cancello.)''',
 14: RAM,
 16: '''Voi e una parte del gruppo restate vicini alle mura e le seguite fino all'altro lato, attenti a non graffiarvi con le spine lungo il forte. Trovate presto un altro cancello, più piccolo, e cominciate a spingere. A differenza di quanto potete vedere degli sforzi lasciati al cancello principale, sentite che questo cede subito, e non c'è terreno scivoloso di cui preoccuparvi. Quando si accorgono della vulnerabilità di questo cancello, i Saryd del gruppo chiedono agli altri di farsi da parte. Trasalite un po' quando lo caricano all'improvviso all'unisono, quasi forzandolo con un solo sforzo concertato. Arrivano però altri difensori a tenerlo, e il cancello diventa sempre più difficile da muovere. Un Arach torna al gruppo principale a chiedere altro aiuto, ma quando arrivano, arrivano anche altri difensori. La lotta continua per molti minuti, e gli attaccanti al vostro fianco non riescono a sfondare. Il fischietto risuona di nuovo, segnando la fine della battaglia e annunciando che i difensori hanno vinto.''',
 18: '''Seguite un gruppo fino ai bordi di questo gruppo, perdendo un po' di tempo prima di cominciare la corsa su per il pendio. Quando alla fine partite, vi voltate e vedete il gruppo principale inciampare e cadere all'indietro più e più volte. Sembra che i difensori, che portano contrassegni verdi invece che blu, stiano versando del liquido scivoloso dai merli sopra il cancello, rallentando chi arriva lungo la via diretta. Raggiungete la cima mentre la forza principale sta ancora lottando, e il vostro gruppo si dirige al cancello. Lungo la strada vedete che cosa intendeva la Kimek parlando di "spine": ciuffi ravvicinati di barbe rossastre e insidiose, lunghe quasi quanto un braccio, coprono i tronchi che formano le mura. Arrivate al cancello, ma per quanto spingiate non cede di un millimetro, chiaramente sbarrato dall'interno. Alla fine il gruppo principale vi raggiunge, ma anche con molte più persone a spingere il cancello resta saldo e immobile.''',
 19: ANOTHER,
 20: '''(Continua a cercare di sfondare il cancello.)''',
 21: RAM,
}

P3 = {
 23: '''Voi e una parte del gruppo restate vicini alle mura e le seguite fino all'altro lato, attenti a non graffiarvi con le spine lungo il forte. Trovate presto un altro cancello, più piccolo, e cominciate a spingere. A differenza di quanto potete vedere degli sforzi lasciati al cancello principale, sentite che questo cede subito, e non c'è terreno scivoloso di cui preoccuparvi. Quando si accorgono della vulnerabilità di questo cancello, i Saryd del gruppo chiedono agli altri di farsi da parte. Trasalite un po' quando lo caricano all'improvviso all'unisono, quasi forzandolo con un solo sforzo concertato. Arrivano però altri difensori a tenerlo, e il cancello diventa sempre più difficile da muovere. Un Arach torna al gruppo principale a chiedere altro aiuto, ma quando arrivano, arrivano anche altri difensori. La lotta continua per un po', finché non sentite forti colpi dall'altro lato del forte. L'organizzatrice Kimek gira sul retro per dire a tutti di tornare all'ingresso principale. Arrivati al cancello principale, vedete che l'ariete l'ha sfondato: cosa che dev'essere stata più facile perché in tanti l'avevano lasciato incustodito per difendere il cancello posteriore. A quel punto il fischietto risuona di nuovo, segnando la fine della battaglia e annunciando che gli attaccanti hanno vinto.''',
 24: '''L'organizzatrice Kimek a capo della vostra parte lancia un evviva, che si diffonde rapidamente fra gli altri. Dopo che i capi delle due squadre si sono incontrati per salutarsi, a tutti viene chiesto di restituire la stoffa colorata ricevuta e di scendere dal pendio. Il vostro gruppo viene indirizzato a un edificio vicino per lavarsi via la terra, se serve. Una volta puliti, tornate all'accampamento, dove il Kimek che vi ha portato qui vi aspetta per guidarvi a molti tavoli bassi con i piatti sopra; a quanto pare, la ricompensa per la vittoria è un banchetto. Dato che quasi tutti i partecipanti sono Kimek, quasi tutto il cibo è preparato come piace a loro: una poltiglia brodosa e parzialmente digerita. Per fortuna ci sono alcuni pasti preparati come piacciono alle altre specie, quindi potete sceglierne uno pensato per i Saryd; i loro piatti sono quanto di più vicino alla cucina umana ci sia, qui.''',
 25: '''Il primo piatto Saryd offerto è fatto di molte verdure cotte, disposte in un piccolo mucchio sul piatto, con un sottile filo di vapore che ancora sale. Parlando con gli organizzatori, venite a sapere che i pasti vogliono rappresentare i raccolti della "fattoria" del forte, e che chi vince si guadagna il diritto al banchetto. Finito di mangiare, tornate dove il treno vi ha lasciati e salite sul successivo, diretto allo spazioporto.''',
 26: '''L'organizzatore Kimek dell'altra parte lancia un evviva, che si diffonde rapidamente fra gli altri. Dopo che i capi delle due squadre si sono incontrati per salutarsi, a tutti viene chiesto di restituire la stoffa colorata ricevuta e di scendere dal pendio. Il vostro gruppo viene indirizzato a un edificio vicino per lavarsi via la terra, se serve. Una volta puliti, il Kimek che vi ha portato qui vi aspetta accanto all'accampamento per guidare i vostri avversari ai molti tavoli bassi con i piatti; a quanto pare, la ricompensa per la vittoria è un banchetto. "Un peccato, è, che la battaglia la vostra squadra abbia perso", dice. "Ma spero che, comunque, l'evento vi sia piaciuto."''',
 27: '''Prima di andarsene con i vincitori, vi spiega qualcosa in più sull'evento, dicendovi che i pasti serviti al banchetto vogliono rappresentare i raccolti della "fattoria" del forte, e che chi vince se ne guadagna il diritto. Infine vi ringrazia per aver partecipato e va con i vincitori ai tavoli. Voi tornate dove il treno vi ha lasciati e salite sul successivo, diretto allo spazioporto.''',
}

src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units']
eng = {u['idx']: u['english'] for u in src}
kind = {u['idx']: u['kind'] for u in src}
NT = [3, 10, 15, 17, 22]
for idx, txt in list(P1.items()) + list(P2.items()) + list(P3.items()):
    assert not txt.startswith('\t'), idx
    assert txt.count('\t') == 0, idx
    assert idx not in NT and kind[idx] == 'MISSION_TEXT', idx
    assert txt.count('"') == eng[idx].count('"'), (idx, txt.count('"'), eng[idx].count('"'))
    assert txt.strip(), idx
assert sorted(P1) == [1, 2, 4, 5, 6, 7, 8, 9], sorted(P1)
assert sorted(P2) == [11, 12, 13, 14, 16, 18, 19, 20, 21], sorted(P2)
assert sorted(P3) == [23, 24, 25, 26, 27], sorted(P3)
assert P2[14] == P2[21] == RAM and P2[12] == P2[19] == ANOTHER
assert [i for i in range(1, 28) if kind[i] == 'UI_LABEL'] == NT

os.makedirs(OUT, exist_ok=True)
for name, d in (('part01.json', P1), ('part02.json', P2), ('part03.json', P3)):
    with open(os.path.join(OUT, name), 'w', encoding='utf-8') as f:
        json.dump({str(k): v for k, v in sorted(d.items())}, f, ensure_ascii=False, indent=1)
print('scritte %d unita (8 + 9 + 5) + 5 UI_LABEL dal sorgente' % (len(P1) + len(P2) + len(P3)))
