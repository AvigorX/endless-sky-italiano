"""mkparts.py — L143: `data/hai/unfettered 0 prologue.txt`, righe 214-317 (30 unita'). Due missioni intere.

`Unfettered Jump Drive 2` (12 unita') e `Unfettered Jump Drive 3` (18): entrambe si chiudono in questo lotto.

Il `VALUE` **`More Jump Drives` ricompare**, identico a L142: la ricomparsa si verifica, non si presume. Le due scelte
`(No.)` e `(Yes.)` compaiono **due volte ciascuna**: `(No.)` resta identico (in italiano e' la stessa parola) e va in
`ID_OK`; `(Yes.)` si traduce «(Sì.)» e usa una costante, cosi' le due occorrenze dicono la stessa cosa.

`jump drive` -> motore di salto, `hyperdrive` -> iperpropulsore, `job board` -> bacheca dei lavori, `Wanderers` resta.
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

NO = "(No.)"
YES = "(Sì.)"

D = {
    1: "More Jump Drives",
    2: "Gli Hai Slegati ti hanno promesso ricompense ricche, e più informazioni sui loro piani, se porterai loro altri "
       "motori di salto.",
    3: "Come prima, quando atterri su questo mondo Slegato con un motore di salto, una grande folla si raduna attorno "
       "alla tua nave. Chiaramente sperano che anche stavolta organizzi una vendita. Vuoi trattare con loro?",
    4: NO,
    5: YES,
    6: "Quando ti avvicini alla folla, uno di loro dice: \"Salve, amico umano. Ti abbiamo fatto conoscere a tutti i "
       "nostri fratelli e sorelle come una delle poche creature che hanno scelto di aiutare i veri Hai a conquistare "
       "la libertà. Se ci dai un altro motore di salto, ti pagheremo un altro milione di crediti, e ti faremo uno dei "
       "nostri emissari per raccogliere i pagamenti con cui i nostri fragili fratelli cercano di comprare la pace. "
       "Accetti questo scambio?\"",
    7: "\"Mi dispiace, mi serve questo motore di salto adesso, ma tornerò più tardi e te lo venderò.\"",
    8: "\"Sì, vi venderò il mio motore di salto.\"",
    9: "Ancora una volta scambiano il tuo motore di salto con un iperpropulsore, e ti pagano molto più di quanto "
       "potresti venderlo altrove. \"Diremo agli altri veri Hai di offrirti lavoro nelle nostre bacheche,\" ti "
       "dicono, \"e ricorda che ci servono ancora altri motori di salto.\"",
    10: "\"Allora ne troverò altri, e ve li porterò.\"",
    11: "\"Potete dirmi a cosa vi servono?\"",
    12: "\"Non ancora. Se dimostrerai ancora la tua amicizia, forse lo faremo.\" Assicuri loro che continuerai a fare "
        "del tuo meglio per aiutarli.",
    13: "Hai un altro motore di salto, e gli Slegati saranno senz'altro disposti a pagarlo bene. Hanno anche accennato "
        "che potrebbero darti più informazioni su che cosa intendono fare con i motori di salto. Vuoi vendergli un "
        "altro motore?",
    14: NO,
    15: YES,
    16: "Ti incontri con alcuni capi locali degli Slegati, che ti pagano di nuovo un milione di crediti e fanno "
        "scambiare il motore di salto dalla tua nave. \"Se ne porterai altri, continueremo a pagarti,\" dicono.",
    17: "\"Potete dirmi a cosa vi servono i motori di salto?\"",
    18: "\"Grazie, ne porterò senz'altro altri quando potrò.\"",
    19: "Dopo una breve discussione sussurrata nella loro lingua, uno dei capi dice: \"Hai dimostrato il tuo valore, "
        "quindi condivideremo il nostro segreto. Gli Hai possedevano un tempo molti mondi ai margini della galassia, "
        "un territorio che possiamo raggiungere solo con il motore di salto. Quei mondi sono fertili e quasi "
        "disabitati. Li rivendicheremo come nostri, e lì ci sarà cibo per sfamare gli Slegati per molte migliaia di "
        "anni a venire.\"",
    20: "\"C'è un altro modo in cui posso aiutarvi a rivendicare quei mondi?\"",
    21: "\"'Quasi disabitati?' Vuoi dire che un'altra specie abita oggi alcuni di quei mondi?\"",
    22: "Sospetti che stiano parlando del territorio oggi abitato dai Wanderer.",
    23: "\"Siete in guerra con i Wanderer? Posso aiutarvi a rivendicare il vostro territorio?\"",
    24: "\"Che cosa farete alla specie che possiede quei mondi adesso?\"",
    25: "\"Il tuo aiuto potrebbe davvero esserci utile,\" dice il capo. \"Dirò agli altri di contattarti se hanno "
        "missioni particolari che puoi svolgere.\"",
    26: "\"Non vedo l'ora di sentire da loro.\"",
    27: "\"Che cosa pensate di fare alla specie che abita quei mondi adesso?\"",
    28: "\"Quei mondi sono ora tenuti da una specie di sciacalli, che banchettano sulle rovine di civiltà orgogliose. "
        "Le nostre sentinelle ci dicono che questi divoratori di carogne hanno cancellato quasi ogni artefatto Hai, "
        "fondendo le nostre città per ricavarne metallo per le loro navi e le loro fabbriche, e nascondendo le "
        "cicatrici delle nostre guerre sotto foreste appena piantate. Sono una specie antica e forte, ma poco "
        "numerosa, e quei mondi sono nostri di diritto.\"",
    29: "Provi a incalzarli per ottenere altre informazioni, ma non ti dicono nulla di utile, oltre a prometterti che "
        "cercheranno il tuo aiuto quando sarà il momento di rivendicare il loro territorio.",
    30: "\"Se vuoi fornirci altri motori di salto, d'ora in poi visita la bacheca dei lavori,\" dice il capo. \"Avremo "
        "guerrieri pronti a riceverli da te per il solito compenso.\"",
}

db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ST = {u['idx']: db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] for u in SRC}
assert set(ST.values()) == {'PENDING'}, {k: v for k, v in ST.items() if v != 'PENDING'}

assert collections.Counter(u['kind'] for u in SRC) == {'MISSION_TEXT': 28, 'VALUE': 1, 'DESCRIPTION': 1}
assert sum(1 for u in SRC if u['english'].startswith('\t')) == 26
assert sum(u['english'].count('"') for u in SRC) == 46
assert [u['idx'] for u in SRC if u['english'].count('"') % 2] == []
ctx = collections.Counter(u['context'] for u in SRC)
assert list(ctx.items()) == [('mission:Unfettered Jump Drive 2', 12), ('mission:Unfettered Jump Drive 3', 18)], list(ctx.items())
assert collections.Counter(t for u in SRC for t in TAGS.findall(u['english'])) == {}
assert [(u['idx'], ENG[u['idx']]) for u in SRC if u['kind'] == 'VALUE'] == [(1, 'More Jump Drives')]
assert [u['idx'] for u in SRC if u['kind'] == 'UI_LABEL'] == []
assert (min(u['line'] for u in SRC), max(u['line'] for u in SRC)) == (214, 317)
assert sorted(D) == list(range(1, 31)), [i for i in range(1, 31) if i not in D]
assert D[4] == D[14] == NO and D[5] == D[15] == YES
assert KEY[4] == KEY[14] == '(No.)' and KEY[5] == KEY[15] == '(Yes.)'

T = {}
for u in SRC:
    eng = u['english']
    T[u['idx']] = '\t' * (len(eng) - len(eng.lstrip('\t'))) + D[u['idx']].lstrip('\t')

for idx, txt in T.items():
    eng = ENG[idx]
    assert txt.count('\t') == eng.count('\t'), idx
    assert txt.count('"') == eng.count('"'), (idx, eng.count('"'), txt.count('"'))
    assert TAGS.findall(txt) == TAGS.findall(eng) == [], idx
    assert len(txt) - len(txt.rstrip()) == len(eng) - len(eng.rstrip()), ('spazio finale', idx)
    assert not re.search(r'[\[\]`\u2019\u2014\u2013\u2026]', txt), idx
    assert not re.search(r"\b(e|piu|perche|cosi|gia|puo|cioe|percio|fa)'", txt), idx
    if idx == 1:
        assert txt == eng, idx
    elif idx in (4, 14):
        assert txt.lstrip('\t') == '(No.)', idx
    else:
        assert txt.strip() and txt.strip() != eng.strip(), idx
    r = len(txt) / len(eng)
    assert 0.55 < r < 1.90, ('gate', idx, round(r, 3), eng[:60])

dup = {}
for u in SRC:
    dup.setdefault(KEY[u['idx']], set()).add(T[u['idx']])
assert not [(k, v) for k, v in dup.items() if len(v) > 1]
assert len(dup) == 28, len(dup)
assert ' '.join(T.values()).count('(Sì.)') == 2
assert ' '.join(T.values()).count('(No.)') == 2

for n, (lo, hi) in enumerate(((1, 8), (9, 16), (17, 24), (25, 30))):
    d = {str(k): T[k] for k in range(lo, hi + 1)}
    with open(os.path.join(PARTS, 'part%02d.json' % (n + 1)), 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
print('30 unita (8+8+8+6) · 2 contesti · 28 testi distinti · (No.) identico x2 · (Sì.) x2')
print('26 tab · 46 virgolette · 1 VALUE identico · zero token')
