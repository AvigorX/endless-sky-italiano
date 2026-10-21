"""mkparts.py — L130: `data/human/boarding missions.txt` (75 unita', righe 417-686).

Secondo lotto del file: **4 contesti** (`boarding pirate`, `Pirate Ambush`, `Pirate Mutiny`, `Slave Crew
Rescue`), **50 `MISSION_TEXT`**, **22 `UI_LABEL`**, **1 `CONVERSATION`**, **1 `DESCRIPTION`**, **1 `DIALOG`**.
**Nessun `VALUE`** in questa finestra: la cella va scritta come asserzione vuota (`0 = 0`).

- **Le 22 `UI_LABEL`** sono **nomi di nodo** (`boarding alone`, `flagship is empty`, `has brig`, …): restano
  identiche al sorgente, sono elencate una per una e verificate a parte.
- **45 unita' con tab**: quasi tutti i `MISSION_TEXT` di `Slave Crew Rescue` sono battute o opzioni indentate.
- **Tarquin** parla in modo affettato e si tradisce con la voce: la resa tiene il registro (`spilorcio`, `zotici`,
  `che se ne sia andato al diavolo`).
- **Due unita' identiche** (35 e 59): stessa resa, garantita dal confronto «stesso inglese ⇒ stessa resa».
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

TAIL = ("Anche se non ti aspetti alcun pericolo, ti senti comunque apprensivo, tutto solo su un vascello sconosciuto "
        "e in avaria, così ti assicuri di portare un'arma da fianco. L'apprensione cresce quando ti rendi conto di non "
        "sentire alcun suono di attività frenetica né di vedere membri dell'equipaggio correre qua e là a riparare i "
        "danni come ti aspetteresti. Mentre raggiungi il ponte di comando, ti rilassi vedendo un solo giovane "
        "elegante e ben vestito che salda una paratia. I suoi movimenti sono agili e competenti, ma il tuo occhio "
        "esperto ti dice che la paratia è danneggiata oltre ogni riparazione, quindi il suo lavoro è inutile. Alza lo "
        "sguardo e si presenta come capitano Tarquin, offrendoti la principesca somma di 350.000 crediti per il tuo "
        "aiuto esperto nel riparare il suo vascello.")
CAUTIOUS = ("Mentre il tuo gruppo d'abbordaggio si arrampica a bordo della <origin>, ti rendi conto di non sentire "
            "alcun suono di attività frenetica né di vedere membri dell'equipaggio correre qua e là a riparare i danni "
            "come ti aspetteresti. Mentre raggiungi il ponte di comando, ti accoglie un solo giovane elegante e ben "
            "vestito che salda una paratia. I suoi movimenti sono agili e competenti, ma il tuo occhio esperto ti "
            "dice che la paratia è danneggiata oltre ogni riparazione, quindi il suo lavoro è inutile. Alza lo "
            "sguardo e si presenta come capitano Tarquin, offrendoti la principesca somma di 350.000 crediti per il "
            "tuo aiuto esperto nel riparare il suo vascello.")
RELIEVED = "Ti senti sollevato che tutta la faccenda sia finita quando sei al sicuro di nuovo a bordo della tua nave."
BRIG_OPEN = ("Gli alloggi dell'equipaggio della nave sono stati trasformati in una cella con porte robuste. Per "
             "fortuna il dispositivo di sblocco le apre tutte, e quasi una dozzina di disgraziati denutriti esce "
             "barcollando, raccontandoti tutta la storia: il capitano Tarquin li teneva come schiavi da diversi mesi, "
             "chiudendoli nei loro alloggi quando la nave attraccava e senza cibo come punizione quando si "
             "lamentavano. ")

D = {
    1: "Fai una scansione a corto raggio delle dotazioni e del carico della <origin>. Tra il carico trovi una cassa "
       "piena di gettoni di credito per un valore di <payment>. Trascini la cassa sulla tua nave prima di pensare "
       "alla prossima mossa.",
    2: "Sali a bordo della <origin>, ma non trovi nessun membro dell'equipaggio. Quando raggiungi la cabina di "
       "pilotaggio, guardi nello spazio e vedi una capsula di salvataggio che si allontana fluttuando. La <origin> "
       "sta emettendo un segnale di soccorso verso i pirati vicini, e una sequenza di autodistruzione è stata "
       "attivata! Corri di nuovo sulla tua nave e ti prepari a combattere.",
    3: "Porta <bunks> membri dell'equipaggio, ex pirati, su <destination>.",
    4: "Quando sali a bordo della <origin>, trovi la maggior parte dell'equipaggio già morta. Uno dei superstiti, che "
       "sembra un ragazzo non più grande di sedici anni, ti si avvicina con le mani in aria. Spiega che dopo che la "
       "nave è stata messa fuori uso, una parte dell'equipaggio ha deciso di rovesciare il capitano tiranno. "
       "Continua dicendo che la maggior parte dei pirati viene costretta in servitù sulle navi pirata. I <bunks> "
       "superstiti ti supplicano di portarli su <destination> perché possano fuggire dalla schiavitù dei pirati.",
    5: "La battaglia sembra aver danneggiato la nave oltre ogni riparazione. Se lasci qui i pirati, potrebbe non "
       "durare molto più a lungo nel vuoto dello spazio.",
    6: "(Aiuta l'equipaggio pirata.)",
    7: "(Lascia l'equipaggio pirata.)",
    8: "I membri dell'equipaggio pirata ti ringraziano per averli portati su <planet>. Uno di loro ti consegna un "
       "piccolo pagamento di <payment>. Auguri a tutti loro di fare fortuna nella nuova vita, e vi separate.",
    11: "Lasci la tua nave vuota e sali da solo sulla <origin>. " + TAIL,
    13: "Lasci il tuo primo ufficiale al comando della tua nave e sali da solo sulla <origin>. " + TAIL,
    15: CAUTIOUS,
    17: "(Accetta questo generoso pagamento e aiuta a riparare la nave.)",
    18: "\"Non vorrei guardare in bocca al cavallo donato, ma perché offri così tanti soldi per il mio aiuto?\"",
    19: "\"Possiamo avere un po' di aiuto dal tuo equipaggio?\"",
    20: "\"Una nave di queste dimensioni non dovrebbe avere più equipaggio?\"",
    21: "Tarquin ride con un po' d'imbarazzo. \"La verità è che sono un po' disperato\", dice. \"La mia stiva è piena "
        "di merci deperibili che devono essere consegnate entro tre giorni a un cliente molto importante, che "
        "probabilmente mi taglierà fuori se non rispetto la scadenza. Ho pensato di risparmiare assumendo contadini "
        "inesperti come equipaggio, ma come vedi non ha funzionato granché bene. Sono rintanati nei loro alloggi "
        "anche adesso. Ti sto offrendo i miei profitti da spilorcio. Chiamiamolo pagare per una lezione imparata.",
    23: "Tarquin ride di gusto. \"Quella gente? Sono un branco di semplici contadini che ho raccolto su New India, "
        "nascosti nei loro alloggi in questo momento. Gli zotici non sono abituati a questo genere di pericolo e non "
        "hanno grandi capacità tecniche. Colpa mia, che sono stato troppo tirchio per assumere gente valida, "
        "suppongo. Dopo che saremo usciti da questo pasticcio, prenderò di sicuro qualche membro dell'equipaggio più "
        "esperto e affidabile.\"",
    25: "\"Possiamo metterci al lavoro adesso?\"",
    26: "(Mettiti al lavoro e ripara la nave.)",
    27: "(Insisti sulla questione.)",
    28: "Qualcosa nella spiegazione del capitano Tarquin non ti convince, così continui a fargli domande per "
        "distrarlo mentre ti avvicini con discrezione alla sezione alloggi dell'equipaggio. Man mano che ti avvicini "
        "cominci a sentire i deboli suoni di persone che battono sui muri e gridano aiuto. Il volto di Tarquin "
        "mostra un'espressione quasi inquietantemente neutra, ma il suo corpo è teso, come se ogni muscolo si fosse "
        "contratto in una volta sola.",
    29: "\"Credo che abbiamo sbagliato strada. Andiamo a riparare la tua nave.\"",
    30: "\"Ora vedo che tipo di nave gestisci, ma non preoccuparti, sei tra amici. Le riparazioni sono gratis.\"",
    31: "\"Ti aiuterò, ma il prezzo è appena salito a un milione di crediti, oppure ti lascio qui e dico alle "
        "autorità che gestisci una nave negriera.\"",
    32: "\"Pretendo che tu liberi i tuoi schiavi.\"",
    33: "(Attaccalo subito.)",
    34: "\"Sì, facciamolo\", risponde Tarquin. Però la sua aria amichevole è sparita, e resta teso come un cavo "
        "d'acciaio. Lavorate in un silenzio di pietra e ritiri goffamente il tuo pagamento quando la <origin> torna "
        "a funzionare.",
    35: RELIEVED,
    37: "Tarquin si rilassa. \"È così bello incontrare un capitano che la pensa come me in questa galassia "
        "ostile\", dice. \"Non mi sognerei mai di accettare riparazioni gratis. Prendi comunque i soldi, insisto.\"",
    38: "(Ora vai a riparare la sua nave.)",
    39: "(Approfitta dell'apertura e attaccalo.)",
    43: "Estrai l'arma il più in fretta che puoi.",
    46: "Tarquin non può sperare di reggere da solo contro tutto il tuo gruppo d'abbordaggio e si arrende in fretta. "
        "Uno sguardo di furia fredda gli brilla negli occhi, mentre il resto del volto resta calmo.",
    47: "(Giustizialo qui e ora.)",
    48: "(Prendilo prigioniero.)",
    49: "Ordini a uno dei membri del tuo gruppo d'abbordaggio di legarlo e sorvegliarlo. Tarquin ti copre di insulti "
        "e si dimena mentre lo perquisisci, trovando una pistola e un coltello nascosti, e il gettone di credito con "
        "cui stava per pagarti. Vai a liberare l'equipaggio della nave.",
    50: "Gli alloggi dell'equipaggio sono stati trasformati in una cella con porte robuste. Non c'è un modo evidente "
        "di aprirle, così tu e i tuoi compagni cominciate a farle saltare.",
    51: "All'improvviso un clacson d'allarme squarcia il rumore con uno staccato aspro. La sequenza di "
        "autodistruzione della nave è stata attivata! Corri nella stanza dove era tenuto Tarquin e scopri che è in "
        "qualche modo fuggito. Al suo posto c'è un membro del tuo equipaggio privo di sensi, con uno squarcio feroce "
        "sul volto, evidentemente inferto da un'altra arma nascosta che non sei riuscito a trovare. Un pannello "
        "vicino indica che una capsula di salvataggio è stata espulsa.",
    52: "La nave esploderà in meno di 30 secondi. Capisci con amarezza che non hai alcuna possibilità di liberare i "
        "prigionieri in tempo, e che provarci comunque farebbe morire tutti. Tu e il tuo gruppo d'abbordaggio "
        "tornate furiosi sulla nave e sganciate i morsetti d'attracco appena in tempo perché la <origin> si "
        "disintegri in una nuvola di detriti spaziali, ponendo crudelmente fine alle vite già infelici delle vittime "
        "del capitano Tarquin.",
    53: "Giuri che sarà l'ultima volta che sottovaluti il capitano Tarquin, se le vostre strade dovessero "
        "incrociarsi di nuovo.",
    55: "Perquisisci Tarquin e trovi una pistola e diversi coltelli nascosti, il gettone di credito con cui stava per "
        "pagarti e un piccolo dispositivo di sblocco. Poi ordini a uno dei membri del tuo gruppo d'abbordaggio di "
        "chiuderlo nella cella della tua nave. Tarquin ti copre di insulti mentre viene portato in prigionia sotto la "
        "minaccia delle armi. Decidi di pensare più tardi a cosa farne e vai a liberare l'equipaggio della nave.",
    56: "Abbatti il capitano Tarquin a sangue freddo, con shock di almeno un membro del tuo gruppo d'abbordaggio. Che "
        "se ne sia andato al diavolo, pensi, mentre perquisisci il corpo dell'ex capitano Tarquin. Trovi una pistola "
        "e diversi coltelli nascosti, il gettone di credito con cui stava per pagarti e un piccolo dispositivo di "
        "sblocco. Vai a liberare il suo equipaggio con quello.",
    58: "Tarquin osserva il tuo gruppo d'abbordaggio e ti fissa gelido per almeno cinque secondi imbarazzanti prima "
        "di rispondere. \"Va bene\", dice freddo, gli occhi che ardono di una rabbia a stento contenuta, mentre il "
        "resto del volto resta calmo. Resta teso come un cavo d'acciaio mentre tu e la tua squadra riparate la nave "
        "in un silenzio di pietra, ritirando goffamente il pagamento quando la <origin> torna a funzionare.",
    59: RELIEVED,
    61: "\"Ci vorrà un giorno freddo all'inferno prima che mi lasci ricattare da qualcuno abbastanza stupido da "
        "salire da solo su una nave in avaria\", sogghigna Tarquin.",
    64: "Il capitano Tarquin getta la testa all'indietro e ride nell'esatto momento in cui estrae una pistola "
        "nascosta e ti spara cinque volte, tutto in un batter d'occhio. I tuoi ultimi pensieri riguardano "
        "l'efficacia della sua distrazione e la stupidità della tua spavalderia.",
    66: "Veloce come un lampo, estrae una pistola nascosta e ti trafigge la spina dorsale prima che tu possa "
        "reagire. Il gioco pericoloso a cui stavi giocando finisce di colpo.",
    68: "Veloce come un lampo, estrae una pistola nascosta, ma tu sei più rapido. È l'ultimo errore che fa. "
        "Perquisisci il corpo dell'ex capitano Tarquin e trovi diversi coltelli nascosti oltre alla pistola, il "
        "gettone di credito con cui stava per pagarti e un piccolo dispositivo di sblocco. Vai a liberare "
        "l'equipaggio con quello.",
    70: BRIG_OPEN + "Sono molto contenti di vedere il suo corpo senza vita disteso sul pavimento della nave.",
    71: "Consegni la <origin> a loro e torni alla tua nave.",
    73: BRIG_OPEN + "Sono molto contenti di sapere che è stato preso in prigionia.",
    74: "Consegni la <origin> a loro e torni alla tua nave per decidere cosa fare di Tarquin.",
    75: "Un rapido controllo dei dati pubblici nel database galattico della giustizia penale non rivela che sia "
        "ricercato per alcun crimine. Decidi di consegnarlo alle autorità di polizia sul pianeta più vicino.",
}

db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ST = {u['idx']: db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] for u in SRC}
assert set(ST.values()) == {'PENDING'}, {k: v for k, v in ST.items() if v != 'PENDING'}

assert collections.Counter(u['kind'] for u in SRC) == {'MISSION_TEXT': 50, 'UI_LABEL': 22, 'CONVERSATION': 1,
                                                       'DESCRIPTION': 1, 'DIALOG': 1}
assert sum(1 for u in SRC if u['english'].startswith('\t')) == 45
assert sum(u['english'].count('"') for u in SRC) == 31
ctx = collections.OrderedDict()
for u in SRC:
    ctx[u['context']] = ctx.get(u['context'], 0) + 1
assert len(ctx) == 4 and list(ctx.values()) == [1, 1, 6, 67], list(ctx.items())
assert collections.Counter(t for u in SRC for t in TAGS.findall(u['english'])) == {
    '<origin>': 12, '<payment>': 2, '<bunks>': 2, '<destination>': 2, '<planet>': 1}
assert not [u['idx'] for u in SRC if u['kind'] == 'VALUE'], 'VALUE assente: la cella va scritta come asserzione vuota'

LAB = [u['idx'] for u in SRC if u['kind'] == 'UI_LABEL']
assert LAB == [9, 10, 12, 14, 16, 22, 24, 36, 40, 41, 42, 44, 45, 54, 57, 60, 62, 63, 65, 67, 69, 72], LAB

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
    if idx in LAB:
        assert txt == eng, idx
    else:
        assert txt.strip() and txt.strip() != eng.strip(), idx
    r = len(txt) / len(eng)
    assert 0.55 < r < 1.90, ('gate', idx, round(r, 3), eng[:60])

dup = {}
for u in SRC:
    dup.setdefault(KEY[u['idx']], set()).add(T[u['idx']])
assert not [(k, v) for k, v in dup.items() if len(v) > 1], [(k[:50], v) for k, v in dup.items() if len(v) > 1]

for n, (lo, hi) in enumerate(((1, 25), (26, 50), (51, 75))):
    d = {str(k): T[k] for k in range(lo, hi + 1)}
    with open(os.path.join(PARTS, 'part%02d.json' % (n + 1)), 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
print('75 unita (25x3) · 53 testi tradotti + 22 UI_LABEL identiche · 4 contesti · 0 VALUE')
print('45 tab · 31 virgolette · 19 token in 5 famiglie · %d testi distinti' % len(dup))
