"""mkparts.py — L107: costruisce `parts/part01-02.json` (38 unita', righe 121-212).

Tre contesti: coda di `Setar Fort Heating` (126-127), `Korath Family to Ringworld` (130-169), `Korath Livestock`
(172-212).

**34 `MISSION_TEXT` + 2 `VALUE` + 2 `DESCRIPTION`**: i `VALUE` (unita' 3 e 20) sono nomi di missione e restano
**identici**, con `<planet>` dentro; le `DESCRIPTION` (4 e 21) si traducono per intero.

**Zero quadre, zero citazioni aperte, zero ripetizioni** (asseriti vuoti). **21 token** in sei famiglie, fra cui
`<bunks>` — nuovo per il progetto: posti letto occupati, distinto da `<tons>` che e' il carico.

L'unita' 16 e' il **Quarg che parla male la lingua**: inglese storpiato (`pridefulest`, `happyfully`,
`vicinitied`) reso con un italiano storto ma comprensibile.
"""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'parts')

P1 = {
 1: '''Quando arrivate su <planet>, un gruppo di Korath aspetta per scaricare il carico. Provate a imitare il loro gesto di saluto, sollevando le mani con i palmi verso il gruppo. Sembrano sorpresi ma sibilano in segno di approvazione.''',
 2: '''Ben presto tutte le provviste sono fuori dalla nave. I Korath vi fanno un gesto di apprezzamento, poi cominciano a disimballarle proprio in mezzo allo spazioporto. Una folla si è già radunata intorno alle attrezzature. Sembra che qui saranno usate bene. Quando tornate alla nave, vedete che il Wanderer che vi aveva offerto il lavoro vi ha trasferito il pagamento di <payment>.''',
 3: '''Korath to <planet>''',
 4: '''Una famiglia Korath di <bunks> persone vi ha pagato <payment> per portarla al mondo ad anello dei Quarg di <destination>.''',
 5: '''La foschia è così fitta su Laki Nemparu che anche le ore più luminose del giorno vi sembrano sera. Tutto qui è così sporco che la maggior parte dei Korath sembra di qualche tonalità più scura rispetto a quelli di altri pianeti. Nel giro di pochi minuti anche sulla vostra pelle si attacca un sottile strato di fuliggine.''',
 6: '''Mentre osservate ciò che vi circonda, un Kor Efret vi si avvicina, seguito da altri due: uno, a giudicare dalla taglia, è probabilmente un bambino, e l'altro è curvo su un bastone che usa per sostegno, probabilmente anziano. Quello davanti parla in lingua Korath e capisce presto che non la capite affatto. Il Kor Efret si ferma a prendere un respiro profondo, poi scoppia in un accesso di tosse per aver aspirato troppa foschia. Passa quasi un minuto intero prima che si riprenda.''',
 7: '''Il Korath indica il cielo e dice: "<planet>, <planet>," mentre gesticola verso i due Korath che sono con lui. Vi premono 500 crediti nelle mani e continuano a borbottare in lingua Korath. <planet> è il nome del mondo ad anello dei Quarg nello spazio Korath. Devono volere un passaggio fin lì. 500 crediti sono scandalosamente pochi per qualunque lavoro di trasporto, ma a giudicare dal loro aspetto non possono permettersi di pagarvi di più. Volete portarli su <planet>?''',
 8: '''(Sì.)''',
 9: '''(Sì, e restituite loro i crediti.)''',
 10: '''(No.)''',
 11: '''Vi mettete i crediti in tasca e fate segno di seguirvi alla nave. Quando il Korath capisce che avete accettato, sospira di sollievo e gesticola rapidamente in segno di gratitudine. Li accompagnate alle loro cuccette... e alla doccia.''',
 12: '''Le spalle del Korath si abbassano quando gli restituite i crediti, ma la delusione diventa sorpresa quando fate segno verso la nave. Quando capiscono che state cercando di rifiutare il denaro, gonfiano il petto e vi spingono di nuovo i crediti in mano. Non accettano un no come risposta, così vi mettete i crediti in tasca e li portate alla nave. Li accompagnate alle loro cuccette... e alla doccia.''',
 13: '''Restituite i crediti al Korath e le loro spalle si abbassano. Guardate il terzetto allontanarsi finché la foschia fitta non li nasconde. Non potete fare a meno di sentirvi un po' in colpa.''',
 14: '''Vi piace la nuova compagnia sulla nave. Il bambino vi ha insegnato un gioco in cui a turno si lancia una palla contro la parete. Passate un'ora o due a giocare con loro nella stiva.''',
 15: '''Quando arrivate, decidete di accompagnare la famiglia nello spazioporto. Vicino alla baia di attracco aspettano altri due Korath, uno adulto e uno anziano, e i tre che avete trasportato corrono a incontrarli. Quando la felice riunione si calma, il Korath che vi aveva chiesto il passaggio si volta verso un Quarg lì vicino e dice qualcosa. Il Quarg risponde, poi si volta verso di voi.''',
 16: '''"Questo individuo orgogliosissimo ha dichiarato che riguardava con reverenza la mia traduzione debitrice e chiede che il mio uso di essa sia preferito. Sono incline ad acconsentire alla sua richiesta felicemente." Questo Quarg non sembra avere una presa particolarmente salda della vostra lingua, ma dovreste riuscire più o meno a capire quello che viene detto. "Il camerata dice: 'Ti ringrazio sproporzionatamente per aver riunificato il mio famigliare, in servizio fatidico alla nostra camerataggine.' Aggiunge inoltre che non c'era metodo in cui questa accozzaglia sarebbe vicinata se la vostra presenza fosse stata assenziata. È tutto."''',
 17: '''"Ditegli che non è affatto un problema."''',
 18: '''"Ditegli che ha una famiglia meravigliosa, e che sono stato felice di aiutare."''',
 19: '''Il Quarg annuisce e si volta a tradurre. Il Korath risponde tenendo i palmi verso di voi e muovendoli in un ampio movimento circolare. "Questo sta a indicare gratitudine di misura sanissima. Ti ringrazia per le tue parole fortunate e ti augura viaggi gentili," dice il Quarg. Accogliete la risposta, ringraziate il Quarg per i suoi servizi di traduzione (approssimativi) e tornate alla nave.''',
}

P2 = {
 20: '''Livestock to <planet>''',
 21: '''Trasporta <bunks> agricoltori Korath e il loro <cargo> su <destination>. Ti hanno già pagato parte dei 10.000 crediti concordati.''',
 22: '''Un Kor Efret che indossa diversi strati di un tessuto simile alla lana vi si avvicina. Solleva entrambi i palmi verso di voi, poi vi fa cenno di seguirlo in un vicolo. Non pensate che rappresenti una minaccia, ma non fa male essere prudenti.''',
 23: '''(Seguilo nel vicolo.)''',
 24: '''(Fai il sicuro e vattene.)''',
 25: '''Il Korath si infila fra gli edifici, addentrandosi in una zona abbandonata della città. Il Korath gira un angolo, e mentre un vento freddo vi investe, da dietro l'angolo arriva un belato allarmante.''',
 26: '''(Gira l'angolo.)''',
 27: '''(Voltati e prova a correre allo spazioporto.)''',
 28: '''Sentite uno scalpiccio dietro di voi e vi voltate. Tre Korath torreggianti, con indosso abiti pesanti simili, sono usciti da una porta lì vicino e vi vengono incontro. Il belato torna, e vi voltate di nuovo, solo per vedere il Kor Efret di prima tornato da dietro l'angolo. Qualunque possibilità aveste di uscirne, ora è sparita.''',
 29: '''Quello davanti si volta verso la direzione da cui è venuto, e il Korath dietro di voi sibila e fa segno di andare avanti. Sembra che dobbiate seguirli. Vi preparate e girate l'angolo per vedere... animali?''',
 30: '''Gli edifici arrugginiti hanno lasciato il posto a una enorme piazza abbandonata, e tutto lo spazio è occupato da un misto di bestiame di grossa taglia e provviste. Vi ricordano delle pecore, ma sono circa cinque volte più grandi, hanno sei zampe e vengono in una varietà di colori bruno-neri. Ognuna ha un manto folto e una coperta aggiuntiva fatta del loro stesso tessuto simile alla lana. È lo stesso materiale che indossano questi Korath. Anche con la coperta in più, le "pecore" stanno accalcate in piccoli gruppi e sembrano soffrire il freddo. Belano di tanto in tanto, forte, ogni volta che un vento freddo attraversa la piazza. Per fortuna, questi Kor Efreti sembrano agricoltori, non rapinatori. Questo dev'essere l'unico posto vicino allo spazioporto dove potevano tenere insieme tutto il gregge.''',
 31: '''Quello che vi ha portato qui, che sembra anche essere il capo, vi fa cenno di avvicinarvi. Ha aperto una mappa di carta, una vista rara nell'era dei viaggi interstellari. Quando date un'occhiata, capite che non è della zona locale, ma dello spazio; sembra mostrare i sistemi circostanti. Il Korath ne indica uno, si ferma e gesticola ampiamente verso il misto di bestiame e provviste, poi porta il dito su un altro sistema e dice qualcosa che suona all'incirca come <planet>. "<planet>?" confermate, e il Korath sibila in approvazione. Sembra che vogliano un trasporto fin lì. Scommettete che il bestiame e le provviste occuperanno più o meno <tons>, e che nel gruppo ci siano <bunks> agricoltori Korath.''',
 32: '''Tira fuori dalla tasca un mazzo di 200 crediti e lo posa a terra, poi ci disegna intorno un cerchio con un pezzo di gesso. Ne disegna altri quattro, fa un grande cerchio intorno ai cinque più piccoli, poi disegna altri nove grandi cerchi. La vostra ipotesi migliore è che offra 10.000 crediti per il trasporto.''',
 33: '''(Accetta di portarli.)''',
 34: '''(Rifiuta il lavoro.)''',
 35: '''Indicate il vostro accordo puntando <planet> sulla mappa e gesticolando verso di voi. Quando capisce che avete accettato, il Korath tiene i palmi verso di voi e li muove in un movimento circolare. Ne portate uno alla nave mentre gli altri restano a preparare gli animali. Quando arrivate, si mette subito al lavoro stendendo teli sul pavimento e spargendoci sopra una specie di paglia. Dopo un po', notate che una delle "pecore" esce da un vicolo guidata da un agricoltore rimasto indietro. Dietro c'è un altro animale, poi un altro. La fila di bestiame, intervallata dagli agricoltori che tengono il passo, si fa lentamente strada nel vostro hangar nell'ora successiva.''',
 36: '''Mentre entrano nella nave a clima controllato, gli agricoltori tolgono le pesanti coperte simili alla lana dalle "pecore" e si tolgono gran parte dei loro strati. Uno porta l'intero mucchio di tessuto a un venditore lì vicino e lo scambia per crediti, mentre gli altri tornano a prendere le provviste ancora nella piazza. Al calare della notte, tutto e tutti sono finalmente caricati sulla nave. Il Korath che aveva venduto i vestiti al mercante vi consegna l'intero mazzo di 4.100 crediti. Sperate di ricevere il resto una volta arrivati su <planet>.''',
 37: '''Gli animali stanno sorprendentemente comodi sulla nave, ma i Korath faticano. A giudicare da quante volte entrano ed escono dal bagno durante il viaggio di un salto, nessuno di loro è mai stato nell'iperspazio. Quando si riprendono dal mal di spazio, si danno da fare a radere il pelo simile alla lana dagli animali e a raccoglierlo.''',
 38: '''Mentre atterrate e aprite le porte del carico rivelando il caldo mondo di <planet>, gli animali si agitano eccitati. Sembrano molto più energici di qualsiasi momento precedente, tanto che i Korath fanno fatica a tenerli tutti insieme mentre escono dalla nave. La lenta desertificazione di questo pianeta è di certo motivo di preoccupazione, ma sembra offrire un ambiente molto più sano a questi animali di quanto facciano le temperature gelide di Setar Fort. Una volta che tutto è fuori dalla nave, un Korath porta la lana a un altro venditore e la vende di nuovo, poi torna e vi consegna 5.900 crediti. Con i 4.100 crediti che vi ha dato prima di partire, avete ricevuto tutti i 10.000 crediti promessi. Solleva le mani con i palmi verso di voi e poi se ne va a raggiungere gli altri agricoltori.''',
}

src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units']
eng = {u['idx']: u['english'] for u in src}
kind = {u['idx']: u['kind'] for u in src}
TAGS = re.compile(r'<[^<>]+>')
ALL = {}
for d in (P1, P2):
    ALL.update(d)
for idx, txt in ALL.items():
    assert not txt.startswith('\t'), idx
    assert txt.count('\t') == 0, idx
    assert txt.count('"') == eng[idx].count('"'), (idx, txt.count('"'), eng[idx].count('"'))
    assert TAGS.findall(txt) == TAGS.findall(eng[idx]), (idx, TAGS.findall(eng[idx]), TAGS.findall(txt))
    assert '[' not in txt and ']' not in txt, idx
    assert txt.strip(), idx
    if kind[idx] == 'VALUE':
        assert txt == eng[idx], (idx, txt, eng[idx])
# uniche unita' identiche: i due VALUE (per regola) e la 10 `(No.)` = `(No.)` (coincidenza linguistica, come in L104)
assert [i for i in ALL if kind[i] != 'VALUE' and ALL[i].strip() == eng[i].strip()] == [10]
assert ALL[10].strip() == '(No.)'
assert sorted(P1) == list(range(1, 20)) and sorted(P2) == list(range(20, 39))
assert [i for i in range(1, 39) if kind[i] == 'VALUE'] == [3, 20]
assert [i for i in range(1, 39) if kind[i] == 'DESCRIPTION'] == [4, 21]
# zero quadre, zero citazioni dispari nel sorgente
assert not [i for i in range(1, 39) if '[' in eng[i] or ']' in eng[i]]
assert not [i for i in range(1, 39) if eng[i].count('"') % 2]
# <bunks> distinto da <tons>: entrambi presenti, in unita' diverse
assert TAGS.findall(P1[4]).count('<bunks>') == 1 and TAGS.findall(P2[21]).count('<bunks>') == 1
assert '<tons>' in P2[31] and '<bunks>' in P2[31]

os.makedirs(OUT, exist_ok=True)
for name, d in (('part01.json', P1), ('part02.json', P2)):
    with open(os.path.join(OUT, name), 'w', encoding='utf-8') as f:
        json.dump({str(k): v for k, v in sorted(d.items())}, f, ensure_ascii=False, indent=1)
print('scritte %d unita (19 + 19)' % len(ALL))
