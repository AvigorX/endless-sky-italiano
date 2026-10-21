"""mkparts.py — L91: costruisce `parts/part01.json` e `parts/part02.json`.

Le stringhe NON contengono tab iniziali: il tab lo antepone il costruttore di `check.py`
(`'\t' * tab dell'inglese`). Le virgolette sono quelle del sorgente, riprodotte per unità.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'parts')

P1 = {
 1: '''Poco dopo che siete scesi dalla <ship> per lo spazioporto di <origin>, sentite un tintinnio sommesso ma ben distinguibile alle vostre spalle, vicino al punto in cui la vostra nave sta facendo rifornimento.''',
 2: '''(Vai a vedere da dove viene.)''',
 3: '''(Ignora il rumore.)''',
 4: '''Avvicinandovi alla fonte del tintinnio, sorprendete tre Successori mentre spalmano lo scafo della <ship> con grumi di una soluzione colorata e maleodorante. La puzza è così acre che riuscite a stento ad avvicinarvi senza conati, ma i Successori sembrano non accorgersene, o non interessarsene.''',
 5: '''"Che cosa state facendo alla mia nave?"''',
 6: '''"Scusate, fate tutti parte della squadra di riparazione?"''',
 7: '''I tre Successori trasaliscono al suono della vostra voce, le braccia che scattano mentre si voltano verso di voi. Uno accenna a fuggire, ma uno degli altri gli si aggrappa al braccio e lo riporta indietro al loro fianco. Tutti e tre assumono lentamente una tonalità di viola spento e la loro pelle sembra contrarsi sopra la muscolatura sottostante. Alla fine uno di loro risponde. "Sì, hai ragione tu! Abbiamo l'ordine di applicare questa ... soluzione per lo scafo, per riparare un punto danneggiato qui."''',
 8: '''Ondate di colore risalgono lungo i corpi degli altri, e le punte delle loro braccia ondeggiano piano.''',
 9: '''"Non avevo mai visto una soluzione del genere. Come funziona?"''',
 10: '''"In tal caso mi scuso per l'interruzione. Continuate."''',
 11: '''I tre Successori trasaliscono al suono della vostra voce, le braccia che scattano mentre si voltano verso di voi. Uno accenna a fuggire, ma uno degli altri gli si aggrappa al braccio e lo riporta indietro al loro fianco. Tutti e tre assumono lentamente una tonalità di viola spento e la loro pelle sembra contrarsi sopra la muscolatura sottostante. Alla fine uno di loro risponde. "Noi... ah... facciamo parte della squadra di riparazione! Abbiamo l'ordine di applicare questa... soluzione per lo scafo, per riparare un punto danneggiato qui."''',
 12: '''Ondate di colore risalgono lungo i corpi degli altri, e le punte delle loro braccia ondeggiano piano.''',
 13: '''"Non avevo mai visto una soluzione del genere. Come funziona?"''',
 14: '''"In tal caso mi scuso per l'interruzione. Continuate."''',
 15: '''Il gruppo si scambia sguardi prima che lo stesso Successore risponda di nuovo. "La... ah... soluzione penetra nelle crepe e nelle fessure dello scafo e, quando si asciuga, le sigilla. Oltre a questo non sappiamo nulla; la applichiamo solo come ci dice l'autorità portuale."''',
 16: '''Uno degli altri interviene, aggiungendo allegramente: "Noi non sappiamo niente!" e gli altri lo fulminano con lo sguardo.''',
 17: '''"Ed è anche così colorata! Siete sicuri che non sia una specie di vernice?"''',
}

P2 = {
 18: '''"Affascinante. Continuate."''',
 19: '''"Oh, è per... ah... la sicurezza. Sì, è molto pericoloso toccarla se non sei addestrato, per questo è di un colore così acceso, come avvertimento." Nessuno dei tre indossa alcun tipo di equipaggiamento protettivo, per quanto possiate vedere, e ormai gran parte del gruppo ha cambiato colore assumendo quella che potreste definire una tonalità di rosa divertita. È qualcosa che uno o due stanno chiaramente cercando di reprimere, la pelle che sfuma in gradienti nel tentativo di mantenere la precedente tinta viola spenta. Uno degli altri cerca di nascondere dietro le braccia una borsa piena di altre lattine di "soluzione per lo scafo".''',
 20: '''"Beh, se lavorate per conto dello spazioporto, allora posso certo chiedervi di toglierla."''',
 21: '''"Bel tentativo, ma io e te sappiamo entrambi che cosa sta succedendo qui."''',
 22: '''"Credo che lo scafo della mia nave sia stato riparato abbastanza. Forse è meglio che vi occupiate delle altre navi che avete in lista."''',
 23: '''"Grazie per aver risposto alle mie domande. Continuate pure."''',
 24: '''Il terzetto sembra piuttosto abbattuto all'udire queste parole, ma dopo un bel po' di conciliaboli fra loro alla fine cedono e accettano di togliere la soluzione, purché non informiate l'autorità portuale di ciò che hanno fatto. Si danno da fare per rimuoverla, o almeno recitano la parte, ma non riescono a strofinare via le parti più secche, e alla fine li lasciate andare quando diventa evidente che una parte della vernice si è legata allo scafo in modo permanente.''',
 25: '''Il terzetto si rallegra all'udire queste parole e, dopo qualche conciliabolo, scivola via nello spazioporto trascinandosi le lattine di soluzione, non prima però di lasciarne una a voi per le "riparazioni d'emergenza"; considerando però quanto puzza, non è certo che riuscireste mai a sopportare di applicarla.''',
 26: '''Al vostro ritorno dallo spazioporto, qualche tempo dopo, trovate una zona sul fianco della <ship> ricoperta di una spessa soluzione colorata dal puzzo incredibilmente acre, così forte che riuscite a malapena ad avvicinarvi. Il disegno forma alcune parole nella scrittura dei Successori e, sebbene il dispositivo di traduzione fatichi a interpretare quei glifi non standard, alla fine propone una traduzione più o meno così: "Ryiaa è stata qui! Con gli amici." I tecnici dello spazioporto impiegano diverse ore per raschiarla via del tutto, ma una lieve alterazione del colore resta legata in modo permanente alle lastre dello scafo, per molto tempo a venire.''',
 27: '''Al vostro ritorno dallo spazioporto, qualche tempo dopo, trovate che la "squadra di riparazione" ha ricoperto una zona sul fianco della <ship> con la sua soluzione colorata e puzzolente. Il disegno forma alcune parole nella scrittura dei Successori, accanto a una raffigurazione alquanto grossolana del vostro volto. Il dispositivo di traduzione fatica a interpretare quei glifi non standard, ma alla fine decifra il testo come "'Erjn'... Stupido! Niente aculei, niente cervello!" I tecnici dello spazioporto impiegano diverse ore per raschiarla via del tutto, ma una lieve alterazione del colore resta legata in modo permanente alle lastre dello scafo, per molto tempo a venire.''',
 28: '''Attraversando lo spazioporto, notate diversi manifesti affissi per pubblicizzare una specie di spettacolo, ognuno dei quali mostra un Successore con le braccia aperte in piedi su una sfera di un blu brillante in cui si agitano forme di polpo. "Myiara l'Immortale", recita il titolo.''',
 30: '''Attraversando lo spazioporto, notate diversi manifesti affissi per pubblicizzare una specie di spettacolo, ognuno dei quali mostra un Successore con le braccia aperte in piedi su una sfera di un blu brillante in cui si agitano forme di polpo. "Myiara l'Immortale", recita il titolo, e l'ultima parola riecheggia il nome di questo sistema stellare.''',
 31: '''Mentre guardate il manifesto, un Successore di passaggio vi nota e vi saluta, aprendo le braccia nel modo tradizionale. "L'alieno onorato!" dice. "Lo spettacolo stasera desta il tuo interesse? È una buona compagnia quella che lo mette in scena."''',
 32: '''"Perché no? Puoi mostrarmi dove si tiene?"''',
 33: '''"Il teatro non mi interessa più di tanto."''',
 34: '''"Saresti di certo un ospite ben trattato", dice il Successore. "Seguimi, e non faremo tardi."''',
}

# unita' 29 = UI_LABEL `myiara system`: resta identica, non entra nelle parti.
src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units']
eng = {u['idx']: u['english'] for u in src}
for idx, txt in list(P1.items()) + list(P2.items()):
    assert not txt.startswith('\t'), idx
    e = eng[idx]
    assert txt.count('\t') == 0, idx
    assert txt.count('"') == e.count('"'), (idx, txt.count('"'), e.count('"'))
    assert txt.strip(), idx
assert sorted(P1) == list(range(1, 18)), sorted(P1)
assert sorted(P2) == list(range(18, 29)) + list(range(30, 35)) and 29 not in P2, sorted(P2)

os.makedirs(OUT, exist_ok=True)
for name, d in (('part01.json', P1), ('part02.json', P2)):
    with open(os.path.join(OUT, name), 'w', encoding='utf-8') as f:
        json.dump({str(k): v for k, v in sorted(d.items())}, f, ensure_ascii=False, indent=1)
print('scritte %d unita (parti 17 + 16) · unita 29 = UI_LABEL, esclusa' % (len(P1) + len(P2)))
