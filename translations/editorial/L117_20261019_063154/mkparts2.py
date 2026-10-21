"""mkparts2.py — L117, seconda stesura: sostituisce `mkparts.py` (che traduceva i nomi di missione).

Il primo `mkparts.py` mappava **anche i 9 nomi di missione** (`Smuggling to <planet>` → «Contrabbando verso
<planet>») e il `check.py` lo ha bocciato sul controllo «i 31 VALUE sono identici al sorgente»: i nomi di
missione restano in inglese per la decisione 259/L103. Qui i `VALUE` sono **identità** e `UNIQ` contiene solo i
**17 testi prosaici**.

Premesse misurate e asserite:
- **98 unita'**, tutte `PENDING`; tipi `{'VALUE': 31, 'DESCRIPTION': 31, 'MISSION_TEXT': 31, 'DIALOG': 5}`;
- **26 testi distinti** (9 nomi + 17 prosa), **31 contesti** (26 con tre unita', 5 con quattro);
- **zero tab**, **zero quadre**, **zero backtick**, **2 virgolette** (solo l'unita' 81);
- **108 token** in sei famiglie — parita' per simbolo **e** per unita'.
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
    ("Smuggle <cargo> to <destination>",
     "Porta <cargo> di contrabbando su <destination> senza farti scansionare o cogliere dalle forze "
     "dell'ordine planetarie. Il compenso è <payment>."),
    ("In addition to the fine",
     "Oltre alla multa, il tuo carico illegale viene confiscato. I pirati non saranno felici di saperlo."),
    ("Run <cargo> to <destination> without being scanned",
     "Porta <cargo> su <destination> senza farti scansionare o cogliere dalle forze dell'ordine planetarie. "
     "Il compenso è <payment>."),
    ("fined 46,000 credits",
     "Porta <cargo> su <destination>. Se le forze dell'ordine ti colgono, riceverai una multa di 46.000 "
     "crediti. Il compenso è <payment>."),
    ("the consequences may be severe. Payment is",
     "Porta <cargo> su <destination>. Se vieni scansionato o colto dalle forze dell'ordine planetarie, le "
     "conseguenze possono essere gravi. Il compenso è <payment>."),
    ("You will need to land away from the spaceport",
     "Porta <cargo> su <destination>. Se vieni scansionato o colto dalle forze dell'ordine planetarie, le "
     "conseguenze possono essere gravi. Dovrai atterrare lontano dallo spazioporto, altrimenti potresti essere "
     "colto sul fatto. Il compenso è <payment>."),
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
assert len(UNIQ) == 17, len(UNIQ)

names = {u['english'] for u in SRC if u['kind'] == 'VALUE'}
prose = [e for e in dict.fromkeys(u['english'] for u in SRC) if e not in names]
assert len(names) == 9 and len(prose) == 17, (len(names), len(prose))


def resolve(eng):
    hits = [t for s, t in UNIQ if s in eng]
    assert len(hits) == 1, (len(hits), eng[:80], hits)
    return hits[0]


cover = {e: resolve(e) for e in prose}
assert len(set(cover.values())) == 17, 'due inglesi distinti con la stessa resa'
T = {u['idx']: (u['english'] if u['kind'] == 'VALUE' else cover[u['english']]) for u in SRC}

assert sum(1 for u in SRC if '\t' in u['english']) == 0
assert sum(u['english'].count('`') for u in SRC) == 0
assert sum(u['english'].count('"') for u in SRC) == 2
assert collections.Counter(u['kind'] for u in SRC) == {'VALUE': 31, 'DESCRIPTION': 31,
                                                       'MISSION_TEXT': 31, 'DIALOG': 5}
ctx = collections.Counter(u['context'] for u in SRC)
assert len(ctx) == 31 and collections.Counter(ctx.values()) == {3: 26, 4: 5}
tok = collections.Counter(t for u in SRC for t in TAGS.findall(u['english']))
assert tok == {'<payment>': 36, '<planet>': 31, '<cargo>': 31, '<destination>': 31,
               '<passengers>': 4, '<bunks>': 3}, tok

for idx, txt in T.items():
    eng = ENG[idx]
    assert '\t' not in txt, idx
    assert txt.count('"') == eng.count('"'), (idx, txt.count('"'), eng.count('"'))
    assert TAGS.findall(txt) == TAGS.findall(eng), (idx, TAGS.findall(txt), TAGS.findall(eng))
    assert '[' not in txt and ']' not in txt and '`' not in txt, idx
    if KIND[idx] == 'VALUE':
        assert txt == eng, idx                      # nomi di missione invariati per decisione
    else:
        assert txt.strip() and txt.strip() != eng.strip(), idx
    r = len(txt) / len(eng)
    assert 0.55 < r < 1.90, ('gate', idx, round(r, 3), eng[:50], txt[:50])

for n, (lo, hi) in enumerate(((1, 33), (34, 66), (67, 98))):
    d = {str(k): T[k] for k in range(lo, hi + 1)}
    with open(os.path.join(PARTS, 'part%02d.json' % (n + 1)), 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
print('98 unita (33+33+32) · 31 VALUE identici · 17 testi prosaici · 31 contesti · 108 token in 6 famiglie')
