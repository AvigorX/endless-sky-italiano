"""mkparts.py — L135: `data/starts.txt`, righe 18-134 (32 unita'). PRIMO LOTTO DI UN FILE NUOVO.

Il file sono **gli inizi di partita**: `VALUE` = **nome dell'inizio** (`Endless Sky`, `Deep Desire`), `DESCRIPTION` =
testo di scelta, `CONVERSATION` = la scena iniziale, `LOGBOOK` = le voci di diario.

Misure: **4 contesti completi**, **zero token in tutto il file** (asserzione vuota), **14 unita' con tab**, **14
virgolette**, **27 testi distinti** su 32 (cinque frasi ripetute fra `start:default` e `start:deep`: unita' 21-25
riprendono 5-9, rese con costanti).

Terminologia coerente con lo staging: `Deep` e `Dirt Belt` restano nomi propri inglesi (266 e 27 occorrenze gia'),
`Syndicate` -> Sindacato, `Navy` -> Marina, `Paradise Worlds` -> Mondi del Paradiso. I numeri seguono la convenzione
italiana (480.000 / 0,4%) come nei lotti precedenti.
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
KEY = {i: e.lstrip('\t') for i, e in ENG.items()}
TAGS = re.compile(r'<[^<>]+>')

REPUBLIC = ("Centinaia di anni fa i territori indipendenti sparsi nello spazio umano accettarono di unirsi in un unico "
            "governo democratico, con la Terra come capitale. L'ascesa della Repubblica inaugurò un lungo periodo di "
            "pace e di prosperità nella storia umana.")
PARLIAMENT = ("La rappresentanza in Parlamento repubblicano si basa sulla popolazione. Questo significa che alcuni "
              "singoli \"Mondi del Paradiso\" hanno più rappresentanti di intere regioni come il Dirt Belt, dove la "
              "popolazione è più rada.")
SYNDICATE = ("Il Sindacato è una megacorporazione, il più grande datore di lavoro dello spazio umano. Chi non trova un "
             "lavoro stabile altrove accorre ai mondi-fabbrica del Sindacato, dove un impiego è quasi garantito. "
             "Sebbene il Sindacato faccia tecnicamente parte della Repubblica, i suoi mondi sono governati "
             "direttamente dalla corporazione.")
SYNDICATE_ENV = ("Il Sindacato è una parte centrale dell'economia repubblicana, ma è anche noto per vendere prodotti "
                 "scadenti e per danneggiare l'ambiente dei mondi che controlla. Il trattamento riservato ai "
                 "lavoratori è discutibile, e la sua opposizione al sindacalismo è leggendaria. Alcune "
                 "cittadine-fabbrica del Sindacato sono state persino accusate di violazioni dei diritti umani.")
PIRATES = ("Nei sistemi stellari più poveri e remoti, dove la Marina pattuglia di rado, gli attacchi pirata alle navi "
           "mercantili sono frequenti. I pirati sono noti anche per attaccare grandi convogli di mercantili senza "
           "scorta in zone più popolate. La maggior parte delle flotte pirata viene da mondi senza legge ai margini "
           "dello spazio umano.")

D = {
    1: "Endless Sky",
    2: "Sei cresciuto su New Boston, un mondo senza niente di interessante nel Dirt Belt. Sogni di possedere "
       "un'astronave dal tuo primo giorno allo spazioporto. Dopo anni di lavoro in una tessitura, hai messo da parte "
       "abbastanza crediti per richiedere una licenza di pilota alla Repubblica. Ora devi accendere un mutuo sulla "
       "tua prima nave...",
    3: "Questa è la classica esperienza di Endless Sky. Comincerai indebitato e dovrai usare la tua nuova astronave "
       "per estinguere il mutuo.",
    4: "Finalmente sono riuscito a mettere insieme abbastanza soldi per comprare una licenza di pilota. Gli interessi "
       "sul mutuo della mia astronave sono esorbitanti.",
    5: REPUBLIC,
    6: PARLIAMENT,
    7: SYNDICATE,
    8: SYNDICATE_ENV,
    9: PIRATES,
    10: "L'architettura della banca è quella che avresti chiamato \"futuristica\" quando sognavi che il futuro fosse "
        "meno squallido del presente: piani su piani di curve, guglie e balconi, tutto in metallo lucente. Un "
        "portiere sta accanto a ciascuna delle pesanti porte di vetro. Indossi il tuo vestito migliore, ma accanto a "
        "loro ti senti sciatto.",
    11: "L'ufficio del mediatore di prestiti è altrettanto intimidatorio. Grandi monitor occupano le pareti, con "
        "quotazioni di borsa e altre informazioni che scorrono quasi troppo in fretta per essere lette. Ogni tanto "
        "intravedi nomi di luoghi che hai visto solo nei film: Aldebaran. Tarazed. Terra.",
    12: "La penna è pesante come il piombo, ma scorre quasi senza attrito mentre apponi le iniziali in fondo a pagina "
        "dopo pagina di sinistri documenti legali e firmi diverse decine di dichiarazioni, avvisi e accordi. Il "
        "banchiere, un uomo di mezza età stempiato in un abito che sospetti costare più dell'astronave che stai per "
        "comprare, sfoglia le pagine davanti a te in fretta, emettendo un secco \"Firmi qui. Ora qui\" mentre indica "
        "ogni pagina. Si muove rapido, meccanico.",
    13: "L'unico momento in cui si anima davvero è quando ti spiega il prospetto sulla verità del prestito. \"Stai "
        "prendendo in prestito 480.000 crediti,\" dice, \"da restituire nell'arco di un anno. Il tuo tasso "
        "d'interesse giornaliero è dello 0,4%, il che significa che i tuoi pagamenti giornalieri sono di 2.503 "
        "crediti, e alla fine dell'anno avrai pagato... 433.567 crediti di interessi. Firma qui.\" Sorride.",
    14: "Scrivi il tuo nome un'ultima volta:",
    15: "L'ascensore è così ben calibrato che non ti accorgi nemmeno che si muove, finché non ti ha riportato nella "
        "hall. Ma mentre esci dalla banca, stai sorridendo. Questa folle avventura ti sembra d'un tratto reale. Lo "
        "farai davvero. Finalmente lascerai questo pianeta.",
    16: "Rispetto alla banca, ti senti molto più a casa nel cantiere navale, camminando tra scafi arrugginiti e navi "
        "più nuove che brillano al sole. Senti odore di grasso, sporco e carburante per razzi; odori meravigliosi. Ci "
        "sono tre modelli di nave nel tuo budget. Quale sceglierai determinerà il tuo futuro...",
    17: "Deep Desire",
    18: "Sei cresciuto su Midgard, un mondo della regione avanzata del Deep. La maggior parte delle persone "
        "intraprende studi superiori, ma tu hai sempre voluto essere capitano di un'astronave. Finiti gli studi "
        "primari, scopri che il Deep offre prestiti a basso interesse ai capitani che si dedicano alla prospezione e "
        "hanno voti abbastanza alti, e tu ce l'hai fatta! Ti dirigi verso la capitale, New Reykjavik...",
    19: "Questo inizio offre un tasso d'interesse più basso e più crediti per potenziare la tua nave.",
    20: "Ho fatto domanda per il programma di capitani del Deep, e sono stato accettato. Il programma comprendeva una "
        "licenza di pilota e un prestito a basso interesse.",
    21: REPUBLIC,
    22: PARLIAMENT,
    23: SYNDICATE,
    24: SYNDICATE_ENV,
    25: PIRATES,
    26: "Il treno dalla tua città natale ondeggia avanti e indietro con un ritmo costante, portandoti sempre più "
        "vicino alla capitale. Qualche fila più avanti, una giovane coppia della tua età parla con entusiasmo del "
        "trasloco nel nuovo appartamento, mentre le loro gambe urtano i bagagli. Dietro di te, un uomo molto più "
        "anziano in una tuta da lavoro unta si congeda da un conoscente.",
    27: "Poco dopo arrivi a New Reykjavik, all'ufficio governativo che gestisce i prestiti per le astronavi. La "
        "reception è un brusio di attività: altri neolaureati dalla faccia fresca chiacchierano tra loro in attesa "
        "del proprio turno. La luce del sole cade dalle finestre a fessura del soffitto su una rappresentazione "
        "tridimensionale dell'emblema del Deep al centro della hall, un albero rosso i cui rami formano la sagoma di "
        "un cervello. Un cerchio di testo circonda la scultura, proclamando i valori fondamentali del Deep: Pace. "
        "Prosperità. Progresso.",
    28: "Alla fine chiamano il tuo numero, e dopo aver letto la tua domanda l'impiegato ti consegna due tessere. Una "
        "è il tuo Certificato di idoneità per un prestito a basso interesse presso una banca vicina. L'altra è la "
        "tua licenza di pilota, già pagata per intero. Il tuo biglietto per le stelle.",
    29: "Inserisci la tessera in uno sportello automatico della banca e, dopo un leggero ping, un grande documento "
        "riempie lo schermo. Una voce sintetica dice: \"Stai prendendo in prestito 680.000 crediti, da restituire "
        "nell'arco di un anno. Il tuo tasso d'interesse giornaliero è dello 0,2%, il che significa che i tuoi "
        "pagamenti giornalieri sono di 2.627 crediti, e alla fine dell'anno avrai pagato 278.760 crediti di "
        "interessi. Scrivi il tuo nome sullo schermo quando sei pronto.\"",
    30: "Dopo aver riletto con cura ogni pagina del contratto di prestito, firmi il tuo nome:",
    31: "Esci di corsa dalla banca e salti sulla metro verso il cantiere navale. Mentre il resto della carrozza guarda "
        "fuori dai finestrini o i propri dispositivi con aria assente, tu riesci a malapena a restare serio, "
        "rigirando la licenza di pilota almeno cento volte prima della fine del viaggio. Pensi di buttare via "
        "l'abbonamento ai trasporti appena sceso, ma all'ultimo momento cambi idea. Non resterà molto altro a legarti "
        "a questo pianeta.",
    32: "Avevi studiato i filmati del cantiere di New Reykjavik nei tuoi anni più giovani, ma vedere il posto di "
        "persona supera ogni tua più sfrenata aspettativa. I venditori usano display olografici per mostrare varie "
        "navi a clienti vestiti con eleganza, mentre astronavi alte come grattacieli incombono silenziose nell'ombra "
        "del cantiere, in attesa che i mercanti più ricchi se ne impossessino. Anche se la maggior parte delle navi è "
        "ben fuori dalla tua portata, ne individui quattro modelli che potrai comprare. Quale sceglierai determinerà "
        "il tuo futuro...",
}

db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ST = {u['idx']: db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] for u in SRC}
assert set(ST.values()) == {'PENDING'}, {k: v for k, v in ST.items() if v != 'PENDING'}

assert collections.Counter(u['kind'] for u in SRC) == {'CONVERSATION': 18, 'LOGBOOK': 8, 'DESCRIPTION': 4, 'VALUE': 2}
assert sum(1 for u in SRC if u['english'].startswith('\t')) == 14
assert sum(u['english'].count('"') for u in SRC) == 14
assert [u['idx'] for u in SRC if u['english'].count('"') % 2] == []
ctx = collections.Counter(u['context'] for u in SRC)
assert len(ctx) == 4 and sorted(ctx.values()) == [3, 3, 13, 13], list(ctx.items())
assert collections.Counter(t for u in SRC for t in TAGS.findall(u['english'])) == {}
assert [u['idx'] for u in SRC if u['kind'] == 'VALUE'] == [1, 17]
assert [ENG[1], ENG[17]] == ['Endless Sky', 'Deep Desire']
assert [u['idx'] for u in SRC if u['kind'] == 'UI_LABEL'] == []
assert (min(u['line'] for u in SRC), max(u['line'] for u in SRC)) == (18, 130)
assert sorted(D) == list(range(1, 33)), (len(D), [i for i in range(1, 33) if i not in D])
assert sum(1 for i in (21, 22, 23, 24, 25) if D[i] == D[i - 16]) == 5

T = {}
for u in SRC:
    eng = u['english']
    T[u['idx']] = '\t' * (len(eng) - len(eng.lstrip('\t'))) + D[u['idx']]

for idx, txt in T.items():
    eng = ENG[idx]
    assert txt.count('\t') == eng.count('\t'), idx
    assert txt.count('"') == eng.count('"'), (idx, eng.count('"'), txt.count('"'))
    assert TAGS.findall(txt) == TAGS.findall(eng) == [], idx
    assert len(txt) - len(txt.rstrip()) == len(eng) - len(eng.rstrip()), ('spazio finale', idx)
    assert not re.search(r'[\[\]`\u2019\u2014\u2013\u2026]', txt), idx
    assert not re.search(r"\b(e|piu|perche|cosi|gia|puo|cioe|percio|fa)'", txt), idx
    if eng.strip() in ('Endless Sky', 'Deep Desire'):
        assert txt == eng, idx
    else:
        assert txt.strip() and txt.strip() != eng.strip(), idx
    r = len(txt) / len(eng)
    assert 0.55 < r < 1.90, ('gate', idx, round(r, 3), eng[:60])

dup = {}
for u in SRC:
    dup.setdefault(KEY[u['idx']], set()).add(T[u['idx']])
assert not [(k, v) for k, v in dup.items() if len(v) > 1]
assert len(dup) == 27, len(dup)

for n, (lo, hi) in enumerate(((1, 8), (9, 16), (17, 25), (26, 32))):
    d = {str(k): T[k] for k in range(lo, hi + 1)}
    with open(os.path.join(PARTS, 'part%02d.json' % (n + 1)), 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
print('32 unita (8+8+9+7) · 27 testi distinti (5 frasi ripetute) · 4 contesti completi')
print('zero token in tutto il file · 14 tab · 14 virgolette (nessuna dispari) · 2 VALUE identici')
