"""mkparts.py — L140: `data/hai/unfettered 0 prologue.txt`, righe 22-81 (25 unita').

Primo lotto di un file nuovo: `mission:First Contact: Unfettered`, il primo contatto con gli **Hai Slegati**. Tutte e
25 le unita' sono `MISSION_TEXT`.

**Quattro frasi ripetute** (le scelte `(Certo.)` e `(Non ora, è troppo rischioso.)`, la domanda sui «veri Hai» e la
battuta «Combattiamo per difenderci dall'estinzione») rese con costanti, cosi' che i due rami dicano le stesse parole.

Il **motto** degli Slegati — «Eravamo padroni di cento mondi quando le scimmie umane non avevano ancora imparato a
usare i pollici.» — compare **cinque volte** in quattro unita' diverse (15, 16, 17, 20, 23, di cui 20 e 23 in coda a
frasi diverse): una costante sola, verificata per occorrenza.

`monkey` -> **scimmia**, come nel resto dello staging. L'«Although despite» del sorgente (un doppio connettivo
sgrammaticato) si riproduce come «Sebbene, nonostante...», senza ripulirlo.
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

SURE = "(Certo.)"
RISKY = "(Non ora, è troppo rischioso.)"
WHAT = "\"Che cosa intendi con 'veri Hai'?\""
FIGHT = "\"Combattiamo per difenderci dall'estinzione,\" dicono."
MOTTO = ("Eravamo padroni di cento mondi quando le scimmie umane non avevano ancora imparato a usare i pollici.")

D = {
    1: "Questo pianeta è popolato da una specie aliena ostile che somiglia a scoiattoli giganti e intelligenti. "
       "Sebbene, nonostante la loro ostilità in orbita, in superficie non ti badano quasi. Vuoi avvicinarti a uno di "
       "loro?",
    2: SURE,
    3: RISKY,
    4: "Incontri lo sguardo di uno degli alieni che lavorano alla banchina e lui si avvicina. \"Ah,\" dice, \"la "
       "scimmia è curiosa. La scimmia non è mai stata faccia a faccia con un vero Hai?\"",
    5: "\"Hai? È così che vi chiamate?\"",
    6: WHAT,
    7: "\"Perché mi avete sparato? Siete in guerra?\"",
    8: "Gli Hai qui sembrano in guerra con il resto della loro specie. Vuoi avvicinarti a uno di loro e chiedere "
       "perché?",
    9: SURE,
    10: RISKY,
    11: "Uno degli Hai che lavorano alla banchina incrocia il tuo sguardo e si avvicina. \"Ah,\" dice, \"la scimmia è "
        "curiosa. La scimmia non è mai stata faccia a faccia con un vero Hai?\"",
    12: "\"No, ho incontrato molti dei tuoi simili a sud di qui.\"",
    13: WHAT,
    14: "\"Perché siete in guerra con tutti gli altri?\"",
    15: "Sibila. \"Non sono veri Hai. Noi siamo gli Hai. Gli inalterati. " + MOTTO + "\"",
    16: "\"Significa che siamo inalterati, Hai come gli Hai furono creati all'inizio. Gli Hai conquistatori. " + MOTTO
        + "\"",
    17: "\"Noi siamo gli Hai. Gli Hai conquistatori. " + MOTTO + "\"",
    18: FIGHT,
    19: "\"Estinzione?\" chiedi. \"Vuoi dire che non ci sono altri Hai?\"",
    20: "\"Siamo tutto ciò che resta degli Hai originali,\" dicono. \"Inalterati. I conquistatori. " + MOTTO + "\"",
    21: FIGHT,
    22: "\"Estinzione?\" chiedi. \"Vuoi dire che non siete la stessa specie degli altri Hai?\"",
    23: "\"Esatto,\" dicono. \"Siamo tutto ciò che resta degli Hai originali. Inalterati. I conquistatori. " + MOTTO
        + "\"",
    24: "\"Dov'era il vostro territorio? Perché non ho mai sentito parlare di voi?\"",
    25: "\"Che cosa intendi con 'gli Hai sono stati alterati'?\"",
}

db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ST = {u['idx']: db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] for u in SRC}
assert set(ST.values()) == {'PENDING'}, {k: v for k, v in ST.items() if v != 'PENDING'}

assert collections.Counter(u['kind'] for u in SRC) == {'MISSION_TEXT': 25}, collections.Counter(u['kind'] for u in SRC)
assert sum(1 for u in SRC if u['english'].startswith('\t')) == 23
assert sum(u['english'].count('"') for u in SRC) == 50
assert [u['idx'] for u in SRC if u['english'].count('"') % 2] == []
assert [(u['idx'], u['english'].count('"')) for u in SRC if u['english'].count('"')] == [
    (4, 4), (5, 2), (6, 2), (7, 2), (11, 4), (12, 2), (13, 2), (14, 2), (15, 2), (16, 2), (17, 2), (18, 2),
    (19, 4), (20, 4), (21, 2), (22, 4), (23, 4), (24, 2), (25, 2)]
assert collections.Counter(u['context'] for u in SRC) == {'mission:First Contact: Unfettered': 25}
assert collections.Counter(t for u in SRC for t in TAGS.findall(u['english'])) == {}
assert [u['idx'] for u in SRC if u['kind'] in ('VALUE', 'UI_LABEL')] == []
assert (min(u['line'] for u in SRC), max(u['line'] for u in SRC)) == (22, 81)
assert sorted(D) == list(range(1, 26)), [i for i in range(1, 26) if i not in D]
assert sum(1 for i in (9, 10) if D[i] == D[i - 7]) == 2
assert sum(1 for i in (21,) if D[i] == D[18]) == 1
assert sum(1 for i in (13,) if D[i] == D[6]) == 1

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
    assert txt.strip() and txt.strip() != eng.strip(), idx
    r = len(txt) / len(eng)
    assert 0.55 < r < 1.90, ('gate', idx, round(r, 3), eng[:60])

dup = {}
for u in SRC:
    dup.setdefault(KEY[u['idx']], set()).add(T[u['idx']])
assert not [(k, v) for k, v in dup.items() if len(v) > 1]
assert len(dup) == 21, len(dup)
assert ' '.join(T.values()).count(MOTTO) == 5, ' '.join(T.values()).count(MOTTO)

for n, (lo, hi) in enumerate(((1, 9), (10, 17), (18, 25))):
    d = {str(k): T[k] for k in range(lo, hi + 1)}
    with open(os.path.join(PARTS, 'part%02d.json' % (n + 1)), 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
print('25 unita (9+8+8) · 21 testi distinti (4 coppie ripetute) · 1 contesto · 23 tab · 50 virgolette')
print('il motto degli Slegati compare 5 volte, sempre identico · zero token')
