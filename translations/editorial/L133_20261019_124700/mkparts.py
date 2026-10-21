"""mkparts.py — L133: `data/hai/unfettered side missions.txt` (67 unita', righe 237-477).

Due contesti: **`Hai Legacy 2`** (10 unita', la consegna con l'Anomalocaris) e **`Hai Legacy 3`** (57 unita', il
duello con Mera e il suo campione).

Forma: **98 virgolette** in 67 unita' — il record del progetto —, **34 unita' con tab**, **2 `VALUE`** (nomi di
missione), **2 `UI_LABEL`** (`too many ships`, ripetuta due volte), **9 `DIALOG`**, **2 `LOGBOOK`**, **8 token** in **6
famiglie** con `<date>` e `<system>` per la prima volta in questo file.

Una incoerenza del **sorgente** si riproduce, non si corregge: il `LOGBOOK` (unita' 10) parla di `food shipment`
mentre il testo (unita' 9) parla di `medical supplies`.
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
    2: "Usa l'Anomalocaris appena acquisito per portare aiuto agli Hai Unfettered su <planet> entro il <date>.",
    3: "Lasci il cantiere e vai allo spazioporto dopo il tuo incontro. Un lavoratore ti accoglie subito mentre altri "
       "cominciano a riempire la tua nave di casse, e un rapido controllo dei dati della spedizione mostra che il "
       "carico è già stato assegnato a tuo nome. Non resta che consegnarlo su <destination> entro il <date>.",
    4: "Mentre torni alla tua nave e ti prepari a decollare dal pianeta, noti un messaggio sul pannello di comando:",
    5: "\"Faresti bene a portare con te l'Anomalocaris che ti abbiamo affidato, per la tua consegna.\"",
    6: "Entrando nel sistema ti prepari a combattere per far passare il carico. Però gli Unfettered, di solito "
       "aggressivi, hanno smesso all'improvviso di spararti.",
    7: "Gli Unfettered e i loro associati non sono certo contenti quando in qualche modo scoprono che non hai "
       "consegnato il carico in tempo, e ti lasciano un breve messaggio sul pannello di comando: \"Non ti "
       "dimostrerai degno di noi fallendo le nostre richieste.\"",
    8: "Hai raggiunto <planet>, ma o non hai portato l'Anomalocaris, o parte del carico era su un'altra nave.",
    9: "Dopo l'atterraggio, un gruppo di Unfettered si raduna attorno alla tua nave e comincia a scaricare le "
       "forniture mediche, anche se stranamente non sembrano avere fretta. Poco dopo aver finito, ricevi un "
       "messaggio piuttosto breve dall'Hai a cui hai comprato la nave, insieme a una somma di crediti insolitamente "
       "grande. \"Grazie per aver aiutato i nostri fratelli, <last>. Accetta questi <payment>.\"",
    10: "Consegnato un carico urgente di cibo agli Hai Unfettered usando l'Anomalocaris, cosa che sembra averli "
        "soddisfatti.",
    12: "Sconfiggi in combattimento lo sfidante Unfettered nel sistema <system>. Hai solo 2 giorni, e restare fuori "
        "uso significa perdere lo scontro.",
    13: "Dopo aver consegnato le forniture, ti accorgi che la tua nave è al centro dell'attenzione. Un Unfettered che "
        "sembra un ingegnere viene a parlarti, inizialmente più cordiale del solito rispetto alle tue esperienze "
        "precedenti con altri Unfettered.",
    14: "\"Benvenuto. Anche se non so come tu abbia ottenuto questa nave, immagino che alcuni di noi lo vedranno come "
        "un segno. Vedi, è un relitto del nostro passato, un passato di cui siamo piuttosto orgogliosi. Per questo la "
        "maggior parte dei guerrieri Unfettered dirà che devi dimostrare il tuo diritto a usarla.\"",
    15: "Dopo un sospiro, il suo tono cambia. \"Ma io non credo a nulla di tutto questo. Quello che per me conta è che "
        "quella nave è sia resistente sia piena di preziosa tecnologia antica.\"",
    16: "I suoi occhi si illuminano mentre si concentra di più sulla tua nave. \"Vedo persino armi che abbiamo "
        "combattuto con valore per ottenere dai selvaggi Korath!\"",
    17: "All'improvviso alza la voce perché tutti la sentano. \"Io, Mera, ti sfido! Sarà un duello uno contro uno: tu "
        "sull'Anomalocaris contro il mio campione. Il vincitore si guadagnerà il diritto di possedere questo "
        "onorevole relitto e le sue possenti armi!\"",
    18: "\"Che cosa ottengo se vinco?\"",
    19: "\"Non posso semplicemente vendertela?\"",
    20: "\"Ho comprato questa nave. È mia, e ne faccio ciò che voglio.\"",
    21: "\"No, perché agli occhi dei miei fratelli questo significherebbe che nemmeno io meritavo questa nave. E "
        "allora la sfiderebbero a me.\"",
    22: "Mera si volta, parla un po' con altri Unfettered e poi si rivolge di nuovo a te. \"Ti guadagnerai il diritto "
        "di accedere ai nostri mondi. Ma, per mantenere il nostro rispetto, devi tenere questo Anomalocaris in buone "
        "condizioni finché non ti dimostrerai in un altro modo. È un artefatto inestimabile. Se rifiuti di dimostrare "
        "il tuo valore, non ti sarà più permesso atterrare qui.\"",
    23: "Poi ti lancia un'occhiataccia. \"Attento: anche se non ci sono regole ufficiali, devi usare solo "
        "l'Anomalocaris. Allora, ti alzerai in volo, o hai troppa paura?\"",
    24: "\"Accetto.\"",
    25: "\"Non ho nulla da dimostrarti. Questa nave ora è mia.\"",
    26: "Mera sogghigna. \"Bene! Non ti combatterò di persona, è troppo rischioso. Dopo tutto sono solo un'ingegnere. "
        "E non vorrei nemmeno negare a mio fratello e al suo equipaggio l'occasione di dimostrarsi contro un potente "
        "guerriero umano!\"",
    27: "Non sei sicuro che Mera faccia sul serio, ma i suoi amici sembrano decisi. Uno che pare il loro capo ti si "
        "avvicina. \"Dunque pensi di meritare di pilotare questa possente nave dell'impero Hai?\"",
    28: "\"Sì, e cosa te lo fa pensare, umano?\", aggiunge un altro.",
    29: "(Non dire nulla.)",
    30: "\"Stai cercando di spaventarmi per farmi rinunciare allo scontro?\"",
    31: "\"Lo scopriremo\", dice un terzo.",
    32: "Il capo del gruppo si avvicina e ti parla con tono più serio. \"Sappi che questa non è tanto una competizione "
        "amichevole quanto uno scontro per guadagnarti davvero il diritto di pilotare questa nave. Devi sapere che "
        "questo scontro ha alcune... regole implicite, anche se non ce ne sono di ufficiali. Diamo per scontato che "
        "tutti le conoscano, ma dato che sei un esterno te le spiegherò\", dice mentre ti allontana dal gruppo.",
    33: "\"Naturalmente, dato che è un duello, nessuno oltre a noi può interferire, ma devi anche sapere che restare "
        "fuori uso conta come sconfitta. Non pensare nemmeno di ingannarci passando a qualcosa che non sia questo "
        "Anomalocaris, o non ci prenderemo la briga di presentarci! Devi dimostrare di meritartela, dopo tutto. Al "
        "vincitore vanno le spoglie, quindi il saccheggio è permesso, ma non tentare di rubare le nostre navi. Se lo "
        "fai, tutti gli Unfettered saranno contro di te!\"",
    34: "Poi ti guarda intensamente, dritto negli occhi. \"A volte pieghiamo le regole per i nostri amici, ma con te "
        "non è questo il caso.\"",
    35: "Mera comincia a sembrare un po' impaziente. \"Vuoi parlare tutto il giorno, o combattere? Vai a Ehma Ti, "
        "insomma!\" Gli Unfettered si dirigono subito alle loro navi, ma Mera ti tira da parte quando sono abbastanza "
        "lontani. \"Voglio che sia fatto entro la fine della giornata, quindi non mettere alla prova la mia "
        "pazienza. Sei fortunato che abbia offerto io questo accordo, perché avevano intenzione di prendersi il "
        "relitto con la forza. Ora, svelto, vai alla tua nave! Fai le ultime modifiche che ti servono, poi vieni a "
        "combattere contro di noi.\"",
    36: "Vedi che gli Unfettered hanno già cominciato le procedure di lancio, quindi dovresti prepararti a decollare "
        "con il tuo Anomalocaris, e con nessun'altra nave, il prima possibile.",
    37: "Visto che è improbabile che collaborino, ti precipiti alla tua nave e decolli, con gli Unfettered che ti "
        "corrono dietro.",
    38: "Mentre lasci l'atmosfera del pianeta, ricevi un breve messaggio. \"Ti aspettiamo a Ehma Ti oggi. Non "
        "deluderci.\"",
    39: "Gli Unfettered non sembrano troppo contenti di vederti andare via con il loro premio. Lo sfidante ti aspetta "
        "già in orbita e ti chiama. \"Dove credi di andare, scimmia?\"",
    41: "Mentre decolli per unirti alla tua flotta in orbita, ricevi una chiamata dagli Unfettered. \"Devi lasciare la "
        "tua flotta in attesa qui. Se ti aiutano, il duello sarà annullato!\"",
    42: "Sei chiamato dagli Unfettered appena raggiungi l'orbita. \"Ci credi ciechi, scimmia? Non stai pilotando il "
        "relitto come nave ammiraglia! Non vali nemmeno una sequenza di lancio; il duello è annullato\", dicono "
        "arrabbiati.",
    43: "Entrando nel sistema vedi che lo sfidante ti aspetta davvero, e ti manda subito un segnale. \"Mostraci di che "
        "cosa sei capace, scimmia! Mostraci che sai controllare bene le tue armi, come ogni guerriero dovrebbe! "
        "Dimostraci di avere la forza di mettere fuori uso le nostre navi, ma anche la moderazione di non "
        "distruggerle!\"",
    45: "Arrivando con la tua flotta in questo sistema, ricevi una chiamata dagli Unfettered. \"Se non sai nemmeno "
        "contare quante navi hai, non sei degno del nostro tempo, scimmia! Il disonore non ti porterà da nessuna "
        "parte con noi, i Veri Hai! Vattene.\"",
    46: "Sei chiamato dagli Unfettered mentre entri nel sistema. \"Scimmia! Perché rifiuti di usare il relitto? Solo "
        "vincendo con il relitto puoi dimostrare di esserne degno. Vattene: non sprecheremo altro tempo con gente "
        "come te.\"",
    47: "Ricevi una chiamata dagli Unfettered. \"Sei fuggito e non hai completato il duello. Perciò non godrai più di "
        "un rispetto immeritato! Ti converrebbe restituirci la nave, se mai ti trovassimo di nuovo sui nostri mondi!",
    48: "Dopo che la tua nave è fuori uso, una delle navi Unfettered ti chiama. \"Hai perso la sfida, ma non ci "
        "aspettavamo molto da un umano come te. Ripareremo la tua nave per una congrua tangente, ma faresti meglio ad "
        "atterrare su uno dei nostri mondi e restituircela con un risarcimento molto generoso. Se proverai a "
        "tenerla, faremo le cose in modo duro.",
    49: "\"Sappi però che la tua tregua con noi finisce appena atterri. Oggi ci hai deluso. Forse un giorno ti "
        "dimostrerai diverso.\"",
    50: "Sei contattato dagli Unfettered mentre entri nell'atmosfera del pianeta. \"Non hai completato il duello. Il "
        "cessate il fuoco è finito. Non godrai più di un rispetto immeritato!\"",
    51: "Ricevi una chiamata da Mera, che sembra piuttosto arrabbiata. \"Distruggere la nave può essere solo frutto di "
        "incompetenza o di intenti malvagi, e non tollereremo né l'una né gli altri!\"",
    52: "Ricevi un messaggio dalla nave Unfettered. \"Ci arrendiamo. Atterra su Firelode per ricevere la tua "
        "ricompensa.\"",
    53: "\"Vieni qui con una flotta e hai la sfacciataggine di mettere fuori uso la mia nave? Il tuo disonore non "
        "conosce limiti, scimmia!\"",
    54: "Ricevi una chiamata da Mera, che sembra piuttosto arrabbiata. \"Distruggere la nave può essere solo frutto di "
        "incompetenza o di intenti malvagi, e non tollereremo né l'una né gli altri!\"",
    55: "Sei riuscito a sconfiggere lo sfidante Unfettered. Ora è il momento di atterrare su Firelode e reclamare la "
        "tua ricompensa.",
    56: "\"Vieni qui con una flotta e hai la sfacciataggine di mettere fuori uso la mia nave? Il tuo disonore non "
        "conosce limiti, scimmia!\"",
    57: "Mera ti chiama. \"Fermati! Sono qui solo come osservatrice. Se distruggi la mia nave, l'accordo salta!\"",
    58: "Mentre distruggi la Lightning Bug, con Mera e il suo equipaggio a bordo, ricevi una chiamata arrabbiata dagli "
        "Unfettered. \"Hai completamente mancato di rispetto alle regole di un duello e hai ucciso una delle nostre "
        "ingegnere più illustri! Non sarai più il benvenuto qui!\"",
    59: "Riuscito a usare un'antica nave da guerra Hai per battere uno sfidante Unfettered, guadagnando il rispetto "
        "degli Hai Unfettered finché la nave resterà in mio possesso.",
    60: "Quando atterri tutto intero, Mera si avvicina, sembrando molto sorpresa. \"Hai vinto davvero! Ho visto "
        "tutto, e i dati che ho raccolto sugli effetti di queste armi esotiche saranno molto utili per la mia "
        "ricerca. È stato difficile per te?\"",
    61: "\"È stato divertente.\"",
    62: "\"È stato facile!\"",
    63: "\"È stata una sfida.\"",
    64: "\"Non diventare troppo sicuro di te, capitano\", riflette. \"Sono sicura che sai cosa succede a certi "
        "piloti.",
    65: "\"Oh, quindi il loro piano ha quasi funzionato dopotutto? Forse avrei dovuto partecipare anch'io allo "
        "scontro.",
    66: "\"Beh, congratulazioni, non pensavo che ne avessi la stoffa. Ti darò l'autorizzazione ad atterrare, a "
        "condizione che tu tenga intero questo relitto del nostro passato. Ricorda: al momento la tua reputazione con "
        "noi dipende unicamente da quella nave. Se in qualche modo la perdi per un'incompetenza tua, farai una "
        "pessima figura con i Veri Hai.\"",
    67: "Mera poi se ne va mentre comincia a rivedere i dati del tuo scontro su un piccolo dispositivo. Per ora sembra "
        "che gli Hai Unfettered abbiano un certo rispetto per te, finché hai l'Anomalocaris.",
}

db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ST = {u['idx']: db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] for u in SRC}
assert set(ST.values()) == {'PENDING'}, {k: v for k, v in ST.items() if v != 'PENDING'}

assert collections.Counter(u['kind'] for u in SRC) == {'MISSION_TEXT': 50, 'DIALOG': 9, 'VALUE': 2, 'DESCRIPTION': 2,
                                                       'LOGBOOK': 2, 'UI_LABEL': 2}
assert sum(1 for u in SRC if u['english'].startswith('\t')) == 34
assert sum(u['english'].count('"') for u in SRC) == 98
ctx = collections.OrderedDict()
for u in SRC:
    ctx[u['context']] = ctx.get(u['context'], 0) + 1
assert len(ctx) == 2 and list(ctx.values()) == [10, 57], list(ctx.items())
assert collections.Counter(t for u in SRC for t in TAGS.findall(u['english'])) == {
    '<planet>': 2, '<date>': 2, '<destination>': 1, '<last>': 1, '<payment>': 1, '<system>': 1}

VAL = [1, 11]
LAB = [40, 44]
assert [u['idx'] for u in SRC if u['kind'] == 'VALUE'] == VAL
assert [u['idx'] for u in SRC if u['kind'] == 'UI_LABEL'] == LAB
assert [ENG[i] for i in VAL] == ['Heritage Reclaimed', 'Ancient Claim']
assert [ENG[i] for i in LAB] == ['too many ships', 'too many ships']
IDENT = VAL + LAB

expected = [i for i in ENG if i not in IDENT]
assert sorted(D) == expected, (len(D), len(expected), [i for i in expected if i not in D],
                               [i for i in D if i not in expected])

T = {}
for u in SRC:
    eng = u['english']
    if u['idx'] in IDENT:
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
    if idx in IDENT:
        assert txt == eng, idx
    else:
        assert txt.strip() and txt.strip() != eng.strip(), idx
    r = len(txt) / len(eng)
    assert 0.55 < r < 1.90, ('gate', idx, round(r, 3), eng[:60])

dup = {}
for u in SRC:
    dup.setdefault(KEY[u['idx']], set()).add(T[u['idx']])
assert not [(k, v) for k, v in dup.items() if len(v) > 1], [(k[:50], v) for k, v in dup.items() if len(v) > 1]

for n, (lo, hi) in enumerate(((1, 23), (24, 45), (46, 67))):
    d = {str(k): T[k] for k in range(lo, hi + 1)}
    with open(os.path.join(PARTS, 'part%02d.json' % (n + 1)), 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
print('67 unita (23+22+22) · %d testi distinti · 2 VALUE + 2 UI_LABEL identici · 98 virgolette' % len(dup))
print('34 tab · 8 token in 6 famiglie · 2 contesti (10 + 57) · 9 DIALOG')
