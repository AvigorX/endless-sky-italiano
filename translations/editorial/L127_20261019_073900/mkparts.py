"""mkparts.py — L127: tutto il contesto `Help The Stranded 1` di `incipias first contact.txt` (63 unita', 224-331).

Forma: **1 contesto** per 63 unita', **58 `MISSION_TEXT`**, **3 `LOGBOOK`**, **1 `VALUE`**, **1 `DESCRIPTION`**,
**55 unita' con tab**, **98 virgolette**, **2 token** (`<first>`, `<last>`), **63 testi distinti**.

- **Il `VALUE`** (`Seek help from the Incipias`) e' un nome di missione: **identico** al sorgente (decisione 259).
- **I due token** stanno in una sola unita' (38): nome e cognome del capitano, da preservare per unita'.
- **Lo stile degli Incipias** e' fatto di composti con trattino (`intention-goal`, `capital-station`,
  `world-traveler`, `not-danger`, `situation-opportunity`, `air-planet`, `system-places`, `future-time`): la resa
  li riproduce con composti italiani con trattino, ed e' una scelta dichiarata.
- **Il Quarg parla di se' in terza persona** (`this one`): reso con «questo uno», come da glossario.
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
    ("Ask the Incipias for help to save one of their ships",
     "Chiedi aiuto agli Incipias per salvare una delle loro navi."),
    ("Would you like to ask the Quarg for insight",
     "Vuoi chiedere ai Quarg un parere sul tuo strano incontro con la nave aliena bloccata?"),
    ("(Yes.)",
     "(Sì.)"),
    ("(Not right now.)",
     "(Non ora.)"),
    ("you search for a Quarg who speaks your language",
     "Appena arrivi sul pianeta cerchi un Quarg che parli la tua lingua, per raccontargli della nave bloccata che "
     "hai trovato. Uno dei Quarg sembra capire la tua intenzione e ti fa cenno di aspettare. Torna poco dopo "
     "accompagnato dallo stesso Quarg con cui avevi parlato prima."),
    ("What could be such a pressing matter",
     "\"Umano, sembri avere una certa fretta. Quale questione può essere così urgente?\", chiede."),
    ("(Explain the situation.)",
     "(Spiega la situazione.)"),
    ("I need advice regarding the species in this region",
     "\"Ho bisogno di un consiglio sulla specie di questa regione.\""),
    ("held council with the young Incipias",
     "Ti guarda con curiosità. \"Dunque hai tenuto consiglio con i giovani Incipias? Questo uno resta perplesso che tu "
     "abbia saputo stabilire un contatto. Ci è voluto un lungo periodo anche a noi per decifrare il loro modo di "
     "diffondere i messaggi.\""),
    ("seems relieved that you were not able to talk to them",
     "Spieghi in fretta cos'è successo. Da quel che capisci, il Quarg sembra sollevato che tu non sia riuscito a "
     "parlare con loro."),
    ("most peculiar situation",
     "\"Ti sei imbattuto in una situazione assai singolare. Superare i confini del loro sistema non è ancora una "
     "capacità degli Incipias.\" Inclina la testa per un momento, considerando quello che hai appena detto. \"È "
     "nostro desiderio aiutarli, ma è ancora prematuro per noi rivelarci alla loro specie, e certo prematuro che "
     "loro interagiscano con intrusi indipendenti come te. Temo che siamo impotenti di fronte a questo infelice "
     "corso degli eventi.\""),
    ("\"I could help them.\"",
     "\"Potrei aiutarli io.\""),
    ("cold-hearted decision",
     "\"Come puoi prendere una decisione così insensibile?\""),
    ("I'll leave them alone",
     "\"Capisco. Li lascerò in pace.\""),
    ("You lack the tools for such a mission",
     "\"Ti mancano gli strumenti per una simile missione. Per quanto ne sa questo uno, nessun vascello in grado di "
     "atterrare su un gigante gassoso è mai stato sviluppato dalla tua specie. E certo non sei in grado di farti "
     "capire da loro in alcun modo significativo.\" Il Quarg ti fissa per un momento, riflettendo un poco."),
    ("produce you with a single one of our translators",
     "\"Ma per il bene degli Incipias, questo uno ti assisterà su quest'ultimo punto. Se non si può dissuaderti dal "
     "tuo corso d'azione, è meglio che ti sia fornito un mezzo di comunicazione, così che le tue interazioni possano "
     "avvenire su termini amichevoli. Questo uno può procurarti uno solo dei nostri traduttori, che ti permetterà di "
     "esporre le tue intenzioni alla specie. Chiedi che ti vendano una delle loro navi, così da essere in grado di "
     "atterrare sui loro pianeti turbolenti.\""),
    ("forbidden from granting the young species",
     "Fa una pausa prima di assumere un tono più serio. \"Tuttavia, ti è vietato concedere alla giovane specie "
     "qualsiasi tecnologia avanzata che sia tua. Se sei d'accordo con noi su questo punto, ti forniremo un "
     "traduttore.\""),
    ("If that's how I can help them",
     "\"Se è così che posso aiutarli, d'accordo.\""),
    ("Why do you not want me to give them my tech",
     "\"Perché non vuoi che dia loro la mia tecnologia?\""),
    ("Halting the natural increase",
     "\"Fermare il naturale accrescimento di una specie è imprevedibile, nel migliore dei casi. Alla tua specie "
     "manca la saggezza per capirlo, perché siete giovani e non avete visto quello che abbiamo visto noi.\" Il Quarg "
     "tace per un momento, perso nei pensieri. \"I rischi prevedibili anche del solo lasciarti comunicare con loro "
     "sono enormi, e non è qualcosa che tu debba considerare banale.\""),
    ("I will accept your conditions",
     "\"Accetterò le tue condizioni per aiutarli.\""),
    ("The risks do sound concerning",
     "\"I rischi sembrano preoccupanti. Dopo tutto li lascerò in pace.\""),
    ("under the protection of the Quarg. Was given",
     "Scoperto che la specie a nord-est dello spazio degli Hai, gli Incipias, è sotto la protezione dei Quarg. "
     "Ricevuto un traduttore da un Quarg per assistere una nave Incipias bloccata, ma avvertito di non dare agli "
     "Incipias alcuna tecnologia avanzata né di interferire nel loro sviluppo."),
    ("Happy this one is",
     "\"Felice è questo uno che tu accetti quella condizione. Tieni presente, capitano, che il minimo passo falso può "
     "avere conseguenze gravi.\" Il Quarg ti fissa. \"Osserveremo le tue azioni, per verificare che siano pacifiche "
     "e senza intenti malvagi o imprudenti. Resta qui per un momento, ti prego\", dice, e si allontana."),
    ("sleek silver box",
     "Il Quarg torna dopo un attimo, portando ora una scatola d'argento levigata con un display su un lato. \"Questo "
     "è il nostro traduttore, il nostro legame con gli Incipias. È in grado di tradurre la loro lingua inconsueta "
     "nella tua parlata. Sappi dell'onore che questo uno ti fa donandotelo\", dice."),
    ("direct it towards the source",
     "Mentre lo riponi, il Quarg parla ancora. \"Per usare adeguatamente questo dispositivo, devi puntarlo verso la "
     "fonte della comunicazione, così che sia in grado di discernere le emissioni rilevanti. Data la complessità "
     "della loro lingua, il traduttore potrebbe non riuscire a rendere adeguatamente alcuni aspetti del loro parlato "
     "oscuro.\""),
    ("The stars have no place",
     "Poi ti guarda dritto negli occhi. \"Ricorda ciò che ti è stato detto, umano. Le stelle non hanno posto per chi "
     "agirebbe in modo sciocco e sconsiderato verso i propri simili.\" Il Quarg se ne va, lasciandoti solo."),
    ("laborious task for an adolescent species",
     "\"È forse un compito laborioso per una specie adolescente come la tua comprendere i nostri modi, ma dobbiamo "
     "porre la continuazione delle specie al di sopra dell'esistenza dei singoli. Se ci rivelassimo a loro in questo "
     "momento inopportuno, lo shock di una specie così avanzata che appare nel loro spazio alimenterebbe le fiamme "
     "del caos.\""),
    ("Then let me help them",
     "\"Allora lascia che li aiuti.\""),
    ("You can deal with the consequences later",
     "\"Puoi affrontare le conseguenze dopo. Aiutali ora!\""),
    ("sour look",
     "Il Quarg assume un'espressione acida. \"Insisti. Sappi che un nostro intervento è fuori discussione.\" Sospira. "
     "\"Tuttavia, questo uno può prevedere la probabilità che tu prenda una decisione avventata e impetuosa di "
     "contattare ancora questi Incipias.\""),
    ("Let me do the work",
     "\"Certo. Lascia che faccia il lavoro.\""),
    ("If you insist on not helping",
     "\"Se insisti a non aiutarli...\""),
    ("clicks its teeth",
     "Il Quarg batte rapidamente i denti prima di continuare."),
    ("under our watch and care",
     "\"Ti siamo grati per la comprensione, ma ricorda questo: gli Incipias sono sotto la nostra vigilanza e la "
     "nostra cura. Nessuno li danneggerà senza incorrere nella nostra ira.\" Con queste parole il Quarg si volta."),
    ("broadcast your first message",
     "Dopo che sei entrato nel sistema, ti prepari a trasmettere il tuo primo messaggio con il traduttore dei "
     "Quarg."),
    ("here to make contact",
     "\"Salve. Sono il capitano <first> <last>, qui per stabilire un contatto.\""),
    ("Greetings, strangers",
     "\"Vi saluto, stranieri. Cerco di aiutarvi.\""),
    ("I come in peace",
     "\"Vengo in pace.\""),
    ("starts to flash a sequence of lights",
     "Noti che il traduttore inizia a lampeggiare in una sequenza di luci, e lo punti verso il dispositivo di "
     "comunicazione della tua nave. Per un minuto non succede assolutamente nulla."),
    ("wave of movement passes through all ships",
     "Dopo qualche tempo, un'onda di movimento attraversa tutte le navi del sistema, e dalla stazione spaziale si "
     "apre un canale di comunicazione. Colori si riversano sul tuo display: un misto di giallo e verde. Punti il "
     "traduttore verso le luci lampeggianti e speri che riesca a captare qualunque cosa ti stiano dicendo questi "
     "alieni."),
    ("Welcome world-traveler",
     "\"Benvenuto, viaggiatore-di-mondi. Ti salutiamo nel nostro spazio-casa.\" La voce è levigata e sintetica, priva "
     "di qualsiasi emozione discernibile. I colori si fermano prima di riversarsi di nuovo sul tuo schermo. \"Qual è "
     "la tua intenzione-scopo qui?\""),
    ("make peaceful contact",
     "\"Sono qui per stabilire un contatto pacifico con voi.\""),
    ("help one of your stranded ships",
     "\"Voglio aiutare una delle vostre navi bloccate.\""),
    ("dock to the capital-station",
     "Ancora una lunga pausa. \"Le tue intenzioni-scopo sono benvenute. Attracca alla stazione-capitale.\" Insieme "
     "al messaggio arriva una piccola mappa della stazione con i portelli di attracco evidenziati."),
    ("gained access to their ships",
     "Incontrati gli Incipias sulla loro stazione spaziale, e ottenuto l'accesso alle loro navi, capaci di entrare "
     "nel gigante gassoso in cui si è rifugiata la nave Incipias bloccata."),
    ("originated from a gas giant",
     "Gli Incipias sono una specie di alieni che vive a nord-est dello spazio degli Hai. Provengono da un gigante "
     "gassoso e somigliano a grandi polpi fluttuanti. Non avendo ancora sviluppato l'iperguida, sono confinati a un "
     "solo sistema e sono sotto la protezione dei Quarg."),
    ("tubes full of fog",
     "Grazie alla mappa, riesci ad attraccare facilmente alla stazione. Il portello si apre ed entri in un ambiente "
     "come niente che tu abbia mai visto. Non ci sono corridoi come in una stazione spaziale umana: al loro posto, "
     "tubi pieni di nebbia, alcuni dei quali salgono persino in verticale, sembrano l'unico modo per spostarsi. Una "
     "folla di esseri si raduna davanti al tuo portello, ognuno che lampeggia di una moltitudine di colori. Un "
     "gruppo di cinque fluttua davanti alla folla, e finalmente vedi bene le creature. Sono grandi, circa tre metri, "
     "con una sezione bulbosa in cima coperta di strutture simili a scaglie. Vicino alla base del bulbo, tre grandi "
     "occhi sono disposti in un arco poco profondo, sotto i quali ci sono otto tentacoli ondulanti dall'aria abile. "
     "Gli Incipias al centro del gruppo iniziano a pulsare di toni calmi."),
    ("Welcome, outer-being, to our capital",
     "\"Benvenuto, essere-esterno, nella nostra capitale. Siamo gli Incipias.\" Si ferma come aspettando una "
     "risposta. La luce sembra irradiarsi dalle scaglie che lo coprono, ma non riesci a dire se la producano o se "
     "sia semplicemente riflessa."),
    ("I am a human",
     "\"Vi saluto, Incipias. Sono un umano.\""),
    ("I thank you for your hospitality",
     "\"Vi ringrazio per l'ospitalità.\""),
    ("begin to diffuse through the crowd like waves",
     "Il tuo traduttore inizia a lampeggiare rapidamente. Gli Incipias sembrano reagire: movimento e colori "
     "cominciano a diffondersi tra la folla come onde."),
    ("the first outer-being that ever communicated",
     "Il \"portavoce\" continua. \"Sei il primo essere-esterno che abbia mai comunicato con noi. Sei l'unico "
     "essere-esterno là fuori?\""),
    ("No, there are others too",
     "\"No, ci sono anche altri.\""),
    ("The galaxy is full of other beings",
     "\"La galassia è piena di altri esseri.\""),
    ("So there are more",
     "Un'altra onda attraversa la folla. \"Dunque ce ne sono altri. Ma, straniero-lontano, come possiamo aiutarti?\""),
    ("Tell them about the stranded ship",
     "(Racconta della nave bloccata e di come voglio aiutarli.)"),
    ("I want one of your ships",
     "\"Voglio una delle vostre navi.\""),
    ("if that is all that it takes",
     "\"Ti permetteremo di comprarne una, se è tutto ciò che serve a renderti un non-pericolo. Perdonaci. Dobbiamo "
     "parlare di cosa significhi questa situazione-opportunità per la nostra specie. Speriamo di poter interrogare-"
     "oltre voi in un'altra occasione.\""),
    ("overflow in green tones",
     "Un'altra onda attraversa la folla, ma questa volta noti un eccesso di toni verdi."),
    ("So they are still alive",
     "\"Dunque sono ancora vivi. Ti daremo accesso alle nostre navi, così che tu possa entrare nel pianeta-d'aria in "
     "cui si sono rifugiati. Nota però che non possono saltare tra luoghi-sistema, non come la tua nave. Speriamo di "
     "poterti interrogare-oltre in un futuro-tempo.\""),
    ("float away but the crowd continues staring",
     "I cinque fluttuano via, ma la folla continua a fissarti, probabilmente per interesse."),
]

db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ST = {u['idx']: db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] for u in SRC}
assert set(ST.values()) == {'PENDING'}, {k: v for k, v in ST.items() if v != 'PENDING'}

assert collections.Counter(u['kind'] for u in SRC) == {'MISSION_TEXT': 58, 'LOGBOOK': 3,
                                                       'VALUE': 1, 'DESCRIPTION': 1}
assert sum(1 for u in SRC if u['english'].startswith('\t')) == 55
assert sum(u['english'].count('"') for u in SRC) == 98
ctx = collections.Counter(u['context'] for u in SRC)
assert len(ctx) == 1 and list(ctx) == ['mission:Incipias: Help The Stranded 1'], ctx
assert collections.Counter(t for u in SRC for t in TAGS.findall(u['english'])) == {'<first>': 1, '<last>': 1}

VAL = [u['idx'] for u in SRC if u['kind'] == 'VALUE']
assert VAL == [1] and ENG[1] == 'Seek help from the Incipias'
distinct = list(dict.fromkeys(ENG.values()))
assert len(distinct) == 63, len(distinct)
prose = [e for e in distinct if e != ENG[1]]
assert len(prose) == 62 == len(UNIQ), (len(prose), len(UNIQ))


def resolve(eng):
    hits = [t for s, t in UNIQ if s in eng]
    assert len(hits) == 1, (len(hits), eng[:90], hits)
    return hits[0]


cover = {e: resolve(e) for e in prose}
assert len(set(cover.values())) == 62, 'due testi distinti con la stessa resa'

T = {}
for u in SRC:
    eng = u['english']
    if u['kind'] == 'VALUE':
        T[u['idx']] = eng
    else:
        T[u['idx']] = '\t' * (len(eng) - len(eng.lstrip('\t'))) + cover[eng]

for idx, txt in T.items():
    eng, kind = ENG[idx], KIND[idx]
    assert txt.count('\t') == eng.count('\t'), idx
    assert txt.count('"') == eng.count('"'), (idx, eng.count('"'), txt.count('"'))
    assert TAGS.findall(txt) == TAGS.findall(eng), (idx, TAGS.findall(txt), TAGS.findall(eng))
    assert not re.search(r'[\[\]`\u2019\u2014\u2013\u2026]', txt), idx
    assert not re.search(r"\b(e|piu|perche|cosi|gia|puo|cioe|percio|fa)'", txt), idx
    if kind == 'VALUE':
        assert txt == eng, idx
    else:
        assert txt.strip() and txt.strip() != eng.strip(), idx
    r = len(txt) / len(eng)
    assert 0.55 < r < 1.90, ('gate', idx, round(r, 3), eng[:60])

for n, (lo, hi) in enumerate(((1, 21), (22, 42), (43, 63))):
    d = {str(k): T[k] for k in range(lo, hi + 1)}
    with open(os.path.join(PARTS, 'part%02d.json' % (n + 1)), 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
print('63 unita (21x3) · 62 testi prosaici + 1 VALUE identico · 1 contesto · 55 tab · 98 virgolette · 2 token')
