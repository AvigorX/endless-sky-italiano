"""mkparts.py — L142: `data/hai/unfettered 0 prologue.txt`, righe 139-201 (20 unita'). Chiude `Unfettered Jump Drive 1`.

Un `VALUE` (`More Jump Drives`) e un `DESCRIPTION`, poi la trattativa. Due testi si ripetono:

* **il rifiuto** (unita' 13 e 18), una costante sola: la stessa frase compare in due rami;
* **`(No.)` resta `(No.)`**: in italiano «No» e' la stessa parola. Sta in `ID_OK` con un controllo dedicato, come in
  L132 — un'identita' legittima si **dichiara**, non si esclude dai controlli.

`jump drive` -> **motore di salto**, `hyperdrive` -> **iperpropulsore**, `Anomalocaris` resta.
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

REFUSAL = ("\"Mi dispiace, ma se ti do questo motore di salto perderò la capacità di catturarne altri. Abbi pazienza, "
           "e te ne porterò diversi quando potrò.\"")

D = {
    1: "More Jump Drives",
    2: "Gli Hai Slegati ti hanno promesso ricompense ricche se porti loro altri motori di salto.",
    3: "Gli Slegati hanno chiaramente notato che hai un motore di salto: una grande folla si è radunata attorno alla "
       "tua nave. Vuoi parlare con loro, e magari organizzare la vendita del tuo motore di salto?",
    4: "(No.)",
    5: "(Sì.)",
    6: "Appena ti avvicini alla folla, uno di loro fa un passo avanti e dice: \"Un milione di crediti, e l'amicizia "
       "del vero popolo Hai. Questa è la nostra offerta, per il motore di salto.\"",
    7: "\"Certo, accetto l'accordo.\"",
    8: "\"Potete offrirmi di più?\"",
    9: "\"Come farà la mia nave a partire senza il mio motore di salto?\"",
    10: "\"Possiamo darti un iperpropulsore al suo posto, se necessario,\" dicono, \"e sarai contato come nostro amico, "
        "così non dovrai partire in fretta, né sotto minaccia di violenza.\" Non puoi fare a meno di chiederti se "
        "proveranno a prendere la tua nave con la forza se non accetti l'accordo.",
    11: "\"Oh, e a proposito, non ti sarà più richiesto di tenere la tua Anomalocaris in condizioni di funzionare per "
        "garantirti la nostra amicizia,\" aggiungono.",
    12: "\"Va bene, accetto la vostra generosa offerta.\"",
    13: REFUSAL,
    14: "Ci riflettono un momento, poi dicono: \"Molto bene. La nostra offerta resta valida, ogni volta che sceglierai "
        "di tornare.\" Ti lasciano tornare alla tua nave senza problemi.",
    15: "\"Non sottovalutare il valore della nostra amicizia,\" dicono. \"Presto saremo di nuovo potenti, con molti "
        "mondi fruttuosi sotto il nostro controllo, e quando quel giorno arriverà trarrai grande beneficio "
        "dall'essere nostro alleato.\"",
    16: "\"Va bene, purché mi diate un iperpropulsore al suo posto, vi darò il mio motore di salto.\"",
    17: "\"Potete prendere il motore di salto, ma non ho bisogno di un iperpropulsore in cambio.\"",
    18: REFUSAL,
    19: "Gli ingegneri Slegati rimuovono in fretta e con cura il tuo motore di salto e lo sostituiscono con un normale "
        "iperpropulsore. Speri sinceramente di non stare commettendo un errore dando loro questa nuova tecnologia. "
        "\"Ricorda,\" dice uno di loro mentre ti consegna il pagamento, \"quando avrai altri motori di salto, torna "
        "qui con loro e ti daremo altre ricompense. Fino ad allora, che la fortuna ti assista, amico umano.\"",
    20: "Gli ingegneri Slegati recuperano in fretta il motore di salto. Speri sinceramente di non stare commettendo un "
        "errore dando loro questa nuova tecnologia. \"Ricorda,\" dice uno di loro mentre ti consegna il pagamento, "
        "\"quando avrai altri motori di salto, torna qui con loro e ti daremo altre ricompense. Fino ad allora, che la "
        "fortuna ti assista, amico umano.\"",
}

db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ST = {u['idx']: db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] for u in SRC}
assert set(ST.values()) == {'PENDING'}, {k: v for k, v in ST.items() if v != 'PENDING'}

assert collections.Counter(u['kind'] for u in SRC) == {'MISSION_TEXT': 18, 'VALUE': 1, 'DESCRIPTION': 1}
assert sum(1 for u in SRC if u['english'].startswith('\t')) == 17
assert sum(u['english'].count('"') for u in SRC) == 38
assert [u['idx'] for u in SRC if u['english'].count('"') % 2] == []
assert collections.Counter(u['context'] for u in SRC) == {'mission:Unfettered Jump Drive 1': 20}
assert collections.Counter(t for u in SRC for t in TAGS.findall(u['english'])) == {}
assert [(u['idx'], ENG[u['idx']]) for u in SRC if u['kind'] == 'VALUE'] == [(1, 'More Jump Drives')]
assert [u['idx'] for u in SRC if u['kind'] == 'UI_LABEL'] == []
assert (min(u['line'] for u in SRC), max(u['line'] for u in SRC)) == (139, 201)
assert sorted(D) == list(range(1, 21)), [i for i in range(1, 21) if i not in D]
assert D[13] == D[18] == REFUSAL
assert D[4] == KEY[4] == '(No.)'

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
    elif idx == 4:
        assert txt == eng and txt.lstrip('	') == '(No.)', idx
    else:
        assert txt.strip() and txt.strip() != eng.strip(), idx
    r = len(txt) / len(eng)
    assert 0.55 < r < 1.90, ('gate', idx, round(r, 3), eng[:60])

dup = {}
for u in SRC:
    dup.setdefault(KEY[u['idx']], set()).add(T[u['idx']])
assert not [(k, v) for k, v in dup.items() if len(v) > 1]
assert len(dup) == 19, len(dup)
assert ' '.join(T.values()).count(REFUSAL) == 2

for n, (lo, hi) in enumerate(((1, 7), (8, 14), (15, 20))):
    d = {str(k): T[k] for k in range(lo, hi + 1)}
    with open(os.path.join(PARTS, 'part%02d.json' % (n + 1)), 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
print('20 unita (7+7+6) · 19 testi distinti · 1 VALUE identico · (No.) identico in ID_OK · rifiuto x2')
print('17 tab · 38 virgolette · zero token')
