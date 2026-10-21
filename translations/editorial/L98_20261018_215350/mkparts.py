"""mkparts.py — L98: costruisce `parts/part01-02.json` (39 unita', righe 1-105).

Primo lotto di `hai culture conversations.txt`. Tre contesti: `Theater Chat` (unita' 1-8),
`Musical Entertainment Expo` (9-24), `The Meme Wars 1` (25-39).

**1 token**: `<destination>` (unita' 7). **3 coppie di quadre** nell'unita' 30: e' la voce del dispositivo
di traduzione che elenca alternative (`[Vittoria, Successo]`) — le quadre si riproducono, non si tolgono.
**3 ripetizioni**: 20/37 (`"How strange."`), 27/31 e 29/39; le unita' 28 e 32 **differiscono per una virgola**
(`meme items and no one` contro `meme items, and no one`): riprodotta.
"""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'parts')

STRANGE = '''"Che strano."'''
WANDER = '''Ringraziate la guardia per il consiglio e proseguite con quello che stavate facendo mentre l'incomprensibile conflitto continua intorno a voi.'''
CONGA = '''Poco più avanti incontrate due diversi gruppi di manifestanti, ammesso che siano questo, che si intrecciano dentro e fuori dagli ingressi dello spazioporto come in una specie di conga. L'anziano triangolare e l'ortaggio a radice avversario ricompaiono più volte sui loro cartelli, alcuni animati in ologramma.'''

P1 = {
 1: '''Mentre attraversate lo spazioporto, vi imbattete nell'insolita coppia di un Hai e un umano, la cui conversazione spicca perché parlano la lingua comune dell'umanità.''',
 2: '''"Oh, oh, Gemanari, questo sembra interessante!" La donna umana dimostra una sessantina d'anni avanzata e, quando vi voltate a guardare, sembra intenerirsi davanti a un annuncio olografico di uno spettacolo teatrale. "È adorabile, non trovi? Oh, e dice che usano effetti di volo olografici a rifrazione con raggi ondulati!"''',
 3: '''L'annuncio in effetti è molto impressionante, e vi fermate a osservarlo per un momento.''',
 4: '''L'Hai, presumibilmente Gemanari, sembra anche lei una signora di una certa età: socchiude gli occhi e arriccia il naso. "Ugh, però è l'interpretazione germontiana."''',
 5: '''La cosa suscita uno sguardo perplesso, e Gemanari riflette un secondo prima di chiarire. "Vorreste dire l'interpretazione darwinista sociale."''',
 6: '''La signora fa una smorfia e simula di vomitare. "Non posso credere che abbiate ancora queste correnti di pensiero, in una società così antica."''',
 7: '''"Oh, in realtà no, almeno non nei circoli scientifici, ma una storia avvincente sopravvive a queste cose. Personalmente non la sopporto, ma è un classico." Siccome la signora non sembra impressionata, Gemanari ridacchia e la prende delicatamente per un braccio per portarla via. "Non preoccuparti, Alinta; credo che la compagnia Misheep Wah'uden stia mettendo in scena la mia interpretazione preferita su <destination>, in questo momento. Possiamo vedere se hanno biglietti a buon mercato. Certo, mia zia insisterebbe che la centottantatreesima versione è l'unica vera, ma lei..."''',
 8: '''Perdete la conversazione mentre si allontanano, e restate a chiedervi cosa avesse di così speciale la centottantatreesima versione di un'opera su un Hai preistorico alato trovato congelato nel ghiaccio.''',
 9: '''Mentre siete fermi nello spazioporto in attesa del rifornimento, vi sorprende quanto sia difficile trovare un posto dove sedervi a mangiare e bere. Gli Hai si sono stipati in ogni bar o locale simile dotato di uno schermo pubblico, sfoggiando fasce, mantelli e ogni sorta di altro accessorio che, per quanto riuscite a capire, somiglia a... merchandising di squadre sportive?''',
 10: '''Non siete esperti di come si presentino queste cose nella società Hai, e così, quando alla fine trovate un posto dove sedervi, in un bar per mancanza di alternative, chiedete al cameriere dall'aria stanca che cosa stia esattamente succedendo.''',
 11: '''"Ah, questo? Sono tutti qui per le dirette della Musical Entertainment Expo. Purtroppo nessuno di loro inizia a bere prima che almeno una delle loro squadre abbia annunciato qualcosa che valga la pena," dice, roteando gli occhi con esasperazione.''',
 12: '''"Ok. Posso solo avere qualcosa da mangiare?"''',
 13: '''"Che cos'è la Musical Entertainment Expo?"''',
 14: '''"Perché non hanno ancora iniziato a bere?"''',
 15: '''"Beh, vede, le grandi etichette discografiche fanno molta ricerca di talenti tutto l'anno. Hanno reparti dedicati esclusivamente a trovare e mettere insieme nuovi gruppi destinati a diventare il prossimo fenomeno. È tradizione festeggiare solo dopo essersi impegnati nel viaggio con una nuova band. Ogni tre anni l'industria organizza ME2, quello che sta vedendo lassù, per presentare il nuovo giro di band e per stuzzicare eventuali uscite di metà stagione che hanno in cantiere."''',
 16: '''"La vostra musica esce da una catena di montaggio?"''',
 17: '''"Non avete musicisti che cercano di sfondare da soli?"''',
 18: '''"Oh, certo, ma soprattutto per farsi prendere da una di queste aziende."''',
 19: '''Il cameriere ridacchia. "Facciamo pop music da più tempo di quanto la vostra gente abbia conosciuto il fuoco. Si tratta dell'esperienza di essere fan di un gruppo mentre sale alla fama e al successo. Un Hai appassionato può andare a cercare una canzone per quasi ogni possibile esperienza di vita, in quasi ogni possibile genere. È il viaggio, e le personalità, quel che conta."''',
 20: STRANGE,
}

P2 = {
 21: '''"Che interessante."''',
 22: '''"Comunque, mi pareva voleste qualcosa da mangiare?"''',
 23: '''Il cameriere accenna un cenno verso di voi e prende l'ordine. "Nessun problema, arriva subito."''',
 24: '''È un pasto rumoroso.''',
 25: '''Entrando nello spazioporto, venite investiti da un tripudio di colori. Ogni superficie vuota che di solito non è spazio pubblicitario a pagamento sembra addobbata con proiettori olografici pendenti, striscioni e nastri. Ci sono persino volantini e manifesti veri, di carta, apparentemente attaccati con nastro adesivo a qualunque superficie li regga. All'inizio vi chiedete se ci sia una specie di festa, ma poi vedete un giovane Hai incappucciato che appiccica un altro proiettore olografico, creando un ortaggio a radice in stile cartone animato con una spada, che comincia a fare a pezzi l'ologramma accanto, una specie di concetto impressionista di un anziano Hai fatto di triangoli iridescenti. Il giovane Hai poi strappa giù uno striscione e spalma una specie di poltiglia su un manifesto enorme, che inizia a sciogliersi mentre due guardie di sicurezza, con aggiunte molto evidentemente non regolamentari alle uniformi, lo inseguono fuori dallo spazioporto.''',
 26: '''Mentre guardate, l'anziano triangolare proiettato in ologramma sembra tremolare e poi si spegne mentre la batteria si esaurisce, apparentemente sotto l'assalto dell'ortaggio a radice, che accenna una danza di vittoria e poi mette in scena qualcosa che per voi non ha assolutamente senso.''',
 27: CONGA,
 28: '''Un'altra guardia di sicurezza, questa in uniforme regolare, vi compare al gomito. "Sembra un po' perso. Non si preoccupi, è solo una guerra di meme. Faccia i suoi affari e non tocchi gli oggetti dei meme e nessuno dovrebbe darle fastidio per questo."''',
 29: WANDER,
 30: '''Mentre guardate, l'anziano triangolare proiettato in ologramma sembra tremolare e poi si spegne mentre la batteria si esaurisce, apparentemente sotto l'assalto dell'ortaggio a radice, che accenna una danza di vittoria. Con vostra sorpresa, il vostro traduttore si fa sentire: "[Vittoria, Successo] per la radice vera e quadrata, che è più [significativa, importante] del [sistema, tradizione] tripartito degli anziani!"''',
 31: CONGA,
 32: '''Un'altra guardia di sicurezza, questa in uniforme regolare, vi compare al gomito. "Sembra un po' perso. Non si preoccupi, è solo una guerra di meme. Faccia i suoi affari e non tocchi gli oggetti dei meme, e nessuno dovrebbe darle fastidio per questo."''',
 33: '''"Certo, lo farò."''',
 34: '''"I vostri anziani hanno un sistema tripartito?"''',
 35: '''La guardia ridacchia e dice: "Oh, lei capisce? In realtà no, ma è una vecchia battuta di una campagna politica ormai passata, secondo cui gli anziani tengono solo a tre principi, e sono tutti quelli che ci toccano meno."''',
 36: '''Quando chiedete cosa abbia scatenato tutto questo, dice: "Oh, le ultime priorità educative sono uscite con un'impostazione su quattro principi, lo stesso giorno in cui un anziano ha citato per sbaglio la vecchia campagna. È stato molto divertente."''',
 37: STRANGE,
 38: '''"Sembra divertente."''',
 39: WANDER,
}

src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units']
eng = {u['idx']: u['english'] for u in src}
TAGS = re.compile(r'<[^<>]+>')
for idx, txt in list(P1.items()) + list(P2.items()):
    assert not txt.startswith('\t'), idx
    assert txt.count('\t') == 0, idx
    assert txt.count('"') == eng[idx].count('"'), (idx, txt.count('"'), eng[idx].count('"'))
    assert TAGS.findall(txt) == TAGS.findall(eng[idx]), (idx, TAGS.findall(eng[idx]), TAGS.findall(txt))
    # le quadre sono la voce del dispositivo di traduzione: parita' esatta, non rimozione
    assert txt.count('[') == eng[idx].count('[') and txt.count(']') == eng[idx].count(']'), idx
    assert txt.strip(), idx
assert sorted(P1) == list(range(1, 21)), sorted(P1)
assert sorted(P2) == list(range(21, 40)), sorted(P2)
assert P1[20] == P2[37] == STRANGE
assert P2[27] == P2[31] == CONGA
assert P2[29] == P2[39] == WANDER
# 28 e 32 differiscono per la virgola prima di "e nessuno"
assert P2[32].count(',') == P2[28].count(',') + 1
assert 'meme e nessuno' in P2[28] and 'meme, e nessuno' in P2[32]
assert eng[30].count('[') == 3 and P2[30].count('[') == 3

os.makedirs(OUT, exist_ok=True)
for name, d in (('part01.json', P1), ('part02.json', P2)):
    with open(os.path.join(OUT, name), 'w', encoding='utf-8') as f:
        json.dump({str(k): v for k, v in sorted(d.items())}, f, ensure_ascii=False, indent=1)
print('scritte %d unita (20 + 19)' % (len(P1) + len(P2)))
