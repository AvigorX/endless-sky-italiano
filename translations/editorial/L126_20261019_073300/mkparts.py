"""mkparts.py — L126: apre `data/incipias/incipias first contact.txt` (55 unita', righe 22-218).

Primo lotto del file: **48 `MISSION_TEXT`**, **4 `UI_LABEL`**, **3 `LOGBOOK`**, **6 contesti**, **37 unita' con
tab**, **65 virgolette**, **zero token**, **52 testi distinti** (tre coppie ripetute).

- **Le 4 `UI_LABEL`** (`ut divitas`, `spec inci`, `both planets`, `new species`) restano **identiche al sorgente**:
  sono testi di nodo, non prosa, e il `check.py` le isola.
- **Due registri**: il Guardiano parla in modo **alto e arcaico** ("Ignoring these words is only but folly", "Here
  lie the unborn flowers"), i Quarg in modo **cerimoniale** ("Your lengthy wanderings have brought forth you here",
  "do not perambulate"). Le rese li distinguono.
- **Unita' 23 con tre virgolette**: il sorgente lascia una virgoletta di chiusura in piu' dopo il punto; la resa la
  riproduce (2 nel testo, 1 finale).
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
    ("dead end, traveler",
     "Una voce comincia a parlare da qualche parte. \"La tua via ti conduce a un vicolo cieco, viaggiatore. Oltre non "
     "c'è nulla per te.\""),
    ("Alarmed, you look around",
     "Allarmato, ti guardi attorno ma non c'è nessuno. Controlli gli scanner ma in questo sistema non c'è altro che "
     "qualche forma di vita indigena. Eppure il tuo sistema di navigazione mostra rotte iperspaziali che portano "
     "oltre."),
    ("(Ignore it.)",
     "(Ignorala.)"),
    ("This doesn't appear to be a dead end",
     "\"Questo non sembra un vicolo cieco.\""),
    ("Why should I listen to you",
     "\"E perché dovrei ascoltarti?\""),
    ("Ignoring these words",
     "\"Ignorare queste parole è pura follia. Torna indietro, viaggiatore.\" La voce riecheggia nell'aria, ancora "
     "senza indicare da dove venga."),
    ("You can't fool me",
     "\"Non puoi ingannarmi. Questo non è un vicolo cieco.\""),
    ("Here lie the unborn flowers",
     "\"Qui giacciono i fiori non ancora nati, che devono ancora schiudersi del tutto. Non c'è nulla qui che tu possa "
     "trovare. Ascolta questo avvertimento e torna indietro.\" La voce suona più energica questa volta, e ti sembra "
     "che venga da dentro la tua testa."),
    ("Unborn flowers. That sounds interesting",
     "\"Fiori non nati. Sembra interessante.\""),
    ("I will see for myself",
     "\"Lo vedrò di persona.\""),
    ("Thank you for the warning",
     "\"Grazie dell'avvertimento.\""),
    ("deep sigh seems to drift",
     "Un sospiro profondo sembra scorrere nel continuum. \"Umano, questi fiori non nati sarebbero solo messi in "
     "pericolo dalla tua presenza.\" Un'impressione di euforia ti pervade mentre senti di nuovo le parole 'fiori non "
     "nati'."),
    ("Please respect the beauty of life",
     "\"Rispetta la bellezza della vita e non entrare in questa regione che presto ne darà un'altra. La tua specie è "
     "molto più avanzata di qualsiasi cosa tu possa sperare di trovare qui. Nessun tesoro ti attende qui.\""),
    ("Why do you care about these",
     "\"Perché ti importa di questi 'fiori'?\""),
    ("What I search for is not technology",
     "\"Ciò che cerco non è tecnologia.\""),
    ("Your persistence on this topic",
     "La voce assume ora un tono calmo. \"La tua insistenza su questo punto è ammirevole, ma permettimi di spiegare "
     "la mia convinzione con un esempio.\""),
    ("not disturb the \"unborn flowers\" that inhabit the region.",
     "Entrato in una regione di spazio a nord-est degli Hai e avvertito da una voce incorporea di non disturbare i "
     "\"fiori non nati\" che abitano la regione."),
    ("Why do humans care about art",
     "\"Perché agli umani importa dell'arte?\" La voce ora sembra lontana ma più presente che mai. \"Perché vi "
     "stupisce, come a noi stupisce vedere un'altra specie crescere e superare i propri fardelli. Le vite degli "
     "altri sono come un quadro che non smette mai di essere dipinto, ma è cosa tragica vedere il quadro fermarsi. "
     "Ecco perché cerchiamo di proteggere queste creazioni della vita: per vedere a quali altezze arrivano.\""),
    ("I see that you can not be convinced",
     "C'è una pausa. \"Vedo che non posso convincerti. Potrei intervenire nel tuo viaggio, ma non amo gli scontri "
     "spiacevoli.\" La voce ora è risoluta. \"Ti lascerò passare, ma ti osserverò, perché sono il guardiano di "
     "questo spazio.\""),
    ("The voice fades out leaving nothing behind",
     "La voce svanisce, non lasciando nulla dietro di sé se non la sensazione di essere osservato."),
    ("Agreed to stay away from there",
     "Entrato in una regione di spazio a nord-est degli Hai e avvertito da una voce incorporea di non disturbare i "
     "\"fiori non nati\" che abitano la regione. Accettato di starne lontano."),
    ("You are understanding, human",
     "\"Sei comprensivo, umano, perciò ti ringrazio a nome degli Incipias.\" La voce svanisce, lasciando solo la "
     "sensazione di essere osservato.\""),
    ("presence from the previous system somehow lingers",
     "La presenza del sistema precedente in qualche modo persiste, mentre continui a sentire di essere osservato."),
    ("I do not take kindly to your deception",
     "Entrando nel sistema, la stessa voce di prima riecheggia nella tua mente, anche se questa volta sembra avere un "
     "peso grave dietro. \"Non apprezzo il tuo inganno, umano. Sappi che sarai osservato.\" La voce svanisce, ma "
     "resta la forte presenza di qualcosa."),
    ("Maybe you can find some more information in nearby systems",
     "Entrando nel sistema, noti navi di un tipo che non hai mai visto. Chiamarle dà solo fruscio. Dopo altri "
     "tentativi senza successo, rinunci. Forse puoi trovare altre informazioni nei sistemi vicini."),
    ("This must be the species the Quarg talked about",
     "Entrando nel sistema, noti navi di un tipo che non hai mai visto. Chiamarle dà solo fruscio. Dopo altri "
     "tentativi senza successo, rinunci. Dev'essere la specie di cui parlavano i Quarg."),
    ("lands with a soft jolt",
     "La tua nave atterra con un piccolo sobbalzo mentre un gruppetto di Quarg si raduna rapidamente attorno, facendo "
     "gesti semplici ma chiari per dirti di aspettare. Dopo essersi resi conto che hai capito, uno di loro si "
     "allontana in fretta. Aspetti parecchio tempo finché non arriva un altro Quarg, presumibilmente uno che parla la "
     "tua lingua. Comincia a parlare con un accento che non riesci a collocare."),
    ("wait for a decent amount of time for a group of three Quarg",
     "Dopo aver fatto atterrare la nave sulla luna, devi aspettare un bel po' perché compaia un gruppo di tre Quarg. "
     "Quello al centro ti fa cenno di avvicinarti, e cominciano a parlare con un accento che non riesci a "
     "collocare."),
    ("Welcome, human. Your lengthy wanderings",
     "\"Benvenuto, umano. I tuoi lunghi vagabondaggi ti hanno condotto fin qui, eppure la tua specie non ha mai messo "
     "piede in questa regione delle stelle. Possiamo chiederti quale sia la tua missione?\""),
    ("I am just exploring the galaxy",
     "\"Sto solo esplorando la galassia.\""),
    ("I am looking for new species",
     "\"Cerco nuove specie.\""),
    ("obvious pursuit for the young",
     "\"È una ricerca ovvia per i giovani\", annuisce. \"Se posso consigliarti, non peregrinare per questo quarto di "
     "spazio con leggerezza. La galassia porta con sé molte situazioni pericolose che la tua specie deve ancora "
     "scoprire o persino comprendere.\" Si raddrizza in tutta la sua altezza, torreggiando su di te."),
    ("What a peculiar task that is",
     "\"Che compito singolare.\" Sembra confuso e inclina la testa. \"Che cosa speri di ottenere? Una quantità "
     "incommensurabile di pericoli accompagna l'incontro e il trattare con altre specie: non lo avevi previsto? I "
     "confini dello spazio non sono oziosi incidenti. Ti consiglio di essere scrupoloso e di ponderare ogni singolo "
     "passo.\""),
    ("almost-hidden frustration",
     "Dopo una breve pausa, noti una frustrazione quasi nascosta in fondo al volto del Quarg, prima che riprenda a "
     "parlare. \"Sei autorizzato a continuare qui i tuoi vagabondaggi nomadi, ma noi Quarg abbiamo delle richieste. "
     "A un intervallo minimo da questa luna la specie vicina ha iniziato il suo viaggio verso le stelle. Non "
     "interromperlo per il tuo, o per il loro bene.\""),
    ("free to use the local facilities",
     "Con queste parole i Quarg si voltano e se ne vanno. Sembra che ora tu sia libero di usare le strutture "
     "locali."),
    ("lone alien spaceship",
     "Entrando nel sistema, noti una nave spaziale aliena solitaria, fuori uso e gravemente danneggiata. A parte lei, "
     "non sembra esserci nessun'altra nave nel sistema, né segno di aiuti. Forse c'è un modo per assistere la nave e "
     "il suo equipaggio."),
    ("Assisted a stranded alien vessel",
     "Aiutata una nave aliena bloccata in un sistema disabitato, il cui equipaggio assomigliava a polpi o meduse "
     "fluttuanti. Impossibile comunicare per la barriera linguistica, ma si è riusciti a dare loro l'equipaggiamento "
     "necessario a riparare la nave. Purtroppo erano privi di iperguida e quindi incapaci di tornare al loro sistema "
     "d'origine."),
    ("hail request",
     "Mentre ti avvicini alla nave relitto, ti invia una richiesta di collegamento. Una volta accettata, gradienti di "
     "colore iniziano improvvisamente a muoversi sul tuo schermo in modo vertiginoso, ma curiosamente non c'è audio. "
     "È chiaro che, senza una sorta di dispositivo di traduzione, non potrai capire qualunque trasmissione tu abbia "
     "appena visto. Continui il tuo tentativo di assistere la nave, preparandoti a portare a bordo alcune provviste "
     "di riparazione."),
    ("hatch opens and as a hallway",
     "Riesci ad attraccare alla nave fuori uso con una certa facilità. Il portello si apre e, mentre davanti a te si "
     "apre un corridoio, è subito evidente che questa nave non è stata progettata per gli umani. Le pareti sono "
     "stranamente curve, e il pavimento non offre quasi alcun appiglio. Mentre porti l'attrezzatura di riparazione "
     "dentro la nave, il tuo sguardo è catturato da cinque alieni giganteschi, in parte polpi e in parte meduse. "
     "Pulsano di colori vivaci, simili ai gradienti apparsi prima sul tuo schermo. Uno di loro fluttua dietro quello "
     "che è chiaramente un'enorme arma montata, e le due canne sono puntate dritte su di te. L'artigliere alieno "
     "lampeggia di luce arancione, e senti la tensione nella stanza salire."),
    ("convey that I intend no harm",
     "(Cerca di comunicare che non ho cattive intenzioni.)"),
    ("Drop the repair equipment and run back",
     "(Lascia cadere l'attrezzatura di riparazione e corri di nuovo sulla mia nave.)"),
    ("Try to shoot at the one behind the turret",
     "(Prova a sparare a quello dietro la torretta e corri.)"),
    ("causing it to explode with a strident sound",
     "Colpisci la creatura che manovra la torretta, facendola esplodere con un suono stridente. Prima che tu possa "
     "goderti la tua breve vittoria, noti un movimento più in fondo al corridoio. Voltando la testa vedi un artigliere "
     "che lampeggia di rosso cupo, prima che ti abbatta vendicando il compagno caduto."),
    ("slowly place the crate",
     "Sentendo che la situazione potrebbe degenerare da un momento all'altro, appoggi lentamente la cassa con "
     "l'attrezzatura di riparazione a terra e fai qualche passo indietro. Stai attento a non fare movimenti bruschi. "
     "Tu e gli alieni restate immobili per un momento, finché uno di loro fluttua lentamente in avanti. Tonalità di "
     "giallo si mescolano ora all'arancione della creatura, e due dei loro tentacoli si avvolgono attorno alla cassa "
     "mentre gli altri quattro si ritirano. Quando l'alieno riesce ad aprire la cassa e a guardare dentro, i suoi "
     "colori passano a un verde debole. Anche il resto dell'equipaggio sembra rilassarsi, assumendo lo stesso "
     "colore."),
    ("pulsating in all colors of the spectrum",
     "Con gli alieni che recuperano l'attrezzatura di riparazione, non c'è altro che tu possa fare, data la barriera "
     "linguistica. Proprio mentre te ne vai, vedi gli alieni iniziare a pulsare di tutti i colori dello spettro; i "
     "gradienti scorrono sulla loro pelle così veloci che sembrano quasi bianchi."),
    ("smashing the button that closes the lock",
     "Lasci cadere l'attrezzatura di riparazione e corri di nuovo sulla tua nave, premendo con forza il pulsante che "
     "chiude il portello. Hai un ultimo sguardo a uno degli alieni: tonalità blu e gialle si mescolano sulla sua "
     "pelle, ma non reagiscono."),
    ("engines of the ship slowly booting back up",
     "Mentre voli via vedi i motori della nave riaccendersi lentamente. A quanto pare hanno capito come usare "
     "l'attrezzatura di riparazione. Invece di lasciare il sistema, però, la nave comincia a volare verso un gigante "
     "gassoso vicino."),
    ("scanner log that is still open on your monitor",
     "Di nuovo sulla tua nave, i tuoi occhi cadono sul registro degli scanner ancora aperto sul monitor. Da notare "
     "che questa nave non aveva iperguida né nulla di simile installato, il che è strano considerando che in questo "
     "sistema non c'è alcun pianeta abitato. Forse dovresti parlare con i Quarg e vedere se sanno qualcosa."),
]

db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ST = {u['idx']: db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] for u in SRC}
assert set(ST.values()) == {'PENDING'}, {k: v for k, v in ST.items() if v != 'PENDING'}

assert collections.Counter(u['kind'] for u in SRC) == {'MISSION_TEXT': 48, 'UI_LABEL': 4, 'LOGBOOK': 3}
assert sum(1 for u in SRC if u['english'].startswith('\t')) == 37
assert sum(u['english'].count('"') for u in SRC) == 65
ctx = collections.Counter(u['context'] for u in SRC)
assert len(ctx) == 6 and collections.Counter(ctx.values()) == {23: 1, 13: 2, 2: 3}, ctx
assert collections.Counter(t for u in SRC for t in TAGS.findall(u['english'])) == {}   # zero token

LAB = [u['idx'] for u in SRC if u['kind'] == 'UI_LABEL']
assert LAB == [30, 32, 34, 39], LAB
assert [ENG[i] for i in LAB] == ['ut divitas', 'spec inci', 'both planets', 'new species']

distinct = list(dict.fromkeys(ENG.values()))
assert len(distinct) == 52, len(distinct)
names = {ENG[i] for i in LAB}
prose = [e for e in distinct if e not in names]
assert len(prose) == 48 and len(UNIQ) == 48, (len(prose), len(UNIQ))


# due voci di diario: la seconda ripete la prima e aggiunge una frase, quindi le firme si sovrappongono.
# Si risolvono per testo esatto, dichiarandolo, invece di allungare la firma a forza.
EXACT = {
    "Entered a region of space northeast of the Hai and was warned by a disembodied voice to not disturb the "
    "\"unborn flowers\" that inhabit the region.":
        "Entrato in una regione di spazio a nord-est degli Hai e avvertito da una voce incorporea di non disturbare i "
        "\"fiori non nati\" che abitano la regione.",
    "Entered a region of space northeast of the Hai and was warned by a disembodied voice to not disturb the "
    "\"unborn flowers\" that inhabit the region. Agreed to stay away from there.":
        "Entrato in una regione di spazio a nord-est degli Hai e avvertito da una voce incorporea di non disturbare i "
        "\"fiori non nati\" che abitano la regione. Accettato di starne lontano.",
}


def resolve(eng):
    if eng in EXACT:
        return EXACT[eng]
    hits = [t for s, t in UNIQ if s in eng]
    assert len(hits) == 1, (len(hits), eng[:90], hits)
    return hits[0]


cover = {e: resolve(e) for e in prose}
assert len(set(cover.values())) == 48, 'due testi distinti con la stessa resa'

T = {}
for u in SRC:
    eng = u['english']
    if u['kind'] == 'UI_LABEL':
        T[u['idx']] = eng
    else:
        T[u['idx']] = '\t' * (len(eng) - len(eng.lstrip('\t'))) + cover[eng]

for idx, txt in T.items():
    eng, kind = ENG[idx], KIND[idx]
    assert txt.count('\t') == eng.count('\t'), idx
    assert txt.count('"') == eng.count('"'), (idx, eng.count('"'), txt.count('"'))
    assert TAGS.findall(txt) == TAGS.findall(eng) == [], idx
    assert not re.search(r'[\[\]`\u2019\u2014\u2013\u2026]', txt), idx
    assert not re.search(r"\b(e|piu|perche|cosi|gia|puo|cioe|percio|fa)'", txt), idx
    if kind == 'UI_LABEL':
        assert txt == eng, idx
    else:
        assert txt.strip() and txt.strip() != eng.strip(), idx
    r = len(txt) / len(eng)
    assert 0.55 < r < 1.90, ('gate', idx, round(r, 3), eng[:60])

for n, (lo, hi) in enumerate(((1, 19), (20, 38), (39, 55))):
    d = {str(k): T[k] for k in range(lo, hi + 1)}
    with open(os.path.join(PARTS, 'part%02d.json' % (n + 1)), 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
print('55 unita (19+19+17) · 52 testi distinti · 4 UI_LABEL identiche · 37 tab · 65 virgolette · 0 token')
