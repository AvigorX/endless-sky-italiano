"""mkparts.py — L134: la coda di `data/hai/unfettered side missions.txt` (8 unita', righe 494-510). CHIUDE IL FILE.

**1 contesto** (`Undeserved Anomalocaris`), **8 `MISSION_TEXT`**, **zero `VALUE`**, **zero `UI_LABEL`**, **zero
token** — tre asserzioni vuote scritte. **7 unita' con tab**, **13 virgolette**, di cui **una sola nell'unita' 6**
(battuta non chiusa dal sorgente).

`Jump Drive` resta in inglese: e' il nome di un modulo, non una descrizione.
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
    1: "Mentre atterri, innumerevoli Hai si dirigono in fretta verso la tua nave, ognuno armato di diverse armi. Uno "
       "di loro ti punta contro e fa una dichiarazione davanti alla folla che si sta rapidamente formando, gridando "
       "abbastanza forte perché tutti sentano. \"Non meriti di pilotare questo relitto del passato!\"",
    2: "Uno che sta dietro di loro interviene. \"Hai sprecato la tua occasione per una battaglia gloriosa che ti "
       "guadagnasse quel diritto! Sappiamo in cosa hai fallito!\"",
    3: "Un Unfettered dall'aria più importante ti si avvicina, parlando con tono minaccioso. \"Devi consegnarci "
       "immediatamente la nave, insieme alle armi dei selvaggi, se non ce le hai già rubate.\" Per un momento "
       "abbassano lo sguardo pensierosi, poi ti parlano di nuovo. \"Ti daremo un'altra nave così potrai andartene, ma "
       "devi darci l'Anomalocaris!\"",
    4: "(Consegna l'Anomalocaris.)",
    5: "(Rifiuta la richiesta e vattene.)",
    6: "Tu e il tuo equipaggio uscite da quella che per poco è stata la tua nave, e alla milizia locale degli "
       "Unfettered viene comunicato che ora è loro. Gli Unfettered che si stavano radunando attorno alla nave si "
       "disperdono contenti, tranne uno, probabilmente il capo a giudicare dalla quantità di armi che porta "
       "addosso. Viene a parlarti, armi in mano ma abbassate. \"Siamo felici che tu abbia saputo ragionare e abbia "
       "deciso di consegnare la nave. In cambio ti forniremo un sostituto adeguato.",
    7: "\"Quel relitto non era destinato a te, ma ci sono altri modi per dimostrarci il tuo valore.\" Il capo di "
       "questi Unfettered continua con una disinvoltura palesemente forzata. \"Diciamo, per esempio, portarci un "
       "Jump Drive... o due... quello di sicuro ti guadagnerà il favore, e dimostrerà che sai combattere.\"",
    8: "Il capo del gruppo Unfettered fa poi accompagnare te da alcuni di loro fino al bordo dello spazioporto. "
       "Mentre ci vai, alcuni sembrano trattenere una certa frustrazione, e avresti giurato che uno volesse "
       "attaccarti da un momento all'altro. Alla fine ti portano a una Lightning Bug atterrata, e dopo qualche "
       "pratica pasticciata gli Unfettered te la lasciano.",
}

db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ST = {u['idx']: db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] for u in SRC}
assert set(ST.values()) == {'PENDING'}, {k: v for k, v in ST.items() if v != 'PENDING'}

assert collections.Counter(u['kind'] for u in SRC) == {'MISSION_TEXT': 8}
assert sum(1 for u in SRC if u['english'].startswith('\t')) == 7
assert sum(u['english'].count('"') for u in SRC) == 13
ctx = collections.Counter(u['context'] for u in SRC)
assert len(ctx) == 1 and list(ctx.items()) == [('mission:Undeserved Anomalocaris', 8)], list(ctx.items())
assert collections.Counter(t for u in SRC for t in TAGS.findall(u['english'])) == {}
assert [u['idx'] for u in SRC if u['kind'] in ('VALUE', 'UI_LABEL')] == []
assert (min(u['line'] for u in SRC), max(u['line'] for u in SRC)) == (494, 510)

expected = [i for i in ENG]
assert sorted(D) == expected, (len(D), len(expected), [i for i in expected if i not in D])

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
    assert txt.strip() and txt.strip() != eng.strip(), idx
    r = len(txt) / len(eng)
    assert 0.55 < r < 1.90, ('gate', idx, round(r, 3), eng[:60])

dup = {}
for u in SRC:
    dup.setdefault(KEY[u['idx']], set()).add(T[u['idx']])
assert not [(k, v) for k, v in dup.items() if len(v) > 1]
assert len(dup) == 8, len(dup)

for n, (lo, hi) in enumerate(((1, 4), (5, 8))):
    d = {str(k): T[k] for k in range(lo, hi + 1)}
    with open(os.path.join(PARTS, 'part%02d.json' % (n + 1)), 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
print('8 unita (4+4) · 8 testi distinti · 1 contesto · 7 tab · 13 virgolette (una sola nell unita 6)')
print('zero VALUE, zero UI_LABEL, zero token: tre asserzioni vuote scritte')
