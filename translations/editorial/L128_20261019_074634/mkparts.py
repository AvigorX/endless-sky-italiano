"""mkparts.py — L128: la coda di `data/incipias/incipias first contact.txt` (43 unita', righe 343-439). CHIUDE IL FILE.

Forma: **3 contesti** (2 + 1 + 40), **33 `MISSION_TEXT`**, **4 `UI_LABEL`**, **3 `LOGBOOK`**, **1 `DIALOG`**, **1
`VALUE`**, **1 `DESCRIPTION`**, **30 unita' con tab**, **43 virgolette**, **6 token** in **5 famiglie**, **43 testi
distinti**.

- **Le 4 `UI_LABEL`** (`has incipias ship`, `initial choice`, `odd question`, `end no time`) restano **identiche**.
- **Il `VALUE`** (`Bring Incipias back to <planet>`) e' un nome di missione **con un token dentro**: identico al
  sorgente, token compreso.
- **La voce di diario dell'unita' 2** e' **identica** a L127 unita' 24: la resa si **rilegge** dal `translation.json`
  di L127 e si confronta, non si riscrive a memoria.
- **Tre unita' con virgolette sbilanciate** (28, 30, 36): il sorgente apre la battuta e non la chiude; la resa la
  riproduce.
"""
import collections
import json
import os
import re
import sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
PARTS = os.path.join(HERE, 'parts')
PREV = os.path.join(L10N, 'staging/editorial/L127_20261019_073900/translation.json')
SRC = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units']
ENG = {u['idx']: u['english'] for u in SRC}
KIND = {u['idx']: u['kind'] for u in SRC}
TAGS = re.compile(r'<[^<>]+>')

UNIQ = [
    ("Noticed an alert on <ship>'s dashboard",
     "Notato un avviso sul pannello della <ship> riguardo a una lieve corruzione dei dati. La seguente voce di diario "
     "è stata recuperata, ma la data originale è andata perduta."),
    ("You identify the stranded alien ship",
     "Riconosci sugli scanner la nave aliena bloccata che avevi assistito, ma senza un modo per comunicare con loro "
     "non puoi aiutarli. Non ti resta che lasciarli al loro destino su questo mondo tempestoso."),
    ("Bring the rescued Incipias back home",
     "Riporta a casa gli Incipias salvati, su <destination>"),
    ("you don't have enough passenger space",
     "Sei atterrato su <origin>, ma non hai abbastanza spazio passeggeri per i <bunks> Incipias. Torna qui quando "
     "avrai liberato lo spazio necessario."),
    ("Your ship dives into the clouds of the gas giant",
     "La tua nave si tuffa tra le nuvole del gigante gassoso, entrando in un ambiente di una scala che non hai mai "
     "sperimentato prima. Nuvole gigantesche torreggiano come castelli, aprendosi talvolta in caverne d'aria "
     "altrettanto vaste. Turbini di vento spazzano l'atmosfera come pilastri che reggono il cielo. Per quanto i venti "
     "siano brutali, la tua nave ci scivola attraverso come se non avessero alcun effetto su di lei."),
    ("Activating your scanners, you look for the stranded ship",
     "Attivando gli scanner, cerchi la nave bloccata di prima. Presto un piccolo segnale appare sul radar, e manovri "
     "la nave verso la sua posizione. La nave bloccata compare, in condizioni ancora peggiori della prima volta. Le "
     "tempeste sembrano aver danneggiato parte dello scafo, e gli scudi sono del tutto abbassati; il generatore di "
     "scudi potrebbe essersi spento quando sono rimasti senza carburante."),
    ("Any attempt to hail the Incipias ship results in no answer",
     "Qualsiasi tentativo di contattare la nave degli Incipias non ottiene risposta. Con cautela, avvicini la tua "
     "nave finché non riesci ad attraccare."),
    ("They seem on guard at first",
     "Quando il portello si apre, vedi cinque Incipias fluttuare davanti a te. All'inizio sembrano in allerta, e ci "
     "mettono un momento a riconoscerti dall'incontro precedente mentre prepari il dispositivo di traduzione per "
     "parlare con loro."),
    ("they were clearly not expecting a human piloting",
     "Quando il portello si apre, vedi cinque Incipias fluttuare davanti a te. Notando la tua presenza, si ritirano "
     "in fretta; chiaramente non si aspettavano un pilota umano alla guida di una delle loro navi. Ci mettono un "
     "momento a riconoscerti dall'incontro precedente mentre prepari il dispositivo di traduzione per parlare con "
     "loro."),
    ("Hello, I have come to save you",
     "\"Salve, sono venuto a salvarvi.\""),
    ("I have been sent by your people",
     "\"Mi hanno mandato i vostri simili per riportarvi a casa.\""),
    ("You light our language",
     "Gli Incipias sembrano passare da uno stato teso a uno stupito, e uno di loro inizia a pulsare. \"Tu luce la "
     "nostra lingua? Che sorpresa. Non saremmo sopravvissuti a un altro giorno-momento qui. Sei il nostro "
     "protettore-di-vite. Ci piacerebbe parlare ancora, ma sta arrivando una calamità-meteo. Dobbiamo andare ora.\" "
     "L'assenza di emozione nella traduzione è preoccupante, dato il contenuto del messaggio."),
    ("You tell them to board your ship",
     "Di' loro di salire sulla tua nave, e poco dopo decolli. Per fortuna parti appena in tempo per evitare una "
     "potente tempesta di vento che si avvicina alla zona."),
    ("split into two groups called the Hicemus",
     "Gli Incipias sembrano divisi in due gruppi, chiamati Hicemus e Conlatio; i primi occupano una stazione "
     "spaziale, i secondi il mondo d'origine degli Incipias. I Conlatio non sembrano permettere estranei sul loro "
     "pianeta natale."),
    ("your passengers thank you again",
     "Una volta atterrato sulla stazione, i tuoi passeggeri ti ringraziano di nuovo e se ne vanno, probabilmente per "
     "riposare come merita. Mentre scendi dalla <ship>, un altro Incipias ti si avvicina. Le sue scaglie sembrano "
     "consumate, e noti intricati attaccamenti simili ad artigli attorno all'estremità dei suoi tentacoli. \"Seguimi, "
     "aiutante-esterno, prima che si raduni una folla. Vorremmo parlare.\""),
    ("They guide you through the hallways",
     "Ti guidano attraverso i corridoi evitando i gruppi più numerosi, anche se scelgono solo corridoi orizzontali. "
     "Arrivi in una grande stanza con vista sull'intera stazione, dove sono già presenti tre Incipias. Uno comincia a "
     "brillare."),
    ("leader-governers of the Hicemus",
     "\"Benvenuto. Siamo i capi-governatori degli Hicemus, il governo regnante degli Incipias. Se sei d'accordo, "
     "vorremmo porti alcune domande-quesiti. In cambio saremmo disposti ad ascoltare le tue domande-quesiti.\""),
    ("Sure, ask me something",
     "\"Certo, chiedimi qualcosa.\""),
    ("I have other stuff to do",
     "\"Mi dispiace, ma ho altro da fare.\""),
    ("A green glow appears on all of them",
     "Un bagliore verde appare su tutti e tre. \"Grazie per averci dedicato tempo-pazienza. Puoi raccontarci di più "
     "del vuoto-spazio profondo che ci circonda?\""),
    ("exhaustive story of what I have seen",
     "(Racconta loro una storia esauriente di ciò che ho visto finora.)"),
    ("rough overview of what I have seen",
     "(Dai un quadro approssimativo di ciò che ho visto.)"),
    ("mixed with green and red",
     "Dopo aver \"visto\" la tua spiegazione, una rapidissima sequenza di colori viene scambiata tra gli Incipias. Il "
     "tuo traduttore non riesce a seguirla, così resti a guardarli lampeggiare in quelli che finiscono per essere "
     "toni gialli mescolati a verde e rosso."),
    ("it truly raise-strengthens",
     "\"Grazie per questo spunto. Tutto ciò che abbiamo raccolto finora è stato osservare-studiare le stelle. "
     "Pensare che là fuori ci sia così tanto... accresce davvero-rafforza la determinazione a esplorare."),
    ("tones mixed with green.",
     "Dopo aver \"visto\" la tua spiegazione, una rapidissima sequenza di colori viene scambiata tra gli Incipias. Il "
     "tuo traduttore non riesce a seguirla, così resti a guardarli lampeggiare in quelli che finiscono per essere "
     "toni gialli mescolati a verde."),
    ("profound-depth insight",
     "\"Grazie per questa visione-profonda. Tutto ciò che abbiamo raccolto finora è stato osservare-studiare le "
     "stelle a noi vicine. Pensare che là fuori ci sia così tanto... suscita davvero una determinazione-volontà a "
     "esplorare."),
    ("But now to you",
     "\"Ma ora tocca a te. C'è qualcosa che vorresti sapere?\""),
    ("Why can I not land on your home planet",
     "\"Perché non posso atterrare sul vostro pianeta natale?\""),
    ("Why do you call this station your capital",
     "\"Perché chiamate questa stazione la vostra capitale?\""),
    ("How is life on a gas giant",
     "\"Com'è la vita su un gigante gassoso?\""),
    ("I do not have any more questions",
     "\"Non ho altre domande.\""),
    ("Our origin-world is not directly ruled by us",
     "Un lampo rosso appare per un solo secondo. \"Il nostro mondo-origine non è governato direttamente da noi. "
     "Potrebbero avvicinarti separatamente in un punto-futuro, ma attento alle loro luci. Hanno valori di "
     "tempi-antichi lasciati da parte da molto tempo da noi, che avanziamo in fretta."),
    ("This station is our greatest action-pride",
     "Quello che pulsa ora assume un verde brillante, \"Questa stazione è il nostro più grande orgoglio-azione, il "
     "nostro ponte-stellare. In onore del nostro impulso a espanderci abbiamo fatto di questa stazione la nostra "
     "capitale, per dimostrare la nostra determinazione.\""),
    ("What an odd-reasonable question",
     "\"Che domanda strano-ragionevole.\" Il suo bagliore si trasforma in un turbine di viola e verde. \"Potremmo "
     "chiedere lo stesso a te: com'è vivere su roccia dura? Ma capiamo la tua origine-ragione. Lascia che ti parli "
     "delle sale-nuvole del nostro cielo-casa. I fulmini tracceranno i più bei canti-di-colore tra le "
     "nuvole-pilastro. Tra di esse ci sono le nostre città, i luoghi più color-vitali che vedrai mai. È una "
     "descrizione un po' gradiente-poetico, ma non so cos'altro dire.\""),
    ("You have given us much to process",
     "\"Grazie ancora per il tuo tempo. Ci hai dato molto su cui riflettere. Speriamo che anche tu abbia tratto "
     "beneficio da questo incontro-colloquio.\""),
    ("a rush of colors reflecting onto the walls",
     "Ti congedi, e mentre esci dalla stanza vedi un fiotto di colori riflettersi sulle pareti."),
    ("We are understanding-sad",
     "\"Siamo comprensione-triste. Buon viaggio, capitano.\" Noti una lieve tonalità blu nella comunicazione del "
     "rappresentante mentre uno degli Incipias ti riaccompagna alla nave."),
]

db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ST = {u['idx']: db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] for u in SRC}
assert set(ST.values()) == {'PENDING'}, {k: v for k, v in ST.items() if v != 'PENDING'}

assert collections.Counter(u['kind'] for u in SRC) == {'MISSION_TEXT': 33, 'UI_LABEL': 4, 'LOGBOOK': 3,
                                                       'DIALOG': 1, 'VALUE': 1, 'DESCRIPTION': 1}
assert sum(1 for u in SRC if u['english'].startswith('\t')) == 30
assert sum(u['english'].count('"') for u in SRC) == 43
ctx = collections.Counter(u['context'] for u in SRC)
assert len(ctx) == 3 and list(ctx.values()) == [2, 1, 40], list(ctx.items())
assert collections.Counter(t for u in SRC for t in TAGS.findall(u['english'])) == {
    '<ship>': 2, '<planet>': 1, '<destination>': 1, '<origin>': 1, '<bunks>': 1}

LAB = [u['idx'] for u in SRC if u['kind'] == 'UI_LABEL']
assert LAB == [11, 13, 38, 42], LAB
assert [ENG[i] for i in LAB] == ['has incipias ship', 'initial choice', 'odd question', 'end no time']
VAL = [u['idx'] for u in SRC if u['kind'] == 'VALUE']
assert VAL == [4] and ENG[4] == 'Bring Incipias back to <planet>'

# l'unita' 2 ripete alla lettera la voce di diario di L127 unita' 24: la resa si rilegge dal lotto precedente.
prev = {u['english']: u['italian'] for u in json.load(open(PREV, encoding='utf-8'))['units']}
SHARED = ENG[2]
assert SHARED in prev, SHARED[:60]
assert SHARED.startswith('Discovered that the species to the northeast of Hai space')

distinct = list(dict.fromkeys(ENG.values()))
assert len(distinct) == 43, len(distinct)
prose = [e for e in distinct if e not in {ENG[i] for i in LAB} and e != ENG[4]]
assert len(prose) == 38 and len(UNIQ) == 37, (len(prose), len(UNIQ))   # 37 firme + la voce riletta da L127


def resolve(eng):
    if eng == SHARED:
        return prev[SHARED]
    hits = [t for s, t in UNIQ if s in eng]
    assert len(hits) == 1, (len(hits), eng[:90], hits)
    return hits[0]


cover = {e: resolve(e) for e in prose}
assert len(set(cover.values())) == 38, 'due testi distinti con la stessa resa'

T = {}
for u in SRC:
    eng = u['english']
    if u['kind'] in ('UI_LABEL', 'VALUE'):
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
    if kind in ('UI_LABEL', 'VALUE'):
        assert txt == eng, idx
    else:
        assert txt.strip() and txt.strip() != eng.strip(), idx
    r = len(txt) / len(eng)
    assert 0.55 < r < 1.90, ('gate', idx, round(r, 3), eng[:60])

for n, (lo, hi) in enumerate(((1, 15), (16, 29), (30, 43))):
    d = {str(k): T[k] for k in range(lo, hi + 1)}
    with open(os.path.join(PARTS, 'part%02d.json' % (n + 1)), 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
print('43 unita (15+14+14) · 38 testi prosaici + 4 UI_LABEL + 1 VALUE identici · 3 contesti · 30 tab · 43 virgolette'
      ' · 6 token · 1 voce di diario riletta da L127')
