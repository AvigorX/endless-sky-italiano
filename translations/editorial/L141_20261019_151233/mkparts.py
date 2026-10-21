"""mkparts.py — L141: `data/hai/unfettered 0 prologue.txt`, righe 83-132 (20 unita'). Chiude la prima missione.

L'unita' **19** (una voce di diario) e' **identica** al testo gia' tradotto in L138 (unita' 16): si **rilegge** dal suo
`translation.json` dopo il confronto dell'inglese. L'unita' **20** e' una **variante** dello stesso fatto (L138 unita'
17) e va resa di nuovo, con lo stesso lessico ma senza copiare la frase.

La voce degli Slegati e' **telegrafica**: articoli saltati, frasi brevi, nessuna cortesia («Silly monkey»). La resa
mantiene il ritmo spezzato invece di «normalizzarlo» in italiano fluido.

`jump drive` -> **motore di salto** (eccezione deliberata del glossario); `wormhole` resta **wormhole**, come nei file
gia' chiusi; `Sheragi` e `Drak` restano.
"""
import collections
import json
import os
import re
import sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
PARTS = os.path.join(HERE, 'parts')
PREV = os.path.join(L10N, 'staging/editorial/L138_20261019_142846/translation.json')
SRC = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units']
ENG = {u['idx']: u['english'] for u in SRC}
KEY = {i: e.lstrip('\t') for i, e in ENG.items()}
TAGS = re.compile(r'<[^<>]+>')

prev = {u['english']: u['italian'] for u in json.load(open(PREV, encoding='utf-8'))['units']}
SHARED = (19,)

SURVIVE = "sopravvivono solo i loro antenati ottusi, proprio come le scimmie sopravvivranno agli umani pensanti"

D = {
    1: "\"Questa è la nostra storia,\" dicono. \"Una volta, molti mondi oltre il wormhole erano nostri. Una volta, "
       "centomila anni ormai passati. Avevamo bisogno di più mondi. Una specie che non si espande diventa come acqua "
       "salmastra, come albero rinsecchito. Ma i popoli-drago a sud avevano creato l'iperpropulsore, e le scimmie "
       "umane avevano cominciato a battere le pietre l'una contro l'altra in quello che i Drak dicevano essere un "
       "modo molto intelligente. Così ci è stato vietato di prendere altri mondi.\"",
    2: "\"'Popoli-drago?'\" chiedi. \"Non ne ho mai sentito parlare.\"",
    3: "\"Sheragi,\" dicono, \"sono estinti. " + SURVIVE + ".\"",
    4: "\"'Popoli-drago?'\" chiedi. \"Intendi gli Sheragi?\"",
    5: "\"Notevole,\" rispondono, \"la scimmia conosce gli Sheragi. Siamo sopravvissuti a tutti loro. Divertente che "
       + SURVIVE + ".\"",
    6: "\"Come siete stati alterati?\" chiedi.",
    7: "Dicono: \"Noi Hai abbiamo combattuto gli Sheragi e preso mondi che i Drak dicevano appartenere a loro, mondi "
       "che gli Sheragi non avevano nemmeno ancora scoperto. I Drak hanno reagito. Su tutti i mondi Hai sono apparse "
       "navi Drak in orbita. Una malattia ha attraversato ogni pianeta: febbre rapida, strana sensazione di "
       "fragilità, come essere ossa fragili con la bocca piena di terra. Le vittime restavano vive, ma ogni ambizione "
       "svanita, nessun desiderio se non morire di vecchiaia comoda.\"",
    8: "\"Avete provato a resistere ai Drak?\"",
    9: "\"Come fai a saperlo, se è successo centomila anni fa?\"",
    10: "\"Scimmia sciocca,\" dicono, \"nessuno può resistere. Sono forti. La loro volontà prevale. E la loro volontà è "
        "che la galassia sia uno zoo, piccoli resti di ogni specie ognuno in una gabbia separata. Per ora lasciano "
        "gli umani liberi perché gli umani crescano in conoscenza, ma presto fabbricheranno una gabbia anche per gli "
        "umani.\"",
    11: "\"Tutti gli Hai lo sanno. La storia si tramanda. Gli altri raccontano una versione alterata, in cui la via "
        "della pace fu una scelta e non una ferita inflitta, ma alcuni in ogni generazione apprendono la verità, e si "
        "uniscono a noi qui.\"",
    12: "\"È una storia spaventosa. Grazie per avermi dedicato il tuo tempo.\"",
    13: "\"C'è qualcosa che posso fare per aiutarvi?\"",
    14: "\"Se mai vorrai venderci un motore di salto,\" dicono, \"ti ricompenseremo lautamente. E se scopri il segreto "
        "per costruire i nostri motori di salto e fuggire da questa prigione, portacelo e vivrai come un dio fra "
        "noi.\"",
    15: "\"Mi dispiace, non conosco il segreto del motore di salto. Nessun essere umano lo conosce.\"",
    16: "\"Se mai avrò un motore di salto in più da vendere, te lo porterò.\"",
    17: "\"Allora lasciaci in pace,\" dicono, e se ne vanno.",
    18: "\"Portaci un motore di salto,\" dicono, \"e ti conteremo fra i nostri amici. Portacene altri, e potremmo "
        "persino considerarti degno di una parte del bottino, quando riprenderemo ciò che è nostro.\"",
    20: "Gli Hai Slegati dicono che una specie simile a un drago, chiamata \"Sheragi\" e da tempo estinta, viveva nello "
        "spazio umano, quando gran parte di quello che oggi è territorio umano era occupato dagli Hai.",
}

db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ST = {u['idx']: db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] for u in SRC}
assert set(ST.values()) == {'PENDING'}, {k: v for k, v in ST.items() if v != 'PENDING'}

assert collections.Counter(u['kind'] for u in SRC) == {'MISSION_TEXT': 18, 'LOGBOOK': 2}
assert sum(1 for u in SRC if u['english'].startswith('\t')) == 18
assert sum(u['english'].count('"') for u in SRC) == 58
assert [u['idx'] for u in SRC if u['english'].count('"') % 2] == []
assert [u['idx'] for u in SRC if not u['english'].startswith('\t')] == [19, 20]
assert collections.Counter(u['context'] for u in SRC) == {'mission:First Contact: Unfettered': 20}
assert collections.Counter(t for u in SRC for t in TAGS.findall(u['english'])) == {}
assert [u['idx'] for u in SRC if u['kind'] in ('VALUE', 'UI_LABEL')] == []
assert (min(u['line'] for u in SRC), max(u['line'] for u in SRC)) == (83, 132)
assert KEY[19] in prev, 'la voce di diario identica a L138 non e passata'
own = {i: D[i] for i in D}
assert sorted(own) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20], sorted(own)

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
    assert txt.strip() and txt.strip() != eng.strip(), idx
    r = len(txt) / len(eng)
    assert 0.55 < r < 1.90, ('gate', idx, round(r, 3), eng[:60])

assert T[19] == prev[KEY[19]]
dup = {}
for u in SRC:
    dup.setdefault(KEY[u['idx']], set()).add(T[u['idx']])
assert not [(k, v) for k, v in dup.items() if len(v) > 1]
assert len(dup) == 20, len(dup)
assert 'sopravvivono solo i loro antenati ottusi' in T[3] and 'sopravvivono solo i loro antenati ottusi' in T[5]

for n, (lo, hi) in enumerate(((1, 7), (8, 14), (15, 20))):
    d = {str(k): T[k] for k in range(lo, hi + 1)}
    with open(os.path.join(PARTS, 'part%02d.json' % (n + 1)), 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
print('20 unita (7+7+6) · 19 testi propri + 1 riletto da L138 · 1 contesto che si chiude')
print('18 tab · 58 virgolette · zero token · variante del diario resa senza copiare L138')
