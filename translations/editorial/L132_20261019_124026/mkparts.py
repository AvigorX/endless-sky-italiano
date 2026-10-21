"""mkparts.py — L132: `data/hai/unfettered side missions.txt` (84 unita', righe 17-229).

Primo lotto del file, due contesti: **`Unfettered returning home`** (18 unita', il giovane Hai che diserta) e **`Hai
Legacy 1`** (66 unita', le due figure incappucciate e l'Anomalocaris).

Forma: **89 virgolette** su 84 unita' (piu' di una per unita': il valore piu' alto trattato finora), **74 unita' con
tab**, **8 token** in **4 famiglie** (`<last>` 4, `<destination>` 2, `<first>` 1, `<payment>` 1), **3 `UI_LABEL`**
(nomi di nodo) e **zero `VALUE`** (asserzione vuota scritta).

Due scelte dichiarate:
- **`Hai-home` resta nome proprio** («Hai-home»), perche' e' il nome del mondo, non una descrizione;
- **l'unita' 4** (`(No.)`) ha per resa `(No.)`: identica per necessita', dichiarata (`ID_OK`), altrimenti il controllo
  «tutte tradotte» la boccia.
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
KEY = {i: e.lstrip('\t') for i, e in ENG.items()}
TAGS = re.compile(r'<[^<>]+>')

D = {
    1: "Questo Hai ti ha chiesto di farlo uscire di nascosto dallo spazio degli Unfettered e di portarlo su "
       "<destination>.",
    2: "Durante la notte senti un leggero rumore di graffi sul portello principale della tua nave. Vai a controllare?",
    3: "(Sì.)",
    4: "(No.)",                      # identica per necessità: dichiarata in ID_OK
    5: "Prendi una torcia e apri il portello, e trovi un giovane Hai con una grande sacca a tracolla. \"Sei tu il "
       "<first> <last>, vero?\", dice. Fai cenno di sì. Dice: \"È vero quello che c'è scritto qui?\"",
    6: "Nelle mani tiene un pezzo di carta stagnola. Riconosci l'involucro di una delle razioni alimentari che hai "
       "trasportato agli Unfettered, il \"tributo\" che pretendono dagli Hai pacifici. Ma non avendo mai aperto una di "
       "quelle razioni, non avevi notato che all'interno c'è una scritta, poche parole nell'alfabeto spigoloso degli "
       "Hai. Il giovane Unfettered vede il tuo sguardo confuso e traduce il messaggio. \"Dice: 'Hai-home è casa tua. "
       "Torna al tuo popolo.'\"",
    7: "\"Credo che sia vero. Gli Hai che hanno dato questo tributo hanno detto che speravano che gli Unfettered "
       "rinunciassero alla violenza e si riconciliassero con loro.\"",
    8: "\"Mi dispiace, ma non credo che ti lasceranno mai vivere tra loro, se è nella tua natura essere incline alla "
       "violenza.\"",
    9: "Hai poca esperienza nel leggere le emozioni degli Hai, ma il giovane sembra abbattuto. \"Ne sei certo?\", "
       "chiede.",
    10: "\"Ne sono certo. Non posso fare nulla per te.\"",
    11: "\"Forse puoi venire con me e scoprirlo, ma non farti troppe illusioni.\"",
    12: "\"Mi porterai su Hai-home?\", chiede. \"Tu puoi stare fuori dai luoghi degli Unfettered. Posso venire con "
        "te?\"",
    13: "\"Sì, ti ci porto.\"",
    14: "\"Mi dispiace, non posso rischiare di far arrabbiare gli Unfettered trasportando un disertore.\"",
    15: "Deluso, il giovane se ne va. Speri di aver fatto la scelta giusta.",
    16: "Accompagni il giovane in una delle tue cabine e gli dici di restare nascosto finché non raggiungi Hai-home.",
    17: "Cerchi il giovane Hai, ma ti accorgi che è salito su una delle tue scorte! Meglio partire e aspettare che le "
        "tue scorte arrivino in questo sistema stellare.",
    18: "Non dovevi preoccuparti dell'accoglienza che il giovane Unfettered avrebbe ricevuto qui su Hai-home. Pochi "
        "minuti dopo che hai contattato con esitazione il governo degli Hai, una folla felice si è radunata attorno "
        "alla tua nave. Quando esce dal portello, sembra sbalordito di essere accolto con tanto calore. Uno dei "
        "governatori degli Hai ti ringrazia per averlo trasportato e ti paga <payment>.",
    19: "Ricordi una figura incappucciata che ti ha offerto un'opportunità d'affari in questo cantiere. Vuoi seguire "
        "le sue indicazioni e dirigerti verso le coordinate indicate?",
    20: "(Certo.)",
    21: "(Forse un'altra volta.)",
    22: "(Mai.)",
    23: "Mentre giri per il cantiere, vieni avvicinato con discrezione da una figura incappucciata. Quando ti fermi "
        "per sentire cosa ha da dire, ti afferra il braccio e tira per farti seguire. \"Continua a camminare\", "
        "sibila lo sconosciuto. Dopo aver indicato e commentato navi a caso, come per imitare i gesti di un normale "
        "passante, ti si rivolge di nuovo.",
    24: "\"I miei associati e io abbiamo una lucrosa proposta d'affari per te. Richiederà tutta la tua attenzione, "
        "quindi faresti bene a chiudere prima gli affari in corso. Se sei interessato, vieni a trovarci a queste "
        "coordinate.\"",
    25: "Proprio prima di andarsene aggiungono: \"Notiamo che gestisci più navi. Tuttavia, questa è una faccenda "
        "solitaria; assicurati di poter parcheggiare quasi tutte le tue navi.\"",
    26: "Senza aspettare una risposta, ti piegano un pezzo di carta in mano e svaniscono in fretta tra la folla. C'è "
        "scritto solo un luogo, e se lo confronti con le mappe locali sembra indicare una spiaggia dall'altra parte "
        "del pianeta.",
    27: "Però la carta dice anche che devi avere almeno dieci milioni di crediti in contanti! Dovrai metterli da parte "
        "o chiedere un prestito e tornare un altro giorno, prima di dirigerti verso il luogo indicato.",
    28: "Ci andrai?",
    29: "(Certo.)",
    30: "(Forse un'altra volta.)",
    31: "Mentre ti chiedi se ci sarà abbastanza spazio per far atterrare la nave sulla spiaggia, noti un biglietto "
        "del treno attaccato sul retro della carta. Altri appunti scritti danno indicazioni precise su come "
        "arrivarci, con in fondo la chiara richiesta di non portare la nave stellare.",
    32: "Con tua sorpresa, la stazione ferroviaria locale è sotterranea. Non riesci a capacitarti della sua enormità: "
        "sembra quasi che da qui si possa raggiungere l'intero pianeta. Chiedi indicazioni a un Hai, imbarazzato "
        "quando scopri che bastava scansionare il biglietto a un terminale vicino e tutte le informazioni utili "
        "sarebbero comparse.",
    33: "Dopo essere uscito dalla stazione, cammini per qualche ora finché non raggiungi la destinazione. All'arrivo "
        "ti guardi attorno in cerca dello sconosciuto. A parte una grotta, una vegetazione rada e, naturalmente, la "
        "spiaggia stessa, non vedi nulla di significativo nei dintorni. Ricontrolli che le coordinate siano giuste e "
        "ti guardi ancora attorno.",
    34: "Aspetti un po' finché non scorgi due figure incappucciate più avanti lungo la spiaggia, e cominci a dubitare "
        "che sia stata una buona idea mentre si avvicinano. Anche quando sono abbastanza vicini per parlare, i loro "
        "volti restano in qualche modo impossibili da scorgere sotto i cappucci. \"Salve, <last>\", dice uno. \"Ci "
        "dispiace per la segretezza, ma la verità è che non possiamo permetterci rischi. È meglio per tutti se non sai "
        "chi siamo, e avevamo bisogno di un luogo isolato per parlarti.\"",
    35: "\"Dimmi di più.\"",
    36: "\"Come mi conosci?\"",
    37: "(Scappa.)",
    38: "Sembrano sorpresi dal tuo improvviso cambio di idea, ma non fanno nulla per fermarti.",
    40: "Senza incidenti, torni alla stazione e compri un biglietto per lo spazioporto.",
    41: "Il secondo sorride. \"Qualsiasi esterno che atterri sul nostro mondo natale deve essere ben noto. Sappiamo "
        "che hai aiutato la nostra gente.\"",
    42: "\"Però non pensare che non siamo al corrente dei tuoi scontri con gli Unfettered\", aggiunge il primo con "
        "tono serio.",
    44: "All'improvviso senti un forte ruggito venire dal mare alle tue spalle, e il terreno comincia a tremare.",
    45: "(Voltati.)",
    46: "Le onde si agitano e il vento ti passa accanto mentre una forma circondata da vapori emerge dall'acqua, come "
        "se un antico mostro marino risalisse dagli abissi.",
    47: "Ma non è un mostro. È una nave, e le sue armi sono puntate dritte su di te!",
    49: "(Corri!)",
    50: "(Aspetta.)",
    51: "(Prova a contattare la mia flotta per chiedere aiuto.)",
    52: "(Sparagli!)",
    53: "Mentre cerchi di reagire, l'Hai più vicino ti afferra saldamente il braccio e grida sopra il rumore. \"Se "
        "questa nave avesse voluto ucciderti, <last>, saresti già morto.\"",
    54: "Riesci a malapena a sentire qualcosa sopra il rumore dei motori, mentre la nave si posa sulla spiaggia. "
        "All'improvviso tutto è calmo. Si voltano verso di te, uno più a suo agio dell'altro. \"Questa nave non ti "
        "vuole alcun male.\"",
    55: "(Non dire nulla.)",
    56: "\"Perché non hai detto nulla prima che succedesse?\"",
    57: "Il secondo risponde: \"Avremmo potuto, ma dov'è il divertimento? Volevamo vedere come avresti reagito.",
    58: "\"Questa nave è la nostra garanzia che nulla vada storto, se tentassi qualcosa contro di noi. Dopo tutto, non "
        "siamo ancora sicuri di poterti dare fiducia.\"",
    59: "I due Hai ti portano poi in una grotta vicina. Cristalli incastonati nelle pareti diffondono un debole "
        "bagliore blu mentre li segui, finché non arrivi a una grande camera dove la luce del sole entra da fessure, "
        "rivelando un'altra nave. Il primo Hai parla di nuovo. \"Quella nave fuori non è in vendita. Questa, però, è "
        "un possente relitto del passato, pensata per la guerra dai tempi in cui il nostro impero controllava le "
        "stelle: un Anomalocaris!\"",
    60: "\"Di cosa si tratta?\"",
    61: "Il secondo ora fa un passo verso di te per parlare, quasi interrompendo il primo. \"Abbiamo una proposta per "
        "te. Se accetti di portare rifornimenti di cui abbiamo molto bisogno ai nostri fratelli, gli Hai Unfettered, "
        "ti venderemo questa nave al modico prezzo di dieci milioni di crediti, comprese due armi appartenenti ai "
        "selvaggi Korath!\" Il primo sembra sorpreso e cerca di intervenire, ma il secondo riprende prima che possano "
        "parlare.",
    62: "\"Queste armi, per le loro dimensioni, colpiscono più forte di qualsiasi cosa nello spazio umano o persino "
        "degli Hai! Non preoccuparti, riuscirai a recuperare il costo di questa nave con facilità aiutandoci. Serve "
        "un carico di forniture mediche su <destination>, e ci mancano il tempo e il personale per portarle noi "
        "stessi con così poco preavviso.",
    63: "\"Certo, la nave è vecchia, e non dovresti aspettarti il miglior prezzo in un cantiere. Tuttavia è un vascello "
        "pregevole, capace di combattere, trasportare merci ed estrarre minerali. Allora, cosa dici, <last>? È "
        "l'occasione della vita; navi come questa non le fanno più.\"",
    64: "\"Vi aiuterò.\"",
    65: "\"Se siete a corto di equipaggio, chi pilotava l'altra nave?\"",
    66: "\"Perché l'altra nave era nascosta sott'acqua?\"",
    67: "\"No, grazie. Non ho intenzione di aggiungere un'altra nave alla mia flotta.\"",
    68: "I due Hai sembrano delusi. \"Peccato. Probabilmente non ci incontreremo più\", dice uno. \"È meglio che tu "
        "dimentichi di averci incontrato qui\", dice l'altro. Fanno cenno alla nave di prima di tornare sott'acqua e "
        "si allontanano lungo la spiaggia.",
    69: "\"Meno sai, meglio è per tutti noi, capitano.\"",
    70: "\"L'abbiamo trovata lì\", risponde il primo.",
    71: "\"È difficile trovare una goccia di pioggia in una tempesta, ma la goccia può vedere tutto mentre cade\", "
        "aggiunge l'altro.",
    72: "Ti danno accesso alla nave e passano a spiegare i dettagli. \"Non ha una vera importanza, ma certo capisci "
        "che non possiamo fare questa vendita per i canali normali. La presenteremo invece come un prestito.\"",
    73: "Capisci in fretta che non ti stanno affatto chiedendo un parere. Anzi, ricevi la notifica del debito prima "
        "ancora che abbiano finito di parlare. \"Dovremo fare alcune modifiche alla nave prima che tu possa usarla.",
    74: "(Torna al cantiere.)",
    75: "\"Perché dovrebbe importare loro una nave diversa?\"",
    76: "\"Dato che questa nave è antica, gli Unfettered cercheranno di preservarla. Lo stesso potrebbe non valere per "
        "altre navi.\"",
    77: "Si allontanano finché non riesci più a sentirli, lasciandoti i codici di accesso della nave perché tu possa "
        "portarla al cantiere. Con l'aiuto del pilota automatico riesci a pilotarla senza complicazioni.",
    78: "Estrai l'arma e cominci a sparare alla nave.",
    79: "Il tuo colpo raggiunge la nave, ma la piccola arma non ha alcuna possibilità contro un'armatura pesante, "
        "anche se un po' consumata. Allora la nave risponde al fuoco, mancandoti di poco e facendo eruttare un geyser "
        "di sabbia che ti costringe a lasciar cadere l'arma. Uno dei due Hai ti si avvicina, apparentemente deluso.",
    80: "\"Sei fortunato a essere ancora vivo, ma anche così non ci servi a nulla se pensi sia saggio usare un'arma da "
        "fuoco contro un'astronave. Addio.\" Si voltano e se ne vanno senza un'altra parola, e la nave decolla.",
    81: "Riesci a mettere a segno un colpo, anche se sembra non fare nulla alla grande navicella davanti a te. Poi "
        "senti una piccola esplosione. Non sei sicuro se i sistemi della nave danneggiata siano ceduti da soli, o se "
        "per un colpo di fortuna il tuo sparo abbia fatto qualcosa.",
    82: "Purtroppo non hai il tempo di riflettere sulle tue azioni, perché la nave esplode di colpo, portandoti con sé "
        "e con tutti gli altri sulla spiaggia.",
    83: "Mancchi il colpo. Né la nave né i due Hai reagiscono. Ti sembra di aver sentito una risatina, ma non sei "
        "sicuro da dove venga.",
    84: "Accettato un accordo alquanto losco per una vecchia nave Hai chiamata Anomalocaris; la transazione non "
        "poteva passare per i canali normali, così è stato emesso un prestito al posto di un acquisto convenzionale. "
        "Sembra essere ancora in uno stato sufficientemente buono per volare.",
}

db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ST = {u['idx']: db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] for u in SRC}
assert set(ST.values()) == {'PENDING'}, {k: v for k, v in ST.items() if v != 'PENDING'}

assert collections.Counter(u['kind'] for u in SRC) == {'MISSION_TEXT': 78, 'UI_LABEL': 3, 'DESCRIPTION': 1,
                                                       'DIALOG': 1, 'LOGBOOK': 1}
assert sum(1 for u in SRC if u['english'].startswith('\t')) == 74
assert sum(u['english'].count('"') for u in SRC) == 89
ctx = collections.OrderedDict()
for u in SRC:
    ctx[u['context']] = ctx.get(u['context'], 0) + 1
assert len(ctx) == 2 and list(ctx.values()) == [18, 66], list(ctx.items())
assert collections.Counter(t for u in SRC for t in TAGS.findall(u['english'])) == {
    '<last>': 4, '<destination>': 2, '<first>': 1, '<payment>': 1}
assert [u['idx'] for u in SRC if u['kind'] == 'VALUE'] == []

LAB = [39, 43, 48]
assert [u['idx'] for u in SRC if u['kind'] == 'UI_LABEL'] == LAB
assert [ENG[i] for i in LAB] == ['train back', 'tell me', 'try again']
ID_OK = [4]                       # "(No.)" -> "(No.)": identica per necessita', dichiarata
assert ENG[4].lstrip('	') == '(No.)'   # l'inglese porta il tab iniziale

expected = [i for i in ENG if i not in LAB]
assert sorted(D) == expected, (len(D), len(expected), [i for i in expected if i not in D],
                               [i for i in D if i not in expected])

T = {}
for u in SRC:
    eng = u['english']
    if u['idx'] in LAB:
        T[u['idx']] = eng
    else:
        T[u['idx']] = '\t' * (len(eng) - len(eng.lstrip('\t'))) + D[u['idx']]

for idx, txt in T.items():
    eng, kind = ENG[idx], KIND[idx]
    assert txt.count('\t') == eng.count('\t'), idx
    assert txt.count('"') == eng.count('"'), (idx, eng.count('"'), txt.count('"'))
    assert TAGS.findall(txt) == TAGS.findall(eng), (idx, TAGS.findall(txt), TAGS.findall(eng))
    assert len(txt) - len(txt.rstrip()) == len(eng) - len(eng.rstrip()), ('spazio finale', idx)
    assert not re.search(r'[\[\]`\u2019\u2014\u2013\u2026]', txt), idx
    assert not re.search(r"\b(e|piu|perche|cosi|gia|puo|cioe|percio|fa)'", txt), idx
    if idx in LAB or idx in ID_OK:
        assert txt == eng, idx
    else:
        assert txt.strip() and txt.strip() != eng.strip(), idx
    r = len(txt) / len(eng)
    assert 0.55 < r < 1.90, ('gate', idx, round(r, 3), eng[:60])

dup = {}
for u in SRC:
    dup.setdefault(KEY[u['idx']], set()).add(T[u['idx']])
assert not [(k, v) for k, v in dup.items() if len(v) > 1], [(k[:50], v) for k, v in dup.items() if len(v) > 1]

for n, (lo, hi) in enumerate(((1, 28), (29, 56), (57, 84))):
    d = {str(k): T[k] for k in range(lo, hi + 1)}
    with open(os.path.join(PARTS, 'part%02d.json' % (n + 1)), 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
print('84 unita (28x3) · %d testi distinti · 3 UI_LABEL + 1 resa identica dichiarata · zero VALUE' % len(dup))
print('74 tab · 89 virgolette · 8 token in 4 famiglie · 2 contesti (18 + 66)')
