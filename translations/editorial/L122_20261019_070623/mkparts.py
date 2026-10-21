"""mkparts.py — L122: chiude `data/human/campaign events.txt` (42 unita', righe 1338-3468, `fine file`).

Coda del file, con la forma **piu' semplice** incontrata in questo file: **41 `DESCRIPTION`** e **1
`MISSION_TEXT`**, **18 contesti**, **21 unita' con tab**, **8 virgolette**, **zero token**, **zero quadre**.

- **3 testi vengono da L120/L121** (il paragrafo del porto di Deep con Poseidon Industries, la miniera di Clink,
  New Austria): la resa si **rilegge** dai loro `translation.json`.
- **33 testi nuovi** in `UNIQ`: **36 testi distinti** per 42 unita'. Tre testi compaiono **tre volte** (il porto di
  Deep, l'apertura di Bloodsea) e due **due volte** (New Iceland, le maschere antipolvere), perche' il file
  racconta lo stesso mondo in momenti diversi.
"""
import collections
import glob
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

PREV = {}
for lot in ('L120_*', 'L121_*'):
    for f in glob.glob(os.path.join(L10N, 'staging/editorial', lot, 'translation.json')):
        for u in json.load(open(f, encoding='utf-8'))['units']:
            PREV[u['english']] = u['italian']

UNIQ = [
    ("nine completed walls",
     "A nord dello spazioporto si trova il Memoriale di Guerra dei Mondi Liberi, una serie di pareti di granito "
     "incise con i nomi dei caduti. Le nove pareti completate sono già piene su entrambi i lati; sembra improbabile "
     "che le altre quattordici resistano fino alla fine della guerra."),
    ("Two additional rings",
     "A nord dello spazioporto si trova il Memoriale di Guerra dei Mondi Liberi, una serie di pareti di granito "
     "incise con i nomi dei caduti. Intorno alle prime ventitré pareti e alle cinquanta pareti del vecchio anello "
     "esterno sono stati costruiti due nuovi anelli di pareti."),
    ("perpetually hazy volcanic world",
     "New Iceland è un mondo vulcanico perennemente fosco, con un'atmosfera leggermente caustica ma con riserve di "
     "metalli e petrolchimici sufficienti ad attirare un gran numero di coloni. Alcuni di quei coloni si guadagnano "
     "da vivere anche come agricoltori, e alcune città industriali ben sviluppate producono beni da esportare su "
     "altri mondi."),
    ("dust masks",
     "Molti abitanti indossano maschere antipolvere per evitare che il particolato dei vulcani si accumuli nei "
     "polmoni."),
    ("massive new base here on New Iceland",
     "Dopo la sconfitta nel sud, la Marina ha iniziato a impiantare qui su New Iceland una nuova enorme base, per "
     "poter mantenere una presenza forte in questo settore."),
    ("outer ring being erected",
     "A nord dello spazioporto si trova il Memoriale di Guerra dei Mondi Liberi, una serie di pareti di granito "
     "incise con i nomi dei caduti. Il sito si è ampliato rispetto alla sua dimensione originale, con un anello "
     "esterno in costruzione per ospitare altre cinquanta pareti di nomi."),
    ("prison colony",
     "Di recente i Mondi Liberi hanno trasformato Clink in una colonia penale per gli ufficiali della Marina e il "
     "personale di supporto catturati nella battaglia per il sistema Rastaban."),
    ("locals here welcome you",
     "Lo spazioporto è un guazzabuglio di piccole strutture metalliche, costruite con i resti delle navi della "
     "Marina e dei pirati che si sono contese questo mondo. La gente del posto ti accoglie sul suo pianeta con "
     "calore."),
    ("photographs from after the war",
     "La taverna al centro del porto si chiama The Parting Glass. Le pareti sono coperte di fotografie del "
     "dopoguerra, scattate tutte qui su Poisonwood: schiavi liberati che salgono sulle navi della Marina per "
     "lasciare il pianeta che ha dato loro tanto dolore; ufficiali della Marina che sbarcano per ritirarsi sul "
     "mondo che hanno liberato; amici andati via; amici rimasti. Ci sono anche foto più recenti: un Cruiser e due "
     "Falcon, fianco a fianco; truppe corazzate che si allontanano da una fabbrica; un capitano che ti è familiare "
     "mentre parla con un uomo che conosci come il comandante Nguyen. È una sensazione strana vedersi tra gli eroi "
     "di una storia su cui hai avuto solo un effetto minimo."),
    ("but not to you",
     "Lo spazioporto è un guazzabuglio di piccole strutture metalliche, costruite con i resti delle navi della "
     "Marina e dei pirati che si sono contese questo mondo. La gente del posto è insolitamente cortese e amichevole "
     "con la maggior parte dei capitani che atterrano qui, ma non con te."),
    ("rattling of the air conditioner",
     "La taverna al centro del porto si chiama The Parting Glass. Entrando, noti che il locale diventa sempre più "
     "silenzioso, finché tutto ciò che senti è il ronzio del condizionatore e il tintinnio dei bicchieri. Allo "
     "stesso tempo, senti il calore di diverse decine di sguardi puntati su di te. Decidi che è meglio andartene "
     "prima che la situazione peggiori."),
    ("nearly uninhabited",
     "Bloodsea è quasi disabitato, a parte pochi piccoli avamposti. Il nome viene dagli oceani del pianeta, che "
     "sono rosso sangue a causa delle alghe rodofite. Sebbene il clima sia temperato e ci siano molte spiagge di "
     "sabbia bianca, nessuno viene qui sperando di fare il bagno."),
    ("saw the writing on the wall",
     "Fino a poco tempo fa questo era un mondo pirata, ma mentre i Mondi Liberi continuavano a espandersi hanno "
     "capito come stavano le cose e hanno deciso di diventare un mondo civilizzato. I Mondi Liberi stanno "
     "costruendo qui un nuovo spazioporto, ma ci vorranno mesi, e nel frattempo si usa ancora quello vecchio."),
    ("new spaceport was completed here",
     "Di recente, con l'aiuto dei Mondi Liberi, qui è stato completato un nuovo spazioporto. Bloodsea era un mondo "
     "pirata, ma il nuovo spazioporto gli ha dato un'aria di rispettabilità, e già un piccolo numero di coloni e "
     "turisti curiosi ha iniziato ad arrivare."),
    ("impressively well designed",
     "Il nuovo spazioporto è sorprendentemente ben progettato, con frangiflutti e piazzole di cemento fresco, "
     "ancora senza segni del tempo o muffa. È anche diverse volte più grande del necessario per il numero di "
     "persone e navi che ci sono, e a parte un mercato vivace sembra stranamente vuoto."),
    ("meat patty",
     "Alcune cose restano immutate dai tempi dei pirati. Il gergo locale incorpora minacce di violenza estrema come "
     "un tic verbale apparentemente privo di significato. \"Ehi, ti taglierò le dita una per una finché non compri "
     "una polpetta!\" grida allegro un venditore mentre passi. \"La prima è gratis, e ti faccio un nodo alla spina "
     "dorsale se non ti piace.\""),
    ("dominated by the Free Worlds militia",
     "Fino a poco tempo fa questo era un mondo pirata, ma ora è ufficialmente \"indipendente\", avendo rinunciato a "
     "sostenere la pirateria e altre attività criminali dopo essere stato dominato dalla milizia dei Mondi Liberi. "
     "Hai la sensazione che la maggior parte della gente del posto non ami molto i Mondi Liberi, però."),
    ("cold ocean world",
     "Albatross è un mondo oceanico freddo che orbita attorno a un sole piccolo e freddo. I primi coloni di "
     "Albatross furono anarchici convinti che, in una società libera da leggi e costrizioni innaturali, tutti "
     "avrebbero lavorato felicemente e liberamente per il bene comune. I coloni successivi furono pirati convinti "
     "che un pianeta libero da leggi e costrizioni sarebbe stata un'ottima base operativa."),
    ("liberated Albatross",
     "Di recente i Mondi Liberi hanno liberato Albatross dai loro oppressori pirati, ma molti abitanti restano "
     "scettici, vedendo nei Mondi Liberi poco di diverso dalle altre organizzazioni che vendevano protezione e che "
     "li avevano dominati."),
    ("only nominally under the control",
     "Covert ospita un potente cartello minerario, solo nominalmente sotto il controllo della legge della "
     "Repubblica. Si dice che sia uno dei pochi pianeti dello spazio umano dove si estraggono e arricchiscono "
     "uranio e plutonio a livello militare. Qualsiasi merce in vendita qui è probabilmente prodotta da lavoro "
     "schiavo, spesso da sopravvissuti di navi catturate dai pirati. Una flotta pirata si aggira ai margini dello "
     "spazioporto, come avvertimento a qualsiasi pilota privato che pensi di imbrogliare o di opporsi al cartello."),
    ("outside the control of Republic law",
     "Covert ospita un potente cartello minerario, che opera fuori dal controllo della legge della Repubblica e di "
     "qualsiasi altra autorità esterna. Si dice che sia uno dei pochi pianeti dello spazio umano dove si estraggono "
     "e arricchiscono uranio e plutonio a livello militare. Qualsiasi merce in vendita qui è probabilmente prodotta "
     "da lavoro schiavo, spesso da sopravvissuti di navi catturate dai pirati. Una flotta pirata enorme è "
     "attraccata ai margini dello spazioporto, come avvertimento a qualsiasi pilota privato che pensi di imbrogliare "
     "o di opporsi al cartello."),
    ("abandoned prematurely",
     "La Marina aveva iniziato a costruire una grande base militare su New Iceland dopo essere stata respinta dal "
     "Bordo Meridionale, ma la sua sconfitta in questo sistema per mano dei Mondi Liberi ha fatto sì che la base "
     "venisse abbandonata prematuramente."),
    ("sapphires found in New Austria",
     "I pochi insediamenti costruiti qui sono nati per l'estrazione di zaffiri e rubini. Gli zaffiri trovati a New "
     "Austria vanno dal blu al giallo, al nero e al trasparente, e servono sia come abrasivi industriali sia per "
     "gioielleria."),
    ("much higher prices than sapphires",
     "Per secoli gli abitanti hanno cercato un giacimento di diamanti, che si venderebbe a prezzi molto più alti "
     "degli zaffiri, e il folclore locale ruota attorno alla prosperità che verrebbe a questo mondo se i diamanti "
     "venissero trovati."),
    ("\"Checkmate\" plan",
     "La Marina aveva un tempo una base militare qui, ma l'ha lasciata quando i Mondi Liberi hanno conquistato "
     "questo sistema nell'ambito del piano \"Checkmate\"."),
    ("not the most hospitable",
     "Geminus, sebbene non sia tra i mondi più ospitali, è un pianeta abbastanza giovane perché grandi riserve di "
     "ferro, titanio e altri metalli siano facilmente accessibili vicino alla superficie. L'attività vulcanica "
     "costante lascia il pianeta perennemente avvolto in una foschia crepuscolare di cenere e nebbia."),
    ("rusting away",
     "I resti frantumati del vecchio Arsenale giacciono ancora abbandonati e si arrugginiscono lentamente "
     "nell'atmosfera caustica del pianeta, ma la Repubblica ha ora costruito un nuovo cantiere navale per "
     "sostituire quello distrutto nell'attentato, e Geminus è tornata a essere un centro di tecnologia e "
     "industria."),
    ("electric carts",
     "Come tutto il resto su Geminus, lo spazioporto non è particolarmente bello, ma è funzionale ed efficiente. "
     "Ciascuno degli ampi corridoi è segnalato come una strada, con spazio al centro per i carrelli elettrici che "
     "trasportano merci, mentre i pedoni sono relegati ai bordi. Telecamere e sensori sono stati collocati a ogni "
     "incrocio, e l'accesso agli impianti di costruzione navale è strettamente controllato."),
    ("plate glass windows",
     "Il cuore dello spazioporto è un'area ristorazione con un anello di negozi al centro e i posti a sedere "
     "all'esterno, dove puoi guardare attraverso le vetrate i campi di lava e il cratere fuori. Di notte vedi il "
     "bagliore vulcanico tutto intorno all'orizzonte."),
    ("Martini is a world of exotic beaches",
     "Martini è un mondo di spiagge esotiche e clima perfetto. Qui avevano sede la banca centrale della Repubblica e "
     "la borsa galattica, prima che un attacco terroristico le distruggesse insieme a gran parte della vecchia "
     "capitale."),
    ("will-do",
     "La nuova capitale è dall'altra parte del continente principale, dove le radiazioni residue non influiranno sul "
     "resto della popolazione. Non è così imponente come la vecchia capitale, ma la sua popolazione è cresciuta con "
     "il trasferimento dalle zone irradiate e sta rapidamente assumendo l'aria di una grande metropoli. Gli "
     "abitanti, molti dei quali sono sopravvissuti all'esplosione, si sono compattati attorno a un atteggiamento di "
     "'si può fare' che si vede solo dopo un evento così devastante e distruttivo."),
    ("newly-designated planetary spaceport",
     "Al momento il nuovo spazioporto planetario designato non ha l'infrastruttura per fungere da spazioporto "
     "principale di Martini. Si usa ancora l'ampio spazioporto temporaneo dell'operazione di soccorso, e da allora "
     "sono state costruite piazzole permanenti, ma ora ci sono piani per demolirlo e dare al nuovo spazioporto "
     "planetario un ampliamento di cui ha disperato bisogno."),
    ("deflector shields",
     "Il vecchio spazioporto di Martini esiste ancora, perché si trovava appena fuori dalla zona dell'esplosione e i "
     "suoi scudi deflettori hanno assorbito gran parte dell'onda d'urto, ma le sue torri sono parzialmente crollate "
     "nei giorni successivi alla devastazione. Ora, da lontano, appare come alcune guglie nere di altezza diseguale "
     "che si alzano davanti a uno sfondo di fumo e resti di una città in rovina, non più scintillante come un "
     "tempo."),
]

db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ST = {u['idx']: db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] for u in SRC}
assert set(ST.values()) == {'PENDING'}, {k: v for k, v in ST.items() if v != 'PENDING'}

assert collections.Counter(u['kind'] for u in SRC) == {'DESCRIPTION': 41, 'MISSION_TEXT': 1}
assert sum(1 for u in SRC if u['english'].startswith('\t')) == 21
assert sum(u['english'].count('"') for u in SRC) == 8
ctx = collections.Counter(u['context'] for u in SRC)
assert len(ctx) == 18 and collections.Counter(ctx.values()) == {2: 8, 1: 4, 4: 4, 3: 2}, ctx
assert collections.Counter(t for u in SRC for t in TAGS.findall(u['english'])) == {}   # zero token, asserito

distinct = list(dict.fromkeys(ENG.values()))
assert len(distinct) == 36, len(distinct)
reused = [e for e in distinct if e in PREV]
assert len(reused) == 3, len(reused)
assert len([e for e in distinct if e not in PREV]) == 33
assert len(UNIQ) == 33, len(UNIQ)


def resolve(eng):
    if eng in PREV:
        return PREV[eng]
    hits = [t for s, t in UNIQ if s in eng]
    assert len(hits) == 1, (len(hits), eng[:90], hits)
    return hits[0]


cover = {e: resolve(e) for e in distinct}
assert len(set(cover.values())) == 36, 'due testi distinti con la stessa resa'

T = {}
for u in SRC:
    eng = u['english']
    T[u['idx']] = '\t' * (len(eng) - len(eng.lstrip('\t'))) + cover[eng].lstrip('\t')

for idx, txt in T.items():
    eng, kind = ENG[idx], KIND[idx]
    assert txt.count('\t') == eng.count('\t'), idx
    assert txt.count('"') == eng.count('"'), (idx, eng.count('"'), txt.count('"'))
    assert TAGS.findall(txt) == TAGS.findall(eng) == [], idx
    assert not re.search(r'[\[\]`\u2019\u2014\u2013\u2026]', txt), idx
    assert not re.search(r"\b(e|piu|perche|cosi|gia|puo|cioe|percio|fa)'", txt), idx
    assert txt.strip() and txt.strip() != eng.strip(), idx
    r = len(txt) / len(eng)
    assert 0.55 < r < 1.90, ('gate', idx, round(r, 3), eng[:60])

for n, (lo, hi) in enumerate(((1, 14), (15, 28), (29, 42))):
    d = {str(k): T[k] for k in range(lo, hi + 1)}
    with open(os.path.join(PARTS, 'part%02d.json' % (n + 1)), 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
print('42 unita (14x3) · 36 testi distinti (3 da L120/L121, 33 nuovi) · 21 tab · 8 virgolette · 0 token')
