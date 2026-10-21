"""mkparts.py — L137: `data/starts.txt`, righe 172-214 (17 unita'). Terzo inizio: `Escaping Squalor`.

Le unita' **5-9 sono le stesse di L135 e L136** (la storia del mondo): si **rileggono** dal `translation.json` di L135
dopo aver verificato che l'inglese coincida.

Misure: **2 contesti completi**, **1 `VALUE`**, **zero token**, **12 virgolette** (6:2 condivisa, 11:2, 13:2, 14:4,
17:2), **8 unita' con tab**, **17 testi distinti** dentro il lotto (12 propri + 5 riletti).

Numeri: 600.000 / 0,5% / 3.580 / 706.571 / 480.000 (convenzione italiana, valore intatto). `Syndicated Systems` resta
il nome del prodotto. Nessuna forma di cortesia «Lei»: il cassiere dà del lei al giocatore e la resa usa il «tu»
coerente con il resto del progetto, tranne dentro le sue battute, dove il «lei» e' quello che il personaggio usa.
"""
import collections
import json
import os
import re
import sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
PARTS = os.path.join(HERE, 'parts')
PREV = os.path.join(L10N, 'staging/editorial/L135_20261019_131024/translation.json')
SRC = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units']
ENG = {u['idx']: u['english'] for u in SRC}
KEY = {i: e.lstrip('\t') for i, e in ENG.items()}
TAGS = re.compile(r'<[^<>]+>')

prev = {u['english']: u['italian'] for u in json.load(open(PREV, encoding='utf-8'))['units']}
SHARED = (5, 6, 7, 8, 9)

D = {
    1: "Escaping Squalor",
    2: "Sei cresciuto sulla Terra, un mondo sovrappopolato con poche opportunità. Ma hai firmato un contratto per "
       "lavorare al servizio del Sindacato, e loro ti hanno dato un posto dove vivere, da mangiare a sufficienza e un "
       "salario decoroso lontano dalla Terra. Dopo te ne sei andato ad Antipode, un mondo di frontiera economico, ma "
       "hai scoperto che non era molto meglio della Terra. Esasperato, hai usato quel che ti restava per viaggiare "
       "fino a Delve, il pianeta più vicino con un cantiere navale...",
    3: "È un inizio più difficile, con rate giornaliere più alte.",
    4: "Ho comprato una licenza di pilota e una nave, ma ho dovuto accendere un mutuo schiacciante. Un'ultima stoccata "
       "del Sindacato, avida come sempre, prima della mia libertà.",
    10: "Delve non assomiglia a nessun pianeta su cui sia mai stato: l'intero spazioporto è scavato in una colossale "
        "caverna montana, con un lato aperto all'aria. Le travi e gli edifici che formano il porto fanno sembrare "
        "misere le strutture di Antipode, eppure sono lontani dai paesaggi urbani opprimenti della Terra.",
    11: "Consegni gli ultimi crediti al capitano che ti ha portato qui. Prima di andarsene, ti dà qualche consiglio. "
        "\"Un avvertimento: se non hai voglia di morire presto, dopo il decollo punta a nord. A sud di qui non c'è "
        "altro che sistemi disabitati e pirati. Non dureresti a lungo con una nave che puoi permetterti.\" La "
        "ringrazi per il passaggio e per il consiglio, poi vi separate.",
    12: "Prima passi dal cantiere per vedere che cosa hanno. Ti nota un venditore che sbuffa quando ti avvicini, forse "
        "per la trasandatezza dei tuoi vestiti rispetto a quelli intorno a te. Gli chiedi che cosa servirebbe per "
        "comprare una nave qui. Ti accenna alla necessità di una licenza di pilota prima di cominciare il suo "
        "sproloquio sui modelli più economici, ma lo interrompi e dici che ti bastava sapere quello.",
    13: "Per fortuna la banca al momento non è molto affollata. Uno dei cassieri ti misura da capo a piedi mentre "
        "entri. \"Come possiamo aiutarla?\" chiede con una gioia sfrenata. Dici che ti serve un prestito per comprare "
        "un'astronave; 600.000 crediti dovrebbero bastare per la licenza e per la nave. Dopo aver consegnato i dati "
        "del tuo conto Syndicated Systems e aver scansionato l'impronta digitale, il cassiere torna con un foglio di "
        "carta.",
    14: "\"Per tua fortuna, i tassi adesso sono ottimi!\" Dai un'occhiata al foglio: il tasso d'interesse giornaliero "
        "è dello 0,5%, il che significa rate giornaliere di 3.580 crediti per un anno intero. Se non restituisci in "
        "anticipo nessuna parte del prestito, avrai pagato 706.571 crediti di interessi, più dei 600.000 del prestito "
        "stesso. \"Firmi qui.\" Il cassiere sorride.",
    15: "Gli interessi sono tremendi, ma non puoi farci niente. Firmi il tuo nome:",
    16: "Dopo aver lasciato la banca, passi un'ora in fila per richiedere una licenza di pilota. La procedura è "
        "stranamente semplice, e quando è finita ti restano 480.000 crediti. Non riesci a scuoterti di dosso la "
        "sensazione che il Sindacato ti stia di nuovo prendendo in giro.",
    17: "Torni al cantiere, questa volta con un gettone di credito in mano per attirare l'attenzione del venditore. "
        "\"Eccoti di nuovo! Spero che possiamo trovarti il modello perfetto,\" dice. Il cantiere è pieno di navi che "
        "non puoi comprare, ma il venditore trova tre modelli nel tuo budget: un intercettore, un mercantile leggero e "
        "una nave da trasporto. Quale sceglierai determinerà il tuo futuro...",
}

db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ST = {u['idx']: db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] for u in SRC}
assert set(ST.values()) == {'PENDING'}, {k: v for k, v in ST.items() if v != 'PENDING'}

assert collections.Counter(u['kind'] for u in SRC) == {'CONVERSATION': 10, 'LOGBOOK': 4, 'DESCRIPTION': 2, 'VALUE': 1}
assert sum(1 for u in SRC if u['english'].startswith('\t')) == 8
assert sum(u['english'].count('"') for u in SRC) == 12
assert [(u['idx'], u['english'].count('"')) for u in SRC if u['english'].count('"')] == [(6, 2), (11, 2), (13, 2),
                                                                                        (14, 4), (17, 2)]
assert [u['idx'] for u in SRC if u['english'].count('"') % 2] == []
ctx = collections.Counter(u['context'] for u in SRC)
assert list(ctx.items()) == [('start:syndicate', 3), ('conversation:syndicate intro', 14)], list(ctx.items())
assert collections.Counter(t for u in SRC for t in TAGS.findall(u['english'])) == {}
assert [u['idx'] for u in SRC if u['kind'] in ('VALUE', 'UI_LABEL')] == [1]
assert ENG[1] == 'Escaping Squalor'
assert (min(u['line'] for u in SRC), max(u['line'] for u in SRC)) == (172, 210)

for k in SHARED:
    assert KEY[k] in prev, ('condivisa assente da L135', k, KEY[k][:50])
own = {i: D[i] for i in D}
assert sorted(own) == [1, 2, 3, 4, 10, 11, 12, 13, 14, 15, 16, 17], sorted(own)

T = {}
for u in SRC:
    eng = u['english']
    body = prev[KEY[u['idx']]] if u['idx'] in SHARED else own[u['idx']]
    T[u['idx']] = '\t' * (len(eng) - len(eng.lstrip('\t'))) + body.lstrip('\t')

for idx, txt in T.items():
    eng = ENG[idx]
    assert txt.count('\t') == eng.count('\t'), idx
    assert txt.count('"') == eng.count('"'), (idx, eng.count('"'), txt.count('"'))
    assert TAGS.findall(txt) == TAGS.findall(eng) == [], idx
    assert len(txt) - len(txt.rstrip()) == len(eng) - len(eng.rstrip()), ('spazio finale', idx)
    assert not re.search(r'[\[\]`\u2019\u2014\u2013\u2026]', txt), idx
    assert not re.search(r"\b(e|piu|perche|cosi|gia|puo|cioe|percio|fa)'", txt), idx
    if idx == 1:
        assert txt == eng
    else:
        assert txt.strip() and txt.strip() != eng.strip(), idx
    r = len(txt) / len(eng)
    assert 0.55 < r < 1.90, ('gate', idx, round(r, 3), eng[:60])

for k in SHARED:
    assert T[k] == prev[KEY[k]], k

dup = {}
for u in SRC:
    dup.setdefault(KEY[u['idx']], set()).add(T[u['idx']])
assert not [(k, v) for k, v in dup.items() if len(v) > 1]
assert len(dup) == 17, len(dup)

for n, (lo, hi) in enumerate(((1, 6), (7, 12), (13, 17))):
    d = {str(k): T[k] for k in range(lo, hi + 1)}
    with open(os.path.join(PARTS, 'part%02d.json' % (n + 1)), 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
print('17 unita (6+6+5) · 12 testi propri + 5 riletti da L135 · 2 contesti completi')
print('zero token · 8 tab · 12 virgolette (6:2, 11:2, 13:2, 14:4, 17:2) · 1 VALUE identico')
