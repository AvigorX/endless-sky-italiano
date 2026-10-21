"""mkparts.py — L121: secondo segmento di `data/human/campaign events.txt` (56 unita', righe 282-1332).

Forma: **41 `DESCRIPTION`**, **14 `MISSION_TEXT`**, **1 `UI_LABEL`**, **12 contesti**, **28 unita' con tab**, **46
virgolette** di dialogo, **1 token** (`<origin>`), **zero quadre**.

- **La `UI_LABEL` (unita' 20, `new stock`) resta identica al sorgente**: e' un nome di nodo, non prosa.
- **52 testi distinti** per 56 unita': quattro coppie ripetono l'inglese (`(Move on.)`, il primo paragrafo di Zug,
  quello di Poseidon Industries, l'apertura di Greenrock) e la resa ripete.
"""
import collections
import json
import os
import re
import sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
PARTS = os.path.join(HERE, 'parts')
SRC = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units']
ENG = {u['idx']: u['english'] for u in SRC}
KIND = {u['idx']: u['kind'] for u in SRC}
TAGS = re.compile(r'<[^<>]+>')

UNIQ = [
    ("volcanic moon",
     "Ingot è una luna vulcanica, del tutto inadatta alla vita ma ricca di metalli. I minatori che lavorano qui "
     "devono passare tutto il loro tempo dentro edifici pressurizzati."),
    ("meteorites are a constant danger",
     "Poiché Ingot non ha quasi atmosfera che freni i meteoriti, questi sono un pericolo costante per i coloni. I "
     "gusci degli edifici hanno più strati, progettati per autoripararsi in caso di impatto, tranne che nei casi "
     "più grandi. La maggior parte dell'estrazione è fatta a distanza da veicoli robotici, ma serve comunque "
     "qualcuno sul posto per controllarli e per riparare quando qualcosa va storto."),
    ("burgeoning Navy base",
     "Ingot ora ospita anche una base della Marina in piena espansione, anche se, dato che il pianeta è così "
     "invivibile, la maggior parte delle truppe vive semplicemente nelle navi in orbita."),
    ("extract and refine rare earth",
     "New Wales ospita alcuni avamposti minerari che estraggono e raffinano terre rare e metalli pesanti. È un "
     "lavoro pericoloso: le miniere sono in profondità e soggette a gas tossici e crolli, e le raffinerie lavorano "
     "con materiali radioattivi fusi e sostanze chimiche caustiche."),
    ("dim light of the star Algorel",
     "A causa della luce piuttosto debole della stella Algorel e della nuvolosità dell'atmosfera, non è un buon "
     "mondo per l'agricoltura, e la popolazione resta piuttosto ridotta."),
    ("planted a base on New Wales",
     "La Marina della Repubblica ha impiantato una base su New Wales. Per ora è solo un grappolo fitto di caserme "
     "prefabbricate ed edifici per l'infermeria alla periferia di una delle colonie minerarie."),
    ("rugged mountain world",
     "New Austria è un mondo montuoso e aspro, pieno di cime innevate e di valli così profonde e ripide che "
     "raramente vedono la luce del sole."),
    ("mining sapphires and rubies",
     "I pochi insediamenti costruiti qui sono nati per l'estrazione di zaffiri e rubini. Gli zaffiri vanno dal blu "
     "al giallo, al nero e al trasparente, e servono come abrasivi industriali e per gioielleria."),
    ("folklore revolves",
     "Per secoli gli abitanti hanno cercato un giacimento di diamanti, e il folclore locale ruota attorno alla "
     "prosperità che verrebbe a questo mondo se i diamanti venissero trovati."),
    ("requisitioned one of the abandoned mining towns",
     "La Marina ha da poco requisito una delle città minerarie abbandonate e ha iniziato a ristrutturarla come base "
     "militare sicura, usando i tunnel delle miniere come bunker sotterranei profondi."),
    ("raft of new outfits for sale",
     "Quando entri nell'emporio di <origin>, noti che ha in vendita una gran quantità di nuovi equipaggiamenti: "
     "sistemi di raffreddamento, postbruciatori, persino nuovi generatori. Stranamente, quasi tutta la nuova merce "
     "sembra venire da Kraz Cybernetics e Delta V, aziende che di solito si vedono vendere lungo il Bordo "
     "Meridionale, non così a nord vicino al centro della Repubblica. È tanto più strano perché quelle aziende sono "
     "state sostenitrici dichiarate dei secessionisti dei Mondi Liberi."),
    ("(Ask the proprietor",
     "(Chiedi al proprietario dei nuovi equipaggiamenti.)"),
    ("(Move on.)",
     "(Vai avanti.)"),
    ("busy at his desk",
     "Il proprietario è indaffarato alla scrivania nel piccolo ufficio dell'emporio, ma quando ti avvicini si alza "
     "e ti saluta. \"Ciao, come posso aiutarti oggi?\""),
    ("How come you're selling Kraz",
     "\"Come mai vendi equipaggiamenti Kraz e Delta V quassù?\""),
    ("It looks like you've got new stock",
     "\"Sembra che tu abbia merce nuova.\""),
    ("not the first to ask",
     "\"Non sei il primo a chiedermelo!\" risponde il proprietario con un entusiasmo eccessivo. \"Con la pirateria "
     "in aumento, le tensioni crescenti e - quello che tutti danno per scontato ma nessuno dice - un conflitto "
     "imminente con i secessionisti amanti delle bombe atomiche laggiù nel Bordo Meridionale, abbiamo avuto molte "
     "richieste di tenere in stock equipaggiamenti più... specializzati.\""),
    ("crate of Javelins",
     "Ti accompagna davanti a una cassa di Javelin. \"Sai, un bel po' di questa roba arriva dal Sindacato. A quanto "
     "pare avevano già una catena di produzione di questi missili, ma ora che Kraz e Delta V non sono più aziende "
     "che operano nella Repubblica, si sono presi tutti i diritti per produrre i loro articoli!\" Ridacchia. \"È un "
     "vantaggio per i capitani che dipendono dagli equipaggiamenti Delta V ma non possono scendere nel Bordo "
     "Meridionale a rifornire l'attrezzatura.\""),
    ("Nitrogen coolers",
     "\"Sì, sì, ce l'abbiamo!\" Ti viene incontro. \"Raffreddatori ad azoto, razzi pesanti, disturbatori radar per "
     "tenere lontani quei fastidiosi Lovelace Sidewinder, postbruciatori ad alta potenza, roba così. Abbiamo "
     "ricevuto molte richieste di tenere equipaggiamenti del Bordo Meridionale, ora che tutte le tensioni laggiù "
     "rendono difficile fare affari.\""),
    ("leans in towards you",
     "Il proprietario si sporge un po' verso di te e dice a voce più bassa: \"Ma sai, è sbagliato rifornirsi da chi "
     "ha fatto quegli attentati e ha ucciso decine di migliaia di persone. È semplicemente sbagliato. Moralmente e "
     "commercialmente."),
    ("Courtesy of Syndicated Systems",
     "\"Però, per cortesia di Syndicated Systems, puoi trovare attrezzatura del sud qui senza sostenere quei "
     "secessionisti! Hanno visto l'occasione di ottenere i diritti degli equipaggiamenti Delta V e Kraz, e l'hanno "
     "colta. E tu ne trai vantaggio\", ridacchia."),
    ("brochure from his vest jacket",
     "Tira fuori un dépliant dal gilet e te lo porge. \"Se ti interessa qualcosa della nostra nuova merce, ferma uno "
     "dei nostri addetti e la faremo preparare e installare subito sulla tua nave."),
    ("I wish you safe travels",
     "\"Ti auguro buon viaggio\", dice, e torna nel suo ufficio."),
    ("growing by amalgamation",
     "Lo spazioporto di Zug è cresciuto per aggregazione nel corso dei secoli. Al centro c'è il \"Vecchio Porto\", "
     "un insieme di botteghe e magazzini graziosi e rudimentali. Le piazzole del Vecchio Porto sono state divelte "
     "per fare spazio a quello che gli abitanti chiamano \"Il Porto\", un insieme di edifici costruiti un secolo fa, "
     "con un'architettura più audace e un design più moderno."),
    ("expansion to the New Port is currently ongoing",
     "A una certa distanza c'è il \"Porto Nuovo\", una struttura imponente con ascensori robotici per il carico e "
     "grandi hangar per navi più costose. Intanto è in corso un ampliamento del Porto Nuovo. Non puoi fare a meno "
     "di chiederti come si chiamerà il nuovo ampliamento."),
    ("chief ship foundry",
     "A una certa distanza c'è il \"Porto Nuovo\", una struttura imponente con ascensori robotici per il carico e "
     "grandi hangar per navi più costose. Di recente è stato ampliato per gestire l'attività crescente richiesta "
     "dai Mondi Liberi, rendendo Zug la principale fucina di navi del sud galattico. Non sorprende che l'aggiunta "
     "al Porto Nuovo sia stata ribattezzata in fretta \"L'Ampliamento\"."),
    ("swarming with Navy guards",
     "L'avamposto minerario brulica di guardie della Marina; sembra che abbiano trasformato questa luna in una base "
     "operativa temporanea. La miniera è chiusa e a nessuno è permesso entrare o uscire dall'avamposto. Non è "
     "chiaro se i minatori siano prigionieri o semplicemente sotto stretta sorveglianza."),
    ("Poseidon Industries",
     "Lo spazioporto sorge su una grande isola, un vulcano ormai estinto con un'elevazione di diversi chilometri al "
     "centro. La maggior parte della pesca su larga scala è di un'unica azienda, la Poseidon Industries, che ha "
     "anche costruito e mantiene lo spazioporto. Strade ripide e tortuose, case e magazzini in cemento robusto "
     "costeggiano i pendii della montagna, e sotto di te, nel porto, sono ormeggiate diverse enormi navi da pesca a "
     "strascico. Ai margini dello spazioporto ci sono le case fatiscenti e il mercato all'aperto delle famiglie di "
     "pescatori più piccole e indipendenti."),
    ("hundreds of Navy officers",
     "Centinaia di ufficiali della Marina pattugliano questo piccolo spazioporto, in cerca di qualsiasi segno di "
     "resistenza locale."),
    ("mining corporation from Zug",
     "Circa dieci anni fa una società mineraria di Zug ha impiantato una colonia su Clink per raccogliere alcune "
     "terre rare presenti nella crosta di questa luna, grazie al suo tasso insolitamente alto di impatti di "
     "asteroidi. L'atmosfera qui è troppo sottile per respirare senza un respiratore, e a causa della bassa gravità "
     "la polvere sollevata dalle operazioni minerarie resta sospesa perennemente nell'aria."),
    ("tight-knit group",
     "I minatori che lavorano qui sono un gruppo molto unito, perché la maggior parte faceva parte della squadra di "
     "colonizzazione originale. Non sono particolarmente aperti agli estranei, e le strutture qui sono così "
     "rudimentali che non tengono nemmeno carburante per le navi in visita."),
    ("rocky desert planet",
     "Farpoint, all'estremità settentrionale dello spazio umano, è un pianeta desertico e roccioso che ospita una "
     "base della Marina della Repubblica e poco altro. L'agricoltura è possibile solo nelle serre, e questo sistema "
     "è troppo lontano dal centro galattico per essere appetibile per il commercio o l'industria."),
    ("Navy Oathkeepers",
     "Ultimamente la base della Marina su Farpoint è cresciuta. È diventata la nuova sede degli Oathkeepers della "
     "Marina, una piccola branca che ha giurato di restare fuori dal conflitto con i Mondi Liberi."),
    ("dense clouds in Winter",
     "Le nubi dense nell'atmosfera di Winter bloccano gran parte della luce solare, creando un paesaggio gelido. Il "
     "pianeta non fu colonizzato prima di un secolo fa, quando un gruppo di investitori di Pherkad decise di "
     "costruirvi un centro manifatturiero, invece di cercare altra terra sul già sovraffollato pianeta Solace. "
     "Sostenendo che le emissioni industriali di anidride carbonica e altri gas serra avrebbero finito per "
     "riscaldare il pianeta e trasformarlo in un paradiso tropicale, riuscirono ad attirare abbastanza coloni da "
     "tenere in funzione le fabbriche."),
    ("Free Worlds Conservatory",
     "Winter ospita il Conservatorio dei Mondi Liberi, una nuova università dedicata a rendere disponibili a un "
     "prezzo ragionevole tecnologia e competenze di terraformazione, oltre che alla protezione e al ripristino "
     "ecologico."),
    ("mountainous world with a population",
     "Thule è un mondo montuoso con una popolazione di quasi un miliardo, colonizzato nei primi giorni "
     "dell'esplorazione spaziale. Quando la colonia fu fondata, il governo sulla Terra non aveva ancora la forza di "
     "controllare altri sistemi oltre al proprio. Per questo Thule rifiutò di unirsi alla Repubblica quando fu "
     "formata, e da allora ha respinto ogni tentativo di costringerla."),
    ("den of pirate activity",
     "Fino a poco tempo fa Thule era un noto covo di pirateria, ma le principali autorità tribali hanno ora "
     "rinunciato alla pirateria per impedire che i Mondi Liberi si intromettessero ulteriormente nei loro affari. "
     "È però probabile che ogni sorta di attività illegale continui in segreto qui."),
    ("Smuggler's Den",
     "Smuggler's Den era un tempo la stazione Grendel, quando era una raffineria in funzione. Poi fu presa dai "
     "pirati e divenne un rifugio per contrabbandieri e corsari di ogni genere. Ora, almeno in teoria, è una "
     "stazione indipendente non più alleata con i pirati. In pratica, sospetti che una buona dose di pirateria "
     "continui comunque qui."),
    ("repair shops here can make",
     "Le officine di riparazione qui possono fare diverse modifiche legali e illegali alla tua nave, e nel cantiere "
     "puoi comprare astronavi ricondizionate... se non ti turba la coscienza pensare al probabile destino dei loro "
     "precedenti proprietari."),
    ("anarchists smell worse",
     "È un fatto strano ma indiscutibile che gli anarchici puzzino più degli esseri umani comuni. Oggi, quando "
     "anche il più economico degli shuttle ha almeno una doccia sonica, non c'è spiegazione logica, se non che le "
     "tendenze anarchiche debbano andare di pari passo con la tendenza a rifiutare le norme sociali sull'igiene. "
     "Qui, in una stazione spaziale, con nient'altro che aria riciclata da respirare, l'effetto è opprimente."),
    ("at least until the Free Worlds occupied it",
     "Greenrock era la cosa più vicina a un centro di governo che i pirati dello spazio umano meridionale "
     "avessero, almeno finché i Mondi Liberi non l'hanno occupata. Quando bande rivali di pirati cercavano di "
     "negoziare su territorio neutrale, si incontravano qui. Quasi tutto era in vendita: armi illegali, navi "
     "personalizzate per la pirateria e persino schiavi."),
    ("marginally more respectable",
     "Ora che i Mondi Liberi occupano il sistema, Greenrock è diventata un mondo marginalmente più rispettabile. I "
     "pirati scorrazzano ancora nelle zone selvagge del pianeta, ma i Mondi Liberi arrestano attivamente criminali "
     "e liberano schiavi nei centri abitati."),
    ("normally shady establishments",
     "Hai sentito abbastanza sulla reputazione di questo porto da non sorprenderti nel vedere i resti dei mercati "
     "di schiavi, ora vuoti per effetto dell'occupazione dei Mondi Liberi. Le attività normalmente losche sono ora "
     "piene di miliziani e di qualche capitano mercantile che vuole esplorare il pianeta finché è ancora in mano ai "
     "Mondi Liberi."),
    ("abandoned shop called",
     "Nonostante la presenza dei Mondi Liberi, i vicoli bui vanno ancora evitati. In fondo a un vicolo vedi una "
     "bottega abbandonata chiamata \"Mike's Mustelids\", ormai invasa da donnole, furetti e ghiottoni che un tempo "
     "erano in gabbia lì."),
    ("cleaned up many of the major population centers",
     "Questo fino a quando i Mondi Liberi occuparono il sistema e ripulirono molti dei principali centri abitati. "
     "Ora che i Mondi Liberi se ne sono andati, il pianeta ha iniziato a tornare al suo stato naturale di crimine e "
     "malvagità."),
    ("spaceport's shady establishments",
     "Hai sentito abbastanza sulla reputazione di questo porto da non sorprenderti nel vedere i resti dei mercati "
     "di schiavi, ora vuoti per effetto dell'occupazione dei Mondi Liberi. Le attività losche dello spazioporto "
     "stanno iniziando a tornare alla loro clientela e ai loro servizi abituali."),
    ("absolutely to be avoided",
     "Ora che i Mondi Liberi se ne sono andati, i vicoli bui vanno evitati del tutto. In fondo a un vicolo vedi una "
     "bottega chiamata \"Mike's Mustelids\", all'interno simile a una giungla. Senti gli ululati e le grida di vari "
     "animali esotici che vengono da dentro, e il vicolo ospita un certo numero di donnole, furetti e ghiottoni "
     "presumibilmente fuggiti che corrono qua e là."),
    ("large, powerful corporations",
     "Greenrock è la cosa più vicina a un centro di governo che i pirati dello spazio umano meridionale abbiano, ma "
     "sotto forma di grandi e potenti società, non di funzionari eletti. Quando bande rivali di pirati cercano di "
     "negoziare su territorio neutrale, si incontrano qui. Quasi tutto è in vendita: armi illegali, navi "
     "personalizzate per la pirateria e persino schiavi."),
    ("for a short while long ago",
     "I Mondi Liberi occuparono questo pianeta per un breve periodo molto tempo fa, tentando di ripulire il centro "
     "criminale, ma quasi ogni traccia della loro influenza sul pianeta è ormai svanita da tempo."),
    ("heavily guarded in case",
     "Hai sentito abbastanza sulla reputazione di questo porto da non sorprenderti nel vedere i mercati di "
     "schiavi, pesantemente sorvegliati nel caso qualche visitatore si trovi in possesso di una coscienza. Né ti "
     "scandalizzano le attività losche che servono ogni sorta di interesse pruriginoso. Dopotutto questo è un "
     "porto pirata, e qui tutto è in vendita."),
    ("completely fenced off",
     "Tutto, in effetti, anche le cose più bizzarre. Trovi un vicolo buio completamente recintato rispetto al resto "
     "dello spazioporto, con gli ululati di animali che arrivano da dietro la barriera. Accanto al vicolo vedi "
     "l'insegna di una bottega chiamata \"Mike's Mustelids\", che promette la vendita di \"animali esotici dalla "
     "giungla dello spazioporto di Greenrock\"."),
]

db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ST = {u['idx']: db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] for u in SRC}
assert set(ST.values()) == {'PENDING'}, {k: v for k, v in ST.items() if v != 'PENDING'}

assert collections.Counter(u['kind'] for u in SRC) == {'DESCRIPTION': 41, 'MISSION_TEXT': 14, 'UI_LABEL': 1}
assert sum(1 for u in SRC if u['english'].startswith('\t')) == 28
assert sum(u['english'].count('"') for u in SRC) == 46
ctx = collections.Counter(u['context'] for u in SRC)
assert len(ctx) == 12 and collections.Counter(ctx.values()) == {15: 1, 10: 1, 5: 1, 4: 3, 3: 2, 2: 4}, ctx
assert collections.Counter(t for u in SRC for t in TAGS.findall(u['english'])) == {'<origin>': 1}

distinct = list(dict.fromkeys(ENG.values()))
assert len(distinct) == 52, len(distinct)
LABEL = [u['idx'] for u in SRC if u['kind'] == 'UI_LABEL']
assert len(LABEL) == 1 and ENG[LABEL[0]] == 'new stock'
prose = [e for e in distinct if e != 'new stock']
assert len(prose) == 51 and len(UNIQ) == 51, (len(prose), len(UNIQ))


def resolve(eng):
    hits = [t for s, t in UNIQ if s in eng]
    assert len(hits) == 1, (len(hits), eng[:90], hits)
    return hits[0]


cover = {e: resolve(e) for e in prose}
assert len(set(cover.values())) == 51, 'due testi distinti con la stessa resa'

T = {}
for u in SRC:
    eng = u['english']
    if u['kind'] == 'UI_LABEL':
        T[u['idx']] = eng
        continue
    T[u['idx']] = '\t' * (len(eng) - len(eng.lstrip('\t'))) + cover[eng]

for idx, txt in T.items():
    eng, kind = ENG[idx], KIND[idx]
    assert txt.count('\t') == eng.count('\t'), idx
    assert txt.count('"') == eng.count('"'), (idx, eng.count('"'), txt.count('"'))
    assert TAGS.findall(txt) == TAGS.findall(eng), (idx, TAGS.findall(txt), TAGS.findall(eng))
    assert not re.search(r'[\[\]`\u2019\u2014\u2013\u2026]', txt), idx
    assert not re.search(r"\b(e|piu|perche|cosi|gia|puo|cioe|percio|fa)'", txt), idx
    if kind == 'UI_LABEL':
        assert txt == eng, idx
    else:
        assert txt.strip() and txt.strip() != eng.strip(), idx
    r = len(txt) / len(eng)
    assert 0.55 < r < 1.90, ('gate', idx, round(r, 3), eng[:60])

for n, (lo, hi) in enumerate(((1, 19), (20, 38), (39, 56))):
    d = {str(k): T[k] for k in range(lo, hi + 1)}
    with open(os.path.join(PARTS, 'part%02d.json' % (n + 1)), 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
print('56 unita (19+19+18) · 52 testi distinti (4 coppie) · 1 UI_LABEL identica · 28 tab · 46 virgolette · 1 token')
