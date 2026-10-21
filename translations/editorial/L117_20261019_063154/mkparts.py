"""mkparts.py — L117: costruisce `parts/part01-03.json` (98 unita', righe 20-1624).

Il blocco e' **fatto di stampi**: 98 unita' ma solo **26 testi distinti** (un nome di missione, una
descrizione e un messaggio di fallimento per ogni lavoro, con le varianti "bulk", "stealth", "wanted" e
"highly wanted"). Per garantire che **lo stesso inglese dia lo stesso italiano** le rese si scrivono **una
volta sola**, in `UNIQ`, e si assegnano per firma: ogni firma deve combaciare con **un solo** testo distinto e
tutti i 26 testi distinti devono essere coperti.

Premesse misurate e asserite:
- **98 unita'**, tutte `PENDING`; tipi `{'VALUE': 31, 'DESCRIPTION': 31, 'MISSION_TEXT': 31, 'DIALOG': 5}`;
- **31 contesti** (26 con tre unita', 5 con quattro): ogni contesto e' una **missione**;
- **zero tab**, **zero quadre**, **zero backtick**, **2 virgolette** (solo l'unita' 81, l'urlo del criminale);
- **108 token** in sei famiglie: `<payment>` 36, `<planet>` 31, `<cargo>` 31, `<destination>` 31,
  `<passengers>` 4, `<bunks>` 3 — parita' per simbolo **e** per unita';
- **26 testi distinti** per **98 unita'**: la ripetizione e' del sorgente e la resa ripete.
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
CTX = {u['idx']: u['context'] for u in SRC}
TAGS = re.compile(r'<[^<>]+>')

# (firma univoca nell'inglese, resa italiana) — l'ordine e' quello di prima comparsa nel file
UNIQ = [
    ("Smuggling to <planet>",
     "Contrabbando verso <planet>"),
    ("Smuggle <cargo> to <destination>",
     "Porta <cargo> di contrabbando su <destination> senza farti scansionare o cogliere dalle forze "
     "dell'ordine planetarie. Il compenso è <payment>."),
    ("In addition to the fine",
     "Oltre alla multa, il tuo carico illegale viene confiscato. I pirati non saranno felici di saperlo."),
    ("Drug run to <planet>",
     "Trasporto di droga verso <planet>"),
    ("Run <cargo> to <destination> without being scanned",
     "Porta <cargo> su <destination> senza farti scansionare o cogliere dalle forze dell'ordine planetarie. "
     "Il compenso è <payment>."),
    ("fined 46,000 credits",
     "Porta <cargo> su <destination>. Se le forze dell'ordine ti colgono, riceverai una multa di 46.000 "
     "crediti. Il compenso è <payment>."),
    ("Bulk smuggling to <planet>",
     "Contrabbando di grosse partite verso <planet>"),
    ("Bulk drug run to <planet>",
     "Grosse partite di droga verso <planet>"),
    ("Highly illegal cargo to <planet>",
     "Carico altamente illegale verso <planet>"),
    ("the consequences may be severe. Payment is",
     "Porta <cargo> su <destination>. Se vieni scansionato o colto dalle forze dell'ordine planetarie, le "
     "conseguenze possono essere gravi. Il compenso è <payment>."),
    ("You will need to land away from the spaceport",
     "Porta <cargo> su <destination>. Se vieni scansionato o colto dalle forze dell'ordine planetarie, le "
     "conseguenze possono essere gravi. Dovrai atterrare lontano dallo spazioporto, altrimenti potresti essere "
     "colto sul fatto. Il compenso è <payment>."),
    ("Highly illegal drugs to <planet>",
     "Droga altamente illegale verso <planet>"),
    ("Wanted individual to <planet>",
     "Ricercato da portare su <planet>"),
    ("This wanted individual wishes",
     "Questo ricercato vuole raggiungere <destination> senza farsi cogliere dalle forze dell'ordine locali. "
     "Vuole anche portare con sé <cargo>. Il compenso è <payment>."),
    ("clutching their battle trophies",
     "Quando scansionano la tua nave, le forze dell'ordine notano il criminale che hai a bordo. Entrati nella "
     "nave per fermarlo, lo trovano nell'angolo di una delle stanze, che stringe i suoi trofei di battaglia e "
     "urla \"non me li porterete mai via!\" Dopo un breve confronto lo portano fuori e ti lasciano con una multa "
     "modesta. Questo non aiuta a costruirti la reputazione di trasportatore affidabile che non fa domande."),
    ("Your <passengers> insists that",
     "Il tuo <passengers> insiste perché tu atterri ai margini dello spazioporto, per non farsi vedere. Dopo "
     "l'atterraggio ti paga <payment>, poi raccoglie in fretta le sue cose e scende dalla nave."),
    ("Wanted individuals to <planet>",
     "Ricercati da portare su <planet>"),
    ("These <bunks> wanted individuals",
     "Questi <bunks> ricercati vogliono raggiungere <destination> senza farsi cogliere dalle forze dell'ordine "
     "locali. Vogliono anche portare con sé <cargo>. Il compenso è <payment>."),
    ("scooping their credits into the airlock",
     "Quando scansionano la tua nave, le forze dell'ordine notano i criminali che hai a bordo. Entrati nella "
     "nave per fermarli, li trovano indaffarati a infilare i loro crediti nel portello d'ancoraggio, sperando "
     "che nessuno possa averli. Gli agenti li fermano in fretta e li portano via insieme al resto dei crediti, "
     "lasciandoti con una multa di media entità. Questo non aiuta a costruirti la reputazione di trasportatore "
     "affidabile che non fa domande."),
    ("Your <passengers> insist that",
     "I tuoi <passengers> insistono perché tu atterri ai margini dello spazioporto, per non farsi vedere. Dopo "
     "l'atterraggio ti pagano <payment>, poi raccolgono in fretta le loro cose e scendono dalla nave."),
    ("firing down the hallways",
     "Quando scansionano la tua nave, le forze dell'ordine notano i criminali che hai a bordo. Entrati nella "
     "nave per fermarli, i criminali cominciano a sparare nei corridoi con le loro armi personalizzate. "
     "Investiti subito dal gas lacrimogeno, non opposero molta resistenza. Gli agenti li portano fuori e ti "
     "lasciano con una multa moderata e qualche segno di laser nei corridoi della nave. Questo non aiuta a "
     "costruirti la reputazione di trasportatore affidabile che non fa domande."),
    ("passed out in their bunks rooms",
     "Quando scansionano la tua nave, le forze dell'ordine notano i criminali che hai a bordo. Entrati nella "
     "nave per fermarli, li trovano tutti svenuti nelle loro cuccette, dopo aver bevuto troppo vino di quello "
     "che avevano portato con sé. Dopo averli portati fuori, ti danno una multa moderata e se ne vanno. Questo "
     "non aiuta a costruirti la reputazione di trasportatore affidabile che non fa domande."),
    ("Galactic criminal to <planet>",
     "Criminale galattico da portare su <planet>"),
    ("wanted by every law enforcement agency",
     "Questo criminale è ricercato da ogni agenzia di polizia della galassia e ha bisogno di un trasporto "
     "sicuro fino a <destination> con il suo <cargo>. Il compenso è alto, ben <payment>, ma trasportare una "
     "persona del genere potrebbe causare molti guai."),
    ("suited head to toe in armor",
     "Le forze dell'ordine si riversano sulla tua nave attraverso i portelli d'ancoraggio, coperti di armatura "
     "dalla testa ai piedi e armati fino ai denti. Il tuo passeggero è costretto ad arrendersi e viene portato "
     "via in manette. Gli agenti valutano di fermare anche te, ma alla fine decidono di ridurre le scartoffie "
     "limitandosi a multarti. Questo non aiuta a costruirti la reputazione di trasportatore affidabile che non "
     "fa domande."),
    ("outside of the main city",
     "Atterri fuori dalla città principale per evitare che il tuo passeggero venga visto. Dopo averti pagato "
     "<payment>, raccoglie le sue cose e scende dalla nave."),
]

db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
STATES = {u['idx']: db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] for u in SRC}
assert set(STATES.values()) == {'PENDING'}, {k: v for k, v in STATES.items() if v != 'PENDING'}
assert len(UNIQ) == 26, len(UNIQ)
assert len({s for s, _ in UNIQ}) == 26

distinct = list(dict.fromkeys(u['english'] for u in SRC))
assert len(distinct) == 26, len(distinct)


def resolve(eng):
    hits = [t for s, t in UNIQ if s in eng]
    assert len(hits) == 1, (len(hits), eng[:80], hits)
    return hits[0]


cover = {eng: resolve(eng) for eng in distinct}
assert len({cover[e] for e in distinct}) == 26, 'due inglesi distinti con la stessa resa'
T = {u['idx']: cover[u['english']] for u in SRC}

# --- premesse strutturali ------------------------------------------------------------------
assert sum(1 for u in SRC if '\t' in u['english']) == 0
assert sum(u['english'].count('`') for u in SRC) == 0
assert sum(u['english'].count('"') for u in SRC) == 2
assert collections.Counter(u['kind'] for u in SRC) == {'VALUE': 31, 'DESCRIPTION': 31,
                                                       'MISSION_TEXT': 31, 'DIALOG': 5}
assert collections.Counter(u['context'] for u in SRC).__len__() == 31
assert collections.Counter(collections.Counter(u['context'] for u in SRC).values()) == {3: 26, 4: 5}
tok = collections.Counter(t for u in SRC for t in TAGS.findall(u['english']))
assert tok == {'<payment>': 36, '<planet>': 31, '<cargo>': 31, '<destination>': 31,
               '<passengers>': 4, '<bunks>': 3}, tok

# --- asserzioni per unita' ----------------------------------------------------------------
for idx, txt in T.items():
    eng = ENG[idx]
    assert '\t' not in txt, idx
    assert txt.count('"') == eng.count('"'), (idx, txt.count('"'), eng.count('"'))
    assert TAGS.findall(txt) == TAGS.findall(eng), (idx, TAGS.findall(txt), TAGS.findall(eng))
    assert '[' not in txt and ']' not in txt and '`' not in txt, idx
    assert txt.strip() and txt.strip() != eng.strip(), idx
    r = len(txt) / len(eng)
    assert 0.55 < r < 1.90, ('gate', idx, round(r, 3), eng[:50], txt[:50])

# --- parti canoniche ----------------------------------------------------------------------
for n, (lo, hi) in enumerate(((1, 33), (34, 66), (67, 98))):
    d = {str(k): T[k] for k in range(lo, hi + 1)}
    with open(os.path.join(PARTS, 'part%02d.json' % (n + 1)), 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
print('98 unita (33+33+32) · 26 testi distinti · 31 contesti · 2 virgolette · 108 token in 6 famiglie')
